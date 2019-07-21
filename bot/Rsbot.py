from discord.ext.commands import Bot

class RsBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
