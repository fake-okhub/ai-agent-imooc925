# 使用partial可以部分格式化提示词
# 这在有些场景非常有用
# 比如当你希望提示词被执行的时候，始终是当前时间
from datetime import datetime
from langchain_core.prompts import PromptTemplate

def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")


prompt = PromptTemplate(
    template="Tell me a {adjective} joke about the day {date}",
    input_variables=["adjective", "date"],
)
partial_prompt = prompt.partial(date=_get_datetime)
print(partial_prompt.format(adjective="funny"))