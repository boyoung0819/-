
import streamlit as st
import random
import html

st.set_page_config(
    page_title="먼작귀 MBTI 도감",
    page_icon="🐹",
    layout="wide",
)

# -----------------------------
# 캐릭터 도감
# MBTI 연결은 재미를 위한 비공식 해석
# -----------------------------
characters = {
    "치이카와": {
        "emoji": "🐹", "no": "001", "color": "#F9DFE6",
        "keywords": ["다정함", "섬세함", "조용한 용기"],
        "desc": "소심하고 걱정이 많지만, 어려운 순간에도 열심히 노력하는 친구예요. 작은 행복을 소중히 여기고 친구들과 함께할 때 힘을 얻어요."
    },
    "하치와레": {
        "emoji": "🐱", "no": "002", "color": "#DCEBFC",
        "keywords": ["긍정", "우정", "표현력"],
        "desc": "밝고 긍정적인 태도로 친구들을 응원해요. 힘든 상황에서도 좋은 점을 찾으려 하고, 자신의 생각과 감정을 솔직하게 표현해요."
    },
    "우사기": {
        "emoji": "🐰", "no": "003", "color": "#FFF0B8",
        "keywords": ["자유로움", "즉흥성", "엉뚱함"],
        "desc": "활기차고 예측하기 어려운 행동으로 주변을 놀라게 해요. 자기만의 방식으로 행동하며 틀에 얽매이지 않는 매력을 보여줘요."
    },
    "모몽가": {
        "emoji": "🐿️", "no": "004", "color": "#EBDFFC",
        "keywords": ["자기표현", "개성", "관심"],
        "desc": "귀여운 모습을 적극적으로 드러내고 원하는 것을 분명하게 표현해요. 장난스럽고 개성이 강해 주변의 시선을 끄는 친구예요."
    },
    "쿠리만쥬": {
        "emoji": "🌰", "no": "005", "color": "#F2E0CF",
        "keywords": ["여유", "차분함", "소소한 행복"],
        "desc": "차분하게 자신만의 시간을 즐기고 맛있는 음식과 음료를 좋아해요. 말수가 많지 않아도 주변에 편안한 분위기를 만들어 줘요."
    },
    "랏코": {
        "emoji": "🦦", "no": "006", "color": "#D8E9F7",
        "keywords": ["실력", "책임감", "든든함"],
        "desc": "실력이 뛰어나고 용감해 다른 친구들에게 존경받아요. 강한 모습뿐 아니라 다른 친구들을 돕고 가르쳐 주는 따뜻함도 가지고 있어요."
    },
    "시사": {
        "emoji": "🦁", "no": "007", "color": "#DDF1DF",
        "keywords": ["성실함", "노력", "배움"],
        "desc": "열심히 배우고 맡은 일을 성실하게 해내는 친구예요. 존경하는 사람에게 배우며 꾸준히 성장하려는 모습이 인상적이에요."
    },
    "카니(고서점)": {
        "emoji": "🦀", "no": "008", "color": "#F8DDE4",
        "keywords": ["배려", "다정함", "조용한 취향"],
        "desc": "책을 좋아하고 다른 사람을 배려하는 다정한 친구예요. 모몽가와의 관계에서도 따뜻하고 사려 깊은 면을 보여줘요."
    },
    "그 아이": {
        "emoji": "🌙", "no": "009", "color": "#E7E3F7",
        "keywords": ["신비로움", "복잡한 감정", "독특함"],
        "desc": "다른 캐릭터들과는 조금 다른 분위기를 지닌 인물이에요. 단순하게 설명하기 어려운 면이 있어 여러 해석을 떠올리게 해요."
    },
    "데카츠요": {
        "emoji": "💪", "no": "010", "color": "#F5DFD8",
        "keywords": ["강렬함", "힘", "독특함"],
        "desc": "강렬한 인상과 독특한 존재감이 특징이에요. 평범한 일상과는 다른 분위기를 만들어 내는 캐릭터예요."
    },
    "오데": {
        "emoji": "🍢", "no": "011", "color": "#F5E5D2",
        "keywords": ["친근함", "느긋함", "개성"],
        "desc": "독특한 모습과 여유로운 분위기로 기억되는 캐릭터예요. 다른 등장인물들과 어울리는 장면에서 개성 있는 매력을 보여줘요."
    },
    "키메라": {
        "emoji": "🌀", "no": "012", "color": "#E6DFF4",
        "keywords": ["변화", "강렬함", "예측 불가"],
        "desc": "평범한 모습과는 다른 독특한 형태와 분위기를 지닌 존재예요. 신비롭고 강렬한 인상을 남기는 캐릭터예요."
    },
    "갑옷씨": {
        "emoji": "🛡️", "no": "013", "color": "#DCEDE8",
        "keywords": ["실용성", "책임", "도움"],
        "desc": "일터를 운영하거나 여러 역할을 맡으며 치이카와 세계의 일상을 만들어 가요. 각자 맡은 일을 수행하고 친구들과 상호작용해요."
    },
    "딱정벌레": {
        "emoji": "🪲", "no": "014", "color": "#DCE8D7",
        "keywords": ["호기심", "예측 불가", "반전"],
        "desc": "작고 독특한 모습으로 등장하지만 이야기에 예상하지 못한 변화를 가져오기도 해요. 겉모습만으로 판단하기 어려운 캐릭터예요."
    },
    "고블린": {
        "emoji": "👾", "no": "015", "color": "#E2E6D8",
        "keywords": ["장난기", "독특함", "변화"],
        "desc": "치이카와 세계에서 만날 수 있는 개성 강한 존재예요. 다른 캐릭터들과는 또 다른 분위기로 이야기를 다채롭게 만들어 줘요."
    },
    "파자마 파티즈": {
        "emoji": "🎤", "no": "016", "color": "#F8DDEE",
        "keywords": ["협동", "표현", "함께하는 즐거움"],
        "desc": "함께 노래하고 공연하는 그룹이에요. 각자의 개성을 살리면서 힘을 합치는 모습에서 협동과 표현의 즐거움을 발견할 수 있어요."
    },
}

