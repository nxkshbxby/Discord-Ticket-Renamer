import discord
from discord.ext import commands
import re
# virusx69
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.author.id == 123 and message.channel.category.id == 123:
        if message.embeds:
            for embed in message.embeds:
                if embed.description:
                    match = re.search(
                        r'\*\*Please Enter Your Product Here\*\*\s*```([^`]+)```',
                        embed.description,
                        re.IGNORECASE
                    )
                    if match:
                        product = match.group(1).strip()
                        if product:
                            try:
                                channel_name = f"{product()}"[:100]
                                await message.channel.edit(name=channel_name)
                                print(f"Channel renamed to: {channel_name}")
                            except discord.Forbidden:
                                print("Missing permissions to rename channel")
                            except Exception as e:
                                print(f"Error: {e}")
    
    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')
