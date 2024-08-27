---
title: "About"
date: 2023-11-06T19:03:00+09:00
draft: false
toc: false
---

[**김태근 (Axect)**](https://github.com/Axect)을 소개합니다.

-----

## 저는

수학, 물리학 그리고 프로그래밍을 좋아하는 대학원생입니다.

-----

## 학력

* M.S. & Ph.D. Integrated: 연세대학교 대학원 물리학과 (2017 ~ )
* B.S.: 연세대학교 천문우주학과 (2012 ~ 2017)

-----

## 연구분야

* 천체입자물리
* 암흑물질 및 BSM
* 과학계산 및 기계학습

-----

## 학문 및 기술

### 수학

* 함수해석학
* 수치해석학
  * 유한차분법
  * 유한요소법
* 미분기하학
* 위상수학

### 물리학

* 천체입자물리학
* 일반상대성이론
* 양자장이론
* 수리물리학

### 기계학습

* 통계적 기계학습
  * 선형회귀 (LASSO, Ridge)
  * 로지스틱 회귀
  * 선형분류
  * Kernel Based Methods
    * Kernel Smoothing
    * Kernel Density Estimation
* 인공신경망
  * MLP, CNN, RNN (LSTM, GRU), Transformer, Mamba
  * Operator learning & Nerual ODE
  * Bayesian Neural Network

### 프로그래밍

* 주 언어
  * Rust, Julia, Python
* 보조 언어
  * C/C++, Haskell
* 프레임워크 및 라이브러리
  * 수치 계산
    * peroxide, BLAS, LAPACK, numpy, scipy
  * 시각화
    * matplotlib, vegas, ggplot2, plotly
  * 웹
    * Django, Vue, Firebase, Surge, Hugo, Zola
  * 머신러닝
    * PyTorch, JAX, Optax, Equinox, Wandb, Optuna, Candle, Tensorflow, Norse

-----

## 프로젝트

* **Peroxide**: Rust 수치 계산 라이브러리 (Maintainer)
  * 링크
    * [Github](https://github.com/Axect/Peroxide)
    * [Crates](https://crates.io/crates/peroxide)
    * [Docs](https://peroxide.surge.sh)
  * 사용 기술
    * Vectorization: SIMD, BLAS, LAPACK
    * FFI: C, Fortran, Python
    * Data structures: Dataframe
    * IO: csv, netcdf, json, parquet, serde
    * Meta-programming: `proc-macro`

* **Puruspe**: 순수 Rust Special function 라이브러리 (Maintainer)
  * 링크
    * [Github](https://github.com/Axect/Puruspe)
    * [Crates](https://crates.io/crates/puruspe)
    * [Docs](https://docs.rs/puruspe)

* **Radient**: Rust 자동미분 라이브러리 (Maintainer)
  * 링크
    * [Github](https://github.com/Axect/Radient)
    * [Crates](https://crates.io/crates/radient)
    * [Docs](https://docs.rs/radient)
  * 사용기술
    * Reverse mode automatic differentiation
    * Arena based memory management

* **Forger**: Rust 강화학습 라이브러리 (Maintainer)
  * 링크
    * [Github](https://github.com/Axect/Forger)
    * [Crates](https://crates.io/crates/forger)
    * [Docs](https://docs.rs/forger)
  * 사용기술
    * Reinforcement Learning
      * Monte Carlo
      * Temporal Difference
      * Q-Learning

* **DeeLeMa**: Deep Learning for Mass estimation (Maintainer)
  * 링크
    * [Github](https://github.com/Yonsei-HEP-COSMO/DeeLeMa)
    * [ArXiv](https://arxiv.org/abs/2212.12836)
    * [PRR](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.043186)
  * 사용기술
    * Deep Learning Framework: PyTorch, PyTorch Lightning
    * Hyperparameter Optimization: Wandb-sweep
    * Monitoring: Wandb, Tensorboard
    * Package Management: PDM

* ZelLayGen: Zellij Layout Generator (Maintainer)
  * 링크
    * [Github](https://github.com/Axect/Zellaygen)
  * 사용기술
    * Language: Rust
    * Serialization & Deserialization: Serde
    * Data format: TOML, KDL

* **NCDataFrame.jl**: Julia에서 DataFrame으로 netCDF I/O를 구현한 라이브러리 (Maintainer)
  * 링크
    * [Github](https://github.com/Axect/NCDataFrame.jl)
    * [JuliaHub](https://juliahub.com/ui/Packages/NCDataFrame/zhMPT/)
    * [Docs](https://juliahub.com/docs/NCDataFrame/zhMPT)

* **Puruda**: Pure Rust Dataframe library (Archived)
  * 링크
    * [Github](https://github.com/Axect/Puruda)
    * [Crates](https://crates.io/crates/puruda)
  * 사용기술
    * Meta-programming: `proc-macro`
    * IO: csv, netcdf

* **HNumeric**: Haskell 수치 계산 라이브러리 (Archived)
  * 링크
    * [Github](https://github.com/Axect/HNumeric)
    * [Hackage](https://hackage.haskell.org/package/HNumeric)

* **DNumeric**: D 수치 계산 라이브러리 (Archived)
  * 링크
    * [Github](https://github.com/Axect/DNumeric)
    * [DUB](https://code.dlang.org/packages/dnumeric)

-----

## 학술활동

### 논문

* {{<emph "Tae-Geun Kim">}}, *HyperbolicLR: Epoch insensitive learning rate scheduler*, [arXiv:2407.15200](https://arxiv.org/abs/2407.15200) (2024)

* Chang Min Hyun, {{<emph "Tae-Geun Kim">}}, and Kyounghun Lee, *Unsupervised sequence-to-sequence learning for automatic signal quality assessment in multi-channel electrical impedance-based hemodynamic monitoring*, [CMPB 108079](https://doi.org/10.1016/j.cmpb.2024.108079), [arXiv:2305.09368](https://arxiv.org/abs/2305.09368) (2023)

* Kayoung Ban, Dong Woo Kang, {{<emph "Tae-Geun Kim">}}, Seong Chan Park and Yeji Park, *DeeLeMa : Missing information search with Deep Learning for Mass estimation*, [Phys. Rev. Research **5**, 043186](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.043186), [arXiv:2212.12836](https://arxiv.org/abs/2212.12836)  (2022)

* Yongsoo Jho, {{<emph "Tae-Geun Kim">}}, Jong-Chul Park, Seong Chan Park and Yeji Park, *Axions from Primordial Black Holes*, [arXiv:2212.11977](https://arxiv.org/abs/2212.11977) (2022)

### 발표

* {{<emph "Tae-Geun Kim">}}, [*Exploration of Primordial Black Holes and Axion-Like Particles through a novel decay model on cosmological scale*](https://www.dropbox.com/scl/fi/q79z6wwwxrshj88gw5y3k/SI2023_TGKim.pdf?rlkey=jv0ypybbi8175rju495a1k0xt&dl=0), 27th International Summer Institute on Phenomenology of Elementary Particle Physics and Cosmology (2023) [Poster]

* {{<emph "Tae-Geun Kim">}}, [*Constraining ALPs via PBH with time-varying decay process*](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_WPDC.html), Workshop on Physics of Dark Cosmos: dark matter, dark energy, and all (2022) [Oral]

* {{<emph "Tae-Geun Kim">}}, [*Constraining ALPs via PBH with time-varying decay process Part.2*](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_kps.html), 2022년 한국물리학회 창립 70주년 가을 학술논문발표회 (2022) [Oral] [Best Oral Award]

* {{<emph "Tae-Geun Kim">}}, [*Bird's eye view of Neutron star cooling*](https://axect.github.io/Slides/PHY/NS/neutron-saga.html), 16th Saga-Yonsei Joint Workshop (2019) [Oral]

-----

## 읽은 책들

### 수학

* 선형대수학
  * Mark S, Gockenbach, *Finite-Dimensional Linear Algebra*. 1st ed., CRC Press (2010)
* 해석학
  * Walter Rudin, *Principles of Mathematical Analysis*. 3rd ed., McGraw Hill (1976)
  * Elias M. Stein, Rami Shakarchi, *Fourier Analysis: An Introduction*. Illustrated ed., Princeton University Press (2003)
  * Elias M. Stein, Rami Shakarchi, *Real Analysis: Measure Theory, Integration, and Hilbert Spaces*. 1st ed., Princeton University Press (2005)
* 미분기하학
  * William M. Boothby, *An Introduction to Differentiable Manifolds and Riemannian Geometry*. Revised 2nd ed., Academic Press (2002)
  * Barrett O'Neill, *Elementary Differential Geometry*. Revised 2nd ed., Academic Press (2006)
* 위상수학
  * James R. Munkres, *Topology*. 2nd ed., Pearson College Div (2000)
  * Werner Ballmann, *Introduction to Geometry and Topology*. 1st ed., Birkhäuser (2018)

### 물리학

* **고전역학**
  * L. D. Landau, E. M. Lifshitz, *Mechanics: Volume 1*. 3rd ed., Butterworth-Heinemann (1976)
  * Herbert Goldstein, *Classical Mechanics*. 3rd ed., Pearson (2001)
* **양자역학**
  * Ashok Das, *Lectures on Quantum Mechanics*. 2nd ed., World Scientific Publishing Company (2012)
  * J. J. Sakurai, Jim J. Napolitano, *Modern Quantum Mechanics*. 2nd ed., Pearson (2010)
* **일반상대성이론**
  * Harvey Reall, *Part 3 General Relativity*, University of Cambridge 65 (2013)
  * M. P. Hobson et al., *General Relativity: An Introduction for Physicists*. Illustrated ed., Cambridge University Press (2006)
  * F. de Felice, C. J. S. Clarke, *Relativity on Curved Manifolds*, Cambridge University Press (1992)
* **양자장이론**
  * Lewis H. Ryder, *Quantum Field Theory*. 2nd ed., Cambridge University Press (1996)
  * Michael E. Peskin, Daniel V. Schroeder, *An Introduction to Quantum Field Theory, Student Economy Edition*. 1st ed., Westview Press (2015)
  * Michele Maggiore, *A Modern Introduction to Quantum Field Theory*, Oxford University Press (2005)
  * Ashok Das, *Field Theory: A Path Integral Approach*. 3rd ed., World Scientific (2006)

### 기계학습

* **통계적 기계학습**
  * Masashi Sugiyama, *Introduction to Statistical Machine Learning*. 1st ed., Morgan Kaufmann (2015)
  * Christopher M. Bishop, *Pattern Recognition and Machine Learning*, Springer (2006)
  * Gareth James et al., *An Introduction to Statistical Learning: with Applications in R*. 1st ed., Springer (2013)
  * Trevor Hastie et al., *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. 2nd ed., Springer (2016)
  * Yaser S. Abu-Mostafa et al., *Learning from Data*, AMLBook (2012)
* **심층학습**
  * Zhang et al., *Dive into Deep Learning*. 1.0.0-alpha0. (2022)
  * Eli Stevens et al., *Deep Learning with PyTorch*, Manning (2020)
  * 오가와 유타로, *만들면서 배우는 파이토치 딥러닝: 12가지 모델로 알아보는 딥러닝 응용법*, 한빛미디어 (2021)
* **강화학습**
  * Laura Graesser and Wah Loon Keng, *Foundations of Deep Reinforcement Learning: Theory and Practice in Python*. 1st ed., Addison-Wesley Professional (2020)
  * Csaba Szepesvári, *Algorithms for Reinforcement Learning*. 1st ed., Morgan & Claypool Publishers (2009)
  

### 기타

* **알고리즘**
  * Tim Roughgarden, *Algorithms Illuminated: Part1: The Basics*. Illustrated ed., Soundlikeyourself Publishing (2017)
* **Rust**
  * Steve Klabnik, Carol Nichols, *The Rust Programming Language*. 1st ed., No Starch Press (2018)
  * Jim Blandy, Jason Orendorff, *Programming Rust: Fast, Safe, Systems Development*. 1st ed., O'Reilly Media (2018)
  * Tim McNamara, *Rust in Action*, Manning (2021)
