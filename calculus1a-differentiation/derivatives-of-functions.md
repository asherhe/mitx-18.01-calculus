---
title: Derivatives of Key Functions
description: Oh boy, a list! I love lists!
---

So here is a big fat list of the derivatives of most of the functions you'll ever need. Bookmark this list if you like, you'll be using this a lot.

## Derivative Properties

These actually aren't for specific functions, but actually for combining them.

[**Definition of Derivative**](./unit1-the-derivative/what-is-the-derivative)

$$
f'(x)=\lim_{\Delta x \to 0}\frac{\Delta f}{\Delta x}=\lim_{\Delta x \to 0} \frac{f(x - \Delta x) - f(x)}{\Delta x}
$$

**Linearity of Differentiation**

This is a generalization of a few [properties of derivatives](./unit1-the-derivative/calculating-derivatives#properties-of-derivatives-from-limit-laws) that we found.

$$
\frac{d}{dx}(a\cdot f(x)+b\cdot g(x)=a\cdot f'(x)+b\cdot g'(x)
$$

[**The Power Rule**](./unit1-the-derivative/calculating-derivatives#the-power-rule)

$$
\frac{d}{dx}x^n=nx^{n-1}
$$

[**The Product Rule**](./unit2-differentiation/product-rule)

$$
\frac{d}{dx}(f(x)g(x))=f(x)\cdot g'(x)+f'(x)\cdot g(x)
$$

[**The Quotient Rule**](./unit2-differentiation/quotient-rule)

$$
\frac{d}{dx}\left(\frac{f(x)}{g(x)}\right)=\frac{f'(x)\cdot g(x)-f(x)\cdot g'(x)}{g(x)^2}
$$

[**The Chain Rule**](./unit2-differentiation/chain-rule)
$$
\frac{d}{dx}f(g(x))=f'(g(x))g'(x)
$$

## Polynomial Stuff
$$
\begin{align*}
\text{Square function}   &\quad \frac{d}{dx}x^2=2x \\
\text{Cube function}     &\quad \frac{d}{dx}x^3=3x^2 \\
\text{Square root}       &\quad \frac{d}{dx}\sqrt x=\frac1{2\sqrt x} \\
\text{Powers in general} &\quad \frac{d}{dx}x^n=nx^{n-1} \\
\text{Polynomials}       &\quad \frac{d}{dx}\sum_{i=0}^n c_ix^i
                                           =\sum_{i=0}^n ic_ix^{i-1}
\end{align*}
$$

## [Trig Functions](./unit2-differentiation/quotient-rule#trig-functions-with-the-quotient-rule)

$$
\begin{align*}
\frac{d}{dx} \sin x &= \cos x \\
\frac{d}{dx} \cos x &= -\sin x \\
\frac{d}{dx} \tan x &= \sec^2 x \\
\frac{d}{dx} \cot x &= -\csc^2 x \\
\frac{d}{dx} \sec x &= \sec x \tan x \\
\frac{d}{dx} \csc x &= -\csc x \cot x
\end{align*}
$$