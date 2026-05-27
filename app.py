import random
import streamlit as st

st.title("🔍 재밌는 검색어 추천기")
keywords = ["do a barrel roll", "askew", "구글 은하수"]

if st.button("✨ 뽑기"):
    st.success(random.choice(keywords))
