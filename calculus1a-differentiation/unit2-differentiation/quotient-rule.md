---
title: The Quotient Rule
description: Because Multiplication ain't Enough
---

We now have the product rule, but since we have products, we must also have quotients. As with products, $\frac{d}{dx}\left(\frac{f(x)}{g(x)}\right)\ne\frac{f'(x)}{g'(x)}$. It's actually more complicated than that (you saw that coming, didn't you?). Let's find it.

As much as I like to use Leibniz notation, it's going to be a bit more convenient to use Prime notation here, so let's say that $h(x)=\frac{f(x)}{g(x)}$. To find $h'$, we again use the definition of the derivative

$$
h'(x)=\frac{\Delta h}{\Delta x}
$$

Instead of diving straight into the algebra, let's find how we can express $\Delta h$ in terms of $f$, $g$, $\Delta f$, and $\Delta g$. This is a rather trivial task:

$$
\Delta h=\frac{f+\Delta f}{g+\Delta g}-\frac fg
$$

Fractions are kind of tricky to deal with, so let's combine this under one common denominator.

$$
\Delta h=\frac{f+\Delta f}{g+\Delta g}-\frac fg=\frac{g(f+\Delta f)-f(g+\Delta g)}{g(g+\Delta g)}=\frac{\Delta f\cdot g - f\cdot\Delta g}{g^2+g\cdot \Delta g}
$$

Now don't forget about $\Delta x$! We still need to divide by that:

$$
\frac{\Delta h}{\Delta x}=\frac{\frac{\Delta f\cdot g - f\cdot\Delta g}{g^2+g\cdot\Delta g}}{\Delta x}=\frac{\frac{\Delta f\cdot g - f\cdot\Delta g}{\Delta x}}{g^2+g\cdot\Delta g}
$$

Let's look away from the denominator and focus on the numerator. We have a bunch of delta's on the top and a delta on the bottom, which reminds us of derivatives. Let's try

$$
\frac{\Delta f\cdot g - f\cdot\Delta g}{\Delta x}=\frac{\Delta f\cdot g}{\Delta x}-\frac{\Delta g\cdot f}{\Delta x}=\frac{\Delta f}{\Delta x}g-\frac{\Delta g}{\Delta x}f=f'\cdot g-f\cdot g'
$$

And now we throw this back into our $\frac{\Delta h}{\Delta x}$ expression. Don't forget that all of our delta's are approaching 0

$$
\frac{\Delta h}{\Delta x}=\frac{\frac{\Delta f\cdot g - f\cdot\Delta g}{\Delta x}}{g^2+g\cdot\Delta g}=\frac{f'\cdot g-f\cdot g'}{g^2+g\cdot\Delta g}=\frac{f'\cdot g-f\cdot g'}{g^2}
$$

And there we have it — the quotient rule.

What can we do with it?

Obviously, we can find derivatives with it. Many of our trig functions are just sine and cosine flipped around and divided. So we can find the derivatives of those.

## Trig Functions with the Quotient Rule

First, remember that

$$
\begin{align*}
\frac{d}{dx}\sin x&=\cos x \\
\frac{d}{dx}\cos x&=-\sin x
\end{align*}
$$

Now let's first deal with tangent. Tangent is defined to be $\frac{\sin x}{\cos x}$. So we can just use the quotient rule and chug along with the algebra:

$$
\begin{align*}
\frac{d}{dx}\tan x=\frac{d}{dx}\left(\frac{\sin x}{\cos x}\right)
&=\frac{(\sin x)'\cos x-\sin x(\cos x)'}{\cos^2x} \\
&=\frac{(\cos x)\cos x-\sin x(-\sin x)}{\cos^2x} \\
&=\frac{\cos^2x+\sin^2x}{\cos^2x} \\
&=\frac{1}{\cos^2x} \\
&=\sec^2x
\end{align*}
$$

To find $\frac{d}{dx}\cot x$, we *could* do this again except with $\frac{\cos x}{\sin x}$, but there's a slightly easier way — we use the quotient rule *again*, but this time on $\frac1{\tan x}$:

$$
\begin{align*}
\frac{d}{dx}\cot x=\frac{d}{dx}\left(\frac{1}{\tan x}\right)
&=\frac{(1)'\cdot\tan x-1(\tan x)'}{\tan^2x} \\
&=\frac{0\cdot\tan x-1(\sec^2 x)}{\tan^2x} \\
&=-\frac{\sec^2x}{\tan^2x} \\
&=-\frac{\frac1{\cos^2x}}{\frac{\sin^2x}{\cos^2x}} \\
&=-\frac1{\sin^2x} \\
&=-\csc^2x
\end{align*}
$$

And now we do this on $\sec x$, which is $\frac1{\cos x}$:

$$
\begin{align*}
\frac{d}{dx}\sec x=\frac{d}{dx}\left(\frac1{\cos x}\right)
&=\frac{(1)'\cdot \cos x-1(\cos x)'}{\cos^2x} \\
&=\frac{0\cdot\cos x-1(-\sin x)}{\cos^2x} \\
&=\frac{\sin x}{\cos^2x} \\
&=\frac{\frac{\sin x}{\cos x}}{\cos x} \\
&=\frac{\tan x}{\cos x} \\
&=\sec x\tan x
\end{align*}
$$

And we can do a similar process with $\csc x$:

$$
\begin{align*}
\frac{d}{dx}\csc x=\frac{d}{dx}\left(\frac1{\sin x}\right)
&=\frac{(1)'\cdot \sin x-1(\sin x)'}{\sin^2x} \\
&=\frac{0\cdot\sin x-1(\cos x)}{\sin^2x} \\
&=-\frac{\cos x}{\sin^2x} \\
&=\frac{\frac{\cos x}{\sin x}}{\sin x} \\
&=\frac{\cot x}{\sin x} \\
&=\csc x\cot x
\end{align*}
$$

And so we now have:

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

