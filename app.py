import random
import urllib.parse
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러보세요!")

# 데이터베이스 (단어: 카테고리) - 오류 해결 및 초희귀 데이터로 전면 리뉴얼
search_data = {
    # 🌿 초희귀 신비한 동식물 (검색 시 비주얼 충격적인 실존 생물)
    "심해 천사고기 Clione": "신비한 동식물", # 천사 같지만 먹이 먹을 때 머리가 갈라지는 무서운 유익족류
    "화살표 미크라테나": "신비한 동식물", # 질럿 거미의 정확한 한국 명칭. 노란 외계 장비처럼 생김
    "스네이크스킨 구라미": "신비한 동식물", # 뱀 가죽 패턴을 가진 기묘한 민물고기
    "마타마타 거북": "신비한 동식물", # 낙엽과 돌처럼 생겨서 구별이 안 되는 괴상한 거북
    "인도보라색개구리": "신비한 동식물", # 1년 중 딱 2주만 지상으로 나오는 보라색 젤리 모양 생물
    "바르바도스 실뱀": "신비한 동식물", # 동전 위에 올라갈 정도로 세상에서 가장 작고 눈이 먼 뱀
    "레인보우 유칼립투스": "신비한 동식물", # 인위적으로 물감을 칠한 듯한 무지개 빛깔의 신비한 나무
    "넓적부리황새 슈빌": "신비한 동식물", # 공룡의 후예라 불리는 거대하고 무섭게 생긴 새
    
    # ✨ 100% 작동하는 구글 이스터에그 (화면 효과 확실함)
    "askew": "구글 이스터에그", # 화면이 오른쪽으로 삐딱하게 기울어짐
    "do a barrel roll": "구글 이스터에그", # 화면이 360도 빙글 회전함
    "google gravity": "구글 이스터에그", # 검색 결과가 중력을 받아 바닥으로 무너짐 (첫 링크 접속)
    "chicxulub": "구글 이스터에그", # 화면에 운석이 떨어지면서 창이 흔들림
    "dart mission": "구글 이스터에그", # 인공위성이 날아가 화면을 들이받고 화면이 기울어짐
    "the wizard of oz": "구글 이스터에그", # 우측 지식창의 빨간 구두를 누르면 화면이 흑백으로 돌며 회전함
    "grogu": "구글 이스터에그", # 화면 우측 하단에 아기 요다가 나타나 화면을 포스로 부수기 시작함
    
    # 👻 [NEW] 인터넷 미스터리 & 괴담 (생소하고 기괴한 도시전설/사건)
    "백룸 The Backrooms": "인터넷 미스터리 & 괴담", # 노란 벽지와 형광등 소리만 가득한 무한한 가상 공간 미스터리
    "사다코 패러독스": "인터넷 미스터리 & 괴담", # 인터넷 방송이나 영상 알고리즘 속에 숨은 기괴한 괴담
    "유튜브 666": "인터넷 미스터리 & 괴담", # 과거 특정 주소로 접속하면 페이지가 피로 물들었다는 전설적인 유튜브 괴담
    "타임머신 설계도 존 티토": "인터넷 미스터리 & 괴담", # 2036년 미래에서 왔다고 주장하며 설계도를 남긴 시간 여행자 소동
    "시카다 3301": "인터넷 미스터리 & 괴담", # 천재 암호학자들만 모집하기 위해 인터넷에 출몰했던 정체불명의 단체
    "셀린 디온 역재생 괴담": "인터넷 미스터리 & 괴담", # 특정 음악을 뒤로 돌려 들으면 기괴한 메시지가 나온다는 미스터리
}

# 사이드바 카테고리 (새 카테고리 반영)
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
    
    # [핵심 해결] 검색어 파라미터를 안전하게 인코딩하여 구글 검색 URL 생성
    encoded_word = urllib.parse.quote(word)
    search_url = f"https://google.com{encoded_word}"
    
    st.link_button("👉 구글에서 정체 확인하기", search_url, type="primary", use_container_width=True)
