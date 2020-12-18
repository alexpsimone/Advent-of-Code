if __name__ == '__main__':
    data = open('11-data.txt', 'r')

old_seat_chart = []
new_seat_chart = []

for line in data:
    line.strip()
    old_seat_chart.append(line)



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

# for line in data
for line_idx, line in old_seat_chart:
    # for seat in line
    for seat_idx, seat in line:
        # if the line number is zero:
        if line_idx == 0:
            # if the seat number zero or -1:
            if seat_idx == 0 or seat_idx == -1:
                new_seat_chart[line_idx][seat_idx] == '#'
            # else
            else:
                neighbors = count_filled_neighbors_top_line(old_seat_chart, line_idx, seat_idx)
                new_seat_chart[line_idx][seat_idx] = determine_seat_change(neighbors, seat)

        # elif the line number is -1

            # if the seat number is zero or -1:
                # if the seat is empty:
                    # fill it, no exceptions
                # if the seat is full:
                    # don't do anything, it'll never be surrounded by 4 others

            # else
                # if the seat is empty:
                    # check index before/after in same line
                    # check index before/equal/after in previous line
                    # if no filled seats in these indices, then fill the seat
                # if the seat is full:
                    # check index before/after in same line
                    # check index before/equal/after in previous line
                    # if at least 4 filled seats in these indices, then empty the seat

        # else
            # if the seat number is zero:
                # check zeroth index in prev and next lines
                # check first index in prev/this/next lines
                # increment counter every time a full seat is seen
                # if this seat is empty and counter == 0:
                    # change seat to full
                # if this seat is full and counter >= 4:
                    # change seat to empty

            # elif the seat number is -1:
                # check -1 index in prev and next lines
                # check -2 index in prev/this/next lines
                # increment counter every time a full seat is seen
                    # if this seat is empty and counter == 0:
                        # change seat to full
                    # if this seat is full and counter >= 4:
                        # change seat to empty

            # else
                # check prev/this/next index in prev line
                # check prev/next index in this line
                # check prev/this/next index in next line
                # increment counter every time a full seat is seen
                # if this seat is empty and counter == 0:
                    # change seat to full
                # if this seat is full and counter >= 4:
                    # change seat to empty


