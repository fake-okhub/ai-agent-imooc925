# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel

joke_chain = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话") | llm
poem_chain = (
    ChatPromptTemplate.from_template("给我写一首关于{topic}的绝句") | llm
)

map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

map_chain.invoke({"topic": "程序员"})