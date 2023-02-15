import os

import discord

import response

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

async def send_message(message, user_message, is_private):
    try:
        response_message = response.handle_response(message)
        print(response_message)
        await message.author.send(response_message) if is_private else await message.channel.send(response_message)
    except Exception as e:
        print(e)

def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents=discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('boop')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        print(message)
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said {user_message} in {channel}")
        print(user_message)
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)


