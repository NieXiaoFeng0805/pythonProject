#计算一个文件大致包含多少字
def count_words(file_name):
    try:
        with open(file_name) as object:
            contens = object.read()
    except FileNoFoundError:
        msg="Sorry , the file "+ file_name + "does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file has about %d word."%num_words)


file_name = ['file_name1.txt','file_name2.txt','file_name3.txt']
for file in file_name:
    count_words(file)
