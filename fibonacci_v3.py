import sys
n1 = 1
n2 = 1 
f_num_list = [1,1]
print ('How many numbers of the Fibonacci sequence do you want?')
num = int(sys.stdin.readline())
for x in range(1,num+1):
    n3 = n1+n2
    f_num_list.append (n3)
    n1 = n2
    n2 = n3 
print ('Which position do you want to see?')
see=int(sys.stdin.readline())
if see == 1:
    print ('The %sst number from the Fibonacci sequence is:  %s' % (see, f_num_list[see - 1]))
elif see == 2:
    print('The %snd number from the Fibonacci sequence is: %s' % (see, f_num_list[see - 1]))
elif see == 3:
    print('The %srd number from the Fibonacci sequence is : %s' % (see, f_num_list[see - 1]))
elif see > num:
    print('Sorry, but you have to provide a number that is %s or less.' % num)
else:
    print('The %sth number from the Fibonacci sequence is: %s' % (see, f_num_list[see - 1]))
if see > num:
    pass
else:
    for i in range (0, see):
        print (f_num_list [i])


    
