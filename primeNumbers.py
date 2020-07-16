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
