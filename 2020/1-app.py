def two_numbers_to_2020():

    num_data = open('1-data.txt')
    nums = set()

    for line in num_data:
        line = line.rstrip()
        nums.add(int(line))

    for num in nums:
        if (2020 - num) in nums:
            return(num, 2020-num, num*(2020-num))

def three_numbers_to_2020():

    num_data = open('1-data.txt')
    nums = set()

    for line in num_data:
        line = line.rstrip()
        nums.add(int(line))

    for first_num in nums:
        difference = 2020 - first_num

        for second_num in nums:
            if second_num < difference:
                third_num = difference - second_num
                if third_num in nums:
                    return(first_num, second_num, third_num, first_num*second_num*third_num)



