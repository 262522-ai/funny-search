import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러보세요!")

# 데이터베이스 (단어: 카테고리) - 오즈의 마법사 삭제 및 초고난도 카테고리 추가
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
    
    # ✨ 구글 이스터에그 (오즈의 마법사 제거, 확실히 작동하는 효과만 엄선)
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

    # 🧠 [NEW] 어휘력 만렙 챌린지 (끝말잇기 무적, 겁나 긴/어려운 단어, 희귀 원소)
    "티틴 단백질 풀네임": "어휘력 만렙 챌린지", # 글자 수만 189,819자에 달하는 세상에서 가장 긴 단어
    "오가네손": "어휘력 만렙 챌린지", # 주기율표의 가장 마지막(118번)에 위치한 초헤비급 인공 방사성 원소
    "스트로보볼카노식 분화": "어휘력 만렙 챌린지", # 지구 과학이나 화산학에서 쓰이는 엄청나게 길고 생소한 전문 용어
    "산새카": "어휘력 만렙 챌린지", # 잎과 뿌리를 약재로 쓰는 사초과 식물로, 끝말잇기 '산' 공격을 방어하는 한방 단어
    "쁨나무": "어휘력 만렙 챌린지", # '쁨'으로 시작하는 유일무이한 표준 국어 단어로 끝말잇기 절대 무적 카드
    "타우마타와카탕이한가코아우아우오타마테아트투리푸카카피키마운가호로누쿠포카이व्": "어휘력 만렙 챌린지" # 뉴질랜드에 있는 세계에서 가장 이름이 긴 언덕 (85글자)
}

# 사이드바 카테고리 (신설 카테고리 반영)
st.sidebar.markdown("### 📂 카테고리 선택")
selected_category = st.sidebar.radio(
    "보고 싶은 분야를 선택하세요:",
    ["전체보기", "신비한 동식물", "구글 이스터에그", "인터넷 미스터리 & 괴담", "어휘력 만렙 챌린지"]
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

    # 추천 결과 출력 (간격 밀착형 구조 유지)
    if st.session_state.chosen_word:
        word = st.session_state.chosen_word
        cat = st.session_state.category
        
        st.info(f"🔮 **[{cat}]**")
        st.code(word, language="")
