import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}


def supabase_select(table, query_params=None):
    if query_params:
        query_string = "&".join(
            [f"{key}={value}" for key, value in query_params.items()]
        )
        url = f"{SUPABASE_URL}/rest/v1/{table}?{query_string}"
    else:
        url = f"{SUPABASE_URL}/rest/v1/{table}?select=*"

    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None


def supabase_insert(table, data):
    url = f"{SUPABASE_URL}/rest/v1/{table}"

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None


def supabase_update(table, id, data):
    url = f"{SUPABASE_URL}/rest/v1/{table}?id=eq.{id}"

    try:
        response = requests.patch(url, headers=headers, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None


def supabase_delete(table, id):
    url = f"{SUPABASE_URL}/rest/v1/{table}?id=eq.{id}"
    try:
        response = requests.delete(url, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None
