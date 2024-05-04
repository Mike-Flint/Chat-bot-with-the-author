from aiogram import types, Router
from aiogram.filters import Command 

user_handlers_router = Router()

from handlers.admin_handlers import admin_handlers_router
user_handlers_router.include_router(admin_handlers_router)


@user_handlers_router.message(Command("start"))
async def START(message: types.Message):
    print(message)
    await message.answer_sticker("CAACAgIAAxkBAAELlttl4hy4TSmsMmdYpzwU7GYWYzhGtAAC1iAAApjPKEnq2IB0fWL2izQE")
    await message.answer(
                         "Все команды бота: \n"
                         "/start - информация в использовании бота\n"
                         "/info - соцсети автора\n\n"
                         "Важная информация: \n"
                         "Все сообщения, которые вы здесь отправите, направляются Автору, по желанию он может вам ответить.\n\n"
                         "Если будет замечено з вашей стороны спам или оскорбление, Автор может заблокировать вас.\n"
                          )
    
@user_handlers_router.message(Command("info"))
async def info(message: types.Message):    
    await message.answer("Автора ссылки:\n"
                         "<a href ='https://www.google.com.ua/' title=''> Twitch </a>----|----"
                         "<a href ='https://www.google.com.ua/' title=''> Kick</a>\n"
                         "<a href ='https://www.google.com.ua/' title=''> Tik Tok </a>---|---"
                         "<a href ='https://www.google.com.ua/' title=''> YouTube </a>\n"
                         "<a href ='https://www.google.com.ua/' title=''> Discord </a>--|--"
                         "<a href ='https://www.google.com.ua/' title=''> Telegram </a>\n"
                         "<a href ='https://www.google.com.ua/' title=''> Git Hub </a>--|--"
                         "<a href ='https://www.google.com.ua/' title=''> Instagram </a>"
                         , disable_web_page_preview=True , parse_mode='HTML')


        
    




