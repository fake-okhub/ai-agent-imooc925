# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 


# 这是一个自定义解析器，将LLM输出的标记迭代器
# 按逗号分隔转换为字符串列表
def split_into_list(input: Iterator[str]) -> Iterator[List[str]]:
    # 保存部分输入直到遇到逗号
    buffer = ""
    for chunk in input:
        # 将当前块添加到缓冲区
        buffer += chunk
        # 当缓冲区中有逗号时
        while "," in buffer:
            # 在逗号处分割缓冲区
            comma_index = buffer.index(",")
            # 输出逗号之前的所有内容
            yield [buffer[:comma_index].strip()]
            # 保存剩余部分用于下一次迭代
            buffer = buffer[comma_index + 1 :]
    # 输出最后一块
    yield [buffer.strip()]


list_chain = str_chain | split_into_list

for chunk in list_chain.stream({"animal": "熊"}):
    print(chunk, flush=True)
