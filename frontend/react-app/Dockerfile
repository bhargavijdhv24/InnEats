FROM node:18

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy all frontend source code
COPY . .

EXPOSE 3000
CMD ["npm", "start"]
