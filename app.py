import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="ABC Tea Stall", page_icon="☕")

# --- PRICING DATA ---
PRICES = {
    "Base": {
        "Water 💧": 0, 
        "Milk 🥛": 10, 
        "Half Water 💧 & Half Milk 🥛": 15, 
        "Plant-Based Milk 🌴": 25, 
        "Condensed Milk (Dessert Style) 🍯": 20
    },
    "Specialty": {
        "None ❌": 20, 
        "Kashmiri Chai 🏔️": 60, 
        "Irani Chai 🇮🇷": 50, 
        "Tandoori Chai 🏺": 55, 
        "Cutting Chai (Mumbai Style) 🚉": 25, 
        "Butter Chai (Tibetan Style) 🧈": 65, 
        "Thai Iced Chai 🧊": 70, 
        "ABC Special Chai 🌟": 80
    },
    "Snacks": {
        "None ❌": 0, 
        "Samosa (2 pcs) 🥟": 30, 
        "Bun Maska 🥯": 45, 
        "Osmania Biscuits (4 pcs) 🍪": 20, 
        "Onion Pakoda 🧅": 40, 
        "Cheese Chilli Toast 🍞": 85
    }
}

# --- HEADER SECTION ---
st.title("Welcome to ABC Tea Stall 🏪")
st.markdown("### Where Chai Becomes an Adventure 🍃✨")

# --- SIDEBAR MENU ---
with st.sidebar:
    with st.expander("❓ How to Order"):
        st.info("""
        1. Enter your name.
        2. Pick your milk & tea type.
        3. Add snacks & quantity.
        4. Click 'Confirm' to brew!
        """)

    st.header("📋 Today's Menu")
    st.write("**Tea Bases** (Add-on price)")
    for item, price in PRICES["Base"].items():
        st.text(f"{item}: ₹{price}")
    st.divider()
    st.write("**Specialty Brews**")
    for item, price in PRICES["Specialty"].items():
        if item != "None ❌": st.text(f"{item}: ₹{price}")
    st.divider()
    st.write("**Tea-Time Snacks**")
    for item, price in PRICES["Snacks"].items():
        if item != "None ❌": st.text(f"{item}: ₹{price}")

# --- CUSTOMIZATION SECTION ---
st.header("🛠️ Customize your Order")
name = st.text_input("🧑‍🦰 Enter your name", placeholder="Chai Lover 💖")

col_a, col_b = st.columns(2)
with col_a:
    tea_base = st.selectbox("🥛 Choose Your Foundation", list(PRICES["Base"].keys()))
    special_chai = st.selectbox("✨ Specialty Brew", list(PRICES["Specialty"].keys()))
    cups = st.number_input("How many cups of tea?", min_value=1, max_value=20, step=1)

with col_b:
    flavour = st.selectbox("🌈 Flavor Profile", ["Plain 🍵", "Adrak 🫚", "Kesar 🌸", "Tulsi 🌿", "Mint 🍃"])
    snack = st.selectbox("🥐 Pair with a Snack", list(PRICES["Snacks"].keys()))
    
    # SNACK QUANTITY INPUT
    if snack != "None ❌":
        snack_qty = st.number_input(f"Quantity of {snack}", min_value=1, max_value=20, step=1)
    else:
        snack_qty = 0

# Descriptions logic
with st.expander("📖 View Chai Descriptions"):
    descriptions = {
        "Kashmiri Chai 🏔️": "Pink, salty-sweet tea with green tea, baking soda, and almonds.",
        "Irani Chai 🇮🇷": "Creamy, slow-cooked 'dum' tea with mawa richness.",
        "Tandoori Chai 🏺": "Brewed in a red-hot clay kulhad for a signature smoky taste.",
        "ABC Special Chai 🌟": "Our 2026 signature: 7 spices, gold-grade tea, and organic honey."
    }
    st.write(descriptions.get(special_chai, "Select a Specialty Chai to see its story!"))

# Add-ons
add_masala = st.toggle("Add Masala 🌶️ (+₹5)")
sugar = st.slider("Sugar level", 0, 10, 5)

# --- PRICE CALCULATION ---
# Tea Calculation
unit_tea_price = PRICES["Specialty"][special_chai] + PRICES["Base"][tea_base]
if add_masala: 
    unit_tea_price += 5
total_tea_cost = unit_tea_price * cups

# Snack Calculation
total_snack_cost = PRICES["Snacks"][snack] * snack_qty

# Grand Total
total_bill = total_tea_cost + total_snack_cost

st.divider()
st.subheader(f"💰 Total Amount: ₹{total_bill}")

# --- ORDER PROCESSING ---
if st.button("Confirm Order 🚀", use_container_width=True):
    with st.status("Brewing...", expanded=False) as status:
        st.write("🔥 Heating the stove...")
        time.sleep(1)
        st.write("🍃 Infusing spices...")
        time.sleep(1)
        status.update(label="✅ Order Confirmed!", state="complete")

    st.success(f"Cheers, {name if name else 'Chai Lover'}! Your tea is ready! 🥂")
    
    # Final Receipt
    st.divider()
    st.markdown(f"### 📜 Receipt for {name if name else 'Guest'}")
    c1, c2 = st.columns(2)
    with c1:
        st.write(f"**Tea:** {special_chai}")
        st.write(f"**Base:** {tea_base}")
        st.write(f"**Flavor:** {flavour}")
        st.write(f"**Snack:** {snack if snack != 'None ❌' else 'None'}")
    
    with c2:
        st.write(f"**Tea Qty:** {cups} (₹{total_tea_cost})")
        st.write(f"**Snack Qty:** {snack_qty} (₹{total_snack_cost})")
        st.markdown(f"## **Total: ₹{total_bill}**")

# FOOTER
st.markdown("---")
st.caption("ABC Tea Stall © 2026 | Handcrafted with ❤️ and Python")