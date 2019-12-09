from book_search import book_search

reading_list = []
# created a variable with an empty array to hold the list of user_select books and adding
while True:
    user_select = input("Which book would you like? ")
    # creating an input for the user to choose what books to add to their reading_list
    if not user_select:
        break
    reading_list.append(user_select)
    print("This is your reading list, ", reading_list)
# showing the reading_list from the user_select books

