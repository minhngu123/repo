from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Alice", "role": "user"},
    2: {"name": "Bob", "role": "admin"}
}

@app.route('/user/<int:user_id>')
def get_user(user_id):
    # Không kiểm tra quyền truy cập, trả về thông tin người dùng dựa vào ID
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)