from .validation import Check
from flask import jsonify
import string, random

class UserManager:
    def __init__(self):
        self.check = Check()
        self.db = []
        
    def generate_token(self):
        char = string.ascii_letters + string.digits
        return "".join(random.choices(char, k=8))

    def create_account(self, data, username, email, passkey):
        success = self.check.request(data)
        if success:
            return success
        body = {
            "username": username,
            "email": email,
            "password": passkey,
            "access_token": self.generate_token(),
            "session_token": "",
            "address": "",
            "hobby": "",
        }
        for user in self.db:
            if user["email"] == email:
                return jsonify({"message": "email has been used"})
        for user in self.db:
            if user["email"] != email:
                self.db.append(body)
                return jsonify({"message": "account created successfully"}), 201
        self.db.append(body)
        return jsonify({"message": "account created successfully"}), 201

    def log_in(self, data, email, passkey):
        success = self.check.request(data)
        if success:
            return success
        for user in self.db:
            if user["email"] == email and user["password"] == passkey:
                user["session_token"] = self.generate_token()
                body = {"message": "log in successfully", "data": user}
                return jsonify(body), 200
        for user in self.db:
            if user["email"] != email or user["password"] != passkey:
                return jsonify({"message": "account not found"}), 404
        return jsonify({"message": "account not found"}), 404

    def user_list(self, access_token):
        data = []
        for user in self.db:
            body = {"username": user["username"], "email": user["email"]}
            data.append(body)
        for user in self.db:
            if user["access_token"] == access_token:
                return jsonify(
                    {"message": "success", "data": data, "number": len(data)}
                )
        for user in self.db:
            if user["access_token"] != access_token:
                return jsonify({"message": "access denied"}), 401
        return jsonify({"message": "access denied"}), 401

    def update(self, data, access_token, username, email, passkey, address, hobby):
        success = self.check.request(data)
        if success:
            return success
        body = {
            "username": username,
            "email": email,
            "password": passkey,
            "address": address,
            "hobby": hobby,
        }
        for user in self.db:
            if user["access_token"] == access_token:
                user.update(body)
                return jsonify({"message": "data has been updated", "data": user}), 201
        for user in self.db:
            if user["access_token"] != access_token:
                return jsonify({"message": "access denied"}), 401
        return jsonify({"message": "access denied"}), 401

    def log_out(self, session_token):
        for user in self.db:
            if user["session_token"] == session_token:
                user["session_token"] = ""
                return jsonify({"message": "you are logged out"}), 200
        for user in self.db:
            if user["session_token"] != session_token:
                return jsonify({"message": "session has ended"}), 401
        return jsonify({"message": "session has ended"}), 401

    def forgot(self, data, email, passkey):
        success = self.check.request(data)
        if success:
            return success
        token = self.generate_token()
        body = {"password": passkey, "access_token": token, "session_token": token}
        for user in self.db:
            if user["email"] == email:
                user.update(body)
                return (
                    jsonify(
                        {
                            "message": "password has been updated",
                            "access_token": token,
                            "session_token": token,
                        }
                    ),
                    201,
                )
        for user in self.db:
            if user["email"] != email:
                return jsonify({"message": "account not found"}), 404
        return jsonify({"message": "account not found"}), 404

    def delete(self, access_token):
        for user in self.db:
            if user["access_token"] == access_token:
                self.db.remove(user)
                return jsonify({"message": "account has been permanently deleted"}), 200
        for user in self.db:
            if user["access_token"] != access_token:
                self.db.remove(user)
                return jsonify({"message": "access denied"}), 401
        return jsonify({"message": "access denied"}), 401