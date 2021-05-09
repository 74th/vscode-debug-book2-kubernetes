import argparse
import asyncio
from proto import Point
from .app import GisAPP, GisAPPIntermediator

parser = argparse.ArgumentParser()
parser.add_argument("--down", default=None)
parser.add_argument("--host", default="0.0.0.0:8080")
parser.add_argument("--pos", default="35.6802117,139.7576692")
args = parser.parse_args()

host, port = args.host.split(":")

loop = asyncio.get_event_loop()

if args.down is not None:
    down_host, down_port = args.down.split(":")
    lat, lon = map(float, args.pos.split(","))
    app1 = GisAPPIntermediator(down_host, down_port, Point(lat, lon))
    loop.run_until_complete(app1.serve(host, port))
else:
    app2 = GisAPP()
    loop.run_until_complete(app2.serve(host, port))
