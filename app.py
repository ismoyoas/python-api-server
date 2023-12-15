from flask import Flask, request
from utils.base import UserManager

app = Flask(__name__)
user = UserManager()

# CREATE A NEW ACCOUNT
@app.route("/users/signup", methods=["POST"])
def create_account():
    print(f"[POST] http://127.0.0.1:5000/users/signup {'-'*80}")
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    passkey = data["password"]
    success = user.create_account(data, username, email.lower(), passkey)
    if success:
        return success

# LOGIN & SHOW ACCOUNT DATA
@app.route("/users/signin", methods=["POST"])
def log_in_and_show_data():
    print(f"[POST] http://127.0.0.1:5000/users/signin {'-'*80}")
    data = request.get_json()
    email = data["email"]
    passkey = data["password"]
    success = user.log_in(data, email.lower(), passkey)
    if success:
        return success

# SHOW A LIST OF USERS
@app.route("/users/<string:access_token>", methods=["GET"])
def user_list(access_token):
    print(f"[GET] http://127.0.0.1:5000/users/{access_token} {'-'*80}")
    success = user.user_list(access_token)
    if success:
        return success

# UPDATE DATA
@app.route("/users/<string:access_token>", methods=["PUT"])
def update_data(access_token):
    print(f"[PUT] http://127.0.0.1:5000/users/{access_token} {'-'*80}")
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    passkey = data["password"]
    address = data["address"]
    hobby = data["hobby"]
    success = user.update(
        data, access_token, username, email.lower(), passkey, address, hobby
    )
    if success:
        return success

# OUT OF SESSION
@app.route("/users/<string:session_token>", methods=["PATCH"])
def log_out_from_account(session_token):
    print(f"[PATCH] http://127.0.0.1:5000/users/{session_token} {'-'*80}")
    success = user.log_out(session_token)
    if success:
        return success

# FORGOT THE PASSWORD
@app.route("/users/forgot_password", methods=["POST"])
def forgot_passkey():
    print(f"[POST] http://127.0.0.1:5000/users/forgot_password {'-'*80}")
    data = request.get_json()
    email = data["email"]
    passkey = data["new_password"]
    success = user.forgot(data, email.lower(), passkey)
    if success:
        return success

# DELETE ACCOUNT
@app.route("/users/<string:access_token>", methods=["DELETE"])
def delete_account(access_token):
    print(f"[DELETE] http://127.0.0.1:5000/users/{access_token} {'-'*80}")
    success = user.delete(access_token)
    if success:
        return success

if __name__ == "__main__":
    app.run(debug=True)