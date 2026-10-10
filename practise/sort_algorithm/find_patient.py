L = [12, 9, 7, 4, 2]
week = 10
head = 0
tail = len(L)-1

if week > L[head]:
    L = L[:head] + [week] + L[head:]
elif week <= L[tail]:
    L = L[:tail+1] + [week] + L[tail+1:]
else:
    while head <= tail:
        
        aim = (head + tail) // 2
        print('head=',head, 'tail=', tail, 'search range:', L[head:tail+1], 'aim=', aim, 'Weeks[aim]=', L[aim])
        if L[aim] == week:
            while L[aim] == week:
                aim += 1
            print(f'Insert number at position {aim}')
            L.insert(aim, week)
            break
        elif week < L[aim] and week > L[aim+1]:
            print(f'{week} weeks less than {L[aim]} at position {aim} and greater than {L[aim+1]} at position {aim+1}')
            print(f'So Insert week number at position {aim+1}')
            L.insert(aim+1, week)
            break
        elif week > L[aim]:
            tail = aim - 1
        else:
            head = aim + 1

if head > tail:
    print("not found")
print(L)