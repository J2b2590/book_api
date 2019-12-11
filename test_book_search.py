import unittest
import requests


from book_search import book_search
book = book_search()


class TestBookSearch(unittest.TestCase):

    def setUp(self):
        pass

    def test_validation(self,from_list = False):
        # additional validation goes here
        user_search = input("What kind of book are you looking for: ")
        search_text = "You have entered an invalid book name, please try again "
        while not user_search:
            user_search = input(search_text)
            print("User did not enter valid input search text should appear")
        if from_list:
            while not any(book["title"] == user_search for book in self.response_list):
                user_search = input(search_text)
        self.assertFalse(user_search == search_text)
        return user_search


    def test_query_api(self):
        self.user_search = input("What kind of book are you looking for: ")
        # self.user_search = self.test_validation(self.user_search)
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

            self.assertTrue(self.user_search == self.test_validation(self.user_search))

            print(book_choice)

    # def __init__(self):
    #     self.query_api()

if __name__ == '__main__':
    unittest.main()
    print("Everything passed")