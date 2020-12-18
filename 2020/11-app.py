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


if __name__ == '__main__':
    data = open('11-data.txt', 'r')

old_seat_chart = []
new_seat_chart = []

for line in data:
    line.strip()
    old_seat_chart.append(line)

while new_seat_chart != old_seat_chart:

    for line_idx, line in old_seat_chart:
        for seat_idx, seat in line:
            if line_idx == 0:
                if (seat_idx == 0 or seat_idx == -1) and seat != '.':
                    new_seat_chart[line_idx][seat_idx] == '#'

                else:
                    neighbors = count_filled_neighbors_top_line(old_seat_chart, line_idx, seat_idx)
                    new_seat_chart[line_idx][seat_idx] = determine_seat_change(neighbors, seat)

            if line_idx == -1:

                if (seat_idx == 0 or seat_idx == -1) and seat != '.':
                    new_seat_chart[line_idx][seat_idx] == '#'
                else:
                    neighbors = count_filled_neighbors_bottom_line(seat_chart, line_idx, seat_idx)
                    new_seat_chart[line_idx][seat_idx] = determine_seat_change(neighbors, seat)
            else:
                if seat_idx == 0:
                    neighbors = count_filled_neighbors_left_col(seat_chart, line_idx, seat_idx)
                elif seat_idx == -1:
                    neighbors = count_filled_neighbors_left_col(seat_chart, line_idx, seat_idx)
                else:
                    neighbors = count_filled_neighbors_general(seat_chart, line_idx, seat_idx)
                new_seat_chart[line_idx][seat_idx] = determine_seat_change(neighbors, seat)


