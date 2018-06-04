#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d(%(funcName)s) %(message)s')


async def time_out(loop, sec):
    logging.info("")
    await asyncio.sleep(sec)
    loop.stop()

def main():
    logging.info("")
    import echo_server
    echo_server.start()
    import echo_client
    echo_client.start()
    echo_client.start()
    echo_client.start(msg=b'end')
    echo_client.start()
    echo_client.start()
    echo_client.start()
    echo_client.start()

if __name__ == '__main__':
    logging.info('作为主程序运行')
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(time_out(loop, 5))

    main()

    loop.run_forever()
else:
    print('package_robot 初始化')
