from message_box import db

'''
status
0 - unread
1 - readed
'''


class MessageLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receiver_id = db.Column(db.Integer)
    message_id = db.Column(db.Integer)
    status = db.Column(db.Integer)
