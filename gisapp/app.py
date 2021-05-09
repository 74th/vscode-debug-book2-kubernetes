from proto import Point, RouteLengthResponse, GisCalcBase, GisCalcStub
import pyproj
from grpclib.server import Server
from grpclib.client import Channel

geod = pyproj.Geod(ellps="WGS84")


class GisAPP(GisCalcBase):
    async def route_length(self, *, route: list["Point"] = []) -> RouteLengthResponse:

        lats: list[float] = [0.0] * len(route)
        lons: list[float] = [0.0] * len(route)
        for i, p in enumerate(route):
            lats[i] = p.latitude
            lons[i] = p.longitude
        l = geod.line_length(lons, lats)

        return RouteLengthResponse(l)

    async def serve(self, host: str, port: int):
        server = Server([self])
        await server.start(host, port)
        await server.wait_closed()


class GisAPPIntermediator(GisCalcBase):
    def __init__(self, down_stream_host: str, down_stream_port: int, point: Point):
        self._point = point
        self._down_stream_channel = Channel(down_stream_host, down_stream_port)
        self._down_stream = GisCalcStub(self._down_stream_channel)

    async def route_length(self, *, route: list["Point"] = []) -> RouteLengthResponse:

        route.append(self._point)

        return await self._down_stream.route_length(route=route)

    async def serve(self, host: str, port: int):
        server = Server([self])
        await server.start(host, port)
        await server.wait_closed()
