from openai import OpenAI
import streamlit as st

with st.sidebar:
    api_key = st.text_input("API：", key="chatbot_api_key", type="password")


st.title("💬 科技文献检索大模型")
st.caption("🚀 一个科技检索文献大模型")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "请给我一个相关的问题"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not api_key:
        st.info("正在添加完善")
        st.stop()

    client = OpenAI(api_key=api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
