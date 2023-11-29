import json

# Đường dẫn tới file JSON lớn
input_file = 'output-money.json'

# Số lượng file con cần tạo
num_files = 5

# Đọc dữ liệu từ file JSON lớn
with open(input_file, 'r',encoding='utf-8') as f:
    data = json.load(f)

# Tính số lượng phần tử trong từng file con
total_records = len(data)
records_per_file = total_records // num_files

# Chia dữ liệu thành các file con
for i in range(num_files):
    # Tạo tên file con
    output_file = f'sub_file_{i}.json'
    
    # Xác định phần dữ liệu cần ghi vào file con
    start_index = i * records_per_file
    end_index = start_index + records_per_file
    
    # Ghi dữ liệu vào file con
    with open(output_file, 'w') as f:
        json.dump(data[start_index:end_index], f)