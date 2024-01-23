from pyrogram import Client, filters
#from pyrogram.errors import BadRequest
import asyncio
from pyrogram import *
from pyrogram.types import *
import time

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION= getenv("SESSION_STRING")
TIME = getenv("TIME")
LOG =getenv("LOG")
GROUPS=getenv("GROUPS")
User = Client(
    name="user-account",
    session_string=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=300
)


@User.search. message (filters.chat(GROUPS) | filters.photo |  | filters.video | filters.document,limit=20)
async def delete(user,message):
    try:
        await asyncio.sleep(60)
        await message.forward(LOG)
        await asyncio.sleep(TIME)
        await message.delete()
    except Exception as e:
        print(e)



User.run()
