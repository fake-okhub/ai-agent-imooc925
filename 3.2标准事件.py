# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 


# 定义模型
from langchain_openai import ChatOpenAI
import os
import asyncio

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
    )
question = "langchain是什么?"

# invoke事件
llm.invoke(question)

# stream事件
for chunk in llm.stream(question):
    print(chunk.content+"|")

# batch事件
llm.batch(["langchain作者是谁？", "Langchain的竞品有哪些？"])

# 异步事件流
async for event in llm.astream_events("介绍下LangChain", version="v2"):
        print(f"event={event['event']} | name={event['name']} | data={event['data']}")