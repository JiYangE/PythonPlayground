#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_excel('translation.xlsx')
df.columns = ['Word', 'Pinyin', 'Pinyin1', 'Pinyin2', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3', 'Group']

for i in range(4):
    df0 = df[df['Group'] == 0]
    df1 = df[df['Group'] == 1].sample(3)
    df2 = df[df['Group'] == 2].sample(10)
    df3 = df[df['Group'] == 3].sample(5)
    df4 = df[df['Group'] == 4].sample(5)
    df5 = df[df['Group'] == 5].sample(5)
    df6 = df[df['Group'] == 6].sample(5)
    df7 = df[df['Group'] == 7].sample(5)
    df8 = df[df['Group'] == 8].sample(5)
    df9 = df[df['Group'] == 9].sample(5)
    frame = [df0, df1, df2, df3, df4, df5, df6, df7, df8, df9]
    final_df = pd.concat(frame)
    with open('result{}.txt'.format(i), 'a') as f:
        for idx, row in final_df.iterrows():
            myrow = {}
            myrow['Word'] = row['Word']
            if str(row['Pinyin2']) == 'nan':
                myrow['Pinyin'] = row['Pinyin1'].replace(" ", "")
            else:
                myrow['Pinyin'] = row['Pinyin1'].replace(" ", "") + row['Pinyin2'].replace(" ", "")
            myrow['Correct'] = row['Correct'].replace(" ", "!")
            myrow['Wrong1'] = row['Wrong1'].replace(" ", "!")
            myrow['Wrong2'] = row['Wrong2'].replace(" ", "!")
            myrow['Wrong3'] = row['Wrong3'].replace(" ", "!") if type(row['Wrong3']) == type('str') else ''
            myrow['Group'] = row['Group']
            f.write('{},{},{},{},{},{},{}\n'.format(myrow['Word'], myrow['Pinyin'], myrow['Correct'], myrow['Wrong1'], myrow['Wrong2'], myrow['Wrong3'], myrow['Group']))
    print('Done')
