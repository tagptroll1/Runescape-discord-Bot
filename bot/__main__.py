from pathlib import Path

import yaml

from .Rsbot import RsBot

default_file = Path("default_config.yml")
config_file = Path("config.yml")

if not default_file.exists():
    raise UserWarning("default_config.yml was not found!")

if not config_file.exists():
    raise UserWarning("config.yml was not found!")

with default_file.open() as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

with config_file.open() as file:
    tmp = yaml.load(file, Loader=yaml.SafeLoader)

    for key, value in tmp.items():
        config[key] = value


token = config.get("bot", {}).get("token")
if token is None or token == "missing":
    raise UserWarning("No token set in config.yml")


prefix = config.get("bot", {}).get("prefix", "!")


bot = RsBot(command_prefix=prefix)
bot.load_extension("bot.cogs.runescape")
bot.run(token)
