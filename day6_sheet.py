#2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a = 20; a+= 30; a%=3; print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
#print('False' in 'False') --> SHOWS AN ERROR
print(((True == False) or (False > True)) and (False <= True))

#3
s1 = "Nice to have it"
s2 = "here"
print(s1+" "+s2)

#4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#5
a.insert(0,s1)
a.insert(7,s2)
print(a)

#6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
for i in numbers:
    if (i%2==0):
        print(i)
    elif(i==237):
        break

#7
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
s = set()
for i in color_list_1:
    if(i not in color_list_2):
        s.add(i)
print(s)

#8
string = input("Enter the string")
string = set(string)
alpha = list('abcdefghijklmnopqrstuvwxyz')
i=0
for word in string:
    if(word in alpha):
        i+=1
if(i==26):
    print('String is Pangram')
else:
    print('String is not Pangram')

#9
n = int(input("Enter an integer : "))
value = n+11*n+111*n
print(value)

#11
string = input("Enter the string")
string = string.split(',')
string.sort()
for i in string[:-1]:
    print(i, end=',')
print(string[-1])

#12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
marks_list = d.get('Marks')
student_list = d.get('Student')
num = marks_list.index(max(marks_list))
print(student_list[num])

#13
string = input("Enter the string")
string = list(string)
alpha = list('abcdefghijklmnopqrstuvwxyz')
num = list('0123456789')
i=0
j=0
for word in string:
    if(word in alpha):
        i+=1
    elif(word in num):
        j+=1
print(f'LETTERS {i}')
print(f'DIGITS {j}')

#14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
s=input('Enter a Subject:-')
l1=d['Name']
l2=[]
l3=[]
l4=d['Ratings']
l5=[]
sub=d['Subject']
for i in range(len(sub)):
    if sub[i]==s:
        l2+=[sub[i]]
        l3+=[l1[i]]
        l5+=[l4[i]]
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)


#16
UP = int(input("UP :-"))
DOWN = int(input("DOWN :-"))
LEFT = int(input("LEFT :-"))
RIGHT = int(input("RIGHT :-"))

x_coordinate = UP - DOWN
y_coordinate = LEFT - RIGHT

result_distance = (x_coordinate*2 + y_coordinate2)*.5
print(int(result_distance))
