from pyhunter import PyHunter
#from reverseip import ReverseIP as rip
import os
import csv
import re
hunter=PyHunter('683cd5a907cee5a8d1f545cd224e9d153d9ea069')

Web_Dom=input('Enter The Name of the website: ')


Temp=hunter.domain_search(Web_Dom)
Temp1=Temp['emails']

for i in range (0,len(Temp1)):
    temp2=Temp1[i]
    print(temp2['value'])

Choice = int(input("\n1.Do you want to save in a text file \n2.Do you want to save it in a spreadsheet\n"))
while Choice>2 or Choice <=0:
    print('Please Enter either 1 or 2 ')
    Choice = int(input("\n1.Do you want to save in a text file  \n2. Do you want to save it in a spreadsheet\n"))
if (Choice == 1):
    file = open(str(Web_Dom + ".txt"),'w')
    for i in range (0,len(Temp1)):
        temp2=Temp1[i]
        file.write(temp2['value'])
        file.write('\n')
    print("The File has been saved ")

    file.close()
elif (Choice == 2):
    csv = open(Web_Dom + ".csv",'w')
    Column_Title = "S.No.,Email\n"
    csv.write(Column_Title)
    for i in range (0,len(Temp1)):
        Sno = str(i+1)
        temp2=Temp1[i]
        email = temp2['value']
        row = Sno + "," + email + "\n"
        csv.write(row)
    print('The CSV has been created')
    csv.close()

input(" ")
