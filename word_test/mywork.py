import random


def ask_pinyin(question):
    pinyin = input('Enter Pinyin for "{}", ==> '.format(question['word']))
    confirm = input('Your answer is {}, submit? (Just press Enter if you are sure)'.format(pinyin))
    while confirm != '':
        pinyin = input('Enter Pinyin for "{}", ==> '.format(question['word']))
        confirm = input('Your answer is {}, submit? (Just press Enter if you are sure)'.format(pinyin))
    return pinyin in question['pinyin']


def ask_meaning(question, correct_question):
    print('We have a list of potential meanings for this word, select the most appropriate one by enter the number:')
    for i in range(len(question['ans'])):
        print('{}: {}'.format(i + 1, question['ans'][i]))
    selection = input("Your selection ==> ")
    while selection not in ['1', '2', '3', '4']:
        selection = input("You need to select from 1, 2, 3, and 4.\nYour selection ==> ")
    confirm = input('Your answer is {}, submit? (Just press Enter if you are sure)'.format(selection))
    while confirm != '':
        selection = input("You need to select from 1, 2, 3, and 4.\nYour selection ==> ")
        confirm = input('Your answer is {}, submit? (Just press Enter if you are sure)'.format(selection))
    judge = question['ans'][int(selection) - 1] == question['cor']
    if judge:
        correct_question.append(question['group'])
        print("You are correct! Go to the next question...")
    else:
        print("Woops, it's not that correct :( Go to the next question...")


def generate_question(row):
    re = {}
    temp = row.split(' ')
    re['word'] = temp[0]
    re['pinyin'] = temp[1]
    re['cor'] = temp[2]
    ans = [temp[2], temp[3], temp[4], temp[5]]
    random.shuffle(ans)
    re['ans'] = ans
    re['group'] = temp[6]
    return re


def main():
    QUESTION_AMT = 4
    count = 0
    correct_question = []
    store = []

    with open('result.txt', 'r') as f:
        while True:
            line = f.readline()
            if line != '':
                store.append(line.rstrip('\n'))
            else:
                break

    total_question = len(store)

    questions = []
    for i in range(len(store)):
        questions.append(generate_question(store[i]))

    for question in questions:
        count += 1
        if count > QUESTION_AMT:
            print('Result: {} out of {} correct selection!'.format(len(correct_question), QUESTION_AMT))
            print('You have done this test! Congratz!')
            break
        while True:
            print('==================\nQuestion {}'.format(count))
            know = input('Do you know this word: "{}", answer by y/n ==> '.format(question['word']))
            if know == 'y':
                correct = ask_pinyin(question)
                if correct:
                    print("Great job!")
                    ask_meaning(question, correct_question)
                    break
            elif know == 'n':
                break
            else:
                know = input(
                    'You typed something that is not expected :(\nDo you know this word: "{}", answer by y/n ==> '.format(
                        question['word']))


main()
