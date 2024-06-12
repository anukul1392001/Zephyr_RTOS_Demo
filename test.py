# Given hex string
hex_string = """
37 c0 73 59 ac 28 fd 9f 1c 66 36 c8 dc 14 a8 87 b1 f5 b1 82 8c 28 49 1a 00 b2 e5 90 f1 7e c4 94 13 42 36 25 2b 33 7b 28 89 6f 42 7b d3 d8 2d 21 a0 ef 8c 8d 66 7a b8 33 63 c6 bb 6a 07 71 66 c3 82 e0 b9 2b 7d 20 67 1f 86 fd 4c 64 9e 78 a6 bc 2f c8 c4 e7 cf 
87 22 5f 10 aa 60 e3 5b 35 df 77 37 8e 65 e5 45 a5 cf d6 c2 ee 48 75 3b 51 a2 c0 6f 63 92 e4 0b 8e 2a 5d 20 33 98 20 8a 20 c4 69 dc d7 7c 42 13 9d 4a f9 08 e4 f3 c5 cc 70 c5 d4 b4 5f 4a 5c 9b 45 9d fe bb 1f d3 f4 78 01 7e fe 60 fd 7f 10 10 11 75 80 9a 68 
5a 77 5e be a0 b1 01 8d bb e2 0a a1 5f 93 9a 14 3b f6 03 36 62 52 a0 b1 65 fe 24 58 d6 10 a4 2f 06 00 62 27 c9 fd ea f1 8b d4 55 a6 ec e0 7a f6 c4 d8 d8 fa 16 20 7a 71 e4 ce de 61 d7 8f c9 78 ce 56 f5 86 47 97 2b 54 e6 1d 6c 11 ba 76 bb d4 3c c6 70 4e 22 
f2 af 04 29 97 35 b0 6a 33 e3 7a 05 f3 82 70 cc 57 08 7b c6 0b d1 1c 4a f2 8c 9a ce d5 82 31 63 a0 0d e0 8f d6 a2 93 64 9c 6b 72 ad 31 c0 ad 2f 55 e6 a2 9c 66 9f 4a 9b 40 9b bb a3 5e 74 ef 8b f4 4f d0 7e 5a cb ed 8c 29 3f aa 73 bf 5b 12 ec 89 05 14 02 cd 
87 2a 21 1b 2f 5f 72 aa 9a 76 21 2e 31 9f 73 53 00 20 cb 24 72 b0 ec e8 c0 fb 66 48 5d 18 c3 be 3f 47 9a b8 a0 2c 2e cc 60 26 11 d9 d8 b6 51 ce 48 11 b8 f1 5b 10 da 11 3a 5e e2 a9 1c f0 72 8c bd ec 36 c0 37 3a 02 57 fa 81 de fa 7e d6 4d 57 f2 dc a5 6a 8d 
b7 29 9b ba af 48 40 76 07 f5 f8 66 0f b2 1d 42 0c ae 6c 23 11 f7 09 be 88 8a 02 f7 a0 6a 65 27 1a d1 ff 6f ca cb 18 17 8d 17 4c 92 d7 91 63 16 52 41 1e ab 8d 81 4b 6b 0e 0c 04 7f 66 d6 52 79 f0 5c fd 68 16 1b 0f b2 06 31 f3 5d 60 2d e1 2c 02 35 c6 3b e7 
70 7e   
"""

# Removing whitespaces and converting hex string to list of bytes
bytes_list = hex_string.split()

# Counting the number of bytes
number_of_bytes = len(bytes_list)
print(number_of_bytes)
