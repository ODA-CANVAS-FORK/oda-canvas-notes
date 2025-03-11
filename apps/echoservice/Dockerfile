FROM python:3.12-alpine


RUN apk update && \
    apk add bash curl jq

# Copy the current directory contents into the container at /app
COPY /app /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

ARG SOURCE_DATE_EPOCH
ENV SOURCE_DATE_EPOCH $SOURCE_DATE_EPOCH
ARG GIT_COMMIT_SHA
ENV GIT_COMMIT_SHA $GIT_COMMIT_SHA
ARG CICD_BUILD_TIME
ENV CICD_BUILD_TIME $CICD_BUILD_TIME

# Run app.py when the container launches
CMD python -u app.py
