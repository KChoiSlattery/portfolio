---
Title: AFN Modeling
Date: 2023-01-01
Category: Projects
Summary: Simulation of data from the Autofluorescence Nephelometer
Tags: 
Status: draft
---

## Parallel and perpendicular cross-sections

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
    C_{\scriptstyle{S}}&=A\int_{\theta_{min}}^{\theta_{max}}|S_1(\theta, x, m)|^2\nu(\theta)\sin{\theta}d\theta 
\end{align}$$

For a collector with the geometry of the AFN, the window function
$\nu(\theta)$ is given by [@hodkinson_response_1965] as:
$$\begin{equation}
    \nu(\theta)=2\arccos\left(\frac{\cos \alpha -\cos \theta_c\cos \theta }{\sin \theta_c \sin \theta }\right)
\end{equation}$$ with $\alpha$ the angular half-aperture of the circular
collector and $\theta_c$ the polar angle of the center of the collector.

For computation, equations
[\[eq:sigmapint\]](#eq:sigmapint){reference-type="ref"
reference="eq:sigmapint"} and
[\[eq:sigmasint\]](#eq:sigmasint){reference-type="ref"
reference="eq:sigmasint"} are be discretized: $$\begin{align}
    C_P&=\frac{\pi D^2}{4}\sum_{i}|S_2(\theta_i, x, m)|^2 \nu(\theta_i)\sin{\theta_i}\ \Delta\theta\\
    C_S&=\frac{\pi D^2}{4}\sum_{i}|S_1(\theta_i, x, m)|^2 \nu(\theta_i)\sin{\theta_i}\ \Delta\theta
\end{align}$$

## Fast computation of many cross-sections

This is enough information to calculate $C_P$ and $C_S$, but by expanding $S_1$ and $S_2$, it can be represented in a form that is much faster to calculate.

$$ S_2(\theta, x, m) = \sum_{n=1}^{\infty}\frac{2n+1}{n(n+1)}(a_n(x,m)\tau_n(\theta)+b_n(x,m)\pi_n(\theta)) $$
$$ S_1(\theta, x, m) = \sum_{n=1}^{\infty}\frac{2n+1}{n(n+1)}(a_n(x,m)\pi_n(\theta)+b_n(x,m)\tau_n(\theta)) $$

where $a_n(x,m)$ and $b_n(x,m)$ are complex coefficients specific to the particle calculated recursively, and $\pi_n(\theta)$ and $\tau_n(\theta)$ are real coefficients that depend only on angle. Since
$$ |S_2|^2=S_2S_2^*, $$
where $(\cdots)^*$ denotes complex conjugation,

$$ |S_2|^2=\left[\sum_{k=1}^{\infty}\frac{2k+1}{k(k+1)}[a_k\tau_n(\theta)+b_k\pi_k(\theta)]\right]\left[\sum_{l=1}^{\infty}\frac{2l+1}{l(l+1)}[a_l^*\tau_l(\theta)+b_l^*\pi_l(\theta)]\right] $$
$$ |S_2|^2=\sum_{k=1}^{\infty}\sum_{l=1}^{\infty}\left(\frac{2k+1}{k(k+1)}\right)\left(\frac{2l+1}{l(l+1)}\right)[a_k\tau_n(\theta)+b_k\pi_k(\theta)]a_l^*\tau_l(\theta)+b_l^*\pi_l(\theta)] $$
$$ |S_2|^2=\sum_{k=1}^{\infty}\sum_{l=1}^{\infty}\left(\frac{2k+1}{k(k+1)}\right)\left(\frac{2l+1}{l(l+1)}\right)[a_ka_k^*\tau_k(\theta)\tau_l(\theta)+a_kb_l^*\tau_k(\theta)\pi_l(\theta)+b_ka_l^*\pi_k(\theta)\tau_l(\theta)+b_kb_l^*\pi_k(\theta)\pi_l(\theta)] $$

substituting into the first equation,
$$ C_P=\frac{\pi \delta^2}{4}\int_{\theta_{0}}^{\theta_{1}}\left[\sum_{k=1}^{\infty}\sum_{l=1}^{\infty}\left(\frac{2k+1}{k(k+1)}\right)\left(\frac{2l+1}{l(l+1)}\right)[a_ka_k^*\tau_k(\theta)\tau_l(\theta)+a_kb_l^*\tau_k(\theta)\pi_l(\theta)+b_ka_l^*\pi_k(\theta)\tau_l(\theta)+b_kb_l^*\pi_k(\theta)\pi_l(\theta)]\right] \nu(\theta)\sin{\theta}\ \,d\theta.$$

The integral can then be distributed as:

$$ C_P=\sum_{k=1}^{\infty}\sum_{l=1}^{\infty}\left(\frac{2k+1}{k(k+1)}\right)\left(\frac{2l+1}{l(l+1)}\right)[a_ka_k^*Q^{(1)}_{kl}+a_kb_l^*Q^{(2)}_{kl}+b*ka_l^*Q^{(2)}_{lk}+b*kb_l^*Q^{(3)}_{kl}] $$

(note the swapped indices of the second and third terms in square brackets), where

$$Q^{(1)}_{kl}=\int_{\theta_0}^{\theta_1}\tau_k(\theta)\tau_l(\theta)\nu(\theta)\sin(\theta)\,d\theta$$
$$Q^{(2)}_{kl}=\int_{\theta_0}^{\theta_1}\tau_k(\theta)\pi_l(\theta)\nu(\theta)\sin(\theta)\,d\theta$$
$$Q^{(3)}_{kl}=\int_{\theta_0}^{\theta_1}\pi_k(\theta)\pi_l(\theta)\nu(\theta)\sin(\theta)\,d\theta$$

Likewise,
$$ C_S=\sum_{k=1}^{\infty}\sum_{l=1}^{\infty}\left(\frac{2k+1}{k(k+1)}\right)\left(\frac{2l+1}{l(l+1)}\right)[a_ka_k^*Q^{(1)}_{kl}+a_kb_l^*Q^{(2)}_{kl}+b_ka_l^*Q^{(2)}_{lk}+b_kb_l^*Q^{(3)}_{kl}] $$

Since the $Q$ terms do not depend on the particle, only on the location of the detector, they can be pre-calculated for a fixed detector position, and then the only things that need to be calculated for each particle are the $a$ and $b$ coefficients.
