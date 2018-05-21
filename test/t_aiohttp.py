import aiohttp
import asyncio


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(url, resp.status)
            # print(url, await resp.text())

loop = asyncio.get_event_loop()     # 得到一个事件循环模型
tasks = [                           # 初始化任务列表
    get("http://zhushou.360.cn/detail/index/soft_id/3283370"),
    get("http://zhushou.360.cn/detail/index/soft_id/3264775"),
    get("http://zhushou.360.cn/detail/index/soft_id/705490")
]
loop.run_until_complete(asyncio.wait(tasks))    # 执行任务
loop.close()
