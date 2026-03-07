# Asyncio and Asynchronous Programming in Python

## Introduction

The `asyncio` package in Python is a library used to write concurrent code using the `async`/`await` syntax. It serves as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, and more.

Before diving deeper into `asyncio`, it's important to understand the fundamental difference between **Synchronous** and **Asynchronous** programming.

---

## Synchronous vs Asynchronous Programming

### Synchronous Programming

In synchronous programming, tasks are executed sequentially, one after the other. Each instruction must wait for the previous one to complete before it can start. This is a linear flow. If one task takes a long time to complete—like fetching data from an API, querying a database, or reading a large file—it will block the execution of the entire program, forcing the CPU to sit idle while waiting.

**Real-world Example:**
Imagine you are at a local coffee shop with only one barista. You place your order for a latte. The barista takes your payment, goes to the espresso machine, makes the latte, hands it to you, and _only then_ turns to the next customer in line to take their order. If your drink takes 5 minutes to make, the next customer has to wait 5 minutes just to place their order.

**Basic Synchronous Python Code:**

```python
import time

def make_tea():
    print("Started making tea...")
    time.sleep(3) # Simulates boiling water (blocked execution)
    print("Tea is ready!")

def make_toast():
    print("Started making toast...")
    time.sleep(2) # Simulates toasting bread (blocked execution)
    print("Toast is ready!")

def prepare_breakfast():
    start_time = time.time()

    make_tea()
    make_toast()

    end_time = time.time()
    print(f"Breakfast prepared in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    prepare_breakfast()
```

_Output Execution Flow:_

```text
Started making tea...
Tea is ready!
Started making toast...
Toast is ready!
Breakfast prepared in 5.01 seconds.
```

_(Notice how the total time is the sum of both tasks: 3 + 2 = 5 seconds)._

---

### Asynchronous Programming

In asynchronous programming, tasks are executed concurrently. If a task requires waiting for an external process (like I/O operations), the program does not stop completely. Instead, it yields control, allowing the program to move on and execute other independent tasks. Once the waiting task finishes its background work, the program resumes it. This prevents idle waiting and significantly improves application performance and responsiveness.

**Real-world Example:**
Imagine a busier coffee shop with a better system. The cashier takes your order, gives you a receipt with a number, and passes the ticket to the barista. While the barista is making your latte, the cashier immediately turns to the next customer and takes their order. When your latte is finished, the barista calls your number. Multiple things are happening at once, and no one is blocked from simply placing an order.

**Basic Asynchronous Python Code:**

```python
import asyncio
import time

async def make_tea():
    print("Started making tea...")
    # asyncio.sleep is a non-blocking wait. It tells the event loop:
    # "I'm going to wait for 3 seconds, go run something else in the meantime."
    await asyncio.sleep(3)
    print("Tea is ready!")

async def make_toast():
    print("Started making toast...")
    await asyncio.sleep(2)
    print("Toast is ready!")

async def prepare_breakfast():
    start_time = time.time()

    # asyncio.gather runs multiple asynchronous tasks concurrently
    await asyncio.gather(
        make_tea(),
        make_toast()
    )

    end_time = time.time()
    print(f"Breakfast prepared in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(prepare_breakfast())
```

_Output Execution Flow:_

```text
Started making tea...
Started making toast...
Toast is ready!
Tea is ready!
Breakfast prepared in 3.01 seconds.
```

_(Notice how the total time is approximately the length of the longest task: 3 seconds. The tasks overlapped!)_

---

## Asynchronous Programming Terminologies and Rules

To effectively write asynchronous code in Python, you must understand a few core concepts and rules.

### 1. `async` and `await` Keywords

- **`async`**: This keyword is used to declare a function as a "coroutine". When you prefix `def` with `async` (e.g., `async def my_func():`), it tells Python that this function is asynchronous and will not execute immediately when called; instead, it returns a coroutine object.
- **`await`**: This keyword is used to pause the execution of the surrounding coroutine until the awaited operation finishes. It passes control back to the event loop, allowing other things to run while this operation finishes.

**Real-world Example:**
`async` is like getting a job description that says "this task involves some waiting." `await` is when you actually reach the part of the job where you put a cake in the oven, set a timer, and go do other chores instead of staring at the oven.

