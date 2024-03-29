spark-submit --master local[2] --deploy-mode client --num-executors 2 --executor-cores 1  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.apache.hadoop:hadoop-aws:3.2.2 main.py

spark-submit --master local[2] --deploy-mode client --num-executors 2 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.apache.hadoop:hadoop-aws:3.2.2 main.py

# Thêm biến môi trường (window) bắt buộc phải set biến môi trường trước khi submit job
set AWS_ACCESS_KEY_ID=your_access_key
set AWS_SECRET_ACCESS_KEY=your_secret_key

# Chạy local (test)
spark-submit --master local[2] --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.apache.hadoop:hadoop-aws:3.2.2 main.py