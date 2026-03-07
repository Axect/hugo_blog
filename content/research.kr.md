---
title: "Research"
date: 2026-02-09T17:00:00+09:00
draft: false
toc: true
---

## 연구 개요

저는 **암흑물질 현상론**과 **scientific machine learning**의 접점에서 연구합니다. 연구의 한 축은 원시 블랙홀(PBH), 액시온 유사 입자(ALP), 그리고 이들이 남기는 광자·양전자·중성미자 신호를 통해 암흑물질의 성질을 정밀하게 제한하는 것입니다. 다른 한 축은 이러한 문제에서 반복적으로 등장하는 고비용 수치계산, 역문제, 동역학 복원을 위해 물리 구조를 보존하는 머신러닝 모델과 계산 프레임워크를 만드는 것입니다.

천문학 학부 배경 위에서 이론입자물리 박사과정을 거치며, 저는 우주론적 입자 진화와 PBH 현상론부터 딥러닝 기반 질량 재구성, 해밀토니안 역학 학습까지 서로 다른 문제를 한 흐름으로 다뤄 왔습니다. Yonsei HEP-COSMO에서 구축한 이 기반은 현재 Fudan University와 RIKEN iTHEMS에서의 연구로 이어지고 있으며, 현상론 계산과 AI 모델링을 별개의 기술이 아니라 서로를 강화하는 연구 도구로 발전시키고 있습니다.

대표적으로 PBH-ALP 연구에서는 우주 팽창을 반영한 입자 수명과 전파를 정교하게 모델링해 관측 가능 신호를 추적했고, DeeLeMa에서는 입자물리 실험의 역문제를 딥러닝으로 재구성했으며, Neural Hamilton에서는 해밀토니안만으로 물리 동역학을 학습하는 연산자 학습 구조를 탐구했습니다. 제가 지향하는 연구는 단순히 "AI를 물리에 적용"하는 것이 아니라, 물리학적 해석 가능성과 계산 효율을 동시에 높이는 새로운 연구 방법론을 만드는 것입니다.

-----

## 현재 연구 방향

### 암흑물질 현상론과 천체입자물리

현재 연구의 중심은 PBH와 ALP를 포함한 암흑물질 후보의 현상론을 더 정밀하게 계산하고, 이를 실제 관측 가능량과 직접 연결하는 것입니다. PBH 증발이 만들어내는 extragalactic photon 신호, sub-MeV 영역의 axion background, 그리고 은하 중심 511 keV excess와 같은 문제를 다루며, 이상화된 근사 대신 우주론적 진화와 천체물리 환경을 더 충실히 반영한 모델을 구축하고 있습니다.

이 방향의 핵심 목표는 "흥미로운 가능성 제시"를 넘어서, 관측 자료와 직접 비교 가능한 수준의 정량적 제약을 만드는 것입니다. 장기적으로는 감마선, 양전자, 중성미자, 중력파를 연결하는 multi-messenger dark matter phenomenology로 확장하고자 합니다.

### 물리학을 위한 연산자 학습과 역문제

두 번째 축은 물리 법칙을 보존하면서도 전통적 수치 솔버보다 빠르게 작동하는 scientific ML 모델을 만드는 것입니다. Neural Hamilton과 Bayesian data assimilation 연구에서는 해밀토니안 동역학을 직접 학습하고 장기 예측 안정성을 높이는 방법을 탐구했고, 현재는 PBH secondary spectra와 같은 복잡한 현상론 계산을 neural operator로 근사하는 방향으로 확장하고 있습니다.

이 연구는 단순한 surrogate modeling에 머물지 않습니다. 제가 관심을 두는 문제는 "AI가 물리 구조를 얼마나 잘 보존하는가", "관측 데이터로부터 매개변수를 얼마나 안정적으로 역추론할 수 있는가", 그리고 "연구자가 실제 현상론 계산에 바로 쓸 수 있는 도구가 될 수 있는가"입니다. 앞으로는 inverse problems와 uncertainty-aware inference를 포함하는 형태로 넓혀 갈 계획입니다.

