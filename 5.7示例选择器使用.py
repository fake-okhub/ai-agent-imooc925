# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 


# 根据输入的提示词长度综合计算最终长度，智能截取或者添加提示词的示例
# Example of intelligently intercepting or adding prompts by calculating the final length based on the length of the input prompts.
from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

#假设已经有这么多的提示词示例组：
# Suppose there are so many prompt examples:
examples = [
    {"input":"happy","output":"sad"},
    {"input":"tall","output":"short"},
    {"input":"sunny","output":"gloomy"},
    {"input":"windy","output":"calm"},
    {"input":"高兴","output":"悲伤"}
]

#构造提示词模板
# Construct prompt template
example_prompt = PromptTemplate(
    input_variables=["input","output"],
    template="原词：{input}\n反义：{output}"
)

#调用长度示例选择器
# Call the length example selector
example_selector = LengthBasedExampleSelector(
    #传入提示词示例组
    # Pass in the prompt example group
    examples=examples,
    #传入提示词模板
    example_prompt=example_prompt,
    #设置格式化后的提示词最大长度
    # Set the maximum length of the formatted prompt
    max_length=25,
    #内置的get_text_length,如果默认分词计算方式不满足，可以自己扩展
    # Built-in get_text_length, if the default word segmentation calculation method does not meet the requirements, you can expand it yourself
    #get_text_length:Callable[[str],int] = lambda x:len(re.split("\n| ",x))
)


#使用小样本提示词模版来实现动态示例的调用
# Use the small sample prompt template to realize the call of dynamic examples
dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个输入词的反义词",
    suffix="原词：{adjective}\n反义：",
    input_variables=["adjective"]
)