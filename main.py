import random
import argparse
import pickle

def educ(text):
    dict = {}
    s = ""
    ls = ""
    for i in text:
        for j in i:
            if j == ' ' or j == '\n' or j == ',' or j == '.':
               if ls != "":
                  try:
                     tmp = dict.get(ls)
                     tmp.append(s)
                     dict.update({ls : tmp})
                  except Exception:
                     dict.update({ls : [s]})
               ls = s
               s = ""
            else:
                if 'а' <= j <= 'я' or 'А' <= j <= 'Я':
                    s += j
    with open('educ.pickle', 'wb') as write:
        pickle.dump(dict, write)

def gen(n):
    with open('educ.pickle', 'rb') as read:
        dict = pickle.load(read)
    now = random.choice(list(dict.keys()))
    text = open("final.txt", "w", encoding="utf8")
    for i in range(n):
        next = random.choice(dict.get(now))
        text.write(next + " ")
        now = next
    text.close()

def read_cmd():
    importer = argparse.ArgumentParser(description='биграмка')
    importer.add_argument('n', type=int, help='Введите размер поля')
    args = importer.parse_args()
    return args.n

text = open("Input.txt", "r", encoding="utf8")
educ(text)
gen(int(input()))
text.close()