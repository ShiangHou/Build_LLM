'''
作业1 写一个train bpe的训练代码
这个函数的入参有三个，分别是
input_path 即输入的文件
vocab_size 词表大小

special token

最后输出两个，一个是
'''

import regex 

def train_bpe(
    input_path : str,
    vocab_size :int,
    special_token : list[str]
    )->tuple(dict[int,bytes],list[tuple[bytes,bytes]]):
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
    vocab : dict[int,bytes] = {i : bytes([0]) for i in range(256)}
    '''
    知识点，这里的bytes是一种数据类型，比如说，bytes[65] 就是所谓的 A，
    之前我们学到过，一共是256个，每一个数字都对应着一个字符串，这里就是直接用bytes这个来去把0-255的数字直接转为了对应的字符串
    然后这里的i:bytes就是字典的key-value
    '''

    # 2. 注册特殊 Token：分配从 256 开始的 ID
    #这里就是把输入中的special_token直接转化为newtoken，然后给上新的id名称就是

    new_token_id = 256 #新的从256开始
    for token in special_token:
        vocab[new_token_id] = token.encode('utf-8')#把token解码utf8然后存在表里
        new_token_id += 1
    

    #初始化合并表格,最开始的时候是空
    merge : list[tuple(bytes,bytes)] = []


    return vocab, merge

