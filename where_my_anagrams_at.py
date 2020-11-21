def anagrams(word, words):
    
    solution = []

    def str_sort(string):
        return "".join(sorted(list(string)))
    
    for item in words:
        if str_sort(word) == str_sort(item):
            solution.append(item)
    return solution
    