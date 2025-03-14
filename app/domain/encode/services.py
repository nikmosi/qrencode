from io import BytesIO

import qrcode
from async_executor import AsyncProcessExecutor


class EncodeService:
    def __init__(self, executor: AsyncProcessExecutor) -> None:
        self.executor = executor

    def _encode(self, text: str) -> BytesIO:
        qr = qrcode.make(text)
        img_io = BytesIO()
        qr.save(img_io)
        img_io.seek(0)
        return img_io

    async def encode(self, text: str) -> BytesIO:
        return await self.executor.run(self._encode, text)
