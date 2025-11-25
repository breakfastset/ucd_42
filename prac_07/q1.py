def read_data(filename):
    """Read data from file into a list of lists of numbers."""
    numbers_list = []
    in_file = open(filename, "r")
    # 10,7,34,12,9,5,19,-5
    for line in in_file.readlines():
        data = line.split(",")  # ['10', '7', '34', .... '-5']
        data = [int(num) for num in data if int(num) >= 10]  # convert all to int
        numbers_list.append(data)  # add data to list of lists
    in_file.close()
    return numbers_list


def display_sorted_numbers(numbers_list):
    """Sort each list and display with commas as separator."""
    for numbers in numbers_list:
        sorted_numbers = sorted(numbers)
        data = [str(num) for num in sorted_numbers]  # convert back to string
        line = ",".join(data)   # convert the list to a string with separator
        print(line)


def main():
    """Start of program."""
    # 1. Read the file contents into a list of lists.
    numbers_list = read_data("numbers.txt")
    # print(numbers_list)
    # 2. Display each list sorted with commas as separators
    display_sorted_numbers(numbers_list)


main()