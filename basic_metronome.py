import random
import string
import time
import webbrowser

# The various YouTube drum rythmic patterns depending on the tempo
video_from_tempo = {
    60: 'https://www.youtube.com/watch?v=aQoUfeRawX8',
    70: 'https://www.youtube.com/watch?v=4SDBJp_B5qQ',
    80: 'https://www.youtube.com/watch?v=uH1MrhJZ2NA',
    90: 'https://www.youtube.com/watch?v=9U3RG0JU4Ds',
    100: 'https://www.youtube.com/watch?v=zZbM9n9j3_g'
}

# The instructions that are going to be randomly generated
instructions = [
    'octave',
    'fifth - octave',
    'arpeggio',
    'scale'
]

# The mode (only relevant for arpeggio and scale instructions)
modes = [
    'major',
    'minor'
]

notes = string.ascii_uppercase[:7]

# The various parameters
tempo = 80 # beats per minute
beat_duration = 60 / tempo  # Duration of a single beat in seconds
measures = 4  # number of measures
beats_per_measure = 4  # beats per measure (4/4 time)

webbrowser.open_new(video_from_tempo[tempo])

# Waiting for the user to press 'space' to start
# commented out because the natural delay before the video is launched is usually good enough
# user_input = input("Press 'enter' to continue...")

# Display text on the console every 4 measures
while True:
    # Pick an instruction
    instr = random.choice(instructions)
    # Pick a base note
    note = random.choice(notes)
    mode = None
    if instr in ['arpeggio', 'scale']:
        mode = random.choice(modes)
    instr += ' -- ' + note + (' -- ' + mode if mode else "")
    print(instr)
    time.sleep(measures*beats_per_measure*beat_duration)