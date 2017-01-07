def send_message(sender_nickname, receiver_nickname, content):
    from message_box.utils.model_utils.user_model_util import get_user_by_nickname
    from message_box import db
    from message_box.utils.model_utils.message_model_util import new_message
    from message_box.utils.model_utils.messagelog_model_util import new_messagelog
    sender = get_user_by_nickname(sender_nickname)
    receiver = None if receiver_nickname == '' else get_user_by_nickname(receiver_nickname)

    if sender.role != 0:
        message = new_message(sender.id, content, message_type=0)
        db.session.add(message)
        db.session.flush()
        message_log = new_messagelog(receiver.id, message.id)
        db.session.add(message_log)
        db.session.commit()
        return True
    elif sender.role == 0:
        message = new_message(sender.id, content, message_type=16)
        db.session.add(message)
        db.session.commit()
        return True
    return False
