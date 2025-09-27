import os
os.chdir("C:/Python-study/06")

def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except:
        print('오류 발생!')
    finally:
        file.close()
        print('finally 호출.')

write_text_file('test.txt', "try_return02")