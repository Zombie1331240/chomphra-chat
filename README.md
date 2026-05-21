from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Chomphra-chat is running on Cloud!"

if __name__ == '__main__':
    # บรรทัดนี้สำคัญมากสำหรับการนำขึ้น Cloud เจ้าค่ะ
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
