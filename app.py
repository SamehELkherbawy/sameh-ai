from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    # هنا هنحط الـ AI الحقيقي لاحقاً
    response = f"أنا سامح، فهمت رسالتك: {user_message}"
    return jsonify({'response': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
