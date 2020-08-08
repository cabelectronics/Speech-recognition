



    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125) 

    volume = engine.getProperty('volume')
    engine.setProperty('volume',1.0)  

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  

    engine.say(text)
    engine.runAndWait()