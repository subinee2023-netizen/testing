import streamlit as st
import pandas as pd

# 0. 천연기념물 샘플 데이터
# (실제 앱에서는 이 부분을 CSV 파일이나 DB에서 불러오는 것이 더 좋습니다.)
# 데이터 출처: 문화재청 국가문화유산포털 (좌표는 예시용 근사치)
MONUMENTS_DATA = {
    "서울": [
        {
            "name": "서울 재동 백송",
            "num": "제8호",
            "lat": 37.5815,
            "lon": 126.9861,
            "desc": "헌법재판소 내에 위치한 백송으로, 나이는 약 600년으로 추정되며, 흰 수피가 아름다운 나무입니다."
        }
    ],
    "강원": [
        {
            "name": "설악산 천연보호구역",
            "num": "제171호",
            "lat": 38.1188,
            "lon": 128.4043,
            "desc": "웅장한 암석 경관과 다양한 희귀 동식물이 서식하는 한국의 대표적인 산입니다. 유네스코 생물권보전지역입니다."
        },
        {
            "name": "삼척 대이리 굴지대",
            "num": "제178호",
            "lat": 37.2851,
            "lon": 129.0435,
            "desc": "환선굴, 관음굴 등 대규모 석회동굴이 밀집해 있는 지역으로, 지질학적 가치가 매우 높습니다."
        }
    ],
    "제주": [
        {
            "name": "한라산 천연보호구역",
            "num": "제182호",
            "lat": 33.3614,
            "lon": 126.5331,
            "desc": "남한에서 가장 높은 산으로, 다양한 고산 식물과 화산 지형을 보유한 생태계의 보고입니다."
        },
        {
            "name": "제주 용천동굴",
            "num": "제466호",
            "lat": 33.5293,
            "lon": 126.8423,
            "desc": "용암동굴 내부에 석회동굴 생성물이 발달한, 세계적으로도 희귀한 복합 동굴입니다. 세계자연유산의 일부입니다."
        }
    ],
    "경북": [
         {
            "name": "독도 천연보호구역",
            "num": "제336호",
            "lat": 37.2422,
            "lon": 131.8643,
            "desc": "동해의 화산섬으로, 독특한 해양 생태계와 지질학적 가치를 지녀 섬 전체가 천연보호구역으로 지정되었습니다."
        },
        {
            "name": "경주 불국사 일원",
            "num": "사적 및 명승 제1호", # 천연기념물은 아니지만 예시로 포함 (실제로는 분류 필요)
            "lat": 35.7900,
            "lon": 129.3320,
            "desc": "불국사와 석굴암을 포함하는 지역으로, 역사적, 문화적 가치와 함께 아름다운 자연 경관을 지니고 있습니다. (데이터 예시)"
        }
    ]
    # 여기에 다른 지역과 천연기념물 데이터를 계속 추가할 수 있습니다.
}

# --- 스트림릿 앱 시작 ---

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="🌳 한국의 천연기념물",
    layout="wide"
)

# 2. 제목
st.title("🌳 한국의 천연기념물")
st.write("우리나라의 아름다운 자연유산, 천연기념물을 지역별로 탐색해 보세요.")

# 3. 사이드바 - 지역 선택
regions = ["전체 보기"] + list(MONUMENTS_DATA.keys())
selected_region = st.sidebar.selectbox("지역을 선택하세요:", regions)

# 4. 메인 콘텐츠
if selected_region == "전체 보기":
    # 4-1. "전체 보기" 선택 시
    st.subheader("📍 전국 천연기념물 지도 (샘플 데이터)")

    # 전체 데이터를 Pandas DataFrame으로 변환
    all_monuments = []
    for region, monuments_list in MONUMENTS_DATA.items():
        for monument in monuments_list:
            all_monuments.append({
                "지역": region,
                "이름": f"{monument['name']} ({monument['num']})",
                "lat": monument["lat"],
                "lon": monument["lon"]
            })
    
    if all_monuments:
        df_all = pd.DataFrame(all_monuments)
        
        # 전체 지도 표시
        st.map(df_all, zoom=6)
        
        # 전체 목록 테이블 표시
        st.subheader("📖 전체 목록")
        st.dataframe(df_all.set_index("지역"))
    else:
        st.warning("표시할 데이터가 없습니다.")

else:
    # 4-2. 특정 지역 선택 시
    st.subheader(f"🏞️ {selected_region} 지역의 천연기념물")
    
    monuments_list = MONUMENTS_DATA.get(selected_region)
    
    if not monuments_list:
        st.info(f"'{selected_region}' 지역에 등록된 천연기념물 데이터가 없습니다.")
    else:
        # 해당 지역의 천연기념물 목록을 순회하며 표시
        for monument in monuments_list:
            st.markdown(f"### {monument['name']} ({monument['num']})")
            st.write(monument['desc'])
            
            # 단일 위치 지도 표시
            map_data = pd.DataFrame([{'lat': monument["lat"], 'lon': monument["lon"]}])
            st.map(map_data, zoom=12) # 특정 위치를 확대해서 보여줌
            
            st.divider() # 각 항목 사이에 구분선 추가

# 5. 앱 정보 (푸터)
st.sidebar.info(
    """
    **정보**
    - 이 앱은 Streamlit을 사용하여 제작되었습니다.
    - 데이터는 문화재청 국가문화유산포털을 참고한 샘플 데이터입니다.
    """
)
