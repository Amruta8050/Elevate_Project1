# 🎬 Movie Recommendation System

## 📌 Project Overview

The **Movie Recommendation System** is a machine learning project that suggests movies to users based on movie genre similarity. The system analyzes movie genres and recommends the most similar movies to the one selected by the user.

This project demonstrates the use of **content-based filtering** and **cosine similarity** to build a simple recommendation engine.

---

## 🎯 Objective

The main objective of this project is to build a system that can:

* Take a movie as input from the user
* Analyze its genre features
* Recommend the top similar movies

---

## 🛠 Tools and Technologies Used

* Python
* Pandas
* Scikit-Learn
* Streamlit
* VS Code

---

## 📂 Project Structure

movie-recommendation-system
│
├── app.py              # Main application file
├── movies.csv          # Dataset containing movie information
├── requirements.txt    # Required Python libraries
└── README.md           # Project documentation

---



## 🧠 How the System Works

1. The dataset contains movie titles and their genres.
2. Genres are converted into numerical vectors using **CountVectorizer**.
3. The system calculates similarity between movies using **Cosine Similarity**.
4. When a user selects a movie, the system finds the most similar movies.
5. The top recommended movies are displayed in the web interface.

---

## 📊 Dataset

The project uses a movie dataset containing:

* Movie ID
* Movie Title
* Genres

This dataset is used to calculate similarity between movies.

---

## 🚀 Features

* Simple and interactive user interface
* Fast movie recommendations
* Genre-based similarity matching
* Built using machine learning techniques

---

## 📌 Future Improvements

* Use a larger dataset such as MovieLens
* Add movie posters and ratings
* Implement collaborative filtering
* Deploy the application online

---

## 📷 Demo

The system allows the user to select a movie and generates top recommended movies based on similarity.

---

## 👩‍💻 Author

Amruta Hadapad

---

##Outputs

