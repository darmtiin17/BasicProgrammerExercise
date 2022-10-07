#program created by Muhhammad Haidar Matin
#ti22i class

#input data


from time import monotonic


prolog = input("hello this is biodata app")
name = input("please, enter your name:")
age = int (input("enter your age:"))
kelas = input("enter your class:")
major = input("enter your major:")
hobbie_1 =  (input("enter your hobbie 1 :"))
hobbie_2 =  (input("enter your hobbie 2 :"))
hobbies = [hobbie_1,hobbie_2]
favoriteFood = bool(input("Do you like seblak || yes/no"))
motto = input("enter your motto")
print("=="*60)

if(favoriteFood == "yes"):
    favoriteFood = True
else :
    favoriteFood == "False"

#display
print("my biodata")
print("Name: ",name)
print("age: ",age)
print("kelas: ",kelas)
print("major: ",major)
print("hobbies: ",hobbies)
print("like seblak: ",favoritefood)
print("motto: ",motto)

print(type(name))
print(type(age))
print(type(kelas))
print(type(major))
print(type(hobbies))
print(type(favoritefood))
print(type(motto)) 
