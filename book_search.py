import requests


class book_search:

    def validation(self, user_search, from_list=False):
        # additional validation goes here
        search_text = "You have entered an invalid book name, please try again "
        while not user_search:
            user_search = input(search_text)
        if from_list:
            # checking if book title matches if not user search will show search text for another input
            while not any(book["title"] == user_search for book in self.response_list):
                user_search = input(search_text)
        return user_search

    def query_api(self):
        self.user_search = input("What kind of book are you looking for: ")
        self.user_search = self.validation(self.user_search)
        # user search sent to validation
        self.response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + self.user_search)
        self.response = self.response.json()
        self.response_list = []
        for item in self.response.get('items', [])[:5]:
            if 'title' not in item['volumeInfo'] or 'authors' not in item['volumeInfo'] or 'publisher' not in item[
                'volumeInfo']:
                continue
            # iterating over items in our api call and splicing to show only 5 data points
            # and only showing item.volumeInfo.authors,item.volumeInfo.title, and item.volumeInfo.publisher
            title = item['volumeInfo']['title']
            author = item['volumeInfo']['authors']
            publisher = item['volumeInfo']['publisher']

            book_choice = "\n" "TITLE: %s,   " "\n"   "AUTHOR: %s,   " "\n"   "PUBLISHER: %s " "\n" % (
                title, author, publisher)

            book = {"title": title, "author": author, "publisher": publisher}
            self.response_list.append(book)

            print(book_choice)

    # method query created to allow user in app.py to query again after
    def __init__(self):
        self.query_api()
