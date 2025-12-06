import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="MBA Dynamic Pricing", layout="wide")

# --- YOUR TRAINED MODEL (Hardcoded from Phase 2 Analysis) ---
# This mimics "loading a saved model" in a production environment
BASE_DEMAND = 61.72       # Your Intercept
PRICE_SENSITIVITY = 0.64  # Your Slope
BASE_PRICE = 75.07        # Your average historical price

# --- THE BRAIN (Functions) ---
def get_optimal_price(current_demand_factor, competitor_price):
    """
    Decides the price based on 'Live' market data.
    """
    # Start with the standard price
    dynamic_price = BASE_PRICE
    strategy_tag = "STABLE"
    
    # STRATEGY 1: Surge Pricing (If demand is high, raise price)
    if current_demand_factor > 1.10: # Demand is 10% higher than normal
        dynamic_price = BASE_PRICE * 1.05 # Raise price 5%
        strategy_tag = "🔥 SURGE PRICING"
        
    # STRATEGY 2: Competitive Response (If rival is cheaper, undercut them)
    elif competitor_price < BASE_PRICE:
        dynamic_price = competitor_price - 0.50 # Beat them by 50 cents
        strategy_tag = "⚔️ COMPETITOR UNDERCUT"
        
    return round(dynamic_price, 2), strategy_tag

def calculate_projected_revenue(price, demand_factor):
    # Formula: (Base_Demand - (Sensitivity * Price)) * External_Factor
    est_qty = (BASE_DEMAND - (PRICE_SENSITIVITY * price)) * demand_factor
    if est_qty < 0: est_qty = 0
    return round(est_qty * price, 2)

# --- THE FRONTEND (Streamlit) ---
st.title("⚡ Dynamic Pricing Engine")
st.markdown(f"""
**Project Status:** 🟢 Live Model Deployment  
**Model Parameters:** Price Elasticity: `{PRICE_SENSITIVITY}` | Base Demand: `{BASE_DEMAND}`  
**Objective:** Maximize revenue by adjusting to real-time competitor and demand signals.
""")

# Create Tabs
tab1, tab2 = st.tabs(["🚀 Live Simulation", "📊 Project Logic (About)"])

with tab1:
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.subheader("Control Panel")
        st.write("Adjust the market volatility:")
        speed = st.slider("Simulation Speed (Seconds)", 0.1, 2.0, 1.0)
        
        if st.button("▶️ Start Simulation (10 Days)"):
            
            # Initialize Session State for Charts
            chart_data = []
            
            # Layout Columns for Metrics
            m1, m2, m3, m4 = st.columns(4)
            place_demand = m1.empty()
            place_comp = m2.empty()
            place_price = m3.empty()
            place_rev = m4.empty()
            
            # Chart Placeholder
            chart_spot = st.empty()
            log_spot = st.empty()
            
            total_rev = 0
            
            # THE LOOP
            for day in range(1, 11):
                # 1. Simulate Market
                live_demand = np.random.uniform(0.8, 1.3)
                live_competitor = np.random.uniform(BASE_PRICE * 0.9, BASE_PRICE * 1.1)
                
                # 2. Get AI Decision
                my_price, reason = get_optimal_price(live_demand, live_competitor)
                
                # 3. Calculate Result
                revenue = calculate_projected_revenue(my_price, live_demand)
                total_rev += revenue
                
                # 4. Update Dashboard
                place_demand.metric("Demand Pulse", f"{live_demand*100:.0f}%")
                place_comp.metric("Competitor", f"${live_competitor:.2f}")
                place_price.metric("My Price", f"${my_price}", reason)
                place_rev.metric("Daily Revenue", f"${revenue:,.0f}")
                
                # 5. Update Chart
                chart_data.append({
                    "Day": day,
                    "My Price": my_price,
                    "Competitor Price": live_competitor
                })
                df_chart = pd.DataFrame(chart_data).set_index("Day")
                chart_spot.line_chart(df_chart)
                
                time.sleep(speed)
            
            st.success(f"Simulation Complete! Total Projected Revenue: ${total_rev:,.2f}")

with tab2:
    st.markdown("### How this works")
    st.write("This engine uses a Linear Regression model trained on Olist E-Commerce data.")
    st.latex(r''' Demand = \alpha - (\beta \times Price) ''')
    st.write(f"Where our $\\beta$ (sensitivity) is **{PRICE_SENSITIVITY}**.")
