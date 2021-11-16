import pyaudio
import struct
import wave

def record(outputFile):
    #defining audio variables
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    Y = 100

    #Calling pyadio module and starting recording
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=chunk)

    stream.start_stream()
    print("Starting!")

    #Recording data until under threshold
    frames=[]

    while True:
        #Converting chunk data into integers
        data = stream.read(chunk)
        data_int = struct.unpack(str(2*chunk) +'B', data)
        #Finding average intensity per chunk
        avg_data=sum(data_int)/len(data_int)
        print(str(avg_data))
        #Recording chunk data
        frames.append(data)
        if avg_data < Y:
            break

    #Stopping recording
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Ending recording!")


    #Saving file with wave module
    wf = wave.open(outputFile, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

record('outputFile1.wav')