import random

numberOfFiles = 10


base_name = ("project", "report", "training", "meeting", "09-28-2021","Financial  Results", "Customer List")
extra_name = ("Q1","Q2", "Q3", "Q4", "<COMPANY_NAME", ,)
hvf_name = ("CONFIDENTIAL", "Sensitive", "Privileged", )
file_ext = (".txt", ".pdf", ".docx")
all = (hvf_name, extra_name, base_name, file_ext)



for n in range(numberOfFiles):
    filename = ' '.join([random.choice(i) for i in all])
    newFile = open(filename, 'w')
    x = []
    for i in range(10): #number of lines in each file
        x.append(random.randint(0,60 + (n * 10)))

    for val in range(len(x)):
        newFile.write(str(x[val]) + "\n")
    newFile.close()
