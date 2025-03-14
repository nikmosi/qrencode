from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin
from litestar.response import Template
from litestar.template.config import TemplateConfig
from litestar.di import Provide

from async_executor import AsyncProcessExecutor
from domain.encode.controller import EncodeController


@get("/")
def home() -> Template:
    return Template(template_name="index.html")


@get("/live_status")
async def hello_world() -> str:
    return "Hello, world!"


def provide_executor() -> AsyncProcessExecutor:
    return AsyncProcessExecutor(max_workers=8)


app = Litestar(
    [hello_world, home, EncodeController],
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
    dependencies={"process_executor": Provide(provide_executor)},
)
