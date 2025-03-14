import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable


class AsyncProcessExecutor:
    def __init__(self, max_workers: int = 8) -> None:
        self._executor = ThreadPoolExecutor(max_workers=max_workers)

    async def run(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            self._executor, _run_helper, func, args, kwargs
        )


def _run_helper(func, args, kwargs):
    return func(*args, **kwargs)