### 2. Event Loop

The event loop is the core executor of asynchronous programming. It is an infinite loop that manages, schedules, and executes asynchronous tasks. It keeps track of all running tasks and decides whose turn it is to run. If a task hits an `await` and pauses, the event loop switches to the next available ready task.

**Real-world Example:**
The event loop is like the head chef in a busy kitchen. The chef knows exactly what every cook is doing. If the fry cook is waiting for fries to finish, the head chef assigns them to chop onions in the meantime. The chef coordinates all the tasks so no one is just standing around.

### 3. Coroutines (Functions vs. Objects)

- **Coroutine Function:** A function defined using `async def`.
- **Coroutine Object:** The object returned when you _call_ a coroutine function. Calling `async def my_func()` does not run its code; it creates a coroutine object. To actually run it, you must schedule it on the event loop (e.g., using `await` or `asyncio.run()`).

**Real-world Example:**
A **coroutine function** is the recipe for baking a cake. A **coroutine object** is the actual physical preparation you've started (getting the ingredients out). You still need to put it in the oven (the event loop) to actually bake it.

### 4. Tasks

A Task is a wrapper around a coroutine that schedules it to run on the event loop _concurrently_ in the background. When you wrap a coroutine in an `asyncio.Task` (commonly via `asyncio.create_task()`), the event loop starts running it as soon as possible, without you necessarily having to `await` it immediately.

**Real-world Example:**
If a coroutine object is preparing a cake, making it a **Task** is like hiring a dedicated assistant to start baking it for you right now, in the background, while you continue working on something else.

### 5. Futures

A Future is a low-level object representing an eventual result of an asynchronous operation that hasn't finished yet. Tasks are actually built on top of Futures. You generally don't create Futures directly in typical `asyncio` code, but you interact with them under the hood. It acts as a placeholder for a value that will exist at some point in the future.

**Real-world Example:**
A **Future** is like the buzzer given to you at an overcrowded restaurant. It doesn't contain food yet, but it is a promise that eventually, it will alert you when your food is ready.

### 6. Why is `await` only used inside an `async` function?

The `await` keyword fundamentally means "pause this function and yield control to the event loop." Standard synchronous Python functions (defined with `def`) run in a straight line and don't know how to yield control to pause mid-execution. Therefore, to use `await`, the function itself must be built to handle pausing and resuming, which is exactly why it must be defined with the `async def` syntax.

**Real-world Example:**
You can't tell a strictly sequential robot assembly line to "pause and do something else," because it was only built to move straight ahead. You have to use a flexible, multi-tasking robot (`async` function) if you want to give it "pause and wait" (`await`) instructions.

### 7. Why can't synchronous functions be awaited?

An `await` statement expects an "awaitable" object—like a coroutine, Task, or Future—something that correctly interacts with the event loop and can signal when it is finished or needs to pause. A synchronous function executes linearly and completely. Since it never yields control to the event loop, waiting for it asynchronously is impossible; running it would just block the entire program until the function finishes.

**Real-world Example:**
You can't "wait asynchronously" for an old landline phone. If someone calls, the single family line is completely occupied until they hang up. You can only "await" operations on a modern smartphone that can put calls on hold or juggle multiple apps simultaneously.

---

## Deeper Dive: Event Loop Execution and Task Management

### How does the Event Loop "find" Coroutines?

A common doubt is: _If a coroutine isn't explicitly passed to `asyncio.run()`, how does the event loop know to execute it?_

The answer lies in the `await` keyword. A coroutine object does nothing on its own. When you start an asynchronous program, you typically pass only one "main" coroutine to `asyncio.run(main())`. This acts as the **entry point** for the event loop.

Once the event loop is running `main()`, any time `main()` hits an `await child_coroutine()`, it acts as a messenger:

1. `main()` says to the event loop: _"I need to pause here because I am waiting for `child_coroutine()` to finish."_
2. The event loop takes control, looks at `child_coroutine()`, and says: _"Since `main()` is paused waiting for you, I'll start running you now."_
3. The event loop dynamically discovers and executes `child_coroutine()`.

