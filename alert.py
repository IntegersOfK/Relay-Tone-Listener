import aubio
import numpy as num
import pyaudio
import wave
import time

# PyAudio object.
p = pyaudio.PyAudio()

# Open stream.
stream = p.open(format=pyaudio.paFloat32,
    channels=1, rate=44100, input=True,
    frames_per_buffer=1024)

# Aubio's pitch detection.
pDetection = aubio.pitch("default", 2048,
    2048//2, 44100)
# Set unit.
pDetection.set_unit("Hz")
pDetection.set_silence(-40)

check_buffer = []

while True:

    data = stream.read(1024, exception_on_overflow=False)
    samples = num.fromstring(data,
        dtype=aubio.float_type)
    pitch = pDetection(samples)[0]
    # Compute the energy (volume) of the
    # current frame.
    volume = num.sum(samples**2)/len(samples)
    # Format the volume output so that at most
    # it has six decimal numbers.
    volume = "{:.6f}".format(volume)

    print(pitch)
    #print(volume)
    check_buffer.append(pitch)

    if len(check_buffer) > 10:
	# Do the check now that we have 10 samples
	if len([buff for buff in check_buffer if buff > 3000 and buff < 3100]) > 5:
		print("ALERTING")
		time.sleep(1);
	check_buffer = [] # Wipe the buffer to listen from scratch

    
