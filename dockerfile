# Use official Python image
FROM python:3.11

# Set working directory in the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the full project code
COPY . .

# Expose the default port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]