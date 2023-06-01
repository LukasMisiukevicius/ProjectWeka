import re
import os
import csv
import collections

hu_balses_arr = ['a', 'e', 'i', 'o', 'ö', 'u', 'ü', 'á', 'é', 'í', 'ó', 'ő', 'ú', 'ű']
lt_balses_arr = ['a', 'ą', 'e', 'ę', 'ė', 'i', 'į', 'y', 'o', 'u', 'ų', 'ū']
pl_balses_arr = ['i', 'y', 'e', 'a', 'o', 'u', 'ą', 'ę']


def run_function(path):
    for filename in os.listdir("./"+path+"/wordlist/"):
        print(filename)
        with open('./'+path+'/wordlist/'+filename,encoding="utf8", errors='ignore') as source:
            Lines = source.readlines()
            total_words = len(Lines)
            total_chars = 0
            smaller_than_3 = 0
            balses = 0
            frequence = collections.Counter(Lines).most_common(1)[0]
            likely_to_repeat = str(round(frequence[1]/total_words,2))
            for word in Lines:
                total_chars += len(word.replace("\n", ""))
                if(len(word.replace("\n", "")) < 2):
                    smaller_than_3+=1
                
                if path == "lt":
                    for character in word:
                        if character in lt_balses_arr:
                            balses+=1
                if path == "pl":
                    for character in word:
                        if character in pl_balses_arr:
                            balses+=1
                if path == "hu":
                    for character in word:
                        if character in hu_balses_arr:
                            balses+=1
               
            count_average = total_chars/total_words
            
            longestWordLength = len(max(Lines, key=len).replace("\n", ""))
            average = str(round(count_average,2))

            smaller_than_2_ratio = str(round(smaller_than_3/total_words,2))
            balses_ratio = str(round(balses/total_chars,2))
            '''
                if path == "lt":
                    data = [longestWordLength, average, smaller_than_2_ratio, balses_ratio, likely_to_repeat, 1]
                if path == "pl":
                    data = [longestWordLength, average, smaller_than_2_ratio, balses_ratio, likely_to_repeat, 2]
                if path == "hu":
                    data = [longestWordLength, average, smaller_than_2_ratio, balses_ratio, likely_to_repeat, 3]'''
            if path == "lt":
                data = [longestWordLength, average, smaller_than_2_ratio, balses_ratio, 1]
            if path == "pl":
                data = [longestWordLength, average, smaller_than_2_ratio, balses_ratio, 2]
            if path == "hu":
                data = [longestWordLength, average, smaller_than_2_ratio, balses_ratio, 3]
            with open("./data_2.csv", "a+") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(data)

run_function("lt")
run_function("pl")
run_function("hu")