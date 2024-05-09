def convert_to_str(numbers: list[int]) -> list[str]:
    """
    Get a list of numbers of type int.
    Returns a new list of string values.
    """
    new_numbers = [str(number) for number in numbers]
    return new_numbers


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(convert_to_str(nums))
