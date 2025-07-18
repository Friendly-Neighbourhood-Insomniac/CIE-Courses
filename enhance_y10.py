from pathlib import Path

# Unique learning objectives for each topic
learning_objectives = {
    '01_Physical_Quantities_and_SI_Units': [
        'Distinguish base from derived SI units.',
        'Convert values using prefixes such as kilo and milli.',
        'Record measurements to an appropriate precision.'
    ],
    '02_Measurement_Techniques_and_Uncertainties': [
        'Use vernier calipers and micrometers accurately.',
        'Calculate percentage uncertainty of measurements.',
        'Suggest ways to minimise systematic errors.'
    ],
    '03_Scalars_and_Vectors': [
        'Classify quantities as scalars or vectors.',
        'Resolve vectors into perpendicular components.',
        'Add vectors using diagrammatic methods.'
    ],
    '04_Kinematics_Speed_Velocity_Acceleration': [
        'Determine speed, velocity and acceleration from data.',
        'Apply equations of motion for constant acceleration.',
        'Interpret displacement- and velocity-time graphs.'
    ],
    '05_Motion_Graphs_DistanceTime_VelocityTime': [
        'Sketch typical distance-time and velocity-time graphs.',
        'Find acceleration from gradients of graphs.',
        'Calculate displacement from the area under velocity-time graphs.'
    ],
    '06_Forces_Types_Resultants_Friction': [
        'Describe common contact and non-contact forces.',
        'Determine the resultant of several forces.',
        'Explain how friction affects motion.'
    ],
    '07_Turning_Effect_of_Forces_Moments_Equilibrium': [
        'Define the moment of a force.',
        'Use the principle of moments for equilibrium problems.',
        'Describe uses of levers and simple machines.'
    ],
    '08_Mass_and_Weight': [
        'Differentiate between mass and weight.',
        'Calculate weight using W = mg.',
        'Describe how weight varies with gravitational field strength.'
    ],
    '09_Density_Concept_and_Calculations': [
        'Measure mass and volume to find density.',
        'Use the formula density = mass/volume.',
        'Explain why some objects float while others sink.'
    ],
    '10_Work_Energy_Power': [
        'Calculate work done by a force.',
        'Relate work to energy transfer.',
        'Determine power from energy and time.'
    ],
    '11_Kinetic_and_Potential_Energy': [
        'Use KE = 1/2 m v^2 and GPE = mgh.',
        'Convert between kinetic and potential energy.',
        'Apply conservation of energy to simple systems.'
    ],
    '12_Efficiency_and_Energy_Transfer': [
        'Define efficiency using energy or power.',
        'Calculate efficiency for mechanical devices.',
        'Suggest methods to improve efficiency.'
    ],
    '13_Thermal_Properties_Specific_Heat_Capacity': [
        'Describe experiments to measure specific heat capacity.',
        'Solve problems using Q = mcΔT.',
        'Interpret heating and cooling curves.'
    ],
    '14_Thermal_Expansion_and_Temperature_Measurement': [
        'Explain expansion of solids, liquids and gases.',
        'Describe how thermometers measure temperature.',
        'Convert between Celsius and Kelvin scales.'
    ],
    '15_Kinetic_Model_of_Matter': [
        'Describe particle motion in solids, liquids and gases.',
        'Relate temperature to average kinetic energy.',
        'Explain gas pressure using the kinetic model.'
    ],
    '16_Change_of_State_Specific_Latent_Heat': [
        'Define melting, boiling and sublimation.',
        'Use Q = mL for phase change calculations.',
        'Describe energy changes at constant temperature.'
    ],
    '17_Pressure_and_Ideal_Gas_Law': [
        'Apply pressure = force/area.',
        'Describe Brownian motion evidence for molecules.',
        'Use pV/T = constant for a fixed mass of gas.'
    ],
    '18_Heat_Transfer_Conduction_Convection_Radiation': [
        'Compare conduction, convection and radiation.',
        'Describe ways to reduce heat loss.',
        'Explain the design of a vacuum flask.'
    ],
    '19_General_Wave_Properties_Frequency_Wavelength_Speed': [
        'Define amplitude, frequency, period and wavelength.',
        'Use v = fλ to calculate wave speed.',
        'Distinguish between transverse and longitudinal waves.'
    ],
    '20_Reflection_and_Refraction': [
        'State and apply the law of reflection.',
        'Use Snell\'s law for refraction at a boundary.',
        'Draw ray diagrams for mirrors and lenses.'
    ],
    '21_Diffraction_and_Interference': [
        'Describe diffraction around openings.',
        'Explain constructive and destructive interference.',
        'Relate interference patterns to path difference.'
    ],
    '22_Light_Ray_Diagrams_and_Colour_Filters': [
        'Construct ray diagrams for simple optical systems.',
        'Explain colour filtering and mixing.',
        'Describe dispersion of white light.'
    ],
    '23_Total_Internal_Reflection_and_Critical_Angle': [
        'Define critical angle and total internal reflection.',
        'Calculate critical angle from refractive index.',
        'Describe applications in optical fibres.'
    ],
    '24_Sound_Properties_Speed_Pitch_Loudness': [
        'Explain how sound waves are produced and propagate.',
        'Relate frequency to pitch and amplitude to loudness.',
        'Determine the speed of sound experimentally.'
    ],
    '25_Electromagnetic_Spectrum_Properties_and_Uses': [
        'List the electromagnetic spectrum in order of wavelength.',
        'Give typical uses and hazards of each region.',
        'Explain how wavelength affects penetration and detection.'
    ],
}

