---
title: "Research"
date: 2026-02-09T17:00:00+09:00
draft: false
toc: true
---

## Research Overview

My research sits at the intersection of **dark matter phenomenology** and **scientific machine learning**. One part of my work studies primordial black holes (PBHs), axion-like particles (ALPs), and the photon, positron, and neutrino signals they can generate. The other part develops machine learning models and computational frameworks that preserve physical structure while accelerating expensive calculations, solving inverse problems, and reconstructing dynamics from limited information.

With training that began in astronomy and continued through a Ph.D. in theoretical particle physics, I have built a research program that moves naturally between astroparticle phenomenology and AI-driven modeling. Work at Yonsei HEP-COSMO established this foundation, and my current appointments at Fudan University and RIKEN iTHEMS are extending it toward precision phenomenology and physics-informed AI. I do not treat these as separate tracks: phenomenology motivates the computational questions, and machine learning becomes useful only when it respects the structure of the underlying physics.

This perspective runs through my recent projects. In PBH-ALP phenomenology, I studied cosmological particle evolution and observational signatures with more careful treatments of propagation and lifetime effects. In DeeLeMa, I approached mass reconstruction in particle physics as a deep-learning inverse problem. In Neural Hamilton, I asked whether operator-learning architectures can infer Hamiltonian dynamics directly from the Hamiltonian itself. Across these projects, the common goal is to build research methods that improve both physical interpretability and computational efficiency.

-----

## Current Research Directions

### Dark Matter Phenomenology and Astroparticle Signatures

My current phenomenology work focuses on making PBH- and ALP-based dark matter studies more precise and more directly comparable to data. This includes extragalactic photon signals from evaporating PBHs, axion backgrounds in the sub-MeV regime, and refined modeling of the Galactic 511 keV excess. A recurring theme is replacing oversimplified assumptions with treatments that better capture cosmological evolution, particle propagation, and realistic astrophysical environments.

The aim is not only to propose interesting dark matter scenarios, but to produce quantitative constraints that can stand up to detailed observational comparison. In the longer term, I want to extend this program toward multi-messenger phenomenology that connects gamma rays, positrons, neutrinos, and gravitational-wave-informed early-universe physics.

### Operator Learning and Inverse Problems for Physics

The second pillar of my work is scientific ML for physics problems where conventional solvers are accurate but too slow, or where the main challenge is inversion rather than forward prediction. In Neural Hamilton and follow-up work on Bayesian data assimilation, I studied how to learn Hamiltonian dynamics while improving long-term stability. I am now extending this line toward neural-operator surrogates for PBH secondary spectra and related phenomenology calculations.

What matters to me here is not generic surrogate modeling. The key questions are whether a model preserves the right physical structure, whether it supports robust inference from observational data, and whether it can become a practical tool for day-to-day phenomenology. That naturally leads to future work on inverse problems, uncertainty-aware inference, and reusable ML tools designed for theoretical physics.

### Method Development and Research Software

My broader work includes biomedical signal-quality assessment, optimization methods such as HyperbolicLR, and open-source numerical software in Rust. These projects are not side topics so much as extensions of the same methodological interest: how to design reliable computational tools for hard scientific problems.

This makes software and methodology a core part of my research identity. Long term, I want to build a workflow in which precise phenomenology, fast learned surrogates, interpretable inference, and reusable research software reinforce one another. The objective is to narrow the gap between theoretical modeling and data-driven discovery without sacrificing rigor in either direction.

-----

## Publications

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

## Selected Talks & Presentations

### 2026

**Accelerating PBH Phenomenology via Neural Operators**
*The 2nd AI+HEP in East Asia @ KEK*, Tsukuba, Japan [Oral]

### 2025

**From Primordial Black Holes to Nuclei: Solving Inverse Problems in Physics with Operator Learning**
*Nuclear Lunch Seminar @ Fudan University*, Shanghai, China [Oral, Invited]

