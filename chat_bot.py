import os
import time

import telebot
from telebot import types

from dotenv import load_dotenv


def configure():
    load_dotenv()


configure()
chat_bot = telebot.TeleBot(f"{os.getenv('TELEBOT_TOKEN')}")


@chat_bot.message_handler(commands=["start"])
def select_language(message):
    markup = types.ReplyKeyboardMarkup()
    english_lng = types.KeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Continue in English")
    ukrainian_lng = types.KeyboardButton("󠁧󠁢󠁥󠁮🇺🇦󠁿 Продовжити спілкування українською")
    markup.row(english_lng, ukrainian_lng)
    chat_bot.send_message(message.chat.id, "Choose language / Оберіть мову спілкування", parse_mode="html",
                          reply_markup=markup)


@chat_bot.message_handler(commands=["index_en"])
def eng_start(message):
    markup = types.ReplyKeyboardMarkup()
    en_button_1 = types.KeyboardButton("📕👀 Quick navigate guide")
    en_button_2 = types.KeyboardButton("🤔 What is MoonAudioProduction?")
    en_button_3 = types.KeyboardButton("💼 View Our Portfolio")
    en_button_4 = types.KeyboardButton("📝 Complete phrase list")
    markup.row(en_button_1, en_button_2, en_button_3)
    markup.row(en_button_4)
    greeting_message = f"Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. " \
                       f"MoonAudioProduction bot is glad to welcome you! " \
                       f"Our custom sound effects and music make your projects more colorful!"
    chat_bot.send_message(message.chat.id, greeting_message, parse_mode="html", reply_markup=markup)
    file = open("static/images/home_moon.png", "rb")
    chat_bot.send_photo(message.chat.id, file, reply_markup=markup)
    second_message = "How can I help You?"
    chat_bot.send_message(message.chat.id, second_message, parse_mode="html")


@chat_bot.message_handler(commands=["index_ua"])
def ua_start(message):
    markup = types.ReplyKeyboardMarkup()
    ua_button_1 = types.KeyboardButton("📕👀 Короткий посібник користувача")
    ua_button_2 = types.KeyboardButton("🤔 Що таке MoonAudioProduction?")
    ua_button_3 = types.KeyboardButton("💼 Переглянути Портфоліо")
    ua_button_4 = types.KeyboardButton("📝 Повний список команд доступних українською")
    markup.row(ua_button_1, ua_button_2, ua_button_3)
    markup.row(ua_button_4)
    greeting_message = f"Привіт, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. " \
                       f"MoonAudioProduction чат-бот радий вітати тебе! " \
                       f"Наші авторські звукові ефекти та оркестрова музика забезпечать якісно належне акустичне " \
                       f"оформлення Вашого проєкту що вигідно вирізнятиме його з-поміж інших!"
    chat_bot.send_message(message.chat.id, greeting_message, parse_mode="html", reply_markup=markup)
    file = open("static/images/home_moon.png", "rb")
    chat_bot.send_photo(message.chat.id, file, reply_markup=markup)
    second_message = "Чим я можу Вам допомогти?"
    chat_bot.send_message(message.chat.id, second_message, parse_mode="html")


@chat_bot.message_handler(commands=["info_en"])
def author_info(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    contact_author = types.KeyboardButton("📞 Contact the Author")
    full_name = types.KeyboardButton("MoonAudioProduction YouTube chanel")
    back_home = types.KeyboardButton("↩️ Back to Main menu")
    markup.add(contact_author, full_name, back_home)
    chat_bot.send_message(message.chat.id, "Make your choice", reply_markup=markup)


@chat_bot.message_handler(commands=["info_ua"])
def author_info(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    contact_author = types.KeyboardButton("📞 Звʼязок з автором")
    full_name = types.KeyboardButton("MoonAudioProduction YouTube канал")
    back_home = types.KeyboardButton("↩️ Повернутися до головного меню")
    markup.add(contact_author, full_name, back_home)
    chat_bot.send_message(message.chat.id, "Будь-ласка, оберіть категорію", reply_markup=markup)


@chat_bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Delete image / Видалити зображення", callback_data="delete")
    markup.row(button)
    chat_bot.reply_to(message, "Wow! Your picture looks awesome! 😄\nВау! Це фото просто супер!! 😄",
                      reply_markup=markup)


@chat_bot.message_handler(content_types=["sticker"])
def get_user_photo(message):
    chat_bot.reply_to(message, "Wow! Your sticker looks good 😄\nВау! Твій стікер суперовий!! 😄")


@chat_bot.message_handler(
    func=lambda message: message.text in ["Cartoon Sounds", "Cartoon Sound", "Cartoon sounds", "Cartoon sound",
                                          "Cartoon", "cartoon"]
)
def cartoon_page(message):
    cartoon_text = "<b>Funny high quality Cartoon sounds</b>"
    cartoon_image = open("static/images/sound_effects/cartoon.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Cartoon Sounds", url="https://audiojungle.net/collections/7794721-cartoon-sound"))
    chat_bot.send_photo(message.chat.id, cartoon_image, caption=cartoon_text, parse_mode="html", reply_markup=markup)


@chat_bot.message_handler(
    func=lambda message: message.text in ["Звуки до Мультфільмів", "Мультфільми", "мультфільми", "мультфільм",
                                          "Мультик", "мультик", "Мультяшні звуки", "мультяшні звуки", "Мультяшні",
                                          "мультяшні"]
)
def cartoon_page(message):
    cartoon_text = "<b>Кумедні звуки до Мультфільмів</b>"
    cartoon_image = open("static/images/sound_effects/cartoon.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Звуки до Мультфільмів",
                                   url="https://audiojungle.net/collections/7794721-cartoon-sound"))
    chat_bot.send_photo(message.chat.id, cartoon_image, caption=cartoon_text, parse_mode="html", reply_markup=markup)


