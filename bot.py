import telebot
from telebot import types

# 🔹 Bot Token
BOT_TOKEN = "7943930374:AAGH_fuU2ycZBL8muVum-9r-9nIjKks-F98"

bot = telebot.TeleBot(BOT_TOKEN)

# 🔹 User Data Store
users = set()  # Set မှာ Start လုပ်တဲ့ Users တွေကို သိမ်းထားမယ်

# 📌 Bot Start Command
@bot.message_handler(commands=['start'])
def start_message(message):
    users.add(message.chat.id)  # User ကို List ထဲထည့်
    bot.reply_to(message, "🎬 မင်္ဂလာပါ! Movies Myanmar Bot မှာ ကြိုဆိုပါတယ်။\n\n🔍 မိမိလိုချင်သော ဇာတ်ကားနာမည်ကို ရိုက်ထည့်ပြီး ရှာဖွေနိုင်ပါသည်။")

# 📌 Movie Search
@bot.message_handler(func=lambda message: True)
def search_movie(message):
    movie_name = message.text.strip()
    if not movie_name:
        bot.reply_to(message, "⚠️ ဇာတ်ကားနာမည်ကို ရိုက်ထည့်ပါ။")
        return

    CHANNEL_ID = "@WinPyaeKyaw0078"  # Channel Username
    
    try:
        forwarded_messages = bot.forward_message(message.chat.id, CHANNEL_ID, message.message_id, disable_notification=True)
        if forwarded_messages:
            bot.reply_to(message, f"✅ '{movie_name}' ကို တွေ့ရှိခဲ့ပါသည်။")
        else:
            bot.reply_to(message, f"❌ '{movie_name}' ကို မတွေ့ရှိပါ။")
    except:
        bot.reply_to(message, "❌ Movie ကို Forward မလုပ်နိုင်ပါ။")

# 📌 /users Command (Admin များအတွက်)
@bot.message_handler(commands=['users'])
def user_count(message):
    bot.reply_to(message, f"👥 Total Users: {len(users)}")

# 📌 /broadcast Command (Admin မှလူတိုင်းကို Message ပို့နိုင်ရန်)
@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    admin_id = 1794465007  # @AceOse Admin ID
    if message.chat.id != admin_id:
        bot.reply_to(message, "❌ Admin မှသာ Broadcast ပို့နိုင်သည်။")
        return

    text = message.text.replace("/broadcast", "").strip()
    if not text:
        bot.reply_to(message, "⚠️ ပို့မည့် Message ကို ရိုက်ထည့်ပါ။")
        return
    
    for user in users:
        try:
            bot.send_message(user, f"📢 {text}")
        except:
            pass  # User Not Found

    bot.reply_to(message, "✅ Broadcast ပို့ပြီးပါပြီ!")

# 🔹 Bot Run
print("🚀 Bot is running...")
bot.polling()
