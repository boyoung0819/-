
import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import quote
from functools import lru_cache
import re
import html

st.set_page_config(
    page_title="먼작귀 MBTI 도감",
    page_icon="🐹",
    layout="wide",
)

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
        135deg, #fff8fb 0%, #f3f8ff 50%, #fffaf0 100%
    );
}

h1, h2, h3 {
    font-family: 'Jua', sans-serif !important;
}

.hero {
    padding: 1.5rem;
    border-radius: 24px;
    background: rgba(255,255,255,.88);
    border: 2px solid #f3dce8;
    text-align: center;
    box-shadow: 0 8px 24px rgba(140,110,130,.08);
}

.profile {
    background: rgba(255,255,255,.9);
    padding: 1.2rem;
    border: 2px solid #e9dff4;
    border-radius: 22px;
}

.type-pill {
    display: inline-block;
    padding: .35rem .8rem;
    border-radius: 999px;
    background: #eee5ff;
    color: #59427a;
    font-weight: 700;
}

.small-note {
    color: #786b78;
    font-size: .88rem;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,.8);
    padding: 12px;
    border: 1px solid #f0e4ec;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 캐릭터 데이터
# image_url에 이미지 파일 주소를 직접 넣으면
# 자동 검색보다 해당 주소를 우선 사용합니다.
# -----------------------------
CHARACTERS = {
    "치이카와": {
        "emoji": "🐹",
        "description": "소심하지만 성실하고, 작은 용기를 모아 나아가는 캐릭터.",
        "image_url": "",
    },
    "하치와레": {
        "emoji": "🐱",
        "description": "밝고 다정하며, 친구를 응원하는 캐릭터.",
        "image_url": "",
    },
    "우사기": {
        "emoji": "🐰",
        "description": "자유분방하고 에너지가 넘치는 캐릭터.",
        "image_url": "",
    },
    "모몽가": {
        "emoji": "🐿️",
        "description": "관심받기를 좋아하고 자기표현이 강한 캐릭터.",
        "image_url": "",
    },
    "쿠리만쥬": {
        "emoji": "🌰",
        "description": "느긋하게 먹는 것을 즐기는 어른스러운 캐릭터.",
        "image_url": "",
    },
    "랏코": {
        "emoji": "🦦",
        "description": "실력이 뛰어나고 믿음직한 선배 같은 캐릭터.",
        "image_url": "",
    },
    "시사": {
        "emoji": "🦁",
        "description": "성실하게 배우고 맡은 일을 해내려는 캐릭터.",
        "image_url": "",
    },
    "카니(고서점)": {
        "emoji": "🦀",
        "description": "조용하고 섬세한 분위기의 캐릭터.",
        "image_url": "",
    },
    "그 아이": {
        "emoji": "👀",
        "description": "독특한 분위기와 예측하기 어려운 면이 있는 캐릭터.",
        "image_url": "",
    },
    "데카츠요": {
        "emoji": "💪",
        "description": "강한 존재감과 독특한 행동이 인상적인 캐릭터.",
        "image_url": "",
    },
    "오데": {
        "emoji": "🎩",
        "description": "차분하고 개성 있는 분위기의 캐릭터.",
        "image_url": "",
    },
    "키메라": {
        "emoji": "👾",
        "description": "독특하고 신비로운 모습의 캐릭터.",
        "image_url": "",
    },
    "갑옷씨": {
        "emoji": "🛡️",
        "description": "먼작귀 세계에서 여러 일을 맡아 돕는 캐릭터.",
        "image_url": "",
    },
    "딱정벌레": {
        "emoji": "🪲",
        "description": "작고 독특한 모습으로 등장하는 캐릭터.",
        "image_url": "",
    },
    "고블린": {
        "emoji": "👺",
        "description": "동굴 등에서 등장하는 개성 있는 캐릭터.",
        "image_url": "",
    },
    "파자마 파티즈": {
        "emoji": "🎉",
        "description": "파자마 파티와 관련된 개성 있는 캐릭터들.",
        "image_url": "",
    },
}


