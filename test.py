import grpc
from proto import gisapp_pb2_grpc, gisapp_pb2

channel = grpc.insecure_channel('localhost:50051')
client = gisapp_pb2_grpc.GISCalcStub(channel)
req = gisapp_pb2.RouteLengthRequest()
res = client.RouteLength()
