#list; a sewuence of elements of any data type
countries = ["Brazil","Canada","Colombia","Ecuador","Iran","Japan","South Korea","Taiwan","Nepal"]

#index a list (index starts from 0)
print(countries[0])
print(countries[-1])
print(len(countries))

#slicing a list
#list[start:end]  start <=  <end
print(countries[:3])#３は含めない　０−２まで
print(countries[3:]) #３からー

#assign a new element
countries[4] = "ABC"
print(countries)

#swap elements
first = countries[0]
countries[0]=countries[1]
print(countries)
countries[1]=first #最初に0に入っていたブラジルがfirstに入っている
print(countries)

# lists methods (functions)
languages =["C","C++","Python","Java","JavaScript"]

#append(): add a new element at the end of the list
languages.append("SQL")
print(languages)
#insert(): add a new element at the given index
languages.insert(0,"Swift")
print(languages)
#pop(index)
languages.pop(0)#インデックスを使って消す
print(languages)
#remove(element)
languages.remove("Java") #特定の文字を消す
print(languages)

#index(element): returns the index of element in the list
print(languages.index("Python"))

#+: concatenate(combine)
#*: repeat num

nums1=[1,2,3]
nums2=[4.5,6]
print(nums1+nums2)
print(nums1 *3)

#"nested" lists
students = [[1,"John","Canada"],[2,"Max","USA"],[3,"Peter","UK"]]
print(students[1][2])
inner = students[1]
print(inner[2])

#list comprehension ->






