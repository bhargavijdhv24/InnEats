from concurrent import futures
import grpc
import proto.food_pb2 as food_pb2
import proto.food_pb2_grpc as food_pb2_grpc
from common.db import db

orders_collection = db["orders"]

class FoodService(food_pb2_grpc.FoodServiceServicer):
    def PlaceOrder(self, request, context):
        # This is illustrative; in a real app you'd validate and persist order
        return food_pb2.OrderResponse(success=True, message="Order received (grpc)")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    food_pb2_grpc.add_FoodServiceServicer_to_server(FoodService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("gRPC server for food_service started on :50052")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
