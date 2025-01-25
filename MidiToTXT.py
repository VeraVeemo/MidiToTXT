import mido
from mido import MidiFile

def note_number_to_name(note_number):
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (note_number // 12) - 1
    note = note_names[note_number % 12]
    return f"{note}{octave}"

def midi_to_text(midi_file_path):
    midi = MidiFile(midi_file_path)
    text_output = []
    ticks_per_beat = midi.ticks_per_beat
    tempo = 500000
    current_time = 0

    for i, track in enumerate(midi.tracks):
        text_output.append(f"Track {i + 1}: {track.name}")
        for msg in track:
            if msg.type == 'set_tempo':
                tempo = msg.tempo
            elif msg.type in ['note_on', 'note_off']:
                current_time += msg.time
                seconds = (current_time / ticks_per_beat) * (tempo / 1_000_000)
                note_name = note_number_to_name(msg.note)
                event_type = 'Note On' if msg.type == 'note_on' else 'Note Off'
                text_output.append(
                    f"{event_type} - {note_name} (Velocity: {msg.velocity}) at {current_time} ticks ({seconds:.2f} seconds)."
                )
    return "\n".join(text_output)

file_path = input("Enter the path to the MIDI file: ")
try:
    text_output = midi_to_text(file_path)
    print(text_output)
except Exception as e:
    print(f"Error: {e}")
