# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 



# 导入必要的库
from langchain_anthropic import ChatAnthropic  # 导入Anthropic的语言模型接口
from langchain_core.output_parsers import StrOutputParser  # 导入字符串输出解析器
from langchain_core.prompts import PromptTemplate  # 导入提示模板

# 初始化Claude模型，使用环境变量中的API密钥和基础URL
claudeLLM = ChatAnthropic(
    model='claude-3-5-sonnet-latest',  # 使用Claude 3.5 Sonnet模型
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # 从环境变量获取API密钥
    base_url=os.environ.get("ANTHROPIC_BASE_URL")  # 从环境变量获取基础URL
)

# 创建分类链 - 用于确定问题类型
chain = (
    # 创建提示模板，要求模型将问题分类为LangChain、Anthropic或Other
    PromptTemplate.from_template(
        """根据下面的用户问题，将其分类为 `LangChain`、`Anthropic` 或 `Other`。

请只回复一个词作为答案。

<question>
{question}
</question>

分类结果:"""
    )
    | claudeLLM  # 将提示发送给Claude模型
    | StrOutputParser()  # 解析模型的输出为纯文本
)

# 创建LangChain专家链 - 模拟Harrison Chase(LangChain创始人)的回答风格
langchain_chain = PromptTemplate.from_template(
    """你是一位LangChain专家。 \
所有回答都必须以"正如Harrison Chase告诉我的"开头。 \
请回答以下问题:

问题: {question}
回答:"""
) | claudeLLM  # 将提示发送给Claude模型

# 创建Anthropic专家链 - 模拟Dario Amodei(Anthropic创始人)的回答风格
anthropic_chain = PromptTemplate.from_template(
    """你是一位Anthropic专家。 \
所有回答都必须以"正如Dario Amodei告诉我的"开头。 \
请回答以下问题:

问题: {question}
回答:"""
) | claudeLLM  # 将提示发送给Claude模型

# 创建通用回答链 - 用于处理其他类型的问题
general_chain = PromptTemplate.from_template(
    """请回答以下问题:

问题: {question}
回答:"""
) | claudeLLM  # 将提示发送给Claude模型

# 自定义路由函数 - 根据问题分类结果选择合适的回答链
def route(info):
    # 根据分类结果选择相应的专家链
    if "anthropic" in info["topic"].lower():  # 如果问题与Anthropic相关
        return anthropic_chain  # 使用Anthropic专家链
    elif "langchain" in info["topic"].lower():  # 如果问题与LangChain相关
        return langchain_chain  # 使用LangChain专家链
    else:  # 其他类型的问题
        return general_chain  # 使用通用回答链

# 导入RunnableLambda用于创建可运行的函数链
from langchain_core.runnables import RunnableLambda

# 创建完整的处理链
# 1. 首先将问题分类并保留原始问题
# 2. 然后根据分类结果路由到相应的专家链处理
full_chain = {"topic": chain, "question": lambda x: x["question"]} | RunnableLambda(route)

# 调用完整链处理用户问题
# 这个问题会被分类为Anthropic相关，然后由anthropic_chain处理
full_chain.invoke({"question": "我该如何使用Anthropic?"})