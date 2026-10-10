L = [2, 3, 9, 234, 32, 21, 6, 334]
L = ['mustard', 'salmon', 'azure', 'ivory', 'sage', 'lilac']
n = len(L)

pass_step = 1
for i in range(n, 1, -1):
    sort_value = False
    print("Pass:", pass_step)
    for j in range(i-1):
        
        print(f'Compare {L[j]} with {L[j+1]}', end='    ')
        if L[j] > L[j+1]:
            print('Swap')
            L[j], L[j+1] = L[j+1], L[j]
            sort_value = True
        else:
            print('Not Swap')
    pass_step += 1
    if not sort_value:
        break

print(L)
# color = 'ivory'
# head = 0
# tail = len(L)-1
# while head <= tail:
#     # count += 1
    
#     aim = (head + tail) // 2
#     print('head=',head, 'tail=', tail, 'search range:', L[head:tail+1], 'aim=', aim, 'Colors[aim]=', L[aim])
#     if L[aim] == color:
#         # count = 0
#         head = 0
#         tail = len(L) - 1
#         break
#     elif color < L[aim]:
#         tail = aim - 1
#     else:
#         head = aim + 1

