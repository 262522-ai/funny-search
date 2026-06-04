import random
import urllib.parse
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러보세요!")

# 데이터베이스 (단어: 카테고리)
search_data = {
    # 🌿 초희귀 신비한 동식물
    "심해 천사고기 Clione": "신비한 동식물",
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
    
    # URL 세부 처리: 공백이나 한글 깨짐을 완벽 방지하는 표준 인코딩 적용
    encoded_word = urllib.parse.quote_plus(word)
    search_url = f"https://google.com{encoded_word}"
    
    # 🎯 [핵심 변경] st.link_button의 오류를 우회하기 위해 마크다운 HTML 직접 인젝션 사용
    # target="_blank"와 rel="noopener noreferrer" 속성으로 온전한 주소창 새 탭 이동을 보장합니다.
    st.markdown(
        f"""
        <a href="{search_url}" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
            <div style="
                background-color: #FF4B4B;
                color: white;
                padding: 10px 20px;
                text-align: center;
                border-radius: 8px;
                font-weight: bold;
                cursor: pointer;
                box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
            ">
                👉 구글에서 정체 확인하기 (새 창)
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
