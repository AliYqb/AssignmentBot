import random
import telebot

bot = telebot.TeleBot("2019327355:AAF9JCQPiBsOQKrEivcNfGlAoFk5nWKQ0jc")

@bot.message_handler(commands=['Start', 'start', 'شروع'])
def wellcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f'{first_name} خوش اومدی')

@bot.message_handler(commands=['Game', 'game', 'بازی'])
def play_game(message):
    bot.reply_to(message, 'بازی حدس عدد')
    bot.send_message(message.chat.id, 'یک عدد بین ۰ تا ۱۰۰۰ بگو')
    game(random.randint(0, 1000))

def game(answer_number):
    def loop_game():
        @bot.message_handler(func=lambda message: True)
        def check_game(message):
            if int(message.text) > answer_number:
                bot.send_message(message.chat.id, 'کمترش کن')
                loop_game()
            elif int(message.text) < answer_number:
                bot.send_message(message.chat.id, 'بیشترش کن')
                loop_game()
            elif int(message.text) == answer_number:
                bot.send_message(message.chat.id, 'ماشالااااا خودشه\nپیداش کردی')
    loop_game()
                    
bot.polling()
