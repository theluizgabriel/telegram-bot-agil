from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
import os
from dotenv import load_dotenv
from pathlib import Path

# Caminho absoluto para o .env na raiz do projeto
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)  # Carrega o .env

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # URL do Angular
    allow_methods=["*"],
    allow_headers=["*"]
)

# Configuração do Supabase
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Rota para salvar mensagens (usada pelo bot)
@app.post("/messages")
async def save_message(text: str, user_id: str):
    data = supabase.table("messages").insert({
        "text": text,
        "user_id": user_id
    }).execute()
    return {"status": "Mensagem salva!", "data": data}

# Rota para listar mensagens (usada pelo frontend)
@app.get("/messages")
async def get_messages():
    data = supabase.table("messages").select("*").execute()
    return {"messages": data.data}