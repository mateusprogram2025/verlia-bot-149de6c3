import discord
from discord.ext import commands
import os

# Importando os cogs
from commands.moderation import Moderation

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True # Necessário para funções de moderação, como ban e unban

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    print(f'📊 Servidores: {len(bot.guilds)}')
    
    # Carregar os cogs
    await bot.add_cog(Moderation(bot))
    
    await bot.tree.sync()  # Sincroniza slash commands

@bot.event
async async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Você não tem permissão para usar este comando.", ephemeral=True)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Faltam argumentos para este comando. Verifique a sintaxe.", ephemeral=True)
    elif isinstance(error, commands.CommandNotFound):
        # Ignora comandos não encontrados
        pass
    else:
        print(f"Erro inesperado: {error}")
        await ctx.send(f"Ocorreu um erro inesperado: {error}", ephemeral=True)

# ═══════════════════════════════════════════
# 🔌 CONEXÃO DO BOT - NUNCA REMOVA ESTA LINHA
# ═══════════════════════════════════════════
bot.run(os.environ.get('BOT_TOKEN'))