def new_message(sender_id, content, message_type):
    from message_box.models.message import Message
    return Message(sender_id=sender_id, content=content, message_type=message_type)