[**Can AI Understand Hamiltonian Mechanics?**](https://www.dropbox.com/scl/fi/ac1233d41f7amxstrvofv/main.pdf?rlkey=ma2pimb4xcyjl17zvy893bnr3&st=2f1yzz16&dl=0)
*Summer Institute 2025*, Yeosu, Korea [Oral] | [📊 Slides](https://www.dropbox.com/scl/fi/ac1233d41f7amxstrvofv/main.pdf?rlkey=ma2pimb4xcyjl17zvy893bnr3&st=2f1yzz16&dl=0)

[**A Neural Operator for Primordial Black Hole Physics**](https://www.dropbox.com/scl/fi/j5m29r4mfz92fqxvj2uuj/main.pdf?rlkey=cfjkz2h0a9de4iqbto12a49np&st=vl5967uy&dl=0)
*The 4th workshop on Symmetry and Structure of the Universe*, Jeonju, Korea [Oral] | [📊 Slides](https://www.dropbox.com/scl/fi/j5m29r4mfz92fqxvj2uuj/main.pdf?rlkey=cfjkz2h0a9de4iqbto12a49np&st=vl5967uy&dl=0)

[**PBH Phenomenology with Operator Learning**](https://www.dropbox.com/scl/fi/wxobs4uyd1d1otewfuq3q/main.pdf?rlkey=06ja38ckktp84mnachku21gjr&st=ghs0fl89&dl=0)
*LSSU Seminar @ JBNU*, Jeonju, Korea [Oral, Invited] | [📊 Slides](https://www.dropbox.com/scl/fi/wxobs4uyd1d1otewfuq3q/main.pdf?rlkey=06ja38ckktp84mnachku21gjr&st=ghs0fl89&dl=0)

[**AI with Hamiltonian Mechanics: From Predictions to Understanding**](https://www.dropbox.com/scl/fi/w4krmvnjfu60woevaibee/AI_with_Hamiltonian_AIHEP-EastAsia.pdf?rlkey=cp9ah1nlkz3x4rkic1ugb6sk2&st=tpaioyql&dl=0)
*AI+HEP in East Asia 2025*, Daejeon, Korea [Oral] | [📊 Slides](https://www.dropbox.com/scl/fi/w4krmvnjfu60woevaibee/AI_with_Hamiltonian_AIHEP-EastAsia.pdf?rlkey=cp9ah1nlkz3x4rkic1ugb6sk2&st=tpaioyql&dl=0)

**Can A.I. Understand Hamiltonian Mechanics?**
*RIKEN DEEP-IN Seminar*, Online [Oral, Invited]

**Can A.I. Understand Hamiltonian Mechanics?**
*Dark Matter as a portal to New Physics 2025*, Pohang, Korea [Oral, Invited]

**Can A.I. Understand Hamiltonian Mechanics?**
*Focused workshop on AI in High Energy Physics 2025*, Seoul, Korea [Oral]

### 2024

**Can A.I. Understand Hamiltonian Mechanics?**
*2024 Korea-France STAR Workshop*, Seoul, Korea [Oral]

**Can A.I. Understand Hamiltonian Mechanics?**
*Invited Seminar @ KIAS*, Seoul, Korea [Oral, Invited]

**Can A.I. Understand Hamiltonian Mechanics?**
*21st Saga-Yonsei Joint Workshop*, Seoul, Korea [Oral]

**Primordial Black Hole dominant Axion background**
*2024 KPS Fall Meeting*, Yeosu, Korea [Oral]

### 2023

[**Exploration of Primordial Black Holes and Axion-Like Particles**](https://www.dropbox.com/scl/fi/q79z6wwwxrshj88gw5y3k/SI2023_TGKim.pdf?rlkey=jv0ypybbi8175rju495a1k0xt&dl=0)
*27th International Summer Institute on Phenomenology*, Nantou, Taiwan [Poster] | [📊 Poster](https://www.dropbox.com/scl/fi/q79z6wwwxrshj88gw5y3k/SI2023_TGKim.pdf?rlkey=jv0ypybbi8175rju495a1k0xt&dl=0)

### 2022

**Exploration of Primordial Black Holes and Axion-Like Particles**
*16th International Conference on Interconnections between Particle Physics and Cosmology*, Daejeon, Korea [Oral]

[**Constraining ALPs via PBH with time-varying decay process**](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_WPDC.html)
*Workshop on Physics of Dark Cosmos*, Busan, Korea [Oral] | [📊 Slides](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_WPDC.html)

[**Constraining ALPs via PBH with time-varying decay process Part.2**](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_kps.html)
*KPS 70th Anniversary and 2022 Fall Meeting*, Busan, Korea [Oral] 🏆 **Best Oral Award** | [📊 Slides](https://axect.github.io/Slides/PHY/PBH_ALP/20221021_kps.html)

### 2019

[**Bird's eye view of Neutron star cooling**](https://axect.github.io/Slides/PHY/NS/neutron-saga.html)
*16th Saga-Yonsei Joint Workshop* [Oral] | [📊 Slides](https://axect.github.io/Slides/PHY/NS/neutron-saga.html)

-----

## Honors & Awards

* **Shanghai Superpostdoc Fellowship**, Shanghai Municipal Government (2025-2027)
* **Fudan Superpostdoc Fellowship**, Fudan University (2025-2027)
* **Academy Research Fellowship**, Yonsei University (2022-2023)
* **Best Oral Presentation Award**, KPS 70th Anniversary and 2022 Fall Meeting (2022)
