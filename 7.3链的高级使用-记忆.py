# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # 导入聊天提示模板和消息占位符
from langchain_core.runnables.history import RunnableWithMessageHistory  # 导入带历史记录的可运行组件
from langchain_deepseek import ChatDeepSeek
import os

llm = ChatDeepSeek(
    model="Pro/deepseek-ai/DeepSeek-V3",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    api_base=os.environ.get("DEEPSEEK_API_BASE"),
)

# 创建聊天提示模板，包含系统提示、历史记录和用户问题
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个擅长{ability}的助手"),  # 系统角色提示，使用ability变量定义助手专长
    MessagesPlaceholder(variable_name="history"),  # 放置历史消息的占位符
    ("human", "{question}"),  # 用户问题的占位符
])

# 将提示模板与DS模型连接成一个链
chain = prompt | llm

# 创建带有消息历史功能的可运行链
chain_with_history = RunnableWithMessageHistory(
    chain,  # 基础链
    # 使用上一个示例中定义的get_by_session_id函数获取历史记录
    get_by_session_id,
    input_messages_key="question",  # 指定输入消息的键名
    history_messages_key="history",  # 指定历史消息的键名
)

# 首次调用链，询问余弦的含义
print(chain_with_history.invoke(  # noqa: T201
    {"ability": "math", "question": "余弦函数是什么意思？"},  # 输入参数
    config={"configurable": {"session_id": "foo"}}  # 配置会话ID为"foo"
))

# 打印存储中的历史记录
# 此时应包含第一次对话的问题和回答
print(store)  # noqa: T201

# 第二次调用链，询问余弦的反函数
# 由于使用相同的会话ID，模型可以参考前一次对话的上下文
print(chain_with_history.invoke(  
    {"ability": "math", "question": "它的反函数是什么？"},  # 输入参数
    config={"configurable": {"session_id": "foo"}}  # 使用相同的会话ID
))

# 再次打印存储中的历史记录
# 此时应包含两次对话的完整历史
print(store)  