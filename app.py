from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/user/<int:user_id>')
def get_user(user_id):
    return jsonify({
        "id": user_id,
        "name": "John Doe",
        "email": f"user{user_id}@example.com"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
