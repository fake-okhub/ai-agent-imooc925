# 导入依赖
# 使用RetryOutputParser进行自动重试
from langchain.output_parsers import RetryOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAI
from pydantic import BaseModel, Field

template = """Based on the user question, provide an Action and Action Input for what step should be taken.
{format_instructions}
Question: {query}
Response:"""


class Action(BaseModel):
    action: str = Field(description="action to take")
    action_input: str = Field(description="input to the action")


parser = PydanticOutputParser(pydantic_object=Action)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
# 假设的用户输入合成提示值
prompt_value = prompt.format_prompt(query="北京今天天气如何?")

# 假设得到的一个错误回答，不符合pydantic的字段要求
bad_response = '{"action": "search"}'
# 运行抛出错误
#try:
#    parser.parse(bad_response)
#except OutputParserException as e:
#    print(e)

# 使用RetryOutputParser实现错误重试
# 定义使用哪个模型进行重试
retry_parser = RetryOutputParser.from_llm(parser=parser, llm=OpenAI(temperature=0,api_key=os.environ.get("OPENAI_API_KEY"),base_url=os.environ.get("OPENAI_API_BASE"),))
# 传入错误信息以及原始的提示值
retry_parser.parse_with_prompt(bad_response, prompt_value)
