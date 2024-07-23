'''
@Author: Your Name
@Date: 2024-07-23
@Last Modified by: Your Name
@Last Modified time: 2024-07-23
@Title :Program to convert a decimal number to a 4-byte binary string representation
'''

def to_binary(number):
    """
    Description:
        Function to convert a decimal number to its binary representation.
    Parameters:
        number: int, the decimal number to convert
    Returns:
        str: the binary representation of the decimal number, padded to 4 bytes (32 bits)
    """
    if number < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    
    binary_digits = []
    
    # Handle the special case where the number is zero
    if number == 0:
        binary_digits.append(0)
    
    
    while number > 0:
        binary_digits.append(number % 2)
        number //= 2
    
    # Reverse the list to get the correct binary representation
    binary_digits.reverse()
    
    # Convert list of digits to string without using map
    binary_str = ''
    for digit in binary_digits:
        binary_str += str(digit)
    
    # Pad the binary string to ensure it is 32 bits (4 bytes)
    padded_binary_str = binary_str.zfill(32)
    
    return padded_binary_str

def main():
    """Main function to execute the program."""
    try:
        decimal_number = int(input("Enter a non-negative integer: "))
        if decimal_number < 0:
            raise ValueError("Input must be a non-negative integer.")
        
        binary_representation = to_binary(decimal_number)
        print(f"The 4-byte binary representation of {decimal_number} is: {binary_representation}")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
