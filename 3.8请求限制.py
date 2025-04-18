#速率限制需要langchain-core >= 0.2.24
# langchain中的InMemoryRateLimiter只只能限制单位时间内的请求数量
# 无法处理根据请求大小来限制的情况
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_anthropic import ChatAnthropic
import time

rate_limiter = InMemoryRateLimiter(
    requests_per_second=1,  # 每1秒请求一次
    check_every_n_seconds=0.1,  # 每100毫秒检查一次是否允许
    max_bucket_size=10,  # 控制最大突发大小
)
#定义模型调用
from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(
model='claude-3-5-sonnet-latest',
api_key=os.environ.get("ANTHROPIC_API_KEY"),
base_url=os.environ.get("ANTHROPIC_BASE_URL"),
rate_limiter=rate_limiter #请求速率限制
)
#使用计时器来计算
# 每次请求的时间间隔
for _ in range(5):
    tic = time.time()
    model.invoke("hello")
    toc = time.time()
    print(toc - tic)

