# Calculus

## Learning Objectives
- Differentiate and integrate a wide range of functions including exponential, logarithmic and trigonometric forms.
- Apply techniques such as substitution and integration by parts to evaluate complex integrals.
- Solve first-order differential equations by separation of variables and by using integrating factors.
- Model real-world problems with differential equations and interpret the solutions graphically.

## Key Terminology
- **Integration by parts**: Integration technique derived from the product rule, $\int u\,dv = uv - \int v\,du$.
- **Substitution**: Change of variable to simplify an integral, also called $u$-substitution.
- **Differential equation**: Equation that relates a function with its derivatives.
- **Integrating factor**: Function multiplied to a linear differential equation to make it directly integrable.
- **Separable equation**: Differential equation that can be written as $N(y)dy=M(x)dx$ and integrated on both sides.

## Core Explanations
- Using the chain rule, product rule and quotient rule for differentiation of composite functions such as $e^{2x}\sin x$.
- Integration of trigonometric powers using identities like $\sin^2x=\tfrac{1}{2}(1-\cos2x)$.
- Step-by-step method for integration by parts, choosing $u$ and $dv$ for convenience and applying repeatedly if necessary.
- Solving $\dfrac{dy}{dx}+Py=Q$ with integrating factors $\mu(x)=e^{\int P dx}$.
- Interpreting solutions of differential equations with initial conditions as models for exponential growth/decay and simple harmonic motion.

## Worked Examples
1. *Integration by parts*: Evaluate $\int x e^x\,dx$.
   - Choose $u=x$, $dv=e^x dx$ ⇒ $du=dx$, $v=e^x$. So $\int x e^x dx = x e^x - \int e^x dx = x e^x - e^x + C$.
2. *Differential equation - separation*: Solve $\frac{dy}{dx}=3y$ with $y(0)=2$.
   - $\frac{1}{y} dy=3 dx$ ⇒ $\ln|y|=3x+C$ ⇒ $y=Ce^{3x}$. Using $y(0)=2$ gives $C=2$, so $y=2e^{3x}$.
3. *Integrating factor*: Solve $\frac{dy}{dx}+2y=e^{x}$.
   - Integrating factor $\mu=e^{2x}$ ⇒ $\frac{d}{dx}(e^{2x}y)=e^{3x}$ ⇒ integrate to get $e^{2x}y=\tfrac{1}{3}e^{3x}+C$ ⇒ $y=\tfrac{1}{3}e^{x}+Ce^{-2x}$.

## Interactive Resources
- [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/CalcII/Integrals.aspx)
- [Wolfram Alpha Differential Equation Solver](https://www.wolframalpha.com/input/?i=solve+dy%2Fdx%3Dxy)

## Exam Tips
- Always add the constant of integration when evaluating indefinite integrals or general solutions to differential equations.
- Check units and physical interpretation when modelling problems (e.g., population growth or cooling rates).
- Practice selecting an efficient method (substitution, parts, partial fractions) before starting lengthy calculations.

## Common Pitfalls
- Forgetting to apply initial conditions, resulting in a general rather than particular solution.
- Mixing up $u$ and $dv$ in integration by parts leading to incorrect signs.
- Incorrectly simplifying logarithmic expressions during separation of variables.

## Worksheet Placeholder
**[Insert SaveMyExams worksheet link or Canvas PDF embed here]**
