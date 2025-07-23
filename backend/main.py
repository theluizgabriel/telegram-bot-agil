from fastapi import FastAPI
from supabase import create_client, Client
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

app = FastAPI()

# Configurar CORS (para o frontend Angular)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexão com o Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# Rota para salvar mensagens (usada pelo bot)
@app.post("/messages")
async def save_message(text: str, user_id: str):
    data = supabase.table("messages").insert({
        "text": text,
        "user_id": user_id
    }).execute()
    return {"status": "Message saved!", "data": data}

# Rota para listar mensagens (usada pelo frontend)
@app.get("/messages")
async def get_messages():
    data = supabase.table("messages").select("*").execute()
    return {"messages": data.data}