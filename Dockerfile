# Use an official Python runtime as a parent image
#FROM python:3
FROM tiangolo/uwsgi-nginx-flask:python3.6

# Set the working directory to /plank
WORKDIR /app

# Copy the current directory contents into the container at /plank
ADD ./plank /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# 5000 for flask if using python image
#EXPOSE 5000
# 80 if using uwsgi-nginx-flask image
EXPOSE 80

# used by flask
ENV FLASK_APP=plank.py
ENV FLASK_DEBUG=1

# used by uwsgi-nginx-flask docker
ENV STATIC_PATH /app/app/data/content
ENV STATIC_URL /content


# needed for flask, not for uwsgi-nginx-flask docker
# Run flask when the container launches
#CMD ["python", "plank.py"]
