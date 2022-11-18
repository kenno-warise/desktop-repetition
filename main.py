import speech_recognition as sr
import pyttsx3


r = sr.Recognizer() # 文字起こし
engine = pyttsx3.init() # 文字の読み出し
quit_list = ['終了', '辞める', 'さようなら']

while True:
    r = sr.Recognizer() # 文字起こし
    engine = pyttsx3.init() # 文字の読み出し
    with sr.Microphone(device_index=0) as input:
        print('録音中:')
        audio = r.listen(input)
    try:
        text = r.recognize_google(audio, language='ja-JP')
        print(text)
        if text in quit_list:
            engine.say(text)
            engine.runAndWait()
            break
        engine.say(text)
        engine.runAndWait()
    except:
        someting = '何か発音してください'
        print(someting)
        engine.say(someting)
        engine.runAndWait()