# Cross-links between related topics
cross_links = {
    '01_Physical_Quantities_and_SI_Units': '02_Measurement_Techniques_and_Uncertainties.md',
    '02_Measurement_Techniques_and_Uncertainties': '01_Physical_Quantities_and_SI_Units.md',
    '03_Scalars_and_Vectors': '04_Kinematics_Speed_Velocity_Acceleration.md',
    '04_Kinematics_Speed_Velocity_Acceleration': '05_Motion_Graphs_DistanceTime_VelocityTime.md',
    '05_Motion_Graphs_DistanceTime_VelocityTime': '04_Kinematics_Speed_Velocity_Acceleration.md',
    '06_Forces_Types_Resultants_Friction': '07_Turning_Effect_of_Forces_Moments_Equilibrium.md',
    '07_Turning_Effect_of_Forces_Moments_Equilibrium': '06_Forces_Types_Resultants_Friction.md',
    '08_Mass_and_Weight': '06_Forces_Types_Resultants_Friction.md',
    '09_Density_Concept_and_Calculations': '17_Pressure_and_Ideal_Gas_Law.md',
    '10_Work_Energy_Power': '11_Kinetic_and_Potential_Energy.md',
    '11_Kinetic_and_Potential_Energy': '10_Work_Energy_Power.md',
    '12_Efficiency_and_Energy_Transfer': '10_Work_Energy_Power.md',
    '13_Thermal_Properties_Specific_Heat_Capacity': '18_Heat_Transfer_Conduction_Convection_Radiation.md',
    '14_Thermal_Expansion_and_Temperature_Measurement': '13_Thermal_Properties_Specific_Heat_Capacity.md',
    '15_Kinetic_Model_of_Matter': '16_Change_of_State_Specific_Latent_Heat.md',
    '16_Change_of_State_Specific_Latent_Heat': '15_Kinetic_Model_of_Matter.md',
    '17_Pressure_and_Ideal_Gas_Law': '09_Density_Concept_and_Calculations.md',
    '18_Heat_Transfer_Conduction_Convection_Radiation': '13_Thermal_Properties_Specific_Heat_Capacity.md',
    '19_General_Wave_Properties_Frequency_Wavelength_Speed': '20_Reflection_and_Refraction.md',
    '20_Reflection_and_Refraction': '21_Diffraction_and_Interference.md',
    '21_Diffraction_and_Interference': '20_Reflection_and_Refraction.md',
    '22_Light_Ray_Diagrams_and_Colour_Filters': '23_Total_Internal_Reflection_and_Critical_Angle.md',
    '23_Total_Internal_Reflection_and_Critical_Angle': '22_Light_Ray_Diagrams_and_Colour_Filters.md',
    '24_Sound_Properties_Speed_Pitch_Loudness': '19_General_Wave_Properties_Frequency_Wavelength_Speed.md',
    '25_Electromagnetic_Spectrum_Properties_and_Uses': '22_Light_Ray_Diagrams_and_Colour_Filters.md',
}

