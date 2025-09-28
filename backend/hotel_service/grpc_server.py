from concurrent import futures
import grpc
import proto.hotel_pb2 as hotel_pb2
import proto.hotel_pb2_grpc as hotel_pb2_grpc
from common.db import db
import os

hotels_collection = db["hotels"]

class HotelService(hotel_pb2_grpc.HotelServiceServicer):
    def CheckAvailability(self, request, context):
        # Note: _id in DB is an ObjectId; this example checks by 'id' string field for simplicity
        hotel = hotels_collection.find_one({"id": request.hotel_id})
        if hotel and hotel.get('rooms', {}).get(request.room_type, 0) > 0:
            return hotel_pb2.AvailabilityResponse(available=True, message="Room available")
        return hotel_pb2.AvailabilityResponse(available=False, message="Room not available")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hotel_pb2_grpc.add_HotelServiceServicer_to_server(HotelService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server for hotel_service started on :50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
