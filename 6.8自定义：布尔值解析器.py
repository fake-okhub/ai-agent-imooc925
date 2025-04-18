# 通过继承BaseOutputParser来实现

from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import BaseOutputParser


# [bool] 描述了一个泛型的参数化。
# 它基本上说明了解析的返回类型是什么
# 在这种情况下，返回类型为 True 或 False
# 自定义解析器将YES、NO字符串解析为布尔值
class BooleanOutputParser(BaseOutputParser[bool]):
    """Custom boolean parser."""

    true_val: str = "YES"
    false_val: str = "NO"

    def parse(self, text: str) -> bool:
        cleaned_text = text.strip().upper()
        if cleaned_text not in (self.true_val.upper(), self.false_val.upper()):
            raise OutputParserException(
                f"BooleanOutputParser expected output value to either be "
                f"{self.true_val} or {self.false_val} (case-insensitive). "
                f"Received {cleaned_text}."
            )
        return cleaned_text == self.true_val.upper()
#设置统一接口名
    @property
    def _type(self) -> str:
        return "boolean_output_parser"

# 如果传入值不是YES NO会报错
#try:
#    parser.invoke("MEOW")
#except Exception as e:
#    print(f"Triggered an exception of type: {type(e)}")

# 我们也可以更换参数
# parser = BooleanOutputParser(true_val="OKAY")
# parser.invoke("OKAY")


# 简单调用
parser = BooleanOutputParser()
parser.invoke("YES")
