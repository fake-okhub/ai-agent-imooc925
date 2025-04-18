#字符模板
# string template
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("你是一个{name},帮我起1个具有{county}特色的{sex}名字")
prompts = prompt.format(name="算命大师",county="法国",sex="女孩")
print(prompts)