from datetime import datetime

from discord import Embed

from bot.exceptions import Fetch400Error, Fetch500Error, UnknownNon200Error
from bot.enums.runescape_skills import icons
from bot.templates.skillpage import insert


class BasePlayerSkills:
    def __init__(self, api, name, data):
        self.name = name
        self.skills_overall = data.pop("overall", None)
        self.data = data
        self.api = api
        self.last_update = datetime.now()

    @classmethod 
    async def from_api(cls, api, name):
        obj = cls(api, name, {})
        await obj.update(force=True)
        return obj

    async def update(self, force=False):
        diff = datetime.now() - self.last_update 
        if force or diff.seconds > 300:
            try:
                resp = await self.get_func(self.name)
            except (Fetch400Error, Fetch500Error, UnknownNon200Error) as e:
                raise e

            self.skills_overall = resp.pop("overall")
            self.data = resp
            self.last_update = datetime.now()


    def skills_embed(self, key="level"):
        values = {}
        for key_, value in self.data.items():
            val = value[key]
            if key == "level":
                values[key_] = val if int(val) > 9 else f"0{val}"
            else:
                values[key_] = val
        footer = self.skills_overall[key]

        skills = insert(icons, values)

        embed = Embed()
        embed.title = f"{self.name}'s skills ({key})"
        embed.description = skills
        embed.set_footer(text=f"Total: {footer}")
        return embed

    @property
    def level_embed(self):
        return self.skills_embed()

    @property
    def exp_embed(self):
        return self.skills_embed(key="exp")

    @property
    def rank_embed(self):
        return self.skills_embed(key="rank")

class PlayerSkills(BasePlayerSkills):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_func = self.api.get_hiscore

class IronmanSkills(BasePlayerSkills):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_func = self.api.get_ironman

class HardcoreSkills(BasePlayerSkills):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_func = self.api.get_hc_ironman
