# This track adds soft background harmonies to the music.
# Lists allow two notes to be played at the same time.
# Beats controls how long each chord lasts.
# Velocity keeps the harmonies quieter than the main melody.

# 1. ANTICIPATION
# The harmony stays silent during the opening.
rest(8)

# 2. EXCITEMENT - 12 beats
# The track stays silent to leave space for the rhythm.
rest(12)

# 3. AWE - 12 beats
# Soft harmonies create a fuller and more spacious sound.
# Each pair of notes plays together for 3.5 beats.

# Fmaj7 / Gsus4 / Cmaj9
playNote([57, 60], beats=3.5, velocity=35)
rest(0.5)

playNote([55, 62], beats=3.5, velocity=39)
rest(0.5)

playNote([55, 64], beats=3.5, velocity=43)
rest(0.5)

# 4. DISAPPOINTMENT - 8 beats
# The background harmony disappears to create contrast.
rest(8)

# 5. HAPPINESS - 12 beats
# The harmony returns with slightly softer velocities.
# Different note combinations create a warmer atmosphere.

# Fmaj7 / Gadd9 / Cmaj7
playNote([57, 60], beats=3.5, velocity=33)
rest(0.5)

playNote([59, 62], beats=3.5, velocity=35)
rest(0.5)

playNote([55, 64], beats=3.5, velocity=31)
rest(0.5)

# 6. CALMNESS - 12 beats
# The harmony stops so the piano can lead the ending.
rest(12)


