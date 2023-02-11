# castLabs__python-programming-task
JWT proxy implementation using FastAPI which appends JWT token in the header, has docker and docker-compose infrastructure, a Makefile, and includes bonus features such as being asynchronous, providing a status endpoint with uptime and request count, and tests.

# Execute
- make build - build with docker
- make run - starts the proxy
- make test - Test if the required keys are present in the x-my-jwt header

# How it works
The main features of this implementation are the append of a JWT token in the x-my-jwt header. The bonus points of this implementation are the use of async and the provision of a "/status" endpoint, which returns the time since startup in seconds and the number of processed requests. To generate the JWT token, the code uses the python library jwt and retrieves the secret from the environment. The main functionality of the app is to accept a post request and forward it to a specified URL, adding the generated JWT token in the header.

The test file contains a single test case that checks if the required keys are present in the x-my-jwt header of the response. This test uses the FastAPI test client to post a JSON payload to the "/" endpoint and then verifies if the response status code is 200, and if the returned JSON contains the required data and the x-my-jwt header. The JWT token is decoded using the jwt library, and its contents are verified to contain the required keys. This test can be improved by mocking the post to postman-echo.com, the methods used to generate the date, jti, and user values, and asserting the correct values are returned in the x-my-jwt header.

