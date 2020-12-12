data = open('4-data.txt')

passport_info = []

for line in data:
    line = line.rstrip()
    passport_info.append(line)

passport_dict = {}
required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn' ,'hzl', 'oth'}
num_valid_passports = 0
valid_passport = True

# for idx, line in enumerate(passport_info):
#     print(idx, line)

for line in passport_info:
    
    print(line)
    
    if line == '':
        print(f'passport_dict before clear: {passport_dict}')

        for required_key in required_keys:
            if required_key not in passport_dict:
                valid_passport = False
            elif required_key == 'byr' and (int(passport_dict[required_key]) < 1920 or int(passport_dict[required_key]) > 2002):
                valid_passport = False
            elif required_key == 'iyr' and (int(passport_dict[required_key]) < 2010 or int(passport_dict[required_key]) > 2020):
                valid_passport = False
            elif required_key == 'eyr' and (int(passport_dict[required_key]) < 2020 or int(passport_dict[required_key]) > 2030):
                valid_passport = False
            elif required_key == 'hgt':
                if passport_dict[required_key][-2:] == 'cm':
                    if int(passport_dict[required_key][:-2]) < 150 or int(passport_dict[required_key][:-2]) > 193:
                        valid_passport = False
                elif passport_dict[required_key][-2:] == 'in':
                    if int(passport_dict[required_key][:-2]) < 59 or int(passport_dict[required_key][:-2]) > 76:
                        valid_passport = False
                else:
                    valid_passport = False
            elif required_key == 'hcl':
                if passport_dict[required_key][0] != '#':
                    valid_passport = False
                else:
                    for letter in passport_dict[required_key][1:]:
                        if letter not in 'abcdef0123456789':
                            valid_passport = False
            elif required_key == 'ecl':
                if len(passport_dict[required_key]) > 3 or passport_dict[required_key] not in eye_colors:
                    valid_passport = False
            elif required_key == 'pid':
                if len(passport_dict[required_key]) != 9:
                    valid_passport = False
                else:
                    for num in passport_dict[required_key]:
                        if num not in '1234567890':
                            valid_passport = False
        if valid_passport:
            num_valid_passports += 1
        else:
            valid_passport = True
        passport_dict = {}
        print(f'num_valid_passports: {num_valid_passports}')

    else:
        k_v_pairs = line.split(' ')
        for k_v_pair in k_v_pairs:
            key = k_v_pair[:3]
            value = k_v_pair[4:]
            passport_dict[key] = value


print(num_valid_passports)


# go through each line of passport_info
# until you reach a blank space...
# check which fields are present in each line and add to passport_dict
# if each value in required_keys is in passport_dict, then increment num_valid_passports
