books = []

while True:
    print('Input book data')
    title = input('Book title: ')
    author = input('Book author: ')

    new_book = [title, author]
    books.append(new_book)

    for index, book in enumerate(books):
        print(f'{index+1} | {book[0]} | \t{book[1]}')
    keep_running = input('Insert book again? [Y/n]')

    if (keep_running == 'n'):
        break

print('success exit program')
