def count_word(filename):
    #计算一个文件大致有多少个单词
    try:
        with open(filename)as f_job:
            contents= f_job.read()
    except FileNotFoundError:
        # mag = "sory, the file "+ filename + "dose not exist"
        # print(mag)
        pass

    else:
        #计算文件大致有多少单词
        word = contents.split()
        num_word  = len(word)
        print("the file "+filename +"has about "+str(num_word))

# fiename = "alice.txt"
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']

for fiilename in filenames:
    count_word(fiilename)