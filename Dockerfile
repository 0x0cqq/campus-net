# syntax=docker/dockerfile:1
FROM node:18-alpine AS build_stage
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM python:3.10-alpine
COPY --from=build_Stage /usr/src/app/dist /app/dist
COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py
RUN ls -la /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python3", "main.py" ]
EXPOSE 5000