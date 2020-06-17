from text import keymsg, keyapi, repopath, filename, notadmin
import requests
from urllib.parse import quote_plus
from telegram.ext import ConversationHandler
from telegram import ForceReply
from github import Github


def askkey(update, context):
    adminlist = (
        Github()
        .get_repo(repopath)
        .get_contents(filename)
        .decoded_content.decode()
        .strip()
        .split("\n")
    )
    if str(
        update.message.from_user.id
    ) in adminlist or update.message.from_user.username.lower() in [
        i.lower() for i in adminlist
    ]:
        text = keymsg
        update.message.reply_text(text, reply_markup=ForceReply())
        return 0
    else:
        update.message.reply_text(notadmin)
        return ConversationHandler.END


def addkey(update, context):
    text = requests.get(keyapi + quote_plus(update.message.text)).text.strip()
    update.message.reply_text(text)
    return ConversationHandler.END
