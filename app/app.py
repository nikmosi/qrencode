from io import BytesIO
from pathlib import Path

import qrcode
from litestar import Litestar, Request, Response, get, post
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin
from litestar.response import Template
from litestar.template.config import TemplateConfig


@get("/")
def home() -> Template:
    return Template(template_name="index.html")


@post("/encode")
async def encode(request: Request) -> Response:
    form_data = await request.form()
    text = form_data.get("data", "")

    if not text:
        return Response(
            content="No data provided", media_type="text/plain", status_code=400
        )

    # Генерируем QR-код
    qr = qrcode.make(text)
    img_io = BytesIO()
    qr.save(img_io)
    img_io.seek(0)

    return Response(content=img_io.read(), media_type="image/png")


@get("/live_status")
async def hello_world() -> str:
    return "Hello, world!"


app = Litestar(
    [hello_world, home, encode],
    openapi_config=OpenAPIConfig(
        title="My API",
        description="This is the description of my API",
        render_plugins=[SwaggerRenderPlugin()],
        version="0.1.0",
        path="/docs",
    ),
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
    ),
)
