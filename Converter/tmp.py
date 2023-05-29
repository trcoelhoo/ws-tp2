
with open("books.nt", "r") as file:
    with open("newbooks.nt", "w") as file02:
        for row in file:
            if row.startswith("<http://books.com/publishers/"):
                comps = row.split()
                id = comps[0].strip(">").strip("<").split("/")[-1]
                comps[0] = f"publisher:{id}"
                file02.write(f"{' '.join(comps)}\n")
            else:
                file02.write(row)
