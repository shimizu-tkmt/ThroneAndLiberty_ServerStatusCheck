import requests
from bs4 import BeautifulSoup
from ctypes import *    # MsgBox
import time         # Sleep
import datetime     # 現在日時取得
import winsound     # Beep音

url = 'https://www.playthroneandliberty.com/ja-jp/support/server-status'
server_name = 'Alexia'
sleep_time = 20
msg_title = 'ThroneAndLiberty_ServerStatusCheck'
item = ''

try:
    while True:
        # HTMLの取得(GET)
        req = requests.get(url, timeout=6.0)
        req.encoding = req.apparent_encoding # 日本語の文字化け防止

        # HTMLの解析
        bsObj = BeautifulSoup(req.text,"html.parser")

        # 要素の抽出
        spans = bsObj.find_all("span")
        for span in spans:
            #print(span.get_text())
            if span.get_text() == server_name:
                item = span.get("aria-label")
                break

        #現在日時出力
        dt_now = datetime.datetime.now()
        print(dt_now)

        print(item)
        #　右から１１文字で判別
        if item[-11:] != 'Maintenance':  # 取り出した要素が偽と見なされる値（空文字列など）であれば 
            break  # 無限ループを終了
        time.sleep(sleep_time)  # 20秒間スリープ

    # ビープ音を鳴らす　３回音程変えて鳴らす
    #winsound.Beep(frequency, duration)
    winsound.Beep(2500, 500)
    winsound.Beep(3000, 500)
    winsound.Beep(4000, 500)

    # MsgBox表示
    user32 = windll.user32
    user32.MessageBoxW(0, item,msg_title, 0x00000000|0x00000040)

except Exception as e:
    print(f"An error occurred: {e}")
    input("Press Enter to close the program...")

