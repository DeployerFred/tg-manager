import ast
import datetime
from pyrogram import Client


async def forwarder(target, forwardTo, api_id, api_hash):
    async with Client("my_account", api_id, api_hash) as app:
        print(str(datetime.datetime.now()))
        print("Target Id:", target, "Forward To:", forwardTo)
        i = 0
        start = int(input("Offset = "))
        if start == None:
            start = 0
        async for message in app.get_chat_history(target, offset=start):
            i += 1
            print("OFFSET:", i)
            if message.document == None:
                pass
            else:
               print("MESSAGE ID: [" , message.id, "]")
               try:
                   fileName=ast.literal_eval(str(message.document))["file_name"]
                   print(fileName)
               except:
                   pass
               await app.copy_message(forwardTo, target, message_id=message.id)