Think of `asyncio.run(main())` as handing the event loop the trunk of a tree. As the event loop climbs the trunk, it dynamically discovers all the branches (`await`ed coroutines) attached to it.

### `asyncio.run()` vs `asyncio.create_task()`

Both involve the event loop, but they serve entirely different purposes:

#### 1. `asyncio.run(coroutine)`: The "Ignition Switch"

- **What it does:** Creates a brand new event loop, runs the given coroutine until it completely finishes, and then strictly closes the loop.
- **When to use it:** Usually only **once** per application. It kicks off your main asynchronous entry point.
- **Behavior:** It blocks standard synchronous execution until the entire async application finishes.

#### 2. `asyncio.create_task(coroutine)`: The "Background Worker"

- **What it does:** Wraps a coroutine into a `Task` and schedules it to run on the _already actively running_ event loop as soon as possible.
- **When to use it:** Inside an active async function to fire off an operation in the background and move on immediately without waiting for it.
- **Behavior:** It is non-blocking. It instantly returns a `Task` object and runs the coroutine concurrently whenever the loop gets a chance.

### Mixing `await` and `create_task()`

What happens if you use both inside the same function?

```python
import asyncio
import time

async def background_task():
    print("Background task started")
    await asyncio.sleep(2)  # Yields control
    print("Background task finished")

async def foreground_task():
    print("Foreground task started")
    await asyncio.sleep(1)  # Yields control
    print("Foreground task finished")

async def main():
    # 1. Fire and forget: Schedule background_task to run concurrently
    bg_task = asyncio.create_task(background_task())

    print("Moving on immediately after create_task...")

    # 2. Block until foreground_task is done
    await foreground_task()

    print("Foreground task is done, main is ending.")

asyncio.run(main())
```

**Execution Flow Breakdown:**

1. `main()` starts. It calls `create_task(background_task())`. The event loop places `background_task` in a queue but _doesn't run it yet_ because `main` hasn't paused.
2. `print("Moving on...")` executes.
3. `main()` calls `await foreground_task()`. `foreground_task` prints its start message and hits `await asyncio.sleep(1)`. This forces `foreground_task` to **yield control** back to the event loop.
4. The event loop, now free, sees `background_task` in the queue. It starts `background_task`, which prints its start message, hits `await asyncio.sleep(2)`, and yields control.
5. After 1 second, `foreground_task` wakes up, finishes, and unpauses `main()`.
6. `main()` completes and prints its final message.
7. Because `main()` finished, `asyncio.run()` aggressively closes the event loop.
   - _Note:_ The `background_task` needed 2 seconds, but `main` finished in 1. Because we never explicitly `await bg_task`, it gets cancelled mid-execution!

**The Golden Rules of Mixing:**

- `create_task` schedules work to happen in the background.
- `await` is the engine that actually drives concurrency. The event loop only switches between tasks when a running task encounters an `await`.
- Keep track of your `create_task` references; if your main program finishes before they do, they will be terminated.

---

## Blocking vs Non-Blocking Calls

When discussing asynchronous programming, understanding how functions affect execution flow is crucial.

### 1. Blocking Calls

A **blocking call** literally "blocks" the execution of your program. When your code executes a blocking function, the entire script stops running at that exact line and waits until that function completely finishes its job. Only after it returns a result does the program move to the next line of code.

- **Common Examples:** `time.sleep()`, reading a file standardly (`open(file).read()`), calling an API using standard `requests`.
- **Real-world Analogy:** Imagine cooking dinner and instructions say "Bake for 30 minutes". A blocking cook stands completely frozen, staring at the oven for 30 minutes. They won't chop vegetables or wash dishes; they just wait.

### 2. Non-Blocking Calls

A **non-blocking call** initiates an operation but immediately returns control to the program, _even if the operation hasn't finished yet_. The program does not stop; it fires off the request and instantly moves to the next line.

- **Common Examples:** `await asyncio.sleep()`, `asyncio.create_task()`, making asynchronous web requests with `aiohttp`.
- **Real-world Analogy:** A non-blocking cook puts the dish in the oven, sets a 30-minute timer, and immediately turns their attention to chopping vegetables or washing dishes. The baking still takes 30 minutes, but the cook moves on to other tasks rather than just staring at the oven.

