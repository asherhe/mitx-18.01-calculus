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

And now we have the derivative of a function, as a function, for which we can just directly pug in values and get a result, instead of doing a long computation with limits for only a specific value.

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

We also have "the derivative of the sum is the sum of the derivatives." We can use the Limit Law of Addition to deal with this (I'll be writing this in [Leibniz Notation](./leibniz-notation) because it's slightly more convenient — I'm writing these notes *after* I watched the next section. 
$$
\begin{align*}
\frac{d}{dx} (f(x) + g(x))
&= \lim_{\Delta x \to 0} \frac{[f(x+\Delta x)+g(\Delta x)]-[f(x)-g(x)]}{\Delta x} \\
&= \lim_{\Delta x \to 0} \frac{[f(x+\Delta x)-f(x)] + [g(x+\Delta x)-g(x)]}{\Delta x} \\
&= \lim_{\Delta x \to 0} \frac{f(x+\Delta x)-f(x)}{\Delta x}
 + \lim_{\Delta x \to 0} \frac{g(x+\Delta x)-f(x)}{\Delta x} \\
&= f'(x)+g'(x)
\end{align*}
$$
Difference of derivatives is somewhat similar to sum of derivatives. Out of $\TeX$​​ typesetting laziness, I won't show the proof here. However, note that this doesn't exactly work for product and quotient of derivatives — I think that'll appear sometime later.

## The Power Rule

And finally, we have the power rule, which is actually very easy once you understand it, and it'll also make computing the derivative of a polynomial a piece of cake. Basically, if $f(x)=	x^n$​, then $f'(x)=nx^{n-1}$​. There are two ways of proving this — an algebraic way and a geometric way (that's not as rigorous but more intuitive). 3Blue1Brown has a great explanation of the geometric proof [here](https://www.youtube.com/watch?v=S0_qX4VJhMQ&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr&index=3), so I guess I'll explain the algebraic one.

So suppose that $f(x)=x^n$​, where $n>0$. $f'(x)$ would then be:

$$
\begin{align*}
\lim_{\Delta x\to0} \frac{f(x+\Delta x)-f(x)}{\Delta x}
&=\lim_{\Delta x\to0} \frac{(x+\Delta x)^n-x^n}{\Delta x} \\
&=\lim_{\Delta x\to0} \frac{[(x+\Delta x)-x]\left[(x+\Delta x)^{n-1}+(x+\Delta x)^{n-2}x+(x+\Delta x)^{n-3}x^2+\cdots+x^{n-1}\right]}{\Delta x} \\
&=\lim_{\Delta x\to0} \frac{\Delta x\left[(x+\Delta x)^{n-1}+(x+\Delta x)^{n-2}x+(x+\Delta x)^{n-3}x^2+\cdots+x^{n-1}\right]}{\Delta x} \\
&=\lim_{\Delta x\to0} \left[(x+\Delta x)^{n-1}+(x+\Delta x)^{n-2}x+(x+\Delta x)^{n-3}x^2+\cdots+x^{n-1}\right] \\
&= x^{n-1}+x^{n-2}x+x^{n-3}x^2+\cdots+x^{n-1} \\
&= nx^{n-1}
\end{align*}
$$

Of course, if $n=0$, we just have $f(x)=1$, and its derivative is obviously zero

Now if we want $n<0$, let $m=-n$​. I'm going to write this in [Leibniz notation](./leibniz-notation), which is a bit different from our current notation because we don't need to define a function to use Leibniz notation. I'm writing this right after I learned Leibniz notation, so I recommend you learn about Leibniz notation. We have:

$$
\begin{align*}
\frac{df}{dx}=\frac{d}{dx}\left(\frac1{x^m}\right)
&=\lim_{\Delta x \to 0} \frac{\frac1{(x + \Delta x)^m} - \frac1{x^m}}{\Delta x} \\
&=\lim_{\Delta x \to 0} \frac{\frac{x^m-(x+\Delta x)^m}{x^m(x + \Delta x)^m}}{\Delta x} \\
&=\lim_{\Delta x \to 0} \frac
{\left[x-(x+\Delta x)\right]\left[x^{m-1}+x^{m-2}(x+\Delta x)+x^{m-3}(x+\Delta x)^2+\cdots+(x+\Delta x)^{m-1}\right]}
{\Delta x[x(x+\Delta x)]^m} \\
&=\lim_{\Delta x \to 0} \frac
{-\Delta x\left[x^{m-1}+x^{m-2}(x+\Delta x)+x^{m-3}(x+\Delta x)^2+\cdots+(x+\Delta x)^{m-1}\right]}
{\Delta x[x(x+\Delta x)]^m} \\
&=\lim_{\Delta x \to 0} -\frac
{x^{m-1}+x^{m-2}(x+\Delta x)+x^{m-3}(x+\Delta x)^2+\cdots+(x+\Delta x)^{m-1}}
{[x(x+\Delta x)]^m} \\
&=-\frac{x^{m-1}+x^{m-2}x+x^{m-3}x^2+\cdots+x^{m-1}}{(x^2)^m} \\
&=-\frac{mx^{m-1}}{x^{2m}} \\
&=n\left(\frac{x^{-n-1}}{x^{-2n}}\right) \\
&=nx^{-n-1+2n} \\
&=nx^{n-1}
\end{align*}
$$

And it all works out, although the algebra was kind of crazy (even worse was the $\TeX$ typesetting).

I still haven't gotten around to proving this for any real number yet, but I'll prove someday. I think.

With our current rules for derivatives, we can easily take the derivative of a few function. First of all, the derivative of any polynomial would be:

$$
\frac d{dx}\left(c_0+c_1x+c_2x^2+\cdots+c_nx^n\right)=c_1+2c_2x+3c_3x^2+\cdots+nc_nx^{n-1}
$$
And if we know the derivatives of two functions, taking the derivative of their sum or difference won't be very hard.
