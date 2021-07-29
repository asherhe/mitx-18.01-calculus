---
title: What is the Derivative?
---

Put into normal-human-readable-words, the derivative of a function $f(x)$ at a point $a$ is how fast $f(x)$ is changing at that exact point $a$. This is a bit of an oxymoron, because for something to change, you've gotta give it time to change, but we're measuring change at an *instant*. But before we can understand how this is defined mathematically, let's first measure the rate of change over a period of time.

Measuring the change in $f(x)$ over a period from $a$ to $b$ looks like this:

$$
\frac {f(b) - f(a)} {b - a}
$$
We're calculating the change in $f$, and then the change in $x$. We can put this more simply as $\frac {\Delta f}{\Delta x}$​.

But what if we want to know what the rate of change is right at $a$

To answer that question, what happens if we move $b$ closer and closer to $a$?

As we move $b$​ closer, we see that we get closer to our rate of change at that *exact point*.

So would the answer be to simply set $b$ to $a$? Well, that wouldn't work

But we can take the *limit* as $b \to a$. So this becomes:
$$
f'(a) = \lim_{b \to a}\frac {f(b) - f(a)} {b - a}
$$
Alternatively, we can write:
$$
f'(a) = \lim_{h \to 0} \frac {f(a + h) - f(a)} h
$$
And then we can just look for the value of this limit, using our function $f$.

For a real-world example, suppose we throw a calculus textbook off of the very top of the Empire State building, and its trajectory is modeled (in meters above splat level) as $f(t)= 443 + 20t - 10t^2$​​, with $t$​ being the time since we threw the textbook. How fast is it going say, one second after you throw it?

We can just simply calculate the limit:
$$
\begin{align*}
f'(1)=\lim_{h \to 0} \frac {f(1 + h) - f(1)} h
&= \lim_{h \to 0} \frac{[443 + 20 (1 + h) - 10 (1 + h)^2] - [443 + 20(1) - 10(1)^2]} h \\
&= \lim_{h \to 0} \frac{(443 + 20 + 20h - 10 - 20h - 10h^2) - (443 + 20 - 10)} h \\
&= \lim_{h \to 0} \frac{10 h^2} h \\
&= \lim_{h \to 0} 10h \\
&= 0
\end{align*}
$$
So after 1 second, the textbook is going at $0\frac ms$. What does this mean? Is it floating in the air?

The derivative describes *instantaneous* rate of change, so right at the instant at which $t=1$​, the textbook will not move. If you imagine throwing something, at some point, it will reach the highest it'll go, and it'll start falling. At $t=1$​​, the textbook is perfectly at that peak point, so it appears that it won't be moving (but not for long)