@chat_bot.message_handler(
    func=lambda message: message.text in ["Domestic Sounds", "Domestic sounds", "Domestic Sound", "Domestic sound",
                                          "Domestic", "domestic"]
)
def domestic_page(message):
    domestic_text = "<b>Natural high quality Domestic sounds</b>"
    domestic_image = open("static/images/sound_effects/domestic.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Domestic Sounds", url="https://audiojungle.net/collections/7794746-domestic-sounds"
        )
    )
    chat_bot.send_photo(message.chat.id, domestic_image, caption=domestic_text, parse_mode="html", reply_markup=markup)


@chat_bot.message_handler(
    func=lambda message: message.text in ["Побутові Звуки", "Побутові звуки", "побутові звуки", "Побутові", "побутові",
                                          "Побут", "побут"]
)
def domestic_page(message):
    domestic_text = "<b>Реалістичні високоякісні Побутові звуки</b>"
    domestic_image = open("static/images/sound_effects/domestic.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Побутові Звуки", url="https://audiojungle.net/collections/7794746-domestic-sounds"
        )
    )
    chat_bot.send_photo(message.chat.id, domestic_image, caption=domestic_text, parse_mode="html", reply_markup=markup)


@chat_bot.message_handler(
    func=lambda message: message.text in ["Futuristic Sounds", "Futuristic Sound", "Futuristic sounds",
                                          "Futuristic sound", "Futuristic", "futuristic", "Sci-Fi Sounds",
                                          "Sci-Fi sounds", "Sci-Fi", "Sci-fi", "sci-fi", "Scifi"]
)
def futuristic_page(message):
    futuristic_text = "<b>Unreal high quality Futuristic sounds</b>"
    futuristic_image = open("static/images/sound_effects/futuristic.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Futuristic Sounds", url="https://audiojungle.net/collections/8554656-futuristic-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, futuristic_image, caption=futuristic_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Футуристичні звуки", "футуристичні звуки", "Футуристичні", "футуристичні"]
)
def futuristic_page(message):
    futuristic_text = "<b>Таємничі та неземні високоякісні Футуристичні звуки</b>"
    futuristic_image = open("static/images/sound_effects/futuristic.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Футуристичні звуки", url="https://audiojungle.net/collections/8554656-futuristic-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, futuristic_image, caption=futuristic_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Game Sounds", "Game sounds", "Game Sound", "Game sound", "Game", "game"]
)
def game_page(message):
    game_text = "<b>Powerful and unique high quality Game sounds</b>"
    game_image = open("static/images/sound_effects/game.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Game Sounds", url="https://audiojungle.net/collections/8107721-game-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, game_image, caption=game_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Ігрові звуки", "ігрові звуки", "Ігрові", "ігрові", "Гра", "гра"]
)
def game_page(message):
    game_text = "<b>Потужні та яскраві високоякісні Ігрові звуки</b>"
    game_image = open("static/images/sound_effects/game.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Ігрові звуки", url="https://audiojungle.net/collections/8107721-game-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, game_image, caption=game_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Human Sounds", "Human sounds", "human sounds", "Human Sound", "Human",
                                          "human", "Human sound", "Baby", "baby", "Babies"]
)
def human_page(message):
    human_text = "<b>This collection includes unique sound effects that can be useful for proper acoustic design " \
                   "of human sounds</b>"
    human_image = open("static/images/sound_effects/human.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Human Sounds", url="https://audiojungle.net/collections/7794758-human-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, human_image, caption=human_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Людські звуки", "людські звуки", "Людина", "людина",
                                          "Людські", "людські"]
)
def human_page(message):
    human_text = "<b>Дана колекція включає в себе реальні звуки що притаманні поведінці та способу життя людини</b>"
    human_image = open("static/images/sound_effects/human.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Людські звуки", url="https://audiojungle.net/collections/7794758-human-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, human_image, caption=human_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Industrial Sounds", "Industrial sounds", "Industrial Sound",
                                          "Industrial sound", "industrial sounds", "industrial sound", "Industrial",
                                          "industrial", "Industry", "industry"]
)
def industrial_page(message):
    industrial_text = "<b>This collection includes unique sound effects that can be useful for proper acoustic design " \
                   "of your videos, films, cartoons or other media projects</b>"
    industrial_image = open("static/images/sound_effects/industrial.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Industrial Sounds", url="https://audiojungle.net/collections/8107747-industrial-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, industrial_image, caption=industrial_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Промислові Звуки", "Промислові", "промислові",
                                          "промислові звуки", "індустріальні", "Індустріальні"]
)
def industrial_page(message):
    industrial_text = "<b>Дана колекція може бути корисною в питанні акустичного оформлення ваших відео, фільмів, " \
                      "або інших медійних проєктів</b>"
    industrial_image = open("static/images/sound_effects/industrial.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Промислові звуки", url="https://audiojungle.net/collections/8107747-industrial-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, industrial_image, caption=industrial_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Interface Sounds", "Interface sounds", "Interface Sound", "Interface sound",
                                          "interface sounds", "interface sound", "Interface", "interface", "UI", "ui"]
)
def interface_page(message):
    interface_text = "<b>This collection includes unique sound effects that can be useful in applications, " \
                     "video-games, etc.</b>"
    interface_image = open("static/images/sound_effects/interface.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Interface Sounds", url="https://audiojungle.net/collections/7794768-interface-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, interface_image, caption=interface_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Звуки інтерфейсу", "звуки інтерфейсу", "Інтерфейс", "інтерфейс", "юай"]
)
def interface_page(message):
    interface_text = "<b>Дана колекція стане в нагоді в питанні акустичного оформлення відеоігр, додатків, тощо</b>"
    interface_image = open("static/images/sound_effects/interface.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Звуки інтерфейсу", url="https://audiojungle.net/collections/7794768-interface-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, interface_image, caption=interface_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Nature Sounds", "Nature sounds", "Nature Sound", "nature sounds",
                                          "nature sound", "Nature", "nature"]
)
def nature_page(message):
    nature_text = "<b>This collection includes exclusively realistic sound effects that can be useful in videos, " \
           "films or video-games</b>"
    nature_image = open("static/images/sound_effects/nature.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Nature Sounds", url="https://audiojungle.net/collections/7794793-nature-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, nature_image, caption=nature_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Природні звуки", "природні звуки", "Природа", "природа", "Звуки природи",
                                          "звуки природи", "Природні", "природні"]
)
def nature_page(message):
    nature_text = "<b>Дана колекція містить виключно реальні звуки природи, що будуть корисні в рамках ваших творчих " \
                  "проєктів</b>"
    nature_image = open("static/images/sound_effects/nature.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Природні звуки", url="https://audiojungle.net/collections/7794793-nature-sounds"
        )
    )
    chat_bot.send_photo(
        message.chat.id, nature_image, caption=nature_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Transitions & Movement", "Transitions & movement", "transitions & movement",
                                          "transitions", "transition", "Movement", "Movements", "movement", "whoosh",
                                          "Whoosh", "whooshes", "Whooshes", "Swhoosh", "swhoosh", "T&M"]
)
def whooshes_page(message):
    whooshes_text = "<b>This collection contains a variety of sound effects that perfectly complement your project.</b>"
    whooshes_image = open("static/images/sound_effects/whoosh.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Transitions & Movement", url="https://audiojungle.net/collections/7794731-transitions-movement"
        )
    )
    chat_bot.send_photo(
        message.chat.id, whooshes_image, caption=whooshes_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Транзішнс", "транзішнс", "транзішн", "транзішн", "Вуш", "вуш", "Вушаки",
                                          "вушаки"]
)
def whooshes_page(message):
    whooshes_text = "<b>Дана колекція містить величезну кількість разноманітних звукових ефектів переходу</b>"
    whooshes_image = open("static/images/sound_effects/whoosh.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Транзішнс", url="https://audiojungle.net/collections/7794731-transitions-movement"
        )
    )
    chat_bot.send_photo(
        message.chat.id, whooshes_image, caption=whooshes_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Urban Sounds", "Urban sounds", "urban sounds", "Urban", "urban", "City",
                                          "city"]
)
def urban_page(message):
    urban_text = "<b>This collection includes unique sound effects that are useful for proper acoustic design " \
           "of urban sounds</b>"
    urban_image = open("static/images/sound_effects/urban.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Urban Sounds", url="https://audiojungle.net/collections/7794785-urban-sounds"
        )
    )
    chat_bot.send_photo(message.chat.id, urban_image, caption=urban_text, parse_mode="html", reply_markup=markup)


