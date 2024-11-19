import random as r
prompt="""
1.alphabets
2.numbers
3.special chars
enter what password need: """
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialchars=[':', ';', '<', '=', '>', '?', '@', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '[', ']', '^', '_', '`', '{', '|', '}', '~']

n=int(input('enter length: '))
x=[int(x) for x in input(prompt).split()][:3]
	
pwd=""
for i in range(n):
	match r.choice(x):
		case 1:
			pwd+=r.choice(alphabets)
		case 2:
			pwd+=r.choice(numbers)
		case 3:
			pwd+=r.choice(specialchars)

print("Generate password : "+str(pwd))
