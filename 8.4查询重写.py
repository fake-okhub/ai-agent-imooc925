# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 
# #####################################################
# #                                                   #
# #                注意：此为本地演示代码                 #       # #
# #                                                   #
# #####################################################

# Build a sample vectorDB
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load blog post
loader = WebBaseLoader("https://python.langchain.com/docs/how_to/MultiQueryRetriever/")
data = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(data)

# VectorDB
vectordb = Chroma.from_documents(documents=splits, embedding=embeddings_model)


from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_deepseek import ChatDeepSeek
import os

llm = ChatDeepSeek(
    model="Pro/deepseek-ai/DeepSeek-V3",
    temperature=0,
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    api_base=os.environ.get("DEEPSEEK_API_BASE"),
)

question = "如何让用户查询更准确？"
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectordb.as_retriever(), llm=llm
)

unique_docs = retriever_from_llm.invoke(question)
print(unique_docs)
len(unique_docs)