from telebot import *
bot = TeleBot("5949918299:AAGLF1Uh2FGv3xeB_3sSo0uL5R6bhGKieVA")
large_text = open("large_text.txt", "rb").read()


@bot.message_handler(commands = ["start"])
def say_hello(message):
	bot.send_message(message.chat.id, "Hello "+message.from_user.username+
					 "\nchoose category")

@bot.message_handler(commands = ["inline"])
def inline(message):
	button = types.InlineKeyboardMarkup(row_width=3)
	b1 = types.InlineKeyboardButton("button_1", callback_data="good")
	button.add(b1,b1,b1)
	bot.send_message(message.chat.id, "some text ", reply_markup=button)

@bot.message_handler(content_types=["text"])
def asd(message):

	print(message.text)
	bot.send_message(message.chat.id, message.text)

bot.polling()


class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
	# Class will check whether the user is admin or creator in group or not
	key = 'is_chat_admin'

	@staticmethod
	def check(message: telebot.types.Message):
		return bot.get_chat_member(message.chat.id, message.from_user.id).status in ['administrator', 'creator']


# To register filter, you need to use method add_custom_filter.
bot.add_custom_filter(IsAdmin())


# Now, you can use it in handler.
@bot.message_handler(is_chat_admin=True)
def admin_of_group(message):
	bot.send_message(message.chat.id, 'You are admin of this group!')

