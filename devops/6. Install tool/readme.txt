Tạo configmap
kubectl create configmap elasticsearch-config --from-file=elasticsearch.yml

Tạo secret chứa thông tin tài khoản aws
kubectl create secret generic aws-credentials \
  --from-literal=AWS_ACCESS_KEY_ID=your-access-key-id \
  --from-literal=AWS_SECRET_ACCESS_KEY=your-secret-access-key

----------------------------------------------------------------

Chạy elasticsearch
helm install my-elasticsearch bitnami/elasticsearch \
  --set replicaCount=3 \
  --set cluster.env.MINIMUM_MASTER_NODES=3 \
  --set data.replicaCount=3

(mặc định data.replicaCount=2, master.replicaCount=3, port = 9200)

------------------------------------------------------------------
Dùng helm để tạo kibana

Map nó với elasticsearch đã tạo 
helm install my-kibana bitnami/kibana \
  --set elasticsearchHosts=my-elasticsearch-client-svc:9200

------------------------------------------------------------------
Cài đặt Prometheus và Grafana bằng Helm

# Tạo namespace cho Prometheus và Grafana
kubectl create namespace monitoring

# Thêm repository Helm của Bitnami
helm repo add bitnami https://charts.bitnami.com/bitnami

# Cài đặt Prometheus
helm install prometheus bitnami/kube-prometheus --namespace monitoring

# Cài đặt Grafana
helm install grafana bitnami/grafana --namespace monitoring


Truy cập grafana dashboard
# Lấy mật khẩu của Grafana
export GRAFANA_PASSWORD=$(kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode)

# Port-forward để truy cập Grafana
kubectl port-forward --namespace monitoring svc/grafana 3000:80

# Mở trình duyệt và truy cập http://localhost:3000/
# Đăng nhập bằng tên người dùng là "admin" và mật khẩu là $GRAFANA_PASSWORD
