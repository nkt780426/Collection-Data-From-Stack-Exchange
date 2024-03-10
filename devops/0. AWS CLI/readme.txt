- Lấy Access key của tài khoản root aws
    Account => Security credentials => Tạo Access key (nhớ download key về giữ cẩn thận)
- Tải AWS CLI và config tài khoản của mình vào
    +) Nhập: aws configure và làm theo hướng dẫn
    +) Nhớ set region là ap-southeast-2 (ở singapore, càng set xa việt nam càng mất tiền)
    
- Truy cập trang web: https://kops.sigs.k8s.io/getting_started/aws/
    +) Nhấn ctrl+F tìm đến dòng sau và làm theo các lệnh bên dưới
        You can create the kOps IAM user from the command line using the following
    +) Sau khi thực hiện các lệnh trên sẽ trả về 1 chuỗi JSON là tài khoản IAM được tạo 
    ra với các quyền tối thiểu để chạy kops
        Lưu cái này vào 1 file nào đấy tý nữa dùng
    +) Thực hiện lệnh aws configure lần nữa và thay Access key và secret key vào

    
=> Vậy là ta đã cấu hình thành công công cụ kops để tạo k8s cluster (vào lại mục user sẽ thấy tên tài khoản kops)
Điểm khác biệt giữa kops và eks là nó triển khai 2 phiên bản của kubernetes 
    +) 1 cái open source free, 1 cái ko free nhưng cũng chả thêm gì nhiều
    +) Với kops bạn phải quản lý tất cả, còn với eks nó sẽ giấu thành phần controller plane đi
    và nhận trách nhiệm quản lý tất cả (và hỗ trợ nếu gặp khó khăn)