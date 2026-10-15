
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="친구 닮은 먼작귀 MBTI 도감",
    page_icon="🐹",
    layout="wide"
)

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets"

# -----------------------------
# 디자인
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}

.stApp {
    background: linear-gradient(
        135deg, #fff4f8 0%, #f4f7ff 52%, #fff9ec 100%
    );
}

h1, h2, h3 {
    font-family: 'Jua', sans-serif !important;
}

.hero {
    padding: 1.5rem;
    border-radius: 24px;
    background: #fffafc;
    border: 2px solid #f2d5e2;
    text-align: center;
    box-shadow: 0 8px 24px rgba(140,110,130,.08);
}

.pill {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 999px;
    background: #eee5ff;
    color: #59427a;
    font-weight: 700;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,.82);
    border-radius: 18px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 캐릭터 도감
# 이미지 파일은 assets 폴더에 넣어 주세요.
# -----------------------------
CHARACTERS = {
    "치이카와": {
        "emoji": "🐹",
        "description": "소심하지만 성실하고, 작은 용기를 모아 나아가는 캐릭터.",
        "image": "character_poster.png"
    },
    "우사기": {
        "emoji": "🐰",
        "description": "자유분방하고 에너지가 넘치는 캐릭터.",
        "image": "character_poster.png"
    },
    "하치와레": {
        "emoji": "🐱",
        "description": "밝고 다정하며 친구를 응원하는 캐릭터.",
        "image": "character_poster.png"
    },
    "랏코": {
        "emoji": "🦦",
        "description": "실력이 뛰어나고 믿음직한 선배 같은 캐릭터.",
        "image": "character_poster.png"
    },
    "쿠리만쥬": {
        "emoji": "🌰",
        "description": "느긋하게 먹는 것을 즐기는 어른스러운 캐릭터.",
        "image": "character_poster.png"
    },
    "모몽가": {
        "emoji": "🐿️",
        "description": "관심받기를 좋아하고 자기표현이 강한 캐릭터.",
        "image": "character_poster.png"
    },
    "시사": {
        "emoji": "🦁",
        "description": "성실하게 배우고 맡은 일을 해내려는 캐릭터.",
        "image": "character_poster.png"
    },
    "카니": {
        "emoji": "🦀",
        "description": "독특한 분위기를 지닌 고서점 관련 캐릭터.",
        "image": "character_poster.png"
    },
    "고블린": {
        "emoji": "👺",
        "description": "동굴 등에서 등장하는 개성 있는 캐릭터.",
        "image": "character_poster.png"
    },
    "갑옷씨": {
        "emoji": "🛡️",
        "description": "먼작귀 세계에서 여러 일을 맡아 돕는 갑옷 캐릭터.",
        "image": "armored_soldiers.png"
    },
    "파자마 파티즈": {
        "emoji": "🎉",
        "description": "파자마 파티와 관련된 개성 있는 캐릭터들.",
        "image": "pajama_party.png"
    },
    "섬 아저씨": {
        "emoji": "🍚",
        "description": "치이카와가 숲속 깊은 곳에서 발견한 식당의 주인.",
        "image": "shim_ojisan.png"
    },
    "세이렌": {
        "emoji": "🧜",
        "description": "노래를 잘하며 섬 이야기에서 중요한 역할을 하는 캐릭터.",
        "image": "seiren.png"
    },
    "한잎과 두잎": {
        "emoji": "🌿",
        "description": "섬에서 함께 등장하는 두 캐릭터.",
        "image": "hanip_duip.png"
    },
    "인어": {
        "emoji": "🐟",
        "description": "세이렌과 함께 등장하는 인어 캐릭터.",
        "image": "mermaid.png"
    },
    "데카츠요": {
        "emoji": "💪",
        "description": "강한 존재감과 독특한 행동이 인상적인 캐릭터.",
        "image": "chimera.png"
    },
    "별똥별": {
        "emoji": "⭐",
        "description": "별똥별의 모습으로 등장하는 신비로운 캐릭터.",
        "image": "yellow_creature.png"
    },
    "아노코": {
        "emoji": "🤍",
        "description": "숲 장면에 등장하는 커다란 흰색 캐릭터.",
        "image": "white_creature.png"
    }
}


