# JWT Proxy Server Using FastAPI
import os
import time
from datetime import datetime, timedelta
from uuid import uuid4

import jwt
import httpx
from fastapi import FastAPI, Request, Response

# Initialize FastAPI

app = FastAPI()

# Start time of the server
start_time = time.time()

# Total number of requests processed by the server
total_requests = 0

# JWT secret key
jwt_secret = os.getenv("JWT_SECRET",
                       "a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf")

# URL to post the request
post_url = os.getenv("POST_URL", "https://postman-echo.com/post")


# Route for the /status endpoint
@app.get("/status")
async def status_check():
    global total_requests
    # Time elapsed since the server started
    uptime = time.time() - start_time
    # Return uptime and number of requests processed by the server
    return f"{total_requests} requests processed, Uptime: {uptime}"


# Route for the root endpoint
@app.post("/")
async def process_request(request: Request):
    # Increment the number of requests processed
    global total_requests
    total_requests += 1

    # Data to be included in the JWT token
    data = {
        "iat": datetime.utcnow(),
        "jti": str(uuid4().hex),
        "user": "username",
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
    }

    # Encode the data into JWT token
    jwt_token = jwt.encode(data, jwt_secret, algorithm="HS512")

    # Send a post request to the specified URL
    async with httpx.AsyncClient() as client:
        response = await client.post(
            post_url,
            data=await request.json(),
            headers={"x-my-jwt": jwt_token, "content-type": request.headers["content-type"]},
        )

    # Return the response from the post request
    return Response(status_code=response.status_code, content=response.content, headers=response.headers)
