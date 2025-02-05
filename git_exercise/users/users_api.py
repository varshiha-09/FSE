from flask import Blueprint, abort, jsonify, request
from git_exercise.users.users_gateway import UsersGateway


def users_api(users_gateway: UsersGateway) -> Blueprint:
    api = Blueprint("users_api", __name__)

    @api.route("/users")
    def list_all():
        return jsonify(users_gateway.list())

    @api.route("/users/<int:user_id>")
    def find(user_id: int):
        user = users_gateway.find(user_id)
        if user is None:
            abort(404)
        return jsonify(user)

    @api.route("/users", methods=["POST"])
    def create_user():
        data = request.get_json()
        if not data or "name" not in data or "email" not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        new_user_id = users_gateway.add_user(data["name"], data["email"])
        return jsonify({"id": new_user_id}), 201

    @api.route("/users/<int:user_id>", methods=["PUT"])
    def update_user(user_id):
        data = request.get_json()
        if not data or "name" not in data or "email" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        user = users_gateway.find(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        updated_user = users_gateway.update_user(user_id, data["name"], data["email"])
        return jsonify(updated_user), 200

    return api  
