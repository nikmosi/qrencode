from async_executor import AsyncProcessExecutor
from domain.encode.services import EncodeService


async def provide_encode_service(process_executor: AsyncProcessExecutor):
    return EncodeService(process_executor)
