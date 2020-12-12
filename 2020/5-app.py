data = open('5-data.txt')
ticket_codes = []
ticket_info = []

row_bitmap = [0 for _ in range(128)]
col_bitmap = [0 for _ in range(8)]

for line in data:
    line = line.rstrip()
    ticket_codes.append(line)

# go through each id
for code in ticket_codes:
    # start your front/back markers at 0 and 127
    front = 0
    back = 127
    # go through the code from left to right
    # start by only checking the first 7 digits, which will be F or B
    for letter in code[:6]:
        # move the front or back marker based on each letter in the code
        # F: lower numbers, B: higher numbers
        difference_FB = back - front + 1
        if letter == 'F':
            back = int(back - difference_FB / 2)
        if letter == 'B':
            front = int(front + difference_FB / 2)

    if code[6] == 'F':
        row = front
    if code[6] == 'B':
        row = back
    row_bitmap[row] += 1
    # row_bitmap[row] += 1
    # now you can look at the last 3 digits, which are L and R
    # start left/right markers at 0 and 7
    left = 0
    right = 7

    for letter in code[7:9]:
        # move the left and right markers based on each letter in the code
        # L: lower numbers, R: higher numbers
        difference_LR = right - left + 1
        if letter == 'L':
            right = int(right - difference_LR / 2)
        if letter == 'R':
           left = int(left + difference_LR / 2)
    
    if code[9] == 'L':
        col = left
    if code[9] == 'R':
        col = right
    
    col_bitmap[col] += 1
    # col_bitmap[col] += 1
    # calculate unique id: row * 8 + col
    unique_id = row * 8 + col
    
    # add [id, (row, col)] to a list
    ticket_info.append(unique_id)


# sort the list by id
# print(sorted(ticket_info))
for idx, row in enumerate(row_bitmap):
    print (idx, row)

for idx, col in enumerate(col_bitmap):
    print (idx, col)


