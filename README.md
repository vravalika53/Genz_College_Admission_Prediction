# 🎓 GenZ College Admission Prediction using ANN

## 📌 Project Overview

The **GenZ College Admission Prediction** project uses an **Artificial Neural Network (ANN)** to predict whether a student is likely to be admitted to college based on academic performance, extracurricular activities, personal evaluation scores, and other student-related factors.

The model is trained as a **binary classification problem**, where:

* `0` → Not Admitted
* `1` → Admitted

The trained model is deployed using **Streamlit** to provide real-time admission predictions.

---

## 🎯 Business Problem

College admission teams need to evaluate a large number of student applications using multiple academic and personal factors. Manual evaluation can be time-consuming and may lead to inconsistent decisions.

This project aims to build a machine learning-based system that can assist admission teams by providing quick and data-driven admission predictions.

---

## 🎯 Project Objective

* Predict student admission status using ANN.
* Analyze important factors related to admission.
* Handle class imbalance using **Class Weights**.
* Improve model performance using **Optuna Hyperparameter Tuning**.
* Evaluate the model using Accuracy, Precision, Recall, and F1-Score.
* Deploy the trained model using **Streamlit**.

---

## 📊 Dataset

The dataset contains **500,000 student records** and **20 columns**.

### Features

| Feature                 | Description                            |
| ----------------------- | -------------------------------------- |
| `student_id`            | Unique student identification number   |
| `age`                   | Student's age                          |
| `gender`                | Student gender                         |
| `state`                 | Student's state                        |
| `family_income`         | Family annual income                   |
| `high_school_gpa`       | High school GPA                        |
| `sat_score`             | SAT examination score                  |
| `act_score`             | ACT examination score                  |
| `attendance_rate`       | School attendance percentage           |
| `ap_courses`            | Number of AP courses completed         |
| `extracurricular_count` | Number of extracurricular activities   |
| `volunteer_hours`       | Volunteer/community service hours      |
| `leadership_positions`  | Number of leadership positions         |
| `coding_projects`       | Number of coding projects              |
| `social_media_hours`    | Daily social media usage               |
| `online_certifications` | Number of online certifications        |
| `essay_score`           | Admission essay score                  |
| `recommendation_score`  | Recommendation score                   |
| `interview_score`       | Interview score                        |
| `admission_status`      | Target: 0 = Not Admitted, 1 = Admitted |

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Preprocessing
   ↓
Handle Class Imbalance
   ↓
Train-Test Split
   ↓
ANN Model Building
   ↓
Hyperparameter Tuning using Optuna
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Deployment
   ↓
Real-Time Prediction
```

---

## 🧠 ANN Model

The model uses multiple dense layers to learn complex relationships between student features and admission outcomes.

### Final Architecture

```text
Input Layer
     ↓
Dense Layer – 256 neurons
     ↓
Dropout + Regularization
     ↓
Dense Layer – 64 neurons
     ↓
Dropout + Regularization
     ↓
Dense Layer – 16 neurons
     ↓
Dropout + Regularization
     ↓
Output Layer – 1 neuron
     ↓
Sigmoid Activation
```

Since this is a binary classification problem, the final layer uses a **Sigmoid activation function**.

---

## ⚙️ Hyperparameter Tuning

**Optuna** was used to find suitable hyperparameters for the ANN.

### Best Hyperparameters

```text
n_layers       : 3
learning_rate  : 0.002589051569821834
batch_size     : 64
activation     : tanh
optimizer      : RMSprop

units_0        : 256
dropout_0      : 0.32249158778234854
regularization_0 : 1.7733264569678538e-05

units_1        : 64
dropout_1      : 0.1350107697754399
regularization_1 : 0.003884361395546827

units_2        : 16
dropout_2      : 0.3472068798420902
regularization_2 : 0.0006567032173762252
```

### Best Validation Accuracy

**81.12%**

---

## ⚖️ Handling Class Imbalance

The dataset contains an unequal number of students in the admission classes.

To prevent the model from favoring the majority class, **Class Weights** were used during model training.

This gives more importance to the minority class and helps improve the model's ability to identify both classes.

---

## 📈 Model Evaluation

The model was evaluated using:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-Score**
* **Confusion Matrix**

These metrics provide a better understanding of how well the model predicts both admitted and non-admitted students.

---

## 🚀 Model Deployment

The trained ANN model was deployed using **Streamlit**.

The application allows users to enter student details such as:

* GPA
* SAT Score
* ACT Score
* Attendance
* AP Courses
* Extracurricular Activities
* Leadership
* Coding Projects
* Essay Score
* Recommendation Score
* Interview Score

The application processes the inputs and provides an admission prediction.

```text
Student Details
      ↓
Preprocessor
      ↓
ANN Model
      ↓
Prediction
      ↓
Admitted / Not Admitted
```

---

## 💡 Key Business Insights

* Academic performance is an important factor in admission prediction.
* GPA, SAT, and ACT scores provide valuable information about academic performance.
* Essay, recommendation, and interview scores help evaluate the overall student profile.
* Extracurricular activities, leadership, volunteering, and certifications provide additional information about student potential.
* ANN can support faster and more consistent admission decision-making.
* The Streamlit application makes the prediction system easy to use in real time.

---

## ⚠️ Challenges

### 1. Class Imbalance

**Solution:** Used class weights during ANN training.

### 2. Model Overfitting

**Solution:** Used dropout and regularization.

### 3. Hyperparameter Selection

**Solution:** Used Optuna for automated hyperparameter tuning.

### 4. Large Dataset

**Solution:** Used appropriate preprocessing and batch-based ANN training.

### 5. Model Deployment

**Solution:** Saved the trained model and preprocessing object and integrated them with Streamlit.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* TensorFlow / Keras
* Optuna
* Streamlit
* Pickle
* Jupyter Notebook

---

## 📂 Project Structure

```text
GenZ_College/
│
├── app.py
├── architecture (1).keras
├── preprocessor (1).pkl
├── genz_college_admission_prediction.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Create and activate the environment

```bash
conda create -n genz python=3.11
conda activate genz
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit

Navigate to the project folder:

```bash
cd /d D:\DL\GenZ_College
```

Then run:

```bash
streamlit run app.py
```

---

## 📌 Conclusion

The **GenZ College Admission Prediction** project demonstrates how an Artificial Neural Network can be used to predict college admission outcomes from multiple student-related features. By using class weights, regularization, and Optuna hyperparameter tuning, the model achieved a **best validation accuracy of 81.12%**. The Streamlit deployment provides an easy-to-use interface for real-time predictions.

---

## 👩‍💻 Author

**Ravali**

Data Science | Machine Learning | Deep Learning | Generative AI
