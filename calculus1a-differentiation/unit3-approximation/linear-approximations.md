---
title: Linear Approximations (And measurement error)
description: Because we all make mistakes sometimes
---

Linear approximations are quite useful in math — many of the tools we found were using linear approximation in one way or another. But linear approximations are also helpful when the math we need to work out is too complicated for the whole function and we're focusing on a small range of values.

Finding linear approximations is a system somewhat like finding derivatives — we have a few linear approximations for functions, and also a few properties.

Here are a few of our basic functions for linear approximations:

**Sine** — $\sin x\approx x$ for $x$ close to zero. If we take the equation of the tangent line at $x=0$, we have $\sin0 + \sin'0(x-0)=0+x\cos0=x$. If we graph $\sin x$ and zoom in really closely on $(0,0)$, we see that $\sin x$ is pretty much indistinguishable from the line $y=x$.

**Cosine** – following the same logic with sine, we get $\cos x\approx 1$ for $x$​ near 0.

**Stuff raised to a power** — $x^r$ is kind of boring — it's always zero. $(1+x)^r$ however, becomes $1+rx$. This doesn't seem all that useful, but we can do a lot of stuff with this, as we'll find out later.

**The exponential function** — The function $e^x$ was defined to have a slope of 1 at $x=0$. It also evaluates to $e^1=1$, so the tangent line is $y=x+1$.

**Logarithmic Function** — Taking the logarithm of 0 (for any base) is absolutely ridiculous, so we instead take the next best thing — $\ln(x+1)$, which shifts it over so that whatever *was* at $x=1$ is now at $x=0$. The derivative of $\ln$ at $x=0$ is $x$, and $\ln(0+1)=0$, so the tangent line is $y=x$​.

**Polynomials** — The linear approximation of a polynomial at $x=0$​​​ is just the constant and linear terms of that polynomial! To reason that through, let's first find $f(0)$​. Since this is a polynomial, everything with an $x$ term gets cancelled, leaving us with only the constant term. Then we encounter a $f'(0)$. If we take the derivative, the constant term vanishes into nothingness, our linear term becomes constant, and everything else still has an $x$ stuck to it. If we then set $x$​ to zero, all that's left is just our linear term. Another way to interpret this is that, because we're looking at values near $x=0$, $x^2$, $x^3$, and other higher terms are negligible compared to $x$, so we just overlook them.

In general, to find the equation of the linear approximation of a function $f(x)$​​​ at $x=a$​​​ would be $y=f(a)+f'(a)(x-a)$​​. See if you can figure out why this works.​

---

We can also combine the linear approximations of these functions to approximate even more functions. For the rest of this page, just note that most of the time, we'll be approximating around $x=0$ anyways, so all of the $x-a$ stuff can just be simplified to $x$.

First of all, let's reason through what happens if we add two functions. Suppose we have two functions — say $\sin x$ and $e^x$. If we add them together, it has the effect of adding their approximations together.

