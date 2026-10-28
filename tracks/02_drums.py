# This function creates a four-beat drum pattern.
# The lists store the positions of kicks, snares and hi-hats.
# Strength controls how strongly the drums are played.
def drum_bar(kicks, snares, hats, strength):
    # Saves the starting position of the current bar.
    start = getPlayhead()
# A loop places kick sounds at different beat positions.
    for beat in kicks:
        moveTo(start + beat)
        playNote(0, beats=0.25, velocity=strength)
# The snare is played slightly softer than the kick.
    for beat in snares:
        moveTo(start + beat)
        playNote(2, beats=0.25, velocity=strength - 12)
# Enumerate gives both the index and beat position.
# Alternating velocities make the hi-hats less repetitive.
    for i, beat in enumerate(hats):
        moveTo(start + beat)
        playNote(4,beats=0.125,velocity=32 if i % 2 == 0 else 23 )
        
# Moves the playhead to the beginning of the next bar.
    moveTo(start + 4)

# 1. ANTICIPATION
# The drums stay silent for eight beats.
# This creates space for the opening melody.
rest(8)

# 2. EXCITEMENT
# Different kick positions create a more active rhythm.
# The final bar adds extra snare hits for variation.
drum_bar([0, 2.5], [1, 3],[0.5, 1.5, 2.5, 3.5], 58)

drum_bar([0, 1.75, 2.5], [1, 3],[0.5, 1.5, 2.75, 3.5], 64)

drum_bar([0, 2, 3.5], [1, 3, 3.75],[0.5, 1.5, 2.5], 68)

# 3. AWE
# Fewer drum hits create a slower, more open feeling.
# The snare moves to beat two in each bar.
drum_bar([0, 3.5], [2],[0.5, 1.5, 3], 66)

drum_bar([0, 1.5], [2],[0.5, 2.75, 3.5], 62)

drum_bar([0], [2],[1.5, 3], 60)

# 4. DISAPPOINTMENT
# The drums stop completely for eight beats.
# This creates a strong contrast with the previous section.
rest(8)

# 5. HAPPINESS
# The earlier rhythmic pattern returns at a softer volume.
# Small changes in beat positions keep the rhythm varied.
drum_bar([0, 2.5], [1, 3],[0.5, 1.5, 2.5, 3.5], 54)

drum_bar([0, 1.75, 2.5], [1, 3],[0.5, 1.5, 3.5], 58)

drum_bar([0, 2], [1, 3],[0.5, 2.5, 3.5], 54)

# 6. CALMNESS
# Only one soft drum bar remains before the final silence.
# The empty snare list means no snare notes are played.
drum_bar([0], [],[1.5, 3], 40)

rest(8)
