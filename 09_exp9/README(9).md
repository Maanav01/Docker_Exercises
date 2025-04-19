# 🚀 Mastering Docker Deployment on AWS EC2 - A Complete Guide

Welcome to the comprehensive guide for deploying a Dockerized application on an AWS EC2 instance. Follow this structured approach to set up your environment, transfer necessary files, build a Docker image, and successfully run your application.

---

## 📌 Prerequisites
Before starting, ensure you have the following:

✔️ **AWS EC2 Instance** (Amazon Linux 2 recommended)  
✔️ **SSH Key Pair** (e.g., `vs-kp-1.pem` for secure access)  
✔️ **Docker Installed** on EC2  
✔️ **Required Files:**  
   - `Dockerfile` - Defines container image setup  
   - `app.py` - The application source code  
   - `requirements.txt` - Lists dependencies  
   - `mushrooms.csv` - Sample dataset for the application  

---

## 🛠 Step-by-Step Deployment Guide

### 1️⃣ Update the System
Keeping the system up-to-date ensures smooth operation:
```bash
sudo yum update -y
```

### 2️⃣ Install Docker
Enable and install Docker using Amazon Linux Extras:
```bash
sudo amazon-linux-extras enable docker
sudo yum install -y docker
```

### 3️⃣ Start and Enable Docker Service
Start Docker and ensure it runs automatically on reboot:
```bash
sudo service docker start
sudo systemctl enable docker
```

### 4️⃣ Create a Directory for Application Files
Organize your project files by creating a directory:
```bash
mkdir downloads
```

### 5️⃣ Transfer Files to EC2
Use SCP to securely transfer application files to the EC2 instance:
```bash
chmod 600 vs-kp-1.pem
scp -i vs-kp-1.pem Dockerfile app.py requirements.txt mushrooms.csv ec2-user@<EC2-Public-IP>:/home/ec2-user/downloads
```
👉 Replace `<EC2-Public-IP>` with your actual EC2 instance public IP.

### 6️⃣ Build the Docker Image
Navigate to the project directory and build the Docker image:
```bash
cd /home/ec2-user/downloads
sudo docker build -t my_app:v1.0 -f Dockerfile .
```

### 7️⃣ Run the Application in a Docker Container
Run the application inside a container, mapping port 8501:
```bash
sudo docker run -d -p 8501:8501 my_app:v1.0
```

---

## 🎯 Application Deployment Status
✅ Your application is successfully deployed and running on AWS EC2!  

### 🌐 Access the Application
Use the following link to access your application:
```
http://<EC2-Public-IP>:8501
```
👉 Replace `<EC2-Public-IP>` with your actual EC2 instance public IP.

---
### Result

![alt text](../dockerlab3/image-2.png)

---

## 🔧 Essential Docker Commands

### Check Running Containers
```bash
sudo docker ps
```

### View Container Logs
```bash
sudo docker logs <container-id>
```

### Stop the Container
```bash
sudo docker stop <container-id>
```

### Remove the Container (if needed)
```bash
sudo docker rm <container-id>
```

### Remove the Docker Image (if needed)
```bash
sudo docker rmi my_app:v1.0
```

---

## 🔍 Troubleshooting & Debugging
### 🔹 Docker Not Running?
Try restarting Docker:
```bash
sudo service docker restart
```

### 🔹 Unable to Access the Application?
1. Ensure your security group allows **inbound traffic on port 8501**.
2. Verify if the application is running:
   ```bash
   curl http://localhost:8501
   ```
3. Check logs for any errors:
   ```bash
   sudo docker logs <container-id>
   ```

---

## 🎉 Congratulations!
You have successfully deployed a Dockerized application on AWS EC2! 🎯 

🔗 **Further Learning:**
- [Docker Official Documentation](https://docs.docker.com/)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)

