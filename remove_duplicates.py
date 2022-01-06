f = open('input.txt', 'r')
u_list = f.readlines()

# Слова или значения для фильтрации
keywordFilter = ['word', 'q']

u_list = [sent for sent in u_list
          if not any(word in sent for word in keywordFilter)]

file = open(file='output.txt', mode='a', encoding='utf-8')
file.write(''.join(map(str, u_list)))
file.close()
