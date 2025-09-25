import os
os.chdir("C:/Python-study/for-data-analysis")

with open('input_open_close.txt', 'r') as in_file, open('output_with2.txt', 'w') as out_file:
    for line in in_file:
        out_file.write(line.upper())