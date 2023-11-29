import telebot

bot = telebot.TeleBot('6912543793:AAEVlMUWM7a3YrRm8GtQ1bcUi-89BOVuqIg')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Желаете получить рецепт?', parse_mode='Markdown')


@bot.message_handler(commands=['recipe'])
def main(message):
    bot.send_message(message.chat.id,
                     'огурцы по корейски - 1. Как заготовить огурцы по-корейски на зиму в банках? Огурцы обработать щеточкой, чтобы не было колючек, срезать кончики и вымыть. Порезать огурцы, 2. На специальной терке или с помощью комбайна с насадкой для корейской моркови измельчить вымытую морковь. Всыпать в нее пару щепоток соли, 3. Маринад для овощей приготовить следующим образом: в отдельной посудине смешать соль, сахар, влить по 100 мл уксуса и растительного масла. Всё перемешать. Готово! Приятного аппетита!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['motivation'])
def main(message):
    bot.send_message(message.chat.id,
                     'Я хочу быть похожим на гусеницу. Много есть. Спать некоторое время. Проснуться красивым. - Джейсон Стетхем.',
                     parse_mode='Markdown')


bot.infinity_polling()
