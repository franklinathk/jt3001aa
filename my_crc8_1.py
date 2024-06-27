def crc8(data, polynomial, initial_value):
    crc = initial_value

    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1

    return crc & 0xFF

# Convert the input string to a list of integers
input_data = [int(byte, 16) for byte in input_string.split()]

# CRC-8 parameters
polynomial = 0x31  # x^8 + x^5 + x^4 + 1
initial_value = 0xFF

# Calculate CRC-8
result = crc8(input_data, polynomial, initial_value)

# Display the result in hexadecimal format
print(hex(result))
