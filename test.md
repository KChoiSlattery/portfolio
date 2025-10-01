

# Nomenclature

  Symbol                  Definition
  ----------------------- ----------------------------------------------
  $P, p$                  Parallel power collected by AFN
  $S, s$                  Perpendicular power collected by AFN
  $C_{\scriptstyle{P}}$   Parallel scattering cross-section
  $C_{\scriptstyle{S}}$   Perpendicular scattering cross-section
  $D, \delta$             Particle diameter
  $m$                     Complex refractive index of particle
  $N, n$                  Real part of particle refractive index
  $k$                     Imaginary refractive index, $m=n-ik$
  $B$                     Incident irradiance (power/area) on particle

# Parallel and perpendicular cross-sections

The cross-sections have units of area and represent the quantity that,
when multiplied by the incident irradiance $B$, return the power
incident on the AFN optics due to scattering from the particle:
$$\begin{equation}
\begin{bmatrix}
    P\\
    S
\end{bmatrix}=
B
\begin{bmatrix}
    C_{\scriptstyle{P}}\\
    C_{\scriptstyle{S}}
\end{bmatrix}
\end{equation}$$ They are calculated using the equations:
$$\begin{align}
    C_{\scriptstyle{P}}&=A\int_{\Omega_{col}}|S_2(\theta, x, m)|^2\ d\Omega \label{eq:sigmap}\\
    C_{\scriptstyle{S}}&=A\int_{\Omega_{col}}|S_1(\theta, x, m)|^2\ d\Omega. \label{eq:sigmas}
\end{align}$$ where $A$ is the particle's geometric cross-section,
$$\begin{equation}
    A=\frac{\pi}{4}D^2.
\end{equation}$$ $S_1$ and $S_2$ are calculated using the methods
described in, e.g., [@bohren_absorption_2004] or
[@prahl_miepython_2023], but normalized such that, when integrated
around all angles, they are equal to the particle's total scattering
efficiency $Q_{sca}$, which represents the ratio of total scattered
power to power incident on the particle: $$\begin{equation}
    \int_{4\pi}|S_1(\theta, x, m)|^2+|S_2(\theta, x, m)|^2\ d\Omega=Q_{sca}.
\end{equation}$$ $x$ represents the size parameter, $$\begin{equation}
    x=\frac{\pi D}{\lambda},
\end{equation}$$ with $\lambda$ the excitation wavelength (outside of
the particle).

