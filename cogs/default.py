import discord
import os
import random
import json
from discord import app_commands
from discord.ext import commands

coloring_the_embed = [0x474747, 0xffffff]

class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Красный', description="Ваш любимый цвет это красный !", emoji="🟥"),
            discord.SelectOption(label='Зелёный', description="Ваш любимый цвет это зелёный !", emoji="🟩"),
            discord.SelectOption(label='Синий', description="Ваш любимый цвет это синий !", emoji="🟦")
        ]

        super().__init__(placeholder="Выберите ваш любимый цвет...", min_values=1, max_values=1, options=options)
    
    async def callback(self, interaction: discord.Interaction):
        try:
            if self.values[0] == "Зелёный":
                embed = discord.Embed(title="Использование команды \"color\" !", description=f"**Ваш любимый цвет - `{self.values[0]}🟩**`", color=0x70b461)
            elif self.values[0] == "Красный":
                embed = discord.Embed(title="Использование команды \"color\" !", description=f"**Ваш любимый цвет - `{self.values[0]}🟥`**", color=0xe22943)
            elif self.values[0] == "Синий":
                embed = discord.Embed(title="Использование команды \"color\" !", description=f"**Ваш любимый цвет - `{self.values[0]}🟦`**", color=0x56abec)

        except TimeoutError:
            embed = discord.Embed(title="Использование команды \"color\" !", description=f"**Время ожидании истекло.**", color=random.choice(coloring_the_embed))

        embed.set_footer(text="New Era of Bots", icon_url="https://cdn.discordapp.com/avatars/1042498144790913125/22c9ba40079a1e1e9f410433a7558aa1.png?size=256https://cdn.discordapp.com/avatars/1042498144790913125/22c9ba40079a1e1e9f410433a7558aa1.png?size=256")
        await interaction.response.send_message(embed = embed, ephemeral=True)

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Dropdown())

class Default(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Раздел \"Default\" был включен !")

    @app_commands.command(name="hello", description="Тестовая команда.")
    async def hello(self, interaction: discord.Interaction):

        embed = discord.Embed(title="Использование команды \"hello\" !", description=f"**Здраствуйте уважаемый пользователь {interaction.user.mention} ! Это `слеш-команда` !**", color=(random.choice(coloring_the_embed)))
        embed.set_footer(text="New Era of Bots", icon_url="https://cdn.discordapp.com/avatars/1042498144790913125/22c9ba40079a1e1e9f410433a7558aa1.png?size=256https://cdn.discordapp.com/avatars/1042498144790913125/22c9ba40079a1e1e9f410433a7558aa1.png?size=256")

        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="color", description="Выбрать свой любимый цвет.")
    async def color(self, interaction: discord.Interaction):

        view = DropdownView()

        await interaction.response.send_message(view=view)

    @app_commands.command(name="say", description="Написать сообщение от имени бота.")
    @app_commands.describe(arg = "Что я должен сказать?")
    async def say(self, interaction: discord.Interaction, arg: str):

        embed = discord.Embed(title="Использование команды \"say\" !", description=f"**({interaction.user.mention}|{interaction.user.name}) сказал: `{arg}` !**", color=(random.choice(coloring_the_embed)))
        embed.set_footer(text="New Era of Bots", icon_url="https://cdn.discordapp.com/avatars/1042498144790913125/22c9ba40079a1e1e9f410433a7558aa1.png?size=256https://cdn.discordapp.com/avatars/1042498144790913125/22c9ba40079a1e1e9f410433a7558aa1.png?size=256")

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Default(bot),
        guilds= [discord.Object(id = 1042498800062828604)])