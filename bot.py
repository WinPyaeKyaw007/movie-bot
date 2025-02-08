import telebot

BOT_TOKEN = "7943930374:AAGH_fuU2ycZBL8muVum-9r-9nIjKks-F98"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🎬 မင်္ဂလာပါ! Movies Myanmar Bot မှာ ကြိုဆိုပါတယ်။\n\n🔍 မိမိလိုချင်သော ဇာတ်ကားနာမည်ကို ရိုက်ထည့်ပြီး ရှာဖွေနိုင်ပါသည်။")

bot.polling()
