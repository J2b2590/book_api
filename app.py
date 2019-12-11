from book_search import book_search

book = book_search()


reading_list = []

while True:
    book_choices = book.response_list
    user_select = input("Which book would you like to add to your reading list? ")
    # user types in the book title they would like to select and it is then Checked if title matches user input
    user_select = book.validation(user_select, True)
    for book_choice in book_choices:
        if book_choice["title"] == user_select:
            reading_list.append(book_choice)

    print("\n" "This is your reading list: ")
    # reading list is made and shows user title, author, and publisher of the book they would like to read
    for user_select in reading_list:
        title = user_select['title']
        author = user_select['author']
        publisher = user_select['publisher']
        saved_reading_list = "\n" "TITLE: %s,   " "\n"   "AUTHOR: %s,   " "\n"   "PUBLISHER: %s " "\n" % (
            title, author, publisher)

        print(saved_reading_list)
    # a new query for book
    book.query_api()