@chat_bot.message_handler(
    func=lambda message: message.text in ["Звуки міста", "звуки міста", "Міські звуки", "міські звуки", "Урбан",
                                          "урбан"]
)
def urban_page(message):
    urban_text = "<b>Дана колекція містить реальні звукові ефекти що записані у самому сердці великого міста</b>"
    urban_image = open("static/images/sound_effects/urban.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Звуки міста", url="https://audiojungle.net/collections/7794785-urban-sounds"
        )
    )
    chat_bot.send_photo(message.chat.id, urban_image, caption=urban_text, parse_mode="html", reply_markup=markup)


@chat_bot.message_handler(
    func=lambda message: message.text in ["🎦 Cinematic Music", "Cinematic Music", "Cinematic music", "cinematic music",
                                          "cinematic", "Cinematic", "Cinema", "cinema", "Cine", "cine", "Film", "film",
                                          "Movie", "movie", "Movies", "movies"]
)
def cinematic_music_page(message):
    urban_text = "<b>This collection includes unique orchestral music composed, mixed and mastered" \
                 " by Ievgenii Balabanov. Presented compositions can useful for proper acoustic design of films " \
                 "and video games</b>"
    urban_image = open("static/images/cinematic_music/cinema.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Epic Cinematic Music", url="https://audiojungle.net/collections/8574718-epic-cinematic-music"
        )
    )
    chat_bot.send_photo(message.chat.id, urban_image, caption=urban_text, parse_mode="html", reply_markup=markup)


@chat_bot.message_handler(
    func=lambda message: message.text in ["🎦 Музика до фільмів", "кіно", "до фильмів", "до кіно", "Фільм", "фільм",
                                          "Фільми", "фільми", "Кінофільм", "кінофільм", "Музика до фільмів",
                                          "музика до фільмів"]
)
def cinematic_music_page(message):
    urban_text = "<b>Дана колекція містить авторські оркестрові композиції, що створені, аранжовані та зведені " \
                 "Євгенієм Балабановим. Наведені композиції стануть яскравим доповненням ваших творчих проєктів</b>"
    urban_image = open("static/images/cinematic_music/cinema.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "🎦 Музика до фільмів", url="https://audiojungle.net/collections/8574718-epic-cinematic-music"
        )
    )
    chat_bot.send_photo(message.chat.id, urban_image, caption=urban_text, parse_mode="html", reply_markup=markup)


@chat_bot.message_handler(
    func=lambda message: message.text in ["🎅 Christmas Music", "Christmas Music", "christmas music", "Christmas",
                                          "christmas", "Xmas", "XMAS", "xmas"]
)
def christmas_music_page(message):
    christmas_text = "<b>This collection includes unique orchestral Christmas music composed, mixed and mastered" \
                 " by Ievgenii Balabanov. Presented compositions can be useful for proper acoustic design " \
                     "of your Christmas projects</b>"
    christmas_image = open("static/images/christmas_music/christmas.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Christmas Music", url="https://audiojungle.net/collections/8574751-christmas-music"
        )
    )
    chat_bot.send_photo(
        message.chat.id, christmas_image, caption=christmas_text, parse_mode="html", reply_markup=markup
    )

    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Sure, why not?", callback_data="Sure, why not?"
        ),
        types.InlineKeyboardButton(
            "No, I’m not interested", callback_data="No, I’m not interested"
        )
    )
    chat_bot.send_message(message.chat.id, "Can I ask you something? 👀",
                          reply_markup=markup)