# -----------------------------
# MBTI 데이터
# -----------------------------
MBTI = {
    "INTJ": (
        "갑옷씨", "전략가",
        "계획을 세우고 효율적인 방법을 찾는 편이에요.",
        ["장기적인 관점", "체계적인 계획", "독립적인 판단"]
    ),
    "INTP": (
        "그 아이", "논리 탐구가",
        "호기심이 많고 독특한 방식으로 생각해요.",
        ["분석적 사고", "새로운 관점", "탐구심"]
    ),
    "ENTJ": (
        "랏코", "통솔자",
        "목표를 정하고 주도적으로 이끄는 모습과 어울려요.",
        ["목표 지향", "결단력", "조직력"]
    ),
    "ENTP": (
        "우사기", "변론가",
        "틀에 얽매이지 않고 즉흥적으로 아이디어를 펼쳐요.",
        ["재치", "도전 정신", "발상 전환"]
    ),
    "INFJ": (
        "카니(고서점)", "옹호자",
        "조용히 관찰하며 의미와 마음을 중요하게 여겨요.",
        ["통찰력", "배려", "가치 중심"]
    ),
    "INFP": (
        "치이카와", "중재자",
        "섬세한 감정과 진심을 소중히 여겨요.",
        ["공감", "상상력", "진정성"]
    ),
    "ENFJ": (
        "하치와레", "선도자",
        "친구를 격려하고 함께 나아가려는 모습과 어울려요.",
        ["소통", "격려", "협력"]
    ),
    "ENFP": (
        "파자마 파티즈", "활동가",
        "새로운 경험과 즐거운 교류를 좋아해요.",
        ["열정", "창의성", "친화력"]
    ),
    "ISTJ": (
        "시사", "현실주의자",
        "책임감을 가지고 차근차근 배우고 실천해요.",
        ["성실함", "책임감", "꾸준함"]
    ),
    "ISFJ": (
        "카니(고서점)", "수호자",
        "세심하게 살피고 조용히 도움을 주는 편이에요.",
        ["세심함", "신뢰", "헌신"]
    ),
    "ESTJ": (
        "갑옷씨", "경영자",
        "규칙과 역할을 중시하고 일을 체계적으로 처리해요.",
        ["실행력", "조직력", "책임감"]
    ),
    "ESFJ": (
        "하치와레", "집정관",
        "주변 사람들과 조화를 이루고 서로 돕는 것을 중요하게 생각해요.",
        ["친절함", "협동", "배려"]
    ),
    "ISTP": (
        "쿠리만쥬", "장인",
        "차분하게 상황을 살피고 실용적인 방법을 찾아요.",
        ["관찰력", "실용성", "침착함"]
    ),
    "ISFP": (
        "모몽가", "모험가",
        "자기만의 취향과 순간의 감정을 중요하게 여겨요.",
        ["감각", "유연함", "개성"]
    ),
    "ESTP": (
        "데카츠요", "사업가",
        "행동이 빠르고 직접 경험하는 편이에요.",
        ["대담함", "적응력", "행동력"]
    ),
    "ESFP": (
        "오데", "연예인",
        "현재의 순간과 개성 있는 표현을 즐겨요.",
        ["표현력", "활기", "즉흥성"]
    ),
}


# -----------------------------
# 인터넷 이미지 검색
# 자동 검색은 검색 사이트의 응답 구조에 따라
# 실패할 수 있습니다.
# -----------------------------
@lru_cache(maxsize=64)
def find_image_url(character):
    query = quote(f"Chiikawa {character} character")
    search_url = (
        "https://www.google.com/search?tbm=isch&q=" + query
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 Chrome/124 Safari/537.36"
        )
    }

    try:
        response = requests.get(
            search_url,
            headers=headers,
            timeout=8
        )
        response.raise_for_status()
        page = response.text

        candidates = re.findall(
            r'https?://[^"\\\s<>]+?\.(?:jpg|jpeg|png|webp)'
            r'(?:\?[^"\\\s<>]*)?',
            page,
            flags=re.I
        )

        for url in candidates:
            url = (
                url.replace("\\u003d", "=")
                   .replace("\\u0026", "&")
                   .replace("&amp;", "&")
            )

            if "gstatic.com" in url or "google.com" in url:
                continue

            if url.startswith("http"):
                return url

    except Exception:
        pass

    return None


# -----------------------------
# 이미지 다운로드 및 검증
# -----------------------------
@lru_cache(maxsize=64)
def load_image(url):
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=8
        )
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        image.load()

        return image.convert("RGB")

    except Exception:
        return None