# Worked examples for each topic
examples = {
    '01_Physical_Quantities_and_SI_Units': [
        ('Convert 2.5 km to metres.', '2.5 km = 2500 m'),
        ('Express 0.0037 m in millimetres.', '0.0037 m = 3.7 mm'),
    ],
    '02_Measurement_Techniques_and_Uncertainties': [
        ('A length is measured as 5.0 cm ±0.1 cm. What is the percentage uncertainty?', '0.1/5.0 × 100 = 2%'),
        ('Add 2.0 ±0.1 m and 3.0 ±0.2 m.', '5.0 ±0.3 m'),
    ],
    '03_Scalars_and_Vectors': [
        ('Two displacements of 3 m east and 4 m north combine to give?', 'Resultant = 5 m at 53°'),
        ('Resolve a 10 N force at 30° to the horizontal.', 'Horizontal component = 8.7 N'),
    ],
    '04_Kinematics_Speed_Velocity_Acceleration': [
        ('A car travels 200 m in 10 s. What is its average speed?', 'v = 20 m/s'),
        ('A bus accelerates from 10 m/s to 22 m/s in 6 s. Find its acceleration.', 'a = 2 m/s²'),
    ],
    '05_Motion_Graphs_DistanceTime_VelocityTime': [
        ('From a velocity-time graph, the speed rises steadily to 8 m/s in 4 s. What is the acceleration?', 'a = 2 m/s²'),
        ('A car travels at 3 m/s for 10 s. Find the distance from the area under the graph.', 's = 30 m'),
    ],
    '06_Forces_Types_Resultants_Friction': [
        ('Two forces of 4 N and 3 N act at right angles. Find the resultant.', 'Resultant = 5 N'),
        ('A 5 kg object experiences a resultant force of 15 N. Calculate its acceleration.', 'a = 3 m/s²'),
    ],
    '07_Turning_Effect_of_Forces_Moments_Equilibrium': [
        ('What moment is produced by a 5 N force 0.2 m from a pivot?', 'Moment = 1 N m'),
        ('A 15 N child sits 1 m from a pivot. Where must a 20 N child sit on the opposite side to balance?', '20 x d = 15 x 1 ⇒ d = 0.75 m'),
    ],
    '08_Mass_and_Weight': [
        ('Find the weight of a 4 kg mass on Earth.', 'W = 4 × 9.8 = 39.2 N'),
        ('Determine the mass of an object that weighs 30 N on Earth.', 'm = 30/9.8 ≈ 3.1 kg'),
    ],
    '09_Density_Concept_and_Calculations': [
        ('A block of mass 0.5 kg occupies 2 ×10^-4 m³. Calculate its density.', 'ρ = 2500 kg/m³'),
        ('Find the mass of 1.2 L of oil of density 900 kg/m³.', 'm = 1.08 kg'),
    ],
    '10_Work_Energy_Power': [
        ('A 100 N force moves a box 5 m. Calculate the work done.', 'W = 500 J'),
        ('A 60 W bulb is on for 2 minutes. How much energy is used?', 'E = 7200 J'),
    ],
    '11_Kinetic_and_Potential_Energy': [
        ('Find the kinetic energy of a 0.5 kg ball moving at 8 m/s.', 'KE = 16 J'),
        ('What is the gravitational potential energy of a 2 kg mass 3 m high?', 'GPE ≈ 59 J'),
    ],
    '12_Efficiency_and_Energy_Transfer': [
        ('A machine takes 200 J and delivers 150 J useful work. Calculate efficiency.', 'Efficiency = 75%'),
        ('A 60 W motor operates at 40% efficiency. What is its useful power output?', '24 W'),
    ],
    '13_Thermal_Properties_Specific_Heat_Capacity': [
        ('How much energy is needed to heat 0.2 kg of water by 30°C?', 'Q = 25200 J'),
        ('5000 J heats 0.1 kg of copper (c=390 J/kg°C). Find the temperature rise.', 'ΔT ≈ 128°C'),
    ],
    '14_Thermal_Expansion_and_Temperature_Measurement': [
        ('A thermometer thread expands 3 mm for a 30°C rise. How much for 10°C?', '1 mm'),
        ('Convert 20°C to Kelvin.', '293 K'),
    ],
    '15_Kinetic_Model_of_Matter': [
        ('Why does the pressure of a gas increase when heated at constant volume?', 'Particles move faster and collide more often.'),
        ('If average molecular speed is 300 m/s at 300 K, estimate the speed at 600 K.', '≈ 424 m/s'),
    ],
    '16_Change_of_State_Specific_Latent_Heat': [
        ('Energy needed to melt 0.1 kg of ice (Lf=334 kJ/kg).', 'Q = 33.4 kJ'),
        ('How much energy to boil 0.05 kg of water (Lv=2.26 MJ/kg)?', 'Q = 113 kJ'),
    ],
    '17_Pressure_and_Ideal_Gas_Law': [
        ('A force of 30 N acts on area 0.5 m². Find the pressure.', 'p = 60 Pa'),
        ('Gas at 300 K has volume 2 m³. What is the volume at 400 K if pressure is constant?', 'V₂ = 2 × 400/300 = 2.67 m³'),
    ],
    '18_Heat_Transfer_Conduction_Convection_Radiation': [
        ('Which surface emits more radiation, black or shiny?', 'Black surfaces emit more.'),
        ('Why does a sea breeze occur during the day?', 'Warm air rises over land and cooler air moves in from the sea.'),
    ],
    '19_General_Wave_Properties_Frequency_Wavelength_Speed': [
        ('A wave has frequency 50 Hz and wavelength 0.2 m. What is its speed?', 'v = 10 m/s'),
        ('If the period of a wave is 0.01 s, find its frequency.', 'f = 100 Hz'),
    ],
    '20_Reflection_and_Refraction': [
        ('A ray strikes a mirror at 30° to the normal. Angle of reflection?', '30°'),
        ('Light enters glass (n=1.5) at 20° to the normal. Find angle of refraction.', '≈13°'),
    ],
    '21_Diffraction_and_Interference': [
        ('Two slits separated by 0.1 mm are lit with 500 nm light on a 1 m screen. What is the fringe spacing?', '5 mm'),
        ('When does destructive interference occur?', 'When path difference equals half a wavelength.'),
    ],
    '22_Light_Ray_Diagrams_and_Colour_Filters': [
        ('An object 10 cm from a mirror with f=5 cm forms an image where?', 'At 10 cm behind the mirror.'),
        ('Which filter transmits only red light?', 'A red filter'),
    ],
    '23_Total_Internal_Reflection_and_Critical_Angle': [
        ('Calculate the critical angle for glass of n=1.5.', '≈42°'),
        ('Why does light stay inside an optical fibre?', 'Because incidence exceeds the critical angle.'),
    ],
    '24_Sound_Properties_Speed_Pitch_Loudness': [
        ('Echo returns in 0.3 s from a wall 50 m away. Speed of sound?', '≈333 m/s'),
        ('If frequency increases, how does the pitch change?', 'Pitch becomes higher.'),
    ],
    '25_Electromagnetic_Spectrum_Properties_and_Uses': [
        ('Which region has the shortest wavelength?', 'Gamma rays'),
        ('Give one use of microwaves.', 'Heating food or satellite communication'),
    ],
}
key_terms = {
    "01_Physical_Quantities_and_SI_Units": ["Quantity", "Base unit", "Prefix"],
    "02_Measurement_Techniques_and_Uncertainties": ["Uncertainty", "Systematic error", "Vernier scale"],
    "03_Scalars_and_Vectors": ["Scalar", "Vector", "Resultant"],
    "04_Kinematics_Speed_Velocity_Acceleration": ["Speed", "Velocity", "Acceleration"],
    "05_Motion_Graphs_DistanceTime_VelocityTime": ["Displacement", "Gradient", "Area"],
    "06_Forces_Types_Resultants_Friction": ["Force", "Resultant", "Friction"],
    "07_Turning_Effect_of_Forces_Moments_Equilibrium": ["Moment", "Pivot", "Equilibrium"],
    "08_Mass_and_Weight": ["Mass", "Weight", "Gravity"],
    "09_Density_Concept_and_Calculations": ["Density", "Mass", "Volume"],
    "10_Work_Energy_Power": ["Work", "Energy", "Power"],
    "11_Kinetic_and_Potential_Energy": ["Kinetic energy", "Potential energy", "Conservation"],
    "12_Efficiency_and_Energy_Transfer": ["Efficiency", "Input energy", "Output energy"],
    "13_Thermal_Properties_Specific_Heat_Capacity": ["Specific heat capacity", "Thermal energy", "Temperature"],
    "14_Thermal_Expansion_and_Temperature_Measurement": ["Expansion", "Thermometer", "Temperature scale"],
    "15_Kinetic_Model_of_Matter": ["Brownian motion", "Gas pressure", "Kinetic theory"],
    "16_Change_of_State_Specific_Latent_Heat": ["Latent heat", "Melting", "Boiling"],
    "17_Pressure_and_Ideal_Gas_Law": ["Pressure", "Molecule", "pV = constant"],
    "18_Heat_Transfer_Conduction_Convection_Radiation": ["Conduction", "Convection", "Radiation"],
    "19_General_Wave_Properties_Frequency_Wavelength_Speed": ["Wavelength", "Frequency", "Amplitude"],
    "20_Reflection_and_Refraction": ["Incident ray", "Refraction", "Refractive index"],
    "21_Diffraction_and_Interference": ["Diffraction", "Interference", "Fringe"],
    "22_Light_Ray_Diagrams_and_Colour_Filters": ["Ray diagram", "Filter", "Dispersion"],
    "23_Total_Internal_Reflection_and_Critical_Angle": ["Critical angle", "Total internal reflection", "Optical fibre"],
    "24_Sound_Properties_Speed_Pitch_Loudness": ["Pitch", "Loudness", "Echo"],
    "25_Electromagnetic_Spectrum_Properties_and_Uses": ["Radio waves", "Microwaves", "Gamma rays"]
}


