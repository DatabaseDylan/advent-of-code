def main():
    with open('batteries.txt', 'r') as file:
        batteries = file.read().splitlines()

    battery_voltages = []

    for battery in batteries:
        unique_numbers = list(dict.fromkeys(list(battery)))
        unique_numbers.sort(reverse=True)
        largest_first_digit = unique_numbers[0]
        battery = tuple(battery)

        largest_second_digit = -1
        i = 0
        keep_running = True
        # Find the first occurence of the largest first digit
        while keep_running == True:
            for digit in battery:
                if digit == largest_first_digit and (i + 1) == len(battery):
                    # if our largest digit in the list only appears at the very end of the list, start over and try the next highest number!
                    largest_first_digit = unique_numbers[1]
                    i = 0
                    break
                elif digit == largest_first_digit:
                    i += 1
                    keep_running = False
                    break
                else:
                    i += 1
        
        # Find the largest second digit after the index of the largest first digit
        for index in range(i,len(battery)):
            current_num = int(battery[index])
            if current_num > largest_second_digit:
                largest_second_digit = current_num
                if largest_second_digit == 9:
                    # Optimization
                    break

        print(int(str(largest_first_digit) + str(largest_second_digit)))
        battery_voltages.append(int(str(largest_first_digit) + str(largest_second_digit)))
    
    print(sum(battery_voltages))

if __name__ == '__main__':
    main()