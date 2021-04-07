# Compact Code

list_of_good_books = ['The Bravest Monk', 'Fairy Tales', 'The Motion of the Suberbans']

# Wrong 
def is_good_book(book_name):
    if book_name in list_of_good_books:
        return True
    else:
        return False



# Correct
def is_good_book_compact_version(book_name):
    return book_name in list_of_good_books
