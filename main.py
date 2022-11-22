from voice_tool import Repetition


iteration_menu = """----------
テキスト入力の場合は何か文字を入力してから「Enter」キーを押してください。
音声認識の場合は何も入力せずにそのまま「Enter」キーを押してください。
----------

"""
print(iteration_menu)
quit_list = ['終了します', 'やめよう', 'やめる', '辞める', 'さようなら', 'おわり', '終わり', 'じゃあ', 'じゃあね']
choice = input()
repetition = Repetition(quit_list=quit_list)

if choice:
    print('テキストモード---->\n')
    while True:
        input_text = input('\n入力 :')
        if input_text in repetition.quit_list:
            repetition.text_reco(input_text)
            break
        elif not input_text:
            repetition.nothing_input()
        else:
            repetition.text_reco(input_text)
else:
    print('音声認識モード--->\n')
    repetition.voice_reco()

