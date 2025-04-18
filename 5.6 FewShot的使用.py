# zeroshot会导致低质量回答
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
model="gpt-4o-mini", 
temperature=0.0,
openai_api_base = os.getenv("OPENAI_API_BASE"),
openai_api_key = os.getenv("OPENAI_API_KEY")
)

res = model.invoke("What is 2 🦜 9?")
print(res)

#增加示例
#使用FewShotChatMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
#增加示例组
examples = [
    {"input": "2 🦜 2", "output": "4"},
    {"input": "2 🦜 3", "output": "5"},
]
#构造提示词模板
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)
#组合示例与提示词
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)
#打印提示词模板
print(few_shot_prompt.invoke({}).to_messages())

## 最终提示词
final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一位神奇的数学奇才"),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

##重新提问
chain = final_prompt | model
result = chain.invoke({"input": "What is 2 🦜 9?"})
print(result)