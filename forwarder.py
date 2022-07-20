import ast
from pyrogram import Client

async def forwarder(target, forwardTo, api_id, api_hash):
    async with Client("my_account", api_id, api_hash) as app:
        async for message in app.get_chat_history(target):
           print(message.id)
           fileName=ast.literal_eval(str(message.document))["file_name"]
           print(fileName)
           await app.copy_message(forwardTo, target, message_id=message.id)