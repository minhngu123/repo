from flask import Flask, request, jsonify, abort, session
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Giả lập cơ sở dữ liệu người dùng
users = {
    "1": {"id": 1, "name": "Alice", "email": "alice@example.com"},
    "2": {"id": 2, "name": "Bob", "email": "bob@example.com"}
}

@app.route('/user/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    session['user_id'] = user_id
    return f"Logged in as {user_id}"

@app.route('/user/<user_id>', methods=['GET', 'POST'])
def user_profile(user_id):
    current_user_id = session.get('user_id')

    if not current_user_id or current_user_id != user_id:
        abort(403)
    if request.method == 'GET':
        # Lấy thông tin người dùng
        user = users.get(user_id)
        if user:
            return jsonify(user)
        return "User not found", 404

    if request.method == 'POST':
        # Cập nhật thông tin người dùng
        if user_id in users:
            data = request.get_json()
            users[user_id].update(data)
            return jsonify(users[user_id])
        return "User not found", 404
    
if __name__ == '__main__':
    app.run(debug=True)