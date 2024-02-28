#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
Numbers_input = input('Kindly enter a list of integer numbers separated by spaces: ')
Number_as_strings = Numbers_input.split()
Numbers = [int(num) for num in Number_as_strings]
total_sum = sum(Numbers)
print("The sum of the integers in the list is:", total_sum)


#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
Books = ("The Holy Quran","Rich Dad Poor Dad", "Song of Fire and Ice", "Hayatus Sahabah", "The Last of us")
for book in Books:
    print(book)


#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
Name = input('Kindly type in your name: ')
Age = input('Kindly input your age: ')
Favorite_colour = input('Kindly input your favorite color: ')
information = {"Name":Name, "Age": Age, "color": Favorite_colour}
print("Your entered information is: ", information)


#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
Numbers_input_1 = input('Kindly enter a first list of integer numbers separated by spaces: ')
Numbers_input_2 = input('Kindly enter a second list of integer numbers separated by spaces: ')
Number_as_strings_1 = Numbers_input_1.split()
Number_as_strings_2 = Numbers_input_2.split()
Numbers_1 = {int(num) for num in Number_as_strings_1}
Numbers_2 = {int(num) for num in Number_as_strings_2}
Set_Intersection = Numbers_1.intersection(Numbers_2)
print(Set_Intersection)


#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
Words = ['ten','escape','remember','nine','fight']
odd_length_words = [word for word in Words if len(Words) % 2 !=0 ]
print("Words with odd number of characters:", odd_length_words)

#week 2 assignment
#Create an empty list called my_list.
my_list = []
#Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#Insert the value 15 at the second position in the list. 
my_list[1] = 15
#Extend my_list with another list: [50, 60, 70].
my_list_2 = [50, 60, 70]
my_list.extend(my_list_2)
#Remove the last element from my_list.
my_list.remove(70)
#Sort my_list in ascending order.
sorted_list = sorted(my_list)
#Find and print the index of the value 30 in my_list.
value = 30
index = my_list.index(value)
print(f"The index of {value} in my_list is: {index}")