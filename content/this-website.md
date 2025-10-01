---
Title: This Website
Date: 2025-09-30
Category: Projects
Summary: A static site generated from Markdown using modified Pelican.
Tags: Web Development, Python, JavaScript
---

The pages are generated from raw Markdown files, which allows editing it to be straightforward and allows me to focus on just creating the content. The source code is located [on GitHub](github.com/kchoislattery/portfolio) and the website is built by a GitHub runner on push. This page serves both as a test and demonstration of features.

## Equations

Just like normal markdown, this supports inline equations, such as $ax^2+bx+c$. It also supports more advanced block equations, such as this (from my [branch and bound example](https://github.com/KChoiSlattery/branch-and-bound/blob/main/example.ipynb)):

$$
\begin{align}
    \mathrm{minimize}\quad &||\mathbf{Ax}-\mathbf{b}||_2^2\nonumber\\
    \text{subject to}\quad & \mathbf{x} \in \{0, 1\}^n,\nonumber\\
    & ||\mathbf{x}||_0=k\nonumber\\
\end{align}
$$

## Code Blocks

Code blocks are natively supported by Pelican-bootstrap, and is compiled to HTML using pygment. This example is from my [Python implementation of a sparse null-space algorithm](https://github.com/KChoiSlattery/sparse-null-space).

```python
from scipy import sparse
from sparse_null import sparse_null

A = sparse.random_array((1000, 15000), density=0.001, rng=12)
H = sparse_null(A, show=True) # show=True enables a progress bar

# Verify that each column of H produces 0 when multiplied into A, should be 8.9e-16
print((A @ H).max())
```

## Images

Images are also supported and are loaded via normal Markdown syntax:

![Camera ring drawing](images/camera-ring-drawing.png)
<center><i>Figure captions are currently implemented via HTML injection in the Markdown. I hope to change this in the future.</i></center>

## PDFs

I can also render PDFs by injecting the [ViewerJS](https://viewerjs.org/) Javascript library and getting Pelican to recognize it:

<iframe src = "ViewerJS/#../documents/aas-poster.pdf" class = "pdf-viewer"> </iframe>
