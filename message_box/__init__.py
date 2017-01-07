# -*- coding:utf-8 -*-

from flask import Flask, request, jsonify
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.secret_key = app.config['SECRET_KEY']

db = SQLAlchemy(app)
redis_store = FlaskRedis(app)


@app.route('/send', methods=['POST'])
def send():
    sender_nickname = request.form.get('sender', '')
    receiver_nickname = request.form.get('receiver', '')
    content = request.form.get('content', '')
    from message_box.utils import send_message
    rv = send_message(sender_nickname, receiver_nickname, content)
    return jsonify({}) if rv else jsonify({'message': 'fail'})


@app.route('/messagelist')
def get_message_list():
    nickname = request.args.get('nickname', '')
    message_type = int(request.args.get('message_type', 0))
    status = request.args.get('status', 0)
    from message_box.utils.model_utils.messagelog_model_util import get_messagelog_list
    rv = get_messagelog_list(nickname, message_type=message_type, status=status)
    return jsonify(rv)


@app.route('/read')
def read_message():
    nickname = request.args.get('nickname', '')
    message_id = request.args.get('message_id', 0)
    from message_box.utils.model_utils.messagelog_model_util import read_message
    rv = read_message(nickname, message_id)
    return jsonify({'rv': rv})
