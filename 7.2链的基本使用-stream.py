# 定义LLM
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    api_base=os.environ.get("DEEPSEEK_API_BASE"),
)

# 使用管道操作符来实现一条链
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("讲一个关于{topic}的笑话,不要有任何解释")

chain = prompt | llm | StrOutputParser()

for chunk in chain.stream("小狗"):
    print(chunk, end="|")