from elasticsearch import Elasticsearch
import json
# Kết nối tới Elasticsearch
es = Elasticsearch([{'host': '34.36.145.14', 'port': 80, 'scheme': 'http'}])

# Tạo một chỉ mục mới trong Elasticsearch
index_name = "m-ind"

# Đẩy dữ liệu JSON vào Elasticsearch
# Mở tệp tin output.json và đọc nội dung
with open( 'output-money.json', 'r',encoding='utf-8') as file:
    content = file.read()

# Phân tích cú pháp JSON
data = json.loads(content)

for item in data:
    # Đẩy từng mục vào Elasticsearch
    es.index(index=index_name, body=item)

# Đóng kết nối Elasticsearch
es.close()