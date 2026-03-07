import asyncio
import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    task_1 = asyncio.create_task(fetch_data(1)) # A task is created and scheduled to run as soon as possible
    task_2 = asyncio.create_task(fetch_data(2)) # A task is created and scheduled to run as soon as possible
    result_2 = await task_2
    print("Task 2 fully completed")
    result_1 = await task_1
    print("Task 1 fully completed")
    return [result_1, result_2]

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Total time taken: {t2 - t1}")


