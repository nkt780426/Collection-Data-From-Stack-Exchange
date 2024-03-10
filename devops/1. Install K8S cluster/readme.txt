# Truy cập vào trang web sau, nhấn ctrl + F tìm dòng sau
We recommend keeping the creation of this bucket confined to us-east-1, otherwise more work will be required.
=> Thực hiện lệnh bên dưới để tạo 1 s3-bucket (kops dùng đây là nơi lưu trữ cấu hình k8s)
  Nhớ đổi region sang ap-southeast-2 và tên bucket. Ví dụng
  aws s3api create-bucket \
    --bucket hoangvo \
    --region ap-southeast-2 \
    --create-bucket-configuration LocationConstraint=ap-southeast-2

# Cài đặt kops và kubectl: 
  https://kops.sigs.k8s.io/install/
  https://kops.sigs.k8s.io/install/

# Tạo k8s cluster
  kops create cluster --name=demok8scluster.k8s.local --state=s3://hoangvo --zones=ap-southeast-2a --node-count=2 --
node-size=t2.micro --master-size=t2.micro  --master-volume-size=8 --node-volume-size=8


* Triển khai
kops update cluster demok8scluster.k8s.local --yes --state=s3://hoangvo

# Cách thêm, xóa node
  - Chỉnh file cấu hình
    kops edit ig nodes
  - Cập nhật cluster
    kops update cluster --name mycluster.hoangvo.k8s.local --yes --admin
  - Sử dụng lệnh sau để không gây gián đoạn dịch vụ
    kops rolling-update cluster --name mycluster.hoangvo.k8s.local --yes

# Kiểm tra cụm có được cài đặt đúng không
  kops validate cluster
  kubectl get nodes

# Sử dụng Helm để cài đặt Nginx Ingress Controller
  helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
  helm repo update
  helm install my-ingress-nginx ingress-nginx/ingress-nginx

# Lấy subdomain free và map nó với địa chỉ ip của ingress controller
