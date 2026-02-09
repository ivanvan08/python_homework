def inversion(arr):
    inv = []
    rnge = len(arr)
    for i in range(rnge):
        for j in range(i + 1, rnge):
            if arr[i] > arr[j]:
                inv.append((arr[i], arr[j]))
    return inv


def is_partly_sorted(arr, multiplier):
    count = len(inversion(arr))
    return count <= multiplier * len(arr)


if __name__ == "__main__":
    arr = [3, 4, 2, 1, 5, 6, 0]
    inv = inversion(arr)
    print(f"Список - {arr}\nІнверсії: {inv}")
    print(f"Частково впорядкований (коеф. - 2) - {is_partly_sorted(arr, 2)}")
    print(f"Частково впорядкований (коеф. - 1.5) - {is_partly_sorted(arr, 1.5)}")
    print(f"Частково впорядкований (коеф. - 1) - {is_partly_sorted(arr, 1)}")
