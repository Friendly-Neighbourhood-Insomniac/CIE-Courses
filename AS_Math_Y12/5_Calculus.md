# Calculus

## Learning Objectives
- Differentiate and integrate polynomial, exponential and trigonometric functions using standard rules.
- Apply derivatives to find stationary points, determine their nature and solve optimisation problems.
- Evaluate definite integrals to calculate areas under curves and between curves.
- Use basic techniques of integration such as substitution and integration by parts for simple expressions.

## Key Terminology
- **Derivative**: Instantaneous rate of change of a function with respect to its variable, denoted $f'(x)$ or $\frac{dy}{dx}$.
- **Integral**: Antiderivative representing accumulated area or the inverse process of differentiation.
- **Stationary point**: Point on a curve where $f'(x)=0$; may be a maximum, minimum or point of inflexion.
- **Definite integral**: Integral evaluated between limits giving the net area under a curve.
- **Chain rule**: Differentiation rule for composite functions: $(f(g(x)))' = f'(g(x))\cdot g'(x)$.

## Core Explanations
- Differentiation rules: power rule, sum/difference rule, product and quotient rules.
- Using second derivative $f''(x)$ to classify stationary points as maxima or minima.
- Integration as the reverse process: $\int x^n\,dx=\tfrac{x^{n+1}}{n+1}+C$ for $n\ne-1$ and $\int e^{ax}\,dx=\tfrac{1}{a}e^{ax}+C$.
- Definite integrals representing the area between a curve and the x-axis, paying attention to sign when the curve crosses the axis.
- Basic methods such as substitution (e.g. $u=ax+b$) and integration by parts $\int u\,dv=uv-\int v\,du$.

## Worked Examples
1. *Differentiation*: Differentiate $f(x)=3x^3-2x^2+x$.
   - $f'(x)=9x^2-4x+1$.
2. *Stationary points*: Find and classify the stationary points of $y=x^3-3x^2+2$.
   - $y'=3x^2-6x=3x(x-2)$ ⇒ stationary points at $x=0$ and $x=2$. $y''=6x-6$. At $x=0$, $y''=-6$ (local maximum). At $x=2$, $y''=6$ (local minimum).
3. *Definite integral*: Evaluate $\int_0^2 (x^2+1)\,dx$.
   - $\left[\tfrac{x^3}{3}+x\right]_0^2=(\tfrac{8}{3}+2)-0=\tfrac{14}{3}$.

## Interactive Resources
- [Wolfram Alpha Calculus Widgets](https://www.wolframalpha.com/widgets/view.jsp?id=8dbc63ab0817797b06b9a8ab405b84a0)
- [GeoGebra Calculus Tools](https://www.geogebra.org/m/GUvT8mJw)

## Exam Tips
- Always include the constant of integration $+C$ for indefinite integrals.
- Sketch curves when solving optimisation problems to confirm whether values correspond to maxima or minima.
- Check the sign of the area when evaluating definite integrals across regions where the function is negative.

## Common Pitfalls
- Forgetting to apply the chain rule or product rule when required.
- Dropping the negative sign in integrals of trigonometric functions like $\int \cos x \,dx = \sin x + C$.
- Misplacing limits after substitution; always revert to the original variable or change the limits accordingly.

## Worksheet Placeholder
**[Insert SaveMyExams worksheet link or Canvas PDF embed here]**
