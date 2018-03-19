import requests
import aiohttp
import asyncio
    
urls =  [  'https://requestb.in/11oai3h1',
          'https://requestb.in/112doe71',
          'https://requestb.in/1m75lh71'
        ]

async def fetch(session, url):
    with aiohttp.Timeout(100):
        async with session.get(url) as response:
            return await response.text()

async def fetch_all(session, urls, loop):
    results = await asyncio.gather(
        *[fetch(session, url) for url in urls],
        return_exceptions=True 
    )

    for index, url in enumerate(urls):
        print('{}: {}'.format(url, 'Error' if isinstance(results[index], Exception) else 'OK'))
    return results

def asyncronous():
    loop = asyncio.get_event_loop()
    with aiohttp.ClientSession(loop=loop) as session:
        the_results = loop.run_until_complete(
            fetch_all(session, urls, loop))

def synchronous():
    for url in urls:
        r = requests.get(url)
        print (url," - ",r.status_code,r.content.decode())

print("Asynchronous")
asyncronous()

print("Synchronous")
synchronous()