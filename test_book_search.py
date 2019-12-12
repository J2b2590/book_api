import unittest
import requests


class TestBookSearch(unittest.TestCase):

    def setUp(self):
        pass

    def test_validation(self, user_search=False, from_list=False):
        search_text = "You have entered an invalid book name, please try again "
        while not user_search:
            user_search = input(search_text)
            self.assertTrue(user_search == search_text)
        if from_list:
            while not any(book["title"] == user_search for book in self.response_list):
                user_search = input(search_text)
        return user_search

    def test_query_api(self):
        self.user_search = input("What kind of book are you looking for: ")
        self.response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + self.user_search)
        self.response = self.response.json()
        self.response_list = []
        for item in self.response.get('items', [])[:5]:
            if 'title' not in item['volumeInfo'] or 'authors' not in item['volumeInfo'] or 'publisher' not in item[
                'volumeInfo']:
                continue
            title = item['volumeInfo']['title']
            author = item['volumeInfo']['authors']
            publisher = item['volumeInfo']['publisher']

            book_choice = "\n" "TITLE: %s,   " "\n"   "AUTHOR: %s,   " "\n"   "PUBLISHER: %s " "\n" % (
                title, author, publisher)

            book = {"title": title, "author": author, "publisher": publisher}
            self.response_list.append(book)
            # testing for book to contain title, author, publisher
            self.assertEqual(
                book,
                {"title": title, "author": author, "publisher": publisher}
            )
            # test to ensure user search is being validated
            print(book_choice)


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