The integrations in equations
[\[eq:sigmap\]](#eq:sigmap){reference-type="ref" reference="eq:sigmap"}
and [\[eq:sigmas\]](#eq:sigmas){reference-type="ref"
reference="eq:sigmas"} are performed by integrating in spherical
coordinates and making the substitution that $d\Omega$ represents a
differential solid angle, $d\Omega=\sin{\theta}d\phi d\theta$.

For an arbitrary collector with an angular profile defined by a window
$\nu(\theta)=\phi_{max}(\theta)-\phi_{min}(\theta)$, $$\begin{align}
    C_{\scriptstyle{P}}&=A\int_{\theta_{min}}^{\theta_{max}}|S_2(\theta, x, m)|^2\nu(\theta)\sin{\theta}d\theta \label{eq:sigmapint}\\
    C_{\scriptstyle{S}}&=A\int_{\theta_{min}}^{\theta_{max}}|S_1(\theta, x, m)|^2\nu(\theta)\sin{\theta}d\theta \label{eq:sigmasint}
\end{align}$$

For a collector with the geometry of the AFN, the window function
$\nu(\theta)$ is given by [@hodkinson_response_1965] as:
$$\begin{equation}
\label{weightfn}
    \nu(\theta)=2\arccos\left(\frac{\cos \alpha -\cos \theta_c\cos \theta }{\sin \theta_c \sin \theta }\right)
\end{equation}$$ with $\alpha$ the angular half-aperture of the circular
collector and $\theta_c$ the polar angle of the center of the collector.

For computation, equations
[\[eq:sigmapint\]](#eq:sigmapint){reference-type="ref"
reference="eq:sigmapint"} and
[\[eq:sigmasint\]](#eq:sigmasint){reference-type="ref"
reference="eq:sigmasint"} must be discretized: $$\begin{align}
    C_P&=\frac{\pi D^2}{4}\sum_{i}|S_2(\theta_i, x, m)|^2 \nu(\theta_i)\sin{\theta_i}\ \Delta\theta\\
    C_S&=\frac{\pi D^2}{4}\sum_{i}|S_1(\theta_i, x, m)|^2 \nu(\theta_i)\sin{\theta_i}\ \Delta\theta
\end{align}$$

# Ensembles of particles

Let $W_{\scriptscriptstyle{P}}$ and $W_{\scriptscriptstyle{S}}$ be
random variables representing additive noise to the signal.
$W_{\scriptscriptstyle{P}}$, $W_{\scriptscriptstyle{S}}$, $D$, $N$, and
$B$ are all random continuous variables. Let also
$\mathbf{U}=\begin{bmatrix}
    P & S
\end{bmatrix}^\intercal$ be the measurement vector and
$\mathbf{C}(\delta, n): \mathbb{R}^2\mapsto \mathbb{R}^2$ be the
function that maps a diameter and refractive index to a pair of
cross-sections, so that $$\begin{equation}
    \mathbf{U}=B\mathbf{C}(D, N)+\begin{bmatrix}W_{\scriptscriptstyle{P}}\\W_{\scriptscriptstyle{S}}\end{bmatrix}
\end{equation}$$ When a particle is sampled from the ensemble, it is
picked randomly from the joint probability density function
$f(w_{\scriptscriptstyle{P}}, w_{\scriptscriptstyle{S}},\delta, n, b)$.
The probability that $\mathbf{U}$ falls within a specific set of values
$\mathcal{U}$ is given by $$\begin{multline}
\label{eq:ubinprob}
    \mathrm{Pr}[\mathbf{U}\in \mathcal{U}]=\\
    \int\!\!\underset{\mathrm{\times5}}{\cdots}\!\!\int1_{\mathcal{U}}\left(b\mathbf{C}(\delta, n)+\begin{bmatrix}w_{\scriptscriptstyle{P}}\\w_{\scriptscriptstyle{S}}\end{bmatrix}\right)\\
    f(w_{\scriptscriptstyle{P}}, w_{\scriptscriptstyle{S}}, \delta, n, b)\,dw_{\scriptscriptstyle{P}}\,dw_{\scriptscriptstyle{S}}\,db\,dn\,d\delta
\end{multline}$$ where the integrals are across all possible values of
the integration variables and $1_{\mathcal{U}}(\mathbf{u})$ is the
indicator function of $\mathcal{U}$: $$\begin{equation}
    1_{\mathcal{U}}(\mathbf{u})=\begin{cases}
        1 & \textrm{if } \mathbf{u} \in \mathcal{U}\\
        0 & \textrm{otherwise}
    \end{cases}
\end{equation}$$

Since $W_{\scriptscriptstyle{P}}$, $W_{\scriptscriptstyle{S}}$, and $B$
are all independent variables, $$\begin{multline}
    f(w_{\scriptscriptstyle{P}}, w_{\scriptscriptstyle{S}}, \delta, n, b)=\\
    f_{\scriptscriptstyle{D, N}}(\delta, n)\cdot f_{\scriptscriptstyle{B}}(b)\cdot f_{\scriptscriptstyle{W_{\scriptscriptstyle{P}}}}(w_{\scriptscriptstyle{P}})\cdot
    f_{\scriptscriptstyle{W_{\scriptscriptstyle{S}}}}(w_{\scriptscriptstyle{S}}).
\end{multline}$$ Substituting into equation
[\[eq:ubinprob\]](#eq:ubinprob){reference-type="ref"
reference="eq:ubinprob"}, $$\begin{multline}
\label{eq:ubinprob2}
    \mathrm{Pr}[\mathbf{U}\in \mathcal{U}]=
    \iint \mathrm{Pr}[\mathbf{U}\in\mathcal{U}|\delta, n]\,f_{\scriptscriptstyle{D, N}}(\delta, n)\,dn\,d\delta
\end{multline}$$ where $\mathrm{Pr}[\mathbf{U}\in\mathcal{U}|\delta, n]$
represents that particle with diameter $\delta$ and refractive index $n$
produces a measurement within $\mathcal{U}$, given by $$\begin{equation}
    \mathrm{Pr}[\mathbf{U}\in\mathcal{U}|\delta, n]=\int \mathrm{Pr}[\mathbf{U}\in\mathcal{U}|\delta, n, b]f_{\scriptscriptstyle{B}}(b) \, db
\end{equation}$$ where
$\mathrm{Pr}[\mathbf{U}\in\mathcal{U}|\delta, n, b]$ is the probability
that the aforementioned particle, having fallen within a part of the
beam with intensity $b$, produces a measurement within $\mathcal{U}$.

For normally-distributed $W_{\scriptscriptstyle{P}}$,
$W_{\scriptscriptstyle{S}}$, with standard deviations
$\sigma_{\scriptscriptstyle{P}}$, $\sigma_{\scriptscriptstyle{S}}$ and
rectangular $\mathcal{U}$ defined by lower-bounds ($p_0$, $s_0$) and
upper-bounds ($p_1$, $s_1$),
$\mathrm{Pr}[\mathbf{U}\in\mathcal{U}|\delta, n, b]$ is given
analytically as $$\begin{multline}
    \mathrm{Pr}[\mathbf{U}\in\mathcal{U}|\delta, n, b]=\\ \frac{1}{4}\left(\mathrm{erf}\left(\frac{p_1-bC_{\scriptscriptstyle{P}}}{\sigma_{\scriptscriptstyle{P}}\sqrt{2}}\right)-\mathrm{erf}\left(\frac{p_0-bC_{\scriptscriptstyle{P}}}{\sigma_{\scriptscriptstyle{P}}\sqrt{2}}\right)\right)\\
    \cdot\left(\mathrm{erf}\left(\frac{s_1-bC_{\scriptscriptstyle{S}}}{\sigma_{\scriptscriptstyle{S}}\sqrt{2}}\right)-\mathrm{erf}\left(\frac{s_0-bC_{\scriptscriptstyle{S}}}{\sigma_{\scriptscriptstyle{S}}\sqrt{2}}\right)\right)
\end{multline}$$

The transformation from the space of probability density functions to
the space of measured histograms is thus a linear operator which acts on
the function $f_{\scriptscriptstyle{D, N}}(\delta, n)$. We denote this
linear operator as $\bm{R}$, so that $$\begin{equation}
    \bm{R}f_{\scriptscriptstyle{D, N}}=\begin{bmatrix}
        \mathrm{Pr}[\mathbf{U}\in\mathcal{U}_1]\\
        \mathrm{Pr}[\mathbf{U}\in\mathcal{U}_2]\\
        \vdots
    \end{bmatrix}
\end{equation}$$ with $\mathcal{U}_1$, $\mathcal{U}_2$, etc. the bins
chosen for the 2D histogram.

# Numerical representation of $f_{\scriptscriptstyle{D, N}}$

In order to invert the measured data to find
$f_{\scriptscriptstyle{D, N}}(\delta, n)$, it is decomposed into a
linear combination of basis functions ${\psi(\delta, n)}$ with
coefficients $\{a\}$: $$\begin{equation}
    f_{\scriptscriptstyle{D, N}}(\delta, n)\approx\sum_{j}a_j\psi_{j}(\delta, n)
\end{equation}$$ This transformation can be represented as a linear
operator $\bm{\Psi}$: $$\begin{equation}
    f_{\scriptscriptstyle{D, N}}\approx\bm{\Psi}\mathbf{a}\textrm{, }\mathbf{a}=\begin{bmatrix}a_1\\a_2\\\vdots\end{bmatrix}
\end{equation}$$ Because $\mathbf{C}(\delta, n)$ is extremely sensitive
to both $\delta$ and $n$, repeatedly performing the integration in
equation [\[eq:ubinprob2\]](#eq:ubinprob2){reference-type="ref"
reference="eq:ubinprob2"} to a reasonable precision is infeasible.
However, due to the linearity of equation
[\[eq:ubinprob2\]](#eq:ubinprob2){reference-type="ref"
reference="eq:ubinprob2"}, $$\begin{equation}
    \mathrm{Pr}[\mathbf{U}\in \mathcal{U}_i]\approx\sum_j a_j\cdot\mathrm{Pr}[\mathbf{U}\in \mathcal{U}_i|\psi_j]
\end{equation}$$ where $$\begin{equation}
\label{eq:rpsi}
    \mathrm{Pr}[\mathbf{U}\in \mathcal{U}_i|\psi_j]=\iint \mathrm{Pr}[\mathbf{U}\in\mathcal{U}_i|\delta, n]\psi_j(\delta, n)\,dn\,d\delta.
\end{equation}$$ Each integral can be evaluated individually, before the
inversion, and then the operation of evaluating a guess for
$f_{\scriptscriptstyle{D, N}}$ can be performed as a matrix operation:
$$\begin{equation}
    \bm{R}\bm{\Psi}\mathbf{a}\approx\begin{bmatrix}
        \mathrm{Pr}[\mathbf{U}\in\mathcal{U}_1]\\
        \mathrm{Pr}[\mathbf{U}\in\mathcal{U}_2]\\
        \vdots
    \end{bmatrix}
\end{equation}$$ If non-negative functions are chosen as the basis, then
by constraining $\mathbf{a}$ to be non-negative, all possible values of
$\bm{\Psi}\mathbf{a}$ will be as well.

# Inverse problem

In the inverse problem, data is collected and binned. The number of
particles that fell into each bin are recorded as $$\begin{equation}
\mathbf{h}=\begin{bmatrix}h_1\\h_2\\\vdots\end{bmatrix},
\end{equation}$$ where $h_i$ represents the number of particles that
fell within the $i$'th bin. At a high level, the inverse algorithm can
be stated as $$\begin{multline}
    \hat{f}_{\scriptscriptstyle{D, N}}=\bm{\Psi}\mathbf{\hat{a}},\ {\mathbf{\hat{a}}}=\underset{\mathbf{a}}{\operatorname{argmin}}\ \Delta(\eta\bm{R}\bm{\Psi}\mathbf{a}, \mathbf{h})+\epsilon L(\bm{\Psi}\mathbf{a})\\
    \textrm{such that} \begin{cases}
        \operatorname{min}\mathbf{a}\geq0\\
        \iint\bm{\Psi}\mathbf{a}\, dn\,d\delta=1
    \end{cases}
\end{multline}$$ where

- $\eta$ is the number of particles observed.

- $\Delta(\bm{R}\bm{\Psi}\mathbf{a}, \mathbf{h})$ is some statistical
  divergence between the probabilities produced by
  $\bm{R}\bm{\Psi}\mathbf{a}$ (the model) and measured by $\mathbf{h}$
  (the data).

- $L(\bm{\Psi}\mathbf{a})$ is the regularizer loss function, which
  quantifies how non-smooth the argument is.

- $\epsilon$ is the regularization parameter, which determines how much
  the loss function should be weighted.

## Divergence functions

### Sum of squared differences

The sum of the squared differences, denoted as $$\begin{equation}
\Delta_{L^2}(\mathbf{x}, \mathbf{y})=||\mathbf{x}-\mathbf{y}||_2^2=\sum_{i}(x_i-y_i)^2,
\end{equation}$$ is simple to code, quick to compute and generates
similar output to the other divergence function for most test samples,
but has little mathematical backing. In particular, it considers all
elements of $\mathbf{h}$ to be of equal reliability when, in theory,
bins with smaller probabilities should have smaller variances in
$\mathbf{h}$.

### Inverse likelihood

The inverse likelihood function is inversely related to the probability
that, under the probabilities produced by the model, the samples
$\mathbf{h}$ are drawn. It is given by $$\begin{equation}
\Delta_{\mathcal{L}}(\mathbf{x},\mathbf{h})=-\sum_{i}h_i\log(x_i)
\end{equation}$$ and is derived from the multinomial distribution.

## Regularizer functions

### Integral of squared Laplacian

This is the only regularizer function I have extensively tested. Because
the Laplacian is a linear operator, this can be implemented as a matrix
operation and an $L^2$ norm. $$\begin{equation}
    L_{\nabla^2}(f_{\scriptscriptstyle{D}, \scriptscriptstyle{N}})=\iint\left[\left(\frac{\partial^2}{\partial \delta^2}+\frac{\partial^2}{\partial n^2}\right)f_{\scriptscriptstyle{D}, \scriptscriptstyle{N}}(\delta, n)\right]^2\, dn\,d\delta
\end{equation}$$
