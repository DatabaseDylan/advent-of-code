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
        ingredient_ids = []
        fresh_ranges = []

        for line in contents:
            if '-' in line:
                ranges = line.split('-')
                fresh_ranges.append({"min": int(ranges[0]), "max": int(ranges[1])})
            elif line != '':
                ingredient_ids.append(int(line))

    fresh_ingredients_counter = 0

    for ingredient_id in ingredient_ids:
        ingredient_is_fresh = get_fresh_details(ingredient_id=ingredient_id, fresh_ranges=fresh_ranges)
        if ingredient_is_fresh == True:
            fresh_ingredients_counter += 1

    print(fresh_ingredients_counter)

if __name__ == '__main__':
    main()