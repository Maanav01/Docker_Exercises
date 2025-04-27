# 🌟 Machine Learning Analysis Streamlit App 🚀

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the **Machine Learning Analysis Streamlit App**! This interactive, multi-page web application showcases a complete machine learning pipeline using the Iris dataset 🌸. Built with Streamlit and containerized with Docker, it offers dataset exploration, model training, visualizations, and SHAP-based model explainability. Perfect for ML enthusiasts and beginners alike! 🎉

## ✨ Features

- **📖 Introduction**: Get an overview of the ML pipeline and app functionality
- **📊 Dataset Loading**: Explore the Iris dataset with interactive statistics
- **🧠 Model Training**: Train a Random Forest Classifier with customizable parameters
- **📈 Visualization & SHAP**: Dive into feature importance and SHAP values for model interpretability
- **🐳 Dockerized**: Run the app in a consistent, portable environment

## 🗂 Project Structure

```
├── 📜 app.py              # Core Streamlit application
├── 🐳 Dockerfile          # Docker configuration
├── 📋 requirements.txt    # Python dependencies
└── 📖 README.md           # You're here!
```

## 🛠 Prerequisites

- [Docker](https://www.docker.com/get-started) 🐳 installed and running
- Basic knowledge of Python 🐍 and machine learning concepts

## 🚀 Quick Start

Get the app up and running in just a few steps!

1. **Clone or create the project**:
   Ensure you have the following files in a directory:
   - `app.py`
   - `Dockerfile`
   - `requirements.txt`

2. **Build the Docker image**:
   ```bash
   docker build -t ml-streamlit-app .
   ```
   ![1](https://github.com/user-attachments/assets/12471912-1200-4cab-addb-14d84ffdb5cc)
   
3. **Run the container**:
   ```bash
   docker run -p 8501:8501 ml-streamlit-app
   ```
   ![2](https://github.com/user-attachments/assets/083095a1-735f-47aa-b63c-54089d15d943)
   
4. **Access the app**:
   Open your browser and visit 🌐 [http://localhost:8501](http://localhost:8501)
   ![3](https://github.com/user-attachments/assets/e1619769-1d52-4b02-b360-52924a6420cd)
   ![4](https://github.com/user-attachments/assets/1b998bd1-66d6-43be-b3f5-05bdfd04ecbb)
   ![5](https://github.com/user-attachments/assets/c3b50d22-e215-4672-b90a-5e0ec37ca294)
   ![6](https://github.com/user-attachments/assets/ffa20a4d-6faa-47fc-a1fc-28bf73ecf1b6)

## 🎮 Usage

Navigate through the app using the sidebar:
- **Introduction** 📖: Learn about the app's purpose and features
- **Dataset Loading** 📊: View the Iris dataset and its statistics
- **Model Training** 🧠: Tweak test set size and number of trees, then train a Random Forest model
- **Visualization & SHAP** 📈: Explore feature importance and SHAP values for model insights

The app uses caching for performance and saves model state with pickle for consistency across pages. 🗄

## 📦 Dependencies

Key packages (listed in `requirements.txt`):
- `streamlit==1.28.1` 🌐
- `pandas==2.1.1` 🐼
- `plotly==5.18.0` 📈
- `numpy==1.26.1` 🔢
- `scikit-learn==1.3.2` 🧠
- `shap==0.44.0` 🔍
- `matplotlib==3.8.2` 🎨

## ⚠️ Notes

- The Iris dataset 🌸 is used for simplicity, but the app's structure supports other datasets with minor tweaks.
- SHAP plots use matplotlib for rendering. Complex visualizations may need adjustments for optimal display.
- Ensure Docker is running before building or running the container.
- Debug issues by checking Docker logs:
  ```bash
  docker logs <container_id>
  ```

## 🤝 Contributing

We welcome contributions! 🙌 Fork the repo, make improvements, and submit a pull request. For major changes, please open an issue to discuss your ideas.

1. Fork the project 🍴
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request 📬

## 📜 License

This project is licensed under the [MIT License](LICENSE) 📄.

## 📬 Contact

Questions or feedback? Reach out at: **maanavsingh8433@gmail.com** ✉️

---

⭐ **Star this repo if you found it helpful!** ⭐

Built with ❤️ using Streamlit and Docker
