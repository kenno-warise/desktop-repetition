# 音声認識反復アプリ

音声認識ライブラリと音声合成ライブラリを使用して、発した言葉をPCが反復するといったシステムです。

現在の使用では、「音声」と「テキスト」のどちらかに対応しています。

発言もしくは入力されたテキストは、音声合成ライブラリによってデバイス（ここではLenovo）のスピーカーから機械の音声として発せられます。

|実行環境|
|----|
|Windows Subsystem for Linux 1|
|Windows10 コマンドプロンプト|
|Python 3.10.0|

|Python外部ライブラリ|
|----|
|PyAudio==0.2.12|
|pyttsx3==2.90|
|SpeechRecognition==3.8.1|
|pyinstaller|

このリポジトリをクローンしてPythonコマンドで実行するには、Windows10の環境で行ってください。

- 以下導入方法（WSLのUbuntuターミナルでリポジトリをクローンします。その後のコマンドはWindows10のコマンドプロンプトでの作業です。）

※WSLのUbuntuターミナル
```
$ git clone https://github.com/kenno-warise/desktop-repetition.git

$ cd desktop-repetition
```

UbuntuからWindowsコマンドプロンプトに切り替える

```
desktop-repetition$ cmd.exe

C:\desktop-repetition>
```

WindowsコマンドプロンプトからUbuntuに切り替えるのは

```
C:\desktop-repetition>wsl

desktop-repetition$
```

※Windows10のコマンドプロンプト

```
C:\desktop-repetition>python -m venv .venv

C:\desktop-repetition>.venv\scripts\activate

(.venv) C:\desktop-repetition>pip install --upgrade pip

(.venv) C:\desktop-repetition>pip install -r requirements.txt

(.venv) C:\desktop-repetition>python main.py
```

※.exe化してデスクトップアプリを作る

```
(.venv) C:\desktop-repetition>pyinstaller main.py --onefile --icon=favicon.ico
```

エクスプローラーから「desktop-repetition」フォルダ内の「dist」と言うフォルダに「main.exe」ファイルあるのでそれをダブルクリック。


## .exe化したアプリを実行している様子

音声認識反復アプリをデスクトップに配置した場合

![repetition_disk](https://user-images.githubusercontent.com/51676019/202615129-51e4a2a6-55de-4c26-8e1e-c6cb84d47ccc.jpg)

クリックするとコンソールが表示されます。

![repetition_disk_2](https://user-images.githubusercontent.com/51676019/202615157-ae41e168-1289-4c3e-b154-49cbcbed8b61.jpg)

何も発言しないと、「発言してください」と促されます。

![repetition_disk_3](https://user-images.githubusercontent.com/51676019/202615182-f3442cb5-3564-42a7-9beb-1daea99adf4e.jpg)
