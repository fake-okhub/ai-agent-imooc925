# 本地演示代码
# 链接: https://pan.baidu.com/s/1H_dzHjYojYlMu1tjtxuEiQ? pwd=cmbx 提取码: cmbx 
# #####################################################
# #                                                   #
# #                注意：此为本地演示代码                 #       # #
# #                                                   #
# #####################################################


from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embedding=embeddings_model)

from langchain_core.documents import Document

document_1 = Document(
    page_content="今天在抖音学会了一个新菜：锅巴土豆泥！看起来简单，实际炸了厨房，连猫都嫌弃地走开了。",
    metadata={"source": "社交媒体"},
)

document_2 = Document(
    page_content="小区遛狗大爷今日播报：广场舞大妈占领健身区，遛狗群众纷纷撤退。现场气氛诡异，BGM已循环播放《最炫民族风》两小时。",
    metadata={"source": "社区新闻"},
)

documents = [document_1, document_2]

vector_store.add_documents(documents=documents)