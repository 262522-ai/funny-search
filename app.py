import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러보세요!")

# 데이터베이스 (단어: 카테고리) - 데이터 추가 및 보완
search_data = {
    # 🌿 신비한 동식물
    "아이아이원숭이": "신비한 동식물",
    "나도독미나리": "신비한 동식물",
    "오리너구리": "신비한 동식물",
    "블롭피쉬": "신비한 동식물",
    "레인보우 유칼립투스": "신비한 동식물",
    "느시": "신비한 동식물",
    "둥근지느러미개치네래": "신비한 동식물",
    
    # 🌍 구글맵 미스터리 (정확한 좌표 및 특이 장소)
    "30°32'43.0\"N 32°33'46.0\"E": "구글맵 미스터리", # 수에즈 운반선 미스터리 구조물
    "50°00'41\"N 110°06'47\"W": "구글맵 미스터리", # 캐나다 배드랜드 가디언(인디언 얼굴)
    "33.836379, 151.080506": "구글맵 미스터리", # 호주 난파선 숲
    "-33.867886, -63.987": "구글맵 미스터리", # 아르헨티나 기타 모양 숲
    "45.1221, -123.1147": "구글맵 미스터리", # 파이어폭스 로고 밭
    "52.4798, 62.1857": "구글맵 미스터리", # 카자흐스탄 거대 오각별
    
    # ✨ 구글 이스터에그 (영어 소문자 검색 기준)
    "askew": "구글 이스터에그",
    "do a barrel roll": "구글 이스터에그",
    "google gravity": "구글 이스터에그",
    "zerg rush": "구글 이스터에그",
    "pacman": "구글 이스터에그",
    "tic tac toe": "구글 이스터에그",
    "blink html": "구글 이스터에그"
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

# 💡 화면 리프레시 시 결과 소멸을 막기 위한 세션 상태 초기화
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = None
if "category" not in st.session_state:
    st.session_state.category = None

# 뽑기 버튼 클릭 시 세션 상태에 저장
if st.button("✨ 오늘의 검색어 뽑기", use_container_width=True):
    if filtered_words:
        st.session_state.chosen_word = random.choice(filtered_words)
        st.session_state.category = search_data[st.session_state.chosen_word]
    else:
        st.warning("선택한 카테고리에 데이터가 없습니다.")
        st.session_state.chosen_word = None
        st.session_state.category = None

# 저장된 추천 결과가 있을 때만 화면에 출력
if st.session_state.chosen_word:
    word = st.session_state.chosen_word
    cat = st.session_state.category
    
    st.markdown("---")
    # 결과 상자 디자인
    st.info(f"🔮 **[{cat}] 오늘의 추천 키워드**\n\n### `{word}`")
    
    # [핵심 기준] 카테고리별 분기 처리하여 버튼 생성
    if cat == "구글맵 미스터리":
        map_url = f"https://www.google.com/maps/search/{word}"
        st.link_button("📍 구글 지도로 좌표 확인하기", map_url, type="primary", use_container_width=True)
    else:
        search_url = f"https://www.google.com/search?q={word}"
        st.link_button("👉 구글에서 정체 확인하기", search_url, type="primary", use_container_width=True)
