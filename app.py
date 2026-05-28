import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("카테고리를 선택하고 버튼을 눌러 신기한 검색어를 찾아보세요!")

# 검색어 데이터베이스 (검색어: [설명, 카테고리])
search_data = {
    # 1. 신기한 생물 카테고리
    "아이아이원숭이": [
        "손가락 하나만 비정상적으로 길어서 나무 속 애벌레를 파먹는 괴상하고 신기한 원숭이입니다.",
        "신기한 생물",
    ],
    "나도독미나리": [
        "이름은 귀엽지만 치명적인 독을 가진 미나리아재비과의 식물입니다.",
        "신기한 생물",
    ],
    "오리너구리": [
        "조류처럼 부리가 있고 알을 낳는데, 포유류인 지구상에서 가장 기묘한 동물 중 하나입니다.",
        "신기한 생물",
    ],
    "블롭피쉬": [
        "지구에서 가장 못생긴 동물로 뽑힌 적이 있는, 심해에 사는 흐물흐물한 물고기입니다.",
        "신기한 생물",
    ],
    # 2. 구글 이스터에그 카테고리
    "askew": [
        "구글 검색창에 입력하면 화면 전체가 오른쪽으로 살짝 기울어집니다!",
        "구글 이스터에그",
    ],
    "do a barrel roll": [
        "구글 검색창에 입력하면 화면이 시계 방향으로 360도 회전합니다.",
        "구글 이스터에그",
    ],
    "google pacman": [
        "구글 검색창에서 바로 플레이할 수 있는 추억의 팩맨 게임이 등장합니다.",
        "구글 이스터에그",
    ],
}

# 사이드바에서 카테고리 선택 기능 추가
categories = ["전체보기", "신기한 생물", "구글 이스터에그"]
selected_category = st.sidebar.selectbox("카테고리를 선택하세요", categories)

# 선택된 카테고리에 맞는 검색어 필터링
if selected_category == "전체보기":
    filtered_words = list(search_data.keys())
else:
    filtered_words = [
        word
        for word, info in search_data.items()
        if info[1] == selected_category
    ]

# 뽑기 버튼 작동
if st.button("✨ 뽑기"):
    if filtered_words:
        # 무작위로 단어 하나 선정
        chosen_word = random.choice(filtered_words)
        description = search_data[chosen_word][0]

        # 결과 박스 시각화
        st.success(f"**추천 검색어: {chosen_word}**")
        st.write(f"ℹ️ {description}")

        # 구글 검색 바로가기 하이퍼링크 생성
        # 검색어 뒤에 공백이나 특수문자가 들어갈 수 있으므로 안전하게 url 인코딩 처리를 위해 쿼리 형태로 전달
        search_url = f"https://www.google.com/search?q={chosen_word}"

        # 예쁜 버튼 형태의 링크 제공
        st.link_button("👉 구글에서 결과 확인하기", search_url)
    else:
        st.warning("선택한 카테고리에 단어가 없습니다.")
