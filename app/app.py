from litestar import Litestar, get
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin


@get("/")
async def hello_world() -> str:
    return "Hello, world!"


app = Litestar(
    [hello_world],
    openapi_config=OpenAPIConfig(
        title="My API",
        description="This is the description of my API",
        render_plugins=[SwaggerRenderPlugin()],
        version="0.1.0",
        path="/docs",
    ),
)
