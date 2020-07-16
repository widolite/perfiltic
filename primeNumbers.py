# Input:
# 1. 5
# 2. 6
# 3. 7
# 4. 53

# Salida:
# 1. PRIMO
# 2. NO_ES_PRIMO
# 3. PRIMO
# 4. PRIMO


from sys import stdin


def is_number_prime(input):
    # su código va acá
    input = int(input)
    if input > 1:
        for num in range(2, input):
            if (input % num) == 0:
                output = "NO_ES_PRIMO"
                break
            else:
                output = "PRIMO"
    else:
        output = "NO_ES_PRIMO"
    input = "{}\n".format(output)
    return input


if __name__ == '__main__':
    # tener cuidado en python con los newlines
    for line in stdin:
        print(is_number_prime(line), end='')
