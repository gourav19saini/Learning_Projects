# Learning Projects

This repository is a collection of machine learning, deep learning, data science, and web deployment projects. Each project is stored as a separate folder under `projects/` so it can be explored and run independently.

## Repository Overview

- Total projects: 10
- Main languages and tools: Python, Flask, Django, Streamlit, scikit-learn, TensorFlow/Keras, pandas, NumPy, Jupyter Notebook
- Project types: regression, classification, recommendation systems, OCR, time-series forecasting, and deployed ML web apps
- Included assets: datasets, notebooks, trained model files, screenshots, demo media, and deployment files

## Projects

| Project | Category | Summary | Main Tech |
| --- | --- | --- | --- |
| [BIke-project_Deployment](projects/BIke-project_Deployment) | Regression / Deployment | Predicts old bike prices and includes a Flask-style web app with trained model artifacts. | Python, Flask, scikit-learn |
| [Population-Growth-Forecasting](projects/Population-Growth-Forecasting) | Forecasting / Dashboard | Forecasts country-level population growth and visualizes historical trends in a web dashboard. | Python, Flask, pandas, scikit-learn, Chart.js |
| [Movie-Recommendation-System](projects/Movie-Recommendation-System) | Recommendation System | Django-based movie recommender using content-based filtering and ML training utilities. | Python, Django, scikit-learn, pandas |
| [Stock_Price_Prediction](projects/Stock_Price_Prediction) | Deep Learning / Time Series | Predicts stock prices using historical data and LSTM-based deep learning models. | Python, TensorFlow/Keras, pandas, yfinance |
| [ml-project-1](projects/ml-project-1) | ML Practice | Collection of regression notebooks covering linear, polynomial, ridge, lasso, elastic net, and multi-linear regression. | Python, Jupyter, scikit-learn |
| [Text_recognizer](projects/Text_recognizer) | OCR | Demonstrates text extraction from images using EasyOCR and Pytesseract. | Python, EasyOCR, Pytesseract |
| [house-price-prediction](projects/house-price-prediction) | Regression | Predicts house prices using exploratory analysis and ML models such as linear regression and gradient boosting. | Python, Jupyter, pandas, scikit-learn |
| [Time-series-forecasting-using-Deep-Learning](projects/Time-series-forecasting-using-Deep-Learning) | Deep Learning / Forecasting | Compares MLP, CNN, LSTM, and hybrid deep learning models for time-series forecasting. | Python, TensorFlow/Keras, pandas, scikit-learn |
| [Spam-Classifier-Project](projects/Spam-Classifier-Project) | Classification / NLP | Classifies SMS and email messages as spam or not spam using NLP preprocessing and ML models. | Python, Flask, NLTK, scikit-learn |
| [Used_Car_Prediction](projects/Used_Car_Prediction) | Regression / Deployment | Predicts used car prices with a trained Random Forest model and web deployment files. | Python, Streamlit, scikit-learn |

## Folder Structure

```text
Learning_Projects/
  projects/
    BIke-project_Deployment/
    Population-Growth-Forecasting/
    Movie-Recommendation-System/
    Stock_Price_Prediction/
    ml-project-1/
    Text_recognizer/
    house-price-prediction/
    Time-series-forecasting-using-Deep-Learning/
    Spam-Classifier-Project/
    Used_Car_Prediction/
  .gitignore
  README.md
```

## How To Use

Clone this repository:

```bash
git clone https://github.com/gourav19saini/Learning_Projects.git
cd Learning_Projects
```

Open any project folder inside `projects/` and follow that project's own `README.md` or source files.

Typical Python project setup:

```bash
cd projects/<project-folder>
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run instructions differ by project. Some projects use Flask or Django apps, while others are Jupyter notebooks or standalone ML scripts.

## Notes

- Some folders include trained models, datasets, images, videos, and notebooks, so the repository size is larger than a code-only project.
- The individual projects were collected for learning and practice. Each project keeps its own structure, dependencies, and documentation.
- Generated files such as `__pycache__`, virtual environments, and notebook checkpoints are ignored through `.gitignore`.

## Suggested Learning Path

1. Start with `ml-project-1` and `house-price-prediction` for core regression practice.
2. Move to `Spam-Classifier-Project` for NLP classification.
3. Explore `Stock_Price_Prediction` and `Time-series-forecasting-using-Deep-Learning` for sequence modeling.
4. Study `BIke-project_Deployment`, `Used_Car_Prediction`, `Population-Growth-Forecasting`, and `Movie-Recommendation-System` to understand model deployment and web app structure.
5. Try `Text_recognizer` for OCR and image-to-text workflows.
