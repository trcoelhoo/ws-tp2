
with open("books.nt", "r") as file:
    with open("newbooks.nt", "w") as file02:
        for row in file:
            _row = list(row.strip("\n"))
            if len(_row) == 0:
                continue
            if _row[-1] == '.':
                file02.write(row)
            else:
                tmp = row.strip("\n")
                file02.write(f"{tmp}.\n")
