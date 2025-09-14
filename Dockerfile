FROM node:18-alpine

# Environment variables with secrets
ENV DATABASE_URL=postgresql://user:docker_password_2024@db:5432/app
ENV API_KEY=sk_docker_1234567890abcdef1234567890abcdef
ENV JWT_SECRET=docker_jwt_secret_2024_very_long_and_secure
ENV AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
ENV AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

# Build arguments with secrets
ARG BUILD_SECRET=build_secret_2024
ARG NPM_TOKEN=npm_1234567890abcdef1234567890abcdef

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies using secret token
RUN npm config set //registry.npmjs.org/:_authToken=${NPM_TOKEN}
RUN npm install

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

# Start application
CMD ["node", "app.js"]
