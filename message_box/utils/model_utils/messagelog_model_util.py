from sqlalchemy.orm import load_only, defer
import datetime


def new_messagelog(receiver_id, message_id, status=0):
    from message_box.models.messagelog import MessageLog
    return MessageLog(receiver_id=receiver_id, message_id=message_id, status=status)


def get_messagelog_list(nickname, message_type, status):
    from user_model_util import get_user_by_nickname
    from message_box.models.messagelog import MessageLog
    from message_box.models.message import Message
    user = get_user_by_nickname(nickname)

    if message_type == 16:
        current_time = datetime.datetime.now()
        ten_minutes_ago = current_time - datetime.timedelta(minutes=10)
        subquery = MessageLog.query.options(load_only('message_id').defer("id")).filter_by(receiver_id=user.id)
        global_message = Message.query.filter_by(message_type=message_type).filter(Message.id.notin_(subquery)).filter(
            Message.post_time > ten_minutes_ago).all()
        d = []
        for message in global_message:
            d.append({'message_id': message.id})
        return d
    elif message_type == 0:
        rv = MessageLog.query.filter_by(status=status, receiver_id=user.id).all()
        d = []
        for log in rv:
            d.append({'message_id': log.message_id, 'log_id': log.id, 'status': log.status})
        return d
    elif message_type == -1:
        subquery = MessageLog.query.options(load_only('message_id').defer("id")).filter_by(receiver_id=user.id)
        global_message = Message.query.filter_by(message_type=16).filter(Message.id.notin_(subquery)).all()
        d = []
        for message in global_message:
            d.append({'message_id': message.id})

        rv = MessageLog.query.filter_by(status=status, receiver_id=user.id).all()
        for log in rv:
            d.append({'message_id': log.message_id, 'log_id': log.id, 'status': log.status})
        return d
    else:
        return []


def read_message(nickname, message_id):
    from user_model_util import get_user_by_nickname
    from message_box.models.messagelog import MessageLog
    from message_box.models.message import Message
    from message_box import db
    user = get_user_by_nickname(nickname)
    message = Message.query.filter_by(id=message_id).first()
    if message:
        if message.message_type == 16:
            log = new_messagelog(user.id, message_id, 1)
            db.session.add(log)
            db.session.commit()
        else:
            log = MessageLog.query.filter_by(receiver_id=user.id, message_id=message_id).first()
            if not log:
                return False
            log.status = 1
            db.session.commit()
        return True
    else:
        return False
