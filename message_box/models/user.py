from message_box import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String)
    role = db.Column(db.Integer)
