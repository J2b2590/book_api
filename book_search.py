import requests


# request module

class book_search:
    user_search = input("What kind of book are you looking for: ")
    # user search is letting the user query the api for their desired book
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + user_search)
    # response variable is making the api call to the book api
    response = response.json()
    # the json method is converting text into a data object to I can read it

    for item in response.get('items', [])[:5]:
        if 'title' not in item['volumeInfo'] or 'authors' not in item['volumeInfo'] or 'publisher' not in item[
            'volumeInfo']:
            continue
        # iterating over items in our api call and splicing to show only 5 data points
        # and only showing item.volumeInfo.authors,item.volumeInfo.title, and item.volumeInfo.publisher

        book_choice = "\n" "TITLE: %s,   " "\n"   "AUTHOR: %s,   " "\n"   "PUBLISHER: %s " % (
            item['volumeInfo']['title'], item['volumeInfo']['authors'], item['volumeInfo']['publisher'])

        print(book_choice)

