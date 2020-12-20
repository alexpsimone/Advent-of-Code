def determine_seat_change(counter, seat_state):
    """Change a seat from empty/full or vice versa depending on counter"""

    if seat_state == 'L' and counter == 0:
        return '#'   
    if seat_state =='#' and counter > 3:
        return 'L'
    else:
        return seat_state

def count_filled_neighbors_top_line(seat_chart, line_idx, seat_idx):
    """Determine if a seat on the top line needs to change."""

    neighbors = 0

    if seat_chart[line_idx][seat_idx - 1] == '#':
        neighbors += 1
    if seat_chart[line_idx][seat_idx + 1] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx - 1] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx + 1] == '#':
        neighbors += 1
    
    return neighbors

def count_filled_neighbors_bottom_line(seat_chart, line_idx, seat_idx):
    """Determine if a seat on the bottom line needs to change."""

    neighbors = 0

    if seat_chart[line_idx][seat_idx - 1] == '#':
        neighbors += 1
    if seat_chart[line_idx][seat_idx + 1] == '#':
        neighbors += 1
    if seat_chart[line_idx - 1][seat_idx - 1] == '#':
        neighbors += 1
    if seat_chart[line_idx - 1][seat_idx] == '#':
        neighbors += 1
    if seat_chart[line_idx - 1][seat_idx + 1] == '#':
        neighbors += 1
    
    return neighbors

def count_filled_neighbors_left_col(seat_chart, line_idx, seat_idx):
    """Determine if a seat on the left column (not top/bottom line) needs to change."""

    neighbors = 0

    if seat_chart[line_idx - 1][seat_idx] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx] == '#':
        neighbors += 1
    if seat_chart[line_idx - 1][seat_idx + 1] == '#':
        neighbors += 1
    if seat_chart[line_idx][seat_idx + 1] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx + 1] == '#':
        neighbors += 1
    
    return neighbors

def count_filled_neighbors_right_col(seat_chart, line_idx, seat_idx):
    """Determine if a seat on the left column (not top/bottom line) needs to change."""

    neighbors = 0

    if seat_chart[line_idx - 1][seat_idx] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx] == '#':
        neighbors += 1
    if seat_chart[line_idx - 1][seat_idx - 1] == '#':
        neighbors += 1
    if seat_chart[line_idx][seat_idx - 1] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx - 1] == '#':
        neighbors += 1
    
    return neighbors

def count_filled_neighbors_general(seat_chart, line_idx, seat_idx):
    """Determine if a seat on the left column (not top/bottom line) needs to change."""
    
    neighbors = 0

    if seat_chart[line_idx - 1][seat_idx - 1] == '#':
        neighbors += 1
    if seat_chart[line_idx - 1][seat_idx] == '#':
        neighbors += 1
    if seat_chart[line_idx - 1][seat_idx + 1] == '#':
        neighbors += 1
    if seat_chart[line_idx][seat_idx - 1] == '#':
        neighbors += 1
    if seat_chart[line_idx][seat_idx + 1] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx - 1] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx] == '#':
        neighbors += 1
    if seat_chart[line_idx + 1][seat_idx + 1] == '#':
        neighbors += 1

    return neighbors

# open text file to get data
if __name__ == '__main__':
    data = open('11-data.txt', 'r')

# instantiate empty lists to fill with seat charts
old_seat_chart = []
new_seat_chart = []

# fill old_seat_chart with seed data
for line in data:
    old_seat_chart.append(line.strip())

# # create new_seat_chart with same empty floor spaces as old_seat_chart
# # use a unique character value (_) where seats would be, so the lists start out different
# for line_idx in range(len(old_seat_chart)):
#     new_seat_chart.append([])
#     for seat_idx in range(len(line)):
#         if old_seat_chart[line_idx][seat_idx] == '.':
#             new_seat_chart[line_idx].append('.')
#         else:
#             new_seat_chart[line_idx].append('_')


# update new_seat_chart
while new_seat_chart != old_seat_chart:

    for line_idx, line in enumerate(old_seat_chart):

        new_seat_chart.append([])

        for seat_idx, seat in enumerate(line):
            # print(f'line_idx: {line_idx} line: {line} seat_idx: {seat_idx} seat: {seat}')

            if line_idx == 0:
                if (seat_idx == 0 or seat_idx == (len(line)-1)) and seat != '.':
                    new_seat_chart[line_idx].append('#')

                else:
                    neighbors = count_filled_neighbors_top_line(old_seat_chart, line_idx, seat_idx)
                    new_seat_chart[line_idx].append(determine_seat_change(neighbors, seat))
            
            elif line_idx == (len(old_seat_chart) - 1):

                if (seat_idx == 0 or seat_idx == (len(line)-1)) and seat != '.':
                    new_seat_chart[line_idx].append('#')
                else:
                    neighbors = count_filled_neighbors_bottom_line(old_seat_chart, line_idx, seat_idx)
                    new_seat_chart[line_idx].append(determine_seat_change(neighbors, seat))

            else:
                if seat_idx == 0:
                    neighbors = count_filled_neighbors_left_col(old_seat_chart, line_idx, seat_idx)
                elif seat_idx == (len(line)-1):
                    neighbors = count_filled_neighbors_right_col(old_seat_chart, line_idx, seat_idx)
                else:
                    neighbors = count_filled_neighbors_general(old_seat_chart, line_idx, seat_idx)

                new_seat_chart[line_idx].append(determine_seat_change(neighbors, seat))

    old_seat_chart = new_seat_chart
    new_seat_chart = []
    

final_tally = 0

for line in new_seat_chart:
    for seat in line:
        if seat == '#':
            final_tally += 1

print(final_tally)