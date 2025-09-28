# InnEats – Hotel Booking & Food Ordering Platform

InnEats is a microservices-based platform for hotel room booking and food ordering with real-time updates.
Built using Flask, MongoDB, React.js, gRPC, Apache Kafka, and Docker.

## Quick start (local)
1. Install Docker & Docker Compose.
2. Clone this repo.
3. From project root run:
   ```bash
   docker-compose up --build
   ```
4. Access frontend: http://localhost:3000
   Users API: http://localhost:5005
   Hotels API: http://localhost:5006
   Food API: http://localhost:5007

## Structure
- backend/: Flask microservices (users, hotel, food)
- frontend/react-app: React UI
- grpc/proto: protobuf definitions
- kafka/: minimal utilities

