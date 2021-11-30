def reverse_stack(st):
    if len(st) <= 1:
        return
    ele = st.pop()
    reverse_stack(st)
    put_back(st, ele)

def put_back(st, ele):
    if not st:
        st.append(ele)
        return
    temp = st.pop()
    put_back(st, ele)
    st.append(temp)


st = [5, 4, 3, 2, 1]
reverse_stack(st)
print(st)