# -----------------------------
# MBTI 유형별 캐릭터
# 각 MBTI에 서로 다른 캐릭터를 배정
# -----------------------------
MBTI = {
    "INTJ": {
        "character": "갑옷씨",
        "title": "전략가",
        "description": "계획을 세우고 효율적인 방법을 찾는 편이에요.",
        "strengths": ["장기적인 관점", "체계적인 계획", "독립적인 판단"]
    },
    "INTP": {
        "character": "별똥별",
        "title": "논리 탐구가",
        "description": "호기심을 바탕으로 독특한 관점에서 생각해요.",
        "strengths": ["분석적 사고", "새로운 관점", "탐구심"]
    },
    "ENTJ": {
        "character": "랏코",
        "title": "통솔자",
        "description": "목표를 정하고 주도적으로 이끄는 모습과 어울려요.",
        "strengths": ["목표 지향", "결단력", "조직력"]
    },
    "ENTP": {
        "character": "우사기",
        "title": "변론가",
        "description": "틀에 얽매이지 않고 즉흥적으로 아이디어를 펼쳐요.",
        "strengths": ["재치", "도전 정신", "발상 전환"]
    },
    "INFJ": {
        "character": "카니",
        "title": "옹호자",
        "description": "조용히 관찰하며 의미와 마음을 중요하게 여겨요.",
        "strengths": ["통찰력", "배려", "가치 중심"]
    },
    "INFP": {
        "character": "치이카와",
        "title": "중재자",
        "description": "섬세한 감정과 진심을 소중히 여겨요.",
        "strengths": ["공감", "상상력", "진정성"]
    },
    "ENFJ": {
        "character": "하치와레",
        "title": "선도자",
        "description": "친구를 격려하고 함께 나아가는 모습과 어울려요.",
        "strengths": ["소통", "격려", "협력"]
    },
    "ENFP": {
        "character": "파자마 파티즈",
        "title": "활동가",
        "description": "새로운 경험과 즐거운 교류를 좋아해요.",
        "strengths": ["열정", "창의성", "친화력"]
    },
    "ISTJ": {
        "character": "시사",
        "title": "현실주의자",
        "description": "책임감을 가지고 차근차근 배우고 실천해요.",
        "strengths": ["성실함", "책임감", "꾸준함"]
    },
    "ISFJ": {
        "character": "한잎과 두잎",
        "title": "수호자",
        "description": "함께하며 서로를 챙기는 모습과 어울려요.",
        "strengths": ["세심함", "신뢰", "협력"]
    },
    "ESTJ": {
        "character": "섬 아저씨",
        "title": "경영자",
        "description": "자신의 일을 책임지고 체계적으로 운영하는 모습과 어울려요.",
        "strengths": ["실행력", "책임감", "관리 능력"]
    },
    "ESFJ": {
        "character": "세이렌",
        "title": "집정관",
        "description": "주변과 관계를 맺고 함께 행동하는 모습과 어울려요.",
        "strengths": ["친화력", "협동", "표현력"]
    },
    "ISTP": {
        "character": "쿠리만쥬",
        "title": "장인",
        "description": "차분하게 상황을 살피고 실용적인 방법을 찾아요.",
        "strengths": ["관찰력", "실용성", "침착함"]
    },
    "ISFP": {
        "character": "모몽가",
        "title": "모험가",
        "description": "자기만의 취향과 순간의 감정을 중요하게 여겨요.",
        "strengths": ["감각", "유연함", "개성"]
    },
    "ESTP": {
        "character": "데카츠요",
        "title": "사업가",
        "description": "상황에 빠르게 반응하고 행동하는 모습과 어울려요.",
        "strengths": ["대담함", "적응력", "행동력"]
    },
    "ESFP": {
        "character": "인어",
        "title": "연예인",
        "description": "표현력이 있고 주변과 함께 움직이는 모습을 떠올리게 해요.",
        "strengths": ["표현력", "활기", "즉흥성"]
    }
}


# -----------------------------
# 이미지 표시
# -----------------------------
def show_character(name, width=None):
    data = CHARACTERS[name]
    image_path = ASSET_DIR / data["image"]

    if image_path.exists():
        try:
            with Image.open(image_path) as image:
                st.image(
                    image.copy(),
                    caption=name,
                    use_container_width=(width is None),
                    width=width
                )
            return
        except Exception:
            pass

    st.markdown(
        f"<div style='text-align:center;font-size:64px'>"
        f"{data['emoji']}</div>",
        unsafe_allow_html=True
    )
    st.caption(f"{name} 사진을 찾을 수 없어 대체 그림을 표시했어요.")


