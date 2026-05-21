from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Chomphra-chat กำลังทำงานบนคลาวด์!"

if __name__ == '__main__':
    # บรรทัดนี้คือหัวใจสำคัญที่ทำให้ Cloud รู้จัก Port เจ้าค่ะ
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
