def encoder(input_number):
    input_string = str(input_number)
    if len(input_string) != 8 or not input_string.isdigit():
        return "Invalid password. Please enter an 8-digit password containing only numbers."

    # Encode each digit
    encoded_list = []
    for digit in input_string:
        adjusted_digit = (int(digit) + 3) % 10
        encoded_list.append(str(adjusted_digit))

    encoded_result = ''.join(encoded_list)

    return encoded_result

def decode(encoded_text):
    digit_list = []
    decoded_text = ""
    for i in range(len(encoded_text)):
        digit_list.append(int(encoded_text[i]))
    processed_list = [number - 3 for number in digit_list]
    for i in range(len(processed_list)):
        decoded_text = decoded_text + str(processed_list[i])
    return decoded_text

def main():
    user_choice = 0
    while user_choice != 3:
        print("Menu")
        print("-------------")
        user_choice = int(input("1. Encode\n2. Decode\n3. Quit\n"))

        if user_choice == 1:
            result_password = encoder(input("Please enter your password to encode: "))
        elif user_choice == 2:
            original_text = decode(result_password)
            print(f"The encoded password is {result_password}, and the original password is {original_text}\n")
            pass
        elif user_choice == 3:
            quit()


if __name__ == "__main__":
    main()
