import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러보세요!")

# 데이터베이스 (단어: 카테고리) - 가짜 단어 삭제 및 요청 사항 완벽 반영
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
    "grogu": "구글 이스터에그",
    
    # 👻 인터넷 미스터리 & 괴담
    "백룸 The Backrooms": "인터넷 미스터리 & 괴담",
    "사다코 패러독스": "인터넷 미스터리 & 괴담",
    "유튜브 666": "인터넷 미스터리 & 괴담",
    "타임머신 설계도 존 티토": "인터넷 미스터리 & 괴담",
    "시카다 3301": "인터넷 미스터리 & 괴담",
    "셀린 디온 역재생 괴담": "인터넷 미스터리 & 괴담",

    # 🧠 [NEW] 지식 만렙 챌린지 (긴 원소, 긴 단어, 생소한 순우리말만 엄선)
    "오가네손": "지식 만렙 챌린지", # 주기율표의 가장 마지막(118번)이자 이름이 가장 긴 방사성 원소
    "프라세오디뮴": "지식 만렙 챌린지", # 발음하기 어렵고 생소한 은백색 희토류 금속 원소
    "티틴 단백질 풀네임": "지식 만렙 챌린지", # 글자 수만 189,819자에 달하는 세상에서 가장 긴 단어
    "타우마타와카탕이한가코아우아우오타마테아트투리푸카카피키마운가호로누쿠포카이व्": "지식 만렙 챌린지", # 뉴질랜드에 있는 세계에서 가장 이름이 긴 언덕 (85글자)
    "아리아리": "지식 만렙 챌린지", # '길을 찾아 나아가다'라는 뜻을 가진 매우 생소하고 이쁜 순우리말
    "안다미로": "지식 만렙 챌린지", # '담은 것이 그릇에 넘치도록 많이'라는 뜻을 가진 신기한 순우리말
    "시나브로": "지식 만렙 챌린지", # '모르는 사이에 조금씩 조금씩'이라는 뜻을 가진 아름다운 순우리말
    "윤슬": "지식 만렙 챌린지" # '햇빛이나 달빛에 비치어 반짝이는 잔물결'을 뜻하는 생소하고 서정적인 순우리말
}

# 사이드바 카테고리 (새 카테고리 이름 업데이트)
st.sidebar.markdown("### 📂 카테고리 선택")
selected_category = st.sidebar.radio(
    "보고 싶은 분야를 선택하세요:",
    ["전체보기", "신비한 동식물", "구글 이스터에그", "인터넷 미스터리 & 괴담", "지식 만렙 챌린지"]
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

# 뽑기 및 밀착형 결과창 컨테이너
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

    # 추천 결과 출력 (간격 밀착형 구조 완벽 유지)
    if st.session_state.chosen_word:
        word = st.session_state.chosen_word
        cat = st.session_state.category
        
        st.info(f"🔮 **[{cat}]**")
        st.code(word, language="")

