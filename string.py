# string: a sequence of characters
# "sequence" - order　順列
# strings are immutable(unchangeable)

# index : 0123456789012　スペースもカウントされる
name = "Justin Bieber"

#1. indexing a string
print(name[6])
print(name[0])
print(name[-1])  # last letter
print(name[-2])  # second last letter

#len():returns the length of a string
print(len(name))
print(name[len(name)-1]) #last character

#2. slicing a string
# str[start:end] start <= < end
print(name[0:3])
print(name[7:13])
print(name[7:len(name)])
print(name[7:]) # always till the end
print(name[:6]) # always start from 0

#(example)
actor = "Ryan Reynolds"
#slice last name
print(actor[5:])
# slice first name
print(actor[:4])

# *multiply a string by an integer
print(actor *3)

#  +  adding another string
print(actor + " from Vancouver")

# string methods (functions)
# Upper case,  Lower case, capitalize
address = "816 Granville ST, Vancouver, BC"
print(address.upper())
print(address.lower())
print(address.capitalize())  #先頭だけ大文字にする


#2. find() returns -1 if not found
#   index () throws an error if not found
print(address.find("vancouver")) #見つからなかったたら-1を返す
print(address.index("Vancouver")) #見つからなかったら何も現れない

#3.
user_id ="19243"
if user_id.isdigit():#中身が数値かどうか判定
    print("Valid User ID")
elif user_id.isalpha() or user_id.isalnum():#文字列の全てが英数字だったらTRUEを返す
    print("Invalid User ID: use number only")

#4. split - splits a string into a list of substrings　
#   join() - joins a list of strings into one big string データを特定の文字などで繋げることができる
#   strip() -strip out all white spaces (space, tab, newline) 空欄を消す

l = address.split(",") #,で区切られている文字を分割する
print(l)
street_address =l[0]
print(street_address)
city =l[1].strip()
province =l[2].strip()

full = f'I live in {street_address},{city},{province}'
print(full)

cities = ["Vancouver", "Burnaby", "Richmond","West Vancouver"]
print(" !! ".join(cities))










