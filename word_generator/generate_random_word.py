import pandas as pd
import random
import math

def generate(words, n):
    for i in range(n):
        selected = random.choice(words)
        words.remove(selected)
        print(selected, end=' ')

def generate_bound(n):
    # 2.5538^10 = 11800
    return [math.floor(2.5538**(i+1)) for i in range(n)]

for a in range(6):
    GROUP_SIZE = 25
    TOP_WORD = 14200
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

    list_bound = generate_bound(GROUP_AMOUNT)
    list_bound.insert(0, 0)

    for i in range(len(list_bound)):
        try:
            lower = list_bound[i]
            upper = list_bound[i + 1]
        except:
            break
        try:
            for wd in word_list:
                try:
                    wd_idx = word_list.index(wd)
                    if wd_idx > lower and wd_idx <= upper:
                        store_list[i].append(wd)
                except:
                    break
        except:
            break


    for i in range(len(store_list)):
        if  len(store_list[i]) < GROUP_SIZE:
            print('\nGroup {}'.format(i))
            for wd in store_list[i]:
                print(wd, end=' ')
        else:
            try:
                print('\nGroup {}'.format(i))
                generate(store_list[i], GROUP_SIZE)
            except:
                break
