def subsets(string, output):
    if not string:
        print(output)
        return

    op1 = output
    op2 = output + string[0]
    subsets(string[1:], op1)
    subsets(string[1:], op2)

subsets("abc", "")