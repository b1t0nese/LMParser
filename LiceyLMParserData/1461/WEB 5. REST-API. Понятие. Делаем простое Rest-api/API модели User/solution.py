from flask import Blueprint, jsonify, request
from . import db_session
from .user import User
from datetime import datetime

users_api = Blueprint(
    "users_api", "users_api", template_folder="templates", url_prefix="api"
)


@users_api.route("/users", methods=["GET"])
def get_all_users():
    users_list = [
        {
            "id": user.id,
            "surname": user.surname,
            "name": user.name,
            "age": user.age,
            "position": user.position,
            "speciality": user.speciality,
            "address": user.address,
            "email": user.email,
            "modified_date": (
                user.modified_date.isoformat() if user.modified_date else None
            ),
        }
        for user in db_session.query(User).all()
    ]
    return jsonify({"users": users_list, "count": len(users_list)}), 200


@users_api.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = db_session.query(User).filter(User.id == user_id).first()
    if user is None:
        return (
            jsonify({"error": "Not found", "message": "Пользователь не найден"}),
            404,
        )

    return (
        jsonify(
            {
                "status": "success",
                "user": {
                    "id": user.id,
                    "surname": user.surname,
                    "name": user.name,
                    "age": user.age,
                    "position": user.position,
                    "speciality": user.speciality,
                    "address": user.address,
                    "email": user.email,
                    "modified_date": (
                        user.modified_date.isoformat() if user.modified_date else None
                    ),
                },
            }
        ),
        200,
    )


@users_api.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return (
            jsonify({"error": "Bad request", "message": "Отсутствуют данные запроса"}),
            400,
        )

    if [
        field for field in ["surname", "name", "email", "password"] if field not in data
    ]:
        return (
            jsonify(
                {"error": "Bad request", "message": f"Отсутствуют обязательные поля"}
            ),
            400,
        )

    existing_user = db_session.query(User).filter(User.email == data["email"]).first()
    if existing_user:
        return (
            jsonify(
                {
                    "error": "Bad request",
                    "message": f"Пользователь с таким email уже существует",
                }
            ),
            400,
        )

    user = User(
        surname=str(data["surname"]),
        name=str(data["name"]),
        age=int(data["age"]) if "age" in data and data["age"] else None,
        position=str(data["position"]) if "position" in data else None,
        speciality=str(data["speciality"]) if "speciality" in data else None,
        address=str(data["address"]) if "address" in data else None,
        email=str(data["email"]),
        hashed_password=str(data["password"]),
        modified_date=datetime.now(),
    )

    db_session.add(user)
    db_session.commit()

    return (
        jsonify(
            {
                "status": "success",
                "message": "Пользователь успешно добавлен",
            }
        ),
        201,
    )


@users_api.route("/users/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    user = db_session.query(User).filter(User.id == user_id).first()
    if user is None:
        return (
            jsonify({"error": "Not found", "message": "Пользователь не найден"}),
            404,
        )
    data = request.get_json()
    if not data:
        return (
            jsonify({"error": "Bad request", "message": "Отсутствуют данные запроса"}),
            400,
        )

    user.surname = data.get("surname")
    user.name = data.get("name")
    try:
        user.age = data.get("age")
    except (ValueError, TypeError):
        return (
            jsonify({"error": "Bad request", "message": "Поле age должно быть числом"}),
            400,
        )
    user.position = data.get("position")
    user.speciality = data.get("speciality")
    user.address = data.get("address")
    if "email" in data:
        existing_user = (
            db_session.query(User)
            .filter(User.email == data["email"], User.id != user_id)
            .first()
        )
        if existing_user:
            return (
                jsonify(
                    {
                        "error": "Bad request",
                        "message": "Пользователь с таким email уже существует",
                    }
                ),
                400,
            )
        user.email = data.get("email")
    user.modified_date = datetime.now()
    db_session.commit()

    return (
        jsonify(
            {
                "status": "success",
                "message": "Пользователь успешно обновлен",
                "user": {
                    "id": user.id,
                    "surname": user.surname,
                    "name": user.name,
                    "age": user.age,
                    "position": user.position,
                    "speciality": user.speciality,
                    "address": user.address,
                    "email": user.email,
                    "modified_date": (
                        user.modified_date.isoformat() if user.modified_date else None
                    ),
                },
            }
        ),
        200,
    )


@users_api.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = db_session.query(User).filter(User.id == user_id).first()
    if user is None:
        return (
            jsonify({"error": "Not found", "message": "Пользователь не найден"}),
            404,
        )

    db_session.delete(user)
    db_session.commit()

    return (
        jsonify(
            {
                "status": "success",
                "message": f"Пользователь успешно удален",
            }
        ),
        200,
    )