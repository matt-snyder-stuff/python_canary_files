import random

numberOfFiles = 500


base_name = ("project", "new","file","report", "training", "meeting" ,"screenshot", "10-07-2021", "plan")
extra_name = ("school","house",)
file_ext = (".txt", ".pdf", ".docx")
all = ( extra_name, base_name, file_ext)



for n in range(numberOfFiles):
    filename = ' '.join([random.choice(i) for i in all])
    newFile = open(filename, 'w')
    x = []
    for i in range(10): #number of lines in each file
        x.append(random.randint(0,60 + (n * 10)))

    for val in range(len(x)):
        newFile.write(str(x[val]) + "\n")
    newFile.close()
