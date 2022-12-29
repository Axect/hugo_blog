---
title: "🌠 Axions from Primordial Black Holes"
date: 2022-12-29T07:32:42+09:00
draft: true
toc: true
images:
tags:
  - physics
  - paper-review
---

{{<img src="/posts/images/007_01_abstract.png" caption="[arXiv:2212.11977](https://arxiv.org/abs/2212.11977)">}}

&emsp;&emsp;2021년 9월 경부터 시작했던 프로젝트가 1년 3개월 간의 연구 끝에 마무리되어 arXiv에 업로드 되었습니다.🥳🥳 이 연구를 진행하면서 아주 파란만장한 일들을 많이 겪었기에 이번 글에서는 그 경험담과 함께 이 연구에 대해서 리뷰해보려고 합니다. 이 포스트에서는 다음과 같은 약자들을 사용하니 참고해주세요.

* **PBH**: Primordial Black Hole (원시 블랙홀)
* **ALP**: Axion-like Particle (액시온 유사입자)

-----

## Phase 1 - Neutrino from PBHs

시간을 거슬러 2021년 9월로 가봅시다. 연구의 발단은 한 논문에서부터였습니다.
{{<img src="/posts/images/007_02_juno.png" caption="[arXiv:2010.16053](https://arxiv.org/abs/2010.16053)">}}

위 논문은 {{<emph "JUNO">}}(Jiangmen Underground Neutrino Observatory) 라는 중성미자 검출기를 사용하여 암흑물질 후보 중 하나인 원시 블랙홀의 양을 제약하는 논문입니다. 이를 위하여 논문에서는 원시 블랙홀로부터 발생하여 지구에 도달하는 중성미자의 양을 계산한 뒤 이를 JUNO의 검출능력과 비교하여 만일 JUNO에서 검출하지 못할 경우 원시 블랙홀의 양의 상한을 제약하였습니다. 논문에서는 PBH를 크게 두 종류로 구분하였는데, 하나는 우리 은하의 Dark halo에 분포하는 PBH ({{<emph "Galactic PBH)">}}) 이고 나머지 하나는 우리 은하 외부의 PBH ({{<emph "Extragalactic PBH)">}})입니다. 마침 저희 연구실의 선배가 우리 은하에 분포하는 천체로부터 발생하는 입자들의 Flux를 계산하는 것에 대해 연구한 경험이 있었기에 이를 활용하여 이 논문의 계산을 따라가보기로 하였습니다. 이에 대한 계산식은 다음과 같습니다.[${}^{[1]}$](#footnotes)

$$
\frac{\mathrm{d} F_{\mathrm{Gal}}}{\mathrm{d} E}=\int \frac{\mathrm{d} \Omega}{4 \pi} \int_0^{l_{\max }} \mathrm{d} l \frac{\mathrm{d}^2 N}{\mathrm{~d} E \mathrm{~d} t} \frac{f_{\mathrm{PBH}} \rho_{\mathrm{Gal}}[r(l, \psi)]}{M_{\mathrm{PBH}}}
$$

* $F_{\mathrm{Gal}}$ : 우리 은하에 분포하는 PBH로부터 발생하는 중성미자의 Flux
* $E$ : 중성미자의 에너지
* $\displaystyle \int \text{d}\Omega$ : 각도에 대한 적분
* $r(l,\psi) \equiv \sqrt{r_\odot^2 + l^2 - 2r_\odot l \cos \psi}$ : 은하 중심으로부터

-----

## A. Footnotes {#footnotes}

[1] : B. Dasgupta, R. Laha, and A. Ray, [Phys. Rev. Lett. 125, 101101 (2020)](http://dx.doi.org/10.1103/PhysRevLett.125.101101), [arXiv:1912.01014 [hep-ph]](https://arxiv.org/abs/1912.01014).