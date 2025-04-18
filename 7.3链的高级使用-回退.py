# 导入必要的库
from unittest.mock import patch  # 导入mock库，用于模拟函数行为
from langchain_anthropic import ChatAnthropic  # 导入Anthropic的语言模型接口
from langchain_openai import ChatOpenAI  # 导入OpenAI的语言模型接口
import httpx  # HTTP客户端库
from openai import RateLimitError  # OpenAI的速率限制错误类

# 创建模拟HTTP请求和响应对象，用于构造模拟的API错误
request = httpx.Request("GET", "/")  # 创建一个GET请求
response = httpx.Response(200, request=request)  # 创建一个状态码为200的响应
# 创建一个OpenAI速率限制错误对象，用于模拟API调用超出速率限制的情况
error = RateLimitError("rate limit", response=response, body="")

# 初始化OpenAI模型
# 注意：设置max_retries = 0是为了避免在遇到速率限制等错误时自动重试
openai_llm = ChatOpenAI(
    model="gpt-4",  # 使用GPT-4模型
    temperature=0,  # 设置温度为0，使输出更确定性
    api_key=os.environ.get("OPENAI_API_KEY"),  # 从环境变量获取API密钥
    base_url=os.environ.get("OPENAI_API_BASE"),  # 从环境变量获取基础URL
)

# 初始化Anthropic模型作为备用选项
anthropic_llm = ChatAnthropic(
    model='claude-3-5-sonnet-latest',  # 使用Claude 3.5 Sonnet模型
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # 从环境变量获取API密钥
    base_url=os.environ.get("ANTHROPIC_BASE_URL"),  # 从环境变量获取基础URL
)

# 创建带有备用选项的语言模型
# 如果主模型(OpenAI)失败，将自动尝试使用备用模型(Anthropic)
llm = openai_llm.with_fallbacks([anthropic_llm])

# 如果不设置回退机制，当API调用超量就会直接报错
# with patch("openai.resources.chat.completions.Completions.create", side_effect=error):
#    try:
#        print(llm.invoke("Why did the chicken cross the road?"))
#    except RateLimitError:
#        print("Hit error")

# 测试备用机制 - 使用中文问题
# 使用patch模拟OpenAI API调用失败（抛出速率限制错误）
with patch("openai.resources.chat.completions.Completions.create", side_effect=error):
    try:
        # 尝试调用语言模型回答中文问题
        # 由于OpenAI被模拟为失败，应该自动切换到Anthropic模型
        print(llm.invoke("为什么程序员需要学会python?"))
    except RateLimitError:
        # 如果仍然遇到错误（备用机制失败），则打印错误信息
        print("Hit error")
