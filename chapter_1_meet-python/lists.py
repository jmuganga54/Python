# #list of movies
# movies = ["The Holy Grail","The Life of Brian", "The Meaning of Life"]

# #Outputting the movies
# print(movies[1])

# #Another list
# cast = ["Cheese","Palin","Jone","Idle"]

# #Printing number of items in a list cast
# print(len(cast))

# #using append to add element at the end of the list
# cast.append("Gillium")

# #Printing out cast after adding one element
# print(cast)

# #Removing data from the end of your list
# cast.pop()

# #Printing out cast list after removing data 
# print(cast)

# #adding a collection of items at the end of the list
# cast.extend(["Gilliam","Chapman"])

# #Printing out after adding a collection of item to the list
# print(cast)

# #Removing a specific data item from the list
# cast.remove("Chapman")

# #Printing the output after removing one element
# print(cast)

# #Add a data item before specifc slot location
# cast.insert(0,"Chapman")

# #Printing after adding 
# print(cast)

# #Adding number after string
# movies.insert(1,1975)
# movies.insert(3,1979)
# movies.append(1983)
# print(movies)

# #Re-create a list at one go without insert or append
# movies = ["The Holly Grail",1975, "The life of Brian",1979, "The Meaning of Life",1983]
# print(movies)

# #LOOPING THE LISTS(ITERATE)
# fav_movies = ["The Holy Grail","The Life of Brian"]

# for each_flick in fav_movies:
#     print(each_flick)

# #Iterating the list using while loop
# count = 0
# while count < len(movies):
#     print(movies[count])
#     count = count + 1


#list within a list
movies = [
        "The Holy Grail",1975, "Terry Jones & Gerry Gillimam", 91,
        ["Graham Chapman",
            ["Michael Palin", "John Cleese", "Terry Gilliam","Eric Idle", "Terry Jones"]]]

# #outputing value from a list within a list
# print(movies[4][1][3])

# #outputing 
# print(movies)

# #looping a list within a list
# for each_item in movies:
#    print(each_item)


# #use of isinstance() function
# names = ["Michael","Terry"]
# print(isinstance(names, list))

# num_names = len(names)
# print(isinstance(num_names,list))

# for each_item in movies:
#     if isinstance(each_item,list):
#         for nested_item in each_item:
#             if isinstance(nested_item,list):
#                 for deeper_item in nested_item:
#                     print(deeper_item)
#             else:
#                 print(nested_item)
#     else:
#         print(each_item)


def print_lol(the_list):
    #process the provided list with a "for" loop
    for each_item in the_list:
        if isinstance(each_item,list):
            #if the item being processed is itself a list, invoke the function
            print_lol(each_item)
        else:
            #if the item being processed ISN'T a list, display the item on screen
            print(each_item) 


#invoke the function created above
print_lol(movies)

#Recursion to rescure
#The use of a recursion function has allowed you to [reduce] 14 lines of messy, hard to understand, brain-hurting code into a six-line function.

#Python 3 defaults its recursion limit to 1,000, which is a log of lists of lists.. and this limit can be changed should you ever need even more depth than that.