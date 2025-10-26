# Portfolio Growth Simulator

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-brightgreen)
![MIT License](https://img.shields.io/badge/License-MIT-green)

A Streamlit web app that simulates long-term investment growth using compound interest, weekly contributions, and market volatility.

---

## App Screenshots

<b>CSV Upload Interface</b><br>
<img src="images/upload_v2.png" width="700"><br><br>
<b>Cleaned Portfolio View</b><br>
<img src="images/portfolio.png" width="700"><br><br>
<b>Simulation Settings Panel</b><br>
<img src="images/sliders.png" width="700"><br><br>
<b>Portfolio Growth Chart</b><br>
<img src="images/chart.png" width="700">


---

## How It Works

1. Upload your portfolio as a CSV file
2. Set your weekly investment amount, expected annual growth rate, and volatility level
3. The app simulates future value using compound growth and optional market randomness
4. Choose to view either the full portfolio or individual stock projections
5. Results are visualized in an interactive chart with projected final values

---

## Features

- Upload your stock portfolio as a CSV  
- Adjust growth %, volatility, and contribution amount  
- View total portfolio or single stock projections  
- See raw, cleaned, and dropped data  
- Visualize compound growth across multiple years  
- (Coming soon) Export projection results  

---

## Sample Portfolio CSV

Use this file to test the app:  
[Download portfolio.csv](https://raw.githubusercontent.com/JorgeF123/portfolio-growth-simulator/main/data/portfolio.csv)


---

```csv
Ticker,Shares,Current Price
AAPL,10,195.12
MSFT,5,410.23
TSLA,8,870.50
```
## How to Run

```bash
git clone https://github.com/JorgeF123/portfolio-growth-simulator.git
cd portfolio-growth-simulator
pip install -r requirements.txt
streamlit run main.py
```

