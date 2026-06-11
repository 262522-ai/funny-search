import random
import streamlit as st
import urllib.parse
import streamlit.components.v1 as components   # ← 추가

# 1. 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")
st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러보세요!")

# 2. 데이터베이스
search_data = {
    "무각거북고둥": "신비한 동식물", "화살표 미크라테나": "신비한 동식물", "스네이크스킨 구라미": "신비한 동식물",
    "마타마타 거북": "신비한 동식물", "인도보라색개구리": "신비한 동식물", "바르바도스 실뱀": "신비한 동식물",
    "레인보우 유칼립투스": "신비한 동식물", "넓적부리황새 슈빌": "신비한 동식물",
    "askew": "구글 이스터에그", "do a barrel roll": "구글 이스터에그", "google gravity": "구글 이스터에그",
    "chicxulub": "구글 이스터에그", "dart mission": "구글 이스터에그", "grogu": "구글 이스터에그",
    "백룸 The Backrooms": "인터넷 미스터리 & 괴담", "사다코 패러독스": "인터넷 미스터리 & 괴담",
    "유튜브 666": "인터넷 미스터리 & 괴담", "타임머신 설계도 존 티토": "인터넷 미스터리 & 괴담",
    "시카다 3301": "인터넷 미스터리 & 괴담", "셀린 디온 역재생 괴담": "인터넷 미스터리 & 괴담",
    "풀무질": "우리말 만렙 챌린지", "오솔오솔": "우리말 만렙 챌린지", "한들한들": "우리말 만렙 챌린지",
    "아스라하다": "우리말 만렙 챌린지", "아련아련": "우리말 만렙 챌린지", "별무리": "우리말 만렙 챌린지",
    "달무리": "우리말 만렙 챌린지",
    "타우마타와카탕이한가코아우아우오타마테아트투리푸카카피키마운가호로누쿠포카이브": "우리말 만렙 챌린지"
}

# 3. 사이드바 카테고리
st.sidebar.markdown("### 📂 카테고리 선택")
selected_category = st.sidebar.radio(
    "보고 싶은 분야를 선택하세요:",
    ["전체보기", "신비한 동식물", "구글 이스터에그", "인터넷 미스터리 & 괴담", "우리말 만렙 챌린지"]
)

# 4. 카테고리별 필터링
if selected_category == "전체보기":
    filtered_words = list(search_data.keys())
else:
    filtered_words = [word for word, cat in search_data.items() if cat == selected_category]

# 5. 세션 상태 유지
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = None
if "category" not in st.session_state:
    st.session_state.category = None

# 6. 뽑기 버튼
if st.button("✨ 오늘의 검색어 뽑기", use_container_width=True):
    if filtered_words:
        st.session_state.chosen_word = random.choice(filtered_words)
        st.session_state.category = search_data[st.session_state.chosen_word]
    else:
        st.warning("선택한 카테고리에 데이터가 없습니다.")

# 7. 결과 출력
if st.session_state.chosen_word:
    word = st.session_state.chosen_word
    cat = st.session_state.category
    
    st.info(f"🔮 **[{cat}]**")
    st.code(word, language="")
    
    encoded_word = urllib.parse.quote(word)
    
    # 기존 구글 검색 링크
    google_url = f"https://www.google.com/search?q={encoded_word}"
    st.link_button("🌐 구글에서 검색 결과 보기", google_url, use_container_width=True)
    
    # 괴담 카테고리 이미지 링크
    if cat == "인터넷 미스터리 & 괴담":
        image_url = f"https://www.google.com/search?tbm=isch&q={encoded_word}"
        st.link_button("🖼️ 구글 이미지에서 보기", image_url, use_container_width=True)
    
    # ✅ 구글 이스터에그는 선택하자마자 바로 새 탭에서 실행
    if cat == "구글 이스터에그":
        components.html(f"""
            <script>
                window.open('{google_url}', '_blank');
            </script>
        """, height=0)
        
        st.caption("💡 새 탭에서 구글 이스터에그가 실행됩니다!")
