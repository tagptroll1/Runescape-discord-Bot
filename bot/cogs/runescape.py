from textwrap import dedent

from discord import Embed
from discord.ext.commands import Cog, command, group

from bot.enums.runescape_skills import icons
from bot.services.runescape import RunescapeApi
from bot.templates.skillpage import insert

class Runescape(Cog):
    def __init__(self):
        self.api = RunescapeApi()

    async def get_skills_embed(
        self, name, key="level"
    ):
        resp = await self.api.get_hiscore(name)
        overall = resp.pop("overall")

        values = {}
        for key_, value in resp.items():
            val = value[key]
            if key == "level":
                values[key_] = val if int(val) > 9 else f"0{val}"
            else:
                values[key_] = val
        footer = overall[key]

        skills = insert(icons, values)

        embed = Embed()
        embed.title = f"{name}'s skills ({key})"
        embed.description = skills
        embed.set_footer(text=f"Total: {footer}")
        return embed

    @command()
    async def item(self, ctx, category: int, letter, page: int=1):
        if len(letter) != 1:
            return await ctx.send(f"letter must be 1 letter, not {letter}")

        resp = await self.api.get_item(category, letter, page)
        await ctx.send(resp)
        
    @group(hidden=True, invoke_without_command=True)
    async def hiscore(self, ctx, *, name):
        await ctx.invoke(self.hiscore_level, name=name)

    @hiscore.command(name="level")
    async def hiscore_level(self, ctx, *, name):
        embed = await self.get_skills_embed(name)
        await ctx.send(embed=embed)

    @hiscore.command(name="exp", aliases=("xp", "experience"))
    async def hiscore_exp(self, ctx, *, name):
        embed = await self.get_skills_embed(name, key="exp")
        await ctx.send(embed=embed)

    @hiscore.command(name="rank")
    async def hiscore_rank(self, ctx, *, name):
        embed = await self.get_skills_embed(name, key="rank")
        await ctx.send(embed=embed)

    @command()
    async def ironman(self, ctx, name):
        resp = await self.api.get_ironman(name)
        await ctx.send(resp)

    @command(aliases=["hcironman", "hardcore"])
    async def hardcoreironman(self, ctx, name):
        resp = await self.api.get_hc_ironman(name)
        await ctx.send(resp)

def setup(bot):
    bot.add_cog(Runescape())