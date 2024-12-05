# -*- coding: utf-8 -*-
# author: itimor

import os
from qrcode import QRCode, constants
import pyotp
import base64
from cpzw import settings


def get_qrcode(secret_key, username):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.dirname(BASE_DIR) + '/upload/qrcode/'
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    suffix = settings.SITE
    data = pyotp.totp.TOTP(secret_key).provisioning_uri(username + '@' + suffix, issuer_name="彩票之王 Verfiy Code")
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=6,
        border=4, )
    try:
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        img_name = filepath + secret_key + '.png'
        img.save(img_name)  # 保存条形码图片

        with open(img_name, "rb") as f:
            # b64encode是编码，b64decode是解码
            return "data:image/png;base64," + bytes.decode(base64.b64encode(f.read()))
    except Exception as e:
        print(e)
        return False


def verify_qrcode(secret_key, verifycode):
    t = pyotp.TOTP(secret_key)
    result = t.verify(verifycode)  # 对输入验证码进行校验，正确返回True
    msg = result if result is True else False
    return msg