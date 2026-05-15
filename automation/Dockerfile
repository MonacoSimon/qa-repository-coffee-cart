FROM cypress/included:latest

WORKDIR /e2e

COPY cypress/package*.json ./
RUN npm ci

COPY cypress/ ./

CMD ["cypress", "run"]