from flask import request, jsonify
from auth import verify_token
from supabase_client import (
    supabase_select,
    supabase_insert,
    supabase_update,
    supabase_delete,
)


def required_fields(data, fields):
    for field in fields:
        if field not in data:
            return False
    return True


def get_posts():
    limit = request.args.get("limit", default=10, type=int)
    offset = request.args.get("offset", default=0, type=int)

    query_params = {"select": "*", "limit": limit, "offset": offset}
    posts = supabase_select("posts", query_params)
    return jsonify(posts)


@verify_token
def create_post():
    fields = [
        "titulo",
        "time_a",
        "time_b",
        "data_jogo",
        "horario",
        "campeonato",
        "local",
    ]
    data = request.get_json()

    if not required_fields(data, fields):
        return jsonify({"error": "Campos obrigatórios ausentes"}), 400

    data = request.get_json()
    novo_post = supabase_insert("posts", data)
    return jsonify(novo_post)


@verify_token
def update_post(id):
    data = request.get_json()
    post_atualizado = supabase_update("posts", id, data)
    return jsonify(post_atualizado)


@verify_token
def delete_post(id):
    resultado = supabase_delete("posts", id)
    return jsonify(resultado)
