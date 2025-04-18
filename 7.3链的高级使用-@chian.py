# 导入DeepSeek聊天模型
from langchain_deepseek import ChatDeepSeek
# 导入字符串输出解析器
from langchain_core.output_parsers import StrOutputParser
# 导入chain装饰器，用于创建自定义链
from langchain_core.runnables import chain
from langchain_core.prompts import ChatPromptTemplate

# 初始化DeepSeek大语言模型
llm = ChatDeepSeek(
    model="Pro/deepseek-ai/DeepSeek-V3",  # 使用DeepSeek模型
    temperature=0,  # 设置温度为0，使输出更确定性
    api_key=os.environ.get("DEEPSEEK_API_KEY"),  # 从环境变量获取API密钥
    api_base=os.environ.get("DEEPSEEK_API_BASE"),  # 从环境变量获取API基础URL
)

# 创建第一个提示模板：请求关于特定主题的笑话
prompt1 = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
# 创建第二个提示模板：询问笑话的主题是什么
prompt2 = ChatPromptTemplate.from_template("What is the subject of this joke: {joke}")


# 使用@chain装饰器定义一个自定义链
@chain
def custom_chain(text):
    # 步骤1: 将输入文本填充到第一个提示模板中
    prompt_val1 = prompt1.invoke({"topic": text})
    # 步骤2: 使用DS模型生成关于指定主题的笑话
    output1 = llm.invoke(prompt_val1)
    # 步骤3: 将模型输出解析为字符串
    parsed_output1 = StrOutputParser().invoke(output1)
    
    # 步骤4: 创建第二个处理链，用于分析笑话主题
    # 这个链将提示模板、DS模型和字符串解析器串联起来
    chain2 = prompt2 | llm | StrOutputParser()
    
    # 步骤5: 将第一步生成的笑话作为输入，让第二个链分析其主题
    return chain2.invoke({"joke": parsed_output1})


# 调用自定义链，输入主题"bears"（熊）
# 整个过程：
# 1. 先生成一个关于熊的笑话
# 2. 然后分析这个笑话的主题是什么
# 3. 返回分析结果
custom_chain.invoke("bears")