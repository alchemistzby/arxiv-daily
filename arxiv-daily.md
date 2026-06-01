## Updated on 2026.06.01
## Table of Contents
<ol>
<li><a href=#qml>QML</a></li>
<li><a href=#qc>QC</a></li>
<li><a href=#ai-for-science>AI for science</a></li>
</ol>


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

## QML

<div class="paper-list">
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Trainable Quantum Spectral Models for Partial Differential Equations</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Achim Streit (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31248" target="_blank">📄 PDF: 2605.31248</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    This work studies trainable quantum spectral models (QSMs) for solving linear partial differential equations (PDEs). Instead of learning solutions directly in physical space, QSMs learn the inverse differential operator in a spectral representation, embedding prior knowledge of the equation's natural basis.   We systematically study the expressibility and trainability of several QSM architectures, ranging from near-diagonal to fully parameterized unitaries. In particular, we introduce a family of richer spectral models that interpolate between purely diagonal operators and fully mixing unitaries through a parameterized mixer controlled by $ε$. Our results reveal an intermediate regime, typically around $ε\approx 0.5$ , where models achieve the best tradeoff between expressibility and trainability. Beyond this threshold, increased circuit complexity degrades convergence without improving accuracy.   Among the architectures considered, models inspired by the inverse step of the Harrow-Hassidim-Lloyd (HHL) algorithm achieve the fastest training convergence while maintaining high solution fidelity. Numerical experiments on the (variable-coefficient) Poisson and Helmholtz equations show that trainable operations in the spectral basis outperform standard variational quantum circuits acting directly in the computational basis. These advantages appear through faster convergence, more stable gradients, and more accurate recovery of the reference solution spectrum, particularly through stronger suppression of spurious high-frequency components, even when the operator is not exactly diagonal in the chosen spectral basis. Our results identify operator-aware spectral representations as a promising route toward trainable and physically grounded quantum methods for scientific computing.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Quantum State Preparation via Neural Network Encoding in Quantum Machine Learning</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Andre Luckow (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31006" target="_blank">📄 PDF: 2605.31006</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    A central challenge in quantum machine learning is the state preparation bottleneck that describes the prohibitive computational cost of loading high-dimensional classical data into a quantum state. Although amplitude encoding can represent $2^n$-dimensional data using only $n$ qubits in principle, preparing arbitrary states remains computationally expensive, typically requiring variational optimization of a parameterized quantum circuit for each individual data instance. In this work, we propose a method that avoids iterative optimization by training a classical neural network to map input data directly to the continuous parameters of a fixed quantum circuit. We demonstrate the generation of quantum image states with high fidelity on data not seen during training. Since all optimization is performed once during training, the resulting model encodes new inputs in a single inference step, providing a scalable pathway for data loading in near-term quantum algorithms. We validate our method on the MNIST and Fashion-MNIST datasets, achieving fidelities up to 0.992 on unseen images and reducing the per-data-instance runtime by more than 5000-fold.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Generative Quantum Data Embeddings for Supervised Learning</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Daniel K. Park (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30866" target="_blank">📄 PDF: 2605.30866</a>
  </div>
  <div class="paper-comments">💬 14 pages, 7 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Many practically relevant applications of quantum machine learning involve classical data, for which performance depends critically on how inputs are embedded into quantum states. Yet the use of a fixed embedding circuit ansatz remains standard practice. We propose an energy-based generative learning framework that synthesizes gate sequences to optimize embedding structures and refine data-tailored parameters, using a fidelity-based surrogate objective to guide the search toward improved class distinguishability. Empirically, the method improves classification performance across diverse settings, while also revealing datasets where architecture search within the present embedding family yields only limited additional gains. We explain this saturation by deriving bounds on the achievable empirical risk in terms of the Wasserstein distance in the input space, showing that classical data geometry provides an \emph{a priori} diagnostic for regimes in which substantial gains from embedding optimization are unlikely. The results establish a practically useful and theoretically motivated framework for searching effective quantum data embeddings through generative optimization, with the attainable gains diagnosed through the geometry of the underlying classical data.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Research progress on quantum neural networks and quantum machine learning</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Xiangdong Zhang (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30724" target="_blank">📄 PDF: 2605.30724</a>
  </div>
  <div class="paper-comments">💬 47 pages, 8 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Machine learning holds fundamental computational significance due to the increasing demand for efficient solutions to complex tasks in data analysis, pattern recognition, and optimization, which are essential for addressing the multifaceted challenges of modern society. As the volume of data proliferates at an unprecedented rate, the need for more powerful machine learning strategies becomes increasingly evident. Quantum neural networks (QNNs) represent an emerging and transformative research field that seeks to harness the unique principles of quantum mechanics to enhance the capabilities of machine learning algorithms. This survey examines various QNN approaches, including fully connected QNNs, quantum convolutional neural networks, equivariant QNNs, quantum Hopfield networks, quantum Boltzmann machines, quantum reservoir computing, and composite networks for quantum reinforcement learning, quantum generative learning, and quantum transfer learning. We summarize the relevant investigations on their performance, including learning accuracy, training time, and resource requirements, etc. Each QNN type has unique strengths and weaknesses, offering diverse solutions for different applications.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Mitigating Noise-Induced Barren Plateaus Using a Non-Unitary Ansatz: Application to Molecular Electronic Transport</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Michael Kolodrubetz (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30572" target="_blank">📄 PDF: 2605.30572</a>
  </div>
  <div class="paper-comments">💬 29 pages, 17 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Variational quantum algorithms (VQAs) offer a promising route toward simulating many-body quantum systems on noisy intermediate-scale quantum (NISQ) hardware. However, their scalability is severely limited by noise-induced barren plateaus (NIBPs), where hardware noise causes the gradients of the cost function to vanish exponentially with circuit depth, rendering optimization impossible. In this work, we demonstrate that introducing nonunitary elements into the variational ansatz can mitigate NIBPs in open-quantum systems. Using an analytically tractable infinite-range dissipative Ising model, we show that a nonunitary ansatz restores finite gradients in the presence of depolarizing noise, enabling convergence to the correct symmetry-broken steady state. We also develop a Floquet-type variational ansatz in which each layer repeats the same parameters, reducing the deep variational circuit to an effective quantum channel whose fixed points can be analyzed directly. We then extend these ideas to a realistic quantum-chemistry system by simulating electron transport through Oligophenylethynylene-sulfurmethyl (OPE-SMe) using Hamiltonians and jump operators of the model derived from first-principles polarizable QM/MM calculations. Our results show that nonunitary variational ansätze provide a scalable and physically grounded route for simulating open-system steady states on NISQ hardware, offering a pathway to overcoming one of the limitations of current quantum hardware.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Qubit-efficient variational algorithm for nuclear structure</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Paul Stevenson (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">nucl-th; quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30261" target="_blank">📄 PDF: 2605.30261</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    In this work, we compare three qubit-mapping strategies to study the structure of the nuclear ground state within the shell model description employing the Variational Quantum Eigensolver (VQE) approach. Although the initial point for different mappings is a Hamiltonian matrix in many-body particle basis or Slater determinant (SD) basis, the structure of the trial wavefunction and resource counts are different for each mapping. These three mappings are tested for a mid $p$-shell nucleus $^{10}$B and compared the quantum resources required to find the ground state for each mapping. Further, we extend the qubit-efficient mapping to study the ground state of one more mid $p$-shell nucleus $^{12}$C. We run circuits up to 26-qubits representing their ground states on a noisy simulator (IBM's FakeFez backend) and quantum hardware ($ibm\_fez$). The best post-error mitigated results from the hardware for $^{10}$B ground state is obtained following SD to qubit mapping with a percent error of 0.21 \%. The percent errors for the same state following cSD and pnSD mapping are 3.37 and 8.88 \%, respectively. On the other hand, following the cSD mapping, the post-error mitigated ground state energy of $^{12}$ C is 6.82 \% away from the exact result. We further evaluate the fidelity of the VQE wavefunctions obtained from hardware with respect to the shell model wavefunctions for the cSD mapping. This cSD mapping can be useful for scaling the VQE algorithm for complex nuclei across different mass regions in terms of qubit efficiency.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Verifying Adversarial Robustness in Quantum Machine Learning: from theory to physical validation via a software tool</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Mingsheng Ying (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.29877" target="_blank">📄 PDF: 2605.29877</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    As with classical neural networks, quantum machine learning (QML) models are vulnerable to small input perturbations that can significantly alter output predictions. Certifying the robustness of QML models, particularly on NISQ hardware, is therefore a fundamental step toward trustworthy quantum AI. This chapter reviews our recently developed comprehensive formal framework for verifying adversarial robustness in QML. The core of this framework is a fidelity-based robustness lower bound computable directly from the measurement outcome distribution, which enables both formal verification and empirical estimation on real quantum devices. Additionally, the optimal bound can be computed via semidefinite programming (SDP) with full knowledge of the quantum machine learning models. We incorporate these results into: (1) an efficient formal verification framework; (2) VeriQR, the first dedicated QML robustness verification tool; and (3) the first experimental benchmark of quantum adversarial robustness on a 20-qubit superconducting processor. Together, these systematic advances enable scalable, physically grounded robustness evaluation of QML models.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Quantum Subliminal Learning</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Yu-Qin Chen (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.29557" target="_blank">📄 PDF: 2605.29557</a>
  </div>
  <div class="paper-comments">💬 4.5 pages, 3 figures, with supplemental materials</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Machine learning models can inherit hidden behavioral traits through innocuous public interfaces, a phenomenon known as subliminal learning. Here we extend this framework to quantum models and study two distillation pathways: an auxiliary channel on random inputs and a restricted task channel in which the student matches a public supervised output while the hidden behavior resides on a disjoint task. Both classical and quantum neural networks (QNNs) exhibit efficient auxiliary-channel subliminal learning, but the task channel shows strong architecture dependence. Classical neural networks transmit little hidden-task information through the public-task interface, whereas QNNs retain most of the hidden-task signal. We show that a unified geometric picture explains both regimes: transmission is controlled by the teacher drift magnitude together with the fraction of hidden-task-relevant drift that remains visible through the public interface. These results identify a concrete security concern for quantum model supply chains and suggest a controlled route for hidden-information transfer in quantum information processing.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Rademacher Complexity Bounds for Parameterized Quantum Circuits Generated by Pauli Strings</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Hiroshi Ohno (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.29546" target="_blank">📄 PDF: 2605.29546</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    In this study, we analyze the Rademacher complexity $\mathcal{R}_{M} $ of a parameterized unitary whose generators are chosen from $ n $-qubit Pauli strings. Although generalization bounds for quantum machine learning models have been studied in several settings, explicit Rademacher-complexity bounds for parameterized unitaries generated by Pauli strings remain less transparent. We derive simple scaling bounds in terms of the number of parameters $ L $ and the number of training samples $ M $: $ \mathcal{O}(\frac{L^{\frac{3}{2}}}{\sqrt{M}}) $ for the full parameter domain and $ \mathcal{O}(\frac{L}{\sqrt{M}})$ for a restricted parameter domain. Furthermore, we compare the obtained results with those for a classical linear model class and suggest a potential statistical-complexity advantage when the norms of both the input and the parameter in the classical model scale with the number of parameters. Numerical experiments provide qualitative evidence consistent with the predicted scaling.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">A Variational Quantum Algorithm for Nonlinear Finite Element Analysis of Hyperelastic Materials</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Caglar Oskay (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; math.NA; physics.comp-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.29181" target="_blank">📄 PDF: 2605.29181</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    This manuscript explores a variational quantum formulation for nonlinear elasticity problems arising from hyperelastic material models, targeting near term noisy intermediate scale quantum (NISQ) devices. The approach leverages the potential energy structure of hyperelasticity and employs a hybrid quantum classical framework in which the energy functional is evaluated using parameterized quantum circuits and optimized through classical routines. To enable implementation on current quantum hardware, polynomial approximations of the nonlinear strain energy density are introduced, yielding a representation compatible with variational quantum algorithms. The methodology is demonstrated on a one dimensional NeoHookean material model using finite element discretizations with first and second order shape functions and nonhomogeneous boundary conditions. Numerical experiments investigate the influence of the polynomial approximation order on the accuracy and efficiency of the proposed approach, illustrating its feasibility for near term quantum devices.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Quantum-Enhanced Adversarial Robustness in Artificial Intelligence</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Jaydip Sen (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.CR; cs.AI</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.28899" target="_blank">📄 PDF: 2605.28899</a>
  </div>
  <div class="paper-comments">💬 This is the pre-print of the chapter which has been accepted for publication in the edited volume titled "Quantum Enhancements to the AI Industry", edited by Eduard Babulak. The volume will be published by IGI Global, USA. This is not the final version of the chapter published in the book</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Artificial Intelligence has achieved remarkable success across diverse application domains. However, its vulnerability to adversarial attacks poses significant challenges to reliability, security, and trustworthiness. Adversarial machine learning demonstrates that even highly accurate models can be manipulated through carefully crafted perturbations, raising serious concerns in safety critical systems such as healthcare, finance, and autonomous technologies. In parallel, quantum computing has emerged as a transformative paradigm capable of addressing complex computational problems through principles such as superposition, entanglement, and quantum interference. The convergence of these fields has led to the emergence of quantum artificial intelligence, which explores how quantum techniques can enhance learning efficiency, scalability, and robustness. This chapter provides a comprehensive overview of adversarial machine learning and existing defense strategies, followed by an accessible introduction to quantum computing and quantum machine learning models. It further presents conceptual frameworks for quantum-enhanced adversarial robustness, emphasizing quantum optimization, feature mapping, and hybrid quantum classical architectures. Practical applications, key challenges, and future research directions are also discussed to support the development of secure and trustworthy AI systems.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Meta-Quantum Ensemble Framework for Robust Network Intrusion Detection</div>
    <div class="paper-date">2026-05-26</div>
  </div>
  <div class="paper-authors">Muhammad Shafique (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; cs.CR</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.28879" target="_blank">📄 PDF: 2605.28879</a>
  </div>
  <div class="paper-comments">💬 10 pages, 9 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Intrusion Detection Systems (IDSs) must maintain high detection sensitivity while operating under strict false-positive constraints, a challenge intensified by class imbalance and heterogeneous IoT traffic. This work investigates whether heterogeneous quantum learners can provide useful and non-redundant decision information for IDS tasks. We study Quantum Support Vector Machines (QSVMs) and Quantum Neural Networks (QNNs), which rely on different learning mechanisms and exhibit distinct prediction behaviors. To combine these models, we propose the System-Level Meta-Quantum Ensemble (MQE), a hybrid quantum-classical framework that fuses QSVM and QNN outputs using a Random Forest meta-learner. The meta-learner captures agreement and disagreement patterns between the quantum branches to improve prediction stability and detection performance. Experiments on TON IoT and CICIDS2017 show that MQE improves selected performance, low-FPR, and reliability metrics over several standalone quantum learners, with gains depending on the dataset, metric, and fusion representation. The results highlight meta-level fusion as a practical strategy for building more reliable QML-based IDS pipelines.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Variational Quantum Models for Knowledge Graph Embeddings on NISQ Devices</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Gustavo Martín Bosyk (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.28723" target="_blank">📄 PDF: 2605.28723</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Variational Quantum Algorithms (VQAs) combine quantum circuits with classical optimization to tackle problems that may benefit from the capabilities of near-term quantum hardware. In knowledge graph embedding, recent proposals based on this approach follow a similar overall architecture but differ in the way they compute the score function and in the number of qubits they require. One design uses $n+1$ qubits and obtains the score through a switch test on an ancillary qubit, while another employs $2n+1$ qubits and applies a swap test between two registers. In both cases, entities and relations are represented in a Hilbert space of dimension $d = 2^n$ , with comparable computational cost and the same mean squared error loss. This work introduces a unified framework that captures the two schemes and makes it possible to explore new variants. Within this setting, we propose an alternative that keeps the intuitive meaning of the score function while dispensing with ancillary qubits and entangled measurements. The result is a model better suited to current NISQ devices, reducing hardware demands without sacrificing interpretability.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Latent-Conditioned Parameterized Quantum Circuits as Universal Approximators for Distributions over Quantum States</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Hirotaka Oshima (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.28690" target="_blank">📄 PDF: 2605.28690</a>
  </div>
  <div class="paper-comments">💬 16 pages, 11 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Many applications in quantum simulation, quantum chemistry, and quantum machine learning require not a single quantum state but an ensemble of states characterizing the heterogeneity of a target system. Preparing such ensembles state-by-state is prohibitive in both variational and fault-tolerant settings, motivating a generative-modeling approach. We introduce latent-conditioned parameterized quantum circuits (LPQCs), a hybrid quantum-classical framework in which classical neural networks map a latent variable sampled from a prior distribution to the parameters of a parameterized quantum circuit. We prove that LPQCs are universal approximators for probability measures over density operators in the $1$ -Wasserstein distance, extending classical universal approximation theorems to the quantum-distribution setting. We additionally introduce a multimodal latent prior and a mixture-of-experts circuit architecture, and show that it empirically alleviates the barren plateau problem during optimization. Numerical experiments validate the framework on a synthetic multi-cluster ensemble of mixed quantum states and on a QM9-derived ensemble of 3-D molecular structures. In these tasks, LPQC outperforms recent quantum generative baselines while remaining competitive with typical classical baselines at substantially reduced output dimensionality. By leveraging classical expressivity in the latent space, LPQCs offer a tractable route to quantum generative modeling.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Thermodynamic-limit dispersion relations on trapped-ion quantum hardware</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Michael J. Hartmann (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; cond-mat.str-el</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.28599" target="_blank">📄 PDF: 2605.28599</a>
  </div>
  <div class="paper-comments">💬 15+6 pages, 7+11 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We run a numerical linked-cluster expansion with a quantum algorithm (NLCE+QA), computing ground-state energies and one quasi-particle dispersions in the thermodynamic limit using a 20-qubit trapped-ion quantum processing unit (QPU). The NLCE+QA framework extracts thermodynamic-limit properties from small-cluster calculations, making it naturally suited for near-term quantum devices. Projector-based block-diagonalization schemes such as projective cluster-additive transformation (PCAT) are essential to NLCE+QA, and they involve matrix inversion and square root operations that amplify measurement noise. A central question is therefore whether current hardware can provide expectation values that are accurate enough to withstand non-linear classical post-processing. We explore this challenge for the transverse-field Ising model (TFIM) in one dimension, on a ladder geometry, as well as in a longitudinal field in one dimension. For the quantum algorithm, we consider adiabatic state preparation (ASP), as well as a variational quantum eigensolver (VQE) trained on a classical device. The final expectation values are obtained from the QPU, using a novel alternative to the Hadamard test that we name the CX-test. We explore the regimes currently attainable on quantum devices and comment on the improvements needed for quantum computers to achieve results beyond classical reach.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Automated Unitary Coupled Cluster Circuit Design via Differentiable Quantum Architecture Search</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Weitang Li (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; physics.chem-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.28049" target="_blank">📄 PDF: 2605.28049</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Designing compact and accurate circuits for the variational quantum eigensolver (VQE) is a central challenge in near-term quantum chemistry. Existing adaptive methods such as ADAPT-VQE design circuits by iteratively selecting operators from a predefined pool guided by gradient information and greedy heuristics. In this work, we adopt differentiable quantum architecture search (DQAS) as a circuit design framework based on the UCCSD operator pool, and introduce two complementary strategies: a global mode that simultaneously optimizes all operator selections, and a layerwise mode that constructs circuits incrementally while preserving previously learned structure. By relaxing discrete operator selection into a continuous differentiable optimization, DQAS enables gradient-based exploration over the combinatorial space of UCC circuit architectures. Benchmarks on BeH2, H4, LiH, H6, and H2O (8-14 qubits) show that both strategies achieve higher accuracy and fewer CNOT gates than ADAPT-VQE in the compact circuit regime, with up to 2.7-fold accuracy improvement for H2O and CNOT reductions of 13-17% at equivalent circuit depths. Benchmarks on the qubit-excitation-based (QEB) operator pool confirm that both advantages generalize beyond UCCSD. These results demonstrate that differentiable architecture search provides an effective and generalizable framework for designing accurate and compact VQE circuits in near-term quantum chemistry.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Do We Really Need Quantum Machine Learning?: A Multidimensional Empirical Study</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Sayanton Dibbo (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.CV; cs.AI; cs.LG; quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.27923" target="_blank">📄 PDF: 2605.27923</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    The rapid growth of computer vision and increasingly complex image recognition tasks has exposed fundamental computational limitations of classical machine learning models, motivating the exploration of quantum computing as an emerging new paradigm. This paper presents a comprehensive benchmarking study of classical and quantum machine learning models for image recognition on the MNIST handwritten digit dataset, evaluating both traditional models, a Classical Support Vector Machine (CSVM) and a Quantum Support Vector Machine (QSVM), and deep neural network models, a Classical Convolutional Neural Network (CCNN) and a Quantum Convolutional Neural Network (QCNN), across four performance dimensions: classification accuracy, computational runtime, parameter count, and memory requirements. Experiments are conducted as functions of both feature dimensionality and sample size, and across CPU and GPU execution environments, providing a controlled, multidimensional comparison to address gaps in prior work. For the SVM-based models, QSVM consistently outperforms CSVM in accuracy, reaching $\sim$ 0.90 versus $\sim$ 0.85 at 1,000 samples, with a higher computational cost. A feature count of 10 qubits and a sample size in the range of 200 -- 500 emerge as practical operating points that balance accuracy and runtime. For the neural network models, CCNN and QCNN achieve comparable classification accuracy, both exceeding 0.96 at 64 features and 60,000 samples, yet QCNN offers substantially superior parameter and memory efficiency, requiring $\sim$ 94\% fewer parameters and $\sim$ 75\% less memory than CCNN at higher feature counts, while incurring higher runtime. Across both model families, quantum models consistently outperform classical models by greater margins in accuracy as feature dimensionality or sample size increases.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Geometric Analysis of Variational Quantum Eigensolver</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Zhen Qin (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; eess.SP; math.OC</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.27795" target="_blank">📄 PDF: 2605.27795</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    The Variational Quantum Eigensolver (VQE) is a fundamental algorithm in quantum computing, yet a coherent geometric characterization of VQE remains missing due to fragmented analyses across fixed-ansatz and adaptive-circuit formulations. In this paper, we establish a geometric analysis of VQE in terms of optimization landscape, initialization guarantee, and noise robustness. First, we study the optimization landscape via an ansatz-free product-unitary formulation over the unitary group, unifying both paradigms. For the single-unitary case, we establish linear convergence of Riemannian gradient descent (RGD) and prove the strict saddle property. For the product-unitary case, we show the convergence rate deteriorates polynomially with circuit depth, providing a geometric explanation of the barren plateau phenomenon. Second, we prove that small-angle random Pauli-rotation circuits satisfy the required initialization conditions with high probability. Third, we show that RGD retains linear convergence under finite-shot measurements, and that coefficient-adaptive allocation achieves strictly lower statistical error than uniform sampling under a fixed measurement budget.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">EFaaS: A Quantum-Classical Serverless Entangled Scheduler for Hybrid Variational Algorithms</div>
    <div class="paper-date">2026-05-26</div>
  </div>
  <div class="paper-authors">Muhammad Shafique (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; cs.DC</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.27540" target="_blank">📄 PDF: 2605.27540</a>
  </div>
  <div class="paper-comments">💬 12 pages, 10 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    As quantum computing enters the Utility Era, realizing near-term advantage relies heavily on Hybrid Variational Quantum Algorithms (VQAs). These algorithms require a tightly coupled, iterative loop between a classical CPU optimizer and a Quantum Processing Unit (QPU). However, current quantum cloud access models are bottlenecked by decoupled batch-queues that sever this loop, introducing massive Time-to-Next-Shot (TTNS) latency. This delay inflates convergence time from minutes to hours and exposes the computation to quantum hardware drift, degrading algorithmic fidelity. Unlike prior works that rely on resource-wasting static hardware reservations or state-oblivious stateless functions, we propose EFaaS, a novel serverless middleware designed specifically for hybrid quantum workflows. EFaaS fundamentally departs from existing architectures by treating classical parameter optimization and quantum circuit execution as entangled, session-aware events. Our main technical innovations are threefold: (1) a Calibration-Aware placement strategy that dynamically routes circuits to QPUs with warm calibration caches, circumventing cold-start penalties, (2) a Dual-Resource Fair Queuing scheduler that maximizes quantum utilization by strictly prioritizing active iterative loops, and (3) the "EF-QuantumFuture" programming abstraction, a novel primitive enabling classical speculative execution to mask compute latency. Across the evaluated baselines, EFaaS achieves TTNS reductions of 11.4%-94.3%, QDC gains of 2.02%-15.78% points, and convergence speedups of 83.2%-98.3%, while eliminating drift penalties.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Native topological readout on qubit hardware: a Fibonacci-chain benchmark of measurement-compilation trade-offs</div>
    <div class="paper-date">2026-05-25</div>
  </div>
  <div class="paper-authors">Babatunde Moses Ayeni (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; cond-mat.str-el; cs.ET</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.25913" target="_blank">📄 PDF: 2605.25913</a>
  </div>
  <div class="paper-comments">💬 16 pgs, 8 figs, 3 tabs</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Recent demonstrations of non-Abelian braiding of graph vertices on noisy intermediate-scale quantum (NISQ) superconducting processor, and the experimental realization of topological order in general on various quantum hardware platforms necessitate an important question: when does a native (topological) fusion readout genuinely help for topological anyonic Hamiltonians implemented on NISQ hardware? We use the Fibonacci anyons chain as a concrete model for understanding the trade-off between measurement cost and compilation cost in that setting. The comparison is made against a simple grouped-Pauli baseline, and is scored by a covariance-aware mean-squared-error (MSE) of the full energy estimator. We based our benchmark on two different important classes of quantum circuits, namely Floquet time-evolved and variational quantum eigensolver quantum circuits, with the underlying Hamiltonian consisting of both braiding and fusion interaction. Our analysis found that there is not a uniform best method across both problems: the fusion readout method performed better on Floquet-type circuits on both the MSE and covariance-aware sampling variance, while the grouped Pauli method performed better on VQE on the MSE but worse on sampling variance. We derive scaling laws, and compute shot-budget crossover points, where one method is operationally favored above the other. The relevance of this work extends beyond Fibonacci chains to two-dimensional topological models compiled on superconducting and other qubit-native platforms, and can be used as a guide in answering the question of when one should measure in the native operator basis of the target physics, or when it is better to fall back on Pauli-basis reconstruction.
  </div>
</div>
</div>

<p align=right>(<a href=#updated-on-20260601>back to top</a>)</p>

## QC

<div class="paper-list">
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">More efficient Clifford+T synthesis for small-angle rotations and application to Trotterization</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Nick S. Blunt (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31544" target="_blank">📄 PDF: 2605.31544</a>
  </div>
  <div class="paper-comments">💬 43 pages, 12 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Clifford+T synthesis of rotation gates is an important routine in fault-tolerant quantum compilation. While Clifford+T synthesis is scalable, it has a high overhead of tens of T gates per rotation in practice, translating to high resource estimates for many fault-tolerant algorithms. However, these well-known results, including those using probabilistic mixtures [Quantum 7, 1208 (2023)], are independent of the rotation angle $θ$, requiring $O(\log 1/δ)$ T gates. We show that it is possible to do much better for small angles, reducing the T cost to $\tilde O(θ^2/δ)$, and returning to existing $O(\log1/δ)$ results in the worst case. This is particularly important since many algorithms, such as Trotterization, are dominated by small-angle rotations. Further, we perform a detailed theoretical and numerical study of quasi-probabilities, which can further reduce the total T cost of large circuits by orders of magnitude with only a small overhead in sample complexity. We also develop a scheme based on quasi-probability mixtures of Clifford+T fallback channels. We derive new $θ$-dependent formulas that can be used for resource estimation of fault-tolerant quantum algorithms. As an application of our results, we show that the gate cost of Trotterization circuits compiled to a Clifford+T gate set is constant in the small Trotter step size limit, and can be reduced by orders of magnitude even for large step sizes. The cost of fault-tolerant Trotterization for a variety of applications should be re-examined in light of these results. Our work dispels the widely-stated claim that Clifford+T rotation synthesis has a high cost independent of $θ$ , and further develops a scalable quasi-probability method for rotation synthesis. We also expect our results to bring forward useful early fault-tolerant quantum computing by reducing required magic state resources.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">(Non-)Traversable Quantum Phase Transitions</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Marin Bukov (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; cond-mat.stat-mech</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31472" target="_blank">📄 PDF: 2605.31472</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Quantum phase transitions manifest as an abrupt change in the ground state of a many-body system; yet it is an open question whether this sudden change necessarily precludes a continuous dynamical connection between the two phases. We introduce a classification of quantum phase transitions based on this geometric aspect of the ground-state manifold, that differs from known classifications. By leveraging the framework of counterdiabatic driving, we explicitly construct schedules that dynamically connect one phase to another. This strategy allows us to uncover a large class of quantum phase transitions, where the states on both sides are separated only by a finite geometric distance in the thermodynamic limit. We term such transitions traversable, since exact counterdiabatic driving links the two phases via a finite dynamical protocol in the thermodynamic limit. We show that multiple known transitions fall into this class -- e.g., symmetry-breaking transitions obeying hyperscaling and discontinuous transitions with an enhanced continuous symmetry. We further show the existence of quantum phase transitions that cannot be crossed dynamically even with the help of nonlocal counterdiabatic driving, as they would require divergent amplitudes and frequencies. Geometrically, these nontraversable transitions correspond to an infinite distance separating the two phases of matter; we show that the class comprises continuous transitions exhibiting mean-field universality, and discontinuous transitions arising from the competition between metastable minima. Our geometric classification goes beyond the known taxonomy, is independent of local order parameters and renormalization group fixed points, and has direct implications for the complexity of state preparation and adiabatic quantum computation.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Intrinsic locality dimension of quantum codes</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Zi-Wen Liu (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31441" target="_blank">📄 PDF: 2605.31441</a>
  </div>
  <div class="paper-comments">💬 36 pages, 8 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Quantum error-correcting codes are a cornerstone of quantum computing, with broad and profound connections to physics and mathematics. In this work, we introduce the notion of intrinsic locality dimension of stabilizer codes that is independent of any background geometry and naturally incorporates flexible architectures and accommodates noninteger values, drawing on mathematical machinery from fractal geometry and geometric measure theory. Important scenarios include topological codes and algebraic codes such as bivariate-bicycle-type codes. We show how the intrinsic dimension serves as a fundamental organizing parameter that unifies code properties. In particular, we prove general limitations on code parameters and compatible fault-tolerant logical gates induced by the intrinsic dimension, generalizing the Bravyi--Poulin--Terhal and Bravyi--König bounds for regular topological codes, respectively. Furthermore, we discuss implications on thermal properties, presenting a conditional no-go result for self-correcting quantum memories in dimension $3-ε$ for any $ε>0$ . Our theory lays a versatile and unifying mathematical foundation for studying the fundamental capabilities and geometric implementations of quantum error correction and fault tolerance.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Flow map learning in nonlinear vector autoregressive models: influence of the feature-library structure on the training error</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Markus Gross (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31438" target="_blank">📄 PDF: 2605.31438</a>
  </div>
  <div class="paper-comments">💬 35 pages, 12 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Time series forecasting often requires learning nonlinear and time-delayed dependencies. A paradigmatic class of forecasting models are nonlinear vector autoregressive processes (NVAR), also known as next-generation reservoir computers (NG-RCs). These models approximate the Koopman operator on the space spanned by their explicit feature library. We consider the identifiability problem for learning Markovian nonlinear dynamical systems and show that the training error as a function of time resolution follows characteristic (pre-)asymptotic scaling laws. These laws depend on whether the feature library can represent the early Lie-series coefficients of the flow map (propagator) exactly or merely approximately. For dynamical systems governed by polynomial vector fields, we demonstrate the mechanism for NVAR/NG-RC models with monomial and Fourier feature libraries. We determine the dependence of the training error on the temporal resolution, the involved nonlinear degree, and the number of delay terms. While delay terms reduce the optimal one-step training error, they improve long-horizon forecasts only when the library provides sufficient nonlinearity. Thus, small training error coexists with weak generalization as the model class is mismatched to the true data-generating process. Numerical experiments on various chaotic dynamical systems confirm the theoretical predictions.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Fidelity bounds for spin-dependent kicks with pulsed lasers</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">E. Torrontegui (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31409" target="_blank">📄 PDF: 2605.31409</a>
  </div>
  <div class="paper-comments">💬 15 pages, 6 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Excitation of trapped-ion hyperfine qubits with fast optical Raman pulses enables faster-than-trap-period entangling gates with qubits of long coherence time for practical quantum computation. Achieving high-fidelity fast two-qubit gates requires high-quality spin-dependent kicks (SDKs), which form their fundamental building blocks. Here, we characterize the control parameters (including Raman frequency difference, pulse arrival times, Lamb--Dicke parameter, temperature, pulse width, and SDK time) that maximize the performance of single-ion SDKs for protocols compatible with performed experiments involving a small number of fast pulses. We demonstrate through analytical methods and numerical simulations that, within the model commonly used for infidelity optimization, finite pulse duration is the dominant source of error, exceeding the contribution of secular motion by orders of magnitude for nanosecond-scale SDKs. Low infidelities -- below $10^{-3}$ for schemes with $\gtrsim10$ fixed-amplitude, equispaced, picosecond pulses -- are achievable in SDK times on the order of nanoseconds. These results provide quantitative design rules for achieving competitive SDK fidelities with current pulsed-laser technology, laying the foundation for sub-microsecond trapped-ion quantum entangling operations.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Sharp periodic Ge concentration modulations beyond the conduction band valley wavevector $k_0$ in nuclear spin-free Si quantum wells</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Kevin-P. Gradwohl (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">physics.app-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31358" target="_blank">📄 PDF: 2605.31358</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Periodic Ge modulations within strained Si quantum wells in SiGe heterostructures offer a route to deterministically enhance conduction-band valley splitting in Si, a key requirement for scalable spin-qubit quantum computing. Efficient enhancement requires modulations in the order of the Si valley wavevector $k_0$ (9.7 nm$^{-1}$), corresponding to a period of 0.64 nm and near-monolayer growth control.   Using nuclear-spin-free molecular beam epitaxy with $^{28}$Si and $^{72}$Ge, we demonstrate Ge-modulated Si quantum wells with periods from 2.00 to 0.49 nm, including modulations at $k_0$ and $2k_0/3$. Synchrotron X-ray techniques and scanning transmission electron microscopy reveal laterally homogeneous Ge modulations over micrometer scales, with amplitudes up to 10 at-% and gradients reaching 20 at-%/nm. Two-bands $\mathbf{k}\cdot\mathbf{p}$ simulations suggest deterministic enhancement of valley splittings in steep trapezoidal $2k_0/3$ heterostructures, while the effect in $k_0$ -type quantum wells is much weaker.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Entanglement distribution protocols under imperfect fidelity and quantum memory conditions</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Claire Goursaud (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; cs.NI</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31347" target="_blank">📄 PDF: 2605.31347</a>
  </div>
  <div class="paper-comments">💬 Presented at the Second Workshop on Workshop on Quantum Networked Applications and Protocols (QuNAP 2026), organized in conjunction with IEEE International Conference on Computer Communications, May 18, 2026</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    The rapid development of quantum computers and sensors urges for the development of a quantum Internet capable of transmitting quantum bits over long distances. Photons used for quantum data transfer are fragile over time and sensitive to their environment, so that they cannot be directly used over long distances. To remedy this problem, long distance paths are segmented into shorter links and entangled pairs of photons are distributed over these links and swapped to create end-to-end entangled pairs over long distances, eventually used for teleportation. In this paper, we develop an existing protocol taking account of fidelity and imperfect memories. We shorten the execution time and thus increase its link success probability creating the so-called Locally Heralded Distribution (LHD). It turns out that the proposed protocol outperforms some previous protocols. We benchmark through simulation the performances of protocols considered in this paper by using a blind entanglement protocol as a baseline.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Emergence of spin entanglement with the pseudogap onset in the Fermi-Hubbard model</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Karsten Held (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cond-mat.str-el; cond-mat.mtrl-sci; cond-mat.quant-gas</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31240" target="_blank">📄 PDF: 2605.31240</a>
  </div>
  <div class="paper-comments">💬 8 figures, 34 pages</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Despite decades of intense theoretical and experimental investigation, the two-dimensional Fermi-Hubbard model still resists a complete microscopic understanding. Conventional approaches typically probe global observables and locally resolved correlation functions. Here, we develop a complementary perspective based on the measurement of entanglement. Using both an ultracold-atom quantum simulator and numerical simulations based on the dynamical vertex approximation, we find that entanglement is closely tied to the onset of the enigmatic pseudogap regime: spin-singlet entanglement emerges only as the pseudogap sets in and, in contrast to classical correlations, remains confined to nearest-neighbour sites in this regime. Our results, therefore, disfavour purely classical-fluctuation theories of the pseudogap and constrain microscopic models to those that develop nearest-neighbour spin-singlet entanglement at the pseudogap onset.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Shallow Electronic State Preparation for Quantum Chemistry with Quantum Monte Carlo Pre-Selection</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Maria-Andreea Filip (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph; physics.chem-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31139" target="_blank">📄 PDF: 2605.31139</a>
  </div>
  <div class="paper-comments">💬 12 pages, 5 figures. 2 pages SI, 5 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Quantum computers hold great promise for molecular simulation, but noise remains a fundamental obstacle. We introduce a Quantum Monte Carlo (QMC) pre-screening procedure that constructs compact, physically motivated Givens rotation ansätze tailored to realistic quantum hardware. By identifying the most important wavefunction contributions early in a QMC simulation, we build circuits that are shallower that conventional alternatives while preserving number symmetry. Benchmarked on Quantinuum System Model H1, QMC-prescreened circuits outperform more complex ansätze under realistic noise conditions. The method offers a practical path toward chemical accuracy on quantum devices, by providing an adjustable trade-off between expressivity and circuit depth to generate shallow circuits suited to current high-noise devices, as well as deeper, more expressive circuits that can be deployed on future lower-noise devices.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Quantum State Preparation via Neural Network Encoding in Quantum Machine Learning</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Andre Luckow (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31006" target="_blank">📄 PDF: 2605.31006</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    A central challenge in quantum machine learning is the state preparation bottleneck that describes the prohibitive computational cost of loading high-dimensional classical data into a quantum state. Although amplitude encoding can represent $2^n$-dimensional data using only $n$ qubits in principle, preparing arbitrary states remains computationally expensive, typically requiring variational optimization of a parameterized quantum circuit for each individual data instance. In this work, we propose a method that avoids iterative optimization by training a classical neural network to map input data directly to the continuous parameters of a fixed quantum circuit. We demonstrate the generation of quantum image states with high fidelity on data not seen during training. Since all optimization is performed once during training, the resulting model encodes new inputs in a single inference step, providing a scalable pathway for data loading in near-term quantum algorithms. We validate our method on the MNIST and Fashion-MNIST datasets, achieving fidelities up to 0.992 on unseen images and reducing the per-data-instance runtime by more than 5000-fold.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Evaluating higher-order product formulae for molecular ground-state energy estimation</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Kosuke Mitarai (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30967" target="_blank">📄 PDF: 2605.30967</a>
  </div>
  <div class="paper-comments">💬 12 pages, 11 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We evaluate deterministic higher-order product formulae for molecular ground-state energy estimation. Motivated by recent fault-tolerant architectures in which non-Clifford operations may be generated more locally and cheaply than in conventional assumptions, we re-examine such formulae as practical candidates for quantum chemistry. Using one-dimensional hydrogen chains from $\mathrm{H}_2$ to $\mathrm{H}_{15}$ as benchmarks, we estimate both the total gate count and the depth of $R_Z$-rotation layers required to reach a target energy error. To make this comparison feasible at larger system sizes, we use a perturbative method to estimate the eigenvalue error induced by each product formula and thereby evaluate the cost of the corresponding phase-estimation procedure. Among the previously considered formulae, the eighth-order construction introduced by Morales et al. [M. E. S. Morales et al., "Greatly improved higher-order product formulae for quantum simulation," arXiv:2210.15817v2 (2024)] minimizes both cost metrics in the benchmark at a chemically relevant target error. We also find that increasing the formal order does not automatically reduce the total cost: near chemical accuracy, the tenth-order formula introduced in the same work can be less efficient than the eighth-order one. Motivated by this observation, we construct a new fourth-order formula; it achieves the lowest total gate count among the formulae considered for all H-chain instances near chemical accuracy and over much of the 0.1-10 mHa target-error window for most instances, while also reducing the $R_Z$ -layer depth. These results clarify how deterministic higher-order product formulae should be selected for molecular ground-state energy estimation.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">On the impact of retrieved content representations in RAG Pipelines</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Guido Zuccon (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.IR; cs.AI; cs.CL</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30790" target="_blank">📄 PDF: 2605.30790</a>
  </div>
  <div class="paper-comments">💬 23 pages, 15 figures, submitted to ACL May 2026 ARR</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Retrieval-Augmented Generation (RAG) supplements a language model's input with retrieved documents, yet most RAG pipelines inherit retrieval components designed for human readers. How retrieved content should be represented when the consumer is a large language model (LLM) rather than a human is less well understood. Recent work has proposed transformations of retrieved content and identified properties that affect generation, but each examines a single transformation or property in isolation, leaving open which features of a document's representation matter most. We address this with a controlled comparison: holding retrieval fixed, we vary only the representation of retrieved documents, comparing an original baseline against thirteen transformations spanning selection, summarisation, and reformulation, in query-dependent and query-independent variants. Across these fourteen representations we measure question-answering accuracy for four generators, and for each representation we also measure answer retention: whether a known answer-bearing document still supports its answer after transformation. We find that answer retention is the primary determinant of generator accuracy; notably, when retention is high, a representation's wording, structure, length, and query-dependence have limited effect. This suggests that accuracy gains attributed to specific mechanisms in prior work may be partly explained by how well those mechanisms preserve answer-bearing content, an attribution that cannot be settled without controlling for retention.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Real-Time Quantum Error Correction System Stack: Architecture, Algorithms, and Engineering Practice</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Dingshun Lv (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30765" target="_blank">📄 PDF: 2605.30765</a>
  </div>
  <div class="paper-comments">💬 55 pages, 10 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Quantum error correction (QEC) is transitioning from physical feasibility demonstrations to systems engineering challenges. Google has achieved below-threshold performance on distance-5/7 surface codes, while Riverlane and Rigetti have demonstrated hardware-integrated low-latency feedback loops. These milestones indicate that the core challenge of real-time decoding has shifted from algorithmic capability to system-level engineering. However, a substantial engineering gap remains between laboratory demonstrations and scalable fault-tolerant quantum computing (FTQC). This white paper addresses three questions: (1) Where are the real bottlenecks in real-time QEC: beyond average decoder speed, the constraints lie in QEC round time, tail latency, and end-to-end data path coordination; (2) How mature are mainstream decoder algorithms: we benchmark the major decoders for both surface codes and quantum low-density parity-check (qLDPC) codes, evaluating their real-time readiness; (3) What system stack do we propose: a six-layer reference architecture from syndrome acquisition to logical operations, with interface definitions and latency budget models. Our results quantify the gap between current decoder performance and real-time requirements, and identify the architectural choices needed to close it.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Mitigating Noise-Induced Barren Plateaus Using a Non-Unitary Ansatz: Application to Molecular Electronic Transport</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Michael Kolodrubetz (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30572" target="_blank">📄 PDF: 2605.30572</a>
  </div>
  <div class="paper-comments">💬 29 pages, 17 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Variational quantum algorithms (VQAs) offer a promising route toward simulating many-body quantum systems on noisy intermediate-scale quantum (NISQ) hardware. However, their scalability is severely limited by noise-induced barren plateaus (NIBPs), where hardware noise causes the gradients of the cost function to vanish exponentially with circuit depth, rendering optimization impossible. In this work, we demonstrate that introducing nonunitary elements into the variational ansatz can mitigate NIBPs in open-quantum systems. Using an analytically tractable infinite-range dissipative Ising model, we show that a nonunitary ansatz restores finite gradients in the presence of depolarizing noise, enabling convergence to the correct symmetry-broken steady state. We also develop a Floquet-type variational ansatz in which each layer repeats the same parameters, reducing the deep variational circuit to an effective quantum channel whose fixed points can be analyzed directly. We then extend these ideas to a realistic quantum-chemistry system by simulating electron transport through Oligophenylethynylene-sulfurmethyl (OPE-SMe) using Hamiltonians and jump operators of the model derived from first-principles polarizable QM/MM calculations. Our results show that nonunitary variational ansätze provide a scalable and physically grounded route for simulating open-system steady states on NISQ hardware, offering a pathway to overcoming one of the limitations of current quantum hardware.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Metasurfaces for neutral-atom trapping</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Mikhail Kats (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">physics.optics; physics.app-ph; physics.atom-ph; quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30498" target="_blank">📄 PDF: 2605.30498</a>
  </div>
  <div class="paper-comments">💬 Review article</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Trapped neutral atoms are one of the leading platforms for quantum information technologies, in particular for quantum computing, but scaling them to array sizes needed for utility-scale quantum computing is a major engineering challenge. Here we review optical metasurfaces as an enabling technology that provides fine control over the phase, amplitude, and polarization of light, with pixel counts far exceeding what is available with spatial light modulators (SLMs) and other active devices. The large pixel counts have recently led to demonstrations of arrays of optical tweezers with hundreds of thousands of sites and arrays of optical bottle-beams with complex three-dimensional trapping profiles. The flexibility and scalability of optical metasurfaces provides a route towards miniaturized, integrated, and highly scalable atomic experiments and instruments.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Improved sample complexity bound for sample-based Lindbladian simulation</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Hyukjoon Kwon (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30301" target="_blank">📄 PDF: 2605.30301</a>
  </div>
  <div class="paper-comments">💬 31 pages</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We establish improved sample-complexity bounds for sample-based Lindbladian simulation based on the Wave Matrix Lindbladization (WML) algorithm. For a jump operator $L$ with dimension $d$, we derive an explicit non-asymptotic sample complexity bound$ n_d^*(t,\varepsilon) \le \left( \frac{2d+3}{8} \right) \
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Non-Abelian Mixer for QAOA on Hybrid Oscillator-Qubit Quantum Processors</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Jianqing Liu (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30234" target="_blank">📄 PDF: 2605.30234</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    The realization of universal control in hybrid oscillator-qubit quantum processors enables the systematic design and implementation of quantum algorithms. However, the algorithmic development for such platforms remains at an early stage. While the Quantum Approximate Optimization Algorithm (QAOA) has been extensively studied in both continuous-variable (CV) and discrete-variable (DV) quantum systems, its development in the hybrid CV-DV setting remains limited. In this paper, we propose a hardware-native non-Abelian mixer for QAOA on hybrid CV-DV quantum processors and develop a corresponding hybrid ansatz for the Max-Cut problem. We evaluate the proposed ansatz on unweighted Erdős-Rényi graphs and benchmark it against the standard transverse-field mixer using the approximation ratio and optimal-solution probability. Across all graph sizes and Fock cutoffs in our simulations, the proposed non-Abelian mixer consistently improves both expected solution quality and the probability of sampling an optimal solution relative to the transverse-field mixer. These results indicate that the proposed non-Abelian mixer is a promising building block for QAOA on hybrid oscillator-qubit platforms.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Programmable Dissipation via Partial Quantum Error Correction</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Yu Zhang (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30217" target="_blank">📄 PDF: 2605.30217</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Noise is typically treated as the adversary of quantum information processing. For open quantum dynamics, however, dissipation is part of the target physics, creating a tension with fault-tolerant architectures designed to suppress decoherence. Here we show that logical noise can instead be turned into a calibrated resource. We treat the error-correction cycle as a programmable primitive: one fault-tolerant round induces a logical completely positive trace-preserving map, and decoder/recovery randomization generates a controllable family of logical channels whose convex mixtures realize Kraus-channel mixing. This enables direct compilation of target dissipators into effective logical dynamics without explicit ancilla qubits for encoding the bath degree of freedoms. We derive an accuracy criterion for multi-step simulation in which the code distance is chosen so that uncontrolled logical errors remain a small fraction of the intended dissipation per step, rather than being driven below an arbitrarily small closed-system tolerance. Partial quantum error correction thus repurposes fault-tolerant structure to sculpt dissipation, offering a resource-efficient route to quantum simulation of open quantum systems.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">End-to-End Molecular Dynamics with a Langevin Thermostat on Quantum Circuits</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Yu-ichiro Matsushita (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30143" target="_blank">📄 PDF: 2605.30143</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We construct a quantum-circuit framework for finite-temperature molecular dynamics in the canonical ensemble (NVT) with a Langevin thermostat, connecting canonical state preparation to subsequent physical-property readouts. The classical nuclear phase-space distribution is encoded as a Koopman--von Neumann (KvN) wave function, and canonical state preparation is formulated as Langevin-type Fokker--Planck relaxation. The Hamiltonian Liouville flow, momentum friction, and momentum diffusion are decomposed into separate circuit blocks. The friction block is represented by a symmetrized momentum-space dilation, whereas the diffusion block is implemented as a cosine filter realized by probabilistic imaginary-time evolution (PITE). We analytically quantify the leading-order temperature bias caused by replacing the Gaussian diffusion kernel with this PITE-realized cosine filter. This analysis yields an internal-temperature correction that targets the desired physical equilibrium distribution. As a proof-of-concept demonstration connecting quantum chemistry to KvN nuclear dynamics, we study the H $_2$ molecule. Numerical simulations show relaxation from a nonequilibrium phase-space distribution to a canonical KvN state. From this canonical state, we demonstrate two complementary readouts: a dynamical quantum-phase-estimation readout of the vibrational density of states associated with the H--H stretch coordinate and a static canonical evaluation of the transition-state-theory (TST) rate constant. This work demonstrates, in a minimal molecular system, a circuit-level protocol that connects Langevin canonical state preparation to physical-property calculations, providing a concrete step toward quantum--classical hybrid molecular dynamics on quantum computers.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Koopman--von Neumann Molecular Dynamics for Green--Kubo Transport Coefficients</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Yu-ichiro Matsushita (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">quant-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30142" target="_blank">📄 PDF: 2605.30142</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We formulate the Green--Kubo transport coefficients of classical molecular dynamics as a readout problem for quantum algorithms using the Koopman--von Neumann (KvN) representation. Both NVE and Nosé--Hoover-type NVT dynamics are derived as unitary evolutions on Hilbert spaces associated with the corresponding classical phase spaces. Numerical benchmarks on finite grids show that the discretization error in the correlation function decreases as a power law in the number of grid points $N_z$. Equivalently, with $N_z=2^{n_z}$, the error decreases exponentially in the register size $n_z$, so a target accuracy $ε$ requires $n_z=\mathcal{O}(\log(1/ε))$ qubits. To read out a transport coefficient, we input a flux-excited state to quantum phase estimation (QPE). The probability $P_0$ of measuring the QPE ancilla register in the all-zero state corresponds to a Bartlett-windowed Green--Kubo integral. With maximum-likelihood amplitude estimation, the statistical estimation of $P_0$ defined by this QPE oracle improves from the $N_{\rm queries}^{-1/2}$ scaling of direct shot sampling to scaling close to $N_{\rm queries}^{-1}$. Our circuit-resource analysis shows that one step of the NVE propagator can be built with $\mathcal{O}(n^2)$ CX gates, where $n=n_x+n_p$ is the total number of position and momentum qubits. For the NVT propagator, the centered-difference Pauli-decomposition implementation of the Nosé--Hoover friction term scales as $\mathcal{O}(n_ξn_p\,2^{n_p})$, where $n_p$ and $n_ξ$ are the numbers of momentum and thermostat qubits, respectively. The proposed framework is a concrete step toward translating the principles of quantum algorithms into the transport-coefficient calculations required in practical molecular simulation.
  </div>
</div>
</div>

<p align=right>(<a href=#updated-on-20260601>back to top</a>)</p>

## AI for science

<div class="paper-list">
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">A holomorphic neural network framework for 3D boundary value problems governed by harmonic potentials</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Tito Andriollo (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">math.NA; cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31231" target="_blank">📄 PDF: 2605.31231</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We present a neural-network-based framework for the solution of three-dimensional boundary value problems where the solution is expressible in terms of harmonic potentials. The approach leverages the Whittaker integral formula, which allows representing the solution through functions that are holomorphic with respect to a suitable complex variable. These functions are subsequently approximated using holomorphic neural networks, which guaranty fulfillment of the holomorphicity requirement. A key feature of the proposed formulation is that the governing partial differential equations (PDEs) are satisfied exactly by construction. Therefore, in contrast to standard physics-informed neural networks, no residual minimization of PDEs is required in the interior of the domain, and training is based exclusively on boundary collocation points. The method is validated against three-dimensional Laplace and linear elasticity problems, where, in the latter case, displacement and stress fields are expressed via the Papkovich-Neuber potentials. The numerical results show an accurate approximation of both scalar and vector fields, with errors remaining controlled throughout the domain. Overall, the work demonstrates that the incorporation of analytical structures into neural network architectures provides a natural and effective framework for the meshless approximation of three-dimensional boundary value problems while preserving the underlying properties of the governing equations.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Neutron Star Equation of State via Physics Informed Neural Network</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Rodrigo Negreiros (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">astro-ph.HE</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31198" target="_blank">📄 PDF: 2605.31198</a>
  </div>
  <div class="paper-comments">💬 5 pages, 4 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We present the first application, to the best of our knowledge, of Physics-Informed Neural Networks (PINNs) to the neutron star equation-of-state (EOS) inverse problem. Two interacting networks -- one representing the EOS $P(\varepsilon)$ as a continuous, non-parametric function, the other solving the Tolman-Oppenheimer-Volkoff (TOV) equations -- are trained jointly on NICER X-ray timing posteriors and pulsar mass measurements. The TOV equations enter as a mean-square ODE residual enforced via automatic differentiation at every training step, rooted in the Neural Differential Equation framework. The inferred EOS satisfies nuclear saturation properties, causality, and perturbative QCD bounds simultaneously; $χ$EFT consistency at $1$--$2\rhoz$ emerges without explicit enforcement, providing a non-trivial self-consistency check. Across $N=15$ independent training runs, we find a neutron star maximum mass $M_\mathrm{max}=2.06^{+0.07}_{-0.09}$ and radius and tidal deformability of a 1.4 $M_\odot$ star $R_{1.4}=12.85^{+0.03}_{-0.06}$~km and $Λ_{1.4}=684$, respectively, with 68\% CI, in agreement with recent Bayesian analyses. Most interestingly, the speed of sound exhibits a reproducible softening at $2$--$4\,\rhoz$ , consistent with a quark-hadron crossover.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Riemannian Diffusion Models on General Manifolds via Physics-Informed Neural Networks</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Juho Lee (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31106" target="_blank">📄 PDF: 2605.31106</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Riemannian diffusion models generalize score-based generative modeling to manifold-supported data via stochastic diffusion equations on the manifold. However, training requires sampling from and differentiating the manifold heat kernel, which is rarely available in closed form beyond a few highly symmetric manifolds. We propose a general approach that approximates the heat kernel by directly solving the manifold heat equation with a physics-informed neural network (PINN). Given an explicit manifold specification, we choose a coordinate system, derive the corresponding heat (Fokker--Planck) equation and a short-time asymptotic approximation, and then train a PINN to learn the log heat kernel. The resulting surrogate enables both forward noising (heat-kernel sampling) and conditional-score evaluation for denoising score matching. We demonstrate the method on diverse manifolds including $S^2$, $SO(3)$, $\mathrm{SPD}(n)$ , and permutation-quotiented point clouds.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Multi-Scale Separable Fourier Neural Networks for Solving High-Frequency PDEs</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Qiaolin He (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.31027" target="_blank">📄 PDF: 2605.31027</a>
  </div>
  <div class="paper-comments">💬 51 pages, 27 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We propose a novel neural network architecture, termed Multi-Scale Separable Fourier Neural Networks (MS-SFNN), for the accurate and efficient solution of linear and nonlinear high-frequency partial differential equations (PDEs). MS-SFNN exploits a separable representation: given a $d$-dimensional input, it employs $d$ independent subnetworks -- each acting on a single coordinate -- and constructs basis functions via element-wise multiplication of their outputs. The PDE solution is approximated as a linear combination of these basis functions, with coefficients determined by least squares. Critically, all network weights and biases are randomly initialized once, from a uniform distribution with unit variance, and remain fixed thereafter. To enhance expressivity, a tunable scaling factor is introduced in each subnetwork to modulate the frequency content of the resulting basis functions. Fourier features are explicitly embedded through cosine activations, endowing the method with strong spectral approximation capabilities. To mitigate the memory bottleneck associated with dense collocation in high-frequency or three-dimensional problems, we replace automatic differentiation with analytically derived basis function derivatives and develop a memory-efficient batched QR decomposition algorithm for solving large-scale least-squares systems. Numerical experiments demonstrate that MS-SFNN achieves unprecedented accuracy across a range of challenging PDEs, significantly outperforming state-of-the-art methods such as Physics-Informed Neural Networks (PINN) and Separated-Variable Spectral Neural Networks (SV-SNN).
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">PINNs Failure Modes are Overfitting</div>
    <div class="paper-date">2026-05-29</div>
  </div>
  <div class="paper-authors">Takashi Matsubara (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30910" target="_blank">📄 PDF: 2605.30910</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Physics-Informed Neural Networks (PINNs) are a common class of machine learning-based partial differential equation (PDE) solvers which train a network to represent a solution by minimizing a residual loss that encodes the PDE. Despite their successes, they are known to fail on certain simple equations, converging to an incorrect solution despite low loss. These failure modes have garnered significant attention in the literature over the past several years, motivating both architectural and optimization based solutions. By directly visualizing the residual, we show that failure modes are the result of overfitting: the loss is minimized on the collocation points, but not elsewhere. Applying regularization causes the failure modes to vanish. Finally, we extend double backpropagation over the full set of residuals, and use it to achieve state-of-the-art performance on four standard failure mode equations with up to $23\times$ fewer collocation points and a vanilla architecture.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">SubsurfaceGen: Procedural Generation of Field-Scale Earth Models and Seismic Data</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Ching-Yao Lai (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG; physics.geo-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30541" target="_blank">📄 PDF: 2605.30541</a>
  </div>
  <div class="paper-comments">💬 38 pages</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Full waveform inversion (FWI) is the gold standard for subsurface imaging, with applications from carbon sequestration to energy and mineral exploration to earthquake hazard assessment. Machine learning approaches to FWI need field-scale, geologically diverse, and physically realistic training data, but existing resources such as Marmousi, SEAM, and OpenFWI fall short on spatial extent, temporal extent, geological diversity, and physical realism. We address these limitations with SubsurfaceGen, a GPU-accelerated generator for 3D velocity models and seismic data. Along with SubsurfaceGen, we release a paired dataset of 4,276 2D velocity slices, 5 s wavefields, and 8 s shot gathers drawn from 42 realistic, field-scale 3D velocity models, each spanning 10 km x 10 km laterally and 6.19 km deep at 10 m resolution. The dataset spans six geological settings -- four built with SubsurfaceGen and two drawn from prior sources -- relevant for carbon sequestration and hydrocarbon exploration. We use this dataset to evaluate neural operators on wavefield prediction and encoder-decoders on end-to-end velocity inversion, holding out one geological setting for out-of-distribution testing. These experiments surface failure modes at field-scale and demonstrate how SubsurfaceGen and the associated dataset can impact ML-based FWI.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Neural Operator-Based Surrogate Model for CFD:Helical Coil Steam Generator in Small Modular Reactor</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Joongoo Jeon (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG; physics.flu-dyn</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30277" target="_blank">📄 PDF: 2605.30277</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Real-time thermal-hydraulic simulation is essential for digital twin (DT) technology that supports the safe and efficient operation of small modular reactors (SMRs). Computational fluid dynamics (CFD) provides high-fidelity flow analysis, but its computational cost prevents direct use in DT applications. AI-based surrogate modeling has been actively investigated to address this limitation, yet neural operator--based surrogates for CFD-level transient analysis of SMR-specific geometries have not been reported. This study presents an integrated framework that combines a reduced-order model (ROM) with neural operators, applied to the helical coil steam generator (HCSG) of the System-integrated Modular Advanced Reactor (SMART). Two ROM strategies tailored to each CFD data type were compared, an MLP-based autoencoder (AE) for unstructured mesh data and a convolutional autoencoder (CAE) for structured mesh data, and each was coupled with the deep operator network (DeepONet) to construct the latent DeepONet (L-DeepONet). The Fourier neural operator (FNO) was additionally adopted for comparison. A multi-scale technique was incorporated into both frameworks to mitigate spectral bias and improve the prediction of Kármán vortex streets developing inside the HCSG. The multi-scale L-DeepONet captured the instantaneous periodic vortex dynamics in both velocity and pressure fields, while the FNO and its multi-scale variant predicted the time-averaged mean flow and provided reliable pressure drop estimates. These complementary characteristics provide a practical model-selection guideline that links each architecture to specific DT objectives based on CFD data type and the required level of flow resolution.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">IGA-ODIL: Optimizing DIscretre robust Loss with Isogeometric Analysis to solve forward and inverse problems faster using machine learning tools</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Tomasz Służalec (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">math.NA</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30272" target="_blank">📄 PDF: 2605.30272</a>
  </div>
  <div class="paper-comments">💬 Physics-informed neural networks, Isogeometric analysis, Residual minimization, Gauss--Newton methods, Scientific machine learning, PDE-constrained optimization</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Physics-informed neural networks (PINNs) formulate the solution of partial differential equations as residual minimization problems over neural network parameterizations. Although highly flexible, optimization of PINNs using modern variants of Stochastic Gradient Descent algorithms is expensive. On the other hand, iterative computation of PINN parameterization using the Gauss-Newton method suffers from convergence difficulties, dense Jacobian structures, and poor conditioning that limit the effectiveness of second-order optimization methods. In this work, we introduce IGA-ODIL, a spline-based residual minimization framework combining ideas from Optimizing DIscrete Loss (ODIL), robust variational residual minimization, and Isogeometric Analysis (IGA). Instead of neural-network parameterizations of PINNs, the unknown solution is represented by smooth B-spline basis functions, leading to sparse structured Jacobians and efficient Gauss--Newton optimization. We also derive robust residual formulations based on weighted Gram operators, making the loss function related with the true error. The resulting systems inherit locality, sparsity, and approximation-theoretic properties of classical finite element and isogeometric methods while preserving the residual-learning philosophy of scientific machine learning. The proposed methodology is evaluated on several benchmark problems, including Poisson equations, convection-dominated advection--diffusion equations, Helmholtz problems with highly oscillatory solutions, nonlinear Allen--Cahn equations, and inverse Helmholtz parameter identification. Numerical experiments demonstrate orders-of-magnitude speedups compared with PINNs and CRVPINNs while maintaining high accuracy and robustness.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Cosmo-PINN: A Physics-Informed Neural Network for Cosmological Reconstruction</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Andronikos Paliathanasis (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">astro-ph.CO; gr-qc</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30139" target="_blank">📄 PDF: 2605.30139</a>
  </div>
  <div class="paper-comments">💬 17 pages, 10 figures, comments are welcome</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We introduce Cosmo-PINN, a Physics-Informed Neural Network for reconstruction of the cosmological theory. In this work we demonstrate the application of the Cosmo-PINN in the reconstruction of the dark energy equation of state parameter $w_{DE}\left( z\right) $ directly from late-time cosmological observations. This framework overcomes the main limitation shared by Gaussian Process and Artificial Neural Network reconstruction approaches, where the recovered solution is driven by the data and it is not necessarily true that it is physically consistent, by embedding the cosmological constraints directly into the loss function as hard constraints, ensuring that the reconstructed quantities satisfy the physical laws at every point during the training. For the training of the network, we employed background data, and specifically the Baryon Acoustic Oscillation from DESI DR2, the Cosmic Chronometers and three different Supernova compilations, while we simultaneously introduce the cosmological parameters $H_{0},~Ω_{m0}$ and $r_{\mathrm{drag}}$ as trained parameters. The reconstruction shows that the trained $w_{DE}\left( z\right) $ crosses the phantom divide within the redshift range $z=0.27-0.42$ in agreement with the value obtained by the Chevallier-Polarski-Linder model. In the quintessence scenario, for large redshifts the dark energy $Ω_{DE}\left( z\right)$ provides a pressureless nonzero contribution to the cosmological fluid suggesting a unified scenario. Finally, we demonstrate the significance of imposing the physical constraints within the loss function by comparing the Cosmo-PINN reconstruction against a purely data-driven neural network with the same architecture.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Striding Across Reynolds Numbers: Representation Geometry in Neural PDE Generalisation</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Jianing Shi (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.30112" target="_blank">📄 PDF: 2605.30112</a>
  </div>
  <div class="paper-comments">💬 12 pages, 8 figures, 5 tables</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Cross-Reynolds generalisation in neural PDE solvers remains poorly characterised. On the canonical forced 2D Navier-Stokes benchmark, a trained Fourier Neural Operator reaches 46.68% relative L2 error under a 10x Reynolds-number shift, yet zero-forward-model retrieval baselines already improve to 41-42%. This suggests representation geometry as a major organising variable among the tested methods. We test this hypothesis through ConvAE-Relay, which matches states in a source-trained convolutional autoencoder latent space and borrows dynamics from a source-regime database, achieving 38.34+/-0.07% using only a source-regime database and no target-regime fitting, labels, or database entries. A 2x2 ablation isolates matching quality as dominant over the update rule. Oracle experiments confirm that source-regime dynamics directions remain transferable (cosine similarity ~0.84) when matching stays on-manifold; autoregressive drift is the primary bottleneck (~12 percentage points). From the learned-prediction side, a U-Net with multi-scale skip connections achieves 34.72+/-0.60%, consistent with the retrieval-side finding that local, multi-scale representations organise cross-Reynolds transfer among tested methods. All claims are scoped to this benchmark.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">A Novel Tensor Product-Based Neural Network for Solving Partial Differential Equations</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Shiquan Zhang (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.29688" target="_blank">📄 PDF: 2605.29688</a>
  </div>
  <div class="paper-comments">💬 44 pages, 11 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    This paper presents the Tensor Product Network (TPNet), a novel neural architecture for efficient and accurate function approximation and PDE solving. The core of the proposal involves constructing the solution explicitly as a linear combination of basis functions integrated into the network, with coefficients determined by a direct least-squares solve, thereby bypassing traditional gradient-based training. The key methodological contribution include: (1) an efficient tensor-product scheme that generates multi-dimensional basis functions from combinations of two sets of subnetwork outputs, significantly reducing model complexity and parameter count while maintaining expressivity; (2) a block time-marching strategy to improve computational efficiency in long-time simulations; and (3) a linear reformulation strategy for handling nonlinear PDEs by treating known nonlinear terms as sources. TPNet achieves superior accuracy and shorter training times than conventional neural network solvers. This performance gain stems from its structured design and deterministic least-squares fitting, which contrast with the iterative, often computationally intensive optimization required by mainstream methods like Physics-Informed Neural Networks (PINNs).
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Deep Adaptive Dimension Reduction for Bayesian Inference in Inverse Problems</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Chao Yang (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG; math.NA</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.29373" target="_blank">📄 PDF: 2605.29373</a>
  </div>
  <div class="paper-comments">💬 25 pages, 5 figures</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Solving high-dimensional PDE-governed inverse problems is often challenging due to complex non-Gaussian posterior distributions, expensive forward model evaluations, and misspecified prior information. To address these issues, we propose a deep adaptive dimension-reduction Bayesian inference framework based on the Variational Flow (VF) model. Since standard normalizing flows are restricted by bijective mappings and cannot directly reduce dimensions, VF overcomes this limitation by integrating VAE-based nonlinear dimension reduction with dual normalizing flows for the latent prior and encoder. This design provides a strictly higher evidence lower bound than VAE and allows more flexible approximation of complex posterior distributions. We further introduce an iterative prior updating strategy that gradually moves the prior mean toward high-probability posterior regions, avoiding manual prior tuning. These components form a closed adaptive loop together with an adaptively fine-tuned Fourier Neural Operator (FNO) surrogate: VF generates posterior-concentrated samples to refine the surrogate, while the updated surrogate further improves posterior inference. Numerical experiments on a 100-dimensional Rosenbrock problem and three standard PDE-governed inverse problems show that our method delivers competitive or superior accuracy compared with MCMC, UKI, and SVGD baselines across all tested configurations, with the most pronounced advantages emerging in challenging scenarios such as high-noise observations and high-dimensional parameter spaces.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Tail observability and fourth-order closure recovery in physics-informed neural networks for Bhatnagar-Gross-Krook normal shocks</div>
    <div class="paper-date">2026-05-28</div>
  </div>
  <div class="paper-authors">Ehsan Roohi (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">physics.flu-dyn</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.29211" target="_blank">📄 PDF: 2605.29211</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Closure-level accuracy in neural kinetic shock solvers is not guaranteed by accurate density, velocity and temperature profiles, because the relevant observables are velocity-weighted projections of the nonequilibrium distribution. We study this observability problem for one-dimensional Bhatnagar--Gross--Krook (BGK) shock waves using a positive macro--micro physics-informed neural network (PINN) in which the distribution is represented as a local Maxwellian multiplied by a bounded exponential correction. Independent discrete-velocity method (DVM) references are used for validation. Shock-tube tests show that sparse joint anchoring of heat flux and normal stress stabilises the primary nonequilibrium layer, whereas residual-only, macro-only and single-moment variants fail in distinct ways. In a stationary Mach-2 normal shock, a flux-locked compact model recovers $ρ$, $u_x$, $T$, $q_x$, $σ_{xx}$ and $m_{xxx}^{cl}$, but leaves $R_{xx}^{cl}$ with order-unity error. DVM diagnostics show that $R_{xx}^{cl}$ is controlled by a sign-changing, tail-weighted cancellation weakly observed by lower moments. A shock-local closure correction aligned with this missing projection reduces the relative $R_{xx}^{cl}$ error to $1.12\times10^{-1}$ while preserving the lower moments. A common-initialisation ablation shows that optional distribution-function probe losses are diagnostic rather than constitutive. A supplementary DVM--PINN comparison for the scalar fourth-order excess $Δ$ shows that the obstruction is anisotropic, sign-changing tail weighting rather than fourth-order polynomial degree alone.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Unveiling Multi-regime Patterns in SciML: Distinct Failure Modes and Regime-specific Optimization</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Yaoqing Yang (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG; cs.AI; physics.comp-ph</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.29153" target="_blank">📄 PDF: 2605.29153</a>
  </div>
  <div class="paper-comments">💬 Accepted by ICML 2026</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Neural networks trained under different hyperparameter settings can fall into distinct training "regimes," with consistent behavior within regimes and qualitative differences across regimes. In this paper, we study such multi-regime behavior in scientific machine learning (SciML) models through a regime-aware diagnostic framework that jointly analyzes performance, training dynamics, and loss-landscape geometry. We identify three key findings: (i) a consistent three-regime structure emerges across many standard SciML models, different constraint enforcements, and various optimizer designs; (ii) optimization effectiveness is regime-specific, with no single method performing well across all regimes; and (iii) SciML models can exhibit fine-grained failure modes that can challenge conventional interpretations of standard loss-landscape metrics. Our results provide an approach to establish a unified, task-oblivious perspective on failure modes in SciML and to inform regime-aware guidance for improving robustness. We validate these findings across widely-used SciML models, including physics-informed neural networks, neural operators, and neural ordinary differential equations, on benchmarks spanning representative ordinary and partial differential equations.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Sequential Physics-Constrained Neural Operator Forward Modeling for the $\textit{Norne}$ Reservoir System</div>
    <div class="paper-date">2026-05-27</div>
  </div>
  <div class="paper-authors">Issam Said (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.28909" target="_blank">📄 PDF: 2605.28909</a>
  </div>
  <div class="paper-comments">💬 22 pages, 2 figures, 2 tables. Code available at https://github.com/clementetienam/physicsnemo/tree/801a85bc08aa9caa0d54027a145b88c68e5e5f36/examples/reservoir_simulation/norne</div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    We develop a comprehensive mathematical and computational framework for sequential surrogate modeling of three-phase black-oil reservoir dynamics using neural operators, with particular emphasis on Fourier Neural Operators (FNO) and their physics-informed variant (PINO). The application focus is the Norne benchmark reservoir, defined on a heterogeneous $46\times112\times22$ grid ($N=113,344$ cells), with a production history spanning $T=30$ timesteps covering 3298 days. Our theoretical contributions are organized around four interlocking problems: (1) functional-analytic formulation in a product-Sobolev-space setting, including well-posedness of the implicit timestep map and sharp local Lipschitz estimates; (2) covariate shift quantification, proving that the Wasserstein-2 distance grows as $W_2 \leq \varepsilon(L^n-1)/(L-1)$, with exponential population-risk discrepancy for $L>1$; (3) physics-constrained spectral stability, showing PINO training with $λ_R \geq λ^*_R$ reduces the learned Jacobian spectral radius to $ρ_F + Cλ_R^{-1/2}$, yielding uniform-in-time rollout error$
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">Faster Thermal Profiling of a Lunar Rover with Machine Learning Adapted Finite Difference Model</div>
    <div class="paper-date">2026-05-26</div>
  </div>
  <div class="paper-authors">Souma Chowdhury (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.27651" target="_blank">📄 PDF: 2605.27651</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Autonomous space systems operating in extreme thermal environments require accurate and efficient thermal modeling to support both pre-mission system design and onboard autonomy. For lunar rovers, large temperature gradients, radiative heat transfer, and variable surface conditions make reliable thermal prediction especially challenging. High-fidelity physics-based simulations provide accurate results but are computationally expensive, while simplified models and lookup-table approach often lack sufficient accuracy. Physics-informed machine learning (PIML) offers a promising alternative by combining data-driven models with embedded physical knowledge. This paper presents a PIML framework for thermal analysis of a simplified lunar rover with internal heat sources, where machine learning enables environment-adaptive coarse meshing. The proposed architecture integrates a transfer neural network (TNN) that adaptively determines 3D finite-difference nodalization based on thermal loads and initial conditions, enabling more accurate coarse-mesh calculations. A differentiable finite-difference thermal simulator is embedded within the framework to enforce physical consistency and support efficient training, while an upscaling layer reconstructs high-resolution temperature fields from the coarse-grid solution. The proposed PIML approach is evaluated against high-fidelity fine-mesh simulations, low-fidelity fixed coarse-mesh models, and a purely data-driven artificial neural network (ANN). Results show that the PIML framework improves prediction accuracy by 50% and 39% relative to the coarse-mesh physics model and ANN model, respectively, while maintaining physically consistent thermal distributions. Computationally, the framework is also 3x faster than high-fidelity simulations, demonstrating an effective balance between accuracy and efficiency for thermal modeling of lunar rover systems.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">From Centerlines to Hemodynamics: Anisotropic RBF Decoders for Coronary Arteries</div>
    <div class="paper-date">2026-05-26</div>
  </div>
  <div class="paper-authors">Maziar Raissi (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.CE</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.27578" target="_blank">📄 PDF: 2605.27578</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Accurate and rapid estimation of hemodynamic metrics, such as pressure and wall shear stress (WSS), is important for assessing the severity of Coronary Artery Disease (CAD). Existing approaches, including invasive Fractional Flow Reserve (FFR) measurements and computationally expensive Computational Fluid Dynamics (CFD) simulations, face challenges in invasiveness, cost, and speed. We present a framework for fast, non-invasive coronary hemodynamics prediction. The model encodes 1D vessel centerlines together with inlet flow rate using a transformer-based encoder, and predicts continuous wall-based fields via an anisotropic Radial Basis Function (RBF) decoder aligned with vessel morphology. To support training and evaluation, we introduce two datasets with paired steady-state OpenFOAM simulations: (i) a synthetic benchmark of 4,200 single-vessel geometries with controlled anatomical variations, and (ii) a multi-vessel dataset derived from ImageCAS including 4,800 cases spanning both right and left coronary arteries, generated by randomly introducing stenoses and varying physiologically plausible flow rates. Across both datasets, our method achieves lower pressure and WSS errors than strong neural-operator baselines (GNOT, Transolver, and ONO) at a fraction of the computational cost of CFD. On the multi-vessel dataset, using 1,024 anisotropic RBF centers our model reduces the mean relative L2 error by 52% compared to the best neural-operator baseline, while at 128 centers it requires 13.8x fewer FLOPs than GNOT and still outperforms all baselines. The single-vessel dataset is publicly available at https://huggingface.co/datasets/angioinsight/single-vessel-flow.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">PINNsur: Physics-Informed Neural Networks for PDEs on Curved Surfaces</div>
    <div class="paper-date">2026-05-26</div>
  </div>
  <div class="paper-authors">Oded Stein (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.GR; math.NA</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.27308" target="_blank">📄 PDF: 2605.27308</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Partial differential equations (PDEs) on surfaces are fundamental to scientific computing and geometry processing. A popular approach to solving PDEs on surfaces is the finite element method (FEM), where the surface is divided into discrete geometric elements (usually triangles). Recently, physics-informed neural networks (PINNs) have emerged as a continuous, mesh-free alternative that does not suffer from FEM's sensitivity to mesh quality or geometric discretization errors. We present PINNSur, a simple framework for using PINNs on curved surfaces: we train a neural field to approximate the surface's normals, and then we express surface differential operators using their projection from $\mathbb{R}^3$ onto the surface. Since every orientable manifold has well-defined normals, our method is suitable for all such surfaces, regardless of curvature or topology, enabling many geometry processing applications. Moreover, despite their empirical success in solving PDEs in flat Euclidean domains, PINNs lack convergence guarantees to the true solution of the underlying PDE, and there is limited systematic experimental evidence demonstrating such convergence. This gap restricts their adoption as reliable solvers compared to established methods like FEM, where convergence to the true solution is well understood and theoretically grounded. These surface PDEs are particularly challenging to solve convergently, as one must not only deal with the convergence of the function approximation, but also with the convergence of the geometric approximation of the surface itself. In this work, we empirically investigate the convergence behavior of PINNs for solving surface PDEs by introducing a simple empirical convergence test.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-odd">
  <div class="paper-header">
    <div class="paper-title">Predictive Moving Sample Method for Physics-Informed Neural Solvers of Time-Dependent PDEs</div>
    <div class="paper-date">2026-05-26</div>
  </div>
  <div class="paper-authors">Jiayu Zhai (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">math.NA</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.26745" target="_blank">📄 PDF: 2605.26745</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Time-dependent partial differential equations (PDEs) often develop sharp fronts, localized peaks, and other moving structures that occupy only a small portion of the space--time domain but dominate the approximation error. This makes fixed or uniformly sampled collocation strategies inefficient for physics-informed neural networks (PINNs), especially in high dimensions and over long-time prediction intervals. We propose the predictive moving sample method (PMSM), which builds on the moving sample method (MSM) in \cite{xu2026moving} by replacing its full time domain iterative training with a progressive time-stepping strategy and simplifying the velocity-field loss to further reduce the per-step cost. To improve practicality for long-time prediction, we further introduce the windowed-reset predictive moving sample method (WR-PMSM), which restricts extension training to an active time window and periodically resets the reference state, thereby reducing the growth of optimization cost while preserving global consistency through a final refinement stage. Across four representative benchmarks, PMSM consistently outperforms both standard PINNs and the original MSM under matched collocation budgets. These results suggest that transporting samples according to residual dynamics provides an effective and practical route to neural network solvers for time-dependent PDEs.
  </div>
</div>
<div style="height: 10px;"></div>
<div class="paper-item paper-item-even">
  <div class="paper-header">
    <div class="paper-title">APEX: Amplitude Anchors and Phase Priors for Target-Scarce Higher-Frequency Wave Prediction</div>
    <div class="paper-date">2026-05-26</div>
  </div>
  <div class="paper-authors">Shikai Fang (last author)</div>
  <div class="paper-meta">
    <span class="paper-categories">cs.LG</span>
    <a class="paper-link" href="https://arxiv.org/abs/2605.26732" target="_blank">📄 PDF: 2605.26732</a>
  </div>
  <div class="paper-abstract">
    <div class="abstract-label">📖 Abstract:</div>
    Learning-based surrogates have become increasingly effective for wave-field prediction, and neural operators in particular have shown strong performance within observed frequency regimes. However, higher-frequency prediction under scarce target supervision remains comparatively underexplored, especially in wave problems where higher-frequency data are substantially more expensive to simulate or measure than lower-frequency data. A central difficulty is that cross-frequency transfer is inherently asymmetric: coarse amplitude structure remains relatively stable across frequencies, whereas phase-sensitive oscillatory structure deteriorates much more rapidly as frequency increases. Motivated by this asymmetry, we propose APEX, Amplitude-anchored and Phase-prior-guided Enhancement from eXtrapolated coarse predictions, a framework for target-scarce higher-frequency wave-field prediction. A lower-frequency neural operator first provides a coarse prediction in the target-frequency regime, from which we retain only the amplitude as a transferable structural anchor. A conditional flow-matching enhancer then reconstructs the target higher-frequency field under the guidance of a Green's-function-inspired phase prior. Experiments on SimpleWave, Helmholtz, and Maxwell benchmarks show that APEX consistently outperforms direct lower-to-higher extrapolation, target-adapted operator, and joint generative baselines under limited target-frequency supervision. Our results suggest that reliable higher-frequency prediction of oscillatory wave fields should not rely on direct end-to-end transfer of the full complex field, but instead on explicitly reusing transferable coarse structure while separately recovering the missing oscillatory detail.
  </div>
</div>
</div>

<p align=right>(<a href=#updated-on-20260601>back to top</a>)</p>

