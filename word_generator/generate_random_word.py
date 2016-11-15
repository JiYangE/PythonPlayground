import pandas as pd
import random
import math

def generate(words, n):
    for i in range(n):
        selected = random.choice(words)
        words.remove(selected)
        print(selected, end=' ')

GROUP_SIZE = 20
TOP_WORD = 3000
GROUP_AMOUNT = 10

data = pd.read_excel('source.xls')
# drop table header
data = data[6:]
data.columns = ["Index", "Word", "Frequency", "D1", "D2"]
data = data[["Index", "Word", "Frequency"]]
data.reset_index(drop=True, inplace=True)
data = data[:TOP_WORD]

store = []
for idx, row in data.iterrows():
    if len(row['Word']) > 1:
        store.append(row)
df = pd.DataFrame(store)
df = df[['Word', 'Frequency']]
df.reset_index(drop=True, inplace=True)

word_list = []
word_list = [row['Word'] for idx, row in df.iterrows()]

bin_size = df.shape[0]
store_list = [[] for i in range(1, GROUP_AMOUNT + 1)]

LIST_SIZE = df.shape[0] // GROUP_AMOUNT
for wd in word_list:
    try:
        wd_idx = word_list.index(wd) // LIST_SIZE
        store_list[wd_idx].append(wd)
    except:
        break

for i in range(len(store_list)):
    print('\nGroup {}'.format(i))
    generate(store_list[i], GROUP_SIZE)
    print()
