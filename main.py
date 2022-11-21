from voice_tool import Repetition


iteration_menu = """----------
テキスト入力の場合は何か文字を入力してから「Enter」キーを押してください。
音声認識の場合は何も入力せずにそのまま「Enter」キーを押してください。
----------

"""
print(iteration_menu)

choice = input()


if choice:
    # テキストモード
    Repetition().text_reco()
else:
    # 音声認識モード
    Repetition().voice_reco()

