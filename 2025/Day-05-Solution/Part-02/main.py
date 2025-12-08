def get_fresh_details(ingredient_id: int, fresh_ranges: list[dict]) -> True:
    for range in fresh_ranges:
        if ingredient_id >= range['min'] and ingredient_id <= range['max']:
            is_fresh = True
            break
        else:
            is_fresh = False

    return is_fresh

def main():
    with open('ingredients.txt', 'r') as file:
        contents = file.read().splitlines()
        fresh_ranges = []

        for line in contents:
            if '-' in line:
                ranges = line.split('-')
                fresh_ranges.append({"min": int(ranges[0]), "max": int(ranges[1])})

    sorted_fresh_ranges = sorted(fresh_ranges, key=lambda x: (x['min'], x['max']))

    unique_fresh_ranges = []

    for current_range in sorted_fresh_ranges:

        # add first element to get the loop started
        if len(unique_fresh_ranges) == 0:
            unique_fresh_ranges.append(current_range)
            continue
        
        previous_range_max = unique_fresh_ranges[-1]['max']
        # if current min is less than or equal to previous max, adjust the previous range to include the new max
        if current_range['min'] <= previous_range_max:
            # only adjust if the new max is higher than previous, otherwise do nothing
            if current_range['max'] > previous_range_max:
                unique_fresh_ranges[-1]['max'] = current_range['max']
                continue
        else:
            unique_fresh_ranges.append(current_range)

    unique_ingredient_ids_high_low = set()
    unique_ingredient_ids_count = 0
    
    for current_range in unique_fresh_ranges:
        unique_ingredient_ids_count += current_range['max'] - current_range['min']
        # when you do 5 - 3, you get 2. We need to subtract 1 so we only get the middle values
        # we will handle max/min later outside of loop
        if current_range['max'] - current_range['min'] != 0:
            unique_ingredient_ids_count -= 1

        # since the values are inclusive on both the low and high side, make sure to count them
        unique_ingredient_ids_high_low.add(current_range['max'])
        unique_ingredient_ids_high_low.add(current_range['min'])

    print((len(unique_ingredient_ids_high_low)) + unique_ingredient_ids_count)

if __name__ == '__main__':
    main()