'''
作业1 写一个train bpe的训练代码
这个函数的入参有三个，分别是
input_path 即输入的文件
vocab_size 词表大小

special token

最后输出两个，一个是词表，即dict[int,bytes]，一个是tuple[bytes,bytes]]，表示哪些合并了
'''

import regex 
#Initialization: 将输入文本视为字节序列，每个字节作为一个token。
# 初始化词汇表包含所有可能的字节（0-255）。以及Special Tokens，比如 <|endoftext|>

#Count Pairs: 统计文本中所有相邻字节对的出现频率

# Merge Pairs: 将频率最高的字节对其合并为一个新的token，更新文本和词汇表:
# Get the most frequent pair: 找到出现频率最高的字节对。
# Add the new pair: 将这个新的字节对加入词汇表。
# Update the word counter: 更新文本中所有出现该字节对的地方。
# Update Pairs Counts: 重新统计文本中所有相邻字节对的出现频率。

#Repeat: 重复步骤2,3，直到达到预定的合并次数


#先写几个辅助的函数


def init_vocab(sepcial_tokens:list[str]|None = None)->dict[int,bytes]:
    '''
    初始化词表，把special token转化为vocab，最后的输出类型是dict[int,bytes]
    其中int就是数，bytes就是一个byte类型的
    思想是，前0-255其实就是一个int对应着一个bytes
    如果复杂的话，会把多个合并成一个，即
    '''
    vocab:dict[int,bytes] = {x:bytes([x]) for x in range(256)}

    #然后我们要把special_token加进去
    #需要一个量来去统计每一次加的位置
    cur_index = 256#从256开始
    if sepcial_tokens:
        for token in sepcial_tokens:
            token_bytes = token.encode('utf-8')
            vocab[cur_index] = token_bytes#就是把对应的token映射到对应的byte上
            cur_index +=1
    return vocab#输出一个加过special token的

#第二个，统计文本中所有相邻字节对出现的频率
def pair_counts(word_count:dict[tuple[int,...],int]) -> dict[tuple[int,int],int]:
    '''
    首先，这里的输入的dict[tuple[int,...],int]即表述一个词是由多个tokenID构成的，
    word_count如下，比如说
     (65, 66, 67): 5,   # token序列 [65,66,67] 出现了5次
    (65, 68): 3,       # token序列 [65,68] 出现了3次
    这里的...就是说长度不固定，可能是65 66
    所里那个int就是词表的位置的id，后面的。。。意思是表示这个词的是哪些token id
    在后面那个int是表示的这个“词”出现的频率
    即tuple[int,...]是 (65, 66, 67)
    int是那个5
    
    最后的输出是两个int，
    tuple[int,int]表示一个相邻的token对
    后面的dict的int表示这个相邻对出现的总次数
    
    '''

    #首先初始化输出
    pairs: dict[tuple[int,int],int] = {}

    for word,count in word_count.items():
        #word就是那个(65, 66, 67)
        for a,b in zip(word,word[1:]):
            pairs[(a,b)] = pairs.get((a,b),0)+count#记录对(a,b)出现的次数
    return pairs

#下一步，找到最多的字节对
def get_most_frequent_pair



def train_bpe(
    input_path : str,
    vocab_size :int,
    special_tokens : list[str]
    )->tuple[dict[int,bytes],list[tuple[bytes,bytes]]]:
    '''
    在这里复述一下bpe的整体的思路
    1. 把语料转化为utf-8,加入special，构建基础词表
    2. Pre-tokenization
    3. 聚合，做一个词频映射表和 邻接对频次表
    4. 贪心迭代
    '''

    #第一步是要把最后的输出给初始化出来


    # ==========================================
    # 第一步：初始化状态 (Initialization)
    # ==========================================
    
    #最后是输出了两个，一个vocab，即字符映射，这里就是0-255的字节
    # 1. 基础词表：包含 256 个单字节 (0 ~ 255)
    # 字典的键是 ID (int)，值是对应的单字节 (bytes)
    vocab : dict[int,bytes] = {i : bytes([i]) for i in range(256)}
    '''
    知识点，这里的bytes是一种数据类型，比如说，bytes[65] 就是所谓的 A，
    之前我们学到过，一共是256个，每一个数字都对应着一个字符串，这里就是直接用bytes这个来去把0-255的数字直接转为了对应的字符串
    然后这里的i:bytes就是字典的key-value
    '''

    # 2. 注册特殊 Token：分配从 256 开始的 ID
    #这里就是把输入中的special_token直接转化为newtoken，然后给上新的id名称就是

    #这里就是一个简单的for循环，
    new_token_id = 256 #新的从256开始
    for token in special_tokens:
        vocab[new_token_id] = token.encode('utf-8')#把token解码utf8然后存在表里
        new_token_id += 1
    

    #初始化合并表格,最开始的时候是空
    #合并表是一个list，里面存着两对，表示每一对都是两个byte类型
    merge : list[tuple[bytes,bytes]] = []

    # 3:读取path，进行预分词
    



    #最后就是需要return这两个
    return vocab, merge

