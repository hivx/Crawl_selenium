# Đọc file gốc và lọc các dòng bắt đầu bằng ký tự @
with open("data/Data_KOL.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Lọc các dòng bắt đầu bằng ký tự @
filtered_lines = [line.strip() for line in lines if line.startswith('@')]

# Ghi các dòng lọc được vào file mới
with open("data/nickname_KOL.txt", "w", encoding="utf-8") as output_file:
    for line in filtered_lines:
        output_file.write(line + "\n")
