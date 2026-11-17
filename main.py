import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import webbrowser
import datetime
import wikipedia


class SoundDeviceStream:
    def __init__(self, stream):
        self._stream = stream

    def read(self, size):
        audio, _ = self._stream.read(size)
        return bytes(audio)

    def stop(self):
        self._stream.stop()

    def close(self):
        self._stream.close()


class SoundDeviceMicrophone(sr.AudioSource):
    CHUNK = 1024
    SAMPLE_RATE = 16000
    SAMPLE_WIDTH = 2

    def __init__(self):
        self.stream = None

    def __enter__(self):
        raw_stream = sd.RawInputStream(
            samplerate=self.SAMPLE_RATE,
            channels=1,
            dtype="int16",
            blocksize=self.CHUNK,
        )
        try:
            raw_stream.start()
        except Exception:
            raw_stream.close()
            raise
        self.stream = SoundDeviceStream(raw_stream)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.stream is not None:
            try:
                self.stream.stop()
            finally:
                try:
                    self.stream.close()
                finally:
                    self.stream = None


def takeCommand():
    r = sr.Recognizer()

    with SoundDeviceMicrophone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if voices:
        engine.setProperty('voice', voices[0].id)

    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in day_dict:
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    minute = time[14:16]
    speak("The time is mam " + hour + " Hours and " + minute + " Minutes")


def Hello():
    speak("hello mam I am your desktop assistant. Tell me how may I help you")


def Take_query():
    Hello()

    while True:
        query = takeCommand().lower()
        if query == "None":
            continue

        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks")
            webbrowser.open("https://www.geeksforgeeks.org")
            continue

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            continue

        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        elif "bye" in query:
            speak("Bye. Check Out GFG for more exciting things")
            exit()

        elif "wikipedia" in query:
            speak("Checking the wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query.strip(), sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop Assistant")


if __name__ == '__main__':
    Take_query()
