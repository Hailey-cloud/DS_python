list = [1,2,3,4,5]
print(list[2])

list.append(6)
print(list)
list.pop(1)
print(list)

given_list = [10,20,30,40,50,60,70,80,90,100]
print(given_list[:5])
print(given_list[-3:])
print(given_list[::2]) #２つとばしで要素を表示する


list_operations = [1,2,3,4,5,6,7,8,9,10]
print(sum(list_operations))
print(min(list_operations))
print(max(list_operations))

#list_comprehension 内包表記 if とfor

print([i*i for i in range(1,11)])
#squareは２乗

three_list = [1,2,3],[4,5,6],[7,8,9]
print(three_list[1][1])

l = "Hello,World!"
print(l[0],l[-1])

l1 = "Python Programming"
print(l1[:6])
print(l1[7:])

l2 = "hello, world!"
print(l2.upper())
print(l2.replace("world","Python"))
print("Hello" +" " + "World")

fruits = "apple,banana,cherry"
print(fruits.split(","))

name = "hina"
age = "25"
full = f'My name is {name} and I am {age} years old.'
print(full)

order = input("Enter your user name: ")
print(order[::-1]) #start:stop:step(-1)


def isPalindrome(string):
    if (string ==string[::-1]):
        return"The string is a palindrome."
    else:
        return"The string is not a paindrome."

print(isPalindrome("madam"))
print(isPalindrome("hello"))

word = input()
print(word[::-1])
if word == word[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a paindrome.")


p =['P','y','t','h','o','n']
print("".join(p))










