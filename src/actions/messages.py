from gtts import gTTS                                   # Импорт модуля преобразования текста в речь
from aiogram import Bot, Dispatcher, types, filters     # Импорт Box, Dispatcher, types, filters из aiogram
from config import TELEGRAM_BOT_TOKEN                   # Импорт токена Telegram из конфигуратора Telegram
import os                                               # Импорт модуля операционной системы

bot = Bot(token = TELEGRAM_BOT_TOKEN)                   # Подключение приложения к боту Telegram
dp = Dispatcher()                                       # Подключение к приложению-диспетчеру бота Telegram

# Текст голосового сообщения
text = """
С Новым Годом тебя! Пусть этот год будет полон радости, удачи и свершений. 
Пусть сбудутся все твои мечты, а каждый день принесет только положительные моменты.

С наступающим! 
"""

@dp.message(filters.CommandStart())
async def send_welcome(message: types.Message):
    """Функция отправки сообщения привествия"""
    await message.reply("""Здравствуй! 🌟 В этот рождественский период мы добавляем немного магии к обращениям. Как бы ты хотел(а) быть назван(а) в этот праздничный сезон?""")

@dp.message()
async def echo(message: types.Message):
    """Функция отправки ответного сообщения"""
    welcome = f"Привет, {message.text}. "               # Текст приветсивя 
    tts = gTTS(welcome + text, lang = "ru")             # Прием и озвучивание текста на русском языке
    tts.save(f"{message.from_user.id}.mp3")             # Сохранение аудиозаписи
    
    # Отправка голосового сообщения 
    await message.answer_voice(types.FSInputFile(f"{message.from_user.id}.mp3"), caption="Привет, дорогой друг! С наступающим Новым годом! 🎄✨ Давай проведем вместе этот волшебный праздник. Послушай меня: в новогоднюю ночь сбудется множество желаний, и каждый снежинка принесет с собой радость и уют. Пусть этот год будет полон смеха, вдохновения и приятных сюрпризов. С наступающим Новым годом! 🎅🎉")
    # Отправка изображения
    await message.answer_photo(types.FSInputFile(f"image/{os.listdir('image')[0]}"))


async def startBot():
    """Функция запуска бота"""
    await dp.start_polling(bot, skip_updates = True) 