### 방법론 확장과 계산 도구 개발

제 연구는 특정 주제 하나에 고립되어 있지 않습니다. 생의학 신호 품질 평가, 최적화용 learning rate scheduler, Rust 기반 수치 라이브러리 개발과 같은 작업은 모두 "복잡한 과학 문제를 계산적으로 다루는 방법"이라는 공통 관심에서 나왔습니다. 이런 경험은 새로운 도메인에 맞는 모델 구조를 빠르게 설계하고, 재현 가능한 연구용 소프트웨어로 정리하는 데 직접 연결됩니다.

따라서 제 장기 목표는 물리학 문제에 특화된 AI 모델을 개별적으로 제안하는 데 그치지 않고, 이론물리와 데이터 기반 추론 사이를 자연스럽게 연결하는 계산 생태계를 구축하는 것입니다. 즉, 정확한 현상론 계산, 빠른 대체 모델, 해석 가능한 추론, 그리고 재사용 가능한 연구 소프트웨어를 하나의 흐름으로 묶는 것이 제 연구의 방향입니다.

-----

## 논문

### 2026

**Primordial Black Holes as a Factory of Axions: Extragalactic Photons from Axions**<br>
{{<emph "Tae-Geun Kim">}}, Jong-Chul Park, Seong Chan Park, Yeji Park<br>
[📄 PTEP ptag011](https://doi.org/10.1093/ptep/ptag011) | [📄 arXiv:2212.11977](https://arxiv.org/abs/2212.11977)

<details>
<summary>📋 BibTeX</summary>

```bibtex
@article{kim2023primordial,
  title={Primordial Black Holes as a Factory of Axions: Extragalactic Photons from Axions},
  author={Kim, Tae-Geun and Park, Jong-Chul and Park, Seong Chan and Park, Yeji},
  journal={Progress of Theoretical and Experimental Physics},
  volume={2023},
  number={1},
  pages={ptag011},
  year={2023},
  doi={10.1093/ptep/ptag011}
}
```
</details>

-----

### 2025

**Learning Hamiltonian Dynamics with Bayesian Data Assimilation**<br>
Taehyeun Kim, {{<emph "Tae-Geun Kim">}}, Anouk Girard, Ilya Kolmanovsky<br>
[📄 arXiv:2501.18808](https://arxiv.org/abs/2501.18808)

<details>
<summary>📋 BibTeX</summary>

```bibtex
@article{kim2025learning,
  title={Learning Hamiltonian Dynamics with Bayesian Data Assimilation},
  author={Kim, Taehyeun and Kim, Tae-Geun and Girard, Anouk and Kolmanovsky, Ilya},
  journal={arXiv preprint arXiv:2501.18808},
  year={2025}
}
```
</details>

-----

### 2024

**Neural Hamilton: Can A.I. Understand Hamiltonian Mechanics?**<br>
{{<emph "Tae-Geun Kim">}}, Seong Chan Park<br>
[📄 arXiv:2410.20951](https://arxiv.org/abs/2410.20951) | [💻 Code](https://github.com/Axect/Neural_Hamilton)

<details>
<summary>📋 BibTeX</summary>

```bibtex
@article{kim2024neural,
  title={Neural Hamilton: Can A.I. Understand Hamiltonian Mechanics?},
  author={Kim, Tae-Geun and Park, Seong Chan},
  journal={arXiv preprint arXiv:2410.20951},
  year={2024}
}
```
</details>

-----

**HyperbolicLR: Epoch insensitive learning rate scheduler**<br>
{{<emph "Tae-Geun Kim">}}<br>
[📄 arXiv:2407.15200](https://arxiv.org/abs/2407.15200)

<details>
<summary>📋 BibTeX</summary>

```bibtex
@article{kim2024hyperboliclr,
  title={HyperbolicLR: Epoch insensitive learning rate scheduler},
  author={Kim, Tae-Geun},
  journal={arXiv preprint arXiv:2407.15200},
  year={2024}
}
```
</details>

-----

**Unsupervised sequence-to-sequence learning for automatic signal quality assessment**<br>
Chang Min Hyun, {{<emph "Tae-Geun Kim">}}, Kyounghun Lee<br>
[📄 CMPB 108079](https://doi.org/10.1016/j.cmpb.2024.108079) | [📄 arXiv:2305.09368](https://arxiv.org/abs/2305.09368)

<details>
<summary>📋 BibTeX</summary>

```bibtex
@article{hyun2024unsupervised,
  title={Unsupervised sequence-to-sequence learning for automatic signal quality assessment in multi-channel electrical impedance-based hemodynamic monitoring},
  author={Hyun, Chang Min and Kim, Tae-Geun and Lee, Kyounghun},
  journal={Computer Methods and Programs in Biomedicine},
  pages={108079},
  year={2024},
  doi={10.1016/j.cmpb.2024.108079}
}
```
</details>

-----

### 2023

**DeeLeMa: Missing information search with Deep Learning for Mass estimation**<br>
Kayoung Ban, Dong Woo Kang, {{<emph "Tae-Geun Kim">}}, Seong Chan Park, Yeji Park<br>
[📄 Phys. Rev. Research 5, 043186](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.043186) | [📄 arXiv:2212.12836](https://arxiv.org/abs/2212.12836) | [💻 Code](https://github.com/Yonsei-HEP-COSMO/DeeLeMa)

<details>
<summary>📋 BibTeX</summary>

```bibtex
@article{ban2023deelema,
  title={DeeLeMa: Missing information search with Deep Learning for Mass estimation},
  author={Ban, Kayoung and Kang, Dong Woo and Kim, Tae-Geun and Park, Seong Chan and Park, Yeji},
  journal={Physical Review Research},
  volume={5},
  number={4},
  pages={043186},
  year={2023},
  doi={10.1103/PhysRevResearch.5.043186}
}
```
</details>

-----

## 주요 발표

### 2026

**Accelerating PBH Phenomenology via Neural Operators**
*The 2nd AI+HEP in East Asia @ KEK*, Tsukuba, Japan [구두발표]

### 2025

**From Primordial Black Holes to Nuclei: Solving Inverse Problems in Physics with Operator Learning**
*Nuclear Lunch Seminar @ Fudan University*, Shanghai, China [구두발표, 초청]

[**Can AI Understand Hamiltonian Mechanics?**](https://www.dropbox.com/scl/fi/ac1233d41f7amxstrvofv/main.pdf?rlkey=ma2pimb4xcyjl17zvy893bnr3&st=2f1yzz16&dl=0)
*Summer Institute 2025*, Yeosu, Korea [구두발표] | [📊 슬라이드](https://www.dropbox.com/scl/fi/ac1233d41f7amxstrvofv/main.pdf?rlkey=ma2pimb4xcyjl17zvy893bnr3&st=2f1yzz16&dl=0)

[**A Neural Operator for Primordial Black Hole Physics**](https://www.dropbox.com/scl/fi/j5m29r4mfz92fqxvj2uuj/main.pdf?rlkey=cfjkz2h0a9de4iqbto12a49np&st=vl5967uy&dl=0)
*The 4th workshop on Symmetry and Structure of the Universe*, Jeonju, Korea [구두발표] | [📊 슬라이드](https://www.dropbox.com/scl/fi/j5m29r4mfz92fqxvj2uuj/main.pdf?rlkey=cfjkz2h0a9de4iqbto12a49np&st=vl5967uy&dl=0)

[**PBH Phenomenology with Operator Learning**](https://www.dropbox.com/scl/fi/wxobs4uyd1d1otewfuq3q/main.pdf?rlkey=06ja38ckktp84mnachku21gjr&st=ghs0fl89&dl=0)
*LSSU Seminar @ JBNU*, Jeonju, Korea [구두발표, 초청] | [📊 슬라이드](https://www.dropbox.com/scl/fi/wxobs4uyd1d1otewfuq3q/main.pdf?rlkey=06ja38ckktp84mnachku21gjr&st=ghs0fl89&dl=0)

[**AI with Hamiltonian Mechanics: From Predictions to Understanding**](https://www.dropbox.com/scl/fi/w4krmvnjfu60woevaibee/AI_with_Hamiltonian_AIHEP-EastAsia.pdf?rlkey=cp9ah1nlkz3x4rkic1ugb6sk2&st=tpaioyql&dl=0)
*AI+HEP in East Asia 2025*, Daejeon, Korea [구두발표] | [📊 슬라이드](https://www.dropbox.com/scl/fi/w4krmvnjfu60woevaibee/AI_with_Hamiltonian_AIHEP-EastAsia.pdf?rlkey=cp9ah1nlkz3x4rkic1ugb6sk2&st=tpaioyql&dl=0)

**Can A.I. Understand Hamiltonian Mechanics?**
*RIKEN DEEP-IN Seminar*, Online [구두발표, 초청]

**Can A.I. Understand Hamiltonian Mechanics?**
*Dark Matter as a portal to New Physics 2025*, Pohang, Korea [구두발표, 초청]

**Can A.I. Understand Hamiltonian Mechanics?**
*Focused workshop on AI in High Energy Physics 2025*, Seoul, Korea [구두발표]

### 2024

**Can A.I. Understand Hamiltonian Mechanics?**
*2024 Korea-France STAR Workshop*, Seoul, Korea [구두발표]

**Can A.I. Understand Hamiltonian Mechanics?**
*Invited Seminar @ KIAS*, Seoul, Korea [구두발표, 초청]

**Can A.I. Understand Hamiltonian Mechanics?**
*21st Saga-Yonsei Joint Workshop*, Seoul, Korea [구두발표]

**Primordial Black Hole dominant Axion background**
*2024 KPS Fall Meeting*, Yeosu, Korea [구두발표]

### 2023

[**Exploration of Primordial Black Holes and Axion-Like Particles**](https://www.dropbox.com/scl/fi/q79z6wwwxrshj88gw5y3k/SI2023_TGKim.pdf?rlkey=jv0ypybbi8175rju495a1k0xt&dl=0)
*27th International Summer Institute on Phenomenology*, Nantou, Taiwan [포스터] | [📊 포스터](https://www.dropbox.com/scl/fi/q79z6wwwxrshj88gw5y3k/SI2023_TGKim.pdf?rlkey=jv0ypybbi8175rju495a1k0xt&dl=0)

### 2022

**Exploration of Primordial Black Holes and Axion-Like Particles**
*16th International Conference on Interconnections between Particle Physics and Cosmology*, Daejeon, Korea [구두발표]

[**Constraining ALPs via PBH with time-varying decay process**](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_WPDC.html)
*Workshop on Physics of Dark Cosmos*, Busan, Korea [구두발표] | [📊 슬라이드](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_WPDC.html)

[**Constraining ALPs via PBH with time-varying decay process Part.2**](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_kps.html)
*KPS 70th Anniversary and 2022 Fall Meeting*, Busan, Korea [구두발표] 🏆 **최우수 구두발표상** | [📊 슬라이드](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_kps.html)

### 2019

[**Bird's eye view of Neutron star cooling**](https://axect.github.io/Slides/PHY/NS/neutron-saga.html)
*16th Saga-Yonsei Joint Workshop* [구두발표] | [📊 슬라이드](https://axect.github.io/Slides/PHY/NS/neutron-saga.html)

-----

## 수상 및 펠로우십

* **상하이 슈퍼박사후연구원 펠로우십**, 상하이시 정부 (2025-2027)
* **푸단 슈퍼박사후연구원 펠로우십**, 푸단대학교 (2025-2027)
* **아카데미 연구 펠로우십**, 연세대학교 (2022-2023)
* **최우수 구두발표상**, KPS 70주년 및 2022 추계학술대회 (2022)
