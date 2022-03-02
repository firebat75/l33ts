def peakIndexInMountainArray(arr: list[int]) -> int:
    x = arr[1:-1]
    return x.index(max(x)) + 1
