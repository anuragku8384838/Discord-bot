import discord
from discord.ext import commands

# Define intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Create bot object
bot = commands.Bot(command_prefix="!", intents=intents)

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Simple command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Respond to any message that mentions the bot
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send(f"Hello {message.author}, how can I help?")
    await bot.process_commands(message)

# Simple moderation command (kick user)
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} has been kicked for {reason}")

# Run the bot
bot.run("YOUR_BOT_TOKEN")
