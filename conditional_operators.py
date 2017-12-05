age = 21
if age >= 18:
    print "You can vote now"
else:
    print "No, You can not vote"


name = 'chowdappa'

if name is 'chowdy':
    print("How are you chowdy")
elif name is 'chowdi':
    print "How are you doing chowdi"
else:
    print "who is there?"

####################  for demo
    print "####################  for demo"
    
foods = ['biryani','pavbhaji','roti-subji','anna-sambar','idle','dosa']
print foods

for f in foods:
    print f
    print len(f)

for n in range(10):
    print n
# In between
for n in range(11, 25):
    print n

# step by 2 in range
for n in range(10, 100, 2):
    print n

##########   While demo
number = 100;
while 1:
    print "hello"
    if number == 80:
        break
    else:
        number-=1
print number



### Single line comment.


found = 'false'
magicNumber = 56
for n in range(100):
    if n == magicNumber:
        print(n, " is magic number found")
        print("magic number is ", n)
        found = 'true'
        break

if found is 'false':
    print "Magic number not found"

 
    
######## continue
magicNumber = 56

for n in range(1, 100):
    if(n == magicNumber):
        print "Magic number found"
        break
    else:
        continue
    
    




