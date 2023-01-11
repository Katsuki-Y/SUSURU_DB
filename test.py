import sys
import os
import sqlite3
import tkinter as tk

# sqliteの初期設定
dbfile = "test.db"
conn = sqlite3.connect(dbfile)
cur = conn.cursor()#データベースを操作するカーソルを指定

# tkinter UIの初期設定
root = tk.Tk()
root.title("SUSURU.DB [ SUSURUTV 訪問ラーメン店検索 ]") # タイトル
root.configure(bg='papaya whip')#ウィンドウの設定 bg=背景色
root.geometry("500x800")#ウィンドウサイズ
root.resizable(width=False, height=False)#ウィンドウサイズを変更不可に

#-----------------1回のみ実行する郡 CREATEやINSERT,DELETE等を書く----------------
# テーブル作成処理
#cur.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')

# 情報の追加
#cur.execute('INSERT INTO persons(name) values("Hanako")')
#cur.execute('INSERT INTO persons(name) values("Hiroki")')

# データベースへコミット
#conn.commit()
#----------------------------------------------------------------------------

for data in cur.execute("SHOW TABLES;"):
    print(data)

# 関数
def val():
    cur.execute("SELECT name FROM persons WHERE id = '" + txt1.get() + "'");#入力された番号からid検索してnameを持ってくる
    label_ans = tk.Label(root, text = cur.fetchall(), fg='black', bg='papaya whip')
    label_ans.place(x=10, y=150)

# UI
label1 = tk.Label(root, text='囚人番号を入力してください',fg='black', bg='papaya whip')
label1.place(x=10, y=10)

txt1 = tk.Entry(width=10,fg='black', bg='white')
txt1.place(x=10, y=50)

button1 = tk.Button(root, text = 'OK', command = val ,bg = "papaya whip")
button1.place(x=10, y=100)


root.mainloop()#ウィンドウを更新

conn.close
