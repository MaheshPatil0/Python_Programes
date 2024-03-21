#Except a string from user varabel count the no of  vowels and consonents in str 1 and print it 

str1=input("Enter a string : ")
str1=str1.lower()
print(str1)
v=['a','e','i','o','u']
vowels=0
conso=0
for i in str1:
    if i in v:
        vowels=vowels+1
    else:
        conso=conso+1
        
print("Vowels are present in string",vowels) 
print("Consonents are present in string",conso)

