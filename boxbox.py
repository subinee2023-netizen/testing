import streamlit as st
import pandas as pd

# 0. 국가지질공원 데이터
# 참고: 실제 데이터는 공식 웹사이트를 참조하세요. 여기서는 예시 데이터를 사용합니다.
# (위도, 경도, 설명, 공식 URL)
GEOPARKS = {
    "소개": {
        "lat": 36.5,
        "lon": 127.5,
        "desc": "대한민국의 국가지질공원은 총 15곳이 있습니다. (2024년 기준)\n\n국가지질공원은 지구과학적으로 중요하고 경관이 우수한 지역으로, 이를 보전하고 교육 및 관광에 활용하기 위해 환경부 장관이 인증한 공원입니다.\n\n왼쪽 사이드바에서 궁금한 지질공원을 선택해 보세요!",
        "url": "https://www.geopark.kr/main.do",
        "zoom": 6
    },
    "제주도": {
        "lat": 33.3846,
        "lon": 126.5580,
        "desc": "한라산, 만장굴, 성산일출봉 등 화산 활동으로 형성된 독특한 지형과 생태계를 보유한 세계적인 화산 지질공원입니다.",
        "url": "http://www.jeju.go.kr/geopark/index.htm",
        "zoom": 9
    },
    "울릉도/독도": {
        "lat": 37.4851,
        "lon": 130.9051,
        "desc": "동해의 화산섬으로, 나리분지, 코끼리바위 등 독특한 화산 지형과 해안 경관을 자랑합니다.",
        "url": "http://www.ulleung.go.kr/geo/",
        "zoom": 9
    },
    "부산": {
        "lat": 35.1583,
        "lon": 129.0747,
        "desc": "도시 전체가 지질공원으로, 낙동강 하구, 태종대, 오륙도 등 해안과 강이 만들어낸 다양한 지질 명소를 포함합니다.",
        "url": "https://www.busan.go.kr/geopark/",
        "zoom": 10
    },
    "한탄강": {
        "lat": 38.0000,
        "lon": 127.0000,
        "desc": "용암이 흐르며 형성된 현무암 주상절리와 협곡이 장관을 이루는 곳으로, 포천, 연천, 철원 일대에 걸쳐 있습니다.",
        "url": "http://www.hantangeopark.kr/",
        "zoom": 9
    },
    "무등산": {
        "lat": 35.1052,
        "lon": 126.9918,
        "desc": "약 8,700만 년 전 화산 활동으로 형성된 서석대, 입석대 등 거대한 주상절리대가 특징입니다.",
        "url": "http://mudeungsan-geopark.com/",
        "zoom": 10
    }
    # 여기에 다른 지질공원 정보도 추가할 수 있습니다.
    # (예: 강원평화, 청송, 경북동해안, 전북서해안 등)
}

# 1. 앱 기본 설정
st.set_page_config(
    page_title="🇰🇷 한국의 국가지질공원",
    layout="wide"
)

# 2. 사이드바 (공원 선택)
st.sidebar.title("🗺️ 국가지질공원")
park_list = list(GEOPARKS.keys())
selected_park = st.sidebar.selectbox(
    "알아보고 싶은 지질공원을 선택하세요:",
    park_list
)

# 3. 메인 페이지 (선택된 공원 정보 표시)

# 선택된 공원의 정보 가져오기
park_info = GEOPARKS[selected_park]

# 3-1. 제목 및 이미지
st.title(f"🇰🇷 {selected_park} 국가지질공원")

# '소개' 페이지의 경우 메인 이미지 표시
if selected_park == "소개":
    st.image("https://www.geopark.kr/images/main/main_visual01.jpg", 
             caption="한국의 국가지질공원 (이미지 출처: 국가지질공원 공식 홈페이지)")

# 3-2. 설명
st.subheader("📖 소개")
st.write(park_info["desc"])

# 3-3. 공식 웹사이트 링크 ( '소개' 포함 모든 페이지에 표시)
st.info(f"**더 알아보기:** [ {selected_park} 공식 웹사이트 방문하기 🔗]({park_info['url']})")


# 3-4. 지도 표시
st.subheader("📍 위치 지도")

# st.map은 위도(lat), 경도(lon) 컬럼을 가진 DataFrame이 필요합니다.
map_data = pd.DataFrame(
    [{'lat': park_info["lat"], 'lon': park_info["lon"]}]
)

st.map(map_data, zoom=park_info["zoom"])


# 3-5. (선택) 전체 공원 목록 보여주기 (소개 페이지에서만)
if selected_park == "소개":
    st.subheader("🏞️ 전체 지질공원 목록")
    
    # '소개'를 제외한 공원 목록 생성
    all_parks_data = []
    for park_name, info in GEOPARKS.items():
        if park_name != "소개":
            all_parks_data.append({
                "name": park_name,
                "lat": info["lat"],
                "lon": info["lon"]
            })
    
    df_all_parks = pd.DataFrame(all_parks_data)
    
    # 전체 맵 보여주기 (줌 레벨 6)
    st.map(df_all_parks, zoom=6)
    
    # 목록 나열
    st.dataframe(df_all_parks.set_index('name'))
