def split_into_chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

# Example usage
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
print(split_into_chunks(L1, n))
