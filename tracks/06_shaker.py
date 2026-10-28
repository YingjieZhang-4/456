# This track adds soft percussion to support the main rhythm.
# Two functions create different shaker patterns.
# Volume controls the strength of the notes.
# Small changes in timing and velocity make the rhythm less repetitive.

# This function creates the first four-beat shaker pattern.
# Different rests and velocities create rhythmic variation.
def shaker_a(volume):
    rest(0.5)
    playNote(4, beats=0.125, velocity=volume)
    rest(0.875)
 # The second sound is played more softly.
    playNote(5, beats=0.125, velocity=volume - 8)
    rest(0.875)

    playNote(4, beats=0.125, velocity=volume - 4)
    rest(0.625)

    playNote(5, beats=0.125, velocity=volume - 10)
    rest(0.625)

# This function creates a different four-beat pattern.
# Changing the rests shifts the timing of the percussion.
def shaker_b(volume):
    rest(0.75)
    playNote(4, beats=0.125, velocity=volume)
    rest(0.625)

    playNote(5, beats=0.125, velocity=volume - 8)
    rest(1.375)

    playNote(4, beats=0.125, velocity=volume - 5)
    rest(0.375)

    playNote(5, beats=0.125, velocity=volume - 10)
    rest(0.375)

# 1. ANTICIPATION - 8 beats
# The percussion stays silent during the opening.
rest(8)

# 2. EXCITEMENT - 12 beats
# Alternating the two functions creates rhythmic variation.
# Increasing volume values gradually adds more energy.
shaker_a(30)
shaker_b(34)
shaker_a(38)

# 3. AWE - 12 beats
# The percussion stops to leave space for the piano and harmony.
rest(12)

# 4. DISAPPOINTMENT - 8 beats
# Silence reduces the rhythmic energy.
rest(8)

# 5. HAPPINESS - 12 beats
# The shaker returns with softer volume values.
# Alternating patterns keep the rhythm from sounding repetitive.
shaker_b(28)
shaker_a(32)
shaker_b(26)

# 6. CALMNESS - 12 beats
# The percussion stops to create a peaceful ending.
rest(12)
