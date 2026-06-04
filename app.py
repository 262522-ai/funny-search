import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러보세요!")

# 데이터베이스 (단어: 카테고리)
search_data = {
    # 🌿 초희귀 신비한 동식물
    "무각거북고둥": "신비한 동식물",
    "화살표 미크라테나": "신비한 동식물",
    "스네이크스킨 구라미": "신비한 동식물",
    "마타마타 거북": "신비한 동식물",
    "인도보라색개구리": "신비한 동식물",
    "바르바도스 실뱀": "신비한 동식물",
    "레인보우 유칼립투스": "신비한 동식물",
    "넓적부리황새 슈빌": "신비한 동식물",
    
    # ✨ 구글 이스터에그
    "askew": "구글 이스터에그",
    "do a barrel roll": "구글 이스터에그",
    "google gravity": "구글 이스터에그",
    "chicxulub": "구글 이스터에그",
    "dart mission": "구글 이스터에그",
    "the wizard of oz": "구글 이스터에그",
    "grogu": "구글 이스터에그",
    
    # 👻 인터넷 미스터리 & 괴담
    "백룸 The Backrooms": "인터넷 미스터리 & 괴담",
    "사다코 패러독스": "인터넷 미스터리 & 괴담",
    "유튜브 666": "인터넷 미스터리 & 괴담",
    "타임머신 설계도 존 티토": "인터넷 미스터리 & 괴담",
    "시카다 3301": "인터넷 미스터리 & 괴담",
    "셀린 디온 역재생 괴담": "인터넷 미스터리 & 괴담",
}

# 사이드바 카테고리
st.sidebar.markdown("### 📂 카테고리 선택")
selected_category = st.sidebar.radio(
    "보고 싶은 분야를 선택하세요:",
    ["전체보기", "신비한 동식물", "구글 이스터에그", "인터넷 미스터리 & 괴담"]
)

# 카테고리별 필터링
if selected_category == "전체보기":
    filtered_words = list(search_data.keys())
else:
    filtered_words = [word for word, cat in search_data.items() if cat == selected_category]

# 세션 상태 유지 (결과 증발 방지)
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = None
if "category" not in st.session_state:
    st.session_state.category = None

# 🎯 [핵심 변경] 레이아웃 밀착 구조 생성
# 버튼과 결과창 사이의 간격을 최소화하기 위해 하나의 컨테이너로 묶어 배치합니다.
main_container = st.container()

with main_container:
    # 뽑기 버튼
    if st.button("✨ 오늘의 검색어 뽑기", use_container_width=True):
        if filtered_words:
            st.session_state.chosen_word = random.choice(filtered_words)
            st.session_state.category = search_data[st.session_state.chosen_word]
        else:
            st.warning("선택한 카테고리에 데이터가 없습니다.")
            st.session_state.chosen_word = None
            st.session_state.category = None

    # 추천 결과 출력 (버튼 바로 아래에 빈틈없이 배치)
    if st.session_state.chosen_word:
        word = st.session_state.chosen_word
        cat = st.session_state.category
        
        # 잔잔바리 텍스트와 구분선을 다 지우고 깔끔하게 결과 박스만 즉시 노출
        st.info(f"🔮 **[{cat}]**")
        st.code(word, language="")
