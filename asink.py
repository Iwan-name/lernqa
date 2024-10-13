# import time
# from pprint import pprint
# import aiohttp
# import asyncio
# import requests
#
# list_end = ["https://ya.ru/", "https://google.com/",
#             "https://www.youtube.com/"]
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         for i in list_end:
#             async with session.get(i) as result:
#                 await asyncio.sleep(5)
#                 print(f"Для 1 {i}", result.status)
#
#             async with session.get(i) as result:
#                 await asyncio.sleep(2)
#                 print(f"Для 2 {i}", result.status)
#
#
# asyncio.get_event_loop().run_until_complete(main())


import asyncio
import aiohttp
import time

# асинхронная функция для загрузки url
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = [
        'https://myrusakov.ru/image-format-learning.html',
        'https://myrusakov.ru/protecting-a-page-with-javascript.html',
        'https://myrusakov.ru/php-fluent-interface.html',
    ]

    start_time = time.time()


    tasks = []
    for url in urls:
        tasks.append(fetch(url))

    end_time = time.time()

    # расчет времени выполнения
    elapsed_time = end_time - start_time
    print('Elapsed time: ', elapsed_time)


    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


asyncio.run(main())
