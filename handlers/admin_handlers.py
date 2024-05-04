from aiogram import types, Router , F
from aiogram.filters import Command , CommandObject
from aiogram.types import Message
import json

admin_handlers_router = Router()

from handlers.End import End


@admin_handlers_router.message(Command("help"))
async def settings(message: Message):
    await message.answer(
                         "Админ панель все команды:\n"
                         "/ban_list - список забаненных.\n\n"
                         "Ответив на сообщение c началом 'Cообщие от' и указав команду 'ban' он будет внесен в бан лист.\n\n"
                         "Ответив на сообщение c бан листа и указав индекс пользователя он будет разбанен.\n\n"
                         "Ответив на сообщение c началом 'Cообщие от' и написав любой текст у которого нет в начале слова 'ban' вы ответите на сообщение.\n\n"
                         )

@admin_handlers_router.message(Command("ban_list"))
async def ban_list(message: Message ):
    with open('Json/ban_list.json', 'r') as file:
        data = json.load(file)

    send = ""
    nummber = 0
    for item in data['Block']:
        nummber += 1
        next_item = f"{nummber} • {item[0]} - {item[1]}\n"
        send += next_item  

    await message.answer(f"Заблокированные:\n{send}")


@admin_handlers_router.message(Command("Raffle_list"))
async def Raffle_list(message: Message ):
    with open('Json/Raffle.json', 'r') as file:
        data = json.load(file)
    
    send = ""
    nummber = 0
    for item in data['Edit']:
        nummber += 1
        if nummber % 100 == 0:
            await message.answer(f"Учасники:\n{send}", disable_web_page_preview=True , parse_mode='HTML')
            send = ""

        next_item = f"{nummber} • @{item[1]} -<a href = '{item[0]}' title=''> Tik Tok </a>\n"
        send += next_item
    
    await message.answer(f"Участники:\n{send}", disable_web_page_preview=True , parse_mode='HTML')
    

@admin_handlers_router.message(Command("Raffle_delete"))
async def Raffle_delete(message: Message ):
    with open('Json/Raffle.json', 'r') as file:
        data = json.load(file)

    data['Edit'] = []

    with open('Json/Raffle.json', 'w') as file:
        json.dump(data, file, indent=4)

    await message.answer("Все участники розыгрыша были удалены")


@admin_handlers_router.message(Command("Raffle_"))
async def Raffle_(message: Message):
    with open('Json/admin_settings.json', 'r') as file:
        data = json.load(file)

    
    if data['OFF_ON_RAFFLE'] == True:
        data['OFF_ON_RAFFLE'] = False
        await message.answer(f"Розыгрыш закрыт")

    elif data['OFF_ON_RAFFLE'] == False:
        data['OFF_ON_RAFFLE'] = True
        await message.answer(f"Розыгрыш открыт.")
    
    with open('Json/admin_settings.json', 'w') as file:
            json.dump(data, file, indent=4)
    
admin_handlers_router.include_router(End)