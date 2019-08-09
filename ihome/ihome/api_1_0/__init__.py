from flask import Blueprint

from ihome.api_1_0 import demo

# 创建蓝图对象
api = Blueprint("api_1_0", __name__)

