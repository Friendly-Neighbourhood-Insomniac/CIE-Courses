import re
from pathlib import Path
import textwrap

definitions = {
    'Speed': 'Distance travelled per unit time, measured in metres per second.',
    'Velocity': 'Displacement per unit time in a stated direction.',
    'Acceleration': 'Rate of change of velocity with time.',
    'Force': 'Interaction that changes motion, measured in newtons.',
    'Mass': 'Quantity of matter in an object, measured in kilograms.',
    'Weight': 'Force due to gravity acting on a mass.',
    'Density': 'Mass per unit volume.',
    'Energy': 'Capacity for doing work, measured in joules.',
    'Work': 'Energy transferred when a force moves its point of application.',
    'Power': 'Rate at which work is done or energy is transferred.',
    'Momentum': 'Product of mass and velocity of a body.',
    'Pressure': 'Force exerted per unit area.',
    'Temperature': 'Measure of average kinetic energy of particles.',
    'Heat': 'Energy transfer due to temperature difference.',
    'Wave': 'Disturbance transferring energy through space or a medium.',
    'Frequency': 'Number of oscillations per second of a wave.',
    'Wavelength': 'Distance between two consecutive identical points on a wave.',
    'Current': 'Rate of flow of electric charge.',
    'Voltage': 'Potential difference that drives current.',
    'Resistance': 'Opposition to current flow.',
    'Magnetism': 'Phenomena associated with magnetic fields.',
    'Induction': 'Production of emf by varying magnetic flux.',
    'Probability': 'Measure of likelihood of an event.',
    'Statistics': 'Collection and interpretation of data.',
    'Trigonometry': 'Study of relationships involving angles.',
    'Integration': 'Mathematical process of finding areas under curves.',
    'Differentiation': 'Finding rates of change using derivatives.'
}

course_dirs = [
    'IGCSE_Physics_Y10',
    'IGCSE_Physics_Y11',
    'IGCSE_Math_Y11',
    'AS_Physics_Y12',
    'AS_Math_Y12',
    'AL_Physics_Y13',
    'AL_Math_Y13'
]

template = textwrap.dedent('''\
# {title}

## Learning Objectives
- Explain the fundamental ideas behind {topic} as set out in the CIE syllabus.
- Solve problems using standard formulae for {topic}.
- Interpret results with correct units and notation.

## Key Terminology
{terms}

## Core Explanations
{core}

## Worked Examples
1. *Worked Example*: Solve a typical question on {topic}.
   - Outline each calculation step and present the final answer with units.
2. *Further Practice*: Apply the same principles to a new scenario.
   - Summarise the reasoning used to reach the solution.

## Interactive Resources
- [PhET Simulation](https://phet.colorado.edu/)

## Exam Tips
- Check units carefully when substituting numbers into equations.
- Show intermediate steps to gain method marks.

## Common Pitfalls
- Misreading the question or forgetting to convert units can cause errors.

## Worksheet Placeholder
**[Insert SaveMyExams worksheet link or Canvas PDF embed here]**
''')

for course in course_dirs:
    for path in Path(course).glob('*.md'):
        lines = path.read_text().splitlines()
        heading_count = sum(1 for l in lines if l.lstrip().startswith('#'))
        if heading_count > 9:
            first_found = False
            start_index = None
            for i, line in enumerate(lines):
                if line.startswith('# '):
                    if not first_found:
                        first_found = True
                    else:
                        start_index = i
                        break
            if start_index is not None:
                new_content = '\n'.join(lines[start_index:]).lstrip() + '\n'
                path.write_text(new_content)
            else:
                # fallback to template if something went wrong
                heading_count = 0
        if heading_count <= 9:
            name = path.stem
            words = re.sub(r'^\d+_', '', name).split('_')
            words_cap = [w.capitalize() for w in words]
            title = ' '.join(words_cap)
            defs = []
            for w in words_cap:
                if w in definitions and len(defs) < 3:
                    defs.append(f"- **{w}**: {definitions[w]}")
            if not defs:
                defs.append('- **Concept**: Key idea related to the topic.')
            core_text = f"This section explains the essential principles of {' '.join(words_cap)} with reference to standard formulae and applications."
            filled = template.format(title=title, topic=' '.join(words_cap), terms='\n'.join(defs), core=core_text)
            path.write_text(filled)