# -----------------------------
# 캐릭터 이미지 표시
# -----------------------------
def show_character(character, custom_url="", width=240):
    data = CHARACTERS[character]

    url = custom_url.strip()

    if not url:
        url = data["image_url"].strip()

    if not url:
        url = find_image_url(character)

    if url:
        image = load_image(url)

        if image is not None:
            st.image(
                image,
                width=width,
                caption=character
            )
            return

    st.markdown(
        f"""
        <div style="
            width:100%;
            min-height:180px;
            background:#ffffff;
            border:1px dashed #e5d7e7;
            border-radius:18px;
            display:flex;
            align-items:center;
            justify-content:center;
            flex-direction:column;
            padding:12px;
            box-sizing:border-box;
        ">
            <div style="font-size:76px">{data['emoji']}</div>
            <div style="font-weight:700;color:#66566b">
                {html.escape(character)}
            </div>
            <div style="
                font-size:12px;
                color:#8c7d90;
                padding:8px;
                text-align:center;
            ">
                사진을 자동으로 불러오지 못했어요.<br>
                사이드바에서 이미지 URL을 입력해 주세요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# 상단 제목
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <h1>🐹 먼작귀 MBTI 도감 🐰</h1>
        <p>내 MBTI와 어울리는 먼작귀 캐릭터를 찾아봐요!</p>
    </div>
    """,
    unsafe_allow_html=True
)

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

    st.markdown("---")
    st.subheader("🖼️ 사진이 안 보이나요?")

    manual_url = st.text_input(
        "대표 캐릭터 이미지 URL",
        placeholder="https://.../character.png"
    )

    st.caption(
        "이미지 파일 자체를 열 수 있는 주소를 입력해 주세요. "
        "웹페이지 주소는 작동하지 않을 수 있어요."
    )


# -----------------------------
# 선택한 MBTI 프로필
# -----------------------------
character, mbti_title, personality, strengths = MBTI[selected]
char_data = CHARACTERS[character]

left, right = st.columns(
    [1, 1.45],
    gap="large"
)

with left:
    st.markdown(
        '<div class="profile">',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="type-pill">{selected}</div>',
        unsafe_allow_html=True
    )

    st.subheader(f"오늘의 캐릭터: {character}")

    show_character(
        character,
        custom_url=manual_url,
        width=300
    )

    st.markdown(f"**{char_data['description']}**")

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

with right:
    st.markdown(f"## {selected} · {mbti_title}")

    st.write(personality)

    st.markdown("### ✨ 어울리는 특징")

    for strength in strengths:
        st.markdown(f"- {strength}")

    st.info(
        "이 MBTI 매칭은 재미를 위한 창작 해석이며, "
        "공식 설정이나 심리검사 결과가 아닙니다."
    )

    st.markdown("### 🧠 MBTI 간단 설명")

    st.write(
        "MBTI는 네 가지 선호 지표를 조합한 성격 유형 분류예요. "
        "유형은 사람을 단정하는 기준이 아니라 자기 이해를 돕는 "
        "참고 자료로 활용해 주세요."
    )


# -----------------------------
# 전체 MBTI 도감
# -----------------------------
st.divider()

st.markdown("## 📚 16가지 MBTI 전체 도감")

st.caption(
    "각 카드의 이미지는 인터넷에서 자동으로 불러오기를 시도합니다. "
    "검색 사이트의 제한이나 이미지 주소에 따라 이모지가 대신 표시될 수 있어요."
)

types = list(MBTI.keys())

for start in range(0, len(types), 4):
    cols = st.columns(4, gap="medium")

    for col, mbti in zip(cols, types[start:start + 4]):
        name, title, desc, _ = MBTI[mbti]

        with col:
            with st.container(border=True):
                st.markdown(f"**{mbti} · {title}**")

                show_character(
                    name,
                    custom_url="",
                    width=180
                )

                st.caption(f"캐릭터: {name}")

                st.write(desc)

                if st.button(
                    "이 유형 보기",
                    key=f"view_{mbti}",
                    use_container_width=True
                ):
                    st.session_state["selected_mbti"] = mbti
                    st.rerun()


# -----------------------------
# 도감에서 선택한 유형 안내
# -----------------------------
if "selected_mbti" in st.session_state:
    chosen = st.session_state["selected_mbti"]

    if chosen != selected:
        st.info(
            f"도감에서 {chosen} 유형을 선택했어요. "
            "왼쪽 사이드바에서 해당 MBTI를 선택하면 "
            "프로필을 확인할 수 있어요."
        )


# -----------------------------
# 이미지 안내
# -----------------------------
st.divider()

st.markdown("### 🛠️ 이미지가 계속 안 뜰 때")

st.write(
    "일부 검색 사이트는 이미지 자동 수집을 차단하거나 "
    "검색 결과의 구조를 변경할 수 있어요. "
    "이 경우 원하는 캐릭터의 이미지 파일 주소를 직접 입력하면 "
    "해당 사진을 불러오도록 시도합니다."
)

st.markdown(
    """
    <p class="small-note">
    먼작귀 캐릭터의 이미지와 이름은 각 권리자에게 권리가 있습니다.
    이 앱은 팬 제작·학습용 예시이며 공식 앱이 아닙니다.
    </p>
    """,
    unsafe_allow_html=True
)
