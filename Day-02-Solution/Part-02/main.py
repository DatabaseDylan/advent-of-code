def main():
    invalid_product_ids = []

    with open('product_ids.txt', 'r') as file:
        product_ids = file.read().split(',')
    
    for product_id_range in product_ids:
        product_id_range = product_id_range.split('-')
        low_val = int(product_id_range[0])
        high_val = int(product_id_range[1])

        for product_id in range(low_val, high_val):
            product_id = str(product_id)

            # if a single digit, exit early
            # e.g. 7
            if len(product_id) == 1:
                continue

            # Convert to SET to remove dupes and if equal to 1 it means every character is repeated
            # Also, Repeat char 1 logic above to avoid introducing a bug if code changes
            # e.g. 111111111
            if len(set(product_id)) == 1 and len(product_id) != 1:
                invalid_product_ids.append(int(product_id))
                continue

            # Optimization
            # e.g. 112
            if len(set(product_id)) != 1 and len(product_id) <= 3:
                continue

            character_count = len(product_id)
            if character_count % 2 == 0:
                split_index = int(character_count / 2)

                while split_index != 0:
                    string_split = [(product_id[i:i+split_index]) for i in range(0, len(product_id), split_index)]

                    if len(set(string_split)) == 1:
                        invalid_product_ids.append(int(product_id))
                        break
                    
                    split_index -= 1
            elif character_count % 3 == 0:
                split_index = int(character_count / 2)

                while split_index != 0:
                    string_split = [(product_id[i:i+split_index]) for i in range(0, len(product_id), split_index)]

                    if len(set(string_split)) == 1:
                        invalid_product_ids.append(int(product_id))
                        break
                    
                    split_index -= 1

    print(sum(invalid_product_ids))

if __name__ == '__main__':
    main()