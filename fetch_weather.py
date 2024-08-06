
import aiohttp
async def fetch_weather(session,url):
    async with session.get(url) as response:
        data = await response.json()
        return data