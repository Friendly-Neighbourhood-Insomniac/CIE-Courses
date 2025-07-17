# Algebra and Functions

## Learning Objectives
- Manipulate exponential and logarithmic functions and solve related equations.
- Apply the binomial theorem for positive integer and fractional indices.
- Use mathematical induction to prove statements about sequences and series.
- Analyse arithmetic and geometric progressions and evaluate sums of series.

## Key Terminology
- **Logarithm**: Inverse of exponentiation satisfying $a^{\log_a b}=b$.
- **Exponential function**: Function of the form $e^x$ or $a^x$ where $a>0$.
- **Induction**: Method of proof establishing that if a statement holds for $n=k$ and implies it holds for $n=k+1$, then it is true for all natural numbers.
- **Binomial series**: Expansion of $(1+x)^n$ for real $n$ where $|x|<1$ when $n$ is not necessarily an integer.
- **Geometric progression**: Sequence where successive terms are multiplied by a constant ratio.

## Core Explanations
- Laws of logarithms: $\log_a xy=\log_a x+\log_a y$, $\log_a(x/y)=\log_a x-\log_a y$, $\log_a x^k=k\log_a x$ and change of base formula.
- Use of natural logarithms and exponentials in solving differential equations and growth/decay problems.
- Binomial expansion $(1+x)^n=1+nx+\tfrac{n(n-1)}{2!}x^2+\dots$ valid for $|x|<1$ when $n$ is not an integer.
- Induction proofs: verify base case, assume true for $k$, then prove for $k+1$. Conclude the statement holds for all positive integers.
- Sum formulae for arithmetic and geometric series: $S_n=\tfrac{n}{2}(a+l)$ and $S_n=a\tfrac{1-r^n}{1-r}$.

## Worked Examples
1. *Logarithm laws*: Simplify $\log_a b+\log_a c$ and solve $\log_2 (x-1)=3$.
   - $\log_a b+\log_a c=\log_a(bc)$. Solve $\log_2(x-1)=3$ ⇒ $x-1=8$ ⇒ $x=9$.
2. *Binomial expansion*: Expand $(1+2x)^{1/2}$ up to the $x^2$ term.
   - $(1+2x)^{1/2}=1+\tfrac{1}{2}(2x)-\tfrac{1}{8}(2x)^2+\dots=1+x-2x^2+\dots$.
3. *Induction*: Prove the formula for the sum of the first $n$ cubes: $1^3+2^3+\dots+n^3=\tfrac{n^2(n+1)^2}{4}$.
   - Base case $n=1$ gives $1=\tfrac{1^2\cdot2^2}{4}=1$. Assume true for $n=k$; add $(k+1)^3$ and simplify to show the result for $n=k+1$.

## Interactive Resources
- [GeoGebra Logarithm Explorer](https://www.geogebra.org/m/hujazXgw)
- [Desmos Binomial Expansion](https://www.desmos.com/calculator)

## Exam Tips
- State the base case and induction step clearly; finish with a concluding statement.
- For binomial expansions, note the range of $x$ for which the series converges if $n$ is not an integer.
- When solving logarithmic equations, ensure arguments of logarithms are positive.

## Common Pitfalls
- Forgetting domain restrictions for logarithms leading to extraneous solutions.
- Skipping steps in the inductive proof or failing to show the transition from $k$ to $k+1$ clearly.
- Using the binomial series outside its radius of convergence when $|x|\ge1$.

## Worksheet Placeholder
**[Insert SaveMyExams worksheet link or Canvas PDF embed here]**
