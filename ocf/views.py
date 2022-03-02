import os
import uuid
import time

from flask import current_app as app
from flask import request, render_template, jsonify, redirect, url_for

from ocf import db
from ocf.utils import superimpose_images, generate_ticket
from ocf.models import Ticket
from ocf.constants import AVATAR_ALLOWED_FORMATS, AVATAR_OVERLAY_IMAGE


@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')


@app.route('/avatar', methods=['GET'])
def avatar_page():
    return 'hi'


@app.route('/avatar', methods=['POST'])
def avatar_process():
    # Check and save the uploaded file
    if 'avatar' not in request.files:
        return json_resp(code=-1, message='缺失文件')
    avatar_file = request.files.get('avatar')
    if avatar_file is None or avatar_file.filename == '':
        return json_resp(code=-1, message='缺失文件')
    avatar_extension = get_file_extension(avatar_file.filename)
    if avatar_extension[1:] not in AVATAR_ALLOWED_FORMATS:
        return json_resp(code=-1, message='文件格式不支持')
    avatar_filename = str(uuid.uuid1()) + avatar_extension
    avatar_filepath = os.path.join(app.config['UPLOAD_DIR'], avatar_filename)
    avatar_file.save(avatar_filepath)

    # Superimpose overlay image
    try:
        superimposed_filename = superimpose_images(avatar_filepath, AVATAR_OVERLAY_IMAGE.as_posix())
        return json_resp({'name': superimposed_filename})
    except Exception as e:
        return json_resp(code=-2, message=f'出现错误：{str(e)}')


@app.route('/ticket', methods=['GET'])
def ticket_page():
    return 'hi'


@app.route('/ticket', methods=['POST'])
def ticket_generate():
    req_data = request.json or request.form
    name = req_data.get('name')
    if not name:
        return json_resp(code=-1, message='名称不能为空')
    ticket = Ticket(name=name)
    db.session.add(ticket)
    db.session.commit()
    ticket_id = '#' + str(ticket.id).zfill(7)
    ticket_filename = generate_ticket(name, ticket_id)
    return json_resp({'name': ticket_filename})
    

def get_file_extension(filename):
    if '.' not in filename:
        return ''
    return '.' + filename.rsplit('.', 1)[1].lower()


def json_resp(data=None, code=0, message='Success'):
    resp_data = {'code': code, 'message': message}
    if data is not None:
        resp_data['data'] = data
    if code != 0 and message == 'Success':
        resp_data['message'] = 'Error'
    return jsonify(resp_data)
