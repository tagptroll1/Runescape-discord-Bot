import csv
import json
import socket
from io import StringIO

from aiohttp import ClientSession, AsyncResolver, TCPConnector

from bot.enums.runescape_skills import skills


class RunescapeApi:
    item_url = (
        "https://services.runescape.com/m=itemdb_rs/api/catalogue/"
        "items.json?category={category}&alpha={alpha}&page={page}"
    )

    hiscore_url = (
        "https://secure.runescape.com/m=hiscore/index_lite.ws?player={player}"
    )

    ironman_url = (
        "https://secure.runescape.com/m=hiscore_ironman/index_lite.ws?player={player}"
    )

    hc_ironman_url = (
        "https://secure.runescape.com/m=hiscore_hardcore_ironman/index_lite.ws?player={player}"
    )

    def __init__(self):
        self.client = ClientSession(
            connector=TCPConnector(
                resolver=AsyncResolver(),
                family=socket.AF_INET,
            )
        )

    async def get(self, url, use_json=False, use_csv=False):
        async with self.client.get(url) as response:
            if response.status != 200:
                return {"status": response.status}
            if use_json:
                return await response.json()

            data = await response.text()

            if use_csv:
                f = StringIO(data)
                csv_reader = csv.reader(f, delimiter=",")
                skills_dict = {}

                for i, stats in enumerate(csv_reader):
                    if i == len(skills):
                        break

                    rank = stats[0]
                    level = stats[1]
                    exp = stats[2]

                    skill_name = skills[i]
                    skills_dict[skill_name] = {
                        "rank": rank,
                        "level": level,
                        "exp": exp,
                    }
                    
                return skills_dict

        return json.loads(data)

    async def get_item(self, category, alpha, page=1):
        url = self.__class__.item_url.format(
            category=category, 
            alpha=alpha, 
            page=page
        )
        return await self.get(url)

    async def get_hiscore(self, name):
        url = self.hiscore_url.format(player=name)
        return await self.get(url, use_csv=True)
        
    async def get_ironman(self, name):
        url = self.ironman_url.format(player=name)
        return await self.get(url)

    async def get_hc_ironman(self, name):
        url = self.hc_ironman_url.format(player=name)
        return await self.get(url)
