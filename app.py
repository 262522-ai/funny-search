import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="재밌는 검색어 추천기", page_icon="🔍")

st.title("🔍 재밌는 검색어 추천기")
st.write("사이드바에서 카테고리를 고르고 버튼을 눌러보세요!")

# 데이터베이스 (단어: 카테고리)
search_data = {
    # 🌿 신비한 동식물
    "아이아이원숭이": "신비한 동식물",
    "나도독미나리": "신비한 동식물",
    "핑크페어리 아르마딜로": "신비한 동식물",
    "관해파리 (Siphonophore)": "신비한 동식물",
    "긴코원숭이": "신비한 동식물",
    "유리개구리": "신비한 동식물",
    "덤보 문어": "신비한 동식물",
    "우파루파 (Axolotl)": "신비한 동식물",
    
    # 🌍 구글맵 미스터리 (좌표 직접 연결)
    "30°32'43.0\"N 32°33'46.0\"E": "구글맵 미스터리", # 사막 문양
    "50°00'41\"N 110°06'47\"W": "구글맵 미스터리", # 배드랜즈 가디언 (얼굴)
    "33.836379, 151.080506": "구글맵 미스터리", # 숲이 된 난파선
    "38°29'0.16\"N 109°40'52.80\"W": "구글맵 미스터리", # 무지개빛 칼륨 연못
    "37°14'37\"N 115°47'39\"W": "구글맵 미스터리", # Area 51 (51구역)
    "14°41'32.3\"S 75°08'56.9\"W": "구글맵 미스터리", # 나스카 라인 (거미)
    "-33.867886, -63.987": "구글맵 미스터리", # 기타 모양 숲
    
    # ✨ 구글 이스터에그
    "askew": "구글 이스터에그",
    "do a barrel roll": "구글 이스터에그",
    "google gravity": "구글 이스터에그",
    "thanos snap": "구글 이스터에그",
}

# 사이드바 카테고리 (라디오 버튼으로 모든 항목 상시 노출)
st.sidebar.markdown("### 📂 카테고리 선택")
selected_category = st.sidebar.radio(
    "보고 싶은 분야를 선택하세요:",
    ["전체보기", "신비한 동식물", "구글맵 미스터리", "구글 이스터에그"],
    index=0 # 처음에 '전체보기'가 선택되어 있게 함
)

# 필터링 로직
if selected_category == "전체보기":
    filtered_words = list(search_data.keys())
else:
    filtered_words = [word for word, cat in search_data.items() if cat == selected_category]

# 뽑기 버튼
if st.button("✨ 신기한 단어 뽑기"):
    if filtered_words:
        chosen_word = random.choice(filtered_words)
        category = search_data[chosen_word]
        
        # 결과 출력
        st.success(f"**결과: {chosen_word}**")
        
        # [핵심] 카테고리에 따라 링크 주소를 다르게 생성
        if category == "구글맵 미스터리":
            # 구글 '지도' 서비스로 바로 연결되는 주소
            map_url = f"https://www.google.com/maps/search/{chosen_word}"
            st.link_button("📍 구글 지도로 바로 날아가기", map_url)
        else:
            # 일반 구글 '검색' 결과로 연결되는 주소
            search_url = f"https://www.google.com/search?q={chosen_word}"
            st.link_button("👉 구글 검색 결과 확인하기", search_url)
    else:
        st.warning("선택한 카테고리에 내용이 없습니다.")
