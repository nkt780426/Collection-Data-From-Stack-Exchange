import pandas as pd
from hdfs import InsecureClient

# Đọc dữ liệu mẫu
df = pd.read_csv(
    "https://thachln.github.io/datasets/bank/bankadditional-full.csv", sep=";"
)
# Kết nối vào Hadoop
client_hdfs = InsecureClient("http://ubuntu:9870", user="root")
# Lưu Dataframe vào Hadoop
with client_hdfs.write(
    "/user/root/datasets/bank-additional-full.csv", encoding="utf-8"
) as writer:
    df.to_csv(writer)
