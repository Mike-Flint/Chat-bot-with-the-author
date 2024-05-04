from aiogram import types, Router , Bot
import json
import asyncio

import key

End = Router()

@End.message( )
async def send_message(message: types.Message , bot: Bot): 
    with open('Json/ban_list.json', 'r') as file:
        data = json.load(file)

    if message.reply_to_message and message.text and message.text.lower().startswith("ban") and message.reply_to_message.from_user.id == key.BOT_id and message.reply_to_message.text.startswith("Cообщие от") and message.from_user.id == key.Admin_id:

        mass = message.reply_to_message.text.split(" | ")
        if any(blk[1] == mass[2] for blk in data["Block"]):
            delete = await message.answer("Пользователь уже забанен.")
            await asyncio.sleep(10)
            await delete.delete()
        else:
            json_file = [mass[1],mass[2]]
            data["Block"].append(json_file)
            delete = await message.answer("Пользователь забанен.")
            
            await asyncio.sleep(10)
            await delete.delete()

            with open('Json/ban_list.json', 'w') as file:
                json.dump(data, file, indent=4)
    elif message.reply_to_message and message.text and message.reply_to_message.text.startswith("Заблокированные:") and message.text.isdigit() and message.reply_to_message.from_user.id == key.BOT_id and message.from_user.id == key.Admin_id:   
        
        if message.text and message.text.isdigit():
            
            nextt = message.text.split()
            try:
                data['Block'].pop(int(nextt[0]) - 1)
            except IndexError:
                delete = await message.answer(f"Такого индекса нету.")
                await asyncio.sleep(10)
                await delete.delete()
                
                return
            with open('Json/ban_list.json', 'w') as file:
                json.dump(data, file, indent=4)

            delete = await message.answer(f"Пользователь разблокирован.")
            await asyncio.sleep(10)
            await delete.delete()
    elif message.reply_to_message and message.text and message.from_user.id == key.Admin_id and message.reply_to_message.from_user.id == key.BOT_id and message.reply_to_message.text.startswith("Cообщие от"):
        
        mass = message.reply_to_message.text.split(" | ")
        await bot.send_message( int(mass[2]) , message.text ) 
          
        delete = await message.answer("Отправлено.")

        await asyncio.sleep(10)
        await delete.delete()
    else:
        if not any(int(block[1]) == message.from_user.id for block in data["Block"]):
            delete = await message.answer("Отправлено.")
            await message.forward(chat_id = str(key.Admin_id) , caption="Новая подпись")
            await bot.send_message( key.Admin_id , f"Cообщие от | @{message.from_user.username} | {message.from_user.id}")

            await asyncio.sleep(10)
            await delete.delete()
        else:
            delete = await message.answer("Вас заблокировали, вам не доступна отправка соопщений.")

            await asyncio.sleep(10)
            await delete.delete()
        