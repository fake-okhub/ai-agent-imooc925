# 引入依赖包，这里的pydantic版本为v2
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field, model_validator
from langchain_deepseek import ChatDeepSeek
# 使用deepseek
llm = ChatDeepSeek(
    model="Pro/deepseek-ai/DeepSeek-V3",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    api_base=os.environ.get("DEEPSEEK_API_BASE"),
)

# 定义一个名为Joke的数据模型
# 必须要包含的数据字段：铺垫(setup)、抖包袱(punchline)
class Joke(BaseModel):
    setup: str = Field(description="笑话中的铺垫问题，必须以?结尾")
    punchline: str = Field(description="笑话中回答铺垫问题的部分，通常是一种抖包袱方式回答铺垫问题，例如谐音、会错意等")


# 实例化解析器、提示词模板
parser = JsonOutputParser(pydantic_object=Joke)
# 注意，提示词模板中需要部分格式化解析器的格式要求format_instructions
prompt = PromptTemplate(
    template="回答用户的查询.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 使用LCEL语法组合一个简单的链
chain = prompt | llm | parser
output = chain.invoke({"query": "给我讲一个笑话"})
print(output)
# parser.get_format_instructions()
#for s in chain.stream({"query":"给我讲一个关于程序员编程的笑话"}):
#    print(s)