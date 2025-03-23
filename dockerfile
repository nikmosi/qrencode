# Use the official Python 3.12.8 image as the base
FROM python:3.12.8-slim

# Set the working directory inside the container
WORKDIR /app

# Install uv (a fast Python package installer)
RUN pip install --no-cache-dir "uv==0.4.30"

# Copy the project files into the container
COPY ./app /app

# Install dependencies using uv
RUN uv sync --frozen

# Expose the port your app runs on (default for Litestar is 8000)
EXPOSE 8000

# Command to run your application
CMD ["uv", "run", "litestar", "run", "--host", "0.0.0.0", "--port", "8000"]
