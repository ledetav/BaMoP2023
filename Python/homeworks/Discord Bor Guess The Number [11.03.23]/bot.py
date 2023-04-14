import asyncio
import discord
from discord.ext import commands
import random

description = '''Угадай число'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def угадай(ctx):
    """Начинает игру "Угадай число"."""
    number = random.randint(-10_000_000, 10_000_000)
    attempts = 0
    max_attempts = 100
    await ctx.send('Я загадал число, попробуйте угадать. У вас 100 попыток.')
    while attempts < max_attempts:
        try:
            message = await bot.wait_for('message', check=lambda msg: msg.author == ctx.author, timeout=30.0)
        except asyncio.TimeoutError:
            await ctx.send('Игра окончена. Вы не успели угадать число.')
            return
        try:
            guess = int(message.content)
        except ValueError:
            await ctx.send('Вы должны ввести целое число от -10000000 до 10000000.')
            continue
        if guess < -10_000_000 or guess > 10_000_000:
            await ctx.send('Вы должны ввести число в диапазоне от -10000000 до 10000000.')
            continue
        attempts += 1
        if guess == number:
            await ctx.send(f'Вы угадали число {number} за {attempts} попыток!')
            return
        elif guess < number:
            await ctx.send(f"Мое число больше, чем {guess}. Осталось {max_attempts - attempts} попыток.")
        else:
            await ctx.send(f"Мое число меньше, чем {guess}. Осталось {max_attempts - attempts} попыток.")
    await ctx.send(f'Вы использовали все {max_attempts} попыток. Игра окончена. Было загадано число {number}.')

TOKEN = ''

bot.run(TOKEN)