#!/usr/bin/env python

from datetime import datetime
from pickle import dump, load

from tkinter import *
import tkinter.messagebox

from todoitem import ToDoItem
from todocontainer import ToDoContainter

# データ保存用ファイル
DUMPFILE = 'todo.dat'

class ToDoApp(Frame):
    """
    ToDo GUIアプリ用クラス
    """
    def createwidgets(self):
        """
        ボタンなどウィンドウの部品を作る
        """
        # スクロールバー付きリストボックス
        self.frame1 = Frame(self)

        frame = self.frame1

        self.listbox = Listbox(frame, height=10, width=30, selectmode=SINGLE, takefocus=1)
        self.yscroll = Scrollbar(frame, orient=VERTICAL)

        # 配置を決める
        self.listbox.grid(row=0, column=0, sticky=NS)
        self.yscroll.grid(row=0, column=0, sticky=NS)

        # 動きとコードを繋げる
        self.yscroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.yscroll.set)
        self.listbox.bind("<ButtonRelease-1>", self.selectitem)

        self.frame1.grid(row=0, column=0)

    
    def setlistitems(self):
        """
        ToDoの内、未消化分のみをリストに表示する
        """
        self.listbox.delete(0, END)
        for todo in self.todos.get_remaining_todos():
            d = todo.duedate
            t = todo.title.ljust(20)
            if todo.duedate < datetime.now():
                t = '* '+t
                item = "{} {:4}/{;02}/{:02} {:02}:{:02}".format(t, d.year, d.month, d.day, d.hour, d.minute)
                self.listbox.insert(END, item)


    def refrectententries(self, todo):
        """
        フィールドに入力された文字列をToDoItemインスタンスに反映する
        """
        todo.title = self.title_e.get()
        todo.description = self.description_e.get()
        dt = datetime.strptime(self.duedate_e.get()+':00', '%Y/%m/%d %H:%M:%S')
        todo.duedate = dt
        if self.finished_v.get() != 0:
            todo.finish()

    def createitem(self):
        """
        新しいToDoアイテムを作る
        """
        todo = ToDoItem('', '', datetime.now())
        self.refrectententries(todo)
        self.todos += todo
        self.clearentires()
        self.setlistitems()
        self.sel_index = -1
        self.save()


    def refreshitems(self):
        """
        タイマーで定期的に呼び出されるメソッド
        ToDoのうち時間になったものがあれば、ダイアログで知らせる
        """
        dirty = False
        for todo in self.todos.get_remaining_todos():
            td = datetime.now()
            d = todo.duedate
            if (d.year == td.year and
                d.month == td.month and
                d.day == td.day and
                d.hour == td.hour and
                d.minute == td.minute):
                msg = "{}の時間です。\n {}".format(todo.title, todo.description, todo.duedate.strftime('%Y/%m/%d %H:%M'))
                tkinter.messagebo.showwarning("時間です。", msg)
                dirty = true
        
        sec = datetime.now().second
        self.after((60-sec)*1000, self.refreshitems)

        if dirty:
            self.setlistitems()

        def load(self):
            """
            ToDoデータをファイルから読み込む
            """
            try:
                f = open(DUMPFILE, 'rb') # !!!
                self.todos = load(f)
            except IOError:
                self.todos = ToDoContainer()

        def save(self):
            """
            ToDoデータをファイルに書き出す
            """
            f = open(DUMPFILE, 'wb') #!!!
            dump(self.todos, f)

    
        

        

