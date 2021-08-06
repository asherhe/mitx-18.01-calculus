---
title: The Chain Rule
description: '"Using the chain rule is like peeling an onion: you have to deal with each layer at a time, and if it is too big you will start crying."'
---

We can add, subtract, multiply, and divide functions. There's still a lot we can't do though. For example, we can't find the derivative of $\sin x^3$, because we don't have any rule about the sine of a function. This is where the chain rule comes in.

So basically, the whole point of the chain rule is to find what happens if we take the derivative of $f(g(x))$ (hence the *chain* part of the chain rule). We have no idea what this is, so let's find out.

The derivative of $f(g(x))$​ is the combined effect of both $f(x)$​ and $g(x)$​. Just so that our equations don't freak you out, let's let $u=g(x)$​. This will make our equations a lot nicer when we finish. If we move $x$​ by a bit (we'll call it $\Delta x$​), then $g(x)$​ will move by roughly $\Delta x\cdot g'(x)$​ ($\Delta x$​ will be going to zero anyways so don't complain about the fact that this isn't precise). This change in $g$​ will also show up in $f$​. So not only will $f$​ change by whatever it's supposed to change by, it'll also change by however much $g$​ changed. Rather than having $f(x)$​ change by $x$​, it'll change by $g(x)=u$​, because we have $g(x)$​ flipping $f(u)$​'s switches, meaning that $f(u)$​ now changes by $f'(u)\cdot g(x)$​. So in the end, the whole thing changes by $f'(g(x))\cdot g'(x)$​. Although this looks kind of sad in prime notation, but it looks all clean and elegant in Leibniz notation:
$$
\frac{df}{dx}=\frac{df}{du}\cdot\frac{du}{dx}
$$
It even seems as if $du$​ can cancel out! (of course, that's not really how life works — it's just notation). How nice.

With this, [some](../unit1-the-derivative/calculating-derivatives) [other](./product-rule) [rules](./quotient-rule), and [a bunch of functions](../derivatives-of-functions), we can find the derivatives of absolutely monstrous expressions like this:
$$
5\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3 - }{x^2 - 2x + \tan(x) - 3}}\right)^8
$$
In fact, let's do it as practice!

## Factoring a monster expression

So suppose we have
$$
f(x) = 5\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)^8
$$
And we want to find the derivative of this for whatever reason.

To find the derivative of this, let's first think through how we would evaluate this normally.

We see something that looks like $5(\dots)^8$​, so we evaluate the stuff in brackets first. Inside, we encounter $6x^2+\dots$ — we just add the two up. The $\dots$ correspond to a square root $\sqrt{\sin(3x)+\dots}$ — we find the stuff in the square root and take the square root of that. We now encounter a fraction, which is $\frac{4x^3}{x^2-2x+\tan x-3}$ — we calculate each side and divide them.

The process for taking the derivative would be similar.

We have a coefficient of 5, so we multiply everything that follows by it. We then have a bunch of stuff to the eighth power, so we find the derivative of the stuff inside and use the chain rule. Inside, we have a function ($6x^2$) being added to another function (a big boy $\sqrt{}$) The square root is again another sum, which involves a quotient, that we deal with with the quotient rule. The numerator and the denominator should be easy enough from then.

So let's do it.

Just so that we don't scare little kids, I'm going to use functions for some of the expressions, because without the functions, it's madness. Of course, I'm going to show you the madness first
