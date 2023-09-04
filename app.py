import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
load_dotenv()


WHITELIST = ["daavidev"]

def is_authorized(update):

    username = update.message.from_user.username
    return username in WHITELIST


def NO_PERM_MESSAGE(update):
    username = update.message.from_user.username
    if username is None:
        return 'Você não tem um username definido! Para definir um username no Telegram, basta acessar as configurações do seu perfil e clicar em "Editar" ao lado do campo "Nome de Usuário", inserindo o nome que deseja utilizar. Após definir seu username, entre em contato com um administrador para autorizar o seu acesso ao bot'
    else:
        return f"""Você não tem permissão para utilizar esse bot! Contate um administrador
Peça autorização enviando seu username: {username}

"""

async def responderMensagem(context, chat_id, resposta):
    await context.bot.send_message(chat_id=chat_id, text=resposta)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_authorized(update):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Olá!

    Eu sou o assistente de Infraestrutura. Fui desenvolvido pelo Davi Antonaji. Se você tiver alguma dúvida, não hesite em contatar o meu criador. Estamos sempre disponíveis para ajudá-lo!

    Utilize /commands para ver o que posso fazer!
    """)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=NO_PERM_MESSAGE(update))


async def reiniciar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_authorized(update):
        subprocess.run(['shutdown /r /t 10'])
        responderMensagem(context, update.effective_chat.id, "Reiniciando servidor em 10 segundos...")
    else:
        responderMensagem(context, update.effective_chat.id, NO_PERM_MESSAGE(update))

app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("reiniciar", reiniciar))

app.run_polling()