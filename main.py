import base64
import os
import json
import re

file_path = 'What A Beautiful Name.txt'

def repl(match, count=[0]):
    x, = count
    count[0] += 1
    if x > 0:
        return ""
    return ""

song_content = []
with open(file_path) as file:
    song_content = file.readlines()

count = 0
presentation_docs = []
for i in song_content:
    if 'rtf_data' in i.strip() and '\\par' in i.strip() and 'LEMON MILK' in i.strip():
        # print(i)
        presentation_docs.append(i)
        count += 1


pattern = '\\\par'
pattern2 = '\\\pard'
match_par = re.findall(pattern, presentation_docs[3])
match_pard = re.findall(pattern2, presentation_docs[3])

par = re.compile(r'\\\\par(?!d)') 
searched = par.findall(presentation_docs[2])

presentation_results = []

#second
for sentence in presentation_docs:
    if 'Double-click' in sentence:
        presentation_results.append(sentence)
    # print("Processing sentence:", sentence)
    # print(sentence)
    else:
        skip_first = True  # Flag variable to skip the first occurrence
        result = ''
        start = 0
        noOfPar= len(re.findall(par, sentence))
        if (noOfPar > 1):
            while True:
                match = re.search(par, sentence[start:])
                if match:
                    result += sentence[start:start + match.start()]
                    if skip_first:
                        result += match.group()
                        skip_first = False
                    else:
                        result += ""
                        skip_first= True
                    start += match.end()
                else:
                    result += sentence[start:]
                    break
        # If it's only one line -> one par only
        else:
            result = re.sub(par, repl, sentence)

        presentation_results.append(result)
    

# save the result to a new txt 
# song_content --> all song

print(presentation_results[1])
new_song_content= []


counter=0
for i in song_content:
    if 'rtf_data' in i.strip() and '\\par' in i.strip() and 'LEMON MILK' in i.strip():
        new_song_content.append(presentation_results[counter])
        counter += 1
    else:
        new_song_content.append(i)

# Save the data to a different txt file
f = open("What A Beautiful Name New.txt", "w")
f.write("".join(new_song_content))
f.close()

