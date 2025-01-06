import aiohttp


async def jokes() -> str:
    url: str = "http://rzhunemogu.ru/RandJSON.aspx?CType=1"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()


async def quotes() -> str:
    url: str = "http://rzhunemogu.ru/RandJSON.aspx?CType=5"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