# PhET or other interactive resources
resources = {
    '04_Kinematics_Speed_Velocity_Acceleration': 'https://phet.colorado.edu/en/simulation/moving-man',
    '06_Forces_Types_Resultants_Friction': 'https://phet.colorado.edu/en/simulation/forces-and-motion-basics',
    '09_Density_Concept_and_Calculations': 'https://phet.colorado.edu/en/simulation/density',
    '10_Work_Energy_Power': 'https://phet.colorado.edu/en/simulation/energy-skate-park',
    '13_Thermal_Properties_Specific_Heat_Capacity': 'https://phet.colorado.edu/en/simulation/specific-heat',
    '17_Pressure_and_Ideal_Gas_Law': 'https://phet.colorado.edu/en/simulation/gas-properties',
    '19_General_Wave_Properties_Frequency_Wavelength_Speed': 'https://phet.colorado.edu/en/simulation/wave-on-a-string',
    '20_Reflection_and_Refraction': 'https://phet.colorado.edu/en/simulation/bending-light',
    '23_Total_Internal_Reflection_and_Critical_Angle': 'https://phet.colorado.edu/en/simulation/legacy/optical-fiber',
    '24_Sound_Properties_Speed_Pitch_Loudness': 'https://phet.colorado.edu/en/simulation/sound',
}

