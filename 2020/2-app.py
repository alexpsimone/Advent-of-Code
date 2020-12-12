
def valid_pass_one():

    data = open('2-data.txt')
    valid_passwords = 0

    for line in data:
        line = line.rstrip()
        password_info = line.split(' ')
        
        letter_in_pass = 0
        required_letter = password_info[1][0]
        given_password = password_info[2]

        for letter in given_password:
            if letter is required_letter:
                letter_in_pass += 1

        valid_nums = password_info[0].split('-')

        if int(valid_nums[0]) <= letter_in_pass <= int(valid_nums[1]):
            valid_passwords += 1

    return valid_passwords


def valid_pass_two():

    data = open('2-data.txt')
    valid_passwords = 0

    for line in data:
        line = line.rstrip()
        password_info = line.split(' ')
        
        letter_in_pass = 0
        required_letter = password_info[1][0]
        given_password = password_info[2]
        indices = password_info[0].split('-')

        idx1 = int(indices[0]) - 1
        idx2 = int(indices[1]) - 1

        if given_password[idx1] == required_letter:
            if given_password[idx2] != required_letter:
                valid_passwords += 1

        elif given_password[idx2] == required_letter:
            valid_passwords += 1
        
    return valid_passwords