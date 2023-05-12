from pyrogram import Client, filters
 
import time
from time import sleep
import random
 
api_id = 10994477
api_hash = "85b0d0b1b41b5717b8e0cad074378ff9"

app = Client("blackpensil", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("so", prefixes=".") & filters.me)
def so(_, msg):
    i = 0
    
    while(i < 20):
    	try:
    		text = "🐕" + str(i) + "Собака"
    		msg.reply_text(text)
    		sleep(1)
    
app.run()   