from datetime import datetime, timedelta

"""
TODO項目を保存するためのクラス
"""
class ToDoItem(object):

    """
    TODO項目インスタンスを初期化する
    """
    def __init__ (self, title, description, duedate, addeddate=None):
        if not addeddate:
            addeddate = datetime.now()

        self.title = title            # タイトル
        self.dscription = description # 解説
        self.duedate = duedate        # 締め切り日
        self.addeddate = addeddate    # 追加日
        self.finished = False         # 終了フラグ
        self.finisheddate = None      # 終了日

    """
    TODO項目を終了する
    """
    def finish (self, date=None):
        self.finished = True
        
        if not date:
            self.finisheddate = datetime.now()

    
    """
    TODO項目の表示式文字列を作成する
    """
    def __repr__(self):
        return "<ToDoItem {}, {}>".format(self.title, self.duedate.strftime('%Y/%m/%d %H:%M'))


    
