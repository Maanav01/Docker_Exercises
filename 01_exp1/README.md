# 🚀 Getting Started with Docker

## 🌟 Overview

This is a simple project designed to demonstrate containerization using Docker. It includes a lightweight Python script (`hello.py`) that prints `"hello"` to the console when executed inside a Docker container.

This setup provides:
- Easy deployment
- Environment consistency
- A perfect intro to Docker fundamentals

---

## 📂 Project Structure

📁 DockerLab1/ ├── 📜 Dockerfile # Defines the Docker image and execution instructions ├── 🐍 hello.py # Python script that prints "hello" └── 📖 README.md # Project documentation


---

## 🔧 Prerequisites

Before starting, ensure the following is installed on your system:

- 🐳 [Docker](https://docs.docker.com/get-docker/)

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository_url>
cd DockerLab1

2️⃣ Build the Docker Image

Build the image using the Dockerfile:

docker build -t hello .

3️⃣ Run the Docker Container

Run the container, which will execute hello.py inside:

docker run hello

🛠️ How It Works

    The Dockerfile uses the official python:3-slim image.

    Sets environment variables to optimize Python behavior inside the container.

    Copies hello.py into the image.

    The container runs python hello.py upon startup, printing hello in the console.

🔄 Stopping & Cleaning Up
Check Running Containers

docker ps

Stop a Container

docker stop <container_id>

Remove Unused Images

docker image prune -a

📜 Dockerfile Reference

FROM python:3-slim

# Keeps Python from generating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier logging
ENV PYTHONUNBUFFERED=1

WORKDIR .

COPY hello.py .

CMD ["python", "hello.py"]

🙌 Thank You!

Thanks for checking out DockerLab1!
If you found this helpful or have suggestions, feel free to contribute or reach out.

Happy Containerizing! 🐳🚀
