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

## Phase 1. Neutrino from PBHs

### 1-1. Start from a paper

시간을 거슬러 2021년 9월로 가봅시다. 연구의 발단은 한 논문에서부터였습니다.
{{<img src="/posts/images/007_02_juno.png" caption="[arXiv:2010.16053](https://arxiv.org/abs/2010.16053)">}}

위 논문은 {{<emph "JUNO">}}(Jiangmen Underground Neutrino Observatory) 라는 중성미자 검출기를 사용하여 암흑물질 후보 중 하나인 원시 블랙홀의 양을 제약하는 논문입니다. 이를 위하여 논문에서는 원시 블랙홀로부터 발생하여 지구에 도달하는 중성미자의 양을 계산한 뒤 이를 JUNO의 검출능력과 비교하여 만일 JUNO에서 검출하지 못할 경우 원시 블랙홀의 양의 상한을 제약하였습니다. 논문에서는 PBH를 크게 두 종류로 구분하였는데, 하나는 우리 은하의 Dark halo에 분포하는 PBH ({{<emph "Galactic PBH">}}) 이고 나머지 하나는 우리 은하 외부의 PBH ({{<emph "Extragalactic PBH">}})입니다. 마침 저희 연구실의 선배가 우리 은하에 분포하는 천체로부터 발생하는 입자들의 Flux를 계산하는 것에 대해 연구한 경험이 있었기에 이를 활용하여 이 논문의 계산을 따라가보기로 하였습니다. 이에 대한 계산식은 다음과 같습니다.[${}^{[1]}$](#footnotes)

$$
\frac{\mathrm{d} F_{\mathrm{Gal}}}{\mathrm{d} E}=\int \frac{\mathrm{d} \Omega}{4 \pi} \int_0^{l_{\max }} \mathrm{d} l \frac{\mathrm{d}^2 N}{\mathrm{d}E \mathrm{~d} t} \frac{f_{\mathrm{PBH}} \rho_{\mathrm{Gal}}[r(l, \psi)]}{M_{\mathrm{PBH}}}
$$

* $F_{\mathrm{Gal}}$ : 우리 은하에 분포하는 PBH로부터 발생하는 중성미자의 Flux

* $E$ : 중성미자의 에너지

* $\displaystyle \int \text{d}\Omega$ : 각도에 대한 적분

* $r(l,\psi) \equiv \sqrt{r_\odot^2 + l^2 - 2lr_\odot\cos \psi}$ : 은하 중심으로부터 지구까지의 거리  
($l$: PBH의 line-of-sight 거리, $\psi$: 두 위치 벡터 사이의 각도)

* $l_{\max } = (r_h^2 - r_\odot^2 \sin^2 \psi)^{1/2} + r_\odot \cos\psi$ : 최대 line-of-sight 거리  
($r_h$: 헤일로 반지름 ($\approx 200\text{kpc}$))

* $\displaystyle \int_0^{l_{\max }} \text{d} l$ : line-of-sight 거리에 대한 적분

* $\dfrac{\mathrm{d}^2 N}{\mathrm{d} E \mathrm{~d} t}$ : PBH로부터 발생하는 중성미자의 에너지 및 시간에 대한 분포

* $f_{\mathrm{PBH}}$ : 암흑물질 대비 PBH의 비율

* $\rho_{\mathrm{Gal}}[r(l,\psi)]$ : 은하에 분포하는 암흑물질 밀도함수

* $M_{\mathrm{PBH}}$ : PBH의 질량

이 수많은 변수들 중 가장 중요한 변수는 적분식 내부에 있는 $\dfrac{\text{d}^2N}{\text{d}E\\,\text{d}t}$인데, 이것이 블랙홀에서 발생한 중성미자를 설명하는 변수이기 떄문입니다. 이 변수는 또한 다음의 두 변수로 나눠집니다.

$$
\frac{\mathrm{d}^2 N}{\mathrm{d} E \mathrm{~d} t}=\left.\frac{\mathrm{d}^2 N}{\mathrm{d} E \mathrm{~d} t}\right|\_{\text {pri }}+\left.\frac{\mathrm{d}^2 N}{\mathrm{d} E \mathrm{~d} t}\right|\_{\mathrm{sec}}
$$

전자는 PBH에서 직접적으로 방출된 중성미자의 양을 나타내고, 후자는 PBH에서 방출된 표준모형 입자들의 상호작용으로 인해 생성된 중성미자의 양을 나타냅니다. 이 논문에서는 이 식들을 구체적으로 설명하지는 않고, {{<emph "BlackHawk">}}라는 프로그램을 이용해서 계산하였다고 기술하였습니다. 따라서 먼저 저는 **BlackHawk**라는 프로그램의 사용법을 익혀야 했습니다. 다행히 문서화가 꽤 잘되어있는 프로그램이라 사용 자체는 어렵지 않았습니다만, 당시 버전에서는 몇몇 에러가 있었고 병렬화가 안되는 등의 문제가 있어서 {{<emph "Julia">}}언어를 사용하여 Wrapper를 작성 후 사용하였습니다. 그렇게 하니 우리은하에서 발생하는 중성미자의 flux는 어렵지 않게 구할 수 있었습니다.

외부은하에서 발생하는 중성미자의 flux 역시 어렵지는 않았는데, 계산식은 다음과 같습니다.

$$
\frac{\mathrm{d} F\_{\mathrm{EG}}}{\mathrm{d} E}=\int\_{t\_{\min }}^{t\_{\max }} \mathrm{d} t {[1+z(t)] \frac{f\_{\mathrm{PBH}} \rho\_{\mathrm{DM}}}{M_{\mathrm{PBH}}} } \times\left.\frac{\mathrm{d}^2 N}{\mathrm{~d} E\_{\mathrm{s}} \mathrm{d} t}\right|\_{E\_{\mathrm{s}}=[1+z(t)] E}
$$

은하 내부와 달라진 점은 중성미자가 우주 초기부터 발생하여 날아올 수 있기 때문에 그에 대한 dilution 효과와 redshift 효과가 식에 반영되어 있다는 점입니다. 이 당시 BlackHawk에서 이를 계산하기 위한 코드가 스크립트 형식으로 포함되어 있었는데 계산해보니 Lagrange interpolation 부분에서 하나 잘못된 점이 발견되어 코드를 Julia로 처음부터 작성하여 계산하였습니다. 여기까지는 BlackHawk 사용법만 숙지한다면 계산이 어렵지 않았습니다. 이렇게 계산한 것을 합쳐보면 논문의 FIG. 1과 같은 결과를 얻을 수 있습니다.

{{<img src="/posts/images/007_03_juno_dFdE.png" caption="FIG. 1 in 2010.16053">}}


### 1-2. Inverse Beta Decay

중성미자는 직접적으로 관측이 불가능하므로 다른 입자들과의 상호작용을 통해 관측하여야 합니다. 특히 JUNO같은 검출기에서는 다음의 반응들을 통해 중성미자를 관측합니다.

* IBD (Inverse Beta Decay) : $\bar{\nu}\_e+p \rightarrow e^{+}+n$
* $e$ES (Electron Elastic Scattering) : $\nu + e^{-} \rightarrow \nu + e^{-}$
* $p$ES (Proton Elastic Scattering) : $\nu + p \rightarrow \nu + p$
* With ${}^{12}\mathrm{C}$
  * NC (Neutral Current) : $\nu + {}^{12}\mathrm{C} \rightarrow \nu + {}^{12}\mathrm{C}^*$
  * CC (Charged Current) : $\nu\_e + {}^{12}\mathrm{C} \rightarrow e^{-} + {}^{12}\mathrm{N}$ & $\bar{\nu}\_e + {}^{12}\mathrm{C} \rightarrow e^{+} + {}^{12}\mathrm{B}$

저희는 리뷰목적으로 논문을 다뤘으므로 이 중에서 IBD channel만 이용하고자 하였는데, 그러기 위해서는 다음 식을 계산하여야 합니다.

$$
\frac{\mathrm{d} N}{\mathrm{~d} E\_0}=\left.N\_p T \int\_{E\_{\mathrm{IBD}}^{\text {thr }}}^{\infty} \sigma\_{\bar{\nu}\_e}^{\mathrm{IBD}}(E) \frac{\mathrm{d}F}{\mathrm{d}E}\right|\_{\bar{\nu}\_e} \mathcal{G}\left(E\_0 ; E\_{\mathrm{v}}, \delta_E\right) \mathrm{d} E
$$

* $N\_p$ : Total number of target protons in the LS (Liquid Scintillator)

* $T$ : Effective running time

* $E\_{\mathrm{IBD}}^{\text {thr }}$ : The threshold energy for IBD

* $\sigma\_{\bar{\nu}\_e}^{\mathrm{IBD}}(E)$ : $\bar{\nu}\_e$ IBD cross section

* $\dfrac{\mathrm{d}F}{\mathrm{d}E}$ : $\bar{\nu}\_e$ flux

* $\mathcal{G}\left(E\_0 ; E\_{\mathrm{v}}, \delta_E\right)$ : Gaussian function of $E\_0$ (Resolution function)

* $E\_{\mathrm{v}} = m\_e + E\_{e^+}$ : The visible energy in the detector

언뜻보면 이미 $\mathrm{d}F/\mathrm{d}E$를 알고 있으므로 계산이 수월할 것 같지만, 각 변수들을 모두 대입하고 적분을 하면 다음과 같은 그림을 얻을 수 있습니다.

-----

## A. Footnotes {#footnotes}

[1] : B. Dasgupta, R. Laha, and A. Ray, [Phys. Rev. Lett. 125, 101101 (2020)](http://dx.doi.org/10.1103/PhysRevLett.125.101101), [arXiv:1912.01014 [hep-ph]](https://arxiv.org/abs/1912.01014).