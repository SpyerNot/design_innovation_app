import streamlit as st
st.header("Fitness app")
st.page_link("homepage.py", label="Home", icon="🏠")
st.page_link("pages/survey.py", label="Survey (Must do first)", icon="1️⃣")
st.page_link("pages/rewards.py", label="Rewards", icon="✨")
st.page_link("pages/games.py",label="Games",icon="🎮")
st.page_link("pages/friendlist.py",label="Friendlist",icon='💗')
st.divider()
