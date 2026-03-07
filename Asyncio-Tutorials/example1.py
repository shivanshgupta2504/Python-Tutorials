import time

def fetch_data(param):
    print(f"Do something with {param}...")
    time.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

def main():
    result_1 = fetch_data(1)
    print("Fetch 1 fully completed")
    result_2 = fetch_data(2)
    print("Fetch 2 fully completed")
    return [result_1, result_2]

t1 = time.perf_counter()

results = main()
print(results)

t2 = time.perf_counter()
print(f"Total time taken: {t2 - t1}")
