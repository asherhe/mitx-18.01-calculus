---
title: Quadratic Approximation
description: Because we like parabolas
---

Now we have linear approximations, but what if we wanted to go one power *higher*?

That's the point of quadratic approximations.

At the moment, we can only approximate lines. But virtually all the functions we know are *curved*, not straight. And our linear approximations can't really account for that. If we knew if a function was curving upward or downward, we could get even *more* accuracy.

So how do we do it?

The "curve" of a function can be expressed as $f''(x)$ — the second derivative of $f$. If constants represents the value of $f$ itself and lines represent $f'$, then quadratics should deal with $f''$.

Let's first try at $x=0$, because we all like zero.

We want to find the quadratic $ax^2+bx+c$, so that it's equal to $f(0)$, its derivative is equal to $f'(0)$, and its second derivative is equal to $f''(0)$. At $x=0$, everything involving an $x$ magically disappears, leaving us with just $c$. So $c=f(0)$. If we take the derivative of this quadratic, we have $2ax+b$. Setting $x$ to zero will get rid of the $2ax$ and we're left with $b$. So $b=f'(0)$. At last, we take the derivative *again* and now we have just a $2a$, and at this point, $x$ doesn't even matter anymore. So $2a=f''(0)$, or $a=\frac{f''(0)}2$. Putting it all together:

$$
Q(f)=f(0)+f'(0)\cdot x+\frac{f''(0)}2\cdot x^2
$$

If we want to slide $x$ around, we can put an $a$ for zero and a $x-a$ for $x$:

$$
Q(f)=f(a)+f'(a)(x-a)+\frac{f''(a)}2(x-a)
$$

<iframe src="https://www.desmos.com/calculator/hgtcp67rnm?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

<center><sup>Note: You can drag the point around — <i>If you can catch it!</i></sup></center>

Here's the quadratic approximations for a few important functions:

- $\sin x\approx x$ — $\sin x$ ain't much of a parabola
- $\cos x\approx1-\frac{x^2}2$​
- $(1+x)^r\approx1+rx+\frac{r(r-1)x^2}2$​
- $e^x\approx1+x+\frac{x^2}2$
- $\ln(x+1)\approx x-\frac{x^2}2$ — Try working out the first and second derivatives of $\ln(x+1)$ yourself.
- $\text{Polynomials}\approx\text{Remove anything higher than a quadratic}$. See the reasoning with polynomials on linear approximation

Like linear approximations, quadratic approximations also have a set of rules for manipulating basic functions into more advanced functions. What's more, they look pretty much the same. Addition and subtraction, if you have read my notes on linear approximation already, are pretty much the same with quadratic approximations.

Multiplication is also the same, but I'll give the proof here anyways because it's exciting.

---

What we're trying to prove right now is that $Q(fg)=Q(Q(f)Q(g))$. Let's first expand $Q(fg)$.

For the sake of brevity, I'm going to omit the $(a)$ from things like $f(a)$, $g'(a)$, and $f''(a)$. In addition, I'll write $(x-a)$ as a plain 'ole $x$, because typing four extra characters is a bit of a pain.

$$
\begin{align*}
Q(fg)&=fg+(fg)'\cdot x+\frac{(fg)''}2\cdot x^2 \\
     &=fg+(f'g+fg')x+\frac{(f'g+fg')'}2\cdot x^2 \\
     &=fg+(f'g+fg')x+\frac{(f''g+f'g')+(f'g'+fg'')}2\cdot x^2 \\
     &=fg+(f'g+fg')x+\frac{f''g+2f'g'+fg''}2\cdot x^2
\end{align*}
$$

And now let's also expand $Q(Q(f)(Q(g))$

$$
\begin{align*}
Q(Q(f)Q(g))&=Q\left(\left(f+f'\cdot x+\frac{f''}2\cdot x^2\right)\left(g+g'\cdot x+\frac{g''}2\cdot x^2\right)\right) \\
           &=fg+f'g\cdot x+fg'\cdot x+\frac{f''g}2\cdot x^2+\frac{fg''}{2}x^2+f'g'\cdot x^2 \\
           &=fg+x(f'g+fg')+\frac{x^2}2(f''g+2f'g'+fg'')
\end{align*}
$$

And as we can see, all is well because those two are equal.

---

Along with quadratic approximation, we also have this thing for tracking the size of the error called big-O notation. If you've studied algorithms before, this may sound rather familiar to you.

Technically speaking, if $f(x)$ is on the order of $x^n$ — meaning that the dominant term is $x^n$ — then we can say that $f(x)=O(x^n)$, meaning that $|f(x)|\le kx^n$.

In our case, we're only dealing with powers, but in other applications, the dominant term could be any function you want (although I've never seen anything involving the trig functions yet).

And to be even more specific, we're working on quadratic approximations near $x=0$, so we won't have to deal with anything lower than $O(x^3)$.

So let's start with an example — because I'm bad at coming up with examples that make sense at all, I'm just going to use the Car Loan example.

> Suppose that you take out a $15,000 loan to purchase a car. The loan has an interest rate of 3% per year, compounded monthly.
>
> The formula for the amount of interest accrued over a time period T measured in number of months is
> 
> $$
> A=15000\left(1+\frac{.03}{12}\right)^T−15000
> $$
> 
> Use a quadratic approximation to approximate the amount of *interest* accrued over 4 years.

Well first of all, because decimals and fractions don't go together well, let's first get rid of the $.03$ in the fraction. $\frac{.03}{12}=\frac3{1200}=\frac1{400}$. So our interest is

$$
A=15000\left(1+\frac1{400}\right)^T-15000
$$

Exponents are tricky to handle, and $\frac1{400}\approx0$, so we can use a quadratic approximation to simplify this

$$
\begin{align*}
A&=15000\left(1+\frac1{400}\right)^T-15000 \\
 &=15000\left(1+\frac T{400}+\frac{T(T-1)}{2\cdot400^2}\right)-15000 \\
\end{align*}
$$

We know that $T=48$, so this thing evaluates to 1905.75.

Actually, to be more accurate (or at least to admit that quadratic approximation isn't flawless), we also have an error term embedded in there, so this is actually

$$
A=15000\left(1+\frac T{400}+\frac{T(T-1)}{2\cdot400^2}+\text{Error}\right)-15000
$$

But in quadratic approximation, all errors are on the order of $x^3$ because $x^3$ is much more significant compared to $x^4$, $x^5$, etc.

So we can be even more precise and say that

$$
A=15000\left(1+\frac T{400}+\frac{T(T-1)}{2\cdot400^2}\right)-15000+O\left(x^3\right)
$$

In our expression, $x=\frac1{400}$​. But big-O notation also comes with a constant expression. So let's find that expression.

First of all, the vanilla, coefficientless $x^3$ is $\left(\frac1{400}\right)^3=\frac1{64000000}$.

That's *really* small.

If we calculate the *actual* value of $A$​ (which is a misery to do by hand), we get $A\approx1909.92$​. So the error in our approximation is $|1909.92-1905.75|=4.17$​. If we lived in the good 'ole days before we had calculators, I don't think anybody would've complained, because a loss of \$4.17 isn't much to cry about.

But anyways the magnitude of the error here is $\frac{4.17}{\frac1{64000000}}=4.17\cdot64000000=266880000$.

48 months is kind of short, but if we stretched this out to something like 10 *years*, we'd be having some *serious* problems with our approximations. Problems of up to \$70.93. Which won't make you very happy.

But at that point, just your interest *alone* is already \$5240.30, so an extra \$71 isn't too much to worry about  