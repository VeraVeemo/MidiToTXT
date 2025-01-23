import mido
from mido import MidiFile

def note_number_to_name(note_number):
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (note_number // 12) - 1
    note = note_names[note_number % 12]
    return f"{note}{octave}"

def midi_to_text(midi_file):
    midi = MidiFile(midi_file)
    text_output = []

    for i, track in enumerate(midi.tracks):
        text_output.append(f"Track {i+1}: {track.name}")
        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                note_name = note_number_to_name(msg.note)  # Convert note number to name
                event_type = 'Note On' if msg.type == 'note_on' else 'Note Off'
                text_output.append(f"{event_type} - {note_name} (Velocity: {msg.velocity}) at time {msg.time}")
                
    return "\n".join(text_output)

midi_file = input("Enter your Midi File path: ")
text_output = midi_to_text(midi_file)
print(text_output)