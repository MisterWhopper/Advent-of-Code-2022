with open("input.txt") as f:
    lines = f.readlines()
    all_totals = []
    current_elf_total = []
    for line in lines:
        if line == "" or line == "\n":
            total = sum(current_elf_total)
            all_totals.append(total)
            current_elf_total.clear()
        else:
            number = int(line)
            current_elf_total.append(number)

print(max(all_totals))
print(sum(reversed(sorted(all_totals)[:3])))