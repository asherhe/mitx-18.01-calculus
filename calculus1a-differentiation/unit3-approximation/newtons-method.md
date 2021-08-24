---
title: Newton's Method
description: Because algebra is kinda complicated
---

Sometimes we want to find the roots of a function (a really scary one like $x^4-\sin x^3+\left(\frac12\right)^x+x-5$), and our traditional methods of factorization don't work. What can we do?

When we can't find an *exact* answer (probably because it doesn't really exist, or because we can't express it), we can at least approximate it.

Newton's method, although very straightforward-sounding, is actually very useful (and fast, unless you have a *really* bad function).

To use Newton's method, say on our really scary function $f(x)=x^4-\sin x^3+\left(\frac12\right)^x-5$​, we first pick a point, preferably near one of the roots.

<iframe src="https://www.desmos.com/calculator/l63l2veeuw?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

As we can see from the graph, $f(x)$ has x-intercepts near $\pm1$​. I'm just going to demonstrate at $x=1$ for now, you can try $x=-1$ later. 

So first we pick our guess #1, $x_0$. We guessed the root to be near $x=1$, so $x_0=1$.

Now we draw the tangent line to $f(x_0)$. The equation of the tangent line at $x_0$ is $y=f(x_0)+f'(x_0)(x-x_0)$. Our second, closer guess would be where this tangent line intersects the x-axis. So we set $y=0$ in that equation and solve:

$$
\begin{align*}
f(x_0)+f'(x_0)(x-x_0)&=0 \\
f'(x_0)(x-x_0)&=-f(x_0) \\
x-x_0&=-\frac{f(x_0)}{f'(x_0)} \\
x&=x_0-\frac{f(x_0)}{f'(x_0)}
\end{align*}
$$

Now let's call guess #2 $x_1$. Now we draw the tangent line at $x_1$ and solve for $x_2=x_1-\frac{f(x_1)}{f'(x_1)}$. And this goes on and on, for $x_3$, $x_4$, $x_5$, and so on, until we get a really, *really* good approximation.

So let's try it out with $f(x)$.

Recall that $f(x)=x^4-\sin x^3+\left(\frac12\right)^x+x-5$​​. We have the tools to take the derivative of this, so let's do it:

$$
\begin{align*}
\frac d{dx}f(x)&=\frac d{dx}x^4-\frac d{dx}\sin x^3+\frac d{dx}\left(\frac12\right)^x+\frac d{dx}x-\frac d{dx}5 \\
               &=4x^3-\sin'x^3\left(\frac d{dx}x^3\right)+\left(\frac12\right)^x\ln\frac12+1 \\
               &=4x^3-3x^2\cos x^3+\left(\frac12\right)^x\ln\frac12+1
\end{align*}
$$

So now we can start making guesses.

Here's a short Python program that makes the guesses for us:

```python
from math import sin, cos, log # math.log is the natural logarithm. Dunno why it's not math.ln though.

def newtonsMethod(f, fPrime, x, guesses):
	'''
	Given an initial guess (x) and the amount of guesses to make (guesses), try to approximate the roots of the function f. fPrime is the derivative of f
	'''
	if (guesses == 0):
		return
	
	print(x)
	newtonsMethod(f, fPrime, x - f(x) / fPrime(x), guesses - 1)


f = lambda x: x**4 - sin(x**3) + 0.5**x + x - 5
fPrime = lambda x: 4 * x**3 - 3 * x**2 * cos(x**3) + log(0.5) * 0.5**x + 1

newtonsMethod(f, fPrime, 1, 10)
```

This program outputs the following:

```
1
2.101879474639997
1.7748433842121978
1.294664757852773
1.4020671061385952
1.386461279026028
1.3861288627862816
1.386128709127082
1.386128709127049
1.386128709127049
```

Right at the end, $x_8$ and $x_9$ both converge to $\approx1.386128709127049$, which would be our answer up to 15 decimal places. If we go any further, the program would still output $1.386128709127049$​ because that's the furthest decimals go for the program.

And here's an animated demonstration of newton's method:

<iframe src="https://www.desmos.com/calculator/x0y3bi9sjo?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

Now, *how fast does Newton's method converge*? Because it seems pretty fast to me.

Well, we can find *basically* how fast it converges.

Let's say we have $\varepsilon_n$ for the error in our $n$-th estimate. Let's also say that the *actual* root is $x^*$. This means that $\varepsilon_n=x^*-x_n$. We also then have $\varepsilon_{n+1}=x^*-x_{n+1}$. Recall that $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$. So now we have $\varepsilon_{n+1}=x^*-\left(x_n-\frac{f(x_n)}{f'(x_n)}\right)=x^*-x_n+\frac{f(x_n)}{f'(x_n)}=\varepsilon_n+\frac{f(x_n)}{f'(x_n)}$. So now we need to find $f(x_n)$.

The tangent line at $f(x_n)$ has the equation $f(x)\approx f(x_n)+f'(x_n)(x-x_n)+O((x-x_n)^2)$. Now let's say we wanted to plug $x^*$ into $f(x)$. This turns into:

$$
f(x^*)=f(x_n)+f'(x_n)(x^*-x_n)+O((x^*-x_n)^2)
$$

Notice that $x^*-x_n=\varepsilon_n$. So $f(x^*)$ is actually

$$
f(x^*)=f(x_n)+f'(x_n)\varepsilon_n+O(\varepsilon_n^2)
$$

But earlier we said that $x^*$ was a root of $f(x)$, so $f(x^*)$ is actually zero. Now we can solve for $f(x_n)$

$$
\begin{align*}
f(x_n)+f'(x_n)\varepsilon_n+O(\varepsilon_n^2)&=0 \\
f(x_n)&=-f'(x_n)\varepsilon_n+O(\varepsilon_n^2)&O(n)\text{ represents the order of growth, so the sign doesn't matter} \\
\end{align*}
$$

Now we can plug it into the equation for $\varepsilon_{n+1}$:

$$
\begin{align*}
\varepsilon_{n+1}&=\varepsilon_n+\frac{f(x_n)}{f'(x_n)} \\
                 &=\varepsilon_n+\frac{-f'(x_n)\varepsilon_n+O(\varepsilon_n^2)}{f'(x_n)} \\
                 &=\varepsilon_n-\varepsilon_n+\frac{O(\varepsilon_n^2)}{f'(x_n)} \\
                 &=\frac{O(\varepsilon_n^2)}{f'(x_n)}
\end{align*}
$$

Since the slope of $f$ in that small area in which most of our guesses are should be *roughly* the same, our errors scale down quadratically.

However, there is one exception to this — if the slope of $x_0$ is almost flat, the tangent line leads us *very* far away from our starting point. Lots of things could also go wrong if the slope runs hog-wild at that point (as is the case with values near $x=0$ for $\sin\frac1x$).

To demonstrate, let's use $f(x)=\atan x$. If we pick any $x_0$ outside the range of about $(-1.391745,1.391745)$​, our guesses get further and further from the origin. If you don't believe me, try it for yourself.

<iframe src="https://www.desmos.com/calculator/y8amx1ipr7?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>
