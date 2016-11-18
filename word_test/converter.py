import pandas as pd

df = pd.read_excel('translation.xlsx')
df.columns = ['Word', 'Pinyin', 'Pinyin1', 'Pinyin2', 'Correct', 'Wrong1', 'Wrong2', 'Wrong3', 'Group']

with open('result.txt', 'a') as f:
    for idx, row in df.iterrows():
        myrow = {}
        myrow['Word'] = row['Word']
        if str(row['Pinyin2']) == 'nan':
            myrow['Pinyin'] = row['Pinyin1'].replace(" ", "")
        else:
            myrow['Pinyin'] = row['Pinyin1'].replace(" ", "") + row['Pinyin2'].replace(" ", "")
        myrow['Correct'] = row['Correct']
        myrow['Wrong1'] = row['Wrong1']
        myrow['Wrong2'] = row['Wrong2']
        myrow['Wrong3'] = row['Wrong3']
        myrow['Group'] = row['Group']
        f.write('{} {} {} {} {} {} {}\n'.format(myrow['Word'], myrow['Pinyin'], myrow['Correct'], myrow['Wrong1'], myrow['Wrong2'], myrow['Wrong3'], myrow['Group']))
