import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:[A-Za-z]+)?', line)

def create_list(book):
    
    my_list = []
    my_file = open(book)
    
    for lines in my_file:
        lines = lines.strip()
        split_line(lines)
        my_list.append(lines)
    
    my_file.close()
    return my_list

dict_list = create_list("dictionary.txt")

alice = open("AliceInWonderLand200.txt")
word_list = []
for i in alice:
    word_list.append(split_line(i))

print(word_list)