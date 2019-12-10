"""HACS http endpoints."""
import os
from homeassistant.components.http import HomeAssistantView
from aiohttp import web
<<<<<<< HEAD
from hacs_frontend import locate_gz, locate_debug_gz
=======
from hacs_frontend import locate_gz
>>>>>>> 2d310d52fb4db0329ba3cad99ef1641f8c170705

from .hacsbase import Hacs


class HacsFrontend(HomeAssistantView, Hacs):
    """Base View Class for HACS."""

    requires_auth = False
    name = "hacs_frontend"
    url = r"/hacs_frontend/{requested_file:.+}"

    async def get(self, request, requested_file):  # pylint: disable=unused-argument
        """Handle HACS Web requests."""
<<<<<<< HEAD
        if self.configuration.debug:
            servefile = await self.hass.async_add_executor_job(locate_debug_gz)
            self.logger.debug("Serving DEBUG frontend")
        else:
            servefile = await self.hass.async_add_executor_job(locate_gz)
=======
        servefile = await self.hass.async_add_executor_job(locate_gz)
>>>>>>> 2d310d52fb4db0329ba3cad99ef1641f8c170705

        if os.path.exists(servefile):
            return web.FileResponse(servefile)
        return web.Response(status=404)


class HacsPluginView(HomeAssistantView, Hacs):
    """Serve plugins."""

    requires_auth = False
    name = "hacs_plugin"
    url = r"/community_plugin/{requested_file:.+}"

    async def get(self, request, requested_file):  # pylint: disable=unused-argument
        """Serve plugins for lovelace."""
        try:
            file = f"{self.system.config_path}/www/community/{requested_file}"

            # Serve .gz if it exist
            if os.path.exists(file + ".gz"):
                file += ".gz"

            if os.path.exists(file):
                self.logger.debug("Serving {} from {}".format(requested_file, file))
                response = web.FileResponse(file)
                response.headers["Cache-Control"] = "max-age=0, must-revalidate"
                return response
            else:
                self.logger.error(f"Tried to serve up '{file}' but it does not exist")

        except Exception as error:  # pylint: disable=broad-except
            self.logger.debug(
                "there was an issue trying to serve {} - {}".format(
                    requested_file, error
                )
            )

        return web.Response(status=404)
