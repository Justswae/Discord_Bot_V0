import discord
import responses
from discord.ext import commands


async def send_message(message,user_message,is_private):
    try:
        response=responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN=''
    client=commands.Bot(command_prefix='#')

    @client.event
    async def on_ready():
        print('Bot is now running')

    @client.event
    async def on_message(message):
        if message.author==client.user:
            return 
        
        username=str(message.author)
        user_message=str(message.content)
        channel=str(message.channel)
        
        print(f"{username} said '{user_message}' in {channel}")
        
        if user_message[0]=='?':
            user_message=user_message[1:]
            await send_message(message,user_message,is_private=True)
        else:
            await send_message(message,user_message,is_private=False)

    client=commands.Bot(command_prefix='#')

    @client.command(aliases=['c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx,amount=2):
        await ctx.channel.purge(limit=amount)
    client.run(TOKEN)
