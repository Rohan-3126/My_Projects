users = [
    (1, 'alice', 30, True),
    (2, 'bob', 24, False),
    (3, 'charlie', 29, True),
    (4, 'Alice', 30, True),
    (5, 'Bob', 24, False),
    (6, 'Charlie', 29, True)
]

with open('file1.bin', 'wb') as f:
    for user_id, name, age, active in users:

        f.write(user_id.to_bytes(4, byteorder='little'))
        

        name_bytes = name.encode('utf-8')
        name_bytes = name_bytes[:20] + b'\x00' * (20 - len(name_bytes))
        f.write(name_bytes)
        
 
        f.write(age.to_bytes(1, byteorder='little'))


        f.write(b'\x01' if active else b'\x00')




users = [
    (1, 'alice', 30, True),
    (2, 'bob', 24, False),
    (3, 'charlie', 29, True),
    (4, 'Alice', 30, True),
    (5, 'Bob', 24, False),
    (6, 'Charlie', 29, True)
]

with open('file2.bin', 'wb') as f:
    for user_id, name, age, active in users:
        # ID as 4 bytes
        f.write(user_id.to_bytes(4, byteorder='little'))
        
        # Username as 20-byte string (padded)
        name_bytes = name.encode('utf-8')
        name_bytes = name_bytes[:20] + b'\x00' * (20 - len(name_bytes))
        f.write(name_bytes)
        
        # Age as 1 byte (if < 256)
        f.write(age.to_bytes(1, byteorder='little'))

        # Active flag as 1 byte
        f.write(b'\x01' if active else b'\x00')
