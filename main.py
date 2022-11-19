import speech_recognition as sr
import pyttsx3


r = sr.Recognizer() # 文字起こし
engine = pyttsx3.init() # 文字の読み出し
quit_list = ['終了', '辞める', 'さようなら']

while True:
    r = sr.Recognizer() # 文字起こしオブジェクトの初期化
    engine = pyttsx3.init() # 文字の読み出しオブジェクトの初期化
    with sr.Microphone(device_index=0) as input:
        print('録音中:')
        audio = r.listen(input)
    # audioに録音された内容に従ってtry文処理を行う
    try:
        # 音声認識されたらその文言を音声合成により読み出す
        text = r.recognize_google(audio, language='ja-JP')
        print(text)
        engine.say(text)
        if text in quit_list:
            # 音声認識された文言がquit_list内にあれば無限ループが停止する
            engine.runAndWait()
            break
        engine.runAndWait()
    except:
        # 音声認識が何もされなければ、発言を促さすように以下のストリングを読み出す
        someting = '何か発音してください'
        print(someting)
        engine.say(someting)
        engine.runAndWait()
