#PROGRAMMING EXERCISE 6-2
#Write a program that asks  the user for the name of a file.
#The program should display only the first five lines of the file's
#contents. If the file contains less than five lines, it should display
#the file's entire contents.

file = str(input("Please enter name for file: "))
f_open = open (file, 'r')

for x in range (5):
      line = file.readline()
      if line:
            print (line)
            
