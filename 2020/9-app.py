if __name__ == '__main__':
    data = open('9-data.txt', 'r')

NUMS = []
for line in data:
    line = line.rstrip()
    NUMS.append(int(line))


def create_num_window(first_idx, NUMS):
    """ Create a sliding window of 26 numbers, starting at a given index."""

    # look in a sliding window of 26 indices
    # the items at indices 0-25 go into num_list
    num_list = [num for num in NUMS[first_idx:(first_idx + 26)]]

    return num_list


def is_valid_cipher(num_list):
    """Determine if the 26th number in a list is the sum of any of the other 25 numbers."""

    sum_val = num_list[-1]

    for x in num_list[:-1]:
        for y in num_list[:-1]:
            if x + y == sum_val and x != y:
                return True
    
    return False

def find_encryption_weakness(NUMS):
    """Find the first number that doesn't have the required property."""    

    for idx in range(len(NUMS)-25):

        num_list = create_num_window(idx, NUMS)
        # print(num_list)

        if not is_valid_cipher(num_list):

            return (idx, num_list[-1])


def recurse_to_solution(NUMS, first, last):

    window = NUMS[first:last]

    # if those numbers equal the key val, then return those numbers
    if sum(window) == 104054607:
        # this doesn't actually return anything meaningful; I finished this by hand after getting window
       window.sort()
       return window[0] + window[-1]
    
    # if the sum is larger than the key val, then move the front of the window back 1 idx
    if sum(window) > 104054607:
        recurse_to_solution(NUMS, first, last -1)

    # if the sum is smaller than the key val, then extend the size of the window by 1 and compare the new sum
    if sum(window) < 104054607:
        recurse_to_solution(NUMS, first - 1, last)



idx, target = find_encryption_weakness(NUMS)

print(recurse_to_solution(NUMS, idx - 2, idx))