def flatten(data):
    result = []
    if not isinstance(data, list):
        result.append(data)
        return result
    else:
        for num in data:
            result = result + flatten(num)
        return result

print([1]+[2])
print(flatten([1,2, [3,4,5],[[[2, 3], 4, [6, 7]]]]))
print(flatten([[[[[[]]]]]]))