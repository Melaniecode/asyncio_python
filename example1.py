import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1) # task 會直接調用 asyncio.sleep(coroutine)並返回一個 future ，不會建立 task
    print('world')

asyncio.run(main())
'''
1. 創建一個新的 Event Loop。
2. 在這個 Event Loop 裡執行 main() coroutine。
3. 等待 main() 完成後關閉 Event Loop。
'''
