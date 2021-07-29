---
title: Limits of Quotients
title: What? We can divide by zero?
---

As we said in our [limit laws](./introduction-to-limits#some-properties-of-limits), $\lim_{x \to a}\frac{f(x)}{g(x)}$ exists *as long as* $M\ne0$. Now we raise an absurd question — what if $M$ *is* zero?

First of all, if $M$ is zero but $L$ is nonzero, this thing blows up to infinity or negative infinity, so that's boring. But what if we have $L=M=0$?

This sounds very silly indeed, because we all know that $\frac00$ is undefined. But what if we had something like:

$$
\lim_{x\to0}\frac{2x}x
$$

This is obviously 2 (if you don't belive me, graph it out somewhere), but it still results in a $\frac00$! How does this work?

As we saw in our example, dividing the two "zeros" gave us a nice, clean 2. But sometimes, it might collapse to zero, or it might blow up to &pm;infinity. So it's kind of hard to find the value of this.

One way we can do this is to factor both the numerator and denominator and try to eliminate common factors. For example, suppose we have:

$$
\lim_{x \to 1} \frac{x^2 + 2x - 3} {x^2 - 3x +2}
$$

If we just plug 1 in, we get a $\frac00$, which is bad. But we ca factor this:

$$
\begin{align*}
\lim_{x \to 1} \frac{x^2 + 2x - 3} {x^2 - 3x +2}
&= \lim_{x \to 1} \frac{(x - 1) (x + 3)} {(x - 1) (x - 2)} \\
&= \lim_{x \to 1} \frac{x + 3} {x - 2} \\
&=-4
\end{align*}
$$

When we solve limits of a quotient $\lim_{x \to a}\frac{f(x)}{g(x)}$, it's split into three cases. For simplicity, suppose that $\lim_{x \to a}f(x)=L$ and $\lim_{x \to a}g(x) = M$. Our three cases are:

1. $M\ne0$​ — we just divide $\frac LM$.

2. $L\ne0,M=0$ — the limit just blows up to &pm;infinity

3. $L=M=0$ — we have to do some factoring and whatnot to get a fraction that we *can* take the limit of (or for which the limit doesn't exist)

When we're graphing functions, a $DNE$​​ doesn't suffice — we want to know whether it goes bananas, skyrockets, or plummets. A function never settling down doesn't happen when we deal with quotients, and this is called "limits of quotients," so we can ignore that. To check whether a limit is positive or negative infinity, we just plug in closer and closer values to our limit (coming from the left or right), and reason through that the sign would be.
