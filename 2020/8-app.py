def is_good_program(rules, bitmap):

    accumulator = 0
    this_idx = 0
    next_idx = 0

    while bitmap[next_idx] != 1:
        
        # print(this_idx, next_idx, accumulator)

        # flip bit for that index from 0 to 1 in bitmap
        bitmap[this_idx] += 1

        # follow directions for that rule
        if rules[this_idx][0] == 'acc':
            accumulator += rules[this_idx][1]
            next_idx = this_idx + 1

        elif rules[this_idx][0] == 'jmp':
            next_idx = this_idx + rules[this_idx][1]

        elif rules[this_idx][0] == 'nop':
            next_idx = this_idx + 1

        this_idx = next_idx

        if next_idx == len(rules):

            print(f'*******ACCUMULATOR***********: {accumulator}')
            return True

    return False


if __name__ == '__main__':
    data = open('8-data.txt', 'r')

rules = []
for line in data:
    line = line.rstrip()
    words = line.split(' ')
    rules.append((words[0], int(words[1])))

# go through data line by line
for idx in range(len(rules)):

    # print(idx, rules[idx])
    # switch one nop to jmp
    if rules[idx][0] == 'jmp':
        new_rules = [val for val in rules]
        new_rules[idx] = ('nop', new_rules[idx][1])
        bitmap = [0 for _ in range(len(rules))]
        if is_good_program(new_rules, bitmap):
            break
    
    # or switch one jmp to nop
    elif rules[idx][0] == 'nop':
        new_rules = [val for val in rules]
        new_rules[idx] = ('jmp', new_rules[idx][1])
        bitmap = [0 for _ in range(len(rules))]
        if is_good_program(new_rules, bitmap):
            break
            



