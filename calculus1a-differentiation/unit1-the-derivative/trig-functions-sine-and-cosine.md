---
title: Trigonometric Functions: Sine and Cosine
description: Because $\frac{d}{d\theta}\sin\theta$ matters too
---

In addition to polynomials, sine and cosine are also relatively easy functions to derive. So let's do it.

The function $\sin\theta$ is wave-like and repeating, so we'd expect that its derivative will also resemble a wave in some way. Let's find out with our definition of the derivative
$$
\begin{align*}
\frac{d}{d\theta}\sin\theta=\lim_{\Delta\theta \to 0} \frac{\sin(\theta+\Delta\theta)-\sin\theta}{\Delta\theta}
&=\lim_{\Delta\theta \to 0} \frac{\sin\theta\cos\Delta\theta+\cos\theta\sin\Delta\theta-\sin\theta} {\Delta\theta} \\
&=\lim_{\Delta\theta \to 0} \sin\theta\left(\frac{\cos\Delta\theta-1}{\Delta\theta}\right)
 +\lim_{\Delta\theta \to 0} \frac{\cos\theta\sin\Delta\theta}{\Delta\theta} \\
&=\cos\theta\left(\lim_{\Delta\theta \to 0}\frac{\sin\Delta\theta}{\Delta\theta}\right)
\end{align*}
$$
So the derivative of $\sin\theta$​ is just $\cos\theta$​  times whatever $\frac{\sin\Delta\theta}{\Delta\theta}$​ is as $\Delta\theta \to 0$​. We can find this geometrically using just the definition of sine and a unit circle.

![](/img/sineapproximation.png)

