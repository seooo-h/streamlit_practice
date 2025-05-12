import streamlit as st

st.title("간단한 짱구 퀴즈")

# 객관식 퀴즈
st.subheader("퀴즈 1: 다음 보기 중 떡잎마을 방범대가 아닌 사람은?")
options = ["짱구", "철수", "유리", "맹구", "수지"]

# index=None → 처음엔 아무것도 선택되지 않음
answer_mc = st.radio("정답을 선택하세요:", options, index=None)

# 사용자가 선택한 경우만 결과 표시
if answer_mc is not None:
    if answer_mc == "수지":
        st.success("정답입니다!👍")
    else:
        st.error("틀렸습니다.💀")

# 주관식 퀴즈
st.subheader("퀴즈 2: 짱구가 다니는 유치원은?")
answer_text = st.text_input("정답을 입력하세요:")

# 입력이 있는 경우만 결과 표시
if answer_text:
    if answer_text.strip().lower() == "떡잎유치원":
        st.success("정답입니다!👍")
    else:
        st.error("틀렸습니다.💀")
