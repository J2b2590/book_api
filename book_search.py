import requests


class book_search:

    @staticmethod
    def validation(user_search):
        if not user_search:
            return False
        return True
    #     additional validation goes here

    def __init__(self):
        self.user_search = input("What kind of book are you looking for: ")
        while not self.validation(self.user_search):
            self.user_search = input("You have entered an invalid book name, please try again ")
        self.response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + self.user_search)
        self.response = self.response.json()
        for item in self.response.get('items', [])[:5]:
            if 'title' not in item['volumeInfo'] or 'authors' not in item['volumeInfo'] or 'publisher' not in item[
                'volumeInfo']:
                continue
            # iterating over items in our api call and splicing to show only 5 data points
            # and only showing item.volumeInfo.authors,item.volumeInfo.title, and item.volumeInfo.publisher

            book_choice = "\n" "TITLE: %s,   " "\n"   "AUTHOR: %s,   " "\n"   "PUBLISHER: %s " "\n" % (
                item['volumeInfo']['title'], item['volumeInfo']['authors'], item['volumeInfo']['publisher'])

            print(book_choice)

