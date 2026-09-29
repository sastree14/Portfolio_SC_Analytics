import streamlit as st

st.set_page_config(page_title="SC-18 Credit Decision Review", layout="wide")
st.title("Credit Risk & Profit Optimization")

pd_value = st.slider("Probability of default", 0.0, 0.30, 0.07, 0.005)
amount = st.number_input("Exposure", min_value=1000.0, value=25000.0, step=1000.0)
rate = st.slider("Annual rate", 0.01, 0.30, 0.11, 0.005)
lgd = st.slider("Loss given default", 0.0, 1.0, 0.45, 0.05)
funding = st.slider("Funding cost", 0.0, 0.20, 0.035, 0.005)

revenue = amount * rate
expected_loss = amount * pd_value * lgd
funding_cost = amount * funding
contribution = revenue - expected_loss - funding_cost

c1, c2, c3 = st.columns(3)
c1.metric("Expected revenue", f"{revenue:,.0f}")
c2.metric("Expected loss", f"{expected_loss:,.0f}")
c3.metric("Expected contribution", f"{contribution:,.0f}")

decision = "Approve" if contribution > 0 and pd_value <= 0.12 else "Review"
st.subheader(f"Suggested decision: {decision}")
st.caption("Public review interface using representative assumptions. Policy thresholds are configurable.")
