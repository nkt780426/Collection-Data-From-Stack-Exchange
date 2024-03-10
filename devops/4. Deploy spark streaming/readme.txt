Đoạn code spark streming đóng vai trò như Kafka producer

B1: Tạo k8s secret key
    kubectl create secret generic aws-credentials \
    --from-literal=AWS_ACCESS_KEY_ID=<your-access-key-id> \
    --from-literal=AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
    (thay key thật vào)
B2: Triển khai đoạn code thành deployment
    vi streaming-deployment.yaml => Copy file ở thư mục này vào
    kubectl apply -f streaming-deployment.yaml
