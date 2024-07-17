import discord
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

channel_id = None

@client.event
async def on_ready():
    global channel_id
    print(f'In Filbus we trust.')
    
    # Ask for the channel ID when the bot starts
    channel_id = input("Enter the channel ID to send messages: ")

    # Convert to integer if it's a valid number
    try:
        channel_id = int(channel_id)
    except ValueError:
        print("Invalid channel ID.")
        return
    
    channel = client.get_channel(channel_id)
    
    if channel:
        await channel.send("Filbus is awake.")
        # Start the loop to send the GIF every hour
        client.loop.create_task(send_gif_every_hour(channel))
    else:
        print("Channel not found.")

async def send_gif_every_hour(channel):
    while True:
        await channel.send("https://tenor.com/view/filbus-gif-15763565782588620290")
        await asyncio.sleep(3600)

@client.event
async def on_disconnect():
    if channel_id:
        channel = client.get_channel(channel_id)
        if channel:
            asyncio.ensure_future(channel.send("Filbus now sleeps."))

client.run(TOKEN)
