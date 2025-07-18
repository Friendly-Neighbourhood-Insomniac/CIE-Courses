# Differential Equations Formation and Solution

## Learning Objectives
- Solve first and second order differential equations using standard techniques such as integrating factors and auxiliary equations.
- Apply Euler's method and improved Euler methods for numerical solutions of differential equations.
- Model real-life situations including exponential growth, decay and simple harmonic motion using differential equations.
- Analyse the stability and accuracy of numerical methods and choose appropriate step sizes.
- Use interactive simulations to reinforce understanding of concepts.

## Key Terminology
- **Homogeneous equation**: Differential equation where all terms involve the dependent variable or its derivatives with no standalone function of the independent variable.
- **Particular solution**: Specific solution satisfying initial or boundary conditions, often added to the complementary (homogeneous) solution.
- **Euler's method**: Numerical technique that approximates solutions by stepping forward using $y_{n+1}=y_n+h f(x_n,y_n)$.
- **Integrating factor**: Function used to transform a non-exact first-order linear equation into an integrable form.
- **Auxiliary equation**: Characteristic equation derived from substituting $y=e^{rx}$ into a constant-coefficient differential equation.
- **Benchmark**: Standard or point of reference for comparison.

## Core Explanations
- Solving $y'+P(x)y=Q(x)$ by multiplying through with the integrating factor $e^{\int P(x)dx}$ and then integrating.
- For second-order constant-coefficient equations $ay''+by'+cy=0$, solving the auxiliary equation $ar^2+br+c=0$ to obtain the complementary solution and adding a suitable particular integral.
- Euler's method step-by-step procedure and error estimation; improved methods such as Heun's or Runge–Kutta provide greater accuracy.
- Formulating models such as radioactive decay $\frac{dN}{dt}=-kN$ or SHM $\frac{d^2x}{dt^2}+\omega^2x=0$ and interpreting solutions.
- Stability considerations: small step sizes reduce error but increase computation time; step size should reflect rate of change of the solution.
- Apply principles in realistic contexts such as laboratory experiments.

## Worked Examples
1. *Second-order equation*: Solve $y''+y=0$ with $y(0)=0$, $y'(0)=1$.
   - Characteristic equation $r^2+1=0$ ⇒ $r=\pm i$ ⇒ complementary solution $y=A\cos x+B\sin x$. Apply conditions to get $y=\sin x$.
2. *Euler's method*: Use step size 0.1 to approximate $y(0.1)$ for $y'=y$, $y(0)=1$.
   - $y_1=y_0+h y'_0=1+0.1(1)=1.1$.
3. *Integrating factor*: Solve $\dfrac{dy}{dx}+3y=6x$ with $y(0)=2$.
   - Integrating factor $e^{3x}$ ⇒ $\frac{d}{dx}(e^{3x}y)=6xe^{3x}$ ⇒ integrate: $e^{3x}y=2e^{3x}+2xe^{3x}$ ⇒ $y=2+2x$.

4. *Practice problem*: Use this problem to check your understanding of the theory.
   - Solution steps should include reasoning and final answer with units.
## Interactive Resources
- [Desmos Differential Equations](https://www.desmos.com/calculator)
- [GeoGebra Euler Method](https://www.geogebra.org/m/qz7k96bw)
<iframe src="https://www.desmos.com/calculator/wrabkf1q2x?embed" width="700" height="450" title="Interactive simulation" loading="lazy"></iframe>

## Exam Tips
- Write complementary and particular solutions clearly and apply initial conditions after combining them.
- In numerical methods, keep step size sufficiently small and estimate errors when possible.
- Check solutions by differentiating back into the original equation to verify correctness.
- Review past papers to identify common question patterns.

## Common Pitfalls
- Missing constants of integration when integrating both sides during separation or integrating factors.
- Using too large a step size with Euler's method, leading to poor approximations.
- Neglecting to verify that a proposed particular solution actually satisfies the non-homogeneous equation.
- Overlooking units when substituting values into formulas.

## Worksheet Placeholder
**[Insert SaveMyExams worksheet link or Canvas PDF embed here]**