@chat_bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "Sure, why not?":
        sticker = open("static/stickers/great.tgs", 'rb')
        chat_bot.send_sticker(callback.message.chat.id, sticker)
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton(
                "Carol of the Bells",
                url="https://audiojungle.net/item/carol-of-the-bells/25166035"
            ),
            types.InlineKeyboardButton(
                "Nah, maybe next time...", callback_data="Nah, maybe next time..."
            )
        )
        chat_bot.send_message(callback.message.chat.id, "Great. I’m glad to hear it! I see you’re looking for Christmas"
                                                        " music. Might you be interested in my favorite song?",
                              reply_markup=markup)

    elif callback.data == "No, I’m not interested":
        chat_bot.send_message(callback.message.chat.id, "Sorry about that!")

    elif callback.data == "Nah, maybe next time...":
        sticker = open("static/stickers/no_problem.tgs", 'rb')
        chat_bot.send_sticker(callback.message.chat.id, sticker)
        chat_bot.send_message(callback.message.chat.id, "It's a pity, but no problems")


@chat_bot.message_handler(
    func=lambda message: message.text in ["🎅 Різдвяна музика", "Різдвяна музыка", "різдвяна музика", "Різдвяна",
                                          "різдвяна", "Різдво", "різдво"]
)
def christmas_music_page(message):
    christmas_text = "<b>Дана колекція містить авторські різдвяні оркестрові композиції, що створені, аранжовані та " \
                     "зведені Євгенієм Балабановим. Наведені композиції стануть яскравим доповненням ваших святкових" \
                     "проєктів</b>"
    christmas_image = open("static/images/christmas_music/christmas.png", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "🎅 Різдвяна музика", url="https://audiojungle.net/collections/8574751-christmas-music"
        )
    )
    chat_bot.send_photo(
        message.chat.id, christmas_image, caption=christmas_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["©️ Logos", "Logos", "logos", "Logo", "logo"]
)
def logo_page(message):
    logo_text = "<b>This collection includes unique mainly orchestral Logos composed, mixed and mastered " \
                "by Ievgenii Balabanov. Presented logos can be useful for proper acoustic design of your " \
                "social media accounts, or any kinds of your media projects.</b>"
    logo_image = open("static/images/logos/logo.jpeg", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "©️ Logos", url="https://audiojungle.net/collections/11369762-logos-idents"
        )
    )
    chat_bot.send_photo(
        message.chat.id, logo_image, caption=logo_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["©️Логотипи", "лого", "Лого", "Логотипи", "логотипи", "логотип", "Логотип"]
)
def logo_page(message):
    logo_text = "<b>Дана колекція містить авторські, переважно оркестрові логотипи, що створені, аранжовані та " \
                     "зведені Євгенієм Балабановим. Дані лого стануть справжньою прикрасою та візитною карткою ваших " \
                "соціальних мереж або акаунтів</b>"
    logo_image = open("static/images/logos/logo.jpeg", "rb")
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "©️Логотипи", url="https://audiojungle.net/collections/11369762-logos-idents"
        )
    )
    chat_bot.send_photo(
        message.chat.id, logo_image, caption=logo_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["View Whole Portfolio", "Portfolio", "portfolio", "View Portfolio", "items",
                                          "Items", "All Items", "all items", "All", "all"]
)
def portfolio_page(message):
    portfolio_text = "<b>Immerse yourself in the atmosphere of high-quality sound effects. On our portfolio page " \
                     "there are more than 1500 items, which will surely satisfy any of our customers</b>"
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Portfolio", url="https://audiojungle.net/user/moonaudioproduction/portfolio"
        )
    )
    chat_bot.send_message(
        message.chat.id, portfolio_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["Переглянути Портфоліо цілком", "Портфоліо", "портфоліо"]
)
def portfolio_page(message):
    portfolio_text = "<b>Зануртеся у атмосферу високої якості звукових ефектів. Наше портфоліо включає понад 1500 " \
                     "унікальних айтемів, що здатні задовольнити будь-які потреби навіть найвибагливіших " \
                     "користувачів</b>"
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Портфоліо", url="https://audiojungle.net/user/moonaudioproduction/portfolio"
        )
    )
    chat_bot.send_message(
        message.chat.id, portfolio_text, parse_mode="html", reply_markup=markup
    )


@chat_bot.message_handler(
    func=lambda message: message.text in ["MoonAudioProduction YouTube chanel", "YouTube", "youtube", "chanel",
                                          "YouTube chanel", "youtube chanel"]
)
def youtube_chanel(message):
    youtube_text = "<b>Official YouTube chanel of MoonAudioProduction which is presents high quality sound " \
                   "materials, thanks to which you will be able to embody your creative projects!</b>"
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "MoonAudioProduction YouTube chanel", url="https://www.youtube.com/@moonaudioproduction784"
        )
    )
    chat_bot.reply_to(message, youtube_text, parse_mode="html", reply_markup=markup)


@chat_bot.message_handler(
    func=lambda message: message.text in ["MoonAudioProduction YouTube канал", "Ютьюб", "Ютуб", "ютьюб", "ютуб"]
)
def youtube_chanel(message):
    youtube_text = "<b>Офіційний YouTube канал MoonAudioProduction що містить зразки високоякісних звукових " \
                   "ефектів!</b>"
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "MoonAudioProduction YouTube канал", url="https://www.youtube.com/@moonaudioproduction784"
        )
    )
    chat_bot.reply_to(message, youtube_text, parse_mode="html", reply_markup=markup)


@chat_bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        chat_bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)


