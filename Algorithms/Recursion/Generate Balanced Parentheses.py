def generate_balanced_parenthesis(i, j, ans = "", li = []):
    if i > j or i < 0 or j < 0:
        return ""

    if i == 0 and j == 0:
        li.append(ans)
        return ""

    if i == 0:
        opi = ans + ")"
        return generate_balanced_parenthesis(i, j - 1, opi, li)

    if j == 0:
        opj = ans + "("
        return generate_balanced_parenthesis(i - 1, j, opj, li)

    else:
        op1 = ans + "("
        op2 = ans + ")"
        return generate_balanced_parenthesis(i - 1, j, op1, li) + generate_balanced_parenthesis(i, j - 1, op2, li)

li = []
print(generate_balanced_parenthesis(9, 9, "", li))
print(len(li))