for md in sorted(Path('IGCSE_Physics_Y10').glob('*.md')):
    key = md.stem
    title = ' '.join(key.split('_')[1:]).capitalize()
    lines = []
    lines.append(f'# {title}')
    lines.append('')
    lines.append('> ❓ How does this topic connect to everyday situations?')
    lines.append('')
    lines.append('<!--')
    lines.append('Gamma Metadata:')
    lines.append('Course: IGCSE Physics Year 10')
    lines.append(f'Topic: {title}')
    lines.append('-->')
    lines.append('')

    lines.append('## 🎯 Learning Objectives')
    for obj in learning_objectives.get(key, []):
        lines.append(f'- {obj}')
    lines.append('')

    lines.append('## 🔑 Key Terms')
    kt_list = key_terms.get(key, ["Force", "Energy", "Power"])
    for term in kt_list:
        lines.append(f"- **{term}**")
    lines.append('')

    lines.append('## 📘 Core Explanation')
    lines.append('This section summarises the main principles of the topic with reference to the CIE syllabus.')
    lines.append('')

    for idx, (q, a) in enumerate(examples.get(key, []), start=1):
        lines.append(f'## 🧮 Worked Example {idx}')
        lines.append(f'**Q:** {q}')
        lines.append('')
        lines.append(f'**A:** {a}')
        lines.append('')

    lines.append('## 💡 Exam Tips')
    lines.append('- Always show your working and include units.')
    lines.append('- Write answers to an appropriate number of significant figures.')
    lines.append('')

    lines.append('## ⚠️ Common Pitfalls')
    lines.append('- Mixing up related quantities or using inconsistent units.')
    lines.append('- Forgetting vector directions where applicable.')
    lines.append('')

    lines.append('## 🔗 Interactive Resources')
    if key in resources:
        lines.append(f'- [PhET Simulation]({resources[key]})')
    else:
        lines.append('- [PhET Simulation](https://phet.colorado.edu/)')
    lines.append('- [Khan Academy](https://www.khanacademy.org/science/physics)')
    lines.append('- [Save My Exams](https://www.savemyexams.co.uk/)')

    if key in cross_links:
        other = cross_links[key]
        lines.append(f'\n📎 See also: [{other}]({other})')

    md.write_text('\n'.join(lines) + '\n')
