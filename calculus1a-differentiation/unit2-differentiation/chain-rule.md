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
5\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan(x) - 3}}\right)^8
$$

In fact, let's do it as practice!

## Derivative of a Monster Expression

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

Caution: Algebra may scare the heck out of you

$$
\begin{align*}
\frac{df}{dx} 
&= \frac{d}{dx} 5\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)^8 \\

&= 5\left(8\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)^7 
 + \left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)'\right) \\
&= 5\left(8\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)^7 
 + \left(12x + \left(\sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)'\right)\right) \\
 
&= 5\left(8\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)^7 
 + \left(12x + \left(\frac1{2\sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}}\right)
 \left(\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}\right)'\right)\right) \\
 
&= 5\left(8\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)^7 
 + \left(12x + \left(\frac1{2\sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}}\right)
 \left(\sin(3x) + \left(\frac{4x^3}{x^2 - 2x + \tan x - 3}\right)'\right)\right)\right) \\
 
&= 5\left(8\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)^7 
 + \left(12x + \left(\frac1{2\sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}}\right)
 \left((\sin(3x))'
 + \frac{12x^2(x^2-2x+\tan x-3)
 - 4x^3(x^2-2x+\tan x-3)'}
 {(x^2-2x+\tan x-3)^2}\right)\right)\right) \\
&= 5\left(8\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)^7 
 + \left(12x + \left(\frac1{2\sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}}\right)
 \left(3\cos(3x)
 + \frac{12x^2(x^2-2x+\tan x-3)
 - 4x^3(2x^2-2+\sec^2 x)}
 {(x^2-2x+\tan x-3)^2}\right)\right)\right) \\
\end{align*}
$$

And now we begin the long and arduous process of simplifying

$$
5\left(8\left(6x^2 + \sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}\right)^7 
 + \left(12x + \left(\frac1{2\sqrt{\sin(3x) + \frac{4x^3}{x^2 - 2x + \tan x - 3}}}\right)
 \left(3\cos(3x)
 + \frac{12x^2(x^2-2x+\tan x-3)
 - 4x^3(2x^2-2+\sec^2 x)}
 {(x^2-2x+\tan x-3)^2}\right)\right)\right) \\
$$

Of course, we can do this by hand, but at this point, I'd rather just Wolfram\|Alpha it, since the $\TeX$ typesetting is even more nightmarish than the algebra.

$$
81920\left(72x^2+2\sqrt{62x+\sin(3x)+\tan(x)-3}\right)^7+\frac{5}{2}\sqrt{62x+\sin(3x)+\tan(x)-3}\left(144x^2\left(x^2-2x+\tan(x)-3\right)-\frac{64x^3\left(4x^2+\sec^2(x)-2\right)}{\left(x^2-2x+\tan(x)-3\right)^2}+3\cos(3x)\right)+60x
$$

All of this algebra reminds me of this quote:

> <span style="font-size: xx-large">“What do you think? Should we leave this up to freak out my algebra kids next period?”</span>
>
> [— Calculus teacher, with a particularly long chain rule problem on the board](https://mathprofessorquotes.com/post/643311134854774784/what-do-you-think-should-we-leave-this-up-to)

Note: It's kind of hard for me to tell if I did this correctly. If I didn't do this correctly, please make your complaint here:

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeBZf9CggbKeJ4wL8Jg45VpVej-q75eVVr2EZ7YWUvFG_vb7A/viewform?embedded=true" width="640" height="637" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>

