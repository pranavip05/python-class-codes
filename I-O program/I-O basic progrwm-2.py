#6. wap to print "hello world"
'''a,b="hello","world"
print(a,b,sep=' ',end='!')'''

#7. wap to find the sum of two numbers
'''a,b=10,20
c=a+b
print(c)'''

#8. wap to get the last digit from a number
'''a=6354367548
b=a%10
print(b)'''

#9. wap to get the square of last digits of a number
'''a=6354367548
b=a%10
c=b**2
print(c)'''


#10. wap to get all digits in same order except last digit from a number
'''a=5453754
b=a//10
print(b)'''

#11. the addition of 10 and 20 is 30
'''a,b=10,20
c=a+b
print('the addition of a and b is:',c)'''

#12.my name is pranavi phadatare
'''a,b='pranavi','phadatare'
print('my name is ',a,b)'''

#13. wap to reverse a two digit number
'''number=int(input("enter a number:"))
last_digit=number%10
first_digit=number//10
reverse=last_digit*10+first_digit
print(f'reverse of{number}is{reverse}')'''

#14. wap to reverse a three digit number
'''number=int(input("enter a number:"))
last_digit=number%10
middle_digit=(number//10)%10
first_digit=number//100
reverse=last_digit*100+middle_digit*10+first_digit
print(f'reverse of{number}is{reverse}')'''


#15. wap to reverse a three digit number
'''number=int(input("enter a number:"))
last_digit=number%10
secondlast_digit=(number//10)%10
middle_digit=(number//100)%100
second_digit=(number//100)%10
first_digit=number//1000
reverse=last_digit*secondlast_digit*100+middle_digit*100+second_digit*10+first_digit
print(f'reverse of{number}is{reverse}')''' 
