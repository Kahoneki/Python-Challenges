def flatten(arr):
    output = []
    for i in arr:
        for k in i:
            output.append(k)
    return output

print(flatten([[1,2],[3,4]]))