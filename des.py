PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

ROTATIONS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

INITIAL_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FINAL_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

P_BOX = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

S_BOXES = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

def permutate(key, table):
    """Permutasikan kunci atau blok berdasarkan tabel tertentu"""
    return [key[i - 1] for i in table]

def left_shift(bits, n):
    """Lakukan rotasi kiri pada array bit"""
    return bits[n:] + bits[:n]

def generate_subkeys(key_64bit):
    """Menghasilkan 16 subkunci dari kunci 64-bit"""
    while len(key_64bit) % 64 != 0:
        key_64bit.append(0)
    # Permutasi pertama (PC1) menghasilkan kunci 56-bit
    key_56bit = permutate(key_64bit, PC1)
    
    # Pecah kunci menjadi dua bagian 28-bit
    C = key_56bit[:28]
    D = key_56bit[28:]
    
    # List subkunci untuk 16 putaran
    subkeys = []
    for round_num in range(16):
        # Rotasi kiri sesuai dengan tabel ROTATIONS
        C = left_shift(C, ROTATIONS[round_num])
        D = left_shift(D, ROTATIONS[round_num])
        
        # Gabungkan kembali dan permutasikan dengan PC2 untuk menghasilkan subkunci 48-bit
        combined_key = C + D
        subkey = permutate(combined_key, PC2)
        
        subkeys.append(subkey)
    
    return subkeys

def xor(a, b):
    return [i ^ j for i, j in zip(a, b)]

def feistel_function(right, subkey):
    expanded_right = permutate(right, EXPANSION_TABLE)  # Ekspansi
    xored = xor(expanded_right, subkey)  # XOR dengan subkey
    
    substituted = []
    for i in range(8):
        block = xored[i*6:(i+1)*6]
        row = (block[0] << 1) + block[5]
        col = (block[1] << 3) + (block[2] << 2) + (block[3] << 1) + block[4]
        substituted += [int(b) for b in format(S_BOXES[i][row][col], '04b')]
    
    return permutate(substituted, P_BOX)

def split_in_half(block):
    return block[:32], block[32:]

def des_round(left, right, subkey):
    new_left = right
    new_right = xor(left, feistel_function(right, subkey))
    return new_left, new_right

def des_encrypt(block, subkeys):
    block = permutate(block, INITIAL_PERMUTATION)  # Permutasi awal
    left, right = split_in_half(block)
    
    for subkey in subkeys:  # 16 putaran Feistel
        left, right = des_round(left, right, subkey)
    
    combined_block = right + left  # Gabungkan kembali L dan R
    return permutate(combined_block, FINAL_PERMUTATION)  # Permutasi akhir

def des_decrypt(block, subkeys):
    block = permutate(block, INITIAL_PERMUTATION)
    left, right = split_in_half(block)
    
    for subkey in reversed(subkeys):  # Urutkan subkunci terbalik
        left, right = des_round(left, right, subkey)
    
    combined_block = right + left
    return permutate(combined_block, FINAL_PERMUTATION)

def string_to_bit_array(text):
    result = []
    for char in text:
        # Mengambil nilai ASCII dari karakter, lalu mengonversinya menjadi representasi biner 8-bit
        bin_val = bin(ord(char))[2:].zfill(8)  # ord() mengubah karakter ke ASCII, bin() menjadi biner
        result.extend([int(bit) for bit in bin_val])  # Pisahkan setiap bit dan tambahkan ke array
    return result

def bit_array_to_string(bit_array):
    chars = []
    for b in range(0, len(bit_array), 8):
        byte = bit_array[b:b+8]  # Ambil setiap 8 bit (1 byte)
        byte_str = ''.join([str(bit) for bit in byte])  # Gabungkan bit jadi string
        chars.append(chr(int(byte_str, 2)))  # Konversi dari biner ke karakter ASCII
    return ''.join(chars)

def des_encrypt_text(plain_text, subkeys):
    bit_array = string_to_bit_array(plain_text)
    
    # Tambahkan padding jika teks bukan kelipatan 64 bit (8 byte)
    while len(bit_array) % 64 != 0:
        bit_array.append(0)  # Tambahkan padding berupa bit 0

    cipher_text = []
    for i in range(0, len(bit_array), 64):
        block = bit_array[i:i+64]
        cipher_block = des_encrypt(block, subkeys)
        cipher_text.extend(cipher_block)

    return cipher_text

def des_decrypt_text(cipher_text, subkeys):
    plain_text_bits = []

    for i in range(0, len(cipher_text), 64):
        block = cipher_text[i:i+64]
        plain_block = des_decrypt(block, subkeys)
        plain_text_bits.extend(plain_block)

    plain_text = bit_array_to_string(plain_text_bits)
    return plain_text

encrypted_texts = []
key = None
subkeys = None

while True:
    print("\n==== MENU ====")
    print("1. Generate new key")
    print("2. Encrypt text")
    print("3. Decrypt all text")
    print("4. Exit")

    choice = input("Enter menu number: ")

    if choice == "1":
        # Generate new key
        key = input("Enter new key: ")
        while len(key) > 8:
            print("Key must not longer than 8 characters, please try again.")
            key = input("Enter new key: ")
        key = string_to_bit_array(key)
        subkeys = generate_subkeys(key)
        # print("New key generated:", key)
        print("New key generated")

    elif choice == "2":
        if key is None:
            print("Please generate a key first (Menu 1).")
        else:
            # Encrypt text
            plain_text = input("Enter text to encrypt: ")
            encrypted = des_encrypt_text(plain_text, subkeys)
            encrypted_texts.append(encrypted)
            print("Text has been encrypted and stored.")

    elif choice == "3":
        if not encrypted_texts:
            print("No encrypted texts found.")
        else:
            # Decrypt all texts
            print("Decrypting all texts...")
            for idx, encrypted in enumerate(encrypted_texts):
                decrypted = des_decrypt_text(encrypted, subkeys)
                print(f"Decrypted text {idx + 1}: {decrypted}")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please select a valid option.")