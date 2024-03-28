#!/usr/bin/env python3
import asyncio
async def countdown(name: str, seconds: int) -> int:
    for _ in seconds:
        print(seconds)
        await asyncio.sleep(1)
