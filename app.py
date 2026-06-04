import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러보세요!")

# 데이터베이스 (단어: 카테고리) - 완전 생소하고 신기한 키워드로 리뉴얼
search_data = {
    # 🌿 신비한 동식물 (상상도 못 한 생소한 실존 생물)
    "질럿 거미 (Micrathena sagittata)": "신비한 동식물", # 피카츄나 스타크래프트 질럿을 닮은 노란 뿔 거미
    "시페루스 파피루스": "신비한 동식물", # 고대 이집트 종이의 원료가 된 외계 식물처럼 생긴 풀
    "코코넛크랩": "신비한 동식물", # 쓰레기통을 부수고 다니는 거대한 외계 괴물 비주얼의 게
    "마타마타 거북": "신비한 동식물", # 낙엽이나 돌처럼 완벽하게 위장한 기괴한 외계 생명체 같은 거북이
    "스네이크헤드 구라미": "신비한 동식물", # 물 밖에서도 호흡하며 땅을 기어 다니는 생태계 파괴 물고기
    "인도보라색개구리": "신비한 동식물", # 평생을 땅속에 살다 일 년에 딱 2주만 지상으로 나오는 보라색 젤리 같은 개구리
    "바르바도스 실뱀": "신비한 동식물", # 세상에서 가장 작은, 펜치나 실처럼 생긴 눈 먼 뱀
    "우파루파 아홀로틀": "신비한 동식물", # 팔다리는 물론 뇌까지 스스로 재생하는 기묘한 도롱뇽
    
    # ✨ 구글 이스터에그 (치면 화면이 변하거나 숨겨진 기능 발동)
    "askew": "구글 이스터에그", # 화면이 오른쪽으로 삐딱하게 기울어짐
    "do a barrel roll": "구글 이스터에그", # 창이 360도 빙글 회전함
    "google gravity": "구글 이스터에그", # 중력이 적용되어 UI가 바닥으로 무너져 내림
    "zerg rush": "구글 이스터에그", # 화면의 글자들을 파괴하는 미니 게임 등장
    "blink html": "구글 이스터에그", # 검색 결과의 특정 글자들이 계속 깜빡거림
    "2025 PN7": "구글 이스터에그", # 구글 창에 달이 두 개 지나가는 최신 준위성 이스터에그
    "text adventure": "구글 이스터에그", # 구글 개발자 도구(F12) 창에서 숨겨진 텍스트 게임 실행
    "dvd video logo": "구글 이스터에그" # 구글 로고가 옛날 DVD 대기 화면처럼 화면 구석을 튕겨 다님
}

# 사이드바 카테고리 (구글맵 제외, 상시 노출)
st.sidebar.markdown("### 📂 카테고리 선택")
selected_category = st.sidebar.radio(
    "보고 싶은 분야를 선택하세요:",
    ["전체보기", "신비한 동식물", "구글 이스터에그"]
)

# 카테고리별 필터링
if selected_category == "전체보기":
    filtered_words = list(search_data.keys())
else:
    filtered_words = [word for word, cat in search_data.items() if cat == selected_category]

# 화면 리프레시 시 결과 증발을 막기 위한 세션 상태 유지
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = None
if "category" not in st.session_state:
    st.session_state.category = None

# 뽑기 버튼
if st.button("✨ 오늘의 검색어 뽑기", use_container_width=True):
    if filtered_words:
        st.session_state.chosen_word = random.choice(filtered_words)
        st.session_state.category = search_data[st.session_state.chosen_word]
    else:
        st.warning("선택한 카테고리에 데이터가 없습니다.")
        st.session_state.chosen_word = None
        st.session_state.category = None

# 추천 결과 출력 구조
if st.session_state.chosen_word:
    word = st.session_state.chosen_word
    cat = st.session_state.category
    
    st.markdown("---")
    st.info(f"🔮 **[{cat}] 오늘의 추천 키워드**\n\n### `{word}`")
    
    # 이제 구글맵이 빠졌으므로 모든 링크는 깔끔하게 구글 검색으로 통일!
    search_url = f"https://google.com{word}"
    st.link_button("👉 구글에서 정체 확인하기", search_url, type="primary", use_container_width=True)
