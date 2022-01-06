def tower_of_honoi(n, frm, to, spare):
    if n == 1:
        print("Moving Disk", n, "from", frm, "to", to)
        return

    tower_of_honoi(n - 1, frm, spare, to)
    print("Moving Disk", n, "from", frm, "to", to)
    tower_of_honoi(n - 1, spare, to, frm)

tower_of_honoi(2, "a", "c", "b")
