from elasticsearch import Elasticsearch
import threading

# Khởi tạo Elasticsearch client
es = Elasticsearch([{'host': '34.36.145.14', 'port': 80, 'scheme': 'http'}])


# Hàm đọc file và ghi dữ liệu vào Elasticsearch
def process_file(filepath):
    with open(filepath, 'r',encoding='utf-8') as f:
        # Đọc nội dung file
        data = f.read()

        # Ghi dữ liệu vào Elasticsearch
        es.index(index='m-ind', body={'content': data})

# Tạo danh sách các file cần đọc và ghi dữ liệu vào Elasticsearch
filepaths = ['sub_file_0.json', 'sub_file_1.json', 'sub_file_2.json', 'sub_file_3.json','sub_file_4.json']

# Chạy các hàm process_file() trên các luồng khác nhau
threads = []
for filepath in filepaths:
    t = threading.Thread(target=process_file, args=(filepath,))
    threads.append(t)
    t.start()

# Đợi cho tất cả các luồng hoàn thành
for t in threads:
    t.join()

# In ra số lượng document đã được thêm vào Elasticsearch
print('Total documents: ', es.count(index='m-ind')['count'])