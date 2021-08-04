---
title: Leibniz Notation
description: Leibniz is a great guy. His name is kind of hard to spell though
---

So far, our notation for the derivative of a function $f(x)$ is $f'(x)$. But this gets kind of complicated when we want to express the derivative of an expression that isn't a function. Do we define an extra function? This kind of clutters up our formulas, so there's a much simpler method. For example, if we want to express the derivative of $x^3+2x^2$, rather than defining a function $f(x)=x^3+2x^2$ and then saying $f'(x)$, we can just say $\frac{d(x^3+2x^2)}{dx}$, or  $\frac{d}{dx}(x^3+2x^2)$ if our expression is very long.

And Leibniz Notation can also include functions and equations. If we have a function $f(x)$, we can just represent this as $\frac{df}{dx}$. If we have an equation $A=\pi r^2$, we can also write $\frac{dA}{dr}$ to denote how fast $A$ changes as $r$ changes.

And if we want to say that the derivative of something is equal to some expression, we can use $\frac{df}{dx}=3x^2+4x$.

To say that the derivative of some expression is equal to some value at a specific point ($f'(a)=b$ in prime notation), we can just use

$$
\left.\frac{df}{dx}\right|_{x=a}=b
$$

One great thing about Leibniz notation is that it actually shows you what the variables *mean*. If we just have a plain old function, $f(x)$, it could mean anything (we can at least get a bit more detail with $f(t)$, but it isn't too much help). But if we have, say, $\frac{dA}{dr}$, we know it has something to do with area ($A$) and radius ($r$)

Leibniz notation takes a while getting used to, but once you get used to it, you will realize how helpful it is.