# 16가지 MBTI에 서로 다른 대표 캐릭터 배정
mbti_data = {
    "INTJ": {
        "title": "전략가", "character": "갑옷씨",
        "reason": "일과 역할을 체계적으로 수행하는 모습에서 계획성과 책임감을 연결했어요.",
        "personality": "큰 그림을 생각하고 목표를 체계적으로 이루려는 편이에요.",
        "strength": "계획 수립과 독립적인 판단"
    },
    "INTP": {
        "title": "논리술사", "character": "그 아이",
        "reason": "쉽게 단정하기 어려운 신비로운 면을 탐구심과 독창적인 사고에 연결했어요.",
        "personality": "궁금한 것을 깊이 생각하고 새로운 관점으로 바라보는 편이에요.",
        "strength": "분석과 창의적인 발상"
    },
    "ENTJ": {
        "title": "통솔자", "character": "랏코",
        "reason": "뛰어난 실력과 다른 친구들을 이끄는 모습에서 리더십과 목표 지향성을 연결했어요.",
        "personality": "목표를 정하고 적극적으로 일을 추진하는 편이에요.",
        "strength": "결단력과 추진력"
    },
    "ENTP": {
        "title": "변론가", "character": "우사기",
        "reason": "예측할 수 없는 행동과 자유로운 모습을 새로운 시도와 아이디어에 연결했어요.",
        "personality": "새로운 가능성을 탐색하고 틀에 얽매이지 않는 것을 좋아해요.",
        "strength": "순발력과 발상의 전환"
    },
    "INFJ": {
        "title": "옹호자", "character": "카니(고서점)",
        "reason": "책을 좋아하고 다른 사람을 배려하는 모습을 깊은 이해와 가치 중심적인 태도에 연결했어요.",
        "personality": "사람의 마음을 이해하려 하고 자신이 중요하게 생각하는 가치를 지켜요.",
        "strength": "공감과 통찰력"
    },
    "INFP": {
        "title": "중재자", "character": "치이카와",
        "reason": "섬세한 감정과 작은 행복을 소중히 여기는 모습이 감수성과 잘 어울려요.",
        "personality": "자신의 감정과 신념을 중요하게 여기고 따뜻한 관계를 소중히 여겨요.",
        "strength": "상상력과 진심 어린 배려"
    },
    "ENFJ": {
        "title": "선도자", "character": "하치와레",
        "reason": "친구를 격려하고 긍정적인 분위기를 만드는 모습에서 사람을 응원하는 힘을 발견했어요.",
        "personality": "다른 사람을 격려하고 함께 성장하는 데 보람을 느껴요.",
        "strength": "소통과 격려"
    },
    "ENFP": {
        "title": "활동가", "character": "파자마 파티즈",
        "reason": "공연을 통해 개성을 표현하고 함께 즐기는 모습이 열정과 가능성을 중시하는 성향과 어울려요.",
        "personality": "새로운 경험을 좋아하고 다양한 가능성을 발견하는 편이에요.",
        "strength": "열정과 창의적인 표현"
    },
    "ISTJ": {
        "title": "현실주의자", "character": "시사",
        "reason": "자격을 갖추고 맡은 일을 성실하게 수행하는 모습에서 책임감과 꾸준함을 연결했어요.",
        "personality": "맡은 일을 꼼꼼하게 해내고 약속과 책임을 중요하게 생각해요.",
        "strength": "성실함과 체계적인 실행"
    },
    "ISFJ": {
        "title": "수호자", "character": "카니(고서점)",
        "reason": "다정하고 배려 깊은 모습이 주변 사람을 살피는 성향과 잘 어울려요.",
        "personality": "가까운 사람을 세심하게 챙기고 안정적인 관계를 중요하게 여겨요.",
        "strength": "세심함과 꾸준한 배려"
    },
    "ESTJ": {
        "title": "경영자", "character": "갑옷씨",
        "reason": "일터와 업무를 책임지는 역할에서 조직력과 실행력을 연결했어요.",
        "personality": "일을 정리하고 구체적인 계획에 따라 실행하는 편이에요.",
        "strength": "조직력과 책임감"
    },
    "ESFJ": {
        "title": "집정관", "character": "하치와레",
        "reason": "친구를 돕고 긍정적인 관계를 만드는 모습에서 협력과 친화력을 연결했어요.",
        "personality": "주변 사람과 조화를 이루고 서로 돕는 관계를 소중히 여겨요.",
        "strength": "친화력과 협동심"
    },
    "ISTP": {
        "title": "장인", "character": "쿠리만쥬",
        "reason": "차분하게 자신만의 시간을 즐기는 모습에서 독립적이고 담담한 분위기를 연결했어요.",
        "personality": "상황을 관찰하고 필요할 때 실용적인 해결책을 찾는 편이에요.",
        "strength": "침착함과 실용적인 판단"
    },
    "ISFP": {
        "title": "모험가", "character": "모몽가",
        "reason": "자신만의 개성과 표현 방식을 적극적으로 드러내는 면을 개성 중시 성향에 연결했어요.",
        "personality": "자신의 취향과 감성을 소중히 여기고 유연하게 행동하는 편이에요.",
        "strength": "감각과 자기표현"
    },
    "ESTP": {
        "title": "사업가", "character": "데카츠요",
        "reason": "강렬한 존재감과 활동적인 인상을 순간적인 행동력과 연결한 재미용 해석이에요.",
        "personality": "직접 경험하면서 빠르게 상황을 파악하는 편이에요.",
        "strength": "행동력과 상황 대처"
    },
    "ESFP": {
        "title": "연예인", "character": "오데",
        "reason": "독특하고 눈에 띄는 모습에서 개성 있는 표현과 생동감 있는 분위기를 연결했어요.",
        "personality": "현재의 경험을 즐기고 주변과 함께하는 순간을 소중히 여겨요.",
        "strength": "유연함과 생생한 표현"
    },
}

