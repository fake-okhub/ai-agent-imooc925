# 纳美星语网址 https://learnnavi.org/

from typing import Iterable
from langchain_anthropic.chat_models import ChatAnthropic
from langchain_core.messages import AIMessage, AIMessageChunk
import re

model = ChatAnthropic(
model='claude-3-5-sonnet-latest',
api_key=os.environ.get("ANTHROPIC_API_KEY"),
base_url=os.environ.get("ANTHROPIC_BASE_URL"),
)

def parse(ai_message: AIMessage) -> str:
    """Convert message to Na'vi style language."""
    content = ai_message.content
    
    # 纳美语特征转换规则
    navi_rules = {
        # 常见问候语转换
        r'\b[Hh]ello\b': 'Kaltxì',
        r'\b[Hh]i\b': 'Kaltxì',
        r'\b[Tt]hank you\b': 'Irayo',
        r'\b[Gg]oodbye\b': 'Eywa ngahu',
        
        # 添加纳美语特征的后缀
        r'\b(friend|friends)\b': 'eylan',
        r'\b(brother|brothers)\b': 'tsmukan',
        r'\b(sister|sisters)\b': 'tsmuke',
        
        # 添加纳美语语气词
        r'[!.]\s*$': ' kxe!',
        r'\?\s*$': ' srak?',
        
        # 在某些词前添加特征前缀
        r'\b(beautiful|pretty)\b': 'na\'vi',
        r'\b(sacred|holy)\b': 'txe\'lan',
    }
    
    # 应用转换规则
    result = content
    for pattern, replacement in navi_rules.items():
        result = re.sub(pattern, replacement, result)
    
    # 添加纳美语特征词缀
    result = f"Oel ngati kameie... {result}"
    
    return result

chain = model | parse
chain.invoke("hello")