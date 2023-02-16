from pyrogram.client import Client
from pyrogram.types.messages_and_media import Message

async def write_new_link(client: Client, message: Message) -> Message:
    
    try:
        link = message.text.split(' ')[1]
        with open('links.txt', 'a', encoding='utf-8') as file:
            file.write(f'{link}\n')
        
        return await client.send_message(
            text=f'Ссылка {link} была успешно добавлена!\n Для отмены пропишите /cancel',
            chat_id=message.chat.id)
        
    except:
        return await client.send_message(
            text="Неправильный формат ввода!\nПример: /add <ссылка>",
            chat_id=message.chat.id
        )
    

async def delete_last_row(client: Client, message: Message) -> None:
    
    try:

        with open('links.txt', 'r', encoding='utf-8') as file:

            content = file.readlines()
        
        with open('links.txt', 'w', encoding='utf-8') as file:

            deleted_row = content[-1::][0].replace('\n', '')

            file.writelines([content[i] for i in range(len(content) - 1)])
        
        await client.send_message(
            text=f'Ссылка {deleted_row} была удалена',
            chat_id=message.chat.id
        )

    except Exception as e:
        await client.send_message(
            text=f'Ошибка. Возможно, текстовый файл не существует или не содержит ссылок',
            chat_id=message.chat.id
        )