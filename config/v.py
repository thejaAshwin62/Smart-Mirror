import speech_recognition as sr

def listen():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use default microphone as audio source
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to recognize audio
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def main():
    # Example: Listen for a command
    command = listen()
    # Perform action based on command

if __name__ == "__main__":
    main()
