def uniq(input):
    output = []
    for element in input:
        if not hammaschon:   # <<< miracle
            output.append(element)
    return output

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_list = uniq(input_list)

for element in output_list:
    print(element)
