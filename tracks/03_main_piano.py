# This function combines background chords with a main melody.
# Chord contains the notes played together as a harmony.
# Notes stores the melody pitches and their lengths.
# Strength controls the volume of the melody.
def phrase(chord, notes, strength):
# Plays a softer chord for four beats.
    playNote(chord, beats=4, velocity=strength - 22)
# Moves back four beats so the melody overlaps the chord.
    rewind(4)
    
# Loops through each pitch and duration in the melody list.
    for pitch, length in notes:
# None represents a pause instead of a note.
        if pitch is None:
            rest(length)
        else:
            playNote(pitch, beats=length, velocity=strength)

# 1. ANTICIPATION
# A gentle opening uses short notes and pauses.
# The changing melody creates a sense of expectation.
phrase([48, 55, 59, 64],[(None, 0.5), (76, 0.75), (79, 0.25),(74, 1.5), (72, 1)], 66)

phrase([45, 55, 60, 64],[(71, 0.5), (72, 1.5), (76, 0.5),(None, 0.5), (67, 1)], 62)

# 2. EXCITEMENT
# Shorter notes and changing rhythms make the melody more active.
# Higher velocity values give this section more energy.

phrase([53, 57, 60, 64],[(76, 0.75), (79, 0.25), (81, 0.5),(79, 1), (76, 0.5), (72, 1)], 76)

phrase([55, 59, 62, 69],[(74, 1.5), (71, 0.5), (None, 0.5),(74, 0.5), (79, 0.75), (81, 0.25)], 80)

phrase([52, 55, 59, 60],[(79, 0.5), (76, 1), (74, 0.5),(72, 0.75), (76, 0.25), (79, 1)], 84)

# 3. AWE
# Longer notes create a more open and spacious melody.
# The higher pitches help express a sense of wonder.
phrase([53, 60, 64, 69],
       [(81, 1.5), (79, 0.5), (76, 2)], 86)

phrase([55, 60, 62, 67],
       [(79, 0.5), (74, 1), (72, 0.5),
        (74, 1.5), (79, 0.5)], 82)

phrase([48, 55, 62, 64],
       [(84, 2.5), (79, 0.5), (76, 1)], 88)

# 4. DISAPPOINTMENT
# Lower pitches and softer velocities reduce the energy.
# Longer rests create space and a quieter atmosphere.
phrase([45, 52, 55, 60],
       [(72, 1.5), (71, 0.5),
        (69, 1), (None, 1)], 58)

phrase([40, 52, 55, 59],
       [(67, 0.5), (64, 1.5),
        (None, 1.5), (67, 0.5)], 52)

# 5. HAPPINESS
# The melody becomes brighter and more active again.
# Some earlier melodic patterns return with small changes.
phrase([53, 57, 60, 64],
       [(76, 0.75), (79, 0.25), (77, 0.5),
        (76, 1.5), (72, 1)], 74)

phrase([55, 59, 62, 69],
       [(74, 1.5), (71, 0.5), (69, 0.5),
        (71, 0.5), (74, 1)], 76)

phrase([52, 55, 59, 60],
       [(79, 1), (76, 0.5), (74, 0.5),
        (72, 1.5), (67, 0.5)], 78)

# 6. CALMNESS
# Longer notes and lower velocities slow the emotional pace.
# A sustained final note creates a gentle resolution.
phrase([53, 57, 60, 64],[(69, 1.5), (72, 0.5), (76, 2)], 64)

phrase([55, 60, 62, 67],[(74, 1.5), (72, 0.5),(71, 1), (None, 1)], 56)

phrase([48, 55, 62, 64],[(72, 4)], 48)
