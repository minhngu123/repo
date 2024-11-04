from flask import Flask, request, jsonify, abort

app = Flask(__name__)

#Giả lập cơ sở dữ liệu người dùng
users={
    1: {"name": "Alice", "role": "user"},
    2: {"name": "Bob", "role": "admin"}
}

#Giả lập cơ sở dữ liệu về quyền truy cập
user_permissions = {
    1: [1], #Người dùng 1 chỉ có thể truy cập vào thông tin của chính mình
    2: [1,2] #Người dùng 2 là admin có thể truy cập thông tin vào tất cả mọi người
}

def check_permission(current_user_id, target_user_id):
    if current_user_id not in user_permissions or target_user_id not in user_permissions[current_user_id]:
        abort(403) # Không có quyền

@app.route('/user/<int:user_id>')
def get_user(user_id):
    current_user_id = request.args.get('user_id', type = int) # Giả sử người dùng hiện tại đăng nhập là 'user_id' trong query
    check_permission(current_user_id, user_id)
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)