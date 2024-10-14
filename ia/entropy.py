from math import log


def i(P):
    if type(P) != list:
        P = [P]

    return sum([-p*log(p)/log(2) for p in P if p != 0])


def replace_I(data):
    splitted = data.replace('i(', "i([").split(',')
    data = ""
    for j in range(len(splitted)):
        sub = splitted[j]
        last_p = sub.rfind(')')
        if last_p > 0:
            splitted[j] = sub[:last_p]+']'+sub[last_p:]
        data += splitted[j] + ","
    return data[:-1]


while True:

    data = input("> ").strip().lower()
    if data == '':
        continue

    if data in ["quit", "q"]:
        break

    # I(1, 2) to I([1, 2])
    data = replace_I(data)

    try:
        print(eval(data))
    except Exception as e:
        print(e)
    print()
