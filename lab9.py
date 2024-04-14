#John Riley

def encoder(input_number):
    #takes input and encodes a password
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

def decode(newstring):
    #take an encoded string and decodes it
    newlist = []
    decodedstring = ""
    for i in range(len(newstring)):
        newlist.append(int(newstring[i]))
    final_list = [sublist - 3 for sublist in newlist]
    for i in range(len(final_list)):
        decodedstring = decodedstring + str(final_list[i])
    return decodedstring




# I added this code as we are a 3 person group and Zilong already added the decoder function, so theres no need for redundant function, hence i am commenting it out.


# def decode(encoded_password):
#     # Validate the input
#     if len(encoded_password) != 8 or not encoded_password.isdigit():
#         return "Invalid password. Please enter an 8-digit password containing only numbers."
#
#     # Decode each digit
#     # creates an empty list for the decoded digits
#     decoded_digits = []
#     for digit in encoded_password:
#         new_digit = (int(digit) - 3) % 10
#         decoded_digits.append(str(new_digit))
#     # joins the decoded digits into a single string, then returns that string
#     decoded_password = ''.join(decoded_digits)
#     return decoded_password
#


def main():
    #menu loop logic
    user_choice = 0
    while user_choice != 3:
        print("Menu")
        print("-------------")
        user_choice = int(input("1. Encode\n2. Decode\n3. Quit\n"))
#provides output based on choice of user

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
