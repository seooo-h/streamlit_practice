import streamlit as st

st.title("간단한 짱구 퀴즈")

# 객관식 퀴즈
st.subheader("퀴즈 1: 다음 보기 중 떡잎마을 방법대가 아닌 사람은?")
options = ["짱구", "철수", "유리", "맹구", "수지"]
answer_mc = st.radio("정답을 선택하세요:", options)

if answer_mc:
    if answer_mc == "수지":
        st.success("정답입니다!👍")
    else:
        st.error("틀렸습니다.💀")

# 주관식 퀴즈
st.subheader("퀴즈 2: 짱구가 다니는 유치원은?")
answer_text = st.text_input("정답을 입력하세요:")

if answer_text:
    if answer_text.strip().lower() == "떡잎 유치원":
        st.success("정답입니다!👍")
    else:
        st.error("틀렸습니다.💀")
