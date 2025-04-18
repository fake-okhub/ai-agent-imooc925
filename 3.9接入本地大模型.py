# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama2-chinese:latest",
    temperature=0,
)
llm.invoke("你好")