from message_box import db
from datetime import datetime

'''
message_type
0 - private message(p2p)
16 - global message(admin2all)
'''


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    message_type = db.Column(db.Integer)
    content = db.Column(db.String)
    post_time = db.Column(db.DateTime, default=datetime.now)
