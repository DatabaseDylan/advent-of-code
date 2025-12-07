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
            character_count = len(product_id)
            if character_count % 2 == 0:
                half_char = int(character_count / 2)
                part_one = product_id[:half_char]
                part_two = product_id[half_char:]

                if part_one == part_two:
                    invalid_product_ids.append(int(product_id))

    print(sum(invalid_product_ids))

if __name__ == '__main__':
    main()