# -----------------------------
# 스타일
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

.stApp {
    background: linear-gradient(180deg, #fffaf0, #fff4f7 55%, #f5f3ff);
    color: #5b4a52;
    font-family: 'Noto Sans KR', sans-serif;
}
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3 {
    font-family: 'Jua', sans-serif !important;
    color: #79586a;
}
.hero {
    background: rgba(255,255,255,.92);
    border: 2px solid #f0d3dd;
    border-radius: 28px;
    padding: 30px 20px;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 8px 25px rgba(130,90,110,.08);
}
.hero-title {
    font-family: 'Jua', sans-serif;
    font-size: clamp(30px, 5vw, 46px);
    color: #bf7d97;
}
.hero-sub {
    line-height: 1.9;
    color: #8a727d;
    margin-top: 8px;
}
.section-title {
    font-family: 'Jua', sans-serif;
    color: #9a6c82;
    font-size: 25px;
    margin: 24px 0 12px;
}
.card {
    background: white;
    border: 2px solid #edcfda;
    border-radius: 25px;
    overflow: hidden;
    box-shadow: 0 8px 22px rgba(110,75,90,.07);
    margin-bottom: 18px;
}
.card-top {
    padding: 12px 17px;
    background: #f9e6ec;
    display: flex;
    justify-content: space-between;
    color: #8c6275;
    font-weight: 900;
}
.card-body {
    padding: 24px 18px;
    text-align: center;
}
.avatar {
    width: 145px;
    height: 145px;
    margin: auto;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 78px;
    border: 4px solid white;
    box-shadow: 0 5px 18px rgba(0,0,0,.08);
}
.char-name {
    font-family: 'Jua', sans-serif;
    font-size: 32px;
    color: #755466;
    margin: 12px 0 6px;
}
.pill {
    display: inline-block;
    padding: 6px 12px;
    margin: 3px;
    border-radius: 99px;
    background: #f9e8ee;
    color: #96647b;
    font-size: 13px;
    font-weight: 800;
}
.info {
    background: rgba(255,255,255,.91);
    border: 1px solid #f0dce4;
    border-radius: 19px;
    padding: 18px;
    line-height: 1.85;
    margin: 7px 0;
    min-height: 170px;
}
.stat {
    background: white;
    border: 1px solid #efdae2;
    border-radius: 17px;
    text-align: center;
    padding: 16px 8px;
}
.stat-label {
    color: #9c8490;
    font-size: 13px;
}
.stat-value {
    font-family: 'Jua', sans-serif;
    color: #a86f88;
    font-size: 21px;
    margin-top: 6px;
}
.stButton > button {
    background: #d991ab;
    color: white;
    border: none;
    border-radius: 14px;
    font-weight: 800;
    min-height: 44px;
}
.stButton > button:hover {
    background: #bd7894;
    color: white;
    border: none;
}
div[data-baseweb="select"] > div {
    border-radius: 13px;
    border-color: #e8cbd4;
}
.note {
    background: #fff3df;
    padding: 16px;
    border-radius: 16px;
    color: #81694e;
    font-size: 13px;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 상단
# -----------------------------
st.markdown("""
<div class="hero">
    <div style="font-size:22px">✦ · ˚ ✧ · ˚ ✦</div>
    <div class="hero-title">🐹 먼작귀 MBTI 도감 🐰</div>
    <div class="hero-sub">
        16가지 MBTI, 16명의 대표 캐릭터!<br>
        나와 가장 잘 어울리는 먼작귀 친구를 만나 보세요.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">📖 도감에 나를 등록해 보자!</div>',
    unsafe_allow_html=True
)

left, right = st.columns([3, 1])

with left:
    selected_mbti = st.selectbox(
        "나의 MBTI를 선택해 주세요",
        list(mbti_data.keys()),
        index=7,
    )

with right:
    st.write("")
    st.write("")
    open_button = st.button("✨ 도감 열기", use_container_width=True)

if "active_mbti" not in st.session_state:
    st.session_state.active_mbti = "ENFP"

if open_button:
    st.session_state.active_mbti = selected_mbti
    st.session_state.show_celebration = True

active = st.session_state.active_mbti
result = mbti_data[active]
character = characters[result["character"]]

if st.session_state.get("show_celebration", False):
    st.balloons()
    st.toast("새로운 먼작귀 도감을 발견했어요!", icon="🎉")
    st.session_state.show_celebration = False

st.markdown(
    '<div class="section-title">💗 나의 대표 캐릭터</div>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="card">
    <div class="card-top">
        <span>CHIikawa FRIENDS · CHARACTER BOOK</span>
        <span>No. {character["no"]}</span>
    </div>
    <div class="card-body">
        <div class="avatar" style="background:{character["color"]}">
            {character["emoji"]}
        </div>
        <div class="char-name">{html.escape(result["character"])}</div>
        <span class="pill">{active}</span>
        <span class="pill">{html.escape(result["title"])}</span>
        <p style="font-size:17px;font-weight:700;margin-top:15px">
            {html.escape(character["keywords"][0])}
            · {html.escape(character["keywords"][1])}
            · {html.escape(character["keywords"][2])}
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# 핵심 지표
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="stat">
        <div class="stat-label">나의 MBTI</div>
        <div class="stat-value">{active}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="stat">
        <div class="stat-label">성격 유형</div>
        <div class="stat-value">{html.escape(result["title"])}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="stat">
        <div class="stat-label">도감 번호</div>
        <div class="stat-value">No. {character["no"]}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">🔎 캐릭터와 MBTI 알아보기</div>',
    unsafe_allow_html=True
)

a, b = st.columns(2)

with a:
    st.markdown('<div class="info">', unsafe_allow_html=True)
    st.markdown("### 🌷 캐릭터 소개")
    st.write(character["desc"])
    st.markdown("**대표 키워드**")
    for keyword in character["keywords"]:
        st.markdown(
            f'<span class="pill">{html.escape(keyword)}</span>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

with b:
    st.markdown('<div class="info">', unsafe_allow_html=True)
    st.markdown(f"### 🧠 {active} · {result['title']}")
    st.write(result["personality"])
    st.markdown("**이 유형의 강점**")
    st.write(result["strength"])
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">💌 이 캐릭터가 나와 어울리는 이유</div>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="info" style="min-height:0">
    <div style="font-size:25px;text-align:center">✨ {active} × {html.escape(result["character"])} ✨</div>
    <p style="text-align:center;font-size:16px">
        {html.escape(result["reason"])}
    </p>
    <p style="text-align:center;color:#9a7888;font-size:13px">
        캐릭터의 특징과 MBTI 성향을 연결한 재미용 해석이에요.
    </p>
</div>
""", unsafe_allow_html=True)

# 전체 도감
st.markdown(
    '<div class="section-title">📚 전체 MBTI 캐릭터 도감</div>',
    unsafe_allow_html=True
)
st.write("다른 MBTI에는 어떤 캐릭터가 배정되었는지 살펴보세요.")

filter_type = st.selectbox(
    "도감 필터",
    ["전체 보기"] + list(mbti_data.keys()),
)

if filter_type == "전체 보기":
    visible_types = list(mbti_data.keys())
else:
    visible_types = [filter_type]

for start in range(0, len(visible_types), 4):
    group = visible_types[start:start + 4]
    cols = st.columns(4)

    for col, mbti in zip(cols, group):
        data = mbti_data[mbti]
        char = characters[data["character"]]

        with col:
            st.markdown(f"""
            <div style="
                background:white;
                border:1px solid #eed9e2;
                border-radius:18px;
                padding:13px 8px;
                text-align:center;
                margin-bottom:12px;
                min-height:180px;
            ">
                <div style="font-size:11px;color:#aa8b9b">
                    No. {char["no"]}
                </div>
                <div style="
                    font-size:43px;
                    background:{char["color"]};
                    border-radius:50%;
                    width:75px;
                    height:75px;
                    margin:8px auto;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                ">{char["emoji"]}</div>
                <div style="font-weight:900;color:#91647a">{mbti}</div>
                <div style="font-size:13px;margin-top:4px">
                    {html.escape(data["character"])}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"{mbti} 보기", key=f"view_{mbti}",
                         use_container_width=True):
                st.session_state.active_mbti = mbti
                st.rerun()

st.markdown("---")

st.markdown("""
<div class="note">
    <b>🍮 도감 이용 안내</b><br>
    이 도감은 먼작귀 캐릭터의 특징을 참고해 MBTI 유형과 연결한 팬메이드 스타일의 콘텐츠예요.
    공식 MBTI 설정은 아니며, 일부 조연의 성격 해석은 제한된 등장 장면을 바탕으로 한
    창작적 해석이에요. MBTI는 사람의 모든 성격을 결정하지 않아요.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center;color:#b49ba7;font-size:13px;margin-top:24px">
    made with ♡ · Chiikawa MBTI Friends
</p>
""", unsafe_allow_html=True)
