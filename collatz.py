def collatz_cycle(n):
    while n != 1:
        #print(n)
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1
    #print(1)

def get_first_n_cycles(n):
    for i in range(1, n + 1):
        cycle = list(collatz_cycle(i))
        #print(f"Cycle {i}:", *cycle)
        yield (f"Cycle {i}:", *cycle)

def list_to_latex(items):
    if not items:
        return ''  # Return an empty string if the input list is empty

    latex_list = "\\begin{itemize}\n"
    for item in items:
        latex_list += f"  \\item {item}\n"
    latex_list += "\\end{itemize}"

    return latex_list

def list_first_20():
    cycles = get_first_n_cycles(20)
    sumlist = []
    for c in cycles:
        sumlist.append(' '.join([''.join(str(x)) for x in c]))
    latexstr = list_to_latex(sumlist)
    print(latexstr)
