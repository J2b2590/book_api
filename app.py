from book_search import book_search


book = book_search()

# for book in book_choice:
#     print(book)
reading_list = []
# created a variable with an empty array to hold the list of user_select books and adding
while True:
    book_choices = book.response_list
    user_select = input("Which book would you like to add to your reading list? ")
    user_select = book.validation(user_select, True)
    for book_choice in book_choices:
        if book_choice["title"] == user_select:
            reading_list.append(book_choice)
    # creating an input for the user to choose what books to add to their reading_list

    print("\n" "This is your reading list: ")
    
    for user_select in reading_list:
        title = user_select['title']
        author = user_select['author']
        publisher = user_select['publisher']
        saved_reading_list = "\n" "TITLE: %s,   " "\n"   "AUTHOR: %s,   " "\n"   "PUBLISHER: %s " "\n" % (
            title, author, publisher)

        print( saved_reading_list)

    book.query_api()

# showing the reading_list from the user_select books


