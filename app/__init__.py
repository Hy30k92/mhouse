from flask import Flask

app = Flask(__name__)
app.config.from_object("config")  # 이 설정은 config.py를 찾으려고 합니다
