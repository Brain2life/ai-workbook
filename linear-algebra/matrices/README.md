# Matrix Overview

A **matrix** is a rectangular array of numbers, symbols, or expressions arranged in **rows and columns**. It is a fundamental concept in mathematics, especially in **linear algebra**, and is used to represent and solve systems of equations, perform transformations, and model data in various fields like physics, computer science, economics, and machine learning.

---

### General Form:

A matrix with $m$ rows and $n$ columns is called an **$m \times n$ matrix**.

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

Here, $a_{ij}$ is the element in the $i$-th row and $j$-th column.

---

### Example:

A $2 \times 3$ matrix:

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

* 2 rows
* 3 columns

---

### Matrix Applications:

* Solving systems of linear equations
* Representing graphs and networks
* Image processing
* Machine learning (e.g., weight matrices in neural networks)
* 3D transformations in computer graphics

---

# Square Matrix

A **square matrix** is a special type of matrix where the **number of rows equals the number of columns**. In other words, it is an $n \times n$ matrix.

---

### Definition:

A matrix $A$ is called a **square matrix** if it has the same number of rows and columns:

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{bmatrix}
$$

---

### Example of a $3 \times 3$ square matrix:

$$
\begin{bmatrix}
2 & 0 & 1 \\
-1 & 3 & 4 \\
5 & 6 & 0
\end{bmatrix}
$$

---

### Special Properties of Square Matrices:

1. **Diagonal** – elements from top-left to bottom-right: $a_{11}, a_{22}, \ldots, a_{nn}$.
2. **Determinant** – only square matrices have a determinant.
3. **Inverse** – if a square matrix is non-singular (determinant ≠ 0), it has an inverse.
4. **Identity matrix** – a square matrix with 1s on the diagonal and 0s elsewhere.
5. **Symmetric matrix** – a square matrix where $A = A^T$ (transpose is equal to itself).
6. **Eigenvalues and eigenvectors** – defined only for square matrices.

# Linear Operations on Matrices

**Linear operations on matrices** refer to operations that preserve the structure of a linear system — mainly **addition**, **subtraction**, **scalar multiplication**, and **matrix multiplication**. These operations form the basis of **linear algebra**.

---

## 1. Matrix Addition

You can **add two matrices** of the **same dimensions** by adding their corresponding elements:

$$
A = \begin{bmatrix}1 & 2\\ 3 & 4\end{bmatrix},\quad
B = \begin{bmatrix}5 & 6\\ 7 & 8\end{bmatrix}
\Rightarrow
A + B = \begin{bmatrix}1+5 & 2+6\\ 3+7 & 4+8\end{bmatrix} = \begin{bmatrix}6 & 8\\ 10 & 12\end{bmatrix}
$$

**Properties**:

* Commutative: $A + B = B + A$
* Associative: $(A + B) + C = A + (B + C)$

## Matrix Subtraction (A − B)

Matrix subtraction is the element-wise subtraction of two matrices of **the same dimensions**:

$$
A = \begin{bmatrix}
7 & 5 \\
2 & 9
\end{bmatrix},\quad
B = \begin{bmatrix}
3 & 1 \\
0 & 4
\end{bmatrix}
\Rightarrow
A - B = \begin{bmatrix}
7 - 3 & 5 - 1 \\
2 - 0 & 9 - 4
\end{bmatrix} = \begin{bmatrix}
4 & 4 \\
2 & 5
\end{bmatrix}
$$

---

### Properties:

* $A - B = A + (-1) \cdot B$ (scalar multiplication)
* Not commutative: $A - B \neq B - A$

---

## 2. Scalar Multiplication

Multiply each element of a matrix by a scalar (real number):

$$
c = 2,\quad A = \begin{bmatrix}1 & -3\\ 0 & 4\end{bmatrix}
\Rightarrow
2A = \begin{bmatrix}2 & -6\\ 0 & 8\end{bmatrix}
$$

**Distributes over addition**:

$$
c(A + B) = cA + cB
$$

---

## 3. Matrix Multiplication

Multiply two matrices $A$ and $B$ **only if** the **number of columns of $A$** equals the **number of rows of $B$**.

$$
A = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix},
\quad
B = \begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
\Rightarrow
AB = \begin{bmatrix}
1\cdot5 + 2\cdot7 & 1\cdot6 + 2\cdot8 \\
3\cdot5 + 4\cdot7 & 3\cdot6 + 4\cdot8
\end{bmatrix} = \begin{bmatrix}
19 & 22 \\
43 & 50
\end{bmatrix}
$$

---

## Summary of Linear Operations

| Operation       | Rule                   | Requirements             |
| --------------- | ---------------------- | ------------------------ |
| Addition        | $A + B$                | Same shape               |
| Subtraction     | $A - B$                | Same shape               |
| Scalar multiply | $c \cdot A$            | Any matrix and scalar    |
| Matrix multiply | $A \cdot B$ or $A @ B$ | Columns of A = rows of B |

# Identity Matrix

A matrix that consists of **ones on the diagonal** and **zeros elsewhere** is called an **identity matrix**.

An **identity matrix** is a **square matrix** (same number of rows and columns) with:

* All **diagonal elements = 1**
* All **off-diagonal elements = 0**

### Example: $3 \times 3$ Identity Matrix

$$
I_3 = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

## Why Is It Called "Identity"?

Because multiplying any matrix $A$ by the identity matrix $I$ (of compatible size) **does not change** $A$:

$$
A \cdot I = A \quad \text{and} \quad I \cdot A = A
$$

Just like multiplying a number by 1:

$$
5 \times 1 = 5
$$

---

## Common Uses:

* Acts as the **multiplicative identity** in matrix algebra
* Used when finding **matrix inverses**
* Represents the **"do nothing"** transformation in geometry and linear maps
* Crucial in solving linear systems $Ax = b$

# Iverse Matrix

An **inverse matrix** of a square matrix $A$ is another matrix $A^{-1}$ such that:

$$
A \cdot A^{-1} = A^{-1} \cdot A = I
$$

Where $I$ is the **identity matrix**.

This is analogous to regular numbers:

* For a number $a$, the inverse is $\frac{1}{a}$
* For a matrix $A$, the inverse is $A^{-1}$

---

### Conditions for a Matrix to Have an Inverse

Not all matrices have inverses. A matrix must meet two rules to have an inverse:

1. It is **square** (same number of rows and columns)
2. Its **determinant is not zero**: $\det(A) \ne 0$

If $\det(A) = 0$, the matrix is **singular** and **not invertible**.

---

### Example

Let:

$$
A = \begin{bmatrix} 
4 & 2 \\ 
7 & 6 
\end{bmatrix}
$$


Then its inverse is:

$$
A^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -2 \\ -7 & 4 \end{bmatrix} 
= \begin{bmatrix} \frac{6}{10} & \frac{-2}{10} \\ \frac{-7}{10} & \frac{4}{10} \end{bmatrix} 
= \begin{bmatrix} \frac{3}{5} & -\frac{1}{5} \\ -\frac{7}{10} & \frac{2}{5} \end{bmatrix}
$$

The inverse of a 2x2 matrix 
$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$  
Then the inverse of \( A \) is given by the formula:  
$$
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
$$

For more information, see [How to find Inverse Matrix in russian](http://mathprofi.ru/kak_naiti_obratnuyu_matricu.html)

---

### Use Cases of Inverse Matrices

* Solving systems of linear equations: $Ax = b \Rightarrow x = A^{-1}b$
* Cryptography (matrix ciphers)
