# ThroneAndLiberty_ServerStatusCheck
# 概要
- THTONE AND LIVERTYのALEXIAサーバーのステータスをチェックするアプリケーションです。

## 下記のWEBサイトをチェックしています。
https://www.playthroneandliberty.com/ja-jp/support/server-status

# 動作内容
- 実行するとWindowsコンソールが立ち上がり20秒に一回サイトをチェックします。
- メンテナンス状態でない場合は、BEEP音3回鳴らしてMsgBox表示して終了します。

# exe作成方法
1. pyinstallerをインストール
~~~ windows shell
pip install pyinstaller
~~~ 

2. コマンドプロンプトで作業フォルダに移動し下記を実行
~~~ windows shell
pyinstaller ThroneAndLiberty_ServerStatusCheck.py
~~~