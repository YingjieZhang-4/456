# This track adds a soft descending melody during Awe.
# Longer notes and lower pitches create a calm, spacious feeling.

# 1. ANTICIPATION + 2. EXCITEMENT
# Stay silent for the first 20 beats.
rest(20)

# 3. AWE - 12 beats
# Three descending notes support the background harmony.
playNote(69, beats=4, velocity=32)
playNote(67, beats=4, velocity=37)
playNote(64, beats=4, velocity=30)

# 4. DISAPPOINTMENT + 5. HAPPINESS
# + first 4 beats of CALMNESS
# Leave space for the other instruments.
rest(24)
