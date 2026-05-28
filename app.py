import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("대체 이게 뭘까요? 검색어를 뽑은 뒤 직접 정체를 확인해 보세요!")

# 데이터베이스 (검색어: [호기심 자극 힌트, 카테고리])
search_data = {
    # 1. 이름은 들어봤나? 초면인 생물
    "아이아이원숭이": [
        "나무 속에 숨은 애벌레를 꺼내 먹기 위해 '특정 손가락 하나'만 기괴할 정도로 길게 진화한 이 동물의 외모는?",
        "초면인 생물",
    ],
    "나도독미나리": [
        "이름 앞에 '나도'가 붙은 귀여운 이름과 달리, 스치기만 해도 치명적인 독을 품고 있는 이 식물의 정체는?",
        "초면인 생물",
    ],
    "느시": [
        "외글자 이름을 가진 새인데, 몸무게가 최대 18kg에 달해 '하늘을 날 수 있는 가장 무거운 새' 중 하나인 이 새의 생김새는?",
        "초면인 생물",
    ],
    "심해용각류": [
        "바다 깊은 곳에 살며 마치 외계 생명체처럼 생긴 기괴하고 거대한 바다 생물의 진짜 모습은?",
        "초면인 생물",
    ],
    "질경이이끼벌레": [
        "식물 같기도 하고 벌레 같기도 한 이름, 물속에 사는 이 괴이한 생명체의 정체는 무엇일까요?",
        "초면인 생물",
    ],
    # 2. 구글 이스터에그
    "askew": [
        "구글 검색창에 입력하면 모니터가 고장 난 것처럼 화면에 신기한 변화가 생깁니다!",
        "구글 이스터에그",
    ],
    "do a barrel roll": [
        "지하철이나 버스에서 검색하면 멀미가 날 수도 있습니다. 화면이 어떻게 변할까요?",
        "구글 이스터에그",
    ],
    # 3. 구글맵 미스터리 좌표
    "30°32'43.0\"N 32°33'46.0\"E": [
        "구글 지도에 이 좌표를 그대로 복사해서 치면 사막 한가운데에 나타나는 거대한 미스터리 문양의 정체는?",
        "구글맵 미스터리",
    ],
}

# 사이드바 카테고리 선택
categories = ["전체보기", "초면인 생물", "구글 이스터에그", "구글맵 미스터리"]
selected_category = st.sidebar.selectbox("카테고리를 선택하세요", categories)

# 필터링
if selected_category == "전체보기":
    filtered_words = list(search_data.keys())
else:
    filtered_words = [
        word
        for word, info in search_data.items()
        if info[1] == selected_category
    ]

# 뽑기 버튼
if st.button("✨ 비밀의 검색어 뽑기"):
    if filtered_words:
        chosen_word = random.choice(filtered_words)
        hint = search_data[chosen_word][0]

        # 결과 출력 (스포일러 방지 스타일)
        st.info(f"🔮 **힌트:** {hint}")

        # 사용자가 직접 검색하도록 유도하는 버튼
        search_url = f"https://www.google.com/search?q={chosen_word}"
        st.link_button(
            f"👉 직접 검색해서 정답 확인하기 ({chosen_word})",
            search_url,
        )
    else:
        st.warning("선택한 카테고리에 단어가 없습니다.")
