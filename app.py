import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")

# 데이터베이스 (검색어: 카테고리)
search_data = {
    # 1. 초면인 생물
    "아이아이원숭이": "초면인 생물",
    "나도독미나리": "초면인 생물",
    "느시": "초면인 생물",
    "심해용각류": "초면인 생물",
    "질경이이끼벌레": "초면인 생물",
    "시시포스쇠똥구리": "초면인 생물",
    "귀신고기": "초면인 생물",
    
    # 2. 구글 이스터에그
    "askew": "구글 이스터에그",
    "do a barrel roll": "구글 이스터에그",
    "google pacman": "구글 이스터에그",
    
    # 3. 구글맵 미스터리
    "30°32'43.0\"N 32°33'46.0\"E": "구글맵 미스터리",
    "51°50'55.0\"N 0°33'15.9\"W": "구글맵 미스터리",
}

# 사이드바 카테고리 선택
categories = ["전체보기", "초면인 생물", "구글 이스터에그", "구글맵 미스터리"]
selected_category = st.sidebar.selectbox("카테고리를 선택하세요", categories)

# 카테고리별 필터링
if selected_category == "전체보기":
    filtered_words = list(search_data.keys())
else:
    filtered_words = [
        word for word, cat in search_data.items() if cat == selected_category
    ]

# 뽑기 버튼
if st.button("✨ 뽑기"):
    if filtered_words:
        # 무작위 단어 선정
        chosen_word = random.choice(filtered_words)

        # 화면에는 오직 단어만 깔끔하게 표시
        st.success(f"**{chosen_word}**")

        # 구글 검색 이동 버튼
        search_url = f"https://www.google.com/search?q={chosen_word}"
        st.link_button("👉 구글에서 정체 확인하기", search_url)
    else:
        st.warning("선택한 카테고리에 단어가 없습니다.")
