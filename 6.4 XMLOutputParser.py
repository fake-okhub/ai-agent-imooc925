 # 引入依赖包
from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek
# 使用deepseek
llm = ChatDeepSeek(
    model="Pro/deepseek-ai/DeepSeek-V3",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    api_base=os.environ.get("DEEPSEEK_API_BASE"),
)
actor_query = "Generate the shortened filmography for Tom Hanks."

parser = XMLOutputParser()

# We will add these instructions to the prompt below
#parser = XMLOutputParser(tags=["movies", "actor", "film", "name", "genre"])

# We will add these instructions to the prompt below
# parser.get_format_instructions()
prompt = PromptTemplate(
    template="""{query}\n{format_instructions}""",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | llm | parser

output = chain.invoke({"query": actor_query})
print(output)