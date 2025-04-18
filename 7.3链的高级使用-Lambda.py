# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 


from operator import itemgetter  # 导入itemgetter函数，用于从字典中提取值

from langchain_core.prompts import ChatPromptTemplate  # 导入聊天提示模板
from langchain_core.runnables import RunnableLambda  # 导入可运行的Lambda函数包装器
from langchain_deepseek import ChatDeepSeek  # 导入DeepSeek聊天模型

# 初始化DeepSeek大语言模型
model = ChatDeepSeek(
    model="Pro/deepseek-ai/DeepSeek-R1",  # 使用DeepSeek-R1模型
    temperature=0,  # 设置温度为0，使输出更确定性
    api_key=os.environ.get("DEEPSEEK_API_KEY"),  # 从环境变量获取API密钥
    api_base=os.environ.get("DEEPSEEK_API_BASE"),  # 从环境变量获取API基础URL
)

# 创建一个简单的聊天提示模板，询问a和b的和
prompt = ChatPromptTemplate.from_template("what is {a} + {b}")

# 构建一个复杂的处理链
chain = (
    {
        # 处理"a"参数:
        # 1. 从输入字典中提取"foo"键的值
        # 2. 将提取的值传递给length_function函数(假设这个函数计算字符串长度)
        "a": itemgetter("foo") | RunnableLambda(length_function),
        
        # 处理"b"参数:
        # 1. 创建一个包含两个键值对的字典:
        #    - "text1": 从输入字典中提取"foo"键的值
        #    - "text2": 从输入字典中提取"bar"键的值
        # 2. 将这个字典传递给multiple_length_function函数
        #    (假设这个函数计算两个文本的总长度)
        "b": {"text1": itemgetter("foo"), "text2": itemgetter("bar")}
        | RunnableLambda(multiple_length_function),
    }
    | prompt  # 将处理后的"a"和"b"值填入提示模板
    | model  # 将填充后的提示发送给DeepSeek模型生成回答
)

# 调用链处理流程，输入一个包含"foo"和"bar"键的字典
# 整个过程:
# 1. 计算"bar"字符串的长度作为a的值
# 2. 计算"bar"和"gah"字符串的总长度作为b的值
# 3. 将这些值填入提示"what is {a} + {b}"
# 4. 让DeepSeek模型回答这个问题
chain.invoke({"foo": "bar", "bar": "gah"})