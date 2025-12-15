import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user} (ID: {bot.user.id})')
    print('------')
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos de barra.")
    except Exception as e:
        print(f"Falha ao sincronizar comandos de barra: {e}")

@bot.hybrid_command(name="ping", description="Verifica a latência do bot.")
async def ping(ctx: commands.Context):
    latency_ms = round(bot.latency * 1000)
    await ctx.send(f'Pong! 🏓 Latência: `{latency_ms}ms`')

async def load_cogs():
    try:
        await bot.load_extension('commands.moderation')
        print("Módulo 'commands.moderation' carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o módulo 'commands.moderation': {e}")

@bot.event
async def on_connect():
    await load_cogs()

bot.run(os.environ.get('BOT_TOKEN'))