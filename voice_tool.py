import speech_recognition as sr
import pyttsx3


class Repetition:
    
    def __init__(self):
        self.quit_list = ['終了', '終了します', 'やめよう', 'やめる', '辞める', 'さようなら', 'おわり', '終わり', 'じゃあ', 'じゃあね']
        # self.input_text = choice
        self.engine = pyttsx3.init() # 文字の読み出しオブジェクトの初期化

    def text_reco(self, input_text):
        # text_recoメソッドが呼ばれたら、テキストモードとして入力されたテキストを読みだしする
        # print('テキスト入力してください---->\n')
        """
        チャットボットを組み合わせる場合はinput_valueを与えるとよい
        """
        text = input_text
        engine = self.engine
        engine.say(text)
        return engine.runAndWait()
        
    def voice_reco(self):
        # voice_recoメソッドが呼ばれたら、マイクから拾われた音声をテキストに文字起こしする

        while True:
            r = sr.Recognizer() # 文字起こしオブジェクトの初期化
            engine = self.engine
            with sr.Microphone(device_index=0) as input:
                print('録音中: ')
                audio = r.listen(input)
            # audioに録音された内容に従ってtry文処理を行う
            try:
                """
                チャットボットを組み合わせる場合はtextを与えるとよい
                """
                # 音声認識されたらその文言を音声合成により読み出す
                text = r.recognize_google(audio, language='ja-JP')
                print(text + '\n')
                engine.say(text)
                if text in self.quit_list:
                    engine.runAndWait()
                    break
                engine.runAndWait()
            except:
                self.nothing_input()

    def nothing_input(self):
        someting = '何かありませんか？\n'
        print(someting)
        engine = self.engine
        engine.say(someting)
        engine.runAndWait()
            
"""
こっちのクラスはメソッドを呼び出すだけでいい

class Repetition:
    
    def __init__(self):
        self.quit_list = ['終了', '終了します', 'やめよう', 'やめる', '辞める', 'さようなら', 'おわり', '終わり', 'じゃあ', 'じゃあね']
    
    def text_reco(self):
        # text_recoメソッドが呼ばれたら、テキストモードとして入力されたテキストを読みだしする
        print('テキスト入力してください---->\n')
            
        while True:
            input_value = input('\n入力: ')
            engine = pyttsx3.init() # 文字の読み出しオブジェクトの初期化
    
            if input_value:
                
                #チャットボットを組み合わせる場合はinput_valueを与えるとよい
                
                text = input_value
                engine.say(text)
                if text in self.quit_list:
                    # 入力テキストがquit_list内にあれば無限ループが停止する
                    engine.runAndWait()
                    break
                engine.runAndWait()
            else:
                # 何も入力されなかった場合は以下を返す
                self.nothing_input(engine)
    
    def voice_reco(self):
        # voice_recoメソッドが呼ばれたら、マイクから拾われた音声をテキストに文字起こしする
        print('音声認識モード準備中です---->\n')
    
        while True:
            r = sr.Recognizer() # 文字起こしオブジェクトの初期化
            engine = pyttsx3.init() # 文字の読み出しオブジェクトの初期化
            with sr.Microphone(device_index=0) as input:
                print('録音中: ')
                audio = r.listen(input)
            # audioに録音された内容に従ってtry文処理を行う
            try:
                
                #チャットボットを組み合わせる場合はtextを与えるとよい
                
                # 音声認識されたらその文言を音声合成により読み出す
                text = r.recognize_google(audio, language='ja-JP')
                print(text + '\n')
                engine.say(text)
                if text in self.quit_list:
                    # 音声認識された文言がquit_list内にあれば無限ループが停止する
                    engine.runAndWait()
                    break
                engine.runAndWait()
            except:
                # 音声認識が何もされなければ、発言を促さすように以下のストリングを読み出す
                self.nothing_input(engine)

    def nothing_input(self, engine):
        someting = '何かありませんか？\n'
        print(someting)
        engine.say(someting)
        engine.runAndWait()
"""            
