---
title: "Software & Projects"
date: 2026-02-09T15:20:00+09:00
draft: false
toc: false
---

Open-source software and research projects by Tae-Geun Kim (Axect).

-----

## 🚀 Active Projects

### Peroxide

{{<center>}}
**Rust numerical computing library**
![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Peroxide?style=flat-square) ![Crates.io](https://img.shields.io/crates/v/peroxide?style=flat-square) ![Downloads](https://img.shields.io/crates/d/peroxide?style=flat-square)
{{</center>}}

Comprehensive numerical computing library for Rust, providing functionality comparable to NumPy/SciPy in Python. Core infrastructure for scientific computing research.

**Key Features:**
* Linear algebra with BLAS/LAPACK integration
* Optimization algorithms (Gradient Descent, Levenberg-Marquardt, etc.)
* Numerical integration & ODE/PDE solvers
* Statistical distributions & special functions
* DataFrame with multiple I/O formats (CSV, NetCDF, JSON, Parquet)
* FFI support for C, Fortran, and Python

**Tech Stack:** SIMD, BLAS, LAPACK, proc-macro metaprogramming

**Quick Install:**
```bash
cargo add peroxide
```

**Links:** [GitHub](https://github.com/Axect/Peroxide) | [Crates.io](https://crates.io/crates/peroxide) | [Documentation](https://peroxide.surge.sh)

-----

### Radient

{{<center>}}
**Rust automatic differentiation library**
![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Radient?style=flat-square) ![Version](https://img.shields.io/crates/v/radient?style=flat-square) ![Downloads](https://img.shields.io/crates/d/radient?style=flat-square)
{{</center>}}

Experimental reverse-mode automatic differentiation library with arena-based memory management for research and prototyping.

**Key Features:**
* Efficient reverse-mode AD with tape-based gradient computation
* Arena allocation for memory safety and performance
* Integration with Peroxide for scientific computing workflows

**Quick Install:**
```bash
cargo add radient
```

**Links:** [GitHub](https://github.com/Axect/Radient) | [Crates.io](https://crates.io/crates/radient) | [Documentation](https://docs.rs/radient)

-----

### DeeLeMa

{{<center>}}
**Deep Learning for Mass Estimation**
![Python](https://img.shields.io/badge/Python-3572A5?style=flat-square&logo=python&logoColor=white) ![Paper](https://img.shields.io/badge/PRR-Published-success?style=flat-square)
{{</center>}}

Deep learning framework for particle physics mass estimation using missing information search. Published in **Physical Review Research**.

**Research Impact:**
* Paper: [Phys. Rev. Research **5**, 043186 (2023)](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.043186)
* Preprint: [arXiv:2212.12836](https://arxiv.org/abs/2212.12836)

**Tech Stack:** PyTorch, PyTorch Lightning, Wandb (hyperparameter tuning), Tensorboard

**Links:** [GitHub](https://github.com/Yonsei-HEP-COSMO/DeeLeMa) | [Paper](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.043186) | [arXiv](https://arxiv.org/abs/2212.12836)

-----

### Neural Hamilton

{{<center>}}
**Can AI Understand Hamiltonian Mechanics?**
![Python](https://img.shields.io/badge/Python-3572A5?style=flat-square&logo=python&logoColor=white) ![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Neural_Hamilton?style=flat-square) ![Paper](https://img.shields.io/badge/arXiv-2410.20951-b31b1b?style=flat-square)
{{</center>}}

Official implementation of operator learning for Hamiltonian mechanics. Explores whether AI can truly understand physical dynamics through four neural architectures (DeepONet, TraONet, VaRONet, MambONet).

**Research Impact:**
* Paper: [arXiv:2410.20951](https://arxiv.org/abs/2410.20951) - Tae-Geun Kim, Seong Chan Park (2024)
* MambONet consistently outperformed RK4 solvers and competing architectures

**Key Features:**
* Novel algorithm for generating physically plausible potentials using Gaussian Random Fields
* Four neural network architectures for operator learning
* Multi-language implementation (Python, Rust, Julia)
* CUDA-compatible for GPU acceleration

**Tech Stack:** PyTorch, CUDA, Rust (numerical backend), Julia (visualization)

**Links:** [GitHub](https://github.com/Axect/Neural_Hamilton) | [arXiv](https://arxiv.org/abs/2410.20951)

-----

### PyTorch Template

{{<center>}}
**Flexible PyTorch template for ML experiments**
![Python](https://img.shields.io/badge/Python-3572A5?style=flat-square&logo=python&logoColor=white) ![Stars](https://img.shields.io/github/stars/Axect/pytorch_template?style=flat-square)
{{</center>}}

Modular PyTorch project template designed for reproducible machine learning experiments with YAML-based configuration.

**Key Features:**
* YAML-based experiment configuration for easy setup
* Multiple random seed support for robust experimentation
* Device selection (CPU/GPU) and learning rate scheduling
* Clean modular structure for extensibility

**Links:** [GitHub](https://github.com/Axect/pytorch_template)

-----

### Quantum Algorithms

{{<center>}}
**Quantum computing algorithm implementations**
![Quantum](https://img.shields.io/badge/Quantum-6929C4?style=flat-square&logo=qiskit&logoColor=white) ![Stars](https://img.shields.io/github/stars/Axect/QuantumAlgorithms?style=flat-square)
{{</center>}}

Comprehensive collection of quantum algorithms implemented in multiple frameworks (Pennylane, RustQIP, Qiskit, Cirq) with interactive Jupyter notebooks.

**Tech Stack:** Pennylane, RustQIP, Qiskit, Cirq, Jupyter

**Links:** [GitHub](https://github.com/Axect/QuantumAlgorithms)

-----

### Puruspe

{{<center>}}
**Pure Rust special functions library**
![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Puruspe?style=flat-square) ![Version](https://img.shields.io/crates/v/puruspe?style=flat-square) ![Downloads](https://img.shields.io/crates/d/puruspe?style=flat-square)
{{</center>}}

Pure Rust implementation of mathematical special functions (Bessel, Gamma, Error functions, etc.) for scientific computing.

**Quick Install:**
```bash
cargo add puruspe
```

**Links:** [GitHub](https://github.com/Axect/Puruspe) | [Crates.io](https://crates.io/crates/puruspe) | [Documentation](https://docs.rs/puruspe)

-----

### Forger

{{<center>}}
**Rust reinforcement learning library**
![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Forger?style=flat-square) ![Version](https://img.shields.io/crates/v/forger?style=flat-square) ![Downloads](https://img.shields.io/crates/d/forger?style=flat-square)
{{</center>}}

Reinforcement learning algorithms implemented in Rust for research and education.

**Algorithms:** Monte Carlo, Temporal Difference, Q-Learning

**Quick Install:**
```bash
cargo add forger
```

**Links:** [GitHub](https://github.com/Axect/Forger) | [Crates.io](https://crates.io/crates/forger) | [Documentation](https://docs.rs/forger)

-----

## 📦 Archived Projects

<details>
<summary><strong>Click to expand archived/experimental projects</strong></summary>

### NCDataFrame.jl
Julia netCDF I/O with DataFrame integration (Archived).
**Links:** [GitHub](https://github.com/Axect/NCDataFrame.jl) | [JuliaHub](https://juliahub.com/ui/Packages/NCDataFrame/zhMPT/)

### ZelLayGen
Zellij layout generator written in Rust.
**Links:** [GitHub](https://github.com/Axect/Zellaygen)

### Puruda
Pure Rust DataFrame library (superseded by Peroxide's DataFrame module).
**Links:** [GitHub](https://github.com/Axect/Puruda) | [Crates.io](https://crates.io/crates/puruda)

### HNumeric
Numerical library for Haskell.
**Links:** [GitHub](https://github.com/Axect/HNumeric) | [Hackage](https://hackage.haskell.org/package/HNumeric)

### DNumeric
Numerical library for D programming language.
**Links:** [GitHub](https://github.com/Axect/DNumeric) | [DUB](https://code.dlang.org/packages/dnumeric)

</details>

-----

## 💬 Collaboration

Interested in using these libraries or collaborating on research? Feel free to:
* Open issues or PRs on GitHub
* Reach out via [email](mailto:axect.tg@proton.me)
* Connect on [LinkedIn](https://www.linkedin.com/in/tae-geun-kim/)

All active projects welcome contributions!
