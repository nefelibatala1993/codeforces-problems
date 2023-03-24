#!/usr/bin/python3

def quick_sort(arr: list, start: int, end: int) -> None:
    if end - start <= 0:
        return

    pivot, write = arr[start], start + 1

    for read in range(start + 1, end + 1):
        if arr[read] < pivot:
            arr[read], arr[write] = arr[write], arr[read]
            write += 1

    arr[start], arr[write - 1] = arr[write - 1], arr[start]

    quick_sort(arr, start, write - 2)
    quick_sort(arr, write, end)


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        nums = list(map(lambda x: int(x), input().split()))

        quick_sort(nums, 0, len(nums) - 1)

        removed = 0

        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) <= 1:
                removed += 1

        if len(nums) - removed == 1:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