**In the context of `asyncio`:**

- `time.sleep(5)` is **blocking**. It freezes the whole script.
- `await asyncio.sleep(5)` is **non-blocking**. It tells the program to pause this specific coroutine for 5 seconds, but _yields control_ back to the event loop so the loop can run other tasks while waiting.

---

## Achieving True Concurrency: A Tale of Two Examples

It's a common misconception that simply adding `async` and `await` automatically makes your code run faster or concurrently. Concurrency only happens when you correctly schedule tasks on the event loop.

Let's compare two approaches to understand why one runs sequentially while the other achieves true concurrency.

### Example A: Sequential Execution (The "False" Concurrency)
Imagine scheduling coroutine objects directly:

```python
async def main():
    task_1 = fetch_data(1) # Just creates a Coroutine object, doesn't start it!
    task_2 = fetch_data(2) # Just creates a Coroutine object.
    
    result_1 = await task_1 # Event loop runs fetch_data(1), main pauses here until it finishes.
    result_2 = await task_2 # AFTER task_1 is done, event loop runs fetch_data(2), main pauses.
    return [result_1, result_2]
```
**The Execution Flow:**
1. `task_1` and `task_2` are created, but they are just idle coroutine objects. The event loop doesn't know about them yet.
2. `await task_1` is called. `main` pauses. The event loop now knows about `fetch_data(1)` and starts it.
3. `fetch_data(1)` rests for 1 second. Because nothing else is scheduled, the event loop just waits.
4. After 1 second, `fetch_data(1)` finishes.
5. `await task_2` is called. The event loop now knows about `fetch_data(2)` and starts it.
6. `fetch_data(2)` rests for 2 seconds. The event loop waits.
7. Total time taken: **~3 seconds**. 
Even though we used asynchronous keywords, the execution was 100% sequential. The event loop was never given the chance to run tasks at the same time!

### Example B: Concurrent Execution with `create_task`
Now, see what happens when we use `asyncio.create_task()`:

```python
async def main():
    # We schedule both on the event loop immediately!
    task_1 = asyncio.create_task(fetch_data(1)) 
    task_2 = asyncio.create_task(fetch_data(2)) 
    
    result_1 = await task_1 # main pauses, but task_2 is already scheduled to run!
    result_2 = await task_2 
    return [result_1, result_2]
```
**The Execution Flow Breakdown:**
1. `task_1` is created using `create_task()`. The event loop is told: *"Hey, put `fetch_data(1)` in your queue to run ASAP."*
2. `task_2` is created using `create_task()`. The event loop is told: *"Put `fetch_data(2)` in your queue to run ASAP."*
3. `await task_1` is called. `main` yields control and pauses.
4. The event loop takes over. It looks at its queue and sees `task_1` and `task_2`.
5. It starts `task_1`. `task_1` hits its 1-second sleep and yields control.
6. The event loop checks its queue again! It sees `task_2` is waiting. It starts `task_2`. `task_2` hits its 2-second sleep and yields control.
7. Both tasks are now sleeping *at the same time*.
8. After 1 second, `task_1` finishes. `main` unpauses, assigns `result_1`, and moves to `await task_2`.
9. `main` yields control again to wait for `task_2`. But `task_2` has *already* been sleeping for 1 second!
10. After 1 more second, `task_2` finishes.
11. Total time taken: **~2 seconds**.

**The Takeaway:**
To achieve concurrency, you must inform the event loop of all your tasks *before* you start blocking your code with `await`. `asyncio.create_task()` allows you to "fire off" multiple operations so they run in tandem in the background.

### Example C: The Order of `await` Matters
What happens if we schedule tasks concurrently with `create_task`, but we deliberately change the order in which we `await` them? What if we `await task_2` (which takes 2 seconds) *before* `await task_1` (which takes 1 second)?

```python
async def main():
    task_1 = asyncio.create_task(fetch_data(1)) # 1-second task
    task_2 = asyncio.create_task(fetch_data(2)) # 2-second task
    
    result_2 = await task_2 # Waiting for the LONGESt task first!
    print("Task 2 fully completed")
    
    result_1 = await task_1 # Waiting for the SHORTER task second!
    print("Task 1 fully completed")
    return [result_1, result_2]
```

**The Execution Output:**
```text
Done with 1
Done with 2
Task 2 fully completed
Task 1 fully completed
```

**The Execution Flow Breakdown:**
1. Both `task_1` and `task_2` are dynamically scheduled concurrently.
2. We immediately hit `await task_2`. `main` yields control and pauses, telling the event loop: *"Wake me up only when `task_2` is completely finished (which takes 2 seconds)."*
3. The event loop starts processing both tasks concurrently.
4. **At the 1-second mark:** `task_1` naturally finishes its sleep in the background! The background coroutine resumes and prints `"Done with 1"`. However, our `main` function is *still* paused because it's strictly waiting for `task_2`. Therefore, the main function cannot proceed to print `"Task 1 fully completed"` yet.
5. **At the 2-second mark:** `task_2` finishes completely. The background coroutine prints `"Done with 2"`.
6. Because `task_2` is finally finished, the `await task_2` block is satisfied and `main` unpauses. It executes the very next line and prints `"Task 2 fully completed"`.
7. `main` then hits `await task_1`. But wait! `task_1` already finished its work a whole second ago! Because the task is already "done", the `await task_1` acts instantaneously, simply grabbing the ready-to-go result without pausing. 
8. `main` instantly prints `"Task 1 fully completed"`.
9. Total time taken: Still **~2 seconds**.

**The Takeaway:**
When using `create_task`, the background tasks themselves run concurrently *independent* of your `await` order. However, `await` forces your `main` function to block sequentially. If you `await` a slow task before a fast task, the fast task will finish quietly in the background, but your main function won't be able to process its result until after the slow task completes!

### Example D: The Danger of Blocking Code in `asyncio`
What happens if we schedule tasks using `asyncio.create_task()` (just like `example3.py` doing concurrent scheduling), but inside our coroutine, we accidentally use a standard synchronous `time.sleep()` instead of `await asyncio.sleep()`?

```python
import time

async def fetch_data(param):
    print(f"Do something with {param}...")
    time.sleep(param) # DANGER: This is a synchronous, blocking sleep!
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    task_1 = asyncio.create_task(fetch_data(1)) 
    task_2 = asyncio.create_task(fetch_data(2)) 
    
    result_1 = await task_1 
    print("Task 1 fully completed")
    result_2 = await task_2 
    print("Task 2 fully completed")
    return [result_1, result_2]
```

**The Execution Output:**
```text
Do something with 1...
Done with 1
Do something with 2...
Done with 2
Task 1 fully completed
Task 2 fully completed
```

**The Execution Flow Breakdown:**
1. `task_1` and `task_2` are created and placed in the event loop's queue.
2. `main` hits `await task_1`, yielding control to the event loop.
3. The event loop starts `task_1`. `task_1` prints `"Do something with 1..."` and hits `time.sleep(1)`.
4. **CRITICAL FAILURE:** Because `time.sleep(1)` is a synchronous **blocking** call, it *freezes the entire Python thread*, including the event loop! The coroutine never yields control back to the event loop to say "I'm pausing". It just stands there completely frozen.
5. Because the event loop is frozen, it cannot look at its queue or start `task_2`! 
6. After 1 second, the freeze lifts. `task_1` prints `"Done with 1"` and genuinely finishes. 
7. *Now* the event loop is finally free again! It looks at its queue, sees `task_2`, and starts it.
8. `task_2` prints `"Do something with 2..."` and hits `time.sleep(2)`. The entire thread and event loop freeze again for 2 whole seconds! 
9. After 2 seconds, `task_2` finishes and prints `"Done with 2"`.
10. With all background tasks done, `main` processes the results and finishes.
11. Total time taken: **~3 seconds**. Our concurrency was completely destroyed!

**The Takeaway:**
If you place a synchronous, blocking function (like `time.sleep()`, heavy mathematical computations, or `requests.get()`) inside an `async` function, it *starves the event loop*. Since the event loop is just a loop running on a single thread, blocking the thread blocks the entire loop. No context-switching can execute, and your program becomes forcefully sequential. 
To achieve concurrency, **all I/O bound waiting points inside coroutines must be non-blocking `await` calls.**
