'''
A script to daily fetch arXiv papers based on keywords and update markdown files.
This repository is inspired by the Vincentqyw/cv-arxiv-daily project.

Features:
1. Support custom keywords search
2. Support specified date range search or fetch the latest updated papers

setup: pip install -r requirements.txt
usage: python main.py --config_path config.yaml
'''

import os
import re
import json
import arxiv
import yaml
import logging
import argparse
import datetime

# Set arxiv library log level to WARNING to avoid verbose information
logging.getLogger('arxiv').setLevel(logging.WARNING)

logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

arxiv_url = "http://arxiv.org/"

def load_config(config_file: str) -> dict:
    '''
    Load configuration from YAML file
    @param config_file: input config file path
    @return: a dictionary of configuration parameters
    '''
    # Function to format search filters for arXiv API
    def pretty_filters(**config) -> dict:
        keywords = dict()
        EXCAPE = '\"'
        QUOTA = ''  # NOT USED
        OR = ' OR '  # TODO: implement OR logic properly
        def parse_filters(filters: list):
            ret = ''
            for idx in range(0, len(filters)):
                filter = filters[idx]
                if len(filter.split()) > 1:
                    ret += (EXCAPE + filter + EXCAPE)
                else:
                    ret += (QUOTA + filter + QUOTA)
                if idx != len(filters) - 1:
                    ret += OR
            return ret
        for k, v in config['keywords'].items():
            keywords[k] = parse_filters(v['filters'])
        return keywords

    with open(config_file, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        config['kv'] = pretty_filters(**config)
        logging.info(f'Keywords: {list(config["keywords"].keys())}')
        logging.info(f'Max results per keyword: {config["max_results"]}')
        
        # Load show_abstract configuration
        config['show_abstract'] = config.get('show_abstract', False)
        logging.info(f'Show abstract: {config["show_abstract"]}')

        # Process date range configuration
        date_range_enabled = False
        if 'date_range' in config and config['date_range'].get('enabled', False):
            date_range = config['date_range']
            start_date_str = date_range.get('start_date')
            end_date_str = date_range.get('end_date')

            config['start_date'] = None
            config['end_date'] = None

            if start_date_str:
                try:
                    config['start_date'] = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
                    date_range_enabled = True
                except ValueError:
                    logging.warning(f"Invalid start_date format: {start_date_str}, ignoring")

            if end_date_str:
                try:
                    config['end_date'] = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
                    date_range_enabled = True
                except ValueError:
                    logging.warning(f"Invalid end_date format: {end_date_str}, ignoring")

            if date_range_enabled:
                config['date_range_enabled'] = True
                # Automatically disable cleanup when custom date range is enabled
                if 'cleanup' in config:
                    config['cleanup']['enabled'] = False
                    logging.info("Auto-disabled cleanup due to custom date range")

                date_range_str = f"{start_date_str} to {end_date_str}" if start_date_str and end_date_str else f"from {start_date_str}" if start_date_str else f"until {end_date_str}"
                logging.info(f"Custom date range enabled: {date_range_str}")
            else:
                config['date_range_enabled'] = False
        else:
            config['date_range_enabled'] = False

    return config

def get_authors(authors, last_author=False):
    """
    Get author information
    @param authors: list of authors
    @param last_author: whether to return only the last author
    @return: author string
    """
    if not last_author:
        output = ", ".join(str(author) for author in authors)
    else:
        # Return only the last author
        output = authors[-1] if authors else ""
    return output

def sort_papers(papers):
    """
    Sort papers by date in descending order
    @param papers: dictionary of papers
    @return: sorted dictionary of papers
    """
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output

def get_daily_papers(topic, query="slam", max_results=2, start_date=None, end_date=None, show_abstract=False):
    """
    Fetch papers from arXiv based on search criteria
    @param topic: research topic name
    @param query: search query string
    @param max_results: maximum number of results to fetch
    @param start_date: start date for filtering (datetime.date)
    @param end_date: end date for filtering (datetime.date)
    @param show_abstract: whether to include paper abstracts
    @return: paper data for markdown
    """
    content = dict()

    # Build search query log information
    if start_date or end_date:
        date_range_str = f" from {start_date} to {end_date}" if start_date and end_date else f" from {start_date}" if start_date else f" until {end_date}"
        logging.info(f"Searching arXiv for '{topic}': {query}{date_range_str}")
    else:
        logging.info(f"Searching arXiv for '{topic}': {query}")

    try:
        # Build query string with date range
        full_query = query
        if start_date and end_date:
            # Convert dates to arXiv API required format
            start_str = start_date.strftime("%Y%m%d")
            end_str = end_date.strftime("%Y%m%d")
            full_query = f"({query}) AND submittedDate:[{start_str} TO {end_str}]"
        elif start_date:
            start_str = start_date.strftime("%Y%m%d")
            full_query = f"({query}) AND submittedDate:[{start_str} TO 20301231]"
        elif end_date:
            end_str = end_date.strftime("%Y%m%d")
            full_query = f"({query}) AND submittedDate:[19910101 TO {end_str}]"

        # Use new arxiv API to avoid deprecation warnings
        client = arxiv.Client()
        search = arxiv.Search(
            query=full_query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )

        papers_found = 0

        for result in client.results(search):
            paper_id = result.get_short_id()
            paper_title = result.title
            paper_url = result.entry_id
            paper_authors = get_authors(result.authors)
            paper_last_author = get_authors(result.authors, last_author=True)
            paper_date = result.published.date()  # Use publication date
            categories = result.categories
            comments = result.comment
            abstract = result.summary if show_abstract else ""

            papers_found += 1

            # Extract paper key: eg: 2108.09112v1 -> 2108.09112
            ver_pos = paper_id.find('v')
            if ver_pos == -1:
                paper_key = paper_id
            else:
                paper_key = paper_id[0:ver_pos]
            paper_url = arxiv_url + 'abs/' + paper_key

            # Process category information - join all categories with semicolon
            categories_str = "; ".join(categories) if categories else ""

            # Process comments - show complete comments without truncation
            comments_str = comments if comments else ""

            # Process abstract - show complete abstract without truncation
            abstract_clean = abstract.replace('\n', ' ').strip() if abstract else ""
            abstract_str = abstract_clean

            # Table format: Date, Title, Last Author, Categories, PDF, Comments, [Abstract]
            if show_abstract:
                content[paper_key] = "|**{}**|**{}**|{}|{}|[{}]({})|{}|{}|\n".format(
                    paper_date, paper_title, paper_last_author, categories_str,
                    paper_key, paper_url, comments_str, abstract_str)
            else:
                content[paper_key] = "|**{}**|**{}**|{}|{}|[{}]({})|{}|\n".format(
                    paper_date, paper_title, paper_last_author, categories_str,
                    paper_key, paper_url, comments_str)

        # Clear log output
        if start_date or end_date:
            logging.info(f"✓ Found {papers_found} papers for '{topic}' in specified date range")
        else:
            logging.info(f"✓ Found {papers_found} papers for '{topic}'")

    except Exception as e:
        logging.error(f"✗ Failed to get papers for '{topic}': {e}")
        papers_found = 0

    data = {topic: content}

    return data

def remove_old_keywords(json_data, current_keywords):
    """
    Remove keywords that are no longer used in the configuration
    @param json_data: JSON data
    @param current_keywords: current keywords from configuration
    @return: cleaned JSON data and removed keywords info
    """
    removed_keywords = {}

    # Find keywords that exist in JSON but not in current configuration
    json_keywords = list(json_data.keys())
    current_keyword_names = list(current_keywords.keys())

    keywords_to_remove = [kw for kw in json_keywords if kw not in current_keyword_names]

    for keyword in keywords_to_remove:
        removed_papers_count = len(json_data[keyword])
        removed_keywords[keyword] = removed_papers_count
        del json_data[keyword]
        logging.info(f"  Removed keyword '{keyword}' with {removed_papers_count} papers")

    return json_data, removed_keywords

def update_json_file(filename, data_dict, current_keywords, clear_existing=False):
    '''
    Update JSON file with new paper data
    @param filename: JSON file path
    @param data_dict: dictionary containing new paper data
    @param current_keywords: current keywords from configuration
    @param clear_existing: whether to clear existing content (when using date range)
    @return: tuple of (existing_count, updated_count, new_papers_count, category_updates)
    '''
    # If clear_existing is specified, create an empty dictionary
    if clear_existing:
        m = {}
        existing_count = 0
        logging.info(f"Clearing existing data in {filename} due to custom date range")
    else:
        # Otherwise load existing data normally
        with open(filename, "r") as f:
            content = f.read()
            if not content:
                m = {}
                existing_count = 0
            else:
                m = json.loads(content)
                existing_count = sum(len(papers) for papers in m.values())

    json_data = m.copy()

    # Remove unused keywords (only execute when not clearing)
    if not clear_existing and existing_count > 0:
        json_data, removed_keywords = remove_old_keywords(json_data, current_keywords)
        if removed_keywords:
            total_removed = sum(removed_keywords.values())
            logging.info(f"✓ Removed {len(removed_keywords)} old keywords with {total_removed} papers")

    # Update papers for each keyword
    new_papers_count = 0
    category_updates = {}
    for data in data_dict:
        for keyword in data.keys():
            papers = data[keyword]
            new_papers_count += len(papers)

            if keyword in json_data.keys():
                # If clearing existing content, replace directly instead of updating
                if clear_existing:
                    json_data[keyword] = papers
                    category_updates[keyword] = len(papers)
                else:
                    # Calculate actual number of new papers (deduplicated)
                    before_count = len(json_data[keyword])
                    json_data[keyword].update(papers)
                    after_count = len(json_data[keyword])
                    added_count = after_count - before_count
                    if added_count > 0:
                        category_updates[keyword] = added_count
            else:
                json_data[keyword] = papers
                category_updates[keyword] = len(papers)

    with open(filename, "w") as f:
        json.dump(json_data, f)

    updated_count = sum(len(papers) for papers in json_data.values())
    return existing_count, updated_count, new_papers_count, category_updates

def parse_date_from_content(paper_content):
    """
    Parse date from paper content, supporting multiple formats
    @param paper_content: paper content string
    @return: parsed date or None if cannot parse
    """
    try:
        # Format: Table format "|2022-01-19|Title|..."
        if '|' in paper_content:
            parts = paper_content.split('|')
            if len(parts) >= 3:
                date_str = parts[1].strip().replace('**', '')
                return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

        return None

    except Exception as e:
        return None

def cleanup_old_papers(filename, keep_days):
    """
    Clean up JSON file, keeping only papers from recent keep_days
    @param filename: JSON file path
    @param keep_days: number of days to keep
    @return: tuple of (total_papers_before, total_papers_after)
    """
    if keep_days <= 0:
        return 0, 0

    cutoff_date = datetime.datetime.now().date() - datetime.timedelta(days=keep_days)
    logging.info(f"Cleaning up papers older than {cutoff_date} (keeping {keep_days} days)")

    with open(filename, "r") as f:
        content = f.read()
        if not content:
            logging.info("Empty file, nothing to clean")
            return 0, 0
        data = json.loads(content)

    total_papers_before = sum(len(papers) for papers in data.values())
    logging.info(f"Papers before cleanup: {total_papers_before}")

    papers_removed = 0
    papers_kept = 0

    for category, papers in data.items():
        papers_to_keep = {}
        for paper_id, paper_content in papers.items():
            paper_date = parse_date_from_content(paper_content)

            if paper_date is None or paper_date >= cutoff_date:
                papers_to_keep[paper_id] = paper_content
                papers_kept += 1
            else:
                papers_removed += 1

        data[category] = papers_to_keep

    # Write back to file
    with open(filename, "w") as f:
        json.dump(data, f)

    total_papers_after = sum(len(papers) for papers in data.values())
    logging.info(f"✓ Cleanup completed: {papers_kept} papers kept, {papers_removed} papers removed")
    logging.info(f"  Papers after cleanup: {total_papers_after}")

    return total_papers_before, total_papers_after

def json_to_md(filename, md_filename,
               task='',
               to_web=False,
               use_title=True,
               use_tc=True,
               use_b2t=True,
               show_abstract=False):
    """
    Convert JSON data to Markdown format
    @param filename: input JSON file path
    @param md_filename: output Markdown file path
    @param task: task name for logging
    @param to_web: whether generating for web
    @param use_title: whether to use title
    @param use_tc: whether to use table of contents
    @param use_b2t: whether to use back to top
    @param show_abstract: whether to show paper abstracts
    """
    def pretty_math(s: str) -> str:
        """
        Format LaTeX math expressions for better display
        @param s: string containing math expressions
        @return: formatted string
        """
        ret = ''
        match = re.search(r"\$.*\$", s)
        if match is None:
            return s
            
        math_start, math_end = match.span()
        math_content = match.group()[1:-1]  # Remove $ signs
        
        # Process the part before math
        before_math = s[:math_start]
        # Process the part after math
        after_math = s[math_end:]
        
        # Check if we need to add spaces around the math expression
        space_before = ''
        space_after = ''
        
        # Check character before math (if exists)
        if before_math and not before_math[-1].isspace() and before_math[-1] != '*':
            space_before = ' '
            
        # Check character after math (if exists)
        if after_math and not after_math[0].isspace() and after_math[0] != '*':
            space_after = ' '
        
        # Reconstruct the string with proper spacing
        ret = before_math + space_before + '$' + math_content.strip() + '$' + space_after + after_math
        return ret

    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-', '.')

    with open(filename, "r") as f:
        content = f.read()
        if not content:
            data = {}
            total_papers = 0
        else:
            data = json.loads(content)
            total_papers = sum(len(papers) for papers in data.values())

    # Clean README.md if it exists, otherwise create it
    with open(md_filename, "w+") as f:
        pass

    # Write data into README.md
    with open(md_filename, "a+") as f:

        if (use_title == True) and (to_web == True):
            f.write("---\n" + "layout: default\n" + "---\n\n")

        if use_title == True:
            f.write("## Updated on " + DateNow + "\n")
        else:
            f.write("> Updated on " + DateNow + "\n")

        # Add: table of contents (without folding)
        if use_tc == True:
            f.write("## Table of Contents\n")
            f.write("<ol>\n")
            for keyword in data.keys():
                day_content = data[keyword]
                if not day_content:
                    continue
                kw = keyword.replace(' ', '-')
                f.write(f"<li><a href=#{kw.lower()}>{keyword}</a></li>\n")
            f.write("</ol>\n\n")

        # Add CSS for alternating row colors
        if to_web == False:  # Only for README, not for web
            f.write("""
<style>
.paper-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
}
.paper-item {
    padding: 12px 15px;
    margin: 15px 0;
    border-radius: 8px;
    border-left: 4px solid #ddd;
}
.paper-item-odd {
    background-color: #f8f9fa;
    border-left-color: #4285f4;
}
.paper-item-even {
    background-color: #ffffff;
    border-left-color: #34a853;
}
.paper-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 8px;
}
.paper-title {
    font-weight: bold;
    font-size: 1.05em;
    margin: 0;
    flex: 1;
}
.paper-date {
    color: #666;
    font-size: 0.9em;
    white-space: nowrap;
    margin-left: 15px;
}
.paper-authors {
    color: #555;
    font-style: italic;
    margin-bottom: 5px;
}
.paper-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.9em;
    color: #666;
}
.paper-categories {
    font-family: monospace;
    background-color: #e9ecef;
    padding: 2px 6px;
    border-radius: 4px;
}
.paper-link {
    color: #1a73e8;
    text-decoration: none;
}
.paper-link:hover {
    text-decoration: underline;
}
.paper-comments {
    color: #d93025;
    font-size: 0.85em;
    margin-top: 4px;
    white-space: pre-wrap; /* Preserve whitespace and wrap text */
    word-wrap: break-word; /* Break long words */
}
.paper-abstract {
    margin-top: 10px;
    font-size: 0.9em;
    line-height: 1.4;
    color: #555;
    white-space: pre-wrap; /* Preserve whitespace and wrap text */
    word-wrap: break-word; /* Break long words */
}
.abstract-label {
    font-weight: bold;
    color: #666;
    margin-bottom: 3px;
}
</style>

""")

        for keyword in data.keys():
            day_content = data[keyword]
            if not day_content:
                continue
            # The head of each part
            f.write(f"## {keyword}\n\n")

            # Sort papers by date
            day_content = sort_papers(day_content)

            # Start paper list
            if to_web == False:  # For README, use styled list
                f.write('<div class="paper-list">\n')
                
                paper_index = 0
                day_content_list = list(day_content.items())
                for paper_key, v in day_content_list:
                    if v is not None:
                        # Parse the table row to extract paper information
                        parts = v.strip().split('|')
                        if len(parts) >= 7:
                            # Adjust index based on whether abstract is included
                            if show_abstract and len(parts) >= 8:
                                date = parts[1].replace('**', '').strip()
                                title = parts[2].replace('**', '').strip()
                                last_author = parts[3].strip()
                                categories = parts[4].strip()
                                pdf_link = parts[5].strip()
                                comments = parts[6].strip()
                                abstract = parts[7].strip()
                            else:
                                date = parts[1].replace('**', '').strip()
                                title = parts[2].replace('**', '').strip()
                                last_author = parts[3].strip()
                                categories = parts[4].strip()
                                pdf_link = parts[5].strip()
                                comments = parts[6].strip()
                                abstract = ""
                            
                            # Extract PDF link and ID
                            pdf_match = re.search(r'\[(.*?)\]\((.*?)\)', pdf_link)
                            if pdf_match:
                                paper_id = pdf_match.group(1)
                                paper_url = pdf_match.group(2)
                            else:
                                paper_id = "PDF"
                                paper_url = "#"
                            
                            # Create styled list item with alternating classes
                            paper_index += 1
                            item_class = "paper-item-odd" if paper_index % 2 == 1 else "paper-item-even"
                            f.write(f'<div class="paper-item {item_class}">\n')
                            
                            # Header with title and date
                            f.write('  <div class="paper-header">\n')
                            f.write(f'    <div class="paper-title">{pretty_math(title)}</div>\n')
                            f.write(f'    <div class="paper-date">{date}</div>\n')
                            f.write('  </div>\n')
                            
                            # Authors with "last author:" label
                            if last_author:
                                f.write(f'  <div class="paper-authors">{last_author} (last author)</div>\n')
                            
                            # Metadata: categories and PDF link
                            f.write('  <div class="paper-meta">\n')
                            if categories:
                                f.write(f'    <span class="paper-categories">{categories}</span>\n')
                            f.write(f'    <a class="paper-link" href="{paper_url}" target="_blank">📄 PDF: {paper_id}</a>\n')
                            f.write('  </div>\n')
                            
                            # Comments - show complete comments without truncation
                            if comments and comments != "":
                                f.write(f'  <div class="paper-comments">💬 {comments}</div>\n')
                            
                            # Abstract (if enabled and available) - show complete abstract without truncation
                            if show_abstract and abstract and abstract != "":
                                f.write(f'  <div class="paper-abstract">\n')
                                f.write(f'    <div class="abstract-label">📖 Abstract:</div>\n')
                                f.write(f'    {pretty_math(abstract)}\n')
                                f.write(f'  </div>\n')
                            
                            f.write('</div>\n')
                            
                            # Add extra space between papers (except for the last one)
                            if paper_index < len(day_content_list):
                                f.write('<div style="height: 10px;"></div>\n')
                
                f.write('</div>\n\n')
                
            else:  # For web (GitPage), keep original format
                if use_title == True:
                    if to_web == False:
                        if show_abstract:
                            f.write("|Publish Date|Title|Last Author|Categories|PDF|Comments|Abstract|\n")
                            f.write("|---|---|---|---|---|---|---|\n")
                        else:
                            f.write("|Publish Date|Title|Last Author|Categories|PDF|Comments|\n")
                            f.write("|---|---|---|---|---|---|\n")
                    else:
                        if show_abstract:
                            f.write("| Publish Date | Title | Last Author | Categories | PDF | Comments | Abstract |\n")
                            f.write("|:---------|:-----------------------|:---------|:----------|:------|:----------|:----------|\n")
                        else:
                            f.write("| Publish Date | Title | Last Author | Categories | PDF | Comments |\n")
                            f.write("|:---------|:-----------------------|:---------|:----------|:------|:----------|\n")

                for _, v in day_content.items():
                    if v is not None:
                        f.write(pretty_math(v))

                f.write(f"\n")

            # Add: back to top
            if use_b2t:
                top_info = f"#Updated on {DateNow}"
                top_info = top_info.replace(' ', '-').replace('.', '')
                f.write(f"<p align=right>(<a href={top_info.lower()}>back to top</a>)</p>\n\n")

    logging.info(f"✓ {task} generation finished - Generated Markdown with {total_papers} papers")

def demo(**config):
    """
    Main function to fetch papers and update output files
    @param config: configuration dictionary
    """
    data_collector = []

    keywords = config['kv']
    max_results = config['max_results']
    publish_readme = config['publish_readme']
    publish_gitpage = config['publish_gitpage']
    show_abstract = config.get('show_abstract', False)

    cleanup_enabled = config['cleanup']['enabled']
    keep_days = config['cleanup']['keep_days']
    date_range_enabled = config.get('date_range_enabled', False)
    start_date = config.get('start_date')
    end_date = config.get('end_date')

    # Display configuration information
    logging.info("=" * 60)
    logging.info("STARTING PAPER COLLECTION")
    logging.info("=" * 60)

    if date_range_enabled:
        date_range_str = f"{start_date} to {end_date}" if start_date and end_date else f"from {start_date}" if start_date else f"until {end_date}"
        logging.info(f"Custom date range: {date_range_str}")
        logging.info(f"Processing {len(keywords)} keywords with max {max_results} papers each in specified date range")
        logging.info("Will clear existing JSON content and replace with papers from date range")
    else:
        logging.info(f"Processing {len(keywords)} keywords with max {max_results} papers each")
        if cleanup_enabled:
            logging.info(f"Cleanup enabled: keeping {keep_days} days of papers")

    logging.info(f"Show abstract: {show_abstract}")

    # Fetch new papers
    total_new_papers = 0
    for topic, keyword in keywords.items():
        # Pass date range parameters and show_abstract
        data = get_daily_papers(topic, query=keyword, max_results=max_results,
                               start_date=start_date, end_date=end_date,
                               show_abstract=show_abstract)

        if topic in data and data[topic]:
            papers_count = len(data[topic])
            total_new_papers += papers_count

        data_collector.append(data)

    logging.info(f"✓ Collected {total_new_papers} new papers from arXiv")

    # 1. Update README.md file
    if publish_readme:
        logging.info("-" * 40)
        logging.info("UPDATING README")
        logging.info("-" * 40)

        json_file = config['json_readme_path']
        md_file = config['md_readme_path']

        # Check if JSON file exists
        json_exists = os.path.exists(json_file)

        # Only perform cleanup if custom date range is not enabled and cleanup is enabled
        if cleanup_enabled and not date_range_enabled and json_exists:
            before_cleanup, after_cleanup = cleanup_old_papers(json_file, keep_days)
        else:
            # Skip cleanup if date range is enabled
            if date_range_enabled:
                logging.info("Skipping cleanup due to custom date range")
            # Get current paper count
            if json_exists and not date_range_enabled:
                with open(json_file, "r") as f:
                    content = f.read()
                    if content:
                        existing_data = json.loads(content)
                        after_cleanup = sum(len(papers) for papers in existing_data.values())
                    else:
                        after_cleanup = 0
            else:
                after_cleanup = 0

        # Update JSON data - clear existing content if date range is enabled
        existing_count, updated_count, new_count, category_updates = update_json_file(
            json_file, data_collector, keywords, clear_existing=date_range_enabled)

        # Print update status for each category
        for category, added_count in category_updates.items():
            if added_count > 0:
                logging.info(f"  Added {added_count} new papers to '{category}'")

        if date_range_enabled:
            logging.info(f"✓ README JSON replaced with {updated_count} papers from date range")
        else:
            actual_added = updated_count - after_cleanup
            logging.info(f"✓ README JSON updated: {actual_added} new papers added")
            logging.info(f"  Total papers in README: {updated_count}")

        # Generate Markdown with show_abstract parameter
        json_to_md(json_file, md_file, task='README', show_abstract=show_abstract)

    # 2. Update docs/gitpage.md file (for gitpage)
    if publish_gitpage:
        logging.info("-" * 40)
        logging.info("UPDATING GITPAGE")
        logging.info("-" * 40)

        json_file = config['json_gitpage_path']
        md_file = config['md_gitpage_path']

        # Check if JSON file exists
        json_exists = os.path.exists(json_file)

        # Only perform cleanup if custom date range is not enabled and cleanup is enabled
        if cleanup_enabled and not date_range_enabled and json_exists:
            before_cleanup, after_cleanup = cleanup_old_papers(json_file, keep_days)

        # Update JSON data - clear existing content if date range is enabled
        existing_count, updated_count, new_count, category_updates = update_json_file(
            json_file, data_collector, keywords, clear_existing=date_range_enabled)

        # Print update status for each category
        for category, added_count in category_updates.items():
            if added_count > 0:
                logging.info(f"  Added {added_count} new papers to '{category}'")

        if date_range_enabled:
            logging.info(f"✓ GitPage JSON replaced with {updated_count} papers from date range")
        else:
            logging.info(f"✓ GitPage JSON updated: {updated_count - existing_count} new papers added")
            logging.info(f"  Total papers in GitPage: {updated_count}")

        # Generate Markdown - GitPage doesn't show abstract for now
        json_to_md(json_file, md_file, task='GitPage',
                  to_web=True, use_tc=False, use_b2t=False, show_abstract=False)

    logging.info("=" * 60)
    logging.info("PROCESS COMPLETED SUCCESSFULLY")
    logging.info("=" * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, default='config.yaml',
                        help='configuration file path')
    args = parser.parse_args()
    config = load_config(args.config_path)
    demo(**config)