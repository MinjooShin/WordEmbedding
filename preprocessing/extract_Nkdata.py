import pandas as pd

# Nk_df = pd.read_csv('../data/apostrophe_NPH_sample_1_en2nk_last.csv', encoding='utf-8')

# print("count of data (sentence):", len(Nk_df))

# Nk_list = []
# for En, Nk in zip(Nk_df['En'], Nk_df['Nk']):
#     Nk_list.append(Nk)
    
from konlpy.tag import Mecab
tokenizer = Mecab()
text = "싸피에서 열공한 우린, 대한민국을 이끌 SW인재"
print(tokenizer.morphs(text))