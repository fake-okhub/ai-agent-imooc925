# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 


from langchain_core.runnables import RunnableParallel, RunnablePassthrough

# 创建一个可并行运行的处理流程
runnable = RunnableParallel(
    passed=RunnablePassthrough(),  # 第一个处理器：直接传递输入，不做修改
    modified=lambda x: x["num"] + 1,  # 第二个处理器：取出输入中的"num"值并加1
)

# 执行这个处理流程，输入是一个包含"num"字段的字典
runnable.invoke({"num": 1})
# 运行结果：{'passed': {'num': 1}, 'modified': 2}
