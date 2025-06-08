## Exercise: Is this function linear? 

This exercise shows how to plot three functions and shows the visual difference between linear and non-linear functions

## Libraries

Install the required libraries:
```bash
pip install matplotlib numpy
```

## What is a linear function or linear combination?

A function $f(x_1, x_2, ..., x_n)$ is **linear** if it satisfies:

* **Additivity**: $f(a + b) = f(a) + f(b)$
* **Homogeneity**: $f(ca) = c \cdot f(a)$

And it looks like:

$$
f(x_1, x_2, ..., x_n) = a_1x_1 + a_2x_2 + \cdots + a_nx_n
$$

Where $a_1, a_2, ..., a_n$ are constants.

## Let's look at the examples:

### Linear:

**3x₁ + 2x₂**

* This is a linear combination of $x₁$ and $x₂$ with constants 3 and 2.
* No powers, products of variables, or functions like sin or exp.

### Not Linear:

**3x₁² + 2x₂**

* Here, $x₁$ is **squared**.
* Squaring a variable breaks the rules of linearity — it's no longer proportional.

### Not Linear:

**3x₁ + 2sin(x₂)**

* The sine of $x₂$ is a **nonlinear transformation**.
* Linear functions can't include trigonometric, exponential, or logarithmic functions of variables.

---

## Intuition:

A **linear function** must form a **plane (or hyperplane)** in space. If the function curves (like a parabola or sine wave), it’s **not linear**.

---

## Summary Table

| Expression          | Linear? | Reason                          |
| ------------------- | ------- | ------------------------------- |
| $3x_1 + 2x_2$       |  Yes   | Linear combination of variables |
| $3x_1^2 + 2x_2$     |  No    | $x_1^2$ is a nonlinear term     |
| $3x_1 + 2\sin(x_2)$ |  No    | $\sin(x_2)$ is nonlinear        |

For more information see:
- [Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python](https://pypi.org/project/matplotlib/)
- [NumPy is the fundamental package for scientific computing with Python](https://pypi.org/project/numpy/)