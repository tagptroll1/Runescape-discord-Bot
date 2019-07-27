import csv
import json
import socket
from async_timeout import timeout as aio_timeout
from io import StringIO

from aiohttp import ClientSession, AsyncResolver, TCPConnector

from bot.exceptions import Fetch400Error, Fetch500Error, UnknownNon200Error
from bot.enums.runescape_skills import skills

def get_session():
    return ClientSession(
        connector=TCPConnector(
            resolver=AsyncResolver(),
            family=socket.AF_INET,
        )
    )


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

    async def fetch(self, url, use_json=False):
        async with get_session() as session:
            async with aio_timeout(10):
                async with session.get(url) as response:
                    status_type = response.status // 100
                    if use_json:
                        data = await response.json()
                    else:
                        data = await response.text()
        print(url)

        if status_type == 4:
            raise Fetch400Error("404 Not found")
        elif status_type == 5:
            raise Fetch500Error("500 Server error")
        elif status_type != 2:
            raise UnknownNon200Error("Non 200 - Unknown")
            
        return data

    async def get(self, url, use_json=False, use_csv=False):
        # Explicit except -> raise
        try:
            data = await self.fetch(url, use_json)
        except Fetch400Error as e:
            raise e
        except Fetch500Error as e:
            raise e
        except UnknownNon200Error as e:
            raise e

        if use_csv and not use_json:
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
        return await self.get(url, use_csv=True)

    async def get_hc_ironman(self, name):
        url = self.hc_ironman_url.format(player=name)
        return await self.get(url, use_csv=True)
