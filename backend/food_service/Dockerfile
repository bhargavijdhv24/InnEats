FROM python:3.10-slim
WORKDIR /app
# Copy service files
COPY users_service/ /app
# Copy common folder
COPY common/ /app/common
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5002
CMD ["python", "app.py"]