@chat_bot.message_handler(content_types=["text"])
def get_user_message(message):
    if message.text == "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Continue in English":
        markup = types.ReplyKeyboardMarkup()
        button_1 = types.KeyboardButton("📕👀 Quick navigate guide")
        button_2 = types.KeyboardButton("🤔 What is MoonAudioProduction?")
        button_3 = types.KeyboardButton("💼 View Our Portfolio")
        button_4 = types.KeyboardButton("📝 Complete phrase list")
        markup.row(button_1, button_2, button_3)
        markup.row(button_4)
        greeting_message = f"Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. " \
                           f"MoonAudioProduction bot is glad to welcome you! " \
                           f"Our custom sound effects and music make your projects more colorful!"
        chat_bot.send_message(message.chat.id, greeting_message, parse_mode="html", reply_markup=markup)
        file = open("static/images/home_moon.png", "rb")
        chat_bot.send_photo(message.chat.id, file, reply_markup=markup)
        second_message = "How can I help You?"
        chat_bot.send_message(message.chat.id, second_message, parse_mode="html")

    elif message.text == "󠁧󠁢󠁥󠁮🇺🇦󠁿 Продовжити спілкування українською":
        markup = types.ReplyKeyboardMarkup()
        ua_button_1 = types.KeyboardButton("📕👀 Короткий посібник користувача")
        ua_button_2 = types.KeyboardButton("🤔 Що таке MoonAudioProduction?")
        ua_button_3 = types.KeyboardButton("💼 Переглянути Портфоліо")
        ua_button_4 = types.KeyboardButton("📝 Повний список команд доступних українською")
        markup.row(ua_button_1, ua_button_2, ua_button_3)
        markup.row(ua_button_4)
        greeting_message = f"Привіт, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. " \
                           f"MoonAudioProduction чат-бот радий вітати тебе! " \
                           f"Наші авторські звукові ефекти та оркестрова музика забезпечать якісно належне акустичне " \
                           f"оформлення Вашого проєкту що вигідно вирізнятиме його з-поміж інших!"
        chat_bot.send_message(message.chat.id, greeting_message, parse_mode="html", reply_markup=markup)
        file = open("static/images/home_moon.png", "rb")
        chat_bot.send_photo(message.chat.id, file, reply_markup=markup)
        second_message = "Чим я можу Вам допомогти?"
        chat_bot.send_message(message.chat.id, second_message, parse_mode="html")

    elif message.text == "🤔 What is MoonAudioProduction?":
        sticker = open('static/stickers/moon.webp', 'rb')
        chat_bot.send_sticker(message.chat.id, sticker)
        chat_bot.reply_to(message, f"<b>Dear {message.from_user.first_name} {message.from_user.last_name}</b> \n"
                                   "We are so excited to welcome you on our MoonAudioProduction workshop! \n"
                                   "Our creativity unites several directions at once: <b>Sound-design</b> "
                                   "and high quality <b>Cinematic music</b> as well as beautiful "
                                   "<b>Christmas Music</b> "
                                   "that creates a unique atmosphere of a family holiday. \n"
                                   "We invite you to familiarize yourself with our portfolio, in which we are sure, "
                                   "You will find what you need to realize your creative projects!!!!",
                          parse_mode="html")

    elif message.text == "🤔 Що таке MoonAudioProduction?":
        sticker = open('static/stickers/moon.webp', 'rb')
        chat_bot.send_sticker(message.chat.id, sticker)
        chat_bot.reply_to(message, f"<b>Шановний(а) {message.from_user.first_name} {message.from_user.last_name}</b> \n"
                                   "Ми надзвичайно раді вітати Вас у нашій звуковій майстерні MoonAudioProduction! \n"
                                   "Наша творчість поєднує в собі відразу декілька спрямувань: <b>Звуковий дизайн</b> "
                                   "а також високоякісну <b>Оркестрову музику</b>, зокрема <b>Музику до кінофільмів</b>"
                                   " а також витончену <b>Різдвяну музику</b>, що створює неперевершену атмосферу "
                                   "сімейного свята.\n"
                                   "Запрошуємо Вас ознайомитись з нашим портфоліо, в рамках якого, ми впевнені, "
                                   "Ви точно знайдете для себе щось цікавеньке!!",
                          parse_mode="html")

    elif message.text in ["💼 View Our Portfolio", "⬅️ Back to Category selection"]:
        markup = types.ReplyKeyboardMarkup()
        sound_effects = types.KeyboardButton("🔉 Sound Effects")
        cinematic_music = types.KeyboardButton("🎦 Cinematic Music")
        christmas_music = types.KeyboardButton("🎅 Christmas Music")
        logos = types.KeyboardButton("©️ Logos")
        all_items = types.KeyboardButton("View Whole Portfolio")
        back = types.KeyboardButton("↩️ Back to Main menu")
        markup.add(sound_effects, cinematic_music, christmas_music, logos, all_items, back)
        chat_bot.send_message(message.chat.id, text="Please select desired category ⤵️", reply_markup=markup)

    elif message.text in ["💼 Переглянути Портфоліо", "⬅️ Повернутися до вибору Категорії"]:
        markup = types.ReplyKeyboardMarkup()
        sound_effects = types.KeyboardButton("🔉 Звукові ефекти")
        cinematic_music = types.KeyboardButton("🎦 Музика до фільмів")
        christmas_music = types.KeyboardButton("🎅 Різдвяна музика")
        logos = types.KeyboardButton("©️Логотипи")
        all_items = types.KeyboardButton("Переглянути Портфоліо цілком")
        back = types.KeyboardButton("↩️ Повернутися до головного меню")
        markup.add(sound_effects, cinematic_music, christmas_music, logos, all_items, back)
        chat_bot.send_message(message.chat.id, text="Будь-ласка, оберіть необхідну категорію ⤵️", reply_markup=markup)

    elif message.text in [
        "🔉 Sound Effects", "Sound Effects", "sound effects", "sounds", "sound", "effects", "effect", "sfx", "SFX",
        "Foley", "foley", "Foley Sound", "foley sound", "Foley sound", "Foley Sounds", "foley sounds"
    ]:
        markup = types.ReplyKeyboardMarkup(row_width=4)
        cartoon = types.KeyboardButton("Cartoon Sounds")
        domestic = types.KeyboardButton("Domestic Sounds")
        futuristic = types.KeyboardButton("Futuristic Sounds")
        game = types.KeyboardButton("Game Sounds")
        human = types.KeyboardButton("Human Sounds")
        industrial = types.KeyboardButton("Industrial Sounds")
        interface = types.KeyboardButton("Interface Sounds")
        nature = types.KeyboardButton("Nature Sounds")
        whooshes = types.KeyboardButton("Transitions & Movement")
        urban = types.KeyboardButton("Urban Sounds")
        back_to_category = types.KeyboardButton("⬅️ Back to Category selection")
        back_home = types.KeyboardButton("↩️ Back to Main menu")
        markup.add(cartoon, domestic, futuristic, game, human, industrial, interface, nature, whooshes, urban,
                   back_to_category, back_home)
        chat_bot.send_message(message.chat.id, text="Please specify the appropriate subcategory⤵️", reply_markup=markup)

    elif message.text in ["🔉 Звукові ефекти", "Звукові Ефекти", "Звукові ефекти", "звукові ефекти", "звуки", "звук",
                          "ефекти", "ефект"]:
        markup = types.ReplyKeyboardMarkup(row_width=4)
        cartoon = types.KeyboardButton("Звуки до Мультфільмів")
        domestic = types.KeyboardButton("Побутові Звуки")
        futuristic = types.KeyboardButton("Футуристичні звуки")
        game = types.KeyboardButton("Ігрові звуки")
        human = types.KeyboardButton("Людські звуки")
        industrial = types.KeyboardButton("Промислові Звуки")
        interface = types.KeyboardButton("Звуки інтерфейсу")
        nature = types.KeyboardButton("Природні звуки")
        whooshes = types.KeyboardButton("Транзішнс")
        urban = types.KeyboardButton("Звуки міста")
        back_to_category = types.KeyboardButton("⬅️ Повернутися до вибору Категорії")
        back_home = types.KeyboardButton("↩️ Повернутися до головного меню")
        markup.add(cartoon, domestic, futuristic, game, human, industrial, interface, nature, whooshes, urban,
                   back_to_category, back_home)
        chat_bot.send_message(message.chat.id, text="Будь-ласка, оберіть необхідну підкатегорію звукових ефектів⤵️",
                              reply_markup=markup)

    elif message.text in ["↩️ Back to Main menu", "Menu", "menu", "Back to menu", "back to menu"]:
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton("📕👀 Quick navigate guide")
        button2 = types.KeyboardButton("🤔 What is MoonAudioProduction?")
        button3 = types.KeyboardButton("💼 View Our Portfolio")
        button4 = types.KeyboardButton("📝 Complete phrase list")
        markup.add(button1, button2, button3, button4)
        chat_bot.send_message(message.chat.id, text="You have successfully redirected to the main menu",
                              reply_markup=markup)

    elif message.text in ["↩️ Повернутися до головного меню", "Меню", "меню", "Повернутися до меню",
                          "повернутися до меню", "до меню", "в меню"]:
        markup = types.ReplyKeyboardMarkup()
        ua_button_1 = types.KeyboardButton("📕👀 Короткий посібник користувача")
        ua_button_2 = types.KeyboardButton("🤔 Що таке MoonAudioProduction?")
        ua_button_3 = types.KeyboardButton("💼 Переглянути Портфоліо")
        ua_button_4 = types.KeyboardButton("📝 Повний список команд доступних українською")
        markup.row(ua_button_1, ua_button_2, ua_button_3)
        markup.row(ua_button_4)
        chat_bot.send_message(message.chat.id, text="Ви успішно повернулися до головного меню",
                              reply_markup=markup)

    elif message.text in ["Hello", "hello", "hi", "Hi"]:
        sticker = open('static/stickers/Home.tgs', 'rb')
        chat_bot.send_sticker(message.chat.id, sticker)
        chat_bot.reply_to(message, "Hi there! 👋", parse_mode="html")

    elif message.text in ["Привіт", "привіт", "здоров"]:
        sticker = open('static/stickers/Home.tgs', 'rb')
        chat_bot.send_sticker(message.chat.id, sticker)
        chat_bot.reply_to(message, "Вітаю! 👋", parse_mode="html")

    elif message.text in [
        "📞 Contact the Author", "contact author", "Contact", "contact", "author", "Author", "Автор", "автор",
        "Contact Author"
    ]:
        chat_bot.reply_to(message, "Full Name: Ievgenii Balabanov;\nemail: moonaudioproduction@gmail.com;\n"
                                   "Phone Number: +380938208494", parse_mode="html")

    elif message.text in ["📞 Звʼязок з автором", "Звʼязок з автором", "Звʼязок", "звʼязок", "автор", "Автор"]:
        chat_bot.reply_to(message, "Прізвище та Імʼя: Balabanov Ievgenii;"
                                   "\nЕлектронна пошта: moonaudioproduction@gmail.com;\n"
                                   "Номер телефону: +380938208494", parse_mode="html")

    elif message.text in ["id", "ID", "Id", "iD", "айді", "Айді"]:
        chat_bot.reply_to(message, f"Your ID: {message.from_user.id}", parse_mode="html")

    elif message.text in ["name", "full name", "Get my full name"]:
        chat_bot.reply_to(message, f"Your full name: <b>{message.from_user.first_name} {message.from_user.last_name}"
                                   f"</b>", parse_mode="html")

    elif message.text in ["How are You?", "how are you", "How are you", "how are You", "how are you?"]:
        chat_bot.reply_to(message, "Thanks, I'm good!", parse_mode="html")

    elif message.text in ["як справи?", "як справи", "Як справи?", "Як справи"]:
        chat_bot.reply_to(message, "Дякую, все супер! Сподіваюсь, що у тебе також))", parse_mode="html")

    elif message.text == "📕👀 Quick navigate guide":
        chat_bot.reply_to(message, "For each user MoonAudioProduction bot gave the opportunity to <b>write me some "
                                   "messages, send me images, GIFs, or video files</b>. \nIn your message, for example,"
                                   " You can try to type something like this:"
                                   "\n- <b>ID</b> (also as 'id', 'Id', 'iD')\n- <b>Hello</b> "
                                   "(e.g. than 'Hello', 'hello', 'hi', 'Hi')"
                                   "\n- <b>How are you?</b> "
                                   "(e.g 'How are You?', 'how are you', 'How are you', 'how are You',  "
                                   "'how are you?')\n"
                                   "\nYou can also checkout the menu button to view the provided <b>commands</b>, or"
                                   " you can write them manually. Here are some existing commands:\n- <b>/start</b> - "
                                   "to restart communication with MoonAudioProduction Bot;\n- <b>/index_en</b> - back"
                                   " to main menu;\n- <b>/info_en</b> - to "
                                   "display author contact details;\n\n<b>P.S. - You can just click on those "
                                   "commands)</b>",
                          parse_mode="html")

    elif message.text == "📕👀 Короткий посібник користувача":
        chat_bot.reply_to(message, "MoonAudioProduction бот надає кожному користувачу можливість <b>надіслати "
                                   "текстове повідомлення, зображення, GIF-анімацію, стікер та відеофайл</b>. "
                                   "\nУ вашому повідомленні, до прикладу,"
                                   " Ви можете надрукувати щось на кшталт:"
                                   "\n- <b>ID</b> (також 'id', 'Id', 'iD', 'айді', 'Айді')\n- <b>Привіт</b> "
                                   "(у тому числі 'привіт', 'здоров')\n- <b>Як справи?</b> (або 'як справи?', "
                                   "'як справи', 'Як справи')\n\nВи також можете переглянути кнопку Меню що містить "
                                   "доступні <b>команди</b>, або ж можете написати їх власноруч. Ось декілька ключових "
                                   "команд:\n- <b>/start</b> - заново почати спілкування з ботом MoonAudioProduction;"
                                   "\n- <b>/index_ua</b> - відображає сторынку головного меню; \n- <b>/info_ua</b> - "
                                   "відображає контакти автора;\n\n<b>П.С. - Якщо не хочеш писати команду - можеш "
                                   "просто жмакати на неї 😜</b>",
                          parse_mode="html")

    elif message.text == "📝 Complete phrase list":
        chat_bot.send_message(message.chat.id, "<b><u>Available phrases:</u></b>\n- <b>ID</b> (also as 'id', 'Id', "
                                               "'iD')\n- <b>Hello</b> (e.g. than 'Hello', 'hello', 'hi', 'Hi')"
                                               "\n- <b>How are you?</b> (e.g 'How are You?', 'how are you', "
                                               "'How are you', 'how are You', 'how are you?')\n- <b>Portfolio</b> "
                                               "(e.g. 'View Whole Portfolio', 'portfolio', 'View Portfolio', 'items', "
                                               "'Items', 'All Items', 'all items')\n- <b>YouTube</b> (e.g. 'youtube', "
                                               "'chanel', 'YouTube chanel', 'youtube chanel')\n- <b>Menu</b> "
                                               "(e.g. 'menu', 'Back to menu', 'back to menu')"
                                               "\n\n<b><u>Portfolio Categories:</u></b>\n- <b>Sound Effects</b> (e.g "
                                               "'sound effects', 'sounds', 'sound', 'effects', 'effect', 'sfx', 'SFX', "
                                               "'Foley', 'foley', 'Foley Sound', 'foley sound', 'Foley sound', "
                                               "'Foley Sounds', 'foley sounds')\n\n- "
                                               "<b>Cinematic Music</b> (e.g. 'Cinematic music', 'cinematic music', "
                                               "'cinematic', 'Cinematic', 'Cinema', 'cinema', 'Cine', 'cine', 'Film', "
                                               "'film', 'Movie', 'movie', 'Movies', 'movies')"
                                               "\n\n- <b>Christmas Music</b> (e.g. 'christmas music', 'Christmas', "
                                               "'christmas', 'Xmas', 'XMAS', 'xmas')\n\n- <b>Logos</b> "
                                               "(e.g. 'logos', 'Logo', 'logo')"
                                               "\n\n<b><u>Categories of Sound Effects:</u></b>"
                                               "\n- <b>Cartoon Sounds</b> (e.g. 'Cartoon Sound', 'Cartoon sounds', "
                                               "'Cartoon sound', 'Cartoon', 'cartoon')\n\n- <b>Domestic Sounds</b> "
                                               "(e.g. 'Domestic Sounds', 'Domestic sounds', 'Domestic Sound', "
                                               "'Domestic sound', 'Domestic', 'domestic', 'Household', 'household')\n\n"
                                               "- <b>Futuristic Sounds</b> (e.g. 'Futuristic Sound', "
                                               "'Futuristic sounds', 'Futuristic sound', 'Futuristic', 'futuristic', "
                                               "'Sci-Fi Sounds', 'Sci-Fi sounds', 'Sci-Fi', 'Sci-fi', 'sci-fi', "
                                               "'Scifi')\n\n- <b>Game Sounds</b> (e.g. "
                                               "'Game sounds', 'Game Sound', 'Game sound', 'Game', 'game')\n\n- "
                                               "<b>Human Sounds</b> (e.g. 'Human sounds', 'human sounds', 'Human Sound'"
                                               ", 'Human', 'human', 'Human sound', 'Baby', 'baby', 'Babies', 'babies')"
                                               "\n\n- <b>Industrial Sounds</b> (e.g. "
                                               "'Industrial sounds', 'Industrial Sound', 'Industrial sound', "
                                               "'industrial sounds', 'industrial sound', 'Industrial', 'industrial',"
                                               "'Industry', 'industry')\n\n- <b>Interface Sounds</b> "
                                               "(e.g. 'Interface sounds', 'Interface Sound', 'Interface sound', "
                                               "'interface sounds', 'interface sound', 'Interface', 'interface', 'UI', "
                                               "'ui')\n\n- <b>Nature Sounds</b> (e.g. 'Nature sounds', 'Nature Sound', "
                                               "'nature sounds', 'nature sound', 'Nature', 'nature')"
                                               "\n\n- <b>Transitions & Movement</b> (e.g. 'Transitions & movement', "
                                               "'transitions & movement', 'transitions', 'transition', 'whoosh', "
                                               "'Whoosh', 'whooshes', 'Whooshes')\n\n- <b>Urban Sounds</b> (e.g. "
                                               "'Urban sounds', 'urban sounds', 'Urban', 'urban', 'City', 'city')"
                                               "\n\nYou can also checkout the menu button to view the "
                                               "provided <b>commands</b>, or you can write them manually. Here are some"
                                               " existing commands:\n- <b>/start</b> - to restart communication with "
                                               "MoonAudioProduction Bot;\n- <b>/index_en</b> - back to main menu;\n- "
                                               "<b>/info_en</b> - to display author contact details;"
                                               "\n\n<b>P.S. - You can just click on those commands)</b>",
                              parse_mode="html")

    elif message.text == "📝 Повний список команд доступних українською":
        chat_bot.send_message(message.chat.id, "<b><u>Доступні для обробки ботом репліки:</u></b>\n- "
                                               "<b>ID</b> (також 'id', 'Id', 'iD')\n- <b>Привіт</b> (також 'привіт',"
                                               "'здоров')\n- <b>Як справи?</b> (e.g ''як справи?', 'як справи', "
                                               "'Як справи')\n- <b>Портфоліо</b> (e.g. 'портфоліо')\n- "
                                               "<b>Ютуб</b> (e.g. 'Ютьюб', 'ютьюб', 'ютуб')\n- <b>Меню</b> "
                                               "(e.g. 'Меню', 'меню', 'Повернутися до меню', 'повернутися до меню', "
                                               "'до меню', 'в меню')\n\n<b><u>Категорії Портфоліо:</u></b>\n- "
                                               "<b>Звукові ефекти</b> (e.g 'Звукові Ефекти', 'звукові ефекти', 'звуки',"
                                               " 'звук', 'ефекти', 'ефект')\n\n- <b>Музика до фільмів</b> (e.g. 'кіно',"
                                               " 'до фильмів', 'до кіно', 'Фільм', 'фільм', 'Фільми', 'фільми', "
                                               "'Кінофільм', 'кінофільм', 'музика до фільмів')\n\n- "
                                               "<b>Різдвяна музика</b> (e.g. 'різдвяна музика', 'Різдвяна', 'різдвяна',"
                                               " 'Різдво', 'різдво')\n\n- <b>Логотипи</b> (e.g. 'лого', 'Лого', "
                                               "'Логотипи', 'логотипи', 'логотип', 'Логотип')\n\n<b><u>Категорії "
                                               "Звукових Ефектів:</u></b>\n- <b>Звуки до Мультфільмів</b> (e.g. "
                                               "'Мультфільми', 'мультфільми', 'мультфільм', 'Мультик', 'мультик', "
                                               "'Мультяшні звуки', 'мультяшні звуки', 'Мультяшні', 'мультяшні')"
                                               "\n\n- <b>Побутові Звуки</b> (e.g. 'Побутові звуки', 'побутові звуки', "
                                               "'Побутові', 'побутові', 'Побут', 'побут')\n\n - <b>Футуристичні звуки"
                                               "</b> (e.g. 'футуристичні звуки', 'Футуристичні', 'футуристичні')\n\n- "
                                               "<b>Ігрові звуки</b> (e.g. 'ігрові звуки', 'Ігрові', 'ігрові', 'Гра', "
                                               "'гра')\n\n- <b>Людські звуки</b> (e.g. 'людські звуки', 'Людина', "
                                               "'людина', 'Людські', 'людські')\n\n- <b>Промислові Звуки</b> (e.g. "
                                               "'Промислові', 'промислові', 'промислові звуки', 'індустріальні', "
                                               "'Індустріальні')\n\n"
                                               "- <b>Звуки інтерфейсу</b> (e.g. 'звуки інтерфейсу', 'Інтерфейс', "
                                               "'інтерфейс', 'юай')\n\n- "
                                               "<b>Природні звуки</b> (e.g. 'природні звуки', 'Природа', 'природа', "
                                               "'Звуки природи', 'звуки природи', 'Природні', 'природні')\n\n- "
                                               "<b>Транзішнс</b> (e.g. 'транзішнс', 'транзішн', 'транзішн', 'Вуш', "
                                               "'вуш', 'Вушаки', 'вушаки')\n\n- <b>Звуки міста</b> (e.g. 'звуки міста',"
                                               " 'Міські звуки', 'міські звуки', 'Урбан', 'урбан')"
                                               "\n\nВи також можете переглянути кнопку"
                                               " Меню що містить доступні <b>команди</b>, або ж можете написати їх "
                                               "власноруч. Ось декілька ключових команд:\n- <b>/start</b> - заново "
                                               "почати спілкування з ботом MoonAudioProduction;\n- <b>/index_ua</b> - "
                                               "відображає сторынку головного меню; \n- <b>/info_ua</b> - відображає "
                                               "контакти автора;\n\n<b>П.С. - Якщо не хочеш писати команду - можеш "
                                               "просто жмакати на неї 😜</b>", parse_mode="html")

    else:
        chat_bot.send_message(message.chat.id, "I'm sorry, but I don't understand you... 😞/ Вибач, але я не розумію "
                                               "тебе... 😞(", parse_mode="html")


if __name__ == '__main__':
    print("Starting bot...")

print("Bot is polling...")
chat_bot.polling(none_stop=True)
