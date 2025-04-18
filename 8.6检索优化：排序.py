# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 
# #####################################################
# #                                                   #
# #                注意：此为本地演示代码                 #       # #
# #                                                   #
# #####################################################


from langchain_openai import OpenAIEmbeddings
import os
embeddings_model = OpenAIEmbeddings(
    model="BAAI/bge-m3",
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url=os.environ.get("DEEPSEEK_API_BASE")+"/v1",
)

from langchain_core.vectorstores import InMemoryVectorStore

texts = [
    "西湖是杭州著名的旅游景点。",
    "我最喜欢的歌曲是《月亮代表我的心》。",
    "故宫是北京最著名的古迹之一。",
    "这是一篇关于北京故宫历史的文档。",
    "我非常喜欢去电影院看电影。",
    "北京故宫的藏品数量超过一百万件。",
    "这只是一段随机文本。",
    "《三国演义》是中国四大名著之一。",
    "紫禁城是故宫的别称，位于北京。",
    "故宫博物院每年接待游客数百万人次。",
]

# 创建检索器
retriever = InMemoryVectorStore.from_texts(texts, embedding=embeddings_model).as_retriever(
    search_kwargs={"k": 10}
)
query = "请告诉我关于故宫的信息？"

# 获取按相关性排序的文档
docs = retriever.invoke(query)
for doc in docs:
    print(f"- {doc.page_content}")


from langchain_community.document_transformers import LongContextReorder

# 重新排序文档：
# 相关性较低的文档将位于列表中间
# 相关性较高的文档将位于开头和结尾
reordering = LongContextReorder()
reordered_docs = reordering.transform_documents(docs)

# 确认相关性高的文档位于开头和结尾
for doc in reordered_docs:
    print(f"- {doc.page_content}")
