from domain.encode.deps import provide_encode_service
from domain.encode.services import EncodeService
from litestar import Controller, Request, Response, post
from litestar.di import Provide


class EncodeController(Controller):
    tags = ["Encodes"]
    dependencies = {
        "encode_service": Provide(provide_encode_service),
    }

    @post("/encode")
    async def encode(self, request: Request, encode_service: EncodeService) -> Response:
        form_data = await request.form()
        text = form_data.get("data", "")

        if not text:
            return Response(
                content="No data provided", media_type="text/plain", status_code=400
            )

        img_io = await encode_service.encode(text)

        return Response(content=img_io.read(), media_type="image/png")
