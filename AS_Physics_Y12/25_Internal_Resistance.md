# Internal Resistance

## Learning Objectives
- Explain electric current, potential difference, and electromotive force in terms of energy transfer per unit charge.
- Use Ohm's law and resistivity relationships to analyse circuits with resistors and internal resistance.
- Calculate electrical power and energy in DC circuits and solve problems involving series and parallel combinations.
- Describe the behaviour of capacitors during charging and discharging and interpret time constant graphs.
- Use interactive simulations to reinforce understanding of concepts.

## Key Terminology
- **Electromotive force (emf)**: Energy supplied per coulomb of charge by a source such as a cell or generator.
- **Resistance**: Ratio of potential difference to current in a component, measured in ohms (Ω).
- **Capacitance**: Charge stored per unit potential difference ($C=Q/V$) measured in farads (F).
- **Internal resistance**: Resistance within a power supply that causes a drop in terminal voltage when current flows.
- **Time constant ($\tau$)**: Product of resistance and capacitance ($RC$) representing the time for charge to fall to $1/e$ of its initial value.
- **Benchmark**: Standard or point of reference for comparison.

## Core Explanations
- Circuit diagrams with symbols for resistors, cells, switches, meters and capacitors.
- Using $V=IR$ to analyse potential difference and current for resistors in series and parallel.
- Energy transferred in a resistor given by $E=VIt$ and power relationships $P=IV=I^2R=V^2/R$.
- Exponential equations for capacitor charging and discharging: $Q=Q_0(1-e^{-t/RC})$ and $Q=Q_0e^{-t/RC}$.
- The effect of internal resistance on terminal voltage: $V=\text{emf}-Ir$.
- Apply principles in realistic contexts such as laboratory experiments.

## Worked Examples
1. *Power in circuits*: Calculate the power dissipated by a 5 \(\Omega\) resistor carrying 2 A of current.
   - $P=I^2R=2^2\times5=20$ W.
2. *Capacitor discharge*: A capacitor of 10 μF is charged to 6 V then allowed to discharge through a 2 kΩ resistor. Determine the time constant and the voltage after 10 ms.
   - $\tau=RC=2000\times10\times10^{-6}=0.02$ s; $V=V_0e^{-t/RC}=6e^{-0.01/0.02}\approx3.6$ V.
3. *Internal resistance*: A cell of emf 1.5 V has internal resistance 0.2 Ω and is connected to a 4.8 Ω load. Find the terminal voltage.
   - $V=\text{emf}-Ir$ where $I=\tfrac{1.5}{4.8+0.2}=0.3$ A, so $V=1.5-0.3\times0.2=1.44$ V.

4. *Practice problem*: Use this problem to check your understanding of the theory.
   - Solution steps should include reasoning and final answer with units.
## Interactive Resources
- [PhET Capacitor Lab](https://phet.colorado.edu/en/simulation/capacitor-lab)
- [PhET Circuit Construction Kit](https://phet.colorado.edu/en/simulation/circuit-construction-kit-dc)
<iframe src="https://phet.colorado.edu/sims/html/ohms-law/latest/ohms-law_en.html" width="700" height="450" title="Interactive simulation" loading="lazy"></iframe>

## Exam Tips
- Use $Q=CV$ and $E=\tfrac{1}{2}CV^2$ when comparing stored energy in capacitors.
- Check whether components are in series or parallel before calculating equivalent resistance or capacitance.
- Include units and prefixes correctly, e.g. μF for microfarads and kΩ for kilo-ohms.
- Review past papers to identify common question patterns.

## Common Pitfalls
- Mixing up emf (source energy per charge) with the potential difference across a component.
- Forgetting that capacitors in series add reciprocally while in parallel they add directly.
- Neglecting the role of internal resistance in limiting current from a real power supply.
- Overlooking units when substituting values into formulas.

## Worksheet Placeholder
**[Insert SaveMyExams worksheet link or Canvas PDF embed here]**
