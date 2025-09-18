import asyncio
import time

async def say_after(delay, what):
  await asyncio.sleep(delay)
  return f"{what} - {delay}"

async def main():

  # task1 = asyncio.create_task(
  # )
  # task2 = asyncio.create_task(
  #   say_after(2, 'world')
  # )
  
  print(f"started at {time.strftime('%X')}")


  ret = await asyncio.gather(task1, task2) 
  '''
  - 要全部的 task 都完成才算結束，最後會 return list
  - gather 會自動把每個 coroutine 變成 task ，所以不用再手動建立了
  '''

  print(ret)

  print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
