file=open('diaries.txt','w')
file.write('Hello, World! \nIts great to meet you.\nI hope i get a good IP.')

with open('diaries.txt', 'r') as file:
    content=file.read()
    print("Content:", content)
file.close()