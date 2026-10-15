import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="먼작귀 캐릭터 MBTI 도감", page_icon="🐹", layout="wide")

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
.stApp { background: linear-gradient(135deg,#fff4f8 0%,#f4f7ff 52%,#fff9ec 100%); }
h1,h2,h3 { font-family:'Jua',sans-serif !important; }
.hero { padding:1.4rem; border-radius:24px; background:#fffafc; border:2px solid #f2d5e2; text-align:center; }
.pill { display:inline-block; padding:5px 12px; border-radius:999px; background:#eee5ff; color:#59427a; font-weight:700; }
div[data-testid="stVerticalBlockBorderWrapper"] { background:rgba(255,255,255,.76); border-radius:18px; }
</style>
""", unsafe_allow_html=True)

# 이미지 파일은 GitHub 저장소의 assets 폴더에 함께 올려야 표시됩니다.
# MBTI 연결은 재미를 위한 창작 설정이며 공식 성격 유형이 아닙니다.
CHARACTERS = {
    "치이카와": ("🐹", "소심하지만 성실하고, 작은 용기를 모아 나아가는 캐릭터.", "character_poster.png"),
    "우사기": ("🐰", "자유분방하고 에너지가 넘치는 캐릭터.", "character_poster.png"),
    "하치와레": ("🐱", "밝고 다정하며 친구를 응원하는 캐릭터.", "character_poster.png"),
    "랏코": ("🦦", "실력이 뛰어나고 믿음직한 선배 같은 캐릭터.", "character_poster.png"),
    "쿠리만쥬": ("🌰", "느긋하게 먹는 것을 즐기는 어른스러운 캐릭터.", "character_poster.png"),
    "모몽가": ("🐿️", "관심받기를 좋아하고 자기표현이 강한 캐릭터.", "character_poster.png"),
    "시사": ("🦁", "성실하게 배우고 맡은 일을 해내려는 캐릭터.", "character_poster.png"),
    "카니": ("🦀", "조용하고 섬세한 분위기의 캐릭터.", "character_poster.png"),
    "키메라": ("👾", "독특하고 신비로운 모습의 캐릭터.", "chimera.png"),
    "고블린": ("👺", "동굴 등에서 등장하는 개성 있는 캐릭터.", "character_poster.png"),
    "갑옷씨": ("🛡️", "먼작귀 세계에서 여러 일을 맡아 돕는 캐릭터.", "armored_soldiers.png"),
    "파자마 파티즈": ("🎉", "파자마 파티와 관련된 개성 있는 캐릭터들.", "pajama_party.png"),
    "섬 아저씨": ("🍚", "섬에서 식당을 운영하는 인물로 소개되는 캐릭터.", "shim_ojisan.png"),
    "세이렌": ("🧜", "노래를 잘하며 섬의 이야기에서 중요한 역할을 하는 캐릭터.", "seiren.png"),
    "한잎과 두잎": ("🌿", "섬에서 함께 등장하는 두 캐릭터.", "hanip_duip.png"),
    "인어": ("🐟", "세이렌과 함께 등장하는 인어 캐릭터.", "mermaid.png"),
    "그 아이": ("⭐", "독특한 분위기와 예측하기 어려운 면이 있는 캐릭터.", "yellow_creature.png"),
    "큰 흰색 캐릭터": ("🤍", "숲 장면에 등장하는 커다란 흰색 캐릭터.", "white_creature.png"),
}

MBTI = {
    "INTJ": ("갑옷씨","전략가","계획을 세우고 효율적인 방법을 찾는 편이에요.",["장기적인 관점","체계적인 계획","독립적인 판단"]),
    "INTP": ("그 아이","논리 탐구가","호기심이 많고 독특한 방식으로 생각해요.",["분석적 사고","새로운 관점","탐구심"]),
    "ENTJ": ("랏코","통솔자","목표를 정하고 주도적으로 이끄는 모습과 어울려요.",["목표 지향","결단력","조직력"]),
    "ENTP": ("우사기","변론가","틀에 얽매이지 않고 즉흥적으로 아이디어를 펼쳐요.",["재치","도전 정신","발상 전환"]),
    "INFJ": ("카니","옹호자","조용히 관찰하며 의미와 마음을 중요하게 여겨요.",["통찰력","배려","가치 중심"]),
    "INFP": ("치이카와","중재자","섬세한 감정과 진심을 소중히 여겨요.",["공감","상상력","진정성"]),
    "ENFJ": ("하치와레","선도자","친구를 격려하고 함께 나아가려는 모습과 어울려요.",["소통","격려","협력"]),
    "ENFP": ("파자마 파티즈","활동가","새로운 경험과 즐거운 교류를 좋아해요.",["열정","창의성","친화력"]),
    "ISTJ": ("시사","현실주의자","책임감을 가지고 차근차근 배우고 실천해요.",["성실함","책임감","꾸준함"]),
    "ISFJ": ("한잎과 두잎","수호자","함께하며 서로를 챙기는 모습과 어울려요.",["세심함","신뢰","협력"]),
    "ESTJ": ("갑옷씨","경영자","규칙과 역할을 중시하고 일을 체계적으로 처리해요.",["실행력","조직력","책임감"]),
    "ESFJ": ("하치와레","집정관","주변 사람들과 조화를 이루고 서로 돕는 것을 중요하게 생각해요.",["친절함","협동","배려"]),
    "ISTP": ("쿠리만쥬","장인","차분하게 상황을 살피고 실용적인 방법을 찾아요.",["관찰력","실용성","침착함"]),
    "ISFP": ("모몽가","모험가","자기만의 취향과 순간의 감정을 중요하게 여겨요.",["감각","유연함","개성"]),
    "ESTP": ("세이렌","사업가","상황에 빠르게 반응하고 행동하는 모습과 어울려요.",["대담함","적응력","행동력"]),
    "ESFP": ("인어","연예인","표현력이 있고 주변과 함께 움직이는 모습을 떠올리게 해요.",["표현력","활기","즉흥성"]),
}

def show_character(name, width=None):
    emoji, description, filename = CHARACTERS[name]
    path = ASSET_DIR / filename
    if path.exists():
        try:
            st.image(Image.open(path), caption=name, use_container_width=(width is None), width=width)
            return
        except Exception:
            pass
    st.markdown(f"<div style='text-align:center;font-size:70px'>{emoji}</div>", unsafe_allow_html=True)
    st.caption("이미지 파일을 찾을 수 없어요. GitHub에 assets 폴더가 함께 올라갔는지 확인해 주세요.")

st.markdown('<div class="hero"><h1>🐹 친구 닮은 먼작귀 캐릭터 MBTI 도감 🐰</h1><p>MBTI와 어울리는 캐릭터를 재미로 찾아봐요!</p></div>', unsafe_allow_html=True)
st.write("")

with st.sidebar:
    st.header("🔎 MBTI 선택")
    selected = st.selectbox("내 MBTI를 골라 주세요", list(MBTI.keys()), index=5)
    st.markdown("---")
    st.caption("도감의 이미지는 사용자가 제공한 이미지 파일을 사용합니다.")

name, type_title, personality, strengths = MBTI[selected]
emoji, description, filename = CHARACTERS[name]

left, right = st.columns([1, 1.35], gap="large")
with left:
    with st.container(border=True):
        st.markdown(f'<span class="pill">{selected}</span>', unsafe_allow_html=True)
        st.subheader(f"오늘의 캐릭터: {name}")
        show_character(name)
        st.write(description)

with right:
    st.markdown(f"## {selected} · {type_title}")
    st.write(personality)
    st.markdown("### ✨ 어울리는 특징")
    for item in strengths:
        st.markdown(f"- {item}")
    st.info("이 매칭은 재미를 위한 창작 해석이며, 공식 설정이나 심리검사 결과가 아닙니다.")

st.divider()
st.markdown("## 📚 16가지 MBTI 전체 도감")
st.caption("카드를 눌러 유형을 선택하면 위 프로필을 바꿀 수 있어요.")
types = list(MBTI.keys())
for start in range(0, len(types), 4):
    cols = st.columns(4, gap="medium")
    for col, mbti in zip(cols, types[start:start+4]):
        char_name, title, desc, _ = MBTI[mbti]
        with col:
            with st.container(border=True):
                st.markdown(f"**{mbti} · {title}**")
                show_character(char_name, width=180)
                st.caption(f"캐릭터: {char_name}")
                st.write(desc)
                if st.button("이 유형 보기", key=f"view_{mbti}", use_container_width=True):
                    st.session_state["chosen_mbti"] = mbti
                    st.rerun()

if "chosen_mbti" in st.session_state:
    st.caption(f"도감에서 선택한 유형: {st.session_state['chosen_mbti']} — 왼쪽 메뉴에서 해당 유형을 선택해 자세히 볼 수 있어요.")

st.divider()
st.markdown("## 🖼️ 추가 캐릭터 도감")
extra_names = ["섬 아저씨", "세이렌", "한잎과 두잎", "인어", "갑옷씨", "파자마 파티즈", "키메라", "그 아이", "큰 흰색 캐릭터"]
for start in range(0, len(extra_names), 3):
    cols = st.columns(3)
    for col, char_name in zip(cols, extra_names[start:start+3]):
        with col:
            with st.container(border=True):
                st.subheader(char_name)
                show_character(char_name)
                st.caption(CHARACTERS[char_name][1])

st.caption("이미지 파일은 사용자가 제공한 자료를 사용합니다. 캐릭터 및 이미지 권리는 해당 권리자에게 있습니다. 이 앱은 비공식 팬 프로젝트입니다.")
