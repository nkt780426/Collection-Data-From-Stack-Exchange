
Tạo nameaspace trên k8s để chứa cụm apache_spark:
    kubectl create namespace apache-spark

Tạo file values.yaml và copy cái file values.yaml ở thư mục này vào
    vi spark-cluster-values.yaml

Deploy spark chart vào cụm k8s:
    Tạo nameaspace apache_spark trong k8s:
        kubectl create nameaspace apache_spark
    helm install <tên release> <tên chart hoặc đường dẫn char> -f spark-cluster-values.files -n apache-spark
