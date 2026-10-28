# This function creates a short bass rhythm.
# Root controls the pitch, and strength controls the volume.
# Changes in note length, pitch and rests create variation.
def pulse(root, strength):
    playNote(root, beats=1.25, velocity=strength)
    rest(0.25)
 # Adds a higher note with a softer volume.
    playNote(root + 7, beats=0.5, velocity=strength - 12)
    rest(0.5)
 # Returns to the original pitch.
    playNote(root, beats=0.75, velocity=strength - 5)
    rest(0.25)
 # Ends the pattern one octave above the root.
    playNote(root + 12, beats=0.5, velocity=strength - 15)
     

# 1. ANTICIPATION
# A long pause creates a quiet opening.
# A low and soft note introduces the bass.
rest(4)
rest(2.5)
playNote(33, beats=1.5, velocity=42)

# 2. EXCITEMENT
# Reuses the bass function with different pitches and strengths.
# Three patterns create a more active rhythm.
pulse(41, 64)
pulse(43, 68)
pulse(36, 70)

# 3. AWE
# Longer notes create a more spacious feeling.
# The steady bass supports the other instruments.
playNote(41, beats=4, velocity=66)
playNote(43, beats=4, velocity=64)
playNote(36, beats=4, velocity=70)

# 4. DISAPPOINTMENT
# Lower velocity and longer rests reduce the energy.
# The gaps between notes create a quieter mood.
playNote(33, beats=2.5, velocity=44)
rest(1.5)

playNote(40, beats=2, velocity=38)
rest(2)

# 5. HAPPINESS
# Brings back the earlier bass pattern with softer dynamics.
# Reusing the function connects this part to Excitement.
pulse(41, 58)
pulse(43, 60)
pulse(36, 62)

# 6. CALMNESS
# Longer notes and softer velocities create a gentle ending.
# The rests leave more space between the final notes.
playNote(41, beats=3, velocity=46)
rest(1)

playNote(43, beats=2, velocity=40)
rest(2)

playNote(36, beats=4, velocity=34)
