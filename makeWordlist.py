import os
import re

def run(path):
    for filename in os.listdir("./"+path+"/pretty/"):
            wordlist = []
            print(filename)
            with open('./'+path+'/pretty/'+filename, encoding="utf8", errors='ignore') as source:
                read_data = source.read()
                read_data = read_data.replace('.', ' ')
                read_data = read_data.replace('-', ' ')
                read_data = read_data.replace(':', ' ')
                per_word = read_data.split()
                for word in per_word:
                    word = re.sub("\W+",'',word)
                    word = word.strip()
                    
                    wordlist.append(word)
                with open('./'+path+'/wordlist/'+filename, 'a+') as destination:
                    destination.writelines("\n".join(wordlist).lower())
run("lt")
run("pl")
run("hu")