# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 
# #####################################################
# #                                                   #
# #                注意：此为本地演示代码                 #       # #
# #                                                   #
# #####################################################

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

from langchain_chroma.vectorstores import Chroma
from langchain_graph_retriever.transformers import ShreddingTransformer


vector_store = Chroma.from_documents(
    documents=list(ShreddingTransformer().transform_documents(animals)),
    embedding=embeddings,
    collection_name="animals",
)

from graph_retriever.strategies import Eager
from langchain_graph_retriever import GraphRetriever

traversal_retriever = GraphRetriever(
    store = vector_store,
    edges = [("habitat", "habitat"), ("origin", "origin")],
    strategy = Eager(k=5, start_k=1, max_depth=2),
)

results = traversal_retriever.invoke("what animals could be found near a capybara?")

for doc in results:
    print(f"{doc.id}: {doc.page_content}")