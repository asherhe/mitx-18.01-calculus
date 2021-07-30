---
title: Calculating Derivatives
description: Because guessing is boring
---

Since we can represent the derivative as a function, there's no rule saying that we can't define a value for this function. And at the moment, the only way we can actually find the derivative of a function is only guesswork. So how do we go about evaluating the derivatives of whole *functions*?

The process is quite similar to finding the derivatives of specific values.

Suppose we want to find the derivative of the function $f(x)=\frac1x$. If you remember our [definition of the derivative](./what-is-the-derivative), we have:

$$
\begin{align*}
f'(x)=\lim_{h \to 0} \frac{f(x + h) - f(x)} h
&= \lim_{h \to 0} \frac{\frac1{x + h} - \frac1x}h \\
&= \lim_{h \to 0} \frac{\frac{x - (x + h)}{x (x + h)}} h \\
&= \lim_{h \to 0} \frac{\frac{-h}{x (x + h)}} h \\
&= \lim_{h \to 0} -\frac1{x(x+h)} \\
&= -\frac1{x^2}
\end{align*}
$$

And now we have the derivative of a function, as a function, for which we can just directly plug in values and get a result, instead of doing a long computation with limits for only a specific value.

## Properties of Derivatives from Limit Laws

Now using our [limit laws](../unit0-limits/introduction-to-limits#some-properties-of-limits), we can derive some properties of derivatives (haha).

First of all, if we have $g(x)=kf(x)$​, then it means that $g'(x)=kf'(x)$​. This can easily be proven:

$$
\begin{align*}
g'(x)=\lim_{\Delta x \to 0} \frac{g(x + \Delta x) - g(x)} {\Delta x}
&= \lim_{\Delta x \to 0} \frac{kf(x + \Delta x) - kf(x)} {\Delta x} \\
&= \lim_{\Delta x \to 0} k\left(\frac{f(x + \Delta x) - f(x)} {\Delta x}\right) \\
&= \lim_{\Delta x \to 0} k\lim_{\Delta x \to 0} \left(\frac{f(x + \Delta x) - f(x)} {\Delta x}\right) \\
&= kf'(x)
\end{align*}
$$
We also have "the derivative of the sum is the sum of the derivatives." Again, we can use the Limit Law of Addition to deal with this. Out of $\TeX$ typesetting laziness, I won't show the proof here, but it should be easy enough.

Difference of derivatives is somewhat similar to sum of derivatives. However, note that this doesn't exactly work for product and quotient of derivatives — I think that'll appear sometime later.

And finally, we have the power rule, which is actually very easy once you understand it, and it'll also make computing the derivative of a polynomial a piece of cake. Basically, if $f(x)=	x^n$​, then $f'(x)=nx^{n-1}$​. There are two ways of proving this — an algebraic way and a geometric way (that's not as rigorous but more intuitive). 3Blue1Brown has a great explanation of the geometric proof [here](https://www.youtube.com/watch?v=S0_qX4VJhMQ&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr&index=3), so I guess I'll explain the algebraic one.

So suppose that $f(x)=x^n$
