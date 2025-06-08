## Exercise: Is this function linear? 

This exercise shows how to plot three functions and shows the visual difference between linear and non-linear functions

## Libraries

Install the required libraries:
```bash
pip install matplotlib numpy
```

## What is a linear function or linear combination?

A **linear combination** of $x_1, \dots, x_n$ has the form

$$
a_1 x_1 + a_2 x_2 + a_3 x_3 + \cdots + a_n x_n
$$

where the numbers $a_1, \dots, a_n \in \mathbb{R}$ are the combination’s **coefficients**.

---

A **linear equation** in the variables $x_1, \dots, x_n$ has the form

$$
a_1 x_1 + a_2 x_2 + a_3 x_3 + \cdots + a_n x_n = d
$$

where $d \in \mathbb{R}$ is the **constant**.

---

An **n-tuple** $(s_1, s_2, \dots, s_n) \in \mathbb{R}^n$ is a **solution of**, or **satisfies**, that equation if substituting the numbers $s_1, \dots, s_n$ for the variables gives a **true statement**:

$$
a_1 s_1 + a_2 s_2 + \cdots + a_n s_n = d
$$

---

A **system of linear equations**:

$$
\begin{aligned}
a_{1,1} x_1 + a_{1,2} x_2 + \cdots + a_{1,n} x_n &= d_1 \\
a_{2,1} x_1 + a_{2,2} x_2 + \cdots + a_{2,n} x_n &= d_2 \\
&\vdots \\
a_{m,1} x_1 + a_{m,2} x_2 + \cdots + a_{m,n} x_n &= d_m \\
\end{aligned}
$$

has the solution $(s_1, s_2, \dots, s_n)$ if that **n-tuple** is a solution of **all** of the equations.

---

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

## References
- [Linear Algebra by Jim Hefferon Fourth edition](http://joshua.smcvt.edu/linearalgebra)