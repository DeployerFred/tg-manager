import ast
from pyrogram import Client

async def fileDownloader(target, api_id, api_hash):
    async with Client("my_account", api_id, api_hash) as app:
        async for message in app.get_chat_history(target):
           if message.document == None:
                pass
           else:
               print(message.id)
               fileName=ast.literal_eval(str(message.document))["file_name"]
               print(fileName)

               async def progress(current, total):
                   print(f"{current * 100 / total:.1f}%")

               await app.download_media(message, progress=progress)