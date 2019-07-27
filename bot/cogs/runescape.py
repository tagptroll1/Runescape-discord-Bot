from textwrap import dedent

from discord import Embed
from discord.ext.commands import Cog, command, group

from bot.exceptions import Fetch400Error, Fetch500Error, UnknownNon200Error
from bot.models.player_skills import (
    PlayerSkills, IronmanSkills, HardcoreSkills
)
from bot.services.runescape import RunescapeApi


class Runescape(Cog):
    def __init__(self):
        self.players = {}
        self.ironmans = {}
        self.hardcores = {}
        self.api = RunescapeApi()

    async def get_player(self, name, type_):
        if type_ == "player":
            dict_ = self.players
            class_ = PlayerSkills
        elif type_ == "iron":
            dict_ = self.ironmans
            class_ = IronmanSkills
        elif type_ == "hardcore":
            dict_ = self.hardcores
            class_ = HardcoreSkills

        try:
            if name in dict_:
                player = dict_[name]
                await player.update()
            else:
                player = await class_.from_api(self.api, name)
                dict_[name] = player
        except Fetch400Error as e:
            return {"message": "User does most likely not exist"}
        except Fetch500Error as e:
            return {"message": "Server error"}
        except UnknownNon200Error as e:
            return {"message": "Something magical happened"}
        
        return player

    @command()
    async def item(self, ctx, category: int, letter, page: int=1):
        if len(letter) != 1:
            return await ctx.send(f"letter must be 1 letter, not {letter}")

        resp = await self.api.get_item(category, letter, page)
        await ctx.send(resp)
        
    @group(invoke_without_command=True)
    async def hiscore(self, ctx, *, name):
        await ctx.invoke(self.hiscore_level, name=name)

    @hiscore.command(name="level", aliases=("lvl",))
    async def hiscore_level(self, ctx, *, name):
        result = await self.get_player(name, "player")
        if isinstance(result, dict):
            return await ctx.send(result["message"])
        await ctx.send(embed=result.level_embed)

    @hiscore.command(name="exp", aliases=("xp", "experience"))
    async def hiscore_exp(self, ctx, *, name):
        result = await self.get_player(name, "player")
        if isinstance(result, dict):
            return await ctx.send(result["message"])
        await ctx.send(embed=result.exp_embed)

    @hiscore.command(name="rank")
    async def hiscore_rank(self, ctx, *, name):
        result = await self.get_player(name, "player")
        if isinstance(result, dict):
            return await ctx.send(result["message"])
        await ctx.send(embed=result.rank_embed)

    @group(invoke_without_command=True)
    async def ironman(self, ctx, name):
        await ctx.invoke(self.ironman_level, name=name)

    @ironman.command(name="level", aliases=("lvl",))
    async def ironman_level(self, ctx, *, name):
        result = await self.get_player(name, "iron")
        if isinstance(result, dict):
            return await ctx.send(result["message"])
        await ctx.send(embed=result.level_embed)

    @ironman.command(name="exp", aliases=("xp", "experience"))
    async def ironman_exp(self, ctx, *, name):
        result = await self.get_player(name, "iron")
        if isinstance(result, dict):
            return await ctx.send(result["message"])
        await ctx.send(embed=result.exp_embed)

    @ironman.command(name="rank")
    async def ironman_rank(self, ctx, *, name):
        result = await self.get_player(name, "iron")
        if isinstance(result, dict):
            return await ctx.send(result["message"])
        await ctx.send(embed=result.rank_embed)

    @group( aliases=("hcironman", "hardcore"),
            invoke_without_command=True)
    async def hardcoreironman(self, ctx, name):
        await ctx.invoke(self.hardcore_level, name=name)

    @hardcoreironman.command(name="level", aliases=("lvl",))
    async def hardcore_level(self, ctx, *, name):
        result = await self.get_player(name, "hardcore")
        if isinstance(result, dict):
            return await ctx.send(result["message"])
        await ctx.send(embed=result.level_embed)

    @hardcoreironman.command(name="exp", aliases=("xp", "experience"))
    async def hardcore_exp(self, ctx, *, name):
        result = await self.get_player(name, "hardcore")
        if isinstance(result, dict):
            return await ctx.send(result["message"])
        await ctx.send(embed=result.exp_embed)

    @hardcoreironman.command(name="rank")
    async def hardcore_rank(self, ctx, *, name):
        result = await self.get_player(name, "hardcore")
        if isinstance(result, dict):
            return await ctx.send(result["message"])
        await ctx.send(embed=result.rank_embed)

def setup(bot):
    bot.add_cog(Runescape())