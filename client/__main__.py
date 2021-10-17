import asyncio
from proto import Point, GisCalcStub

from grpclib.client import Channel

channel = Channel("127.0.0.1", 8080)
client = GisCalcStub(channel)

async def main():
    route=[
        Point(latitude=35.658577, longitude=139.745451),
        Point(latitude=35.710063, longitude=139.81070),
        ]
    res = await client.route_length(route=route)
    print(f"Answer: {res.length}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
channel.close()
