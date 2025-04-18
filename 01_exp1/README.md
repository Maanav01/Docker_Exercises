🚀 Getting Started with Docker
🌟 Overview

This is a simple project designed to demonstrate containerization using Docker. It includes a Python script (hello.py) that prints "hello" to the console when executed inside a Docker container. This setup allows for easy deployment and environment consistency across different systems.
📂 Project Structure

📂
│── 📜 Dockerfile           # Defines the Docker image and installation steps
│── 🐍 hello.py             # Simple Python script that prints "hello"
│── 📖 README.md            # Project documentation

🔧 Prerequisites

Before you get started, make sure you have the following installed:

    🐳 Docker

🚀 Installation & Setup
1️⃣ Clone the Repository

git clone <repository_url>

2️⃣ Build the Docker Image

Docker will create an image based on the Dockerfile, which contains the necessary instructions to set up the environment and copy hello.py.

docker build -t hello .

3️⃣ Run the Docker Container

After building the image, you can run a container that will execute hello.py.

docker run hello

🛠️ How It Works

    The Dockerfile is based on a lightweight Python image (python:3-slim).
    It sets environment variables to optimize Python execution.
    It copies hello.py into the container.
    When the container starts, it runs python hello.py, printing "hello" to the console.

🔄 Stopping & Cleaning Up
Checking Running Containers

To view active Docker containers:

docker ps

To stop a running container:

docker stop <container_id>

Removing Unused Docker Images

If needed, clean up unnecessary images:

docker image prune -a

📜 Dockerfile

Below is the content of the Dockerfile used in this project:

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR .
COPY hello.py .

# During debugging, this entry point will be overridden. 
# For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "hello.py"]

🙌 Thank You!
Thank you for using DockerLab1! We hope this guide was helpful. If you have any questions or suggestions, feel free to reach out. Happy coding! 🚀
