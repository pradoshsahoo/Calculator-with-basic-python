print("--------------CALCULATOR----------------")
print("Operator supported-'+','-','*','/','%'")
s=input("Input a string containing <Operand><space><operator><space><operand>\nExample-2 * 3\nEnter yor string -> ")
lst=s.split(' ')
if lst[1]=='+':
    print(int(lst[0])+int(lst[2]))
elif lst[1]=='-':
    print(int(lst[0])-int(lst[2]))
elif lst[1]=='*':
    print(int(lst[0])*int(lst[2]))
elif lst[1]=='/':
    print(int(lst[0])/int(lst[2]))
elif lst[1]=='%':
    print(int(lst[0])%int(lst[2]))
else:
    print("Invalid input (Check for spaces in input)")