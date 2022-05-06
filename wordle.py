import requests
number_len = 7
num_guesses = 7
import random
word_site = "http://www.mieliestronk.com/corncob_lowercase.txt"

response = requests.get(word_site)
WORDS = response.content.splitlines()
five_letter_words = []
for i in range(len(WORDS)):
    if len(str(WORDS[i])) == (number_len+3):
        w = str(WORDS[i])
        w = w.replace("'","")
        w = list(w)
        del w[0]
        five_letter_words.append(w)
correct = (random.choice(five_letter_words))
cor = list(correct)
del cor[0]
#correct = ""
correct = list(correct)
print(correct)
ans_list = []
use_list = []
use1_list = []
leg = 0
leg1 = 1
tf = True
for p in range(num_guesses):
    answer = input("input "+str(number_len)+" letter word:")
    if list(answer) not in five_letter_words:
        print("please input an actual word you uneducated piece of pitiful waste")
        continue
    elif len(answer) != number_len:
        print("5 letter word please.")
        continue
    for i in range(number_len):
        for p in range(len(use1_list)):
            if not use1_list[p] in answer:
                tf = False
        for j in range(len(use_list)):
            if not answer[use_list[j]] == correct[use_list[j]]:
                tf = False
                break
    if tf is False:
        print("use actually helpful hints that i gave you, you moron")
        tf = True
        continue
    answer = list(answer)
    print(answer)
    for i in range(number_len):
        if answer[i] == correct[i]:
            ans_list.append('green')
            use_list.append(i)
            leg += 1
            leg1 += 1
            continue
        elif answer[i] in correct:
            if correct.count(answer[i]) == leg1:
                ans_list.append('yellow')
                use1_list.append(answer[i])
                leg1 += 1
                continue
            else:
                ans_list.append('grey')
                continue
            '''
            elif correct.count(answer[i]) == leg+1:
                ans_list.append('yellow')
                use1_list.append(answer[i])
                continue
            '''
        elif answer[i] not in correct:
            ans_list.append('grey')
    print(ans_list)
    ans_list.clear()
    if answer == correct:
        print("you got it right! congratulations!")
        break




