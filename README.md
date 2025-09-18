# [Python] Asyncio
主要負責建立 Event Loop、管理 Coroutine 與 Task。能同時處理多個 I/O 任務。
- Event Loop：管理員，安排 Task 什麼時候執行、暫停、恢復
- Task：包裝 coroutine 的「執行實體」，由 Event Loop 管理
- Coroutine：程式片段，Task 執行它時才跑起來

## 1. Event Loop
- 負責管理與調度多個非同步 `task`
- 當某個 Task 遇到 I/O 等待時，Event Loop 可以切換去執行其他 Task
    - Coroutine
        - 是一段可以`「暫停與恢復執行」`的函式或程式片段，
        - 通常用 **async def** 定義。
        - 本質：只是程式物件，還沒執行。
        ```python=
        # coroutine function
        async def foo():
            await asyncio.sleep(1)
            
        foo() # 回傳的就是一個 coroutine object。
        ```
    - Task
        - event loop 執行的最小單位
        - 把 coroutine 排程到 Event Loop 執行
        - Task 會被 Event Loop 排程，遇到 await 暫停時會自動交出控制權

## 2. async 的特性
- 不會讓 **CPU-bound 運算** 變快，只是解決 **I/O-bound 等待** 的效率問題  
- 適合處理需要等待的任務（如網路請求、資料庫查詢、檔案讀寫）  
- 所有 coroutine 都在同一個 thread 裡執行，同一時間只會執行一個任務，不存在搶 CPU 的情況，所以可以避免 race condition
- Context switch
    - Thread / Process 的 context switch = 由 OS 來決定，CPU 要切換暫存器、快取、狀態，很昂貴。
    - Coroutine / Task 的切換 = 純 Python level，由 await 主動讓出控制權，不需要 OS 干預，切換成本小很多。
- Task 必須「主動讓出控制權」，不然event loop會進入死循環

## Reference
- https://www.youtube.com/watch?v=brYsDi-JajI
- https://myapollo.com.tw/blog/begin-to-asyncio/
- https://www.youtube.com/watch?v=K0BjgYZbgfE
