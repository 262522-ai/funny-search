import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러보세요!")

# 데이터베이스 (단어: 카테고리) - 설명 없이 깔끔하게 단어만 매칭
search_data = {
    # 🌿 신비한 동식물
    "아이아이원숭이": "신비한 동식물",
    "나도독미나리": "신비한 동식물",
    "오리너구리": "신비한 동식물",
    "블롭피쉬": "신비한 동식물",
    
    # 🌍 구글맵 미스터리 (좌표 직접 연결)
    "30°32'43.0\"N 32°33'46.0\"E": "구글맵 미스터리", 
    "50°00'41\"N 110°06'47\"W": "구글맵 미스터리", 
    "33.836379, 151.080506": "구글맵 미스터리", 
    "-33.867886, -63.987": "구글맵 미스터리", 
    
    # ✨ 구글 이스터에그
    "askew": "구글 이스터에그",
    "do a barrel roll": "구글 이스터에그",
    "google gravity": "구글 이스터에그",
}

# 사이드바 카테고리 (라디오 버튼으로 화살표 없이 '상시 노출')
st.sidebar.markdown("### 📂 카테고리 선택")
selected_category = st.sidebar.radio(
    "보고 싶은 분야를 선택하세요:",
    ["전체보기", "신비한 동식물", "구글맵 미스터리", "구글 이스터에그"]
)

# 카테고리별 필터링
if selected_category == "전체보기":
    filtered_words = list(search_data.keys())
else:
    filtered_words = [word for word, cat in search_data.items() if cat == selected_category]

# 뽑기 버튼
if st.button("✨ 오늘의 검색어 뽑기"):
    if filtered_words:
        chosen_word = random.choice(filtered_words)
        category = search_data[chosen_word] # 뽑힌 단어의 카테고리 확인 (기준)
        
        # 화면에는 단어만 깔끔하게 표시
        st.success(f"**추천 결과: {chosen_word}**")
        
        # [핵심 기준] 카테고리가 구글맵 미스터리면 구글 지도로, 아니면 일반 검색으로!
        if category == "구글맵 미스터리":
            map_url = f"https://www.google.com/maps/search/{chosen_word}"
            st.link_button("📍 구글 지도로 바로 확인하기", map_url)
        else:
            search_url = f"https://www.google.com/search?q={chosen_word}"
            st.link_button("👉 구글에서 정체 확인하기", search_url)
    else:
        st.warning("선택한 카테고리에 데이터가 없습니다.")
