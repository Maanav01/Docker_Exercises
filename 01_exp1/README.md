# 🚀 DockerLab1 - Hello World Container

This is a minimal Docker project demonstrating the basics of containerization using Python. It includes a simple script that prints "hello" to the console inside a Docker container.

---

## 📁 Project Structure

```
DockerLab1/
├── Dockerfile        # Docker image definition
├── hello.py          # Python script that prints 'hello'
└── README.md         # Project documentation
```

---

## ⚙️ Prerequisites

- Docker installed on your system → [Install Docker](https://docs.docker.com/get-docker/)

---

## 🛠️ Steps to Run

### 📦 1. Clone the Repository

```bash
git clone https://github.com/Maanav01/Docker_Exercises.git
cd Docker_Exercises/DockerLab1
```

### 🧱 2. Build the Docker Image

```bash
docker build -t hello .
```
![Screenshot from 2025-04-18 15-38-23](https://github.com/user-attachments/assets/93e2b0c1-3208-4b7b-9918-719996db5f3d)


### 🚀 3. Run the Container

```bash
docker run hello
```

✔️ Output should display:

```
hello
```

---

## 📜 Dockerfile Used

```Dockerfile
FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR .

COPY hello.py .

CMD ["python", "hello.py"]
```

---

## 🧹 Clean Up

To see running containers:

```bash
docker ps
```

To stop a container:

```bash
docker stop <container_id>
```

To remove unused images:

```bash
docker image prune -a
```

---

## 🙌 Final Note

This lab provides a great first step in learning Docker.  
Feel free to modify, extend, or containerize your own scripts next!

Happy Containerizing! 🐳
