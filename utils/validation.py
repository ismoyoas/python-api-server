from flask import jsonify
import re

class Check:
    def __init__(self):
        pass

    def request(self, data):
        for key in data:
            if key == "username" and (
                data["username"].isspace() or "" == data["username"]
            ):
                return jsonify({"message": "username cannot be empty"}), 401
        for key in data:
            if key == "email" and (data["email"].isspace() or "" == data["email"]):
                return jsonify({"message": "email cannot be empty"}), 401
        for key in data:
            if key == "email" and (
                not re.search(re.compile(r"@.*\."), data["email"])
                or " " in data["email"]
            ):
                return jsonify({"message": "invalid email"}), 400
        for key in data:
            if key == "password" and (
                data["password"].isspace() or "" == data["password"]
            ):
                return jsonify({"message": "password cannot be empty"}), 401
        for key in data:
            if key == "new_password" and (
                data["new_password"].isspace() or "" == data["new_password"]
            ):
                return jsonify({"message": "password cannot be empty"}), 401
        for key in data:
            if key == "password" and len(data["password"]) <= 5:
                return (
                    jsonify({"message": "minimum password length is 8 characters"}),
                    401,
                )
        for key in data:
            if key == "new_password" and len(data["new_password"]) <= 5:
                return (
                    jsonify({"message": "minimum password length is 8 characters"}),
                    401,
                )
        return None
