# @author Mohan Sharma
import os
import sys

from com.crack.snap.make import services, utils, routes, model
from com.crack.snap.make.containers import Container

container = Container()

# Set the environment based on user input
container.env.override(
	lambda: os.environ.get("APP_ENV", "dev")
)

# Wire the container to allow it to inject dependencies in all modules
container.wire(modules=[sys.modules[__name__], utils, routes, services, model])
