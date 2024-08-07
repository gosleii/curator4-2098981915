import telebot

bot = telebot.TeleBot('7398342880:AAG5aFIEZL-QT9upHEahO0Z1_7eXtt8usK8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Выбери в меню что хочешь узнать или найти ))', parse_mode='Markdown')


@bot.message_handler(commands=['broadcast'])
def video(message):
    bot.send_message(message.chat.id,
                     '[Лови ссылку для просмотра матчей всего мирового тенниса](https://vk.com/tennisprimesport?from=search)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['rankings_atp'])
def rankings(message):
    bot.send_message(message.chat.id,
                     '[Рейтинг ATP прямо сейчас](https://news.sportbox.ru/Vidy_sporta/Tennis/ATP/stats/reiting_1)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['new_fact'])
def fact(message):
    bot.send_message(message.chat.id,
                     'Первый теннисный мяч был вырезан из дерева, потом их стали делать из кожи. Наполняли кожаные теннисные мячи высушенными внутренностями животных, шерстью или опилками. Удар таким объектом был очень травмоопасен, даже смертелен и обладал способностью отскакивать лишь от твердой поверхности. Поэтому игра велась в основном в каменных залах.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['grand_slam'])
def slam(message):
    bot.send_message(message.chat.id, 'Карлос Алькарас', parse_mode='Markdown')


bot.infinity_polling()