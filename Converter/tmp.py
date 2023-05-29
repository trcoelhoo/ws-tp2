
with open("books.nt", "r") as file:
    with open("newbooks.nt", "w") as file02:
        for row in file:
            if row.startswith("<http://books.com/publishers/") and "ns#type" in row:
                comps = row.split()
                comps[2] = '<http://books.com/publishers#Publisher>.'
                nwrow = " ".join(comps)
                file02.write(f"{nwrow}\n")
            else:
                file02.write(row)
