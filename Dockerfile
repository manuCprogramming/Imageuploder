# Use official Python image as base
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create media directory and set permissions
RUN mkdir -p /app/media/mediamyimage && chmod -R 755 /app/media

# Expose the port the app runs on
EXPOSE 8000

# Command to start Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]