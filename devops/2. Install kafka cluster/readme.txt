Cài đặt helm: https://helm.sh/docs/intro/install/

Tải repo bitnami về
    helm repo add bitnami https://charts.bitnami.com/bitnami

# Create k8s nameaspace for kafka
    kubectl create namespace apache-kafka

# Install Kafka cluster
    helm install apache-kafka bitnami/kafka -n apache-kafka --set replicaCount=2

# Kiểm tra triển khai có thành công không
    kubectl get service -n apache-kafka

# Tạo topic bằng kafka cli từ 1 pod trong cụm kafka

    Lấy tên 1 pod:
        kubectl get pods -n apache-kafka
    Vào CLI của pod
        kubectl exec -it <kafka-pod-name> -n apache-kafka -- /bin/bash
    Tạo topic bằng kafka cli:
        kafka-topics.sh --bootstrap-server localhost:9092 --create --topic stack-exchange --partitions 2 --replication-factor 2
    Kiểm tra danh sách các topic:
        kafka-topics.sh --bootstrap-server localhost:9092 --list

# Lấy địa chỉ IP của cụm kafka (không cần nữa vì thay bằng tên service là apache-kafka rồi)

    Tìm service chính chứa cụm kafka broker
        kubectl get services -n apache-kafka
    Sau khi tìm được sử dụng lệnh sau để lấy địa chỉ IP cluster
        kubectl get service <kafka-service-name> -n my-kafka-namespace