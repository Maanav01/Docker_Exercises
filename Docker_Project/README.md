# Machine Learning Analysis Streamlit App

This is a multi-page Streamlit application that demonstrates a complete machine learning pipeline using the Iris dataset. It includes dataset loading, model training, visualization, and SHAP values analysis for model explainability. The app is containerized using Docker for easy deployment.

## Features

- **Introduction**: Overview of the ML pipeline
- **Dataset Loading**: Load and explore the Iris dataset with basic statistics
- **Model Training**: Train a Random Forest Classifier with adjustable parameters
- **Visualization & SHAP**: Visualize feature importance and SHAP values for model interpretability
- Deployable via Docker for consistent environments

## Project Structure

```
├── app.py              # Main Streamlit application
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed and running
- Basic familiarity with Python and machine learning concepts

## Setup and Installation

1. **Clone the repository** or create the following files in a directory:
   - `app.py`
   - `Dockerfile`
   - `requirements.txt`

2. **Build the Docker image**:
   ```bash
   docker build -t ml-streamlit-app .
   ```
   ![1](https://github.com/user-attachments/assets/12471912-1200-4cab-addb-14d84ffdb5cc)

3. **Run the Docker container**:
   ```bash
   docker run -p 8501:8501 ml-streamlit-app
   ```
   ![2](https://github.com/user-attachments/assets/083095a1-735f-47aa-b63c-54089d15d943)

4. **Access the app**:
   Open your browser and navigate to `http://localhost:8501`.
   ![3](https://github.com/user-attachments/assets/e1619769-1d52-4b02-b360-52924a6420cd)
   ![4](https://github.com/user-attachments/assets/1b998bd1-66d6-43be-b3f5-05bdfd04ecbb)
   ![5](https://github.com/user-attachments/assets/c3b50d22-e215-4672-b90a-5e0ec37ca294)
   ![6](https://github.com/user-attachments/assets/ffa20a4d-6faa-47fc-a1fc-28bf73ecf1b6)


## Usage

- Use the sidebar to navigate between the four pages:
  - **Introduction**: Learn about the app's purpose and features
  - **Dataset Loading**: View the Iris dataset and its statistics
  - **Model Training**: Adjust parameters (test set size, number of trees) and train a Random Forest model
  - **Visualization & SHAP**: Explore feature importance and SHAP values for model explainability
- The app caches data and models for better performance.
- Model state is preserved using pickle to maintain consistency across pages.

## Dependencies

Key Python packages (specified in `requirements.txt`):
- streamlit==1.28.1
- pandas==2.1.1
- plotly==5.18.0
- numpy==1.26.1
- scikit-learn==1.3.2
- shap==0.44.0
- matplotlib==3.8.2

## Notes

- The Iris dataset is used for simplicity, but the app's structure supports other datasets with minor modifications.
- SHAP plots are rendered using matplotlib. Some complex SHAP visualizations may require additional tweaking for optimal display in Streamlit.
- Ensure Docker is running before executing the build and run commands.
- If you encounter issues, check the Docker logs for error messages:
  ```bash
  docker logs <container_id>
  ```

## Contributing

Feel free to fork this project and submit pull requests with improvements. For major changes, please open an issue to discuss your ideas.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact: demo@example.com
