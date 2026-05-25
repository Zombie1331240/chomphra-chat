from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "chomphra-chat is running successfully on Cloud!"

@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"status": "error", "message": "Missing 'message' field"}), 400
        
        user_msg = data.get('message')
        sender = data.get('sender', 'Unknown User')
        print(f"[{sender}]: {user_msg}")
        
        return jsonify({
            "status": "success",
            "received": True,
            "sender": sender,
            "reply": f"Chomphra-chat ได้รับข้อความ '{user_msg}' เรียบร้อยแล้วครับ"
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
