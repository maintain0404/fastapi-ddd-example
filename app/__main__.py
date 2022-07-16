from functools import partial

from uvicorn import run as run_

from core.exc_handler import *  # noqa: F401, F403
from core.server import app  # noqa: F401
from handler import *  # noqa: F401, F403

from .config import DeployMode, config

run = partial(
    run_,
    app,
    host=config.APP_HOST,
    port=config.APP_PORT,
    loop="uvloop",
    http="httptools",
)


if config.DEPLOY_MODE == DeployMode.LOCAL:
    run(
        reload=True,
        debug=True,
    )
else:
    run()
