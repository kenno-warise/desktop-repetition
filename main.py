import speech_recognition as sr
import pyttsx3


input_text = """----------
テキスト入力の場合は何か文字を入力してから「Enter」キーを押してください。
音声認識の場合はそのまま「Enter」キーを押してください。
----------

"""
quit_list = ['終了', 'やめる', '辞める', 'さようなら']
input_value = input(input_text)

if input_value:
    print('テキスト入力してください---->')
    print()
    
    while True:
        input_value = input('入力: ')
        print()
        engine = pyttsx3.init() # 文字の読み出しオブジェクトの初期化

        if input_value:
            text = input_value
            engine.say(text)
            if text in quit_list:
                # 入力テキストがquit_list内にあれば無限ループが停止する
                engine.runAndWait()
                break
            engine.runAndWait()
        else:
            # 何も入力されなかった場合は以下を返す
            someting = 'テキストを入力してください'
            print(someting)
            print()
            engine.say(someting)
            engine.runAndWait()
else:
    print('音声認識モード準備中です---->')
    print()
    
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
            print()
            engine.say(text)
            if text in quit_list:
                # 音声認識された文言がquit_list内にあれば無限ループが停止する
                engine.runAndWait()
                break
            engine.runAndWait()
        except:
            # 音声認識が何もされなければ、発言を促さすように以下のストリングを読み出す
            someting = '何か発言してください'
            print(someting)
            print()
            engine.say(someting)
            engine.runAndWait()
