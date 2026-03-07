import asyncio
import time

async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    task_1 = fetch_data(1) # This is coroutine object
    task_2 = fetch_data(2) # This is coroutine object
    result_1 = await task_1
    print("Task 1 fully completed")
    result_2 = await task_2
    print("Task 2 fully completed")
    return [result_1, result_2]

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Total time taken: {t2 - t1}")



