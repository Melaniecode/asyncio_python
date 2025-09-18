import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # 第二個 say_after 要等前一個結束後才可以建立 task 才能變成 task ， 才能被放進 event loop 
    # 思考點： 何不兩個一起等 -> create_task
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
