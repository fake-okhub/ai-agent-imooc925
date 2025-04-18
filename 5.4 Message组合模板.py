from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 直接创建消息
# create messages directly
sy = SystemMessage(
  content="你是一个起名大师",
  additional_kwargs={"大师姓名": "陈瞎子"}
)

hu = HumanMessage(
  content="请问大师叫什么?"
)
ai = AIMessage(
  content="我叫陈瞎子"
)
[sy,hu,ai]