import concurrent.futures
import asyncio

async def async_task():
    print("Start async_task")
    await asyncio.sleep(2)
    print("End async_task")

def sync_task():
    print("Start sync_task")
    # Some CPU-bound operation
    result = sum(i for i in range(10**10))
    print("End sync_task")
    return result

async def main():
    print("Main Start")

    # Xử lý bất đồng bộ
    await asyncio.gather(async_task())
    
    result = sync_task()
    print(f"Result from sync_task: {result}")

    # Xử lý đồng thời
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     future = executor.submit(sync_task)
    #     result = await asyncio.to_thread(future.result)
    #     print(f"Result from sync_task: {result}")

    print("Main End")

if __name__ == "__main__":
    asyncio.run(main())