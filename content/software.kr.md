---
title: "Software & Projects"
date: 2026-02-09T15:20:00+09:00
draft: false
toc: false
---

Tae-Geun Kim (Axect)의 오픈소스 소프트웨어 및 연구 프로젝트입니다.

-----

## 🚀 활성 프로젝트

### Peroxide

{{<center>}}
**Rust 수치계산 라이브러리**
![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Peroxide?style=flat-square) ![Crates.io](https://img.shields.io/crates/v/peroxide?style=flat-square) ![Downloads](https://img.shields.io/crates/d/peroxide?style=flat-square)
{{</center>}}

Python의 NumPy/SciPy에 필적하는 종합 수치계산 라이브러리입니다. 과학계산 연구를 위한 핵심 인프라를 제공합니다.

**주요 기능:**
* BLAS/LAPACK 통합 선형대수
* 최적화 알고리즘 (경사하강법, Levenberg-Marquardt 등)
* 수치적분 & ODE/PDE 솔버
* 통계 분포 & 특수함수
* 다양한 I/O 형식 지원 DataFrame (CSV, NetCDF, JSON, Parquet)
* C, Fortran, Python FFI 지원

**기술 스택:** SIMD, BLAS, LAPACK, proc-macro 메타프로그래밍

**빠른 설치:**
```bash
cargo add peroxide
```

**링크:** [GitHub](https://github.com/Axect/Peroxide) | [Crates.io](https://crates.io/crates/peroxide) | [문서](https://peroxide.surge.sh)

-----

### Radient

{{<center>}}
**Rust 자동미분 라이브러리**
![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Radient?style=flat-square) ![Version](https://img.shields.io/crates/v/radient?style=flat-square) ![Downloads](https://img.shields.io/crates/d/radient?style=flat-square)
{{</center>}}

연구 및 프로토타이핑을 위한 실험적 역방향 자동미분 라이브러리입니다. 아레나 기반 메모리 관리를 사용합니다.

**주요 기능:**
* 테이프 기반 기울기 계산을 통한 효율적인 역방향 AD
* 메모리 안정성과 성능을 위한 아레나 할당
* 과학계산 워크플로를 위한 Peroxide 통합

**빠른 설치:**
```bash
cargo add radient
```

**링크:** [GitHub](https://github.com/Axect/Radient) | [Crates.io](https://crates.io/crates/radient) | [문서](https://docs.rs/radient)

-----

### DeeLeMa

{{<center>}}
**질량 추정을 위한 딥러닝**
![Python](https://img.shields.io/badge/Python-3572A5?style=flat-square&logo=python&logoColor=white) ![Paper](https://img.shields.io/badge/PRR-Published-success?style=flat-square)
{{</center>}}

결측 정보 탐색을 사용한 입자물리학 질량 추정 딥러닝 프레임워크입니다. **Physical Review Research**에 게재되었습니다.

**연구 영향:**
* 논문: [Phys. Rev. Research **5**, 043186 (2023)](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.043186)
* 사전출판: [arXiv:2212.12836](https://arxiv.org/abs/2212.12836)

**기술 스택:** PyTorch, PyTorch Lightning, Wandb (하이퍼파라미터 튜닝), Tensorboard

**링크:** [GitHub](https://github.com/Yonsei-HEP-COSMO/DeeLeMa) | [논문](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.043186) | [arXiv](https://arxiv.org/abs/2212.12836)

-----

### Neural Hamilton

{{<center>}}
**AI가 해밀토니안 역학을 이해할 수 있을까?**
![Python](https://img.shields.io/badge/Python-3572A5?style=flat-square&logo=python&logoColor=white) ![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Neural_Hamilton?style=flat-square) ![Paper](https://img.shields.io/badge/arXiv-2410.20951-b31b1b?style=flat-square)
{{</center>}}

해밀토니안 역학을 위한 연산자 학습의 공식 구현입니다. 네 가지 신경망 아키텍처(DeepONet, TraONet, VaRONet, MambONet)를 통해 AI가 물리 동역학을 진정으로 이해할 수 있는지 탐구합니다.

**연구 영향:**
* 논문: [arXiv:2410.20951](https://arxiv.org/abs/2410.20951) - 김태근, 박성찬 (2024)
* MambONet이 RK4 솔버 및 경쟁 아키텍처를 지속적으로 능가

**주요 기능:**
* Gaussian Random Field를 사용한 물리적으로 타당한 포텐셜 생성 알고리즘
* 연산자 학습을 위한 네 가지 신경망 아키텍처
* 다중 언어 구현 (Python, Rust, Julia)
* GPU 가속을 위한 CUDA 호환

**기술 스택:** PyTorch, CUDA, Rust (수치 백엔드), Julia (시각화)

**링크:** [GitHub](https://github.com/Axect/Neural_Hamilton) | [arXiv](https://arxiv.org/abs/2410.20951)

-----

### PyTorch Template

{{<center>}}
**ML 실험을 위한 유연한 PyTorch 템플릿**
![Python](https://img.shields.io/badge/Python-3572A5?style=flat-square&logo=python&logoColor=white) ![Stars](https://img.shields.io/github/stars/Axect/pytorch_template?style=flat-square)
{{</center>}}

YAML 기반 설정으로 재현 가능한 머신러닝 실험을 위해 설계된 모듈식 PyTorch 프로젝트 템플릿입니다.

**주요 기능:**
* 손쉬운 설정을 위한 YAML 기반 실험 구성
* 견고한 실험을 위한 다중 랜덤 시드 지원
* 장치 선택(CPU/GPU) 및 학습률 스케줄링
* 확장성을 위한 깔끔한 모듈 구조

**링크:** [GitHub](https://github.com/Axect/pytorch_template)

-----

### Quantum Algorithms

{{<center>}}
**양자 컴퓨팅 알고리즘 구현**
![Quantum](https://img.shields.io/badge/Quantum-6929C4?style=flat-square&logo=qiskit&logoColor=white) ![Stars](https://img.shields.io/github/stars/Axect/QuantumAlgorithms?style=flat-square)
{{</center>}}

여러 프레임워크(Pennylane, RustQIP, Qiskit, Cirq)로 구현된 양자 알고리즘의 종합 컬렉션과 인터랙티브 Jupyter 노트북입니다.

**기술 스택:** Pennylane, RustQIP, Qiskit, Cirq, Jupyter

**링크:** [GitHub](https://github.com/Axect/QuantumAlgorithms)

-----

### Puruspe

{{<center>}}
**순수 Rust 특수함수 라이브러리**
![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Puruspe?style=flat-square) ![Version](https://img.shields.io/crates/v/puruspe?style=flat-square) ![Downloads](https://img.shields.io/crates/d/puruspe?style=flat-square)
{{</center>}}

과학계산을 위한 수학적 특수함수(베셀, 감마, 오차함수 등)의 순수 Rust 구현입니다.

**빠른 설치:**
```bash
cargo add puruspe
```

**링크:** [GitHub](https://github.com/Axect/Puruspe) | [Crates.io](https://crates.io/crates/puruspe) | [문서](https://docs.rs/puruspe)

-----

### Forger

{{<center>}}
**Rust 강화학습 라이브러리**
![Rust](https://img.shields.io/badge/Rust-DEA584?style=flat-square&logo=rust&logoColor=black) ![Stars](https://img.shields.io/github/stars/Axect/Forger?style=flat-square) ![Version](https://img.shields.io/crates/v/forger?style=flat-square) ![Downloads](https://img.shields.io/crates/d/forger?style=flat-square)
{{</center>}}

연구 및 교육을 위해 Rust로 구현된 강화학습 알고리즘 라이브러리입니다.

**알고리즘:** Monte Carlo, Temporal Difference, Q-Learning

**빠른 설치:**
```bash
cargo add forger
```

**링크:** [GitHub](https://github.com/Axect/Forger) | [Crates.io](https://crates.io/crates/forger) | [문서](https://docs.rs/forger)

-----

## 📦 보관된 프로젝트

<details>
<summary><strong>보관/실험 프로젝트 보기</strong></summary>

### NCDataFrame.jl
DataFrame 통합 Julia netCDF I/O 패키지 (보관됨).
**링크:** [GitHub](https://github.com/Axect/NCDataFrame.jl) | [JuliaHub](https://juliahub.com/ui/Packages/NCDataFrame/zhMPT/)

### ZelLayGen
Rust로 작성된 Zellij 레이아웃 생성기입니다.
**링크:** [GitHub](https://github.com/Axect/Zellaygen)

### Puruda
순수 Rust DataFrame 라이브러리 (Peroxide의 DataFrame 모듈로 대체됨).
**링크:** [GitHub](https://github.com/Axect/Puruda) | [Crates.io](https://crates.io/crates/puruda)

### HNumeric
Haskell 수치계산 라이브러리입니다.
**링크:** [GitHub](https://github.com/Axect/HNumeric) | [Hackage](https://hackage.haskell.org/package/HNumeric)

### DNumeric
D 프로그래밍 언어용 수치계산 라이브러리입니다.
**링크:** [GitHub](https://github.com/Axect/DNumeric) | [DUB](https://code.dlang.org/packages/dnumeric)

</details>

-----

## 💬 협업

이 라이브러리를 사용하거나 연구 협업에 관심이 있으신가요? 언제든지:
* GitHub에서 이슈나 PR을 열어주세요
* [이메일](mailto:axect.tg@proton.me)로 연락주세요
* [LinkedIn](https://www.linkedin.com/in/tae-geun-kim/)에서 연결하세요

모든 활성 프로젝트는 기여를 환영합니다!