# -----------------------------
# 제목
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🐹 친구 닮은 먼작귀 캐릭터 MBTI 도감 🐰</h1>
    <p>내 MBTI와 어울리는 먼작귀 캐릭터를 찾아봐요!</p>
</div>
""", unsafe_allow_html=True)

st.write("")


# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:
    st.header("🔎 MBTI 선택")

    selected = st.selectbox(
        "내 MBTI를 골라 주세요",
        list(MBTI.keys()),
        index=5
    )

    st.divider()

    st.caption(
        "캐릭터와 MBTI의 연결은 재미를 위한 창작 해석이며 "
        "공식 설정은 아니에요."
    )


# -----------------------------
# 선택한 MBTI 프로필
# -----------------------------
profile = MBTI[selected]
name = profile["character"]

left, right = st.columns([1, 1.35], gap="large")

with left:
    with st.container(border=True):
        st.markdown(
            f'<span class="pill">{selected}</span>',
            unsafe_allow_html=True
        )
        st.subheader(f"오늘의 캐릭터: {name}")
        show_character(name)
        st.write(CHARACTERS[name]["description"])

with right:
    st.markdown(f"## {selected} · {profile['title']}")
    st.write(profile["description"])

    st.markdown("### ✨ 어울리는 특징")
    for item in profile["strengths"]:
        st.markdown(f"- {item}")

    st.info(
        "이 매칭은 재미를 위한 창작 해석이에요. "
        "실제 성격이나 심리검사 결과를 판단하는 기준은 아니에요."
    )


# -----------------------------
# 캐릭터 MBTI 도감
# 중복 캐릭터 없이 한 번씩 표시
# -----------------------------
st.divider()
st.markdown("## 📚 캐릭터 MBTI 도감")
st.caption(
    "캐릭터마다 한 장씩만 표시했어요. "
    "MBTI가 연결된 캐릭터는 유형도 함께 볼 수 있어요."
)

# MBTI에 배정된 캐릭터와 아직 MBTI가 연결되지 않은 캐릭터를
# 하나의 도감에 합쳐서 중복 없이 표시합니다.
character_to_mbti = {
    info["character"]: mbti
    for mbti, info in MBTI.items()
}

catalog_order = [
    "치이카와",
    "우사기",
    "하치와레",
    "랏코",
    "쿠리만쥬",
    "모몽가",
    "시사",
    "카니",
    "고블린",
    "갑옷씨",
    "파자마 파티즈",
    "섬 아저씨",
    "세이렌",
    "한잎과 두잎",
    "인어",
    "데카츠요",
    "별똥별",
    "아노코"
]

# 같은 이름이 목록에 들어가더라도 한 번만 표시
catalog_order = list(dict.fromkeys(catalog_order))

for start in range(0, len(catalog_order), 3):
    columns = st.columns(3, gap="medium")

    for column, character in zip(
        columns,
        catalog_order[start:start + 3]
    ):
        with column:
            with st.container(border=True):
                st.markdown(f"### {character}")
                show_character(character)
                st.write(CHARACTERS[character]["description"])

                matched_mbti = character_to_mbti.get(character)

                if matched_mbti:
                    st.markdown(
                        f'<span class="pill">'
                        f'{matched_mbti} · '
                        f'{MBTI[matched_mbti]["title"]}'
                        f'</span>',
                        unsafe_allow_html=True
                    )

                    if st.button(
                        "이 유형 보기",
                        key=f"view_{matched_mbti}",
                        use_container_width=True
                    ):
                        st.session_state["selected_mbti"] = matched_mbti
                        st.rerun()
                else:
                    st.caption("아직 MBTI 유형을 연결하지 않았어요.")

if "selected_mbti" in st.session_state:
    chosen = st.session_state["selected_mbti"]

    if chosen != selected:
        st.info(
            f"{chosen} 유형을 선택했어요. "
            "왼쪽 MBTI 메뉴에서 해당 유형을 골라 프로필을 확인해 주세요."
        )

st.divider()

st.caption(
    "이미지는 제공된 자료를 사용합니다. "
    "캐릭터와 이미지의 권리는 각 권리자에게 있으며, "
    "이 앱은 비공식 팬 프로젝트입니다."
)
