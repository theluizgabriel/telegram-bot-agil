import telebot
from supabase import create_client
import os
from dotenv import load_dotenv
from pathlib import Path

# Configuração do .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Configuração simplificada do Supabase
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@bot.message_handler(func=lambda message: True)
def save_message(message):
    try:
        data, count = supabase.table("messages").insert({
            "text": message.text,
            "user_id": str(message.from_user.id)
        }).execute()
        bot.reply_to(message, "✅ Mensagem salva!")
    except Exception as e:
        print("Erro:", e)
        bot.reply_to(message, "❌ Erro ao salvar mensagem")

print("Bot iniciado...")
bot.polling()