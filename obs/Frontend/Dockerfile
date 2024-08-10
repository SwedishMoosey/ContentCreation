# Base Image
FROM node:22-alpine3.19

# Set the working directory in the container
WORKDIR /app

# Copy packages to working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy rest of application to the working directory
COPY . .

# Build application
RUN npm run build

# Start application
ENV HOST=0.0.0.0 PORT=3000 NODE_ENV=development
CMD ["npx", "next", "dev"]