We can also prove this (I'll do this for the rest of the properties too). Let's say that we have a function $L$ that takes a function as an input (which sounds kind of strange at first, but it's quite helpful and even shows up a lot in functional programming) and finds its linear approximation at the point $x=a$. Then $L(f)$ will be defined to be

$$
L(f)=f(a)+f'(a)(x-a)
$$

This is basically our definition of the tangent line.

And what are we trying to prove?

We wanted to find $L(f+g)$, and we think it'll be $L(f)+L(g)$. So we're trying to prove that $L(f+g)=L(f)+L(g)$. We can just fine the values of each and check if they're equal.

$$
L(f+g)=(f+g)(a)+(f+g)'(a)(x-a)
      =f(a)+g(a)+[f'(a)+g'(a)](x-a)
$$

Notice that we used the addition of derivatives to find $(f+g)'$.

Now we find $L(f)+L(g)$

$$
\begin{align*}
L(f)+L(g)&=[f(a)+f'(a)(x-a)]+[g(a)+g'(a)(x-a)] \\
         &=f(a)+f'(a)(x-a)+g(a)+g'(a)(x-a) \\
         &=f(a)+g(a)+[f'(a)+g'(a)](x-a)
\end{align*}
$$

And we see that they are equal.

Subtraction will go pretty much the same way, except that it's a $-$ instead of a $+$.

Now what about multiplication?

Let's try an example — $e^x\sin x$. Let's graph all of them out, along with their linear approximations near $x=0$

<iframe src="https://www.desmos.com/calculator/9ek6dg4foi?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

If we take the product of the linear approximations of $e^x$ and $\sin x$, we get $x(x+1)=x^2+x$, while the actual result is $x$. This is because we're looking for a *linear* approximation, meaning that we discard anything higher than a $x$.

So how do we prove that $L(fg)=L(L(f)L(g))$? Remember that we wrap the right-hand side with a $L$ because we only want the linear terms.

Let's first expand $L(fg)$. From here, I'll be using just the function name, rather than including the inputs — $f(a)$ becomes $f$, $g'(a)$ becomes $g$, and so on and so forth — otherwise the math would be too complicated.

$$
\begin{align*}
L(fg)&=fg+(fg)'(x-a) \\
     &=fg+(f'g+fg')(x-a)
\end{align*}
$$

And now for the hard part — expanding $L(L(f)L(g))$

$$
\begin{align*}
L(L(f)L(g))&=L((f+f'(x-a)) \\
           &\;\;\;\;\;\;\;\;\;(g+g'(x-a))) \\
           &=fg+f'g(x-a)+fg'(x-a) \\
           &=fg+(f'g+fg')(x-a)
\end{align*}
$$

Notice that we excluded $f'g'(x-a)^2$ from the equation. This is because we were already looking for a linear approximation, so there was no point in keeping the quadratic term. And since the two results are equal, it all works out.

---

Sometimes, what we want to approximate doesn't look like a clean $e^x$​, $\cos x$​, or whatever. Solving that revolves around substituting some expression for a variable that *is* close to zero (for strange ones like $\ln(1+x)$​, I mean that we want $x$​ to be close to zero, not $1+x$​). For example, if we wanted to approximate $e^{x+1}$​ near $x=0$​, we can't just simply do it directly because $x+1\not\approx 0$​. Instead, we set a variable $u=x+1$​ so that 

Sometimes, our expression doesn't exactly match the form of the easy-to-approximate functions, so we have to make it that way. For example, suppose we want to find $(5+\sin x)^2$​​​​​. This seems a bit like $(1+x)^r$​​​, but not exactly, since we have a 5 rather than 1. We can factor the 5 out of this to get $5^2\cdot(1+\frac{\sin x}5)^2$​​. Since $\frac{\sin x}5$​​ nears zero as $x$​​ nears zero, we can rewrite this as $25\left(1+2\left(\frac{\sin x}5\right)\right)\approx25\left(1+2\cdot\frac x5\right)=25+10x$.

Also, we can represent quotients with a $(\dots)^{-1}$. But then that means the inside must approach 1.

## Accounting for Measurement Error

Nothing is perfect. Especially when we measure things with our puny rulers. That's why, in lots of real-life use cases, we usually have a $\pm\text{whatever}$​ after a measurement. Calculating measurement error was rather confusing at first. I'll just use the example on the course.

There's a really tall building on MIT campus called the Green Building (which was once apparently turned into a giant Tetris game, from what I've heard). To demonstrate calculus, they decided to measure its height, by measuring the angle it makes at a certain distance.

To calculate that distance, they just had this rope that they used to measure the distance.

And to find the angle, they used this protractor with a dangling string perpendicular to the ground.

And also, since the observer isn't lying flat on the ground, we also had to account for the eye height of the observer.

Here is a diagram of It all:

![See table below.](https://openlearninglibrary.mit.edu/assets/courseware/v1/4fd3055c881f14b6ee4b57d09c758fb4/asset-v1:MITx+18.01.1x+2T2019+type@asset+block/images_greenbld_diagram.svg)

And here are the measurements they got:

| Quantity                   | Variable | Measurement                 | Error                     |
| -------------------------- | -------- | --------------------------- | ------------------------- |
| Height to Jen's eyeball    | $h$      | 4.9 ft                      | &pm; .01 ft               |
| Distance to Green building | $x$      | 175 ft                      | &pm; 3 ft                 |
| Angle                      | $\theta$ | $57^\circ=\frac{19}{60}\pi$ | $\pm3^\circ=\frac\pi{60}$ |

We can do some simple trigonometry and find that $y=h+x\tan\theta=4.9\text{ ft}+175\text{ ft}\cdot\tan57^\circ\approx274.376\text{ ft}$​.

I also want to point out that all of these measurements had some error associated to it.

- Errors in $h$ could result from the fact that the ground wasn't exactly flat, or that the measurement of Jen's height wasn't exactly accurate.
- Errors in $x$ could be a result of the rope not being very exact, the rope not being aligned perfectly, or even the rope being stretched.
- Errors in $\theta$ could arise from the fact that the string wasn't exactly perpendicular to the ground, or the fact that the protractor isn't at eye level.

For a bit of background here, there are two types of observational error — random errors and systematic errors.

Random errors are a result of things that are beyond our control. For example, misalignment of the rope and wind can cause our measurements to change.]

Systematic errors arise from problems with our measuring devices. For example, $\theta$ might also be inexact because Jen isn't holding the protractor at *exactly* eye level, and $x$ could've been off because the rope might've expanded or shrunk from temperature or handling.

So in reality, our diagram looks a bit more like this:

![Each variable includes a small error.](https://openlearninglibrary.mit.edu/assets/courseware/v1/d37cb727913f5ab0ae7c0a4fb3dc4b91/asset-v1:MITx+18.01.1x+2T2019+type@asset+block/images_greenbld_diagram2.svg)

Now comes the question — how do we calculate $\Delta y$?

Our formula for finding $y$ was $y=h+x\tan\theta$. We're not very concerned about the $h$ term here, but the harder part is $\tan\theta$. How do we find the change for this?

Let's try to find $\tan(\theta+\Delta\theta)$. $\theta+\Delta\theta$ is our measurement angle, so using the definition of tangent:

$$
\begin{align*}
\tan(\theta+\Delta\theta)&=\frac{(y+\Delta y)-(h+\Delta h)}{x+\Delta x} \\
                         &=\frac{\Delta y-\Delta h+(y-h)}{x+\Delta x} \\
                         &=\frac{\Delta y-\Delta h+x\tan\theta}{x+\Delta x} \\
(x+\Delta x)\tan(\theta+\Delta\theta)&=\Delta y-\Delta h+x\tan\theta \\
\Delta y&=(x+\Delta x)\tan(\theta+\Delta\theta)+\Delta h-x\tan\theta \\
\end{align*}
$$

At this point, we should try to find a linear approximation of $\tan(\theta+\Delta\theta)$. We can let $x=\theta+\Delta\theta$, and approximate near $x=\theta$, meaning $x-\theta=\Delta\theta$

$$
\tan(\theta+\Delta\theta)=\tan\theta+\Delta\theta\tan'\theta=\tan\theta+\Delta\theta\sec^2\theta
$$

And so we can substitute this back into our equation and continue to do algebra

$$
\begin{align*}
\Delta y&=(x+\Delta x)\tan(\theta+\Delta\theta)+\Delta h-x\tan\theta \\
        &=(x+\Delta x)(\tan\theta+\Delta\theta\sec^2\theta)+\Delta h-x\tan\theta \\
        &=(x\tan\theta+x\Delta\theta\sec^2\theta+\Delta x\tan\theta+\Delta x\Delta\theta\sec^2\theta)+\Delta h-x\tan\theta \\
        &=x\Delta\theta\sec^2\theta+\Delta x\tan\theta+\Delta x\Delta\theta\sec^2\theta+\Delta h \\
        &=x\Delta\theta\sec^2\theta+\Delta x\tan\theta+\Delta h    &\Delta x\Delta\theta\text{ is almost negligable compared to everything else, so we can ignore it}
\end{align*}
$$

Now we can just plug our data in and calculate it.

In case you forgot, here's the table

| Quantity                   | Variable | Measurement                 | Error                     |
| -------------------------- | -------- | --------------------------- | ------------------------- |
| Height to Jen's eyeball    | $h$      | 4.9 ft                      | &pm; .01 ft               |
| Distance to Green building | $x$      | 175 ft                      | &pm; 3 ft                 |
| Angle                      | $\theta$ | $57^\circ=\frac{19}{60}\pi$ | $\pm3^\circ=\frac\pi{60}$ |

So

$$
\begin{align*}
\Delta y&=x\Delta\theta\sec^2\theta+\Delta x\tan\theta+\Delta h \\
        &\le175\text{ ft}\cdot\frac\pi{60}\cdot\sec^2\frac{19}{60}\pi+3\text{ ft}\cdot\tan\frac{19}{60}\pi+0.01\text{ ft} \\
        &\approx35.52\text{ ft}
\end{align*}
$$

Apparently, the Green building is actually 295 feet tall, which fits within our error margin.

To sum it up, the whole point of using linear approximations in calculating error margins is so that we can convert some crazy function (like tangent) into a line, which is much easier to deal with.