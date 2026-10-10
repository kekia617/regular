books = ['Catcher in the Rye', 'East of Eden', 'Goldfinch', 'Gone with the Wind',
        'Grapes of Wrath', 'Great Gatsby', 'Little Women', 'Of Mice and Man',
        'Scarlet Letter', 'To Kill a Mockingbird']
symptoms = ['heart_failure', 'kidney_failure', 'lung_abscesses', 'respiratory_failure', 'septic_shock']

count = 0
head = 0
tail = len(books) - 1
tail = len(symptoms) - 1
books_index = []
book_index = 0
# for book in books:
book = 'To Kill a Mockingbird'
symptom = 'septic_shock'
# while head <= tail:
#     # count += 1
    
#     aim = (head + tail) // 2
#     print('head=',head, 'tail=', tail, 'aim=', aim, 'books[aim]=', books[aim])
#     if books[aim] == book:
#         books_index.append(count)
#         # count = 0
#         head = 0
#         tail = len(books) - 1
#         break
#     elif book < books[aim]:
#         tail = aim - 1
#     else:
#         head = aim + 1
while head <= tail:
    # count += 1
    
    aim = (head + tail) // 2
    print('head=',head, 'tail=', tail, 'aim=', aim, 'symptoms[aim]=', symptoms[aim])
    if symptoms[aim] == book:
        # count = 0
        head = 0
        tail = len(symptoms) - 1
        break
    elif symptom < symptoms[aim]:
        tail = aim - 1
    else:
        head = aim + 1