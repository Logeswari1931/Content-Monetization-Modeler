# 📊 YouTube Ad Revenue Prediction App

## 📝 Project Overview
This Streamlit web application predicts **YouTube Ad Revenue** based on various video performance metrics and audience engagement details.  
It uses a **Linear Regression model** trained on historical data to estimate potential ad revenue for a given set of inputs.

---

## ⚙️ Features
- Interactive Streamlit interface  
- Input fields for key numeric features such as:
  - Views  
  - Likes  
  - Comments  
  - Watch Time (minutes)  
  - Video Length (minutes)  
  - Subscribers  
  - Revenue per View  
  - Watch Time per View  
  - Watch-to-Length Ratio  
  - Engagement Rate  
- Dropdown menus for categorical features like:
  - Category (Tech, Gaming, Music, Lifestyle, Entertainment)  
  - Device (Mobile, Tablet, TV)  
  - Country (IN, US, UK, CA, DE)  
- Displays the **predicted ad revenue** instantly after clicking “Predict Ad Revenue”.

---

## 🧠 Model Information
- The app uses a **Linear Regression model** stored in the file:
  ```
  linear_regression_model.pkl
  ```
- The model expects input features that are **one-hot encoded** for categorical variables.

---

## 🖥️ Installation and Setup

### 1️⃣ Clone or Download the Project
```bash
git clone https://github.com/Logeswari1931/Content-Monetization-Modeler.git
cd Content-Monetization-Modeler
```

### 2️⃣ Install Dependencies
Make sure you have Python 3.8+ installed.  
Then install the required packages:
```bash
pip install streamlit pandas joblib
```

### 3️⃣ Run the App
If you see “Streamlit not recognized,” use one of these commands:
```bash
streamlit run app.py
# or (if Streamlit not found)
python -m streamlit run app.py
```

### 4️⃣ Access in Browser
Once running, the app will open automatically or can be accessed at:
```
http://localhost:8501
```

---

## 🧩 File Structure
```
.
├── app.py                     # Streamlit app file
├── linear_regression_model.pkl # Trained ML model
├── requirements.txt            # Dependencies (optional)
└── README.md                   # Project documentation
```

---

## 💡 Example Usage
1. Enter values such as Views, Likes, Watch Time, etc.  
2. Choose a category, device type, and country.  
3. Click **“Predict Ad Revenue”**.  
4. The app will display the estimated revenue in USD.

---

## 🧰 Tech Stack
- **Python**
- **Streamlit**
- **Pandas**
- **Joblib**
- **Scikit-learn** (for model training)

---

## 👩‍💻 Author
**Logeshwari P**  
📍 Pallikaranai, Chennai
