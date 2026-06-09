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
def get_most_frequent_pair(pair_counter:dict[tuple[int,int],int])->tuple[int,int]:
    '''
    这里的输入就是pair_counts的输出，即那个[int,int]表示两个相邻的token对，后面的就是出现的总次数
    这里想找到出现次数最多的那一个就行

    方法是先找到频率最高的，然后
    '''
    max_freq = max(pair_counter.values())#这个就是找到最大的次数是哪一个，因为pair是个字典
    candidates = [pair for pair,freq in pair_counter.items() if freq == max_freq ]

    res = max(candidates)

    return res#这里返回的是出现最多的字节对



def add_pair_to_vocab(
        vocab:dict[int,bytes],
        pair:tuple[int,int]
)-> int:
    '''
    这里的入参两个，一个是我们的词表，一个是刚才get_most_frequent_pair得到的字节对

    '''

    index1,index2 = pair
    vocab[len(vocab)] = vocab[index1]+vocab[index2]#如果一个是a，一个是b，那么这里就得到了ab这个的byte值

    return len(vocab)-1
    


#下一步是更新文本中所有出现该字节对的地方，以及重新统计文本中所有相邻字节对的出现频率
#需要遍历所有的word，看有没有出现，出现的化就去做

def merge(
        word_counter:dict[tuple[bytes] | tuple[int], int],
        pair:tuple[int,int],
        new_id:int
)->tuple[dict[tuple[int], int], dict[tuple[int, int], int]]:
    '''
    pair是之前的get_most_frequent_pair找到的字节对
    new_id
    '''
    pass