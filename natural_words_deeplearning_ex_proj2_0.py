!pip install konlpy # colab에서 실행해야 코드가 정상 작동됨 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # 시각화
import re # regex 특수문자, 특정 키워드 일괄 처리
import urllib.request
from konlpy.tag import Okt # 한국어 토크나이저
from tensorflow.keras.preprocessing.text import Tokenizer # 우리가 실습했던 내용들 라이브러리로 사용예정
from tensorflow.keras.preprocessing.sequence import pad_sequences

urllib.request.urlretrieve("http://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt", filename="rating_train.txt")
urllib.request.urlretrieve("http://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt", filename="ratings_test.txt")

train_data= pd.read_table('/content/rating_train.txt')
test_data= pd.read_table('/content/ratings_test.txt')

print(train_data[:5])


