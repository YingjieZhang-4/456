# This track adds soft guitar notes to support the piano.
# playNote() controls the pitch, duration and volume.
# rest() creates space between notes.
# The guitar plays only selected notes to avoid overcrowding the melody.

# 1. ANTICIPATION
# The guitar stays silent during the opening.
rest(8)

# 2. EXCITEMENT - 12 beats
# A few short notes add detail without covering the main melody.

# Fmaj7 - A
# Waits before playing a soft A note.
rest(2.5)
playNote(69, beats=1, velocity=38)
rest(0.5)

rest(4)

# Cmaj7 - E
# Adds an E note near the end of the section.
rest(2)
playNote(64, beats=1.5, velocity=36)
rest(0.5)

# 3. AWE - 12 beats
# Longer pauses create an open and spacious atmosphere.

# Fmaj7 - A
# A single note adds a gentle accent.
rest(1)
playNote(69, beats=1, velocity=40)
rest(1)

# Gsus4 - leave space
# The guitar pauses to let the piano stand out.
rest(4)

# Cmaj9 - E
# A longer E note adds a soft layer to the harmony.
rest(1.5)
playNote(64, beats=2, velocity=36)
rest(0.5)

# 4. DISAPPOINTMENT - 8 beats
# The guitar stops completely to create an emotional contrast.
rest(8)

# 5. HAPPINESS - 12 beats
# The guitar returns with a few gentle melodic accents.

# Fmaj7 - A
# Plays a soft A note after a short pause.
rest(2)
playNote(69, beats=1.5, velocity=38)
rest(0.5)

# Gadd9 - D
# Introduces a different pitch for variation.
rest(2.5)
playNote(62, beats=1, velocity=33)
rest(0.5)

# Cmaj7 - E
# Adds another soft note to support the harmony.
rest(2)
playNote(64, beats=1.5, velocity=36)
rest(0.5)

# 6. CALMNESS - 12 beats
# The guitar becomes quieter near the ending.

# Am7 - E
# A low velocity creates a gentle final guitar accent.
rest(2)
playNote(64, beats=1.5, velocity=28)
rest(0.5)

# Leave the ending to the piano
# Eight beats of silence allow the piano to finish alone.
rest(8)
