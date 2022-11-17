import discord
from discord.ext import commands

class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents = discord.Intents.all(),
            case_insensitive = True,
            application_id = 1042498144790913125
        )

        self.initial_extensions = [
            "cogs.default"
        ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)

        await bot.tree.sync(guild = discord.Object(id = 1042498800062828604))

    async def close(self):
        await super().close()
        await self.sessions.close()

    async def on_ready(self):
        print("Бот готов к будущим задачам !")

        try:
            synced = await bot.tree.sync()
            await bot.tree.sync(guild = discord.Object(id = 1042498800062828604))
            print(f"Синхронизировано [{len(synced)}] комманд !")

        except Exception as e:
            print(e)    

bot = MyBot()
bot.run("MTA0MjQ5ODE0NDc5MDkxMzEyNQ.Gqm63L.ayXDXkBAsmUUwPkgvT8sJHutQjteqhHprURCIU")
