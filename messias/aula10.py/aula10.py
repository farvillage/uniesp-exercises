with open('Moby-Dick.txt', 'r', encoding='utf-8') as fs:
    content = fs.read()
    print(content.rstrip())