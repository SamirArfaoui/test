#!/usr/bin/env python3

import asyncio

async def countdown(name: str, seconds: int) -> int:
    for i in range(seconds, 0, -1):
        print(f"{name}: {i} seconds remaining")
        await asyncio.sleep(1)
    print(f"{name}: Countdown finished")

async def main():
    timers = [
        asyncio.create_task(countdown("Timer 1", 5)),
        asyncio.create_task(countdown("Timer 2", 10)),
        asyncio.create_task(countdown("Timer 3", 3))
    ]
    await asyncio.gather(*timers)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")
