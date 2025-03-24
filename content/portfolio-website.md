---
Title: This portfolio website
Date: 2024-09-17
Category: Side projects
Summary: A static site hosted on Github Pages generated from markdown documents using Pelican. 
---

*It's alive!*

The pages are generated from raw markdown files, which allows editing it to be straightforward and allows me to focus on just creating the content. Features include:

## Headers

### Subheaders

## Equations

Just like normal markdown, this supports inline equations, such as $ax^2+bx+c$, as well as more advanced block equations, such as this nonsense equation:

$$\int_{\mathbb{R}}\left\{\left[\frac{\log{a}}{\sqrt{b}}+\mu^{-2\alpha}\right]\left[\left(\begin{pmatrix}\sigma_{xx} & 0 \\ 0 & \sigma_{yy}\end{pmatrix}\mathbf{q}\times\mathbf{w}\right)\cdot\mathbf{p}\right]\right\}\sin{\theta}\, d\mu$$

## Images

Also just like normal markdown, this supports images:
![Camera ring drawing](images/camera-ring-drawing.png)

## PDFs

This is a little funkier because it required injecting the [ViewerJS](https://viewerjs.org/) Javascript library into Pelican and requires me to put raw HTML into my markdown, which makes the source code unsightly, but here's an example of a PDF: 
<iframe src = "ViewerJS/#../documents/aas-poster.pdf" class = "pdf-viewer"> </iframe>