# 📈 From Static to Dynamic: My Real-Time Pricing Engine


![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive_App-ff4b4b?style=flat&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Deployed_&_Live-success)

## 👋 The "Why" Behind This Project
As an MBA student specializing in Business Analytics, I've always been fascinated by a simple question: **"Why do Uber and Amazon change their prices every minute, while most retailers only change them once a season?"**

I wanted to move beyond theory and build a tool that actually *does* this.

My goal was to create a **Dynamic Pricing Engine** that acts like a digital analyst—constantly watching demand trends and competitor moves to set the perfect price in real-time.

---

## 🚀 See It In Action
I deployed this project as a live web application so you can play with the market simulation yourself.

👉 **[Launch the Live Dashboard Here](https://share.streamlit.io/)**
*(If the app is sleeping, give it 30 seconds to wake up!)*

---

## 💡 The Business Problem
Most traditional retailers use "Cost-Plus Pricing" (e.g., *It cost $50, let's sell it for $70*).
**The flaw?** It's blind to the market.
* **Problem A:** When demand explodes (e.g., Black Friday), you run out of stock too fast and leave profit on the table.
* **Problem B:** When a competitor undercuts you by $1, you lose all your customers.

**My Solution:** An algorithm that prioritizes **Revenue** over static margins.

---

## 🔍 How I Built It (The Journey)

### Step 1: Real Data Analysis 📊
I didn't want to use fake numbers. I used the **Olist Brazilian E-Commerce Dataset** (100k+ real orders) and focused on the "Bed, Bath & Table" category.

### Step 2: Finding the "Magic Number" (Elasticity) 🧮
Using Python (Scipy), I ran a Linear Regression on the historical sales to find the **Price Elasticity of Demand (PED)**.

> **My Key Insight:** The model revealed a Price Sensitivity of **-0.64**.
> *Translation:* For every $1.00 I raised the price, I only lost 0.64 sales. This proved that customers were loyal enough that we could safely raise prices during surges to increase total revenue.

### Step 3: The Simulation Engine 🤖
I built a Python loop that acts as the "Server." It monitors two live signals:
1.  **Demand Pulse:** If traffic spikes >10%, the engine activates **Surge Pricing (+5%)**.
2.  **Competitor Watch:** If a rival drops their price, the engine intelligently **undercuts them by $0.50** to defend market share.

---

## 📸 Project Screenshots

| The Dashboard | The Elasticity Analysis |
|:---:|:---:|
| *<img width="270" height="368" alt="Screenshot 2025-12-06 204343" src="https://github.com/user-attachments/assets/edef480b-8a11-4d88-a1cb-53506eb627f9" />* | 
|*<img width="389" height="256" alt="image" src="https://github.com/user-attachments/assets/445bcb02-e49b-4a2e-ba66-c414fb25c6d7" />* |
| *Real-time revenue tracking* | *Calculating the demand curve* |

---

## 🛠️ Tech Stack & Tools Used
* **Python:** The core logic.
* **Streamlit:** For building the interactive frontend (no HTML/CSS needed!).
* **Pandas/NumPy:** For data wrangling and simulation math.
* **Scipy:** For the statistical regression models.

---

## 💻 How to Run This Locally
If you want to look at the code or run it on your own machine:

```bash
# 1. Clone this repository
git clone [https://github.com/your-username/pricing-engine-demo.git](https://github.com/your-username/pricing-engine-demo.git)

# 2. Go into the folder
cd pricing-engine-demo

# 3. Install the requirements
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
