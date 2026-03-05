# --- File Handling with Context Manager (with open) ---

# Writing to a file
# 'w' mode: write (creates file if not exists, overwrites if it does)
# with open("test.txt", "w") as file:
#     file.write("Hello, Python!\n")
#     file.write("This is a file handling example.\n")
#     # 'file' is automatically closed when we leave this block

# Reading from a file
# 'r' mode: read (default)
try:
    with open("test.txt", "r") as file:
        # Method 1: readlines() with list comprehension and strip()
        # strip() removes whitespace from both ends, including \n
        content_stripped = [line.strip() for line in file.readlines()]
    
        print("\n--- File Content (with readlines() and strip()) ---")
        print(content_stripped)
    

except FileNotFoundError:
    print("File not found.")

# Appending to a file
# 'a' mode: append (adds to the end)
# with open("test.txt", "a") as file:
#     file.write("Adding a new line.\n")
