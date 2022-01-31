import torch
import freefield
import slab
import numpy as np
from pathlib import Path
import time

freefield.initialize_setup('dome', default_mode="play_rec")

# speaker_IDs = [21, 22, 23, 24, 25]
# levels = [70, 80, 90, 100]

speaker_IDs = [21, 22]
levels = [70, 80]

click = slab.Sound.pinknoise(samplerate=slab.signal._default_samplerate, duration=0.01)
pink_noise = slab.Binaural.pinknoise(samplerate=slab.signal._default_samplerate, duration=3.0)
pulse_noise = pink_noise.pulse(frequency=2, duty=0.5)
tone = slab.Sound.tone(frequency=1500, duration=0.5)
vowel_a = slab.Sound.vowel(vowel='a')
vowel_e = slab.Sound.vowel(vowel='e')
vowel_i = slab.Sound.vowel(vowel='i')
gunshot = slab.Sound.read('212208__alexthegr81__tapesnare-15.wav')
balloon = slab.Sound.read('178475__digitaldominic__balloon-popping.wav')

gunshot.samplerate = 48828
balloon.samplerate = 48828

sounds = {
    # "click": click,
    "pink_noise": pink_noise,
    "pulse_noise": pulse_noise,
    # "gunshot": gunshot,
    # "balloon": balloon,
    "tone": tone
}

i = 1

for speaker_ID in speaker_IDs:
    print(speaker_ID)
    for sound_ID, sound in sounds.items():
        print(sound_ID)
        for level in levels:
            sound.level = level

            freefield.write('trigcode', i, 'RX82')

            rec = []
            rec = freefield.play_and_record_reverb(sound, speaker_ID)
            # speaker_name = "speaker-" + str(speaker_ID)
            # sound_name = "sound-" + sound_ID
            # level_name = "level-" + str(level)
            # file_name = speaker_name + "_" + sound_name + "_" + level_name + ".wav"
            # rec.write(file_name,  normalise=False)
            time.sleep(1)
            i += 1
