# 🍎 Fruit Quality Classifier — FreshHarvest AI System

An AI-powered **fruit freshness inspection system** built using **Streamlit**, designed to automate quality checks and reduce human error in warehouse operations such as those at **FreshHarvest Logistics**.

This application classifies fruits as **Good** or **Not Good** using image analysis.  
Users can upload images or capture them using their device camera, and the system instantly evaluates freshness.

---

# 📘 Project Background (FreshHarvest Use Case)

FreshHarvest Logistics is a mid-sized company distributing fresh fruits and vegetables across California.  
They supply produce to supermarkets and farmers' markets, striving for high-quality delivery standards.

### **📌 Challenges Identified**
From the FreshHarvest problem statement:

1. **Operational Inefficiency**  
   Manual inspections lead to human error, poor lighting issues, and worker fatigue.

2. **Business Losses**  
   Spoiled items slip through quality checks, leading to refunds, brand damage, and financial loss.

3. **Customer Complaints**  
   Retailers frequently report spoiled or overripe produce — especially **strawberries**, **tomatoes**, and **mangoes**.

### **💡 AI-Based Proposed Solution**
The company plans to install **high-speed cameras** on conveyor belts.  
A deep learning model will classify fruit crates in real-time as **Fresh** or **Spoiled**.

This project simulates the frontend part of such a system through a user-friendly Streamlit app.

---

# 🌐 Live Demo  
Experience the AI model in action:

👉 **https://fruit-classifier-mo8b7j6pmflf9vredqgeqh.streamlit.app/**

---

# 🚀 Features

- 🖼️ Upload or capture fruit images  
- 🤖 Real-time AI-based fruit freshness detection  
- 📊 Confidence score + detailed analysis  
- 🎨 Elegant and responsive UI with custom styling  
- 🚦 Clear Good / Not Good classification result  
- 📌 Supports multiple fruit types (from FreshHarvest dataset)

---

# 🧠 Fruits Included (FreshHarvest Dataset)

The system supports 8 fruits/vegetables from the problem statement:

- 🍌 Banana  
- 🍋 Lemon  
- 🥝 Lulo  
- 🥭 Mango  
- 🍊 Orange  
- 🍓 Strawberry  
- 🍅 Tomato  
- 🍈 Tamarillo  

---

# 🧩 Technologies Used

- **Python 3.8+**  
- **Streamlit** — Web UI  
- **TensorFlow / Keras** — Deep learning model (plug & play ready)  
- **Pillow (PIL)** — Image processing  
- **NumPy** — Numerical operations  
- **OpenCV** (optional, can be replaced with PIL resize)  

---

# 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/fruit-quality-classifier.git
cd fruit-quality-classifier
```

### 2️⃣ Create a Virtual Environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App
```bash
streamlit run app.py
```

---

# 🖥️ How It Works

1. User uploads or captures a fruit image  
2. Image is preprocessed (resized, normalized)  
3. AI model predicts freshness  
4. Result shown with:  
   - Predicted class  
   - Confidence score  
   - Detailed interpretation  
   - Visual indicators (colors, animations)

---

# 📸 Example Output

### Example Screenshots

![Screenshot 1](https://github.com/OmThawaregitgub/Fruit-classifier/blob/master/Images/Screenshot%20(399).png)

![Screenshot 2](https://github.com/OmThawaregitgub/Fruit-classifier/blob/master/Images/Screenshot%20(401).png)

---

# 🧠 Model Integration Guide

The app currently uses a **demo prediction**.  
To integrate your real AI model:

1. Save your trained model (e.g., `fruit_model.h5`) in the project directory  
2. Update the `load_model()` function inside `FruitQualityClassifier`  
3. Modify the `predict()` method to call the model's inference  
4. Ensure input shape matches your model (e.g., 224×224×3)

---

# 📂 Folder Structure

```
fruit-quality-classifier/
│
├── app.py                 # Main Streamlit application
├── model/                 # Folder for trained model (optional)
├── images/                # Screenshots / input samples
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

# 🧑‍💻 Author

**Om Thaware**  
📧 othaware175@gmail.com   
🔗 LinkedIn: www.linkedin.com/in/om-thaware 

---

# 📜 License

This project is distributed under the **MIT License**.  
You are free to use, modify, and distribute the software.

---

### ⭐ If you found this useful, please give the repository a star!  
Built with ❤️ using **Streamlit**.

