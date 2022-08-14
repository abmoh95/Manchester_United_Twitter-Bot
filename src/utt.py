import csv

list1 = []

str1_ = "sdfs öskdfös kf sdföksdf ö sdföksd l ssd ksö \n"
str2_ = "asda  asfsdf sfsf sf"

str1_ += str2_
print(str1_)

with open('utt.csv', 'w') as outfile:
    c = csv.writer(outfile)
    c.writerow("hello my friend")

str_ = "sasdada f s fsdf sdf sfs fsdf  s"

with open('utt.txt', 'a+') as outfile:
    #b = outfile.write(str_ + "\n")
    c = outfile.writelines(str1_ + "\n")


with open('utt.txt', 'r') as oo:
    if 'sasdada f s fsdf sdf sfs fsdf  s' in oo.read():
        print("true")

