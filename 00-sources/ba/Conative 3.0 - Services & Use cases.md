# 	

# 

# **Conative 3.0 \- Services & Use cases**

# 

| Project Code | Conative |
| :---: | :---: |
| **Documentation Code** | v3.0.0 |
| **Last Modified Date** | Jul 27, 2023 |
| **Author** | [Frank Tran](mailto:franktran@cbidigital.com) |

# 

# 

# **CHANGE RECORDS**

\*N \- New, E – Edit, R \- Remove

| Date | Section Change | N\* E, R | Content Change | PIC \- Person In Charge |
| :---- | :---- | :---- | :---- | :---- |
|    Jun 30, 2023 |  | \*N |  |  |
| Jul 6, 2023 |  | \*N | Update UC 4.1 \- 4.10 Product Performance |  |
| Jul 18, 2023 |  | \*N, E | Update  STT UC Product performance  Add UC 4.2. 1 \- 4.2.4 Sales by Category UC 4.3. 1 \- 4.3.4 Sales by Collection Config column |  |
| Jul 19, 2023 |  | E | Update UC 1.4 Update password  Update UC 4.1.4 Advanced Filter  Bổ sung fields  Bổ sung rules Update UC Select time range  Default time range  Define last xx days |  |
| Jul 19, 2023 |  | E | Update UC 1.4 Update password  Update UC 4.1.4 Advanced Filter  Bổ sung fields  Bổ sung rules Update UC Select time range  Default time range  Define last xx days |  |
| Jul 24, 2023 |  | E | Update UC 4.1.4 Advanced Filter  Quy định hiển thị & thao tác  |  |
| Jul 27, 2023 | Custom report | E | Update UC 4.1.12-13 Quy định hiển thị & thao tác  |  |
| Jul 31, 2023 | Custom report | \*N, E, R | Update  UC id cho Custom report (3.1 \- 3.6) Remove UC 4.1.12 \- 16 |  |
| Jul 31, 2023 | Custom report | \*N, E, | Add UC 3.3.2 Remove access Add UC 3.6 Search Custom report Add UC 3.7 Filter custom report  |  |

# 

# 

# **List of Services** 

**High priority**

1. **User Service** 

   1. Sign up & create 1st Organization 

   2. Sign in 

   3. Forgot password

   4. Update Password 

   5. Update user’s name 

   6. Column Configuration 

      

      

2. **Organization Service**

   1. Create Organization

   2. Switch Organization 

   3. View members in an organization

   4. Update roles & permissions 

   5. Invite user to an Organization

   6. Remove user out of an organization

   7. Leave Organization 

3. **Report Service**

   1. Create custom report

   2. Update custom report	

   3. Share custom report

   4. Delete View 

   5. Export 

 


4. **Data Service** 

   1. Product performance view

   2. Low stock 

   3. Sales by collection

   4. Sales by price range 

   5. Sales by category

   6. Facebook Ads mapping 

   7. Mizmooz (Color grouping)

   8. Chart API module 

   9. Advanced filter 

   10. 

5. **Setting Service**

- Default settings by Organization 

  - Time zone 

  - Lead time 

  - Price Range 

  - Column configuration & time range 

  - Price Range

  - Category 

- Setting by Users

6. **Integration Service** 

- Connect to Shopify 

- Connect to Google Ads

- Connect to Google Analytics 

- Connect to Facebook ads

7. **Authorization Service** 

8. **Notification Service** 

9. **Payment & subscription Service**

10. **Purchase Order Modules**

- View PO list 

- Filter location

- Create new PO

- Add new vendor / Supplier 

11. **Tenancies Service**

12. **Event Service**

# 

Use cases chi tiết 

# **UC 1.1 \- Sign up & Create 1st Organization**

## **1.1. Mục tiêu**

User đăng ký tài khoản và tạo organization trên hệ thống App.Conative.ai

## **1.2. Input**

Email address  
First Name & Last Name

Password & Confirm Password

Organization Name  
Link invite (Đối với các user được gửi invite qua email) \- Optional  
Select consent checkbox

**1.3. Output**

Đăng ký tài khoản và và tạo Organization thành công / thông báo lỗi và nguyên nhân đăng ký không thành công

**1.4. Workflow**

**Diagram:** 

### **Main flow (Happy case)**

1\. User vào trang Sign up của App.conative.ai  
2\. User nhập email và bấm **Create for Free**  
3\. Hệ thống gửi OTP về email để verify email (Phase 2\)  
4\. User nhập OTP để verify email (Phase 2\)  
5\. Hệ thống kiểm tra OTP nhập chính xác và tự động redirect sang trang nhập thông tin Profile & Organization  
6\. User nhập /chọn thông tin để sign up & create Organization 

- First Name & Last name  
- Password & Confirm Password  
- Organization Name  
- Chọn Organization Size (0-50, 51-100, 101 \- 200, \>200)  
- Chọn Industry (Ecommerce, Retail)


7\. Nhấn vào consent checkbox  
8\. Bấm **Create for Free** để hoàn thành Sign up & create Organization  
9\. Hệ thống kiểm tra thông tin nhập hợp lệ với business rule.  
10\. Thông báo Sign up & Create Organization thành công, direct vào trang **Onboarding** của Conative.   
11\. Kết thúc use case

### **Alternative Flow**

Đăng ký tài khoản bằng link invite từ email của Admin Organization

1\. Admin Organization thêm Team member bằng cách nhập email của user được mời   
2\. Hệ thống gửi Invite link qua email của user  
3\. User bấm vào link invite trong email  
4\. Hệ thống kiểm tra link invite còn hiệu lực sẽ direct user sang trang Sign In  
5\. Nếu chưa có tài khoản, bấm Sign up  
6\. Hệ thống hiển thị form nhập thông tin để tạo tài khoản:

- First Name & Last Name  
- Password & Confirm Password

7\. Hệ thống kiểm tra thông tin nhập hợp lệ  
8\. Sign up tài khoản và cho phép user truy cập vào Organization đã được mời, direct vào trang **Dashboard** của Conative. 

9\. Kết thúc use case

3a. Hệ thống kiểm tra thông tin: Email không hợp lệ / Email đã tồn tại trong hệ thống

- Thông báo lỗi thông tin nhập không hợp lệ / Email đã tồn tại trong hệ thống \[Message: *to be updated\]*  
- Kết thúc use case

3b. Hệ thống kiểm tra thông tin: Password không hợp lệ

- Thông báo lỗi thông tin nhập không hợp lệ \[Message: *to be updated\]*  
- Kết thúc use case

## **1.5 Business rule**

**Quy định hiển thị và thao tác**

Email

- Mặc định rỗng  
- Bắt buộc nhập  
- Trong trường hợp sign up bằng link invite, email đăng ký phải khớp với email được invite  
- Email sign up không được trùng với email đã tồn tại trong hệ thống

First Name & Last Name 

- Mặc định rỗng  
- Bắt buộc nhập

Password:

- Mặc định rỗng  
- Bắt buộc nhập  
- Ít nhất 6 ký tự, 1 số, 1 chữ in hoa, 1 chữ thường, 1 ký tự đặc biệt  
- Password & Confirm password phải khớp nhau

Organization Name

- Mặc định rỗng  
- Bắt buộc nhập  
- Logo của Organization sẽ hiển thị 2 chữ cái đầu viết in hoa của Organization

Organization size & Industry

- Dropdown  
- Mặc định rỗng  
- Bắt buộc chọn 

Invite link:

- Hết hạn sau khi invite 24h

Avatar: 

- Hiển thị chữ cái đầu của tên người dùng 

Consent checkbox

Bắt buộc nhập

**1.6 Reference**

Wireframe & Design:

* Wireframe: [https://www.figma.com/file/hVQ0gOjlLM5EbeIWgz1J7W/Conative-AI?type=design\&node-id=3574-54635\&t=4ZnCVuzMxn0egHPF-4](https://www.figma.com/file/hVQ0gOjlLM5EbeIWgz1J7W/Conative-AI?type=design&node-id=3574-54635&t=4ZnCVuzMxn0egHPF-4)

* Design

API Doc

# **UC 1.2 \- [Sign in](#uc-1.2---sign-in)** {#uc-1.2---sign-in}

## **1.1. Mục tiêu**

User đăng nhập thành công vào hệ thống App.Conative.ai bằng email và password đã được cấp. 

## **1.2. Input** 

Email

Password

## **1.3. Output** 

Đăng nhập thành công vào một Organization / thông báo lỗi và nguyên nhân đăng nhập không thành công 

## **1.4. Workflow** 

### **Main flow (Happy case)** 

1\. Vào trang Sign in của App.conative.ai

2\. Nhập email và password của tài khoản 

3\. Hệ thống kiểm tra thông tin email đã tồn tại trong hệ thống và password nhập chính xác 

4\. Hệ thống hiển thị danh sách các organization mà user này thuộc về

5\. User chọn organization mình muốn truy cập trên Conative

6\. Đăng nhập thành công vào Organization, redirect đến trang **Dashboard**

7\. Kết thúc use case

### **Alternative Flow**

Sign in bằng link Invite của Admin Organization 

1\. Admin Organization thêm Team member bằng cách nhập email của user được mời 

2\. Hệ thống gửi Invite link qua email của user

3\. User bấm vào link invite trong email

4\. Hệ thống kiểm tra link invite còn hiệu lực sẽ direct user sang trang Sign in

5\. Nếu đã có tài khoản, quay về **Main flow Sign in**

### **Exceptional flow**

2a. Tài khoản không tồn tại trên hệ thống 

- Hệ thống kiểm tra email nhập vào và không tìm thấy email của tài khoản trong hệ thống 

- Thông báo tài khoản không tồn tại trên hệ thống Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

- Kết thúc use case


2b. Password không chính xác 

- Hệ thống kiểm tra password nhập vào không chính xác 

- Thông báo password không chính xác. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

- Kết thúc use case 

## **1.5 Business rule** 

**Quy định phân quyền**

User thực hiện use case này phải có role: 

- Member, Admin của organization bất kỳ trên Conative 

**Quy định hiển thị và thao tác** 

Email

- Mặc định rỗng 

- Bắt buộc nhập

- Là email của tài khoản đã có trong hệ thống


Password 

- Mặc định rỗng

- Bắt buộc nhập

- Ít nhất 86 ký tự, 1 số, 1 chữ in hoa, 1 chữ thường, 1 ký tự đặc biệt

Link Invite

- Thời hạn expiry của link invite: 24h. 

- Thông báo link đã expired khi user bấm vào link trên mail và direct về trang lỗi. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

Link ở trang Sign in: 

- Privacy policy: [https://www.conative.ai/privacy-policy](https://www.conative.ai/privacy-policy)  
- Terms of service: [https://www.conative.ai/terms-of-service](https://www.conative.ai/terms-of-service) 

## **1.6 Reference** 

- Use case Diagram

- Workflow

- Wireframe & Design

- API Doc

# **UC 1.3 \- Forgot password**

## **1.1. Mục tiêu**

Yêu cầu reset lại mật khẩu trong trường hợp quên mật khẩu khi đăng nhập.

## **1.2. Input** 

Email của user 

## **1.3. Output**

Link reset password 

## **1.4. Workflow** 

### **Main flow (Happy case)**

1\. Bấm "Forgot Password" ở trang Đăng nhập

2\. Nhập email đăng ký tài khoản để nhận link Reset Password. 

3\. Hệ thống gửi link reset password và code đến email được đăng ký tương ứng

4\. Hệ thống direct sang trang verify OTP 

5\. User nhập OTP nhận được trong mail để xác thực OTP

6\. Hệ thống xác nhận OTP thành công và direct người dùng sang trang nhập New Password

7\. User nhập New password & Confirm Password khớp nhau, sau đó chọn **Change password.** 

8\. Hệ thống thông báo Change password thành công, direct user về trang Sign in. 

9\. User sign in với password mới thành công. 

10\. Kết thúc use case  

### **Exceptional flow**

2a. User nhập email không tồn tại trong hệ thống 

\- Hệ thống thông báo lỗi. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

3b. User không nhận được email từ hệ thống

\- User chọn **Resend code** để hệ thống gửi lại OTP qua email sau. 

\- Hệ thống gửi OTP mới đến email của user, và disable CTA resend code trong vòng 30s

5a.  User nhập OTP không chính xác

\-   Hệ thống hiển thị underlined text: **Your verification code is incorrect.**  

5b. Nhập code đã expired: 

 \- Hệ thống hiển thị underlined text: **Your verification code has expired. Please enter a new one\!** 

5c.  Thời gian để enter & re-enter password là 5 phút. Sau 5 phút hiển thị underlined text: **OTP is expired.**

## **1.5 Business rule**

## **Quy định hiển thị và thao tác**

Email reset password 

- Mặc định rỗng 

- Bắt buộc nhập 

- Underlined text khi user chọn Reset password mà bỏ trống email. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

Verification code OTP

- Mặc định rỗng

- Bắt buộc nhập 

- Underlined text khi user không nhập hoặc nhập OTP không hợp lệ. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)** 

- Thời gian hiệu lực của OTP: 5 phút 

- Thời gian giữa các lần resend OTP: 30s. 

- Sau khi user chọn **Click to Resend,** CTA sẽ chuyển thành text resend in \<xx second\> 30s sẽ đếm ngược. Hết 30s hiển thị lại  CTA **Click to resend**

Password & Confirm password 

- Mặc định rỗng 

- Bắt buộc nhập 

- Password Ít nhất 8 ký tự, 1 số, 1 chữ in hoa, 1 chữ thường, 1 ký tự đặc biệt

- Password mới không được trùng với password cũ lần gần nhất

- Hiển thị dấu tick xanh kế bên password sau khi user nhập password hợp lệ

- Hiển thị dấu chấm chéo đỏ kế bên password sau khi user nhập password không hợp lệ

- Hiển thị dấu tick xanh bên cạnh field Confirm new password sau khi user nhập password khớp với field New Password

- Underlined text khi 1 trong 2 field password / confirm password bỏ trống: **Please enter your new password**

- Underlined text khi password & Confirm password không match hoặc field Confirm password bỏ trống. 

## **1.6 Reference** 

Design: [https://zpl.io/XYowQpX](https://zpl.io/XYowQpX)

# **UC 1.4 \- Update Password** 

Design: [https://zpl.io/z80BgjX](https://zpl.io/z80BgjX)

## **1.1. Mục tiêu**

User có thể thay đổi mật khẩu tài khoản 

## **1.2. Input** 

Current password, new password, new password confirmation 

## **1.3. Output** 

## **1.4. Workflow** 

### **Main flow (Happy case)** 

1. Người dùng chọn thay đổi password

2. Người dùng điền password hiện tại 

3. Hệ thống verify BE 

- Nếu đúng, đến bước tiếp theo 

- Nếu sai, thông báo lỗi và yêu cầu người dùng nhập lại và đề xuất “Quên mật khẩu”

4. Người dùng điền password mới 

5. Hệ thống validate FE format 

- Nếu đúng, đến bước tiếp theo 

- Nếu sai, thông báo lỗi và yêu cầu người dùng nhập lại, đề xuất lỗi 

6. Người dùng điền xác nhận lại password mới 

7. Hệ thống validate FE format 

- Nếu đúng, đến bước tiếp theo 

- Nếu sai, thông báo lỗi và yêu cầu người dùng nhập lại

8. Người dùng bấm chọn xác nhận thay đổi password 

9. Hệ thống ghi vào database 

### **Alternative flow**

3\. Hệ thống verify BE 

- Nếu đúng, đến bước tiếp theo 

- Nếu sai, thông báo lỗi và yêu cầu người dùng nhập lại và đề xuất “Quên mật khẩu”

4\. Người dùng chọn “Quên mật khẩu”

5\. Tiếp tục UC Forgot password 

## **Business rule**

Validation: 

- Password mới phải đúng theo format yêu cầu: x ký tự, …

- Password confirmation phải giống với password mới 

Quy định hiển thị:

- Password nhập vào chỉ hiển thị “\*” 

- Có thể chọn ẩn hoặc hiện password nhập vào 

# **UC 1.5 \- Update user’s name** 

# **UC 2.1 \- Switch Organizations in 1 account** 

## **1.1. Mục tiêu**

User chọn organization mình đã tạo / được tham gia để truy cập và thao tác trong Organization đó

## **1.2. Input** 

Quyền member / admin của user của ít nhất 2 organization 

## **1.3. Output** 

Chuyển đổi qua Organization khác thành công 

## **1.4. Workflow** 

### **Main flow (Happy case)** 

1\. User vào menu Account, hover **Switch organization**, sau đó chọn organization muốn switch 

2\. Hệ thống kiểm tra thông tin user và Organization hợp lệ

3\. Redirect user sang trang Admin của Organization user vừa switch

4\. Kết thúc use case

### **Alternative Flow** 

Chọn organization trong list organization sau khi sign in (Xem Flow [Sign in](#uc-1.2---sign-in))

## **1.5 Business rule** 

**Quy định phân quyền**

User thực hiện use case này phải có role: 

- Member, Admin của organization đó

## **1.6 Reference** 

- Use case Diagram

- Workflow

- Wireframe & Design

- API Doc

# 

# **UC 2.2 \- Create Organization** 

## **1.1. Mục tiêu** 

Tạo một organization mới trong hệ thống để quản lý các user, tuỳ chỉnh và xem được dữ liệu của organization của mình. 

## **1.2 Input** 

Quyền tạo Organization

Organization name

## **1.3 Output** 

Organization được tạo thành công 

Người tạo được mặc định gán role & permission  của Admin và là user đầu tiên của Organization đó

## **1.4 Workflow**

### **Main flow (Happy case)**

1\. User vào trang Sign up của App.conative.ai

2\. User nhập email và bấm **Create for Free**

3\. Hệ thống gửi OTP về email để verify email (Phase 2\)

4\. User nhập OTP để verify email (Phase 2\)

5\. Hệ thống kiểm tra OTP nhập chính xác và tự động redirect sang trang nhập thông tin Profile & Organization

6\. User nhập /chọn thông tin để sign up & create Organization 

* First Name & Last name

* Password & Confirm Password

* Organization Name

* Chọn Organization Size (0-50, 51-100, 101 \- 200, \>200)

* Chọn Industry (Ecommerce, Retail)

7\. Bấm **Create for Free** để hoàn thành Sign up & create Organization

8\. Hệ thống kiểm tra thông tin nhập hợp lệ với business rule.

9\. Thông báo Sign up & Create Organization thành công, direct vào trang Home của Conative.  direct sang trang Create Organization

5\. Kết thúc use case

### **Exceptional flow** 

### **Alternative Flow** 

Create 2nd Organization 

1. Ở mục menu Account, hover vào **Switch Organization,** chọn **Add new Organization** 

2. Hiển thị Popup \> Chọn **Set up a new organization**

3. Nhập thông tin Organization: 

* Organization Name

* Chọn Organization Size (0-50, 51-100, 101 \- 200, \>200)

* Chọn Industry (Ecommerce, Retail)

4. Bấm **Create new Organization** để hoàn thành create Organization

5. Hệ thống kiểm tra thông tin nhập hợp lệ với business rule.

6. Thông báo Create Organization thành công, direct vào trang Home của Organization vừa tạo.

7. Kết thúc use case.

## **1.5 Business rule**

**Quy định hiển thị và thao tác**

Organization Name

* Mặc định rỗng

* Bắt buộc nhập

Organization size & Industry

* Dropdown

* Mặc định rỗng

* Bắt buộc chọn 

## **1.6. Reference**

- Wireframe: [https://www.figma.com/file/hVQ0gOjlLM5EbeIWgz1J7W/Conative-AI?type=design\&node-id=3596-57207\&t=mbaHNPP1OKa56g3z-4](https://www.figma.com/file/hVQ0gOjlLM5EbeIWgz1J7W/Conative-AI?type=design&node-id=3596-57207&t=mbaHNPP1OKa56g3z-4)

- Design

- API Doc

 

# **UC 2.3 \- View members in an organization**

## **1.1 Mục tiêu** 

 Xem danh sách các user trong hệ thống, bao gồm email, username, role & permission của mỗi user.

## **1.2 Input**

Có permission xem danh sách các user trong hệ thống 

## **1.3. Output**

 Xem danh sách các user trong hệ thống, bao gồm email, username, role & permission của mỗi user.

## **1.4. Workflow** 

1\. Sau khi đăng nhập vào một Organization, user vào menu **Account,** chọn **Admin** 

2\. Vào menu Organization \> Member 

3\. Xem danh sách member của Organization đó

4\. Kết thúc use case

# **UC 2.4 \-  Update role & permission**

## **1.1. Mục tiêu:** 

Thay đổi role & permission của một user đã có trong hệ thống 

## **1.2. Input** 

Role & Permission của hệ thống đó

## **1.3 Output**

Role & Permission của user được thay đổi thành công 

## **1.4 Workflow**

### **Mainflow** 

1\. Ở trang quản lý Organization, hệ thống hiển thị danh sách các user trong hệ thống, bao gồm email, User name, role của mỗi user. 

2\. Admin chọn một user muốn thay đổi role & permission, bấm vào dropdown ở cột role để thay đổi role mới

3\. Hệ thống tự động cập nhật role mới cho user đó và hiển thị thông báo hành công 

4\. Hệ thống hiển thị lại danh sách các user trong hệ thống với vai trò và quyền hạn mới của user được cập nhật.

5\. Kết thúc use case

### **Exceptional flow** 

## **1.5 Business rule**

**Quy định phân quyền**

User thực hiện use case này phải có role: 

- Admin của organization đó

- Role & permission của user phải được định nghĩa trước trong hệ thống


- 

## **1.6 Reference**

- Wireframe: [https://www.figma.com/file/hVQ0gOjlLM5EbeIWgz1J7W/Conative-AI?type=design\&node-id=3620-56674\&t=mbaHNPP1OKa56g3z-4](https://www.figma.com/file/hVQ0gOjlLM5EbeIWgz1J7W/Conative-AI?type=design&node-id=3620-56674&t=mbaHNPP1OKa56g3z-4)

- API Doc

# **UC 2.5 \- Invite user to an Organization** 

## **1.1. Mục tiêu:** 

Thêm một user mới vào hệ thống bằng cách gửi link invite qua email cho user đó

## **1.2. Input** 

Email của user được mời vào hệ thống 

## **1.3 Output**

User nhận được invite link qua email, đăng nhập thành công vào organization trên hệ thống 

## **1.4 Workflow**

### **Mainflow** 

1\. Ở trang quản lý Organization, Admin chọn "Add member".

2\. Hệ thống hiển thị một form để nhập thông tin của user mới, bao gồm email, role & permission 

3\. Admin nhập thông tin và bấm “**Add**”

4\. Hệ thống thêm user đó vào organization với status là Pending, hiển thị email & status của user trong danh sách member.

5\. Hệ thống gửi invite link đến email của user.

6\. User chọn invite link trong email 

7\. Hệ thống direct user sang trang Join Organization và yêu cầu xác thực bằng OTP. 

8\. Hệ thống gửi OTP đến email của user. 

9\. User nhập OTP và xác thực thành công. 

10\. Hệ thống direct user vào trang Dashboard Conative của Organization đó, status của user sẽ chuyển thành **Active** 

11\. Kết thúc Use case 

### **Exceptional flow** 

3a. Email đã tồn tại trong Organization

- Thông báo email đã tồn tại

4a. Link invite hết hạn, Admin gửi lại invite

- Sau khi link invite được gửi đến email của user, sẽ có thời hạn hiệu lực trong vòng 24h

- Sau thời gian đó mà user không bấm vào link để sign in thì sẽ hiển thị thêm CTA **Remind** kế bên status. Admin bấm **Remind** để gửi lại link invite. 

4b. Link invite hết hạn, Admin cancel Invite

- Sau khi link invite được gửi đến email của user, sẽ có thời hạn hiệu lực trong vòng 24h

- Sau thời gian đó mà user không bấm vào link để sign in thì sẽ hiển thị thêm CTA **Cancel Invite**kế bên status. Admin bấm **Cancel Invite** để huỷ lời mời. 

- Hệ thống sẽ hiển thị popup xác nhận, bấm **Yes, cancel** để xác nhận. 

- Hệ thống sẽ xoá user được mời ra khỏi danh sách member trong Organization. 

4c. Invite 1 user cùng lúc vào 2 hoặc nhiều  Organization

- invite email: ["hangnguyen@chidoanh.com](https://devtak.cbidigital.com/%22hangnguyen@chidoanh.com) ở ORG: melinda  
- switch qua org chanluu  
- Chọn invite email: ["hangnguyen@chidoanh.com](https://devtak.cbidigital.com/%22hangnguyen@chidoanh.com)  
- Kết quả:   
+ Vẫn cho phép gửi mail đến user để invite vào organization khác   
*   
+ Khi email Link invite gửi đến thì quay về flow 4a và 4b

**Alternative Flow** 

Email của user chưa tồn tại trong hệ thống (To be updated)

## **1.5 Business rule**

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin của organization đó

**Quy định hiển thị và thao tác**

Email

- Email của user mới phải là một địa chỉ email hợp lệ và chưa được sử dụng bởi user nào khác trong hệ thống.

- Mỗi lần Add member chỉ nhập được 1 email 


Role & Permission

- Role của user mới phải là một trong các role được định nghĩa trước trong hệ thống (Admin, Member)

- Permission của user mới phải phù hợp với role của user đó và không vượt quá permission của admin

Link Invite

- Email thông báo cho user mới có chứa một liên kết để user mới có thể kích hoạt tài khoản của mình.


Status của user 

- Active: User đã thuộc organization

- Pending: Sau khi hệ thống gửi link invite cho đến khi user join organization

OTP xác thực: 

- Hết hạn sau 5 phút


# **UC 2.6 \- Remove a user out of organization** 

## **1.1. Mục tiêu**

Xóa một user khỏi organization và huỷ bỏ quyền truy cập của user đó trong organization

## **1.2. Input** 

Quyền remove user ra khỏi Organization 

## **1.3. Output**

 User được remove ra khỏi organization thành công và không còn quyền truy cập đến các dự án và tài nguyên của organization.

## **1.4. Workflow** 

### **Main flow (Happy case)** 

1\. Ở trang quản lý Organization, hệ thống hiển thị danh sách các user trong hệ thống, bao gồm email, username, role & permission của mỗi user. 

3\. Admin chọn một user muốn remove ra khỏi organization 

4\. Hệ thống hiển thị popup xác nhận để remove user ra khỏi organization

5\. Admin bấm “Remove” 

6\. Hệ thống xoá user ra khỏi organization trong và huỷ bỏ quyền truy cập của user đó vào organization. Hệ thống hiển thị thông báo thành công.

7\. Hệ thống hiển thị lại danh sách các user trong organization với user đã được remove.

8\. Kết thúc use case

## **1.5 Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin của organization đó (Được phép remove Admin khác ra khỏi Organization)

## **1.6 Reference** 

- Wireframe & Design

- API Doc

# **UC 2.7 \- Leave Organization**

## **1.1. Mục tiêu**

Rời khỏi organization và huỷ bỏ quyền truy cập của mình trong organization

## **1.2. Input** 

Là member của Organization 

## **1.3. Output**

User rời khỏi organization thành công và không còn quyền truy cập vào organization.

## **1.4. Workflow** 

### **Main flow (Happy case)** 

1\. Ở trang quản lý Organization, user chọn tính năng "Leave organization".

2\. Hệ thống hiển thị popup để xác nhận để rời khỏi organization, bao gồm tên của organization và một nút "Leave Organization".

3\. User nhấn nút "Leave Organization".

4\. Hệ thống xoá user ra khỏi organization và huỷ bỏ quyền truy cập của user đó vào organization. Hệ thống hiển thị thông báo thành công.

5\. Hệ thống chuyển user đến trang chủ của hệ thống.

6\. Kết thúc use case

### **Exceptional flow**

3a. Nếu user nhấn nút "Cancel", hệ thống huỷ bỏ quá trình mời user và quay lại danh sách các user trong hệ thống. 

3b. Nếu user rời khỏi là admin duy nhất của Organization: 

- Hiển thị popup thông báo không thể leave Organization do là admin duy nhất

## **1.5 Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 

- Chỉ được Leave Organization khi có một admin khác đồng thời trong Organization

## **1.6 Reference** 

- Wireframe & Design: 

- API Doc

# **UC 3.1.1 \- Create Custom report by selecting Report template**

## **Mục tiêu**

User có thể tạo Custom report trên trang Custom report list bằng cách chọn Report template, sau đó save lại các thao tác search, filter trên report template đó

## **Input** 

Select Report template 

## **Output**

Create new custom report 

Rename report 

Notification \- Create custom report successfully / failed

## **Workflow** 

### **Main flow (Happy case)** 

1\. Ở trang **Custom report list**, user chọn \[Create Custom report\] để tạo Custom report mới theo Report template.

2\. User nhập Report name & chọn report template muốn tạo.

3\. Hệ thống direct sang trang report tương ứng, theo default setting mặc định (time range, column, view…)

4\. Hệ thống hiển thị thông báo report tạo thành công. 

5\. Hệ thống cập nhật Report name trên trang report tương ứng.

6\. User có thể vào **Custom report list** đã tạo để xem lại report vừa lưu. 

7\. Kết thúc use case. 

**Exceptional Flow 1 \- Report name hoặc Report template empty** 

2a. User không nhập report name hoặc chưa chọn Report template 

3a. Hệ thống hiển thị thông báo user yêu cầu nhập đầy đủ thông tin. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

4a. Kết thúc use case.

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 


**Quy định hiển thị và thao tác** 

**Default setting của các report template**

\- Là default setting của các report tương ứng 

**Report name** 

\- Maximum characters: 100

\- Sau khi tạo report, Report name sẽ thay thế report template name.

**Button \[Update report\]**

\- Primary

\- Luôn enable 

**Button \[Save as\]**

\- Luôn enable 

**Button \[Delete\]**

\- Luôn enable 

**Button \[Export\]**

\- Luôn enable 

**Button \[Rename\]**

\- Luôn enable 

# **UC 3.1.2 \- Create Custom report on Product Performance** 

## **Mục tiêu**

User có thể tạo Custom report trên trang Product Performance bằng cách save các filter, search & config column trên trang product Performance 

## **Input** 

Search 

Filter 

Config column 

Select time range 

Sort fields 

Save report 

## **Output**

Create new custom report 

Rename report 

Notification \- Create custom report successfully / failed

## **Workflow** 

### **Main flow (Happy case)** 

1\. Ở trang Product Performance, user chọn \[Save as\] để tạo Custom report mới theo Report template **Product Performance** 

2\. Hệ thống hiển thị pop-up **Save custom report** 

3\. User nhập Report name 

4\. User chọn \[Save\] để lưu Custom report 

5\. Hệ thống tạo Custom report theo report Name đã được nhập, hiển thị thông báo lưu report thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

6\. Hệ thống đổi tên report trên UI

7\. User có thể vào **Custom report** để xem lại report vừa lưu. 

8\. Kết thúc use case. 

### **Alternative flow 1 \- Create Custom report by Selecting Report template**

UC 3.1.2 \- Create Custom report by selecting Report template

### **Exceptional flow 1 \- Cancel saving report**

4a. User chọn \[Cancel\] để quay lại report 

5a. Hệ thống tắt popup, quay lại report 

6a. Kết thúc use case

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 


**Quy định hiển thị và thao tác** 

**Report name** 

\- Mặc định hiển thị **report template name** (eg. Product performance, Sales by Category…)

\- Maximum characters: 100

\- Sau khi tạo report, Report name sẽ thay thế report template name.

**Button save as**

\- Luôn enable 

## **Reference** 

- Wireframe & Design: 

- API

# **UC 3.1.3 \- Create Custom report on Dashboard** 

## **Mục tiêu**

User có thể tạo Custom report trên trang Dashboard bằng cách save các filter, search & config column trên trang Dashboard 

## **Input** 

Search 

Filter 

Config column 

Select time range 

Sort fields 

Save report 

## **Output**

Create new custom report 

Rename report 

Notification \- Create custom report successfully / failed

## **Workflow** 

### **Main flow (Happy case)** 

1\. Ở trang Product Performance, user chọn \[Save as\] để tạo Custom report mới theo Report template **Dashboard** 

2\. Hệ thống hiển thị pop-up **Save custom report** 

3\. User nhập Report name 

4\. User chọn \[Save\] để lưu Custom report 

5\. Hệ thống tạo Custom report theo report Name đã được nhập, hiển thị thông báo lưu report thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

6\. Hệ thống đổi tên report trên UI

7\. User có thể vào **Custom report** để xem lại report vừa lưu. 

8\. Kết thúc use case. 

### **Alternative flow 1 \- Create Custom report by Selecting Report template**

UC 3.1.2 \- Create Custom report by selecting Report template

### **Exceptional flow 1 \- Cancel saving report**

4a. User chọn \[Cancel\] để quay lại report 

5a. Hệ thống tắt popup, quay lại report 

6a. Kết thúc use case

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 


**Quy định hiển thị và thao tác** 

**Report name** 

\- Mặc định hiển thị **report template name** (eg. Product performance, Sales by Category…)

\- Cập nhật report name sau khi user lưu Custom report 

**Button save as**

\- Luôn enable 

## **Reference** 

- Wireframe & Design: 

- API

# **UC 3.1.4 \- Create Custom report on Sales by Category** 

## **Mục tiêu**

User có thể tạo Custom report trên trang Sales by Category bằng cách save các filter, search & config column trên trang Sales by Category 

## **Input** 

Search 

Filter 

Config column 

Select time range 

Sort fields 

Save report 

## **Output**

Create new custom report 

Rename report 

Notification \- Create custom report successfully / failed

## **Workflow** 

### **Main flow (Happy case)** 

1\. Ở trang Product Performance, user chọn \[Save as\] để tạo Custom report mới theo Report template **Sales by Category** 

2\. Hệ thống hiển thị pop-up **Save custom report** 

3\. User nhập Report name 

4\. User chọn \[Save\] để lưu Custom report 

5\. Hệ thống tạo Custom report theo report Name đã được nhập, hiển thị thông báo lưu report thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

6\. Hệ thống đổi tên report trên UI

7\. User có thể vào **Custom report** để xem lại report vừa lưu. 

8\. Kết thúc use case. 

### **Alternative flow 1 \- Create Custom report by Selecting Report template**

UC 3.1.2 \- Create Custom report by selecting Report template

### **Exceptional flow 1 \- Cancel saving report**

4a. User chọn \[Cancel\] để quay lại report 

5a. Hệ thống tắt popup, quay lại report 

6a. Kết thúc use case

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 


**Quy định hiển thị và thao tác** 

**Report name** 

\- Mặc định hiển thị **report template name** (eg. Product performance, Sales by Category…)

\- Maximum characters: 100

\- Sau khi tạo report, Report name sẽ thay thế report template name.

**Button save as**

\- Luôn enable 

## **Reference** 

- Wireframe

# **UC 3.1.5 \- Create Custom report on Sales by Collection** 

## **Mục tiêu**

User có thể tạo Custom report trên trang Sales by Collection bằng cách save các filter, search & config column trên trang Sales by Collection 

## **Input** 

Search 

Filter 

Config column 

Select time range 

Sort fields 

Save report 

## **Output**

Create new custom report 

Rename report 

Notification \- Create custom report successfully / failed

## **Workflow** 

### **Main flow (Happy case)** 

1\. Ở trang Product Performance, user chọn \[Save as\] để tạo Custom report mới theo Report template **Sales by Collection** 

2\. Hệ thống hiển thị pop-up **Save custom report** 

3\. User nhập Report name 

4\. User chọn \[Save\] để lưu Custom report 

5\. Hệ thống tạo Custom report theo report Name đã được nhập, hiển thị thông báo lưu report thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

6\. Hệ thống đổi tên report trên UI

7\. User có thể vào **Custom report** để xem lại report vừa lưu. 

8\. Kết thúc use case. 

### **Alternative flow 1 \- Create Custom report by Selecting Report template**

UC 3.1.2 \- Create Custom report by selecting Report template

### **Exceptional flow 1 \- Cancel saving report**

4a. User chọn \[Cancel\] để quay lại report 

5a. Hệ thống tắt popup, quay lại report 

6a. Kết thúc use case

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 


**Quy định hiển thị và thao tác** 

**Report name** 

\- Mặc định hiển thị **report template name** (eg. Product performance, Sales by Collection…)

\- Maximum characters: 100

\- Sau khi tạo report, Report name sẽ thay thế report template name.

**Button save as**

\- Luôn enable 

## **Reference** 

- Wireframe

# **UC 3.2 \- Update Custom report**

# **UC 3.2.1 \- Update report** 

## **Mục tiêu**

User có thể ghi đè Custom report đã tạo với cùng Report name

## **Input** 

Update report 

## **Output**

Update custom report 

Notification \- Update custom report successfully / failed

## **Workflow** 

### **Main flow (Happy case)** 

1\. Ở trang **Custom report**, user chọn 1 Custom report đã được tạo bất kỳ 

2\. Hệ thống direct sang trang report tương ứng

3\. User thao tác chỉnh sửa trên report đó, sau đó chọn \[Update Report\] để update các thay đổi 

4\. Hệ thống ghi đè các update lên report đó, hiển thị thông báo đẫ update report thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case. 

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 

- Là owner (Author) của custom report


**Quy định hiển thị và thao tác** 

**Report name** 

\- Report name của Custom report được cập nhật lần gần nhất 

**Button \[Save report\]**

\- Primary

\- Luôn enable 

**Button \[Save as\]**

\- Luôn enable 

**Button \[Delete\]**

\- Luôn enable 

**Button \[Export\]**

\- Luôn enable 

**Button \[Rename\]**

\- Luôn enable 

# **UC 3.2.2 \- Rename report** 

## **Mục tiêu**

User có thể cập nhật tên cho Custom report đã tạo bằng 2 cách \- trên trang Report hoặc trong Custom report list

## **Input** 

Update report 

## **Output**

Update custom report 

Notification \- Update custom report successfully / failed

## **Workflow** 

### **Main flow (Happy case)** 

1\. Ở trang **Custom report**, user chọn 1 Custom report đã được tạo bất kỳ 

2\. Hệ thống direct sang trang report tương ứng

3\. User chọn \[Rename Report\]

4\. Hệ thống hiển thị popup Rename report, user nhập report name mới cho report 

5\. Hệ thống ghi đè report name mới lên report đó, hiển thị thông báo đã rename report thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case. 

### **Alternative flow 1**

1\. Ở trang **Custom report**, user chọn \[More\] trên 1 Custom report đã được tạo bất kỳ

2\. Hệ thống hiển thị CTA vs icon \[Rename\] / \[Delete\] 

3\. User chọn \[Rename report\] 

4\. Hệ thống hiển thị popup Rename report, user nhập report name mới cho report 

5\. Hệ thống ghi đè report name mới lên report đó, hiển thị thông báo đã rename report thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case. 

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 

- Là owner (Author) của custom report


  

**Quy định hiển thị và thao tác** 

**Button \[Rename\]**

\- Trang report \- Luôn enable 

\- Trang Custom report list \- Drop down

# **UC 3.3.1 \- Manage Permission of Custom report**

## **Mục tiêu**

Owner của Custom report phân quyền khi chia sẻ Custom report của mình tạo cho các user khác trong cùng Organization view.

## **Inpput**

Permission 

## **Output**

User khác không có / có quyền view Custom report được tạo bởi Owner

## **Workflow** 

### **Main flow** 

1\. Trên trang **Custom report list,** owner chọn report bất kỳ, chọn **\[More\] \> \[Share\]** 

2\. Hệ thống hiển thị popup **Share report** 

3\. Ở mục **General Access**, owner chọn dropdown để phân quyền: 

- Set quyền **Private** \> Chọn **\[Only collaborators of the report can access via link\]** và nhập email của user khác nếu muốn share với những user nhất định.   
- Set quyền **Public** \> chọn **\[People in the organization can view\]**

4\. Hệ thống hiển thị thông báo cập nhật permission thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case

### **Exceptional flow 1 \- User không có quyền view Private report** 

1\. User bấm vào link report nhưng không có quyền view report 

2\. Hệ thống direct đến trang báo lỗi không có quyền

3\. Kết thúc use case

## **Business Rule** 

### **Quy định phân quyền**

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 

- Là owner (Author) của custom report

Định nghĩa permission của Custom report

**Private** report

- Report chỉ hiển thị trong **Custom report** list của Owner (Author).  
- User khác trong Organization không có quyền view report.  
- Những user nào trong hệ thống được owner invite sẽ có quyền view report.

**Public report**

- Report hiển thị trong Custom report list của Owner và tất cả các user khác trong Organization.  
- User khác trong Organization có quyền view report, không có quyền Delete report.

### **Quy định hiển thị và thao tác** 

**Default Permission**

- Private

# **deUC 3.3.2 \- Remove Access from Custom report**

## **Mục tiêu**

Owner của Custom report remove access của user đã invite ra khỏi custom report mình đã tạo

## **Input**

Remove access

## **Output**

User bị remove sẽ không có quyền view Custom report được tạo bởi Owner

## **Workflow** 

### **Main flow** 

1\. Trên trang **Custom report list,** owner chọn report bất kỳ, chọn **\[More\] \> \[Share\]** 

2\. Hệ thống hiển thị popup **Share report** 

3\. Ở danh sách Collaboration list, owner chọn **Dropdown permission** \> **\[Remove Access\]** 

3\. Hệ thống remove access của user và hiển thị thông báo remove thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case

## **Business Rule** 

### **Quy định phân quyền**

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 

- Là owner (Author) của custom report

### **Quy định hiển thị và thao tác** 

**Dropdown** 

- Mặc định đóng  
- Đối với user group  
- Không hiển thị dropdown đối với Report owner

# **UC 3.4 \- View Custom report list** 

## **Mục tiêu**

User có thể xem được custom report đã tạo trong List Custom report, và chọn xem từng report.

## **Input**

View report

## **Output**

Report Name

Author: Full name of the user creates report

Created date: dd/mm/yyyy

Updated date: dd/mm/yyyy

Action: View & Delete

## **Workflow** 

1\. Trên sidebar menu, người dùng chọn \[Custom Report\] để vào xem danh sách các custom report đã tạo. Các thông tin 

2\. Người dùng chọn vào report cần xem 

3\. Hệ thống direct user sang trang Custom report tương ứng. 

4\. Kết thúc Use Case 

## **Business Rule**

### **Quy định phân quyền**

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 

- Có quyền view Custom report

### **Quy định hiển thị và thao tác** 

Danh sách report 

\- Mặc định hiển thị các Report template của Conative, bao gồm: 

1. Dashboard   
2. Product Performance   
3. Sales by Category  
4. Sales by Collection  
5. *Inventory Planner (Coming soon)*   
6. *Gap Analysis (Coming soon)*

\- Mặc định sort theo thời gian tạo mới nhất 

\- Thứ tự các field trên danh sách Custom report

| Field | Display | Required? | Description |
| :---- | :---- | :---- | :---- |
| Report Name | Text | Yes |  |
| Author | Text | Yes | Đối với report do user create:  Name \= Author’s full name Đối với report mặc định của Conative Name \= “Conative”  |
| Created on | Date | Yes | Date that user create the report |
| Last updated on | Date | Yes | Date that user update report lately (Lần gần nhất) |
| Action \- View  \- Rename \- Delete | Dropdown  |  |  |

# **UC 3.5 \- Delete report** 

## **Mục tiêu**

User có thể delete cho Custom report đã tạo bằng 2 cách \- trên trang Report hoặc trong Custom report list

## **Input** 

Delete Report

## **Output**

Delete custom report 

Notification thông báo đã delete report 

## **Workflow** 

### **Main flow (Happy case)** 

1\. Trên trang **Custom report list,** owner chọn report bất kỳ, chọn **\[More\] \> \[Delete\]** 

2\. Hệ thống hiển thị popup **xác nhận Delete report**

3\. User chọn 

\- \[**Delete**\] để xác nhận detete

\- \[**Cancel\]** để quay lại trang **Custom report list**

4\. Hệ thống delete report, thông báo delete thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case 

### **Alternative flow** 

1\. Ở trang **Custom report** đã tạo, user chọn **\[More\] \> \[Delete\]** 

2\. Hệ thống hiển thị popup **xác nhận Delete report**

3\. User chọn 

\- \[**Delete**\] để xác nhận delete

\- \[**Cancel\]** để quay lại trang **report**

4\. Hệ thống delete report, thông báo delete thành công. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)** 

5\. Hệ thống redirect về trang Custom report list. 

5\. Kết thúc use case. 

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 

- Là owner (Author) của custom report


**Quy định hiển thị và thao tác** 

# **UC 3.6 \- Search Custom Report**

## **Mục tiêu**

User có thể tìm kiếm những custom report do mình tạo hoặc có quyền view trong custom report list. 

## **Input** 

Custom report name

## **Output**

Custom report list

## **Workflow** 

### **Main flow (Happy case)** 

1\. Trên trang **Custom report list,** user bấm vào thanh Search

2\. Hệ thống đề xuất 5 report được tìm kiếm gần đây nhất

3\. User nhập report name muốn tìm kiếm

4\. Hệ thống trả về các report theo key word tìm kiếm.

\- Có kết quả: trả về danh sách report tương ứng

\- Không có kết quả: trả về trang **no report found**

5\. Kết thúc use case.

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 


**Quy định hiển thị và thao tác** 

**Search rule**

- Tìm kiếm theo Report name: search gần đúng 

**Search bar**

- HIển thị CTA close \[x\] khi user nhập thông tin  
- Dropdown hiển thị suggest 5 report gần nhất

# **UC 3.7 \- Filter Custom Report by Author & Report template**

## **Mục tiêu**

User có thể filter những custom report do mình tạo hoặc có quyền view trong custom report list theo Owner (author) name hoặc Report template

## **Input** 

Author Name 

Report Template

## **Output**

Custom report list

## **Workflow** 

### **Main flow (Happy case)** 

1\. Trên trang **Custom report list,** user bấm vào ít nhất 1 dropdown filter

- Author   
- Report template

2\. Hệ thống hiển thị các kết quả trong dropdown filter

- Author: hiển thị tất cả user trong organization  
- Report template: hiển thị tất cả report template của Conative

3\. User bấm chọn 1 hoặc nhiều filter

4\. Hệ thống trả về các report theo filter tương ứng

\- Có kết quả: trả về danh sách report tương ứng

\- Không có kết quả: trả về trang **no report found**

5\. Kết thúc use case.

### **Alternative Flow 1 \- Clear all filters**

3a. User chọn **Clear all** để clear all filter 

4a. Hệ thống clear filter và trả về các report theo filter tương ứng

\- Có kết quả: trả về danh sách report tương ứng

\- Không có kết quả: trả về trang **no report found**

5\. Kết thúc use case.

## **Business rule** 

**Quy định phân quyền** 

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 


**Quy định hiển thị và thao tác** 

**Author filter** 

- Cho phép chọn nhiều  
- Trả về tất cả user trong Organization, Current user hiển thị trên cùng   
- Hiển thị theo Full name của user 


**Report template filter** 

- Cho phép chọn nhiều  
- Trả về tất cả report template của Conative


# **UC 4.1. Product performance Report**

# **UC 4.1.1 Select View of Product / Variant in Product Performance**

## **1.1. Mục tiêu**

Người dùng chọn View in **All products / All Variants** để xem data trong table **Product Performance** theo Level product hoặc level Variant 

## **1.2. Input** 

## **1.3. Output**

Hiển thị data Product Performance theo level Product hoặc level Variant

 xem data trong table **Product Performance** theo Level product hoặc level Variant 

## **1.4. Workflow** 

### **Main flow**

1\. Trên trang Product Performance / Dashboard, người dùng bấm vào dropdown \[View in **All products / All variants** \]

2\. Bấm chọn View: 

- **All products:** Xem report ở level product 

- **All variants:** Xem report ở level variant 

3\. Kết thúc use case 

### **Alternative flow**

(Thêm flow cho người dùng chọn view khi config column \- Update sau) 

## **Business rule**

1\. Quy định hiển thị

1. Mặc định hiển thị **View in All Products** cho người dùng lần đầu 

2. Hiển thị data theo các field (Column) cho **View in all products / View in all variant**

2\. Thao tác 

1. Đối với **View in All Products,** Bấm vào dropdown: drill down hiển thị data của các variant thuộc product đó tương ứng với các field. 

# **UC 4.1.2 Search Product**

## **Mục tiêu**

Shopify: Người dùng có thể tìm kiếm sản phẩm bằng cách nhập SKU, Product Title, Barcode. 

## **Input**

Truyền vào Barcode / Product title / SKU

## **Output**

Trả dữ liệu theo Use case [**View Dashboard / Product Performance**](#uc-4.1.8-view-dashboard-/-product-performance-table-\(variant-level\))

## **Workflow**

### **Main flow**

1\. Trên trang Product Performance / Dashboard, người dùng bấm vào thanh \[Search\]

2\. Hệ thống đề xuất 5 sản phẩm được tìm kiếm gần đây nhất

3\. Người dùng nhập thông tin để tìm kiếm sản phẩm 

1. Shopify: Người dùng có thể tìm kiếm sản phẩm bằng cách nhập SKU, Title, Barcode. 

4\. Hệ thống trả về dữ liệu sản phẩm theo điều kiện tìm kiếm

1. View Product: Trả về product 

2. View Variant: Trả về variant 

5\. Kết thúc use case 

### **Alternative flow**

3a. Người dùng chọn sản phẩm theo đề xuất của hệ thống 

- Hệ thống trả về dữ liệu sản phẩm theo điều kiện tìm kiếm

1. View Product: Trả về product 

2. View Variant: Trả về variant 

- Kết thúc use case 

### **Exceptional flow**

4a. Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

- Kết thúc use case.

## **Business Rule**

- Tìm kiếm theo Product title: search gần đúng 

- Tìm kiếm theo SKU: search gần đúng 

- Tìm kiếm theo Barcode: search gần đúng 

# **UC 4.1.3. Select time range**

## **Mục tiêu**

Người dùng có thể chọn thời gian mà họ muốn xem dữ liệu của sản phẩm

## **Workflow**

### **Main flow**

1\. Trên trang Product Performance / Dashboard, người dùng bấm vào \[Calendar\]

2\. Hệ thống hiển thị popup để chọn khoảng thời gian

3\. Người dùng chọn khoảng thời gian mong muốn xem dữ liệu bằng cách chọn time range \[Date range\] có sẵn hoặc chọn ngày start date / end date trên lịch 

4\. Người dùng bấm **Apply** để lưu thời gian vừa chọn

5\. Hệ thống trả về dữ liệu theo khung thời gian tương ứng 

6\. Kết thúc use case 

### **Exception flow**

3a. Người dùng chọn khoảng thời gian trong tương lai

- Disable các ngày trong khoảng thời gian đó

5a.  Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

- Kết thúc use case.

## **Business Rule**

1\. Quy định hiển thị

1. Khoảng thời gian mặc định: Last 30 days (30 ngày gần nhất) 

2. Khi người dùng filter theo time range có sẵn của Conative, start date & end date tự động được highlight theo khoảng thời gian tương ứng, và ngược lại. 

2\. Quy định time zone mặc định trên Conative

- Default time zone: UTC \-4 (Eastern Time) 

2\. Quy định về khung thời gian có sẵn trên Conative

Time zone mặc định: 

1. Today

2. Yesterday

3. Last 7 days: 

   1. Starting date: 7 days before (including yesterday)

   2. End date: Yesterday

4. Last 30 days: 

   1. Starting date: 30 days before (including yesterday)

   2. End date: Yesterday

5. This month

6. Last month

7. Last 3 months

8. This year

9. Last year 

10. Week to date: 

    1. Starting date: ngày thứ Hai của tuần gần nhất

    2. End date: Today

11. Year to date:

    1. Starting date: ngày đầu tiên của năm gần nhất (Vd: 2023 \> Starting time là ngày 1/1/2023)

    2. End date: Today

    3. Quarter to date

    4. Starting date: ngày đầu tiên của quý gần nhất (Vd: Q2/2023 \> Starting time là ngày 1/4/2023)

    5. End date: Today

# **UC 4.1.4 Advanced Filter in Product Performance** 

## **1.1. Mục tiêu**

Trên các trang Product Performance, user có thể filter các metrics và lưu lại lại filter thành custom report.

## **1.2. Input** 

Filter (select)

Condition (Operators)

Filter values 

## **1.3. Output**

Có thể filter các metrics và lưu lại filter thành custom report 

## **1.4. Workflow** 

### **Main flow (Happy case)**

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Chọn \[Apply Filter\]

8\. Hệ thống trả về dữ liệu theo điều kiện filter

Alternative Flow 1

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Người dùng xóa bớt value bằng cách tick vào \[x\] bên cạnh value 

8\. Chọn \[Apply Filter\]

9\. Hệ thống trả về dữ liệu theo điều kiện filter

### **Alternative Flow 2**

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Chọn \[Clear All\]

8\. Xóa các filter đã lựa chọn 

### **Exceptional flow 1**

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng không chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Chọn \[Apply Filter\]

4\. Hệ thống thông báo lỗi và yêu cầu user chọn filter.

### **Exceptional Flow 2** 

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]  
2\. Người dùng không chọn filter & điều kiện filter  
3\. Người dùng không tìm kiếm thấy filter value ở field \[Value\]   
4\. Hệ thống trả về thông báo lỗi. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

## **Business Rule (Phase 1):**

Quy định hiển thị và thao tác 

Manage Filter \- Block filter đầu tiên

- Mặc định hiển thị mỗi khi user bật popup filter

- Select Operator: ẩn

Block filter sau đó: 

- Select Operator mặc định “And” 

Search Filters (Operators, Filter, Condition, Value \- Multiple selection)

- Suggest kết quả theo từ khóa search 

Hiển thị List Operators, conditions, value \- multiple selection

- Mặc định hiển thị dropdown khi chọn field

- Số lượng item hiển thị mặc định: 30

- Show more\> hiển thị 30 item kế tiếp

List Advanced filter

[https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit\#gid=1148307543](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=1148307543)

## **Refer45ence** 

Design: [https://zpl.io/z8Gjxl4](https://zpl.io/z8Gjxl4)

API: [**https://devtak.cbidigital.com/projects/conative-analytics-dubrovnik/wiki/advance-filter**](https://devtak.cbidigital.com/projects/conative-analytics-dubrovnik/wiki/advance-filter)

# **UC 4.1.5 Config column  \- Product level**

## **Mục tiêu**

Chọn/ thay đổi metric muốn hiển thị ở sản phẩm, product level

### **Main flow (Happy case)**

1\. Trên trang Product Performance / Dashboard, View all products người dùng bấm \[Config column\]

2\. Người dùng search và chọn metric (chưa hiện có) để thêm vào bảng dữ liệu sản phẩm 

3\. Người dùng chọn \[Modify columns\] 

4\. Hệ thống trả dữ liệu theo column đã chọn 

5\. Kết thúc use case 

### **Alternative Flow 1**

2a. Người dùng chọn \[Select all\] trong \[add column\] để chọn hiển thị tất cả các metric  

### **Alternative Flow 2**

2b. Người dùng kéo thả metric để sắp xếp thứ tự cột trong bảng dữ liệu 

### **Alternative Flow 3**

2c. Người dùng chọn \[Clear all\] trong \[add column\] để xóa các metric đã chọn 

### **Alternative Flow 4**

3a. Người dùng chọn \[Restore default\] 

4\. Hệ thống trả lại dữ liệu mặc định   


**Business rule**

Quy định hiển thị và thao tác 

**Thứ tự hiển thị field mặc định cho user mới:** 

Ann Marie: 

1. Product title   
2. Lot code  
3. Expiration date  
4. Stock   
5. Gross sales  
6. % of Revenue  
7. Gross quantity   
8. Return quantity   
9. Return rate   
10. Total sales  
11. Price   
12. Day on site   
13. Sales per day (ATS)  
14. Sales per day (In stock)  
15. Sales per day (out of stock)  
16. Sales day left  
17. Sell through  
18. On order   
19. Total inventory value  
20. Trend   
21. Next 90-day sales (AI)  
22. 90-day sales (Rule-based)  
23. Reorder quantity (AI)

**Other brands:** 

1. Product title  
2. Gross sales  
3. % of Revenue  
4. Gross quantity   
5. Return value  
6. Return quantity   
7. Return rate   
8. Total sales  
9. Price   
10. Product view  
11. Conversion rate  
12. Ad spend  
13. Ad clicks  
14. Day on site  
15. Sales per day (ATS)  
16. Sales per day (In stock)  
17. Sales per day (out of stock)  
18. Sales day left (ATS)  
19. Sell through  
20. Stock  
21. On order   
22. ATS  
23. Total inventory value  
24. Trend   
25. Next 90-day sales (AI)  
26. 90-day sales (Rule-based)  
27. Reorder quantity (AI)  
28. Replenishable 

**Các field (Column) được config**

| STT | Field  | Business rules for Config column |
| :---- | :---- | :---- |
| 1 | Product title | **Rule** Mặc định hiển thị ở đầu table  Không được remove hay thay đổi vị trí (Không có CTA \[x\] & icon kéo thả) |
| 2 | Gross sales | **Rule** Có thể thay đổi vị trí Có thể remove |
| 3 | Gross quantity  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 4 | Return value | **Rule** Có thể thay đổi vị trí Có thể remove |
| 5 | Return quantity | **Rule** Có thể thay đổi vị trí Có thể remove |
| 6 | Return rate | **Rule** Có thể thay đổi vị trí Có thể remove |
| 7 | Total sales | **Rule** Có thể thay đổi vị trí Có thể remove |
| 8 | Price | **Rule** Có thể thay đổi vị trí Có thể remove |
| 9 | Product views | **Rule** Có thể thay đổi vị trí Có thể remove |
| 10 | Ad clicks | **Rule** Có thể thay đổi vị trí Có thể remove |
| 11 | Ad spend | **Rule** Có thể thay đổi vị trí Có thể remove |
| 12 | % of revenue | **Rule** Có thể thay đổi vị trí Có thể remove |
| 13 | Conversion rate | **Rule** Có thể thay đổi vị trí Có thể remove |
| 14 | Day on site | **Rule** Có thể thay đổi vị trí Có thể remove |
| 15 | Sales per day | **Rule** Có thể thay đổi vị trí Có thể remove |
| 16 | Sales day left | **Rule** Có thể thay đổi vị trí Có thể remove |
| 17 | Sell through | **Rule** Có thể thay đổi vị trí Có thể remove |
| 18 | Lot code | **Rule** Có thể thay đổi vị trí Có thể remove |
| 19 | Expiration date | **Rule** Có thể thay đổi vị trí Có thể remove |
| 20 | Stock | **Rule** Có thể thay đổi vị trí Có thể remove |
| 21 | On order | **Rule** Có thể thay đổi vị trí Có thể remove |
| 22 | ATS | **Rule** Có thể thay đổi vị trí Có thể remove |
| 23 | Total inventory value | **Rule** Có thể thay đổi vị trí Có thể remove |
| 24 | Trend | **Rule** Có thể thay đổi vị trí Có thể remove |
| 25 | Next 90-day sales (AI) | **Rule** Có thể thay đổi vị trí Có thể remove |
| 26 | Last 90-day sales (Rule based)  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 27 | Reorder quantity (AI) | **Rule** Có thể thay đổi vị trí Có thể remove |
| 28 | Replenishable | **Rule** Có thể thay đổi vị trí Có thể remove |
| 29 | Product status  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 30 | Gross margin | **Rule** Có thể thay đổi vị trí Có thể remove |
| 31 | Gross profit | **Rule** Có thể thay đổi vị trí Có thể remove |
| 32 | Product id | **Rule** Có thể thay đổi vị trí Có thể remove |
| 33 | Category | **Rule** Có thể thay đổi vị trí Có thể remove |
| 34 | Days until stock out | **Rule** Có thể thay đổi vị trí Có thể remove |
| 35 | Net sales | **Rule** Có thể thay đổi vị trí Có thể remove |
| 36 | Net quantity | **Rule** Có thể thay đổi vị trí Có thể remove |
| 37 | Tax | **Rule** Có thể thay đổi vị trí Có thể remove |
| 38 | Discount value | **Rule** Có thể thay đổi vị trí Có thể remove |
| 39 | ROP | **Rule** Có thể thay đổi vị trí Có thể remove |
| 40 | Channel | **Rule** Có thể thay đổi vị trí Có thể remove |
| 41 | Compare-at-price | **Rule** Có thể thay đổi vị trí Có thể remove |
| 42 | Cost | **Rule** Có thể thay đổi vị trí Có thể remove |

1. Người dùng click \[Clear all\], hệ thống xóa tất cả metric đã chọn nhưng giữ lại \[Product title\] 

2. Khi số lượng metric được chọn nhỏ hơn tổng metric, enable \[Select all\], \[Clear all\]

3. Khi tất cả các metric đều được chọn (số lượng metric được chọn bằng tổng metric), Enable \[Clear all\], disable\[Select all\] 

4. Khi không có metric nào được chọn (số lượng metric được chọn bằng 0), enable\[Select all\], disable\[Clear all

# **UC 4.1.6 Config column  \- Variant level**

## **Mục tiêu**

Chọn/ thay đổi metric muốn hiển thị ở sản phẩm, variant level

### **Main flow (Happy case)**

1\. Trên trang Product Performance / Dashboard, View all variant người dùng chọn **\[Config column\]**

2\. Người dùng search và chọn metric (chưa hiện có) để thêm vào bảng dữ liệu sản phẩm 

3\. Người dùng chọn \[Modify columns\] 

4\. Hệ thống trả dữ liệu theo column đã chọn 

5\. Kết thúc use case 

### **Alternative Flow 1**

2a. Người dùng chọn \[Select all\] trong \[add column\] để chọn hiển thị tất cả các metric  

### **Alternative Flow 2**

2b. Người dùng kéo thả metric để sắp xếp thứ tự cột trong bảng dữ liệu 

### **Alternative Flow 3**

2c. Người dùng chọn \[Clear all\] trong \[add column\] để xóa các metric đã chọn 

### **Alternative Flow 4**

3a. Người dùng chọn \[Restore default\] 

4\. Hệ thống trả lại dữ liệu mặc định     

## **Business rule**

Quy định hiển thị và thao tác 

**Thứ tự hiển thị field mặc định cho user mới:** 

1. Product title  
2. SKU  
3. Gross sales  
4. % Revenue  
5. Gross quantity  
6. Return value  
7. Return quantity  
8. Return rate   
9. Total sales  
10. Price  
11. Product view  
12. Conversion rate  
13. Day on site  
14. Sales per day (ATS)  
15. Sales per day (In stock)  
16. Sales per day (Out of stock)  
17. Sales days left (ATS)  
18. Sell through  
19. Stock  
20. On order  
21. ATS  
22. Total Inventory Value  
23. Trend  
24. Next 90-day sales (AI)  
25. 90-days Sales (Rule-based)  
26. Reorder quantity (AI)  
27. Replenishable  
28. Product status

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Product title | **Rule** Mặc định hiển thị ở đầu table  Không được remove hay thay đổi vị trí (Không có CTA \[x\] & icon kéo thả) |
| 2 | SKU |  |
| 3 | Gross sales |  |
| 4 | % of revenue |  |
| 5 | Gross quantity |  |
| 6 | Return value |  |
| 7 | Return quantity |  |
| 8 | Total sales |  |
| 9 | Price  |  |
| 10 | Product views |  |
| 11 | Conversion Rate |  |
| 12 | Day on site |  |
| 13 | Sales per day |  |
| 14 | Sales day left |  |
| 15 | Sell through |  |
| 16 | Stock  |  |
| 17 | On order |  |
| 18 | ATS |  |
| 19 | Total inventory value |  |
| 20 | Trend |  |
| 21 | Next 90-Day Sales (AI) |  |
| 22 | Last 90-Day Sales |  |
| 23 | Reorder Quantity (AI) |  |
| 24 | Replenishable |  |
| 25 | Product Status |  |

1. Người dùng click \[Clear all\], hệ thống xóa tất cả metric đã chọn nhưng giữ lại \[Product title\] 

2. Khi số lượng metric được chọn nhỏ hơn tổng metric, enable \[Select all\], \[Clear all\]

3. Khi tất cả các metric đều được chọn (số lượng metric được chọn bằng tổng metric), Enable \[Clear all\], disable\[Select all\] 

4. Khi không có metric nào được chọn (số lượng metric được chọn bằng 0), enable\[Select all\], disable\[Clear all\]

# **UC 4.1.7 View Dashboard /  Product performance table (Product level)**

## **Mục tiêu**

Hiển thị danh sách các metric của Product level cho các product theo input

## **Input**

- Search  
- Filter  
- Select time range  
- Channel settings  
- Config column 

## **Output**

- Trả về danh sách field của Product level


| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | Product title | Product Title as listed in ecommerce platform | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 2 | Gross sales | Total sales recorded prior to sales discounts and sales returns | **Calculation  Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 3 | Gross quantity  | Total units recorded prior to sales discounts and sales returns | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 4 | Return value | The value of product returned  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 5 | Return quantity | The total unit quantity of product returned  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 6 | Return rate |  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 7 | Total sales | Value of Net Sales Plus Shipping Income and Taxes | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 8 | Price | Price as listed in ecommerce platform | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 9 | Product views | The number of customers viewing specific product information. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 10 | Ad clicks | The total number of clicks on ads in Google and Facebook ad channels. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 11 | Ad spend  | Total sum of media spend on Google and Facebook ad channels. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 12 | % of revenue | Contribution percentage of overall revenue from this product  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 13 | Conversion rate |  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 14 | Day on site | Total number of days product has been live on your website | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 15 | Sales per day | The average number of products sold in a day. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 16 | Sales day left (ATS) | The amount of days the current stock of an item will last based on current sales per day. Calculated by ATS divided by Sales Per Day | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Sales days left (Stock) | Predicted days until stock reaches zero | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description Ở trang dashboard  sẽ show  Level product |
| 17 | Sales per day (In stock) | The average number of products sold in a day. (accounting only for days when the product is in stock) | **Calculation** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27) **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description  |
| 18 | Sales per day (Out of stock) | The average number of products sold in a day. (accounting only for days when the product is out of stock) | **Calculation**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27)  **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 19 | Sell through | Percentage of overall proudcts sold to total overall inventory quantity of any given product.   | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 20 | Lot code |  | **Display:**  Chỉ hiển thị với Industry Cosmetic (Vd: brand Ann marie) Chỉ hiển thị đối với variant khi user chọn dropdown hiển thị list variant của product Nếu product chỉ có 1 lot code và lot code đó có stock \= 0 \> hiển thị (-) khi expand dropdown  **Default Column**  Yes (Vị trí default column xem ở UC 4.1.5 Config column \- Product level)  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 21 | Expiration date |  | **Display:**  Chỉ hiển thị với Industry Cosmetic (Vd: brand Ann marie) Chỉ hiển thị đối với variant khi user chọn dropdown hiển thị list variant của product  **Default Column**  Yes (Vị trí default column xem ở UC 4.1.5 Config column \- Product level) **Sort** Mặc định sort theo ngày gần nhất đến ngày xa nhất khi user expand product  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 22 | Stock | Total quantity of product received in inventory. | **Display Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 23 | On order | The number of products ordered with the supplier but not yet received. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 24 | ATS | The total quantity of product available to sell, this the sum of all product inventory in Stock and On Order. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 25 | Total inventory value | Total value of all in Stock inventory. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 26 | Trend |  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 27 | Next 90-day sales (AI) | Sales forecast for the next 90 days | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 28 | Last 90-day sales (Rule based)  | Total sales quantity in the previous 90 days | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 29 | Reorder quantity (AI) | Conative AI-powered suggested quantity to reorder, by deducting Sales Forecast by ATS | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 30 | Replenishable | The status whether or not an item is going to be reproduced in the future | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 31 | Product status  | Product status on Shopify (Active, Disabled, Draft) | **Default Column**  Yes  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description   |
| 32 | Gross margin | Net Revenue minus Cost of Goods Sold | **Calculation**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Gross profit | Net Revenue minus Cost of Goods Sold and Operating Expenses. | **Calculation**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 33 | Product id | Unique Product Identifier from ecommerce platform | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 34 | Bar code |  | Trả về null (-) do barcode ở variant level **Default Column**  No  **Sort** Theo A-Z và ngược lại  |
|  | Category |  | **Default Column**  No  **Sort** Theo A-Z và ngược lại |
| 35 | Days until stock out | Predicted days until stock reaches zero | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 36 | Default image |  | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 37 | Net sales | Gross Sales of minus the value of Returns and Discounts. | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 38 | Net quantity |  | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 39 | Tax | The total amount of taxes based on each product | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 40 | Discount value | Deduction from the usual cost of the product | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 41 | ROP | The minimum level of inventory needed to cover the Lead Time | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 42 | Channel | Name of channel used by marketing or sales | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 43 | Action |  |  |
| 44 | Compare-at-price | The comparison of the original price and the sale price. | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Cost |  | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Chưa có content |
|  | Received Quantity |  | Unit & Formula: Tham chiếu Conative \-Feature checklist [Link](https://docs.google.com/spreadsheets/u/0/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit) Description tooltip: Luôn enable Config column: Luôn enable Default column: [Link](https://docs.google.com/spreadsheets/d/10hPub5Zb1vJD1IKCE7cOu6vdkQge7b0n/edit#gid=1488753815) Sort: Luôn enable (Default) Theo cao đến thấp Filter: Single & numeric Export: Luôn enable Compare: Disable API interface property field: received\_qty\_percent  |
|  | Received Quantity (%) |  | Unit & Formula: Tham chiếu Conative \-Feature checklist  [Link](https://docs.google.com/spreadsheets/u/0/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit) Description tooltip: Luôn enable Config column: Luôn enable Default column: [Link](https://docs.google.com/spreadsheets/d/10hPub5Zb1vJD1IKCE7cOu6vdkQge7b0n/edit#gid=1488753815) Sort: Luôn enable (Default) Theo cao đến thấp Filter: Single & numeric Export: Luôn enable Compare: Disable API interface property field: received\_qty\_percent  |
|  | Ordered Quantity |  | Unit & Formula: Tham chiếu Conative \-Feature checklist[Link](https://docs.google.com/spreadsheets/u/0/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit) Description tooltip: Luôn enable Config column: Luôn enable Default column: [Link](https://docs.google.com/spreadsheets/d/10hPub5Zb1vJD1IKCE7cOu6vdkQge7b0n/edit#gid=1488753815) Sort: Luôn enable (Default) Theo cao đến thấp Filter: Single & numeric Export: Luôn enable Compare: Disable API interface property field: ordered\_qty |
|  | Ordered Quantity (%) |  | Unit & Formula: Tham chiếu Conative \-Feature checklist[Link](https://docs.google.com/spreadsheets/u/0/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit) Description tooltip: Luôn enable Config column: Luôn enable Default column: [Link](https://docs.google.com/spreadsheets/d/10hPub5Zb1vJD1IKCE7cOu6vdkQge7b0n/edit#gid=1488753815) Sort: Luôn enable (Default) Theo cao đến thấp Filter: Single & numeric Export: Luôn enable Compare: Disable API interface property field: ordered\_qty |

## **Business rule**

**Quy định hiển thị và thao tác** 

- Header: 

  - Không xuống dòng 

  - Đối với field có value dạng chữ (text) thì canh lề trái 

  - Đối với field có value dạng số (number) thì canh lề phải 

- Column

  - Freeze Column Product title và Column Position (khi filter collection) khi user scroll ngang   
- Hiển thị field position của product và freeze ở ngoài cùng bên trái khi filter Collection  
- Hiển thị tooltip mô tả của từng field khi hover vào header của của field đó  
- Hiển thị hình ảnh của sản phẩm khi hover vào **product title**

# **UC 4.1.8 View Dashboard /  Product performance table (Variant level)** {#uc-4.1.8-view-dashboard-/-product-performance-table-(variant-level)}

## **Mục tiêu**

Hiển thị danh sách các metric của Variant level cho các product theo input

## **Input**

- Search  
- Filter  
- Select time range  
- Channel settings  
- Config column 

## **Output**

- Trả về danh sách field của Variant level


| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | Product title | Product Title as listed in ecommerce platform | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 2 | Color  |  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 3 | Gross sales | Total sales recorded prior to sales discounts and sales returns | **Calculation  Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 4 | Gross quantity  | Total units recorded prior to sales discounts and sales returns | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 5 | Return value | The value of product returned  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 6 | Return quantity | The total unit quantity of product returned  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 7 | Return rate |  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 7 | Total sales | Value of Net Sales Plus Shipping Income and Taxes | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 8 | Price | Price as listed in ecommerce platform | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 9 | Product views | The number of customers viewing specific product information. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 10 | Ad clicks | The total number of clicks on ads in Google and Facebook ad channels. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 11 | Ad spend  | Total sum of media spend on Google and Facebook ad channels. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 12 | % of revenue | Contribution percentage of overall revenue from this product  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 13 | Conversion rate |  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 14 | Day on site | Total number of days product has been live on your website | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 15 | Sales per day | The average number of products sold in a day. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 16 | Sales day left (ATS) | The amount of days the current stock of an item will last based on current sales per day. Calculated by ATS divided by Sales Per Day | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 17 | Sell through | Percentage of overall products sold to total overall inventory quantity of any given product.   | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 18 | Lot code |  | **Display:**  Chỉ hiển thị với Industry Cosmetic (Vd: brand Ann marie) Chỉ hiển thị đối với variant khi user chọn dropdown hiển thị list variant của product  **Default Column**  Yes (Vị trí default column xem ở UC 4.1.5 Config column \- Product level)  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 19 | Expiration date |  | **Display:**  Chỉ hiển thị với Industry Cosmetic (Vd: brand Ann marie) Chỉ hiển thị đối với variant khi user chọn dropdown hiển thị list variant của product  **Default Column**  Yes (Vị trí default column xem ở UC 4.1.5 Config column \- Product level) **Sort** Mặc định sort theo ngày gần nhất đến ngày xa nhất khi user expand product  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 20 | Stock | Total quantity of product received in inventory. | **Display Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 21 | On order | The number of products ordered with the supplier but not yet received. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 22 | ATS | The total quantity of product available to sell, this the sum of all product inventory in Stock and On Order. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 23 | Total inventory value | Total value of all in Stock inventory. | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 24 | Trend |  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 25 | Next 90-day sales (AI) | Sales forecast for the next 90 days | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 26 | Last 90-day sales (Rule based)  | Total sales quantity in the previous 90 days | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 27 | Reorder quantity (AI) | Conative AI-powered suggested quantity to reorder, by deducting Sales Forecast by ATS | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 28 | Replenishable | The status whether or not an item is going to be reproduced in the future | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 29 | Product status  | Product status on Shopify (Active, Disabled, Draft) | **Default Column**  Yes  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description   |
| 30 | Gross margin | Net Revenue minus Cost of Goods Sold | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 31 | Gross profit | Net Revenue minus Cost of Goods Sold and Operating Expenses. | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 32 | Product id | Unique Product Identifier from ecommerce platform | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Variant id | Unique VariantIdentifier from ecommerce platform | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Bar code |  | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Color |  | **Default Column**  Yes  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 33 | Category |  | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 34 | Days until stock out | Predicted days until stock reaches zero | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Next arrival date |  | **Rule**  The arrival date of nearest PO that include the item  **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 35 | Net sales | Gross Sales of minus the value of Returns and Discounts. | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 36 | Net quantity |  | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 37 | Tax | The total amount of taxes based on each product | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 38 | Discount value | Deduction from the usual cost of the product | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 39 | ROP | The minimum level of inventory needed to cover the Lead Time | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 40 | Channel | Name of channel used by marketing or sales | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 41 | Sales per day (In stock) | The average number of products sold in a day. (accounting only for days when the product is in stock) | **Calculation** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27) **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description  |
| 42  | Sales per day (Out of stock) | The average number of products sold in a day. (accounting only for days when the product is out of stock) | **Calculation**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27)  **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 43 | Action |  |  |
| 44 | Compare-at-price | The comparison of the original price and the sale price. | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 45 | Cost |  | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Chưa có content |

## 

## **Business rule**

1a. Quy định hiển thị và thao tác 

- Header: 

  - Không xuống dòng 

  - Đối với field có value dạng chữ (text) thì canh lề trái 

  - Đối với field có value dạng số (number) thì canh lề phải 

- Column

  - Freeze Column Product title và Column Position (khi filter collection) khi user scroll ngang   
- Hiển thị tooltip mô tả của từng field khi hover vào header của của field đó  
- Hiển thị hình ảnh của sản phẩm khi hover vào **product title**   
- Hiển thị field position của product và freeze ở ngoài cùng bên trái khi filter Collection  
- Hiển thị mặc định với người dùng mới hoặc với người dùng chọn **Restore default** gồm các field và thứ tự như sau: 

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Product title |  |
| 2 | SKU |  |
| 3 | Gross sales |  |
| 4 | % of revenue |  |
| 5 | Gross quantity |  |
| 6 | Return value |  |
| 7 | Return quantity |  |
| 8 | Total sales |  |
| 9 | Price  |  |
| 10 | Product views |  |
| 11 | Conversion Rate |  |
| 12 | Day on site |  |
| 13 | Sales per day |  |
| 14 | Sales day left |  |
| 15 | Sell through |  |
| 16 | Stock  |  |
| 17 | On order |  |
| 18 | ATS |  |
| 19 | Total inventory value |  |
| 20 | Trend |  |
| 21 | Next 90-Day Sales (AI) |  |
| 22 | Last 90-Day Sales |  |
| 23 | Reorder Quantity (AI) |  |
| 24 | Replenishable |  |
| 25 | Product Status |  |

# **UC 4.1.8\_new View Dashboard /  Product performance table (Color level)**

Link docs:  [https://docs.google.com/document/d/1SP6EGEHcSR4woTEewJmH2VEmsJz96BeQz3xgNF63mHc/edit](https://docs.google.com/document/d/1SP6EGEHcSR4woTEewJmH2VEmsJz96BeQz3xgNF63mHc/edit)

# **UC 4.1.9 View Product Detail Page (Product level)**

## **Mục tiêu**

Người dùng có thể xem được thông tin sản phẩm trong trang PDP

## **Input**

Chọn một sản phẩm bất kỳ trên trang Product Performance 

## **Output**

Hiển thị các thông tin về sản phẩm 

View: Product Level

Dimension / Metadata

Bar chart **Monthly product sales**

| Field name | Product / Variant level | Description |
| :---- | :---- | :---- |
| **Calendar (Time range)** | Both |  |
| **Product title** | both |  |
| **Product ID** | Both |  |
| **SKU** | **Variant level** |  |
| **Category** | Both |  |
| **Variant ID** | Both |  |
| **Barcode** | Both |  |
| **Image thumbnail** | Both |  |
| **Product status** | Both |  |
| **Price** | Variant level |  |
| **Replenishable** | Both |  |
| **Collection list** | Both |  |

Metrics

| Field name | Show value as |
| :---- | :---- |
| Gross sales | Percentage of overall total |
| Gross quantity |  |
| Net sales |  |
| Net quantity |  |
| Return value |  |
| Return quantity |  |
| Total sales |  |
| Return quantity |  |
| Sell through |  |
| Tax |  |
| Discount |  |
| Ad spend |  |
| Ad click |  |
| Product views |  |
| Sales per day |  |
| Sales day left |  |
| Stock |  |
| On order |  |
| ATS |  |
| ROP |  |
| Next 90-day Sales (AI) |  |

## **Workflow**

### **Main flow**

1\. Trên trang product performance, người dùng bấm vào tên sản phẩm bất kỳ để vào trang Product detail. 

2\. Hệ thống hiển thị popup PDP

3\. Người dùng chọn khoảng thời gian mong muốn xem dữ liệu bằng cách chọn time range \[Date range\] có sẵn hoặc chọn ngày start date / end date trên lịch 

4\. Người dùng bấm **Apply** để lưu thời gian vừa chọn

5\. Hệ thống trả về dữ liệu theo khung thời gian tương ứng

6\. Người dùng chọn toggle \[Replenishable\] để đánh dấu sản phẩm này có được tiếp tục Replenish hay không

7\. Hệ thống lưu lại thao tác Replenishable 

8\. Người dùng xem bar chart **Monthly Product Sales,** hover vào cột nào thì cột đó hiện dữ liệu Gross quantity và forecast quantity 

9\. Người dùng chọn ‘\[Export\] để xuất dữ liệu sản phẩm trên ra file CSV theo format sau. 

10\. Hệ thống export dữ liệu và thông báo export thành công 

10\. Người dùng chọn \[Back\] / \[x\] để đóng pop up. 

11\. Kết thúc use case 

### **Alternative flow**

9a. Người dùng chọn \[View variant level\] 

10a. Hệ thống trả về dữ liệu của variant (Use case 4.5.2)

10b. Kết thúc use case 

### **Exceptional flow**

## **Business Rule**

**Quy định hiển thị và thao tác** 

**Calendar (Time frame)**

- Mặc định hiển thị thời gian đã chọn bên ngoài trang Product listing 

- Cho phép chỉnh sửa. (Thao tác tương tự UC 4.4)

**Collection list:** 

- Hiển thị các collection mà product này thuộc về

**Compared:** 

- Hiện tại ẩn chức năng Compare trên UI (Chưa làm ở hệ thống mới)

Các field data dimension \- metrics

- Mặc định hiển thị \[-\] nếu không có dữ liệu 

Replenishable 

- Mặc định hiển thị **On**

- Khi người dùng chọn toggle **On / Off** thì hệ thống sẽ thông báo “Successful Update”

**Bar chart Monthly Product Sales (Product)**

- **Tooltip:**   
  - Hiển thị khi user hover vào chart của từng tháng   
  - Content:   
    - Month, yy (Ví dụ: Sep, 23\)  
    - Forecast: \<sales forecast\>  
    - Gross quantity: \<gross quantity\>  
- **X-axis (Trục hoành):** Hiển thị 12 tháng trong quá khứ, tháng hiện tại, 6 tháng tương lai*. (Ví dụ. Tháng hiện tại là tháng 9/2023, trục x sẽ hiển thị khoảng thời gian từ tháng 9/2022 \- 9/2023 \- 3/2024)*  
- **Y-axis (Trục tung):** Hiển thị giá trị quantity sold. Min value \= 0, Range \= 500 (Ví dụ: 0, 500, 1000, 1500,...)  
  - Tháng trong quá khứ: Hiển thị actual gross quantity theo từng tháng  
  - Tháng hiện tại: Hiển thị actual gross quantity & sales forecast của tháng hiện tại   
  - Tháng trong tương lai: Hiển thị sales forecast theo từng tháng  
- **Chart:**   
  - Highlight chart khi user hover   
  - Hiển thị legend (sales per month) trên mỗi chart

Export

- Khi người dùng export thì có thông báo export thành công.

# **UC 4.1.10 View Product Detail Page (Variant level)**

## **Mục tiêu**

Người dùng có thể xem được thông tin variant trong trang PDP

## **Input**

Chọn một variant bất kỳ trên trang Product Performance 

Chọn một sản phẩm bất kỳ trên trang Product performance, sau đó vào PDP chọn \[View Variant level\]

## **Output**

Hiển thị các thông tin về sản phẩm 

View: Variant Level

Dimension / Metadata

| Field name | Description |
| :---- | :---- |
| **Calendar (Time range)** |  |
| **Product title** |  |
| **Product ID** |  |
| **SKU** |  |
| **Category** |  |
| **Variant ID** |  |
| **Barcode** |  |
| **Image thumbnail** |  |
| **Product status** |  |
| **Price** |  |
| **Replenishable** |  |
| **Collection list** |  |

Metrics

| Field name | Show value as |
| :---- | :---- |
| Gross sales | Percentage of overall total |
| Gross quantity |  |
| Net sales |  |
| Net quantity |  |
| Return value |  |
| Return quantity |  |
| Total sales |  |
| Return quantity |  |
| Sell through |  |
| Tax |  |
| Discount |  |
| Ad spend |  |
| Ad click |  |
| Product views |  |
| Sales per day |  |
| Sales day left |  |
| Stock |  |
| On order |  |
| ATS |  |
| ROP |  |
| Next 90-day Sales (AI) |  |

## **Workflow**

### **Main flow**

1\. Trên trang product performance, người dùng bấm vào tên variant bất kỳ để vào trang Product detail. 

2\. Hệ thống hiển thị popup PDP của variant theo business rule bên dưới

3\. Người dùng chọn khoảng thời gian mong muốn xem dữ liệu bằng cách chọn time range \[Date range\] có sẵn hoặc chọn ngày start date / end date trên lịch 

4\. Người dùng bấm **Apply** để lưu thời gian vừa chọn

5\. Hệ thống trả về dữ liệu theo khung thời gian tương ứng

6\. Người dùng chọn variant trong list dropdown mà người dùng muốn xem dữ liệu

7\. Người dùng chọn toggle \[Replenishable\] để đánh dấu sản phẩm này có được tiếp tục Replenish hay không

8\. Hệ thống lưu lại thao tác Replenishable 

9\. Người dùng xem bar chart **Monthly Product Sales,** hover vào cột nào thì cột đó hiện dữ liệu Gross quantity và forecast quantity 

10\. Người dùng chọn ‘\[Export\] để xuất dữ liệu sản phẩm trên ra file CSV theo format sau. 

11\. Hệ thống export dữ liệu và thông báo export thành công 

12\. Người dùng chọn \[Back\] / \[x\] để đóng pop up. 

13\. Kết thúc use case 

### **Alternative flow**

1a. Người dùng chọn xem PDP của Product, sau đó chuyển qua \[View variant level\] 

2\. Tiếp tục bước 2 như ở main flow

### **Exceptional flow**

## **Business Rule**

**Quy định hiển thị và thao tác** 

Hiển thị Variant 

- Đối với các variant có nhiều status, ưu tiên hiển thị variant có status Active

- Đối với các variant có status active & có sales trong time range đó, mặc định hiển thị variant có **gross sales cao nhất** 

- Đối với các variant có status Active và không có sales, mặc định hiển thị lấy theo thứ tự của Shopify

Calendar (Time frame)

- Mặc định hiển thị thời gian đã chọn bên ngoài trang Product listing 

- Cho phép chỉnh sửa. (Thao tác tương tự UC 4.4)

Collection list: 

- Hiển thị các collection mà variant này thuộc về

Compared: 

- Hiện tại ẩn chức năng Compare trên UI (Chưa làm ở hệ thống mới)

Các field data dimension \- metrics

- Mặc định hiển thị \[-\] nếu không có dữ liệu 

Replenishable 

- Mặc định hiển thị **On**

- Khi người dùng chọn toggle **On / Off** thì hệ thống sẽ thông báo “Successful Update”

**Bar chart Monthly Product Sales (Variant)**

- **Tooltip:**   
  - Hiển thị khi user hover vào chart của từng tháng   
  - Content:   
    - Month, yy (Ví dụ: Sep, 23\)  
    - Forecast: \<sales forecast\>  
    - Gross quantity: \<gross quantity\>  
- **X-axis (Trục hoành):** Hiển thị 12 tháng trong quá khứ, tháng hiện tại, 6 tháng tương lai*. (Ví dụ. Tháng hiện tại là tháng 9/2023, trục x sẽ hiển thị khoảng thời gian từ tháng 9/2022 \- 9/2023 \- 3/2024)*  
- **Y-axis (Trục tung):** Hiển thị giá trị quantity sold. Min value \= 0, Range \= 500 (Ví dụ: 0, 500, 1000, 1500,...)  
  - Tháng trong quá khứ: Hiển thị actual gross quantity theo từng tháng  
  - Tháng hiện tại: Hiển thị actual gross quantity & sales forecast của tháng hiện tại   
  - Tháng trong tương lai: Hiển thị sales forecast theo từng tháng  
- **Chart:**   
  - Highlight chart khi user hover   
  - Hiển thị legend (sales per month) trên mỗi chart

Export

- Khi người dùng export thì có thông báo export thành công.

# 

# **UC 4.1.11 Export product list, variant list và product detail**

## **Mục tiêu**

Người dùng có thể export dữ liệu của danh sách product, variant hoặc một product / variant cụ thể với các field và thứ tự đã được config trên trang Product Performance

## **Input**

## **Output**

Export file CSV 

## **Workflow** 

Mainflow 

1. Trên trang Dashboard / Product Performance, user chọn \[Export\]

2. Hệ thống export file theo yêu cầu và thông báo Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

## **Business Rule** 

Format file CSV khi export list of product / variant 

- File Name

  -  \<Product Performance \- Products Month dd \- Month dd, yyyy\> (Eg: Product Performance \- Products Jul 01 \- Jul 31, 2023\)

  -  \<Product Performance \- Variants Month dd \- Month dd, yyyy\> (Eg: Product Performance \- Variants Jul 01 \- Jul 31, 2023\)

- Dữ liệu (Các row & column) được export và format file CSV dựa theo kết quả dữ liệu trả về khi người dùng thực hiện các use case trên PRoduct performance ví dụ Select View, Sêlect Time range, Search product, Filter product, Sort product, Config Column

Format file CSV khi export product, Variant ở trang PDP

- File Name

  -  \<Product Performance \- Products Month dd \- Month dd, yyyy\> (Eg: Product Performance \- Products Jul 01 \- Jul 31, 2023\)

  -  \<Product Performance \- Variants Month dd \- Month dd, yyyy\> (Eg: Product Performance \- Variants Jul 01 \- Jul 31, 2023\)

- Dữ liệu (Các row & column) được export sẽ bao gồm các tất cả các field dữ liệu của product đó và dựa theo kết quả dữ liệu trả về khi người dùng filter time range trong PDP. 

- Format file dữ liệu bao gồm 3 sheet: 

  - Product metrics (Tương tự format file CSV Product performance)

  - ~~List of Collection: Liệt kê các collection mà product này thuộc về (1 cột Collection Name)~~

  - ~~Monthly Product sales: To be updated~~

# 

# **~~UC 4.1.12. Save Report as new~~**

## **~~Mục tiêu~~**

~~Người dùng có thể lưu lại report với các filter hiện tại thành **Custom report** để tiện cho việc xem lại report mà không cần thao tác filter mỗi lần đăng nhập vào Conative~~

## **~~Workflow~~**

### **~~Main flow~~**

~~1\. Trên trang Product Performance / Dashboard, người dùng thao tác chọn khung thời gian, filter và tìm kiếm~~

~~2\. Người dùng bấm \[Save report\]~~

~~2\. Hệ thống hiển thị popup để người dùng chọn lưu mới hoặc cập nhật report cũ **(Save as new / Update existing)** \> Bấm **Save as new**~~

~~3\. Hệ thống hiển thị popup để lưu thông tin report~~

~~4\. Người dùng đặt tên report~~

~~4\. Người dùng bấm **Save**~~ 

~~5\. Hệ thống kiểm tra dữ liệu hợp lệ \> lưu lại Custom report trong Menu~~ 

~~6\. Hệ thống thông báo “Report saved” và hiển thị tên report vừa được lưu bên cạnh title **Product Performance**~~

~~7\. Kết thúc use case~~ 

### **~~Exception flow~~**

~~4a. Người dùng bấm **Cancel, \[x\]**~~

- ~~Tắt popup và không lưu thông tin~~ 

- ~~Kết thúc Use case~~

## **~~Business Rule~~**

~~1\. Quy định đặt tên cho report:~~ 

- ~~Tối đa 50 ký tự~~ 

- ~~Mặc định rỗng~~

- ~~Bắt buộc nhập~~

# **~~UC 4.1.13 Update existing report~~** 

## **~~Mục tiêu~~**

~~Người dùng có thể cập nhật filter, search, config column và cập nhật **Custom report** đã lưu trước đó~~

## **~~Workflow~~**

### **~~Main flow~~**

~~1\. Trên trang CustProduct Performance / Dashboard, người dùng thao tác chọn khung thời gian, filter và tìm kiếm~~

~~2\. Người dùng bấm \[Save report\]~~

~~2\. Hệ thống hiển thị popup để người dùng chọn lưu mới hoặc cập nhật report cũ **(Save as new / Update existing)** \> Bấm **Update existing**~~

~~3\. Hệ thống hiển thị popup để lưu thông tin report~~

~~4\. Người dùng chọn **Custom report** đã tạo trước  đặt tên report~~

~~4\. Người dùng bấm **Save**~~ 

~~5\. Hệ thống kiểm tra dữ liệu hợp lệ \> lưu lại Custom report trong Menu~~ 

~~6\. Hệ thống thông báo “Report saved” và hiển thị tên report vừa được lưu bên cạnh title **Product Performance**~~

~~7\. Kết thúc use case~~ 

### **~~Exception flow~~**

~~4a. Người dùng bấm **Cancel, \[x\]**~~

- ~~Tắt popup và không lưu thông tin~~ 

- ~~Kết thúc Use case~~

## **~~Business Rule~~**

~~1\. Quy định đặt tên cho report:~~ 

- ~~Tối đa 50 ký tự~~ 

- ~~Mặc định rỗng~~

- ~~Bắt buộc nhập~~

## **~~1.3. Tài liệu tham khảo~~** 

- ~~Design: [Design](https://zpl.io/z8Gjxl4)~~ 

- ~~API: [API Usage](https://devtak.cbidigital.com/projects/conative-analytics-dubrovnik/wiki/advance-filter)~~

# **~~UC 4.1.14. Share custom report via link (Phase 1\)~~**

## **~~Mục tiêu~~**

~~Người dùng có thể chia sẻ report đã được lưu cho thành viên khác trong org~~ 

## **~~Input~~**

~~Link custom report~~

## **~~Output~~**

~~User trong cùng Org có thể xem được Custom report của các thành viên khác khi nhận được link share~~

## **~~Workflow~~** 

### **~~Main flow~~**

~~1\. Trên trang danh sách Custom report, user chọn action menu \> chọn \[Share\]~~ 

~~2\. Hệ thống hiển thị popup Share~~

~~3\. User chọn \[Copy link\] và gửi gửi link đã copy cho user khác trong cùng Organization~~ 

~~4\. User truy cập vào link~~ 

~~5\. Hệ thống xác thực link và user thuộc organization thành công, direct đến trang report~~

~~6\. Kết thúc Use case~~ 

### **~~Alternative flow~~** 

~~1a. Trên trang Custom report, user chọn \[Share\]~~ 

- ~~Quay trở về bước 2 Main flow~~

### **~~Exceptional Flow~~** 

~~4a. User không có quyền truy cập vào custom report~~ 

- ~~Hệ thống direct đến trao báo lỗi, Hiển thị thông báo **You need access permission** nếu user không thuộc Organization  truy cập link~~

~~4b. User thuộc Organization, nhưng đã sign out~~

- ~~Hệ thống direct đến trang Sign in~~

- ~~User sign in với tài khoản cùng Organization~~ 

- ~~Hệ thống direct đến trang Report tương ứng~~ 

- ~~Kết thúc use case~~ 


## **~~Business Rule~~** 

### **~~Quy định phân quyền~~**

~~User thực hiện use case này phải có role:~~ 

- ~~Admin, member của organization đó~~

### **~~Quy định hiển thị và thao tác~~** 

~~Link Custom report~~

- ~~Shorten link~~ 

- ~~Popup thông báo **Link copied** sau khi user chọn \[copy link\]~~

- ~~Hiển thị thông báo **You need access permission** nếu user không thuộc Organization  truy cập link~~

~~Reference~~

 

# **~~UC 4.1.15. View Custom report list~~** 

## **~~Mục tiêu~~**

~~User có thể xem được custom report đã tạo trong List Custom report, và chọn xem từng report.~~

## **~~Input~~**

~~View report~~

## **~~Output~~**

~~Report Name~~

~~Author: Full name of the user creates report~~

~~Created date: dd/mm/yyyy~~

~~Updated date: dd/mm/yyyy~~

~~Action: View & Delete~~

## **~~Workflow~~** 

~~1\. Trên sidebar menu, người dùng chọn \[Custom Report\] để vào xem danh sách các custom report đã tạo. Các thông tin~~ 

~~2\. Người dùng chọn vào report cần xem~~ 

~~3\. Hệ thống direct user sang trang Custom report tương ứng.~~ 

~~4\. Kết thúc Use Case~~ 

## **~~Business Rule~~**

### **~~Quy định hiển thị và thao tác~~** 

~~\- Danh sách report được sort theo thời gian tạo mới nhất~~ 

# **~~UC 4.1.16. Delete Custom report~~** 

## **~~Mục tiêu~~**

~~User có thể delete custom report đã tạo trong List Custom report~~

## **~~Input~~**

~~View report~~

## **~~Output~~**

~~Report Name~~

~~Author: Full name of the user creates report~~

~~Created date: dd/mm/yyyy~~

~~Updated date: dd/mm/yyyy~~

~~Action: View & Delete~~

## **~~Workflow~~** 

~~1\. Trên sidebar menu, người dùng chọn \[Custom Report\] để vào xem danh sách các custom report đã tạo. Các thông tin~~ 

~~2\. Người dùng chọn vào report cần delete, bấm chọn \[Deleete\]~~

~~3\. Hệ thống hiển thị popup xác nhận delete~~

~~4\. User:~~ 

- ~~Delete: chọn \[Delete\]. Hệ thống delete report và thông báo delete report thành công~~  
- ~~Cancel: Chọn \[Cancel\] để quay trở lại trang Custom report list~~

~~4\. Kết thúc Use Case~~ 

## **~~Business Rule~~**

### **~~Quy định phân quyền~~**

### **~~Quy định hiển thị và thao tác~~** 

# **UC 4.1.17. View Dashboard Donut chart \[Sales by Category\]** 

## **Mục tiêu** 

User xem được pie chart sales by category trên trang Dashboard theo time range mong muống

## **Main flow** 

1\. Trên trang dashboard, user xem pie chart Sales by Category 

2\. User chọn \[Revenue\] hoặc \[Unit sold\] để xem tổng Revenue hoặc unit sold và revenue hoặc Unit Sold theo từng category. 

3\. Hệ thống hiển thị Revenue hoặc Units sold tương ứng theo lựa chọn của user 

4\. User select / unselect từng Category để cộng hoặc trừ ra revenue hoặc units sold của category đó so với tổng revenue / units sold.


## **Business Rule** 

Quy định hiển thị và thao tác 

- Đơn vị mặc định là revenue $  
- Mặc định hiển thị 5 category có Percentage of Revenue (Gross sales) cao nhất và Others theo time range   
- Hover vào từng màu trên chart \> Highlight phần chart của category đó, hiển thị Category name & revenue của category đó   
- Unselect 1 category \> Disable category name của category đó, hide màu của category đó trên donut chart 

# **UC 4.1.18. Dashboard- Donut chart \[Sales by Price Range\]** 

User xem được pie chart sales by category trên trang Dashboard theo time range mong muống

## **Main flow** 

1\. Trên trang dashboard, user xem pie chart Sales by Price Range 

2\. User chọn \[Revenue\] hoặc \[Unit sold\] để xem tổng Revenue hoặc unit sold và revenue hoặc Unit Sold theo từng Price Range. 

3\. Hệ thống hiển thị Revenue hoặc Units sold tương ứng theo lựa chọn của user 

4\. User select / unselect từng Price Range để cộng hoặc trừ ra revenue hoặc units sold của Price Range đó so với tổng revenue / units sold.  

## **Business Rule** 

Quy định hiển thị và thao tác 

- Đơn vị mặc định là revenue $  
- Mặc định hiển thị 5 Price Range có Percentage of Revenue (Gross sales) cao nhất và Others theo time range   
- Hover vào từng màu trên chart \> Highlight phần chart của Price Range đó, hiển thị Price Range name & revenue của Price Range đó   
- Unselect 1 Price Range \> Disable Price Range name của Price Range đó, hide màu của Price Range đó trên donut chart 

# **UC 4.2. Sales by Category**

# **UC 4.2.1. Search category**

## **Mục tiêu**

Shopify: Người dùng có thể tìm kiếm category bằng cách nhập category name trên search bar. 

## **Input**

Truyền vào Category name

## **Output**

Trả dữ liệu theo Use case **View Sales by Category**

## **Workflow**

### **Main flow**

1\. Trên trang **Sales by Category**, người dùng bấm vào thanh \[Search\]

2\. Hệ thống đề xuất 5 category được tìm kiếm gần đây nhất

3\. Người dùng nhập thông tin để tìm kiếm category

1. Shopify: Người dùng có thể tìm kiếm category bằng cách nhập category name

4\. Hệ thống trả về dữ liệu sản phẩm theo điều kiện tìm kiếm

5\. Kết thúc use case 

### **Alternative flow**

3a. Người dùng chọn category theo đề xuất của hệ thống 

- Hệ thống trả về dữ liệu category theo điều kiện tìm kiếm

- Kết thúc use case 

### **Exceptional flow**

4a. Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

- Kết thúc use case.

## **Business Rule**

- Tìm kiếm theo Product title: search gần đúng 

- Tìm kiếm theo SKU: search gần đúng 

- Tìm kiếm theo Barcode: search gần đúng

# **UC 4.2.2. Select time range**

## **Mục tiêu**

Người dùng có thể chọn thời gian mà họ muốn xem dữ liệu của category

## **Workflow**

### **Main flow**

1\. Trên trang Sales by Category, người dùng chọn \[Calendar\]

2\. Hệ thống hiển thị popup để chọn khoảng thời gian

3\. Người dùng chọn khoảng thời gian mong muốn xem dữ liệu bằng cách chọn time range \[Date range\] có sẵn hoặc chọn ngày start date / end date trên lịch 

4\. Người dùng bấm **Apply** để lưu thời gian vừa chọn

5\. Hệ thống trả về dữ liệu theo khung thời gian tương ứng 

6\. Kết thúc use case 

### **Exception flow**

3a. Người dùng chọn khoảng thời gian trong tương lai

- Disable các ngày trong khoảng thời gian đó

5a.  Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

- Kết thúc use case.

## **Business Rule**

1\. Quy định hiển thị

3. Khoảng thời gian mặc định: Last 30 days (30 ngày gần nhất) 

4. Khi người dùng filter theo time range có sẵn của Conative, start date & end date tự động được highlight theo khoảng thời gian tương ứng, và ngược lại. 

2\. Quy định về khung thời gian có sẵn trên Conative

12. Today

13. Yesterday

14. Last 7 days

15. This month

16. Last month

17. Last 3 months

18. This year

19. Last year 

20. Week to date: 

    1. Starting date: ngày thứ Hai của tuần gần nhất

    2. End date: Today

21. Year to date:

    1. Starting date: ngày đầu tiên của năm gần nhất (Vd: 2023 \> Starting time là ngày 1/1/2023)

    2. End date: Today

    3. Quarter to date

    4. Starting date: ngày đầu tiên của quý gần nhất (Vd: Q2/2023 \> Starting time là ngày 1/4/2023)

    5. End date: Today

# **UC 4.2.3. Config column \- Sales by Category**

## **Mục tiêu**

Chọn/ thay đổi metric muốn hiển thị ở report Sales by Category

Input 

**Output**

Trả về danh sách field của Sales by Category

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Category title  |  |
| 2 | Gross sales |  |
| 3 | % of Gross sales |  |
| 4 | Gross quantity |  |
| 5 | Return value |  |
| 6 | Return quantity |  |
| 7 | Total sales |  |
| 8 | Ad spend |  |
| 9 | Ad clicks |  |
| 10 | Product views |  |
| 11 | Total inventory value  |  |

### **Main flow (Happy case)**

1\. Trên trang Product Performance / Dashboard, View all products người dùng bấm \[Config column\]

2\. Người dùng search và chọn metric (chưa hiện có) để thêm vào bảng dữ liệu sản phẩm 

3\. Người dùng chọn \[Modify columns\] 

4\. Hệ thống trả dữ liệu theo column đã chọn 

5\. Kết thúc use case 

### **Alternative Flow 1**

2a. Người dùng chọn \[Select all\] trong \[add column\] để chọn hiển thị tất cả các metric  

### **Alternative Flow 2**

2b. Người dùng kéo thả metric để sắp xếp thứ tự cột trong bảng dữ liệu 

### **Alternative Flow 3**

2c. Người dùng chọn \[Clear all\] trong \[add column\] để xóa các metric đã chọn 

### **Alternative Flow 4**

3a. Người dùng chọn \[Restore default\] 

4\. Hệ thống trả lại dữ liệu mặc định     

## **Business rule**

Quy định hiển thị và thao tác 

**Thứ tự hiển thị field mặc định cho user mới:** 

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Category title  |  |
| 2 | Gross sales |  |
| 3 | % of Gross sales |  |
| 4 | Gross quantity |  |
| 5 | Return value |  |
| 6 | Return quantity |  |
| 7 | Total sales |  |
| 8 | Ad spend |  |
| 9 | Ad clicks |  |
| 10 | Product views |  |
| 11 | Total inventory value  |  |

5. Người dùng click \[Clear all\], hệ thống xóa tất cả metric đã chọn nhưng giữ lại \[Product title\] 

6. Khi số lượng metric được chọn nhỏ hơn tổng metric, enable \[Select all\], \[Clear all\]

7. Khi tất cả các metric đều được chọn (số lượng metric được chọn bằng tổng metric), Enable \[Clear all\], disable\[Select all\] 

8. Khi không có metric nào được chọn (số lượng metric được chọn bằng 0), enable\[Select all\], disable\[Clear all\]

# **UC 4.2.4. Export Category report** 

## **Mục tiêu**

Người dùng có thể export dữ liệu của danh sách category cụ thể với các field và thứ tự đã được config trên trang Sales by Category

## **Input**

## **Output**

Export file CSV 

## **Workflow** 

### **Main flow**

1\. Ở trang Sales by Category, người dùng chọn \[Export\] để xuất dữ liệu 

2\. Kết thúc use case 

## **Business Rule** 

Format file CSV khi export list categories

- File Name

  -  \<All categories Month dd \- Month dd, yyyy\> (Eg: All categories Jul 01 \- Jul 31, 2023\)

- Dữ liệu (Các row & column) được export và format file CSV dựa theo kết quả dữ liệu trả về khi người dùng thực hiện các use case trên Sales by Category ví dụ Select Time range, Search category, Filter category, Sort category, Config Column

Các field và thứ tự field được export khi user để ở view mặc định 

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Category title  |  |
| 2 | Gross sales |  |
| 3 | % of Gross sales |  |
| 4 | Gross quantity |  |
| 5 | Return value |  |
| 6 | Return quantity |  |
| 7 | Total sales |  |
| 8 | Ad spend |  |
| 9 | Ad clicks |  |
| 10 | Product views |  |
| 11 | Total inventory value  |  |

# **UC 4.3. Sales by Collection**

# **UC 4.3.1. Search Collection** 

## **Mục tiêu**

Shopify: Người dùng có thể tìm kiếm Collection bằng cách nhập Collection name trên search bar. 

## **Input**

Truyền vào Collection name

## **Output**

Trả dữ liệu theo Use case **View Sales by Collection** 

## **Workflow**

### **Main flow**

1\. Trên trang **Sales by Collection** , người dùng bấm vào thanh \[Search\]

2\. Hệ thống đề xuất 5 Collection được tìm kiếm gần đây nhất

3\. Người dùng nhập thông tin để tìm kiếm Collection 

1. Shopify: Người dùng có thể tìm kiếm Collection bằng cách nhập Collection name

4\. Hệ thống trả về dữ liệu sản phẩm theo điều kiện tìm kiếm

5\. Kết thúc use case 

### **Alternative flow**

3a. Người dùng chọn Collection  theo đề xuất của hệ thống 

- Hệ thống trả về dữ liệu Collection  theo điều kiện tìm kiếm

- Kết thúc use case 

### **Exceptional flow**

4a. Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

- Kết thúc use case.

## **Business Rule**

- Tìm kiếm theo Product title: search gần đúng 

- Tìm kiếm theo SKU: search gần đúng 

- Tìm kiếm theo Barcode: search gần đúng

# **UC 4.3.2. Select time range (Sales by Collection Report)**

## **Mục tiêu**

Người dùng có thể chọn thời gian mà họ muốn xem dữ liệu của Collection 

## **Workflow**

### **Main flow**

1\. Trên trang Sales by Collection , người dùng chọn \[Calendar\]

2\. Hệ thống hiển thị popup để chọn khoảng thời gian

3\. Người dùng chọn khoảng thời gian mong muốn xem dữ liệu bằng cách chọn time range \[Date range\] có sẵn hoặc chọn ngày start date / end date trên lịch 

4\. Người dùng bấm **Apply** để lưu thời gian vừa chọn

5\. Hệ thống trả về dữ liệu theo khung thời gian tương ứng 

6\. Kết thúc use case 

### **Exception flow**

3a. Người dùng chọn khoảng thời gian trong tương lai

- Disable các ngày trong khoảng thời gian đó

5a.  Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

- Kết thúc use case.

## **Business Rule**

1\. Quy định hiển thị

1. Khoảng thời gian mặc định: Last 30 days (30 ngày gần nhất) 

2. Khi người dùng filter theo time range có sẵn của Conative, start date & end date tự động được highlight theo khoảng thời gian tương ứng, và ngược lại. 

2\. Quy định về khung thời gian có sẵn trên Conative

1. Today  
2. Yesterday  
3. Last 7 days  
4. This month  
5. Last month  
6. Last 3 months  
7. This year  
8. Last year 

9. Week to date: 

   1. Starting date: ngày thứ Hai của tuần gần nhất

   2. End date: Today

10. Year to date:

    1. Starting date: ngày đầu tiên của năm gần nhất (Vd: 2023 \> Starting time là ngày 1/1/2023)

    2. End date: Today

    3. Quarter to date

    4. Starting date: ngày đầu tiên của quý gần nhất (Vd: Q2/2023 \> Starting time là ngày 1/4/2023)

    5. End date: Today

# **UC 4.3.3. Config column \- Sales by Collection** 

## **Mục tiêu**

Chọn/ thay đổi metric muốn hiển thị ở report Sales by Collection 

Input 

**Output**

Trả về danh sách field của Sales by Collection 

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Collection title  |  |
| 2 | Gross sales |  |
| 3 | % of Gross sales |  |
| 4 | Gross quantity |  |
| 5 | Return value |  |
| 6 | Return quantity |  |
| 7 | Total sales |  |
| 8 | Ad spend |  |
| 9 | Ad clicks |  |
| 10 | Product views |  |
| 11 | Total inventory value  |  |

### **Main flow (Happy case)**

1\. Trên trang Product Performance / Dashboard, View all products người dùng bấm \[Config column\]

2\. Người dùng search và chọn metric (chưa hiện có) để thêm vào bảng dữ liệu sản phẩm 

3\. Người dùng chọn \[Modify columns\] 

4\. Hệ thống trả dữ liệu theo column đã chọn 

5\. Kết thúc use case 

### **Alternative Flow 1**

2a. Người dùng chọn \[Select all\] trong \[add column\] để chọn hiển thị tất cả các metric  

### **Alternative Flow 2**

2b. Người dùng kéo thả metric để sắp xếp thứ tự cột trong bảng dữ liệu 

### **Alternative Flow 3**

2c. Người dùng chọn \[Clear all\] trong \[add column\] để xóa các metric đã chọn 

### **Alternative Flow 4**

3a. Người dùng chọn \[Restore default\] 

4\. Hệ thống trả lại dữ liệu mặc định     

## **Business rule**

Quy định hiển thị và thao tác 

**Thứ tự hiển thị field mặc định cho user mới:** 

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Collection title  |  |
| 2 | Gross sales |  |
| 3 | % of Gross sales |  |
| 4 | Gross quantity |  |
| 5 | Return value |  |
| 6 | Return quantity |  |
| 7 | Total sales |  |
| 8 | Ad spend |  |
| 9 | Ad clicks |  |
| 10 | Product views |  |
| 11 | Total inventory value  |  |

1. Người dùng click \[Clear all\], hệ thống xóa tất cả metric đã chọn nhưng giữ lại \[Product title\] 

2. Khi số lượng metric được chọn nhỏ hơn tổng metric, enable \[Select all\], \[Clear all\]

3. Khi tất cả các metric đều được chọn (số lượng metric được chọn bằng tổng metric), Enable \[Clear all\], disable\[Select all\] 

4. Khi không có metric nào được chọn (số lượng metric được chọn bằng 0), enable\[Select all\], disable\[Clear all\]

# **UC 4.3.4. Export Collection Report**

## **Mục tiêu**

Người dùng có thể export dữ liệu của danh sách collection cụ thể với các field và thứ tự đã được config trên trang Sales by Collection

## **Input**

## **Output**

Export file CSV 

## **Workflow** 

### **Main flow**

1\. Ở trang Sales by Collections, người dùng chọn \[Export\] để xuất dữ liệu 

2\. Kết thúc use case 

## **Business Rule** 

Format file CSV khi export list Collection

- File Name

  -  \<All collections Month dd \- Month dd, yyyy\> (Eg: All collections Jul 01 \- Jul 31, 2023\)

- Dữ liệu (Các row & column) được export và format file CSV dựa theo kết quả dữ liệu trả về khi người dùng thực hiện các use case trên Sales by Collection ví dụ Select Time range, Search Collection, Filter Collection, Sort Collection, Config Column

Các field và thứ tự field được export khi user để ở view mặc định 

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Collection title  |  |
| 2 | Gross sales |  |
| 3 | % of Gross sales |  |
| 4 | Gross quantity |  |
| 5 | Return value |  |
| 6 | Return quantity |  |
| 7 | Total sales |  |
| 8 | Ad spend |  |
| 9 | Ad clicks |  |
| 10 | Product views |  |
| 11 | Total inventory value  |  |

# **UC 4.4.1. View Understock report**

## **Mục tiêu**

Hiển thị danh sách các metric của Variant level cho các product Replenishable= Yes, sale days left \< 45

## **Input**

- Search  
- Filter  
- Select time range  
- Channel settings  
- Config column 

## **Output**

- Trả về danh sách field của Variant level của các product Replenishable= Yes, sale days left \< 45

| STT | Field  | Calculation | Unit |
| :---- | :---- | :---- | :---- |
| 1 | Product title | \- |  |
| 2 | Gross sales |  |  |
| 3 | Gross quantity  |  |  |
| 4 | Return value |  |  |
| 5 | Return quantity |  |  |
| 6 | Return rate |  |  |
| 7 | Total sales |  |  |
| 8 | Price |  |  |
| 9 | Product views |  |  |
| 10 | % of revenue |  |  |
| 11 | Conversion rate |  |  |
| 12 | Day on site |  |  |
| 13 | Sales per day |  |  |
| 14 | Sales day left |  |  |
| 15 | Sell through |  |  |
| 16 | Stock |  |  |
| 17 | On order |  |  |
| 18 | ATS |  |  |
| 19 | Total inventory value |  |  |
| 20 | Trend |  |  |
| 21 | Next 90-day sales (AI) |  |  |
| 22 | Last 90-day sales (Rule based)  |  |  |
| 23 | Reorder quantity (AI) |  |  |
| 24 | Replenishable |  |  |
| 25 | Product status  |  |  |
| 26 | Gross margin |  |  |
| 27 | Gross profit |  |  |
| 28 | SKU |  |  |
| 29 | Product id |  |  |
| 30 | Variant id |  |  |
| 31 | Category |  |  |
| 32 | Color |  |  |
| 33 | Compared at price |  |  |
| 34 | Days until stock out |  |  |
| 35 | Net sales |  |  |
| 36 | Net quantity |  |  |
| 37 | Tax |  |  |
| 38 | Discount value |  |  |
| 39 | ROP |  |  |
| 40 | Channel |  |  |

## **Business rule**

1a. Quy định hiển thị và thao tác 

- Hiển thị tooltip mô tả của từng field khi hover vào header của của field đó

- Hiển thị hình ảnh của sản phẩm khi hover vào **product title** 

- Hiển thị mặc định với người dùng mới hoặc với người dùng chọn **Restore default** gồm các field và thứ tự như sau: 

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Product title |  |
| 2 | SKU |  |
| 3 | Gross sales |  |
| 4 | % of revenue |  |
| 5 | Gross quantity |  |
| 6 | Return value |  |
| 7 | Return quantity |  |
| 8 | Total sales |  |
| 9 | Price  |  |
| 10 | Product views |  |
| 11 | Conversion Rate |  |
| 12 | Day on site |  |
| 13 | Sales per day |  |
| 14 | Sales day left |  |
| 15 | Sell through |  |
| 16 | Stock  |  |
| 17 | On order |  |
| 18 | ATS |  |
| 19 | Total inventory value |  |
| 20 | Trend |  |
| 21 | Next 90-Day Sales (AI) |  |
| 22 | Last 90-Day Sales |  |
| 23 | Reorder Quantity (AI) |  |
| 24 | Replenishable |  |
| 25 | Product Status |  |

# **UC 4.5.1. View Overstock report**

## **Mục tiêu**

User có thể xem được các variant của những product được replenishable có Sales days left \> Days of stock (Dynamic settings), được sort theo Sales days left từ cao đến thấp.

## **Input**

- Setting: Days of stock

- Search

- Filter

- Select time range

- Config column 

## **Output**

- Trả về danh sách field của Variant level của các product Replenishable= Yes, sale days left (ATS) \> Days of stock, Default sort by Sales days left (ATS) cao đến thấp


| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | Product title | Product Title as listed in ecommerce platform | **Default Column**  No **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | SKU |  | **Default Column**  No **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 2 | Gross sales | Total sales recorded prior to sales discounts and sales returns | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B5) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 3 | Gross quantity  | Total units recorded prior to sales discounts and sales returns | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B5) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 4 | Return value | The value of product returned  | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B8) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 5 | Return quantity | The total unit quantity of product returned  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 6 | Return rate |  | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B10) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 7 | Total sales | Value of Net Sales Plus Shipping Income and Taxes | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B11) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 8 | Price | Price as listed in ecommerce platform | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 9 | Product views | The number of customers viewing specific product information. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 10 | Ad clicks | The total number of clicks on ads in Google and Facebook ad channels. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B17) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 11 | Ad spend  | Total sum of media spend on Google and Facebook ad channels. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 12 | % of revenue | Contribution percentage of overall revenue from this product  | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 13 | Conversion rate |  | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 14 | Day on site | Total number of days product has been live on your website | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 16 | Sales day left (ATS) | The amount of days the current stock of an item will last based on current sales per day. Calculated by ATS divided by Sales Per Day | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Default sort từ cao đến thấp Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 17 | Sell through | Percentage of overall products sold to total overall inventory quantity of any given product.   | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 18 | Lot code |  | **Display:**  Chỉ hiển thị với Industry Cosmetic (Vd: brand Ann marie) Chỉ hiển thị đối với variant khi user chọn dropdown hiển thị list variant của product  **Default Column**  Yes (Vị trí default column xem ở UC 4.1.5 Config column \- Product level)  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 19 | Expiration date |  | **Display:**  Chỉ hiển thị với Industry Cosmetic (Vd: brand Ann marie) Chỉ hiển thị đối với variant khi user chọn dropdown hiển thị list variant của product  **Default Column**  Yes (Vị trí default column xem ở UC 4.1.5 Config column \- Product level) **Sort** Mặc định sort theo ngày gần nhất đến ngày xa nhất khi user expand product  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 20 | Stock | Total quantity of product received in inventory. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 21 | On order | The number of products ordered with the supplier but not yet received. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 22 | ATS | The total quantity of product available to sell, this the sum of all product inventory in Stock and On Order. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 23 | Total inventory value | Total value of all in Stock inventory. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 24 | Trend |  | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 25 | Next 90-day sales (AI) | Sales forecast for the next 90 days | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 26 | Last 90-day sales (Rule based)  | Total sales quantity in the previous 90 days | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 27 | Reorder quantity (AI) | Conative AI-powered suggested quantity to reorder, by deducting Sales Forecast by ATS | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B18) **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 28 | Replenishable | The status whether or not an item is going to be reproduced in the future | **Default Column**  Yes **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 29 | Product status  | Product status on Shopify (Active, Disabled, Draft) | **Default Column**  Yes  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description   |
| 30 | Gross margin | Net Revenue minus Cost of Goods Sold | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 31 | Gross profit | Net Revenue minus Cost of Goods Sold and Operating Expenses. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 32 | Product id | Unique Product Identifier from ecommerce platform | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Variant id | Unique VariantIdentifier from ecommerce platform | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Bar code |  | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Color |  | **Default Column**  Yes  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 33 | Category |  | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 34 | Days until stock out | Predicted days until stock reaches zero | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Next arrival date |  | **Rule**  The arrival date of nearest PO that include the item  **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 35 | Net sales | Gross Sales of minus the value of Returns and Discounts. | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 36 | Net quantity |  | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 37 | Tax | The total amount of taxes based on each product | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 38 | Discount value | Deduction from the usual cost of the product | **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 39 | ROP | The minimum level of inventory needed to cover the Lead Time | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 40 | Channel | Name of channel used by marketing or sales | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 41 | Sales per day (In stock) | The average number of products sold in a day. (accounting only for days when the product is in stock) | **Calculation** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27) **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description  |
| 42  | Sales per day (Out of stock) | The average number of products sold in a day. (accounting only for days when the product is out of stock) | **Calculation**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27)  **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 43 | Action |  |  |
| 44 | Compare-at-price | The comparison of the original price and the sale price. | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 45 | Cost |  | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Chưa có content |

## 

## **Business rule**

Quy định hiển thị và thao tác 

- Header: 

  - Không xuống dòng 

  - Đối với field có value dạng chữ (text) thì canh lề trái 

  - Đối với field có value dạng số (number) thì canh lề phải 

- Column

  - Freeze Column Product title và Column Position (khi filter collection) khi user scroll ngang   
- Hiển thị tooltip mô tả của từng field khi hover vào header của của field đó  
- Hiển thị hình ảnh của sản phẩm khi hover vào **variant title**   
- Hiển thị field position của product và freeze ở ngoài cùng bên trái khi filter Collection  
- Hiển thị mặc định với người dùng mới hoặc với người dùng chọn **Restore default** gồm các field và thứ tự như sau: 

| STT | Field |
| :---- | :---- |
| 1 | Variant Title |
| 2 | SKU |
| 3 | Gross sales |
| 4 | Gross Quantity |
| 5 | Sell Through |
| 6 | Conversion Rate |
| 7 | Sales Per Day |
| 8 | Sales Days Left (ATS) |
| 9 | Next 90-Day Sales (AI) |
| 10 | Stock |
| 11 | On Order |
| 12 | ATS |
| 13 | Price |
| 14 | Compare at Price |
| 15 | Cost |
| 16 | Total Inventory Value |
| 17 | Total cost |
| 18 | Trend |
| 19 | % Of Revenue |
| 20 | Product Views |
| 21 | Return Value |
| 22 | Return Quantity |
| 23 | Total Sales |
| 24 | Day On Site |

## **Business rule**

1a. Quy định hiển thị và thao tác 

- Hiển thị tooltip mô tả của từng field khi hover vào header của của field đó

- Hiển thị hình ảnh của sản phẩm khi hover vào **product title** 

- Hiển thị mặc định với người dùng mới hoặc với người dùng chọn **Restore default** gồm các field và thứ tự như sau: 

| STT | Field |  |
| :---- | :---- | :---- |
| 1 | Product title |  |
| 2 | SKU |  |
| 3 | Gross sales |  |
| 4 | % of revenue |  |
| 5 | Gross quantity |  |
| 6 | Return value |  |
| 7 | Return quantity |  |
| 8 | Total sales |  |
| 9 | Price  |  |
| 10 | Product views |  |
| 11 | Conversion Rate |  |
| 12 | Day on site |  |
| 13 | Sales per day |  |
| 14 | Sales day left |  |
| 15 | Sell through |  |
| 16 | Stock  |  |
| 17 | On order |  |
| 18 | ATS |  |
| 19 | Total inventory value |  |
| 20 | Trend |  |
| 21 | Next 90-Day Sales (AI) |  |
| 22 | Last 90-Day Sales |  |
| 23 | Reorder Quantity (AI) |  |
| 24 | Replenishable |  |
| 25 | Product Status |  |

# **UC 4.5.2 Overstock Report Export variant list và variant detail**

## **Mục tiêu**

Người dùng có thể export dữ liệu của danh sách variant với các field và thứ tự đã được config trên trang Overstock report

## **Input**

## **Output**

Export file CSV 

## **Workflow** 

Mainflow 

3. Trên trang Overstock Report, user chọn \[Export\]

4. Hệ thống export file theo yêu cầu và thông báo Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

## **Business Rule** 

Format file CSV khi export list of variant

- File Name

  -  \<Overstock report Month dd \- Month dd, yyyy\> (Eg: Overstock report \- Variants Jul 01 \- Jul 31, 2023\)

- Dữ liệu (Các row & column) được export và format file CSV dựa theo kết quả dữ liệu trả về khi người dùng thực hiện các use case trên Overstock report ví dụ Select View, Sêlect Time range, Search product, Filter product, Sort product, Config Column

Format file CSV khi export product, Variant ở trang PDP

- File Name

  -  \<Overstock report \- Month dd \- Month dd, yyyy\> (Eg: Overstock report \- Jul 01 \- Jul 31, 2023\)

- Dữ liệu (Các row & column) được export sẽ bao gồm các tất cả các field dữ liệu của product đó và dựa theo kết quả dữ liệu trả về khi người dùng filter time range trong PDP.

# **reUC 4.5.3 Advanced Filter in Overstock report**

## **1.1. Mục tiêu**

Trên các trang Overstock, user có thể filter các metrics và lưu lại lại filter thành custom report.

## **1.2. Input** 

Filter (select)

Condition (Operators)

Filter values 

## **1.3. Output**

Có thể filter các metrics và lưu lại filter thành custom report 

## **1.4. Workflow** 

### **Main flow (Happy case)**

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Chọn \[Apply Filter\]

8\. Hệ thống trả về dữ liệu theo điều kiện filter

Alternative Flow 1

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Người dùng xóa bớt value bằng cách tick vào \[x\] bên cạnh value 

8\. Chọn \[Apply Filter\]

9\. Hệ thống trả về dữ liệu theo điều kiện filter

### **Alternative Flow 2**

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Chọn \[Clear All\]

8\. Xóa các filter đã lựa chọn 

### **Exceptional flow 1**

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng không chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Chọn \[Apply Filter\]

4\. Hệ thống thông báo lỗi và yêu cầu user chọn filter.

### **Exceptional Flow 2** 

1\. Trên trang Overstock report, người dùng bấm \[Filter\]  
2\. Người dùng không chọn filter & điều kiện filter  
3\. Người dùng không tìm kiếm thấy filter value ở field \[Value\]   
4\. Hệ thống trả về thông báo lỗi. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

## **Business Rule (Phase 1):**

|  | Filters (Fields) | Conditions (Operators) | Types |
| :---- | :---- | :---- | :---- |
|  | **Product**  |  |  |
|  | Collection | Is Is not | Multiple selection |
|  | Barcode | Is Is not | Multiple selection Short text |
|  | Tag | Is Is not | Multiple selection Short text |
|  | Color  | Is Is not | Multiple selection |
|  | Status | Is Is not | Multiple selection |
|  | SKU | Is Is not | Multiple selection |
|  | Gross Sales | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
|  | Gross Quantity | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
|  | Stock | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
|  | ATS | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 3 | Return value | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 4 | Return quantity | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 5 | Return rate | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 6 | Total sales | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 7 | Price | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 8 | Product views | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 9 | % of revenue | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 10 | Conversion rate | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 11 | Day on site | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 12 | Sales per day | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 13 | Sales day left (ATS) | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 14 | Sell through | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 15 | Stock | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 16 | On order | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 17 | ATS | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 18 | Total inventory value | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 19 | Trend | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 20 | Next 90-day sales (AI) | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 21 | Last 90-day sales (Rule based)  | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 22 | Reorder quantity (AI) | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 23 | Replenishable | Is Is not | Multiple selection |
| 24 | Product status  | Is Is not | Multiple selection |
| 25 | Gross margin | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 26 | Gross profit | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 27 | SKU | Is Is not | Multiple selection |
| 28 | Product id | Is Is not | Multiple selection |
| 29 | Variant id | Is Is not | Multiple selection |
| 30 | Category | Is Is not | Multiple selection |
| 31 | Color | Is Is not | Multiple selection |
| 32 | Compared at price | Is Is not | Multiple selection |
| 33 | Days until stock out | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 34 | Net sales | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 35 | Net quantity | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 36 | Tax | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 37 | Discount value | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 38 | ROP | Equal to Less than Less than or equal Greater than Greater than or equal Between | Input value |
| 39 | Channel | Is Is not | Multiple selection |

## **Business Rule bổ sung (Phase 2):**

Quy định hiển thị và thao tác 

Manage Filter \- Block filter đầu tiên

- Mặc định hiển thị mỗi khi user bật popup filter

- Select Operator: ẩn

Block filter sau đó: 

- Select Operator mặc định “And” 

Search Filters (Operators, Filter, Condition, Value \- Multiple selection)

- Suggest kết quả theo từ khóa search 

Hiển thị List Operators, conditions, value \- multiple selection

- Mặc định hiển thị dropdown khi chọn field

- Số lượng item hiển thị mặc định: 30

- Show more\> hiển thị 30 item kế tiếp

## **Reference** 

Design: [https://zpl.io/z8Gjxl4](https://zpl.io/z8Gjxl4)

API: [**https://devtak.cbidigital.com/projects/conative-analytics-dubrovnik/wiki/advance-filter**](https://devtak.cbidigital.com/projects/conative-analytics-dubrovnik/wiki/advance-filter)

# 

# **UC 6.1. View Integration Progress** 

## **Mục tiêu**

User có thể xem được tất cả các data source, status connection và progress pull data từ từng source

## **Input**

Integration hub

Connect data source 

## **Output**

Data source connection status

Authorization notification 

Data mapping notification 

Data pulling progress

## **Workflow**

### **Mainflow**

1\. Ở trang Integration hub, user connect data source (Tham khảo use case 6.1 \- 6.3)

2\. Hệ thống hiển thị thông báo khi: 

- User connect data source thành công  
- Hệ thống đang load data sau khi connect data source 

Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

3\. Kết thúc Use case 

### **Exceptional flow 1 \- Connect data source không thành công**

1\. Hệ thống hiển thị notification thông báo connect data source không thành công  Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

2\. Kết thúc Use Case 

### **Exceptional flow 2 \- Access token expired**

1\. Hệ thống hiển thị notification thông báo access token expired ( Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**)

2\. Kết thúc Use Case 

## **Business Rule:** 

Quy định hiển thị và thao tác: 

Trong quá trình init load dữ liệu, khi user chọn các trang report sẽ mặc định hiển thi popup thông báo đang load data. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**.

Design: 

[https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative\_New?type=design\&node-id=495-37032\&mode=design\&t=XQA7BAKc5jKQmdQj-4](https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative_New?type=design&node-id=495-37032&mode=design&t=XQA7BAKc5jKQmdQj-4)

Note: Chỉ cần title, bỏ thành progress đi

# **UC 6.2. Connect to Shopify**

## **1.1. Mục tiêu**

Người dùng kết nối được với tài khoản Shopify của họ và pull được dữ liệu về hệ thống Conative

## **1.2. Input** 

- Permission để install app trong Shopify

- Myshopify url

- API key

- API password

## **1.3. Output** 

- Cài đặt thành công app Conative AI trên Store Shopify của user

- Connect và lấy được data API SHopify trả về

## **1.4. Workflow** 

### **Main flow (Happy case)** 

1\. User vào Shopify Admin, install Custom app theo hướng dẫn.

2\. Vào trang Integration Hub (Conative), chọn **connect to Shopify** 

3\. Hệ thống hiện thị các field thông tin để người dùng nhập: 

- Myshopify url

- API key

- API password

4\. Chọn **Connect** 

5\. Hệ thống map dữ liệu với trường thông tin tương ứng và bắt đầu pull dữ liệu về hệ thống

6\. Thông báo người dùng về progress cập nhật dữ liệu và khi hoàn tất pull dữ liệu 

7\. Kết thúc use case 

### **Exceptional flow 1 \- User nhập sai thông tin connect Shopify**

4\. Chọn Connect 

5\. Hệ thống hiển thị thông báo lỗi. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

### **Exceptional flow 2 \- Connect failed, Reconnect**

4\. Chọn Connect 

5\. Hệ thống kiểm tra thông tin thất bại, hiển thị thông báo lỗi. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

6\. User chọn \[Reconnect\] để connect lại với Shopify. 

## **1.5 Business rule**

**Quy định phân quyền**

User thực hiện use case này phải có role: 

- Admin của organization bất kỳ trên Conative 

**Quy định hiển thị và thao tác** 

Page Integration hub 

- Source có 3 trạng thái: 

  - Chưa connect: CTA \[Connect\]

  - Đã connect: Có dấu tick xanh, CTA \[Update\]

  - Connect failed / Token expired: Có dấu (\!), CTA \[Reconnect\] \+ Error message: **Looks like your Shopify token has expired. Just reconnect it and you'll be able to view your data**

Field Your myshopify.com url: 

- Mặc định rỗng 

- Bắt buộc nhập 

Field Your API key: 

- Mặc định rỗng 

- Bắt buộc nhập 

Field API password 

- Mặc định rỗng

- Bắt buộc nhập 

- Mặc định masking ký tự khi nhập, unmask khi user chọn \[eyes open\]


## **1.6 Reference** 

# **UC 6.3. Connect to Facebook**

## **1.1. Mục tiêu**

Người dùng kết nối được với tài khoản Facebook của họ và pull được dữ liệu về hệ thống Conative

## **1.2. Input** 

- Email to login to Facebook 

- Access to the Ads Manager

## **1.3. Output** 

- Kết nối với Facebook thành công và pull được dữ liệu Ad spend & Ad click

## **1.4. Workflow** 

### **Main flow (Happy case)** 

1\. Vào trang Integration Hub, chọn **connect to Facebook**

2\. Hệ thống direct người dùng sang Facebook, yêu cầu đăng nhập vào store và cấp quyền để cài đặt app Conative AI

4\. Cấp quyền và cài đặt thành công 

5\. Chọn mapping dữ liệu tự động / thủ công với Ad mapping 

6\. Hệ thống map dữ liệu với trường thông tin tương ứng và bắt đầu pull dữ liệu về hệ thống

7.Thông báo người dùng về progress cập nhật dữ liệu và khi hoàn tất pull dữ liệu 

8\. Kết thúc use case 

### **Exceptional flow 2 \- Connect failed, Reconnect**

4\. Chọn Connect 

5\. Hệ thống direct link sang Facebook để authorize quyền cho account. Authorize không thành công, call back ngược về Conative

6\. Hệ thống hiển thị thông báo lỗi. Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

7\. User chọn \[Reconnect\] để bắt đầu lại flow authorize với Facebook

8\. Kết thúc use case

### **Exception flow 3 \- Bắn job failed, Reconnect** 

5\. Hệ thống map dữ liệu và pull dữ liệu không thành công 

6\. Ở trang Integration hub, hệ thống hiển thị thông báo lỗi. Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

7\. User chọn \[Reconnect\] để bắt đầu lại flow authorize với Facebook

## **1.5 Business rule** 

- Source có 3 trạng thái: 

  - Chưa connect: CTA \[Connect\]

  - Đã connect: Có dấu tick xanh, CTA \[Update\]

  - Connect failed / Token expired: Có dấu (\!), CTA \[Reconnect\]

## **1.6 Reference** 

# **UC 6.4. Connect to Google (Updating)**

## **1.1. Mục tiêu**

Người dùng kết nối được với tài khoản Google của họ và pull được dữ liệu về hệ thống Conative

## **1.2. Input** 

- Email to login to Google account

- Access to the Ads account

## **1.3. Output** 

- Kết nối với Google thành công và pull được dữ liệu Ad spend & Ad click từ Google ads, Product page view từ Google Analytics

## **1.4. Workflow** 

### **Main flow (Happy case)** 

1\. Vào trang Integration Hub, chọn **connect to Google**

2\. Hệ thống bật popup để đăng nhập vào tài khoản Google yêu cầu cấp quyền để cài đặt app Conative AI

3\. Chọn account cần pull dữ liệu

4\. Hệ thống map dữ liệu với trường thông tin tương ứng và bắt đầu pull dữ liệu về hệ thống

5.Thông báo người dùng về progress cập nhật dữ liệu và khi hoàn tất pull dữ liệu 

6\. Kết thúc use case 

### **Exceptional flow 2 \- Connect failed, Reconnect**

4\. Chọn Connect 

5\. Hệ thống direct link sang Google để authorize quyền cho account. Authorize không thành công, call back ngược về Conative

6\. Hệ thống hiển thị thông báo lỗi. Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

7\. User chọn \[Reconnect\] để bắt đầu lại flow authorize với Google

8\. Kết thúc use case

### **Exception flow 3 \- Bắn job failed, Reconnect** 

5\. Hệ thống map dữ liệu và pull dữ liệu không thành công 

6\. Ở trang Integration hub, hệ thống hiển thị thông báo lỗi. Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

7\. User chọn \[Reconnect\] để bắt đầu lại flow authorize với Google

## **1.5 Business rule** 

- Source có 3 trạng thái: 

  - Chưa connect: CTA \[Connect\]

  - Đã connect: Có dấu tick xanh, CTA \[Update\]

  - Connect failed / Token expired: Có dấu (\!), CTA \[Reconnect\]

## **1.6 Reference** 

# **Workflow \- Create Subscription plan in Stripe**

1. In the Stripe Dashboard, go to the [subscriptions](https://dashboard.stripe.com/test/subscriptions) page.  
2. Click **\+Create subscription**.  
3. Find or add a customer.  
4. Enter the pricing and product information. You can add multiple products.  
5. Set the start and end date of the subscription.  
6. Set the starting date for the billing cycle. This defines when the next invoice is generated. 

# **Workflow \- Edit Subscription plan in Stripe**

1. Go to the [subscriptions](https://dashboard.stripe.com/test/subscriptions) page.  
2. Find the subscription you want to modify, click the overflow menu (  
3. ), then click **Update subscription**. You can also click the  
    next to the subscription name. From this menu, you can also:  
   * **Cancel the subscription**. In the modal that opens, select the date to cancel the subscription—immediately, at the end of the current period, or on a custom date. You can also select the option to refund the last payment for this subscription and create a [credit note](https://stripe.com/docs/invoicing/dashboard/credit-notes) for your records.  
   * **Pause payment collection**. In the modal that opens, select the duration of the pause—indefinite or ending on a custom date—and how invoices should behave during the pause.  
   * **Share payment update link**. In the modal that opens, you can share a link with the customer to update their payment details.   
4. Make your changes to the subscription.  
5. Click **Update subscription**.

**\*can’t delete a subscription**

# **UC 6.5 Connect to OceanX Bridge (File Sync)**

## **1.1. Mục tiêu**

Người dùng kết nối được với tài khoản OceanX Bridge để lấy được dữ liệu về Conative 

## **1.2. Input** 

- Csv (Parcel Ship)

## **1.3. Output**

- Expiration date   
- Lot code   
- Stock quantity

## **1.4. Workflow** 

### **Main flow (Happy case)** 

1. Vào trang Integration Hub, chọn **connect to Bridge \> Upload file**

2. Hệ thống redirect đến trang Upload Inventory file

3. Người dùng bấm chọn \[Upload Inventory file\]

4. Hệ thống hiển thị drawer

5. User chọn type (cách thức ETL)

6. User upload file

7. Hệ thống validate định dạng file thành công

8. Hệ thống hiển thị \[Mapping Column\] 

9. Hệ thống mặc định mapping bằng field: 

   1. Warehouse

   2. SKU

   3. LotCode

   4. Expiration

   5. Stock

10. User chọn map warehouse từ file upload với warehouse của Shopify

11. Người dùng chọn \[Upload file\]

12. Hệ thống validate CSV input và hiển thị progress upload, số lượng variant upload thành công, số lượng variant upload không thành công 

13. Hệ thống hiển thị danh sách file được upload Conative và status ETL

## **Business Rule**

### **Main flow (Happy case)** 

1. Vào trang Integration Hub, chọn **connect to Bridge \> Upload file**

2. Hệ thống redirect đến trang Upload list Inventory file

3. Người dùng bấm chọn \[Upload Inventory file\]

4. Hệ thống hiển thị drawer

5. User chọn type (cách thức ETL)

6. Người dùng bấm \[+\] chọn Upload CSV file và chọn file cần upload ở mục \[File\]

7. Người dùng chọn file upload

8. Hệ thống validate định dạng file:

   1. Nếu không đúng định dạng (vd: png, pdf…): Thông báo lỗi 

   2. Nếu đúng định dạng CSV: Chuyển đến bước kế tiếp

9. Hệ thống hiển thị \[Mapping Column\] và mặc định mapping field của Conative với các column có header tương ứng trên file upload (Xem business rule):

   1. Warehouse \= Warehouse code

   2. SKU \= Product code

   3. LotCode \= Lot code

   4. Expiration date \= Expiration date

   5. Stock \= Available quantity

10. Hệ thống hiển thị danh sách warehouse của Shopify và danh sách warehouse được lấy từ field \[Warehouse code\] trong file upload

11. User mapping warehouse 

12. User chọn \[Upload file\]

13. Hệ thống upload file lên S3

    1. Nếu không thành công: Thông báo lỗi và cho user upload lại 

    2. Nếu thành công: Thông báo thành công

14. Hệ thống thực hiện job và import vào EDW (Enterprise Data Warehouse) (Xem Job status ở Business Rule)

    1. Nếu không thành công: Thông báo lỗi và thay đổi Job status lỗi

    2. Nếu thành công: Thông báo lỗi và thay đổi Job status thành công

15. User view report Product Performance / Dashboard để xem số lượng stock đã được cập nhật cho từng expiration date & lot code 

16. Kết thúc Use case

### **Exceptional flow 1 \-  Missing data with empty fields in file uploaded**

Exceptional flow 2 \- Duplicating SKU in file uploaded 

Exceptional flow 3 \- File uploaded không đúng định dạng 

## **Business Rule**

**Quy định hiển thị và thao tác**

**File upload list Inventory file**

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | Date upload | Ngày file được upload lên hệ thống  | **Rule Format hiển thị:** 05 Sep, 2023 |
| 2 | File uploaded | Tên file được upload |  |
| 3 | Uploaded by | User upload file lên hệ thống  |  |
| 4 | Job id | Id ETL của Job được truyền từ layer 1 để Layer nhận thông tin và  | **Rule** L1 quy định  |
| 5 | Job status |  | Xem ở mục **ETL Job** |

**Popup Upload file**

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
|  | Type | CDC (Captured data change) when user select import snapshot file / receipt  | **Rule** Gồm 3 type:  1\. import receipt 2\. export receipt 3\. Snapshot from Bridge (recept/snapshot) Mặc định chọn type **Snapshot from Bridge (receipt / snapshot)**  |

**Inventory csv template:**

- exportInventoryLevels (From Bridge) 

\[CTA & Bar\] Select file to upload

- \[File selection\]: 

| Khi chưa có file  | Khi đã tải file  |
| :---- | :---- |
| No file selected  | File\_name  (Nếu tên file quá dài, hiển thị “...” |

- CTA \[+\]: Người dùng nhấn chọn để tải file lên hệ thống  
- CTA \[![][image1]\]: Người dùng nhấn chọn để thay đổi file khác


**File validation & Mapping columns**

- File type: Csv  
- Mapping column:  
  - Đảm bảo header của column trong file upload phải match với key dùng để map (Phải cover được case Header viết hoa, viết thường, có dấu cách để hạn chế human error trong lúc upload file)


| Field | Rule |
| :---- | :---- |
| SKU  | Mục Column in your file Field SKU được mặc định map với column “Product Code”  Dropdown **disabled** khi đã map theo mặc định Nếu không tìm thấy column “Product code” \=\> hiển thị “No data found” Bắt buộc nhập  |
| Lot code | Mục Column in your file Field Lot Code được mặc định map với column “Lot Code”  Dropdown **disabled** khi đã map theo mặc định Nếu không tìm thấy column “Lot  code” \=\> hiển thị “No data” Bắt buộc nhập  Mapping rule:  Override data mới nhất Bỏ qua nếu Lot code \= Null  |
| Expiration date  | Mục Column in your file Field Expiration date  được mặc định map với column “Expiration date ”  Dropdown **disabled** khi đã map theo mặc định Nếu không tìm thấy column “Expiration date” \=\> hiển thị “No data” Bắt buộc nhập  Mapping rule:  Override data mới nhất Bỏ qua nếu Expiration date \= Null Bỏ qua nếu Expiration date \= String  Không phân biệt ngày trong quá khứ  |
| Stock | Mục Column in your file Field Stock được mặc định map với column “Available Quantity”  Dropdown **disabled** khi đã map theo mặc định Nếu không tìm thấy column “Expiration date” \=\> hiển thị “No data” Bắt buộc nhập Mapping rule:  Override data mới nhất Bỏ qua nếu Stock \= String  Không phân biệt số âm / dương Không làm tròn nếu là số thập phân |
| Warehouse | Mục Column in your file Warehouse code  được mặc định map với column “Warehouse code”  Dropdown **disabled** khi đã map theo mặc định Nếu không tìm thấy column “Expiration date” \=\> hiển thị “No data” Bắt buộc nhập  Mapping rule Bỏ qua nếu Warehouse code \= null |


  **Warehouse Mapping**


| Warehouse | Warehouse from Bridge  Dropdown list hiển thị danh sách Warehouse code trên Bridge theo rule Mapping column (field warehouse) Bắt buộc chọn ít nhất 1  Warehouse from Shopify Dropdown list hiển thị danh sách Warehouse status \= Active sync từ Shopify Bắt buộc chọn tương ứng với số lượng warehouse đã chọn ở cột Bridge Mapping rule 1 warehouse code ở Bridge chỉ map với 1 warehouse ở Shopify. Không được map trùng ETL rule:  Đồng bộ stock theo warehouse được mapping giữa Brdige & Shopify |
| :---- | :---- |


- Hệ thống báo lỗi khi   
  - File không đúng định dạng   
  - Không tìm thấy header của cột được map mặc định trong file upload (Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563))

**CTA \[Upload file\]**

- Mặc định disable  
- Enable sau khi hệ thống validate file upload và mapping column thành công

**ETL Job**

- Job id: Id của job ETL (Định nghĩa bởi L1)  
- Job status   
  - **Scheduled**: File được upload lên S3 nhưng chưa job chưa chạy   
  - **Processing**: Đang thực hiện đưa data vào EDW  
  - **Successful**: Khi **tất cả** record trong file được đồng bộ thành công **và** user đồng ý **skip** các trường hợp mapping hoặc job chạy lỗi.   
  - **Failed**: Khi mapping hoặc job chạy lỗi


- CDC  
  - Type **recept/snapshot**: Override data (Ví dụ: Khi user upload file mới có cùng cùng expired date nhưng stock thay đổi thì lấy data stock mới từ file mới nhất)   
    

- Những case cần lưu ý: 

  - Duplicated SKU on Shopify: Ưu tiên cập nhật data cho variant có status \= **Active.** Nếu các SKU Duplicate đều có status \= **Active** trên Shopify thì không cập nhật data

  - Duplicated lot code, expiration date, sku, but different Available quantity in file: Merge các item thành 1, sum available quantity. 

  - Missing SKU on Shopify: Không cập nhật data cho các record có SKU không có trên Shopify

  - Empty expiration date / Lot code in file: Không cập nhật data cho các record có expiration date hoặc Lot code empty

  - Wrong format of expiration date: Không cập nhật data cho các record có expiration date có format không chuẩn

  - Missing warehouse on Shopify: Không cập nhật data cho các record khác warehouse code so với Shopify

  - Stock của từng Lot code sẽ được lấy từ Bridge nhưng stock tổng của Product chứa Lot code đó thì vẫn được pull từ Shopify

- Hệ thống báo lỗi (Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)) khi:

  - Missing SKU on Shopify

  - Duplicated SKU (Status \= Active) on Shopify

  - Wrong format of expiration date 

  - Missing warehouse on Shopify

# 

# **UC 9.1 \- Using free trial on Subscription**

## **Mục tiêu**

User sau khi đã sign up & create Organization, hoặc được invite vào organization có thể sử dụng được tính năng của gói Subscription trong thời gian Free trial

## **Input**

Free trial Duration

Features included in Subscription

## **Output**

Sử dụng các tính năng của gói Subscription

## **Workflow**

### **Main flow**

1\. User sign up & create organization thành công (UC 1.1, UC 2.2)

2\. User sử dụng được các tính năng trên Conative được bao gồm trong Subscription “Starter” đã được tạo trên Stripe (Tham chiếu UC 9.1)

3\. Hệ thống lấy API thời gian kết thúc free trial so sánh với thời điểm thực 

1. Nếu chưa đến end date: quay về step3  
2. Nếu đã qua end date, chuyển sang bước tiếp theo 

4\. Hệ thống tắt access của người dùng vào các tính năng của conative

5\. Hệ thống trở về trang chủ và hiện thông báo hết hạn free trial, yêu cầu người xác nhận có dùng có muốn tiếp tục sử dụng 

1. Nếu chọn \[Yes\], hệ thống hiển thị trang \[Your plan\] và tiếp tục UC 9.2  
2. Nếu chọn \[No\], hệ thống downgrade subscription ở strive

5\. Stripe 

6\. Kết thúc use case 

## **Business Rule**

1. ### **Quy định phân quyền**

User thực hiện use case này phải có role: 

- Admin, Member của organization đó 

Quy định hiển thị và thao tác 

2. ### **Quy định hiển thị và thao tác** 

Khi trên tài khoản stripe có update về subscription plan thì ở phía Conative sẽ update thông tin subscription plan tương ứng 

3. Lấy API end date từ stripe để hiển thị số ngày đến thời điểm hết hạn free trial ở trang \[Current plan\]

 


4. Stripe gửi email sắp hết hạn free trial trong đầu mỗi 2 ngày cuối của thời hạn free trial kèm CTA: Pay now 

   

5. Stripe gửi email đã hết hạn free trial trong đầu mỗi 3 ngày cuối của thời hạn xác nhận kèm CTA: Continue using 

# **UC 9.2. Make payment on Subscription**

## **Mục tiêu**

Người dùng có thể chọn đăng ký và thanh toán gói subscription mong muốn

## **Input**

Billing Address: country/region, address, city, state, ZIP code, Business name 

Payment Method information: Card Number, Expiration date, CVV 

Billing Contact: Full name,  Email

## **Output**

Đăng ký và thanh toán gói subscription mong muốn thành công 

## **Workflow**

### **Main flow (thanh toán khi chưa hết free trial)**

1\. Người dùng chọn \[Plan & Billing\] \> \[My plan\] từ Admin menu, Ở trang \[Current plan\] người dùng nhấn chọn \[Pay now\] 

2\. Hệ thống hiển thị trang \[Your plan\]

3\. Ở trang \[Your plan\] Người dùng chọn Billing cycle 

4\. Người dùng chọn \[Continue\]

5\. Hệ thống kiểm tra qua API stripe, có sẵn thông tin thanh toán hay chưa?

1. Nếu có: hệ thống hiển thị thông tin đã có sẵn cho người dùng   
2. Nếu không: hệ thống yêu cầu người dùng thêm thông tin thanh toán

6\. Hệ thống hiển thị Subtotal review

7\. Người dùng nhấn chọn \[Pay now\]

8\. Stripe record thông tin thanh toán, thay đổi status

9\. Hệ thống cập nhật status invoice ở trang Billing

10\. Hệ thống gửi mail xác nhận đến người dùng (Config trên Send customer email trên Stripe [https://stripe.com/docs/invoicing/send-email](https://stripe.com/docs/invoicing/send-email) )

11\. Hệ thống tự auto renew gói subscription khi tới ngày hết hạn

12\. Kết thúc use case 

## **Alternative flow 1 (upgrade plan do hệ thống dừng plan khi hết hạn trial)**

1\. Sau khi kết thúc use case \[9.1 Using free trial\] nhưng chưa có thông tin thanh toán. Người dùng nhận được đề xuất đăng ký subscription để tiếp tục sử dụng app khi vào conative (**UI: Free trial expired**)

1. Nếu đồng ý \[Yes\]: chuyển hiển thị sang trang \[purchase plan\]  
2. Nếu không \[No\]: hệ thống downgrade subscription ở strive, kết thúc use case 

2\. Ở trang \[Your plan\] Người dùng chọn Billing cycle 

3\.  Người dùng chọn \[Continue\]

4\. Hệ thống kiểm tra qua API stripe, có sẵn thông tin thanh toán hay chưa?

3. Nếu có: hệ thống hiển thị thông tin đã có sẵn cho người dùng chọn, và kèm theo “thêm thông tin thanh toán”  
4. Nếu không: hệ thống yêu cầu người dùng thêm thông tin thanh toán  
   Hệ thống verify thông tin mới qua stripe, nếu đúng chuyển sang step5. nếu không, hiển thị lỗi và yêu cầu người dùng nhập lại 

5\. Hệ thống hiển thị Subtotal review

6\. Người dùng nhấn chọn \[Pay now\]

7\. Hệ thống khởi tạo subscription ở stripe cho người dùng và tiếp tục step8

8\. Stripe record thông tin thanh toán 

9\. Hệ thống cập nhật status invoice ở trang Billing

10\. Hệ thống gửi mail xác nhận đến người dùng

11\. Hệ thống tự auto renew gói subscription khi tới ngày hết hạn

12\. Kết thúc use case 

## **Alternative flow 2 (Thanh toán qua reminder email)**

1. Người dùng nhận được 1 trong 2 mail sau:

* Stripe gửi email sắp hết hạn free trial trong đầu mỗi 7 ngày cuối của thời hạn free trial kèm CTA: Pay now   
* Stripe gửi email đã hết hạn free trial trong đầu mỗi 3 ngày cuối của thời hạn xác nhận kèm CTA: Continue using

# Automate customer emails (có sẳn template): [Link](https://stripe.com/docs/billing/revenue-recovery/customer-emails#payment-confirmation-notifications) 

2. Người dùng nhấn chọn CTA (link)

3. Xuất hiện màn hình \[Your plan\] của Conative

* Nếu đã có đăng nhập, sang bước tiếp theo  
* Nếu chưa có đăng nhập, hiện trang Log in  
4. Người dùng tiếp tục như main flow

## **Alternative flow 2: contact sales  (on hold)**

1\. Sau khi kết thúc use case \[Using free trial\] Người dùng nhận được đề xuất đăng ký subscription để tiếp tục sử dụng app 

3. Nếu đồng ý: chuyển hiển thị sang trang pricing  
4. Nếu không: kết thúc use case 

2\. Ở trang Pricing, người dùng chọn 1 trong 2 đề xuất: standard subscription và contact sales cho những gói advanced 

3\. Người dùng chọn contact sales để upgrade những gói advanced 

4\. Hệ thống hiển thị pop up contact sales và yêu cầu người dùng nhập thông tin liên hệ theo 2 cách:

1. Người dùng lựa chọn lấy thông tin từ tài khoản hiện có  
2. Người dùng nhập vào thông tin muốn nhận tư vấn 

5\. Người dùng nhấn chọn submit 

6\. Bộ phận sales liên hệ người dùng qua thông tin được cung cấp và tư vấn 

7\. Người dùng xác nhận subscription phù hợp 

8\. Hệ thống activate access cho người dùng vào phần thực hiện thanh toán subscription đã chọn 

9\. Hệ thống generate activating link và gửi người dùng qua mail 

10\. Người dùng nhấn vào link và thực hiện bước thanh toán subscription 

11\. Tiếp tục step 4 ở main flow và kết thúc use case 

**Exception cases:**

## 1\. Renew không thành công vì thẻ không đủ tiền / lỗi thẻ 

2\. Hệ thống tạm khóa access các tính năng được dùng trong subscription ở Conative và chuyển status subscription ở Stripe thành `paused`

3\. Người dùng nhận được đề xuất lỗi và  kiểm tra thẻ để tiếp tục sử dụng app khi vào conative (**UI: Renew subscription error**)

4\. Hệ thống thông báo yêu cầu đến người dùng qua mail 

5\. Người dùng nạp tiền vào thẻ hoặc kiểm tra lỗi và xác nhận lại với hệ thống 

6\. Hệ thống kiểm tra, charge tiền và setup lại subscription và payment cycle (kiểm tra cách mỗi 24h trong 1 tuần)

- Nếu không còn lỗi, tiếp tục bước tiếp theo   
- Nếu còn lỗi, quay lại bước 3 

7\. Hệ thống mở access các tính năng, người dùng tiếp tục sử dụng

## **Business Rule**

Conative admin tạo subscription:

- Duration: từ ngày tài khoản org owner được tạo mới đến “forever”  
- Set up product: standard subscription   
- Billing starting là ngày bắt đầu chuyển sáng status active  
- Free trial days: x ngày   
- Status: `active`


**Quy định phân quyền** 

Admin: có quyền xem và thao tác use case 

Member: chỉ xem được \[Current plan\], inactive \[Pay now\]

1. Chỉ cần 1 user của brand (sau này khi có phân quyền sẽ chỉ có những user có quyền mới có thể register/expand subscription) register subscription, tất cả các user thuộc org đó sẽ có thể sử dụng conative mà không cần phải register subscription khác.   
2. Khi user có status là "pending" hoặc"enable" thì User không thể đăng kí user\_sub với sub\_plan cùng id  
3. Khi gói được pay thành công thì chặn quyền \[Pay Now\] của các user còn lại 

**Quy định hiển thị và thao tác:**

1. **Page Current plan**  

| Information | Input |
| :---- | :---- |
| Have X day left to …. | Stripe API |
| Highlight features  | Stripe API |

- Nếu X\>1, hiển thị "Days"  
- Nếu X\<=1, hiển thị "Day"

**Subscription status: trialing** (Subscription statuses: [Link](https://stripe.com/docs/billing/subscriptions/overview) )

- Wording: You are currently on a Free trial   
- “x” days: trial days available  
- 

**Subscription status: incomplete, paused**

- Wording: Your free trial has expired  
- “X” days \= 0

2. **Page Your Plan**

| Information | Input |
| :---- | :---- |
| Plan’s name | Stripe API |
| Billing  | Stripe API |
| Subtotal  | Stripe API |
| Estimate taxes | Stripe API |
| Total | Stripe API |

Billing cycle bao gồm: 

- Monthly (mặc định chọn)

Billing thay đổi theo lựa chọn 

| Information | Input |
| :---- | :---- |
| Billing cycle:  Monthly (Default) Yearly (Tạm ẩn) | Stripe API |
| Price:  xxx$ per month  Xxx $ per year  | Stripe API |

Button \[Continue\] được click, chuyển sang trang \[Payment\]

Button \[Cancel\] ở trang \[Your plan\] được chọn sẽ quay lại màn hình \[Current plan\]

Text \[1. Your plan\] ở đầu trang mặc định màu xám đen, sau khi người dùng chọn \[Continue\] sang trang \[2. Payment\] thì text chuyển sang xanh lá

3. **Page Payment**

Button \[Paynow\] (mặc định Disable) chỉ được active khi các input (Billing contact, Billing address, Payment method information) pass validation 

Button \[Cancel\] ở trang \[Your plan\] được chọn sẽ quay lại màn hình \[Current plan\]

Page Checkout (Review)

| Information | Input |
| :---- | :---- |
| Plan’s name  | Stripe API |
| Subtotal  | Stripe API |
| Estimate tax | Stripe API |
| Total | Stripe API |

Page Checkout (Your Payment)

* Billing contact

| Information | Input |
| :---- | :---- |
| Full Name | Full name of Organization Admin |
| Email | Email of Organization Admin |

* Billing address:

| Information | Type | Default display | Required? | Note |
| :---- | :---- | :---- | :---- | :---- |
| Country/region | Dropdown | United State | Yes | Country/region dictionary  |
| Address | Text | Address | Yes |  |
| City | Text | City | Yes |  |
| State | Dropdown | State | Yes |  |
| Zip code  | Text | Zip code  | Yes |  |
| Business name | Text | Business name | Yes |  |

**Mặc định hiển thị:**

- Nếu đã có Billing contact (thông tin người dùng) và Billing Address (user đã nhập thông tin ở trang billing): Mặc định hiển thị sẵn thông tin, hiện CTA \[Edit\] ở đầu phải (**UI: Plan\_Payment\_1**)  
- Nếu đã có Billing contact nhưng không có Billing Address: Mặc định hiển thị form điền thông tin, điền sẵn những thông tin đã có, hiện 2 button \[Update\] và \[Cancel\] ở bên dưới (**UI: Plan\_Payment\_Edit billing address**)


CTA \[Edit\] được click vào, hệ thống show form điền thông tin cho Billing contact và Billing Address 

Disable button \[Update\] khi chưa pass validation ở Billing contact và Billing Address đến khi pass sẽ chuyển sang active. 

Button \[Cancel\] được click, hệ thống trở lại bước trước đó

* Payment method information: Card Holder Name, Card Number, cvv 

| Information | Type | Default display | Required? | Note |
| :---- | :---- | :---- | :---- | :---- |
| Payment method |  | Mastercard | Yes | chọn thẻ theo avatar, các thẻ được sử dụng: link below |
| Expiration date | Date |  | Yes |  |
| Card number  | Number |  | Yes | Hidden input |
| CVV | Number |  | Yes | Hidden input |

**Accepted card: [Link](https://stripe.com/docs/payments/cards/supported-card-brands)**

Visa, Mastercard, American Express, Discover & Diners Club, China UnionPay, Japan Credit Bureau (JCB)

**Mặc định hiển thị:**

- Nếu đã có Payment method, hệ thống mặc định hiển thị thông tin thẻ có sẵn (hiển thị hết) dưới dạng mask (Payment method \- hiện thẻ, Card number \- chỉ hiện 4 số cuối lấy từ API Stripe, CVV), hiện CTA \[Edit\] ở đầu phải (**UI: Plan\_Payment\_Filled infprmation**)  
- Nếu chưa có Payment method, hệ thống mặc định hiển thị form điền thông tin, hiện button \[Save payment method\] (**UI:Plan\_Payment\_1**)

CTA \[Edit\] được click vào, hệ thống show form điền thông tin cho Payment method 

Disable button \[Save payment method\] khi chưa pass validation ở Payment method input đến khi pass sẽ chuyển sang active. Button được click, hệ thống lưu lại Payment method vào Billing Information. Hệ thống kiểm tra:

* Nếu chưa có payment method nào trong Billing Information, lưu thông tin thẻ vừa add vào và set là primary payment method  
* Nếu đã có 1 payment method (primary payment method) trong Billing Information, lưu thông tin thẻ vừa add vào và set là secondary payment method

4. **Renew subscription error**

Button \[Change payment method\] được click, hệ thống chuyển đến màn hình billing information và tiếp tục UC 9.3

**Quy định khác** 

Gói subscription được renew thành công: thông tin billing được cập nhật tương ứng trong phần Billing

# **UC9.3. Add payment method in Billing page**

## **Mục tiêu**

Người dùng có thể thêm hoặc chỉnh sửa phương thức thanh toán 

## **Input**

Billing address: country/region, address, city, state, ZIP code, Business name 

Payment method information: Card Number, Expiration date, CVV 

## **Output**

Hệ thống cập nhật thêm hoặc chỉnh sửa phương thức thanh toán của người dùng 

## **Workflow**

### **Main flow**

1\. Người dùng chọn \[Plan & Billing\] \> \[Billing information\] từ Admin menu

2\. Hệ thống kiểm tra tài khoản đăng nhập có phải Org owner hay không 

1. Nếu đúng: hệ thống hiển thị mục payment method  
2. Nếu sai: hệ thống không hiển thị mục payment method cho người dùng 

3\. Ở trang Billing, người dùng chọn thêm thông tin thanh toán 

4\. Hệ thống yêu cầu người dùng thêm thông tin thanh toán

5\. Hệ thống verify thông tin mới qua stripe, nếu đúng chuyển sang step6. nếu không, hiển thị lỗi và yêu cầu người dùng nhập lại 

6\. Stripe record thông tin thanh toán 

7\. Hệ thống update và hiển thị thông tin mới 

8\. Kết thúc use case 

## **Alternative flow**

3\. Ở trang Billing, người dùng chọn thêm thông tin thanh toán 

4\. Hệ thống yêu cầu người dùng cập nhật thông tin thanh toán mới 

5\. Hệ thống verify thông tin mới qua stripe, nếu đúng chuyển sang step6. nếu không, hiển thị lỗi và yêu cầu người dùng nhập lại 

6\. Stripe record thay thế thông tin thanh toán cũ bằng thông tin mới 

7\. Hệ thống update và hiển thị thông tin mới 

8\. Kết thúc use case 

## **Business Rule**

1/ Thông tin thanh toán bao gồm:

Billing address: 

| Information | Type | Default display | Required? | Note |
| :---- | :---- | :---- | :---- | :---- |
| Country/region | Dropdown | United State | Yes |  |
| Address | Text | Address | Yes |  |
| City | Text | City | Yes |  |
| State | Dropdown | State | Yes |  |
| Zip code  | Text | Zip code  | Yes |  |
| Business name | Text | Business name | Yes |  |

Payment method information: Card Holder Name, Card Number, cvv 

| Information | Type | Default display | Required? | Note |
| :---- | :---- | :---- | :---- | :---- |
| Card holder name | Text |  | Yes |  |
| Card number  | Number |  | Yes | Hidden input |
| CVV | Number |  | Yes | Hidden input |

2/ Payment method: có tối đa 2 method và chỉ hiển thị 4 số cuối (lấy từ API Stripe)  

# **UC 9.4. Cancel subscription plan** 

## **Mục tiêu**

Người dùng có thể hủy gói Sub hiện tại

## **Input**

## **Output**

Hệ thống kết thúc gói plan hiện tại của user

## **Workflow**

### **Main flow**

1\. Người dùng chọn \[Plan & Billing\] \> \[My plan\] từ Admin menu, Ở trang \[Current plan\] người dùng nhấn chọn CTA \[Cancel plan\] 

2\. Hệ thống hiển thị chi tiết thông tin plan, và ngày kết thúc cycle hiện tại

3\. Người dùng xác nhận yêu cầu hủy

4\. Downgrade trong cycle tiếp theo trên Stripe, thay đổi status

5\. Hệ thống tắt access của user cho các tính năng

6\. Hệ thống hiển thị trang \[Current plan\] và cập nhật UI \[Plan\_Free trial\_Cancelled\]

7\. Stripe gửi email hủy thành công cho user 

## **Alternative flow**

1\.  Sau khi kết thúc use case \[9.1 Using free trial\] nhưng chưa có thông tin thanh toán. Người dùng nhận được đề xuất đăng ký subscription để tiếp tục sử dụng app khi vào conative (**UI: Free trial expired**)

- Nếu đồng ý \[Yes\]: chuyển hiển thị sang trang \[purchase plan\]  
- Nếu không \[No\]: tiếp tục bước 4 ở main flow, kết thúc use case

## **Exceptional flow (Cancel không thành công)**

## **Business Rule**

# **UC 9.5. View and export billing history** 

## **Mục tiêu**

Người dùng có thể xem thông tin lịch sử billing

## **Input**

## **Output**

Hệ thống hiển thị thông tin lịch sử billing

## **Workflow**

### **Main flow**

1. Người dùng chọn \[Plan & Billing\] \> \[Billing history\] từ Admin menu  
2. Hệ thống kiểm tra dữ liệu  
- Không có dữ liệu Billing, hệ thống hiển thị No billing history  
- Có dữ liệu, đến bước tiếp theo  
3. Hệ thống hiển thị list các thông tin billing đã được thực hiện  
4. Người dùng chọn CTA \[View detail\]  
5. Hệ thống xuất và download invoice về máy của user  
6. Kết thúc Usecase 

## **Business Rule**

Template invoice (view detail)  

### **Quy định phân quyền**

User thực hiện use case này phải có role: 

- Admin của organization đó 

### **Quy định hiển thị và thao tác** 

Danh sách report 

Mặc định hiển thị các Billing history template của Conative, bao gồm: 

1. Invoice   
2. Status   
3. Plan   
4. Billing date   
5. Amount   
6. Action: view detail 

| Field | Display | Required? | Description |
| :---- | :---- | :---- | :---- |
| Invoice | Number  | Yes | Invoice No.  |
| Status |  | Yes | Status Categories:  |
| Plan  | Text | Yes | Plan name |
| Billing date  | Date | Yes | Date that event happened  |
| Amount  | Currency  | Yes | Payment subtotal  |
| Action View detail  | CTA  |  |  |

# **UC 9.6. Discount**  

## **Mục tiêu**

Người dùng có thể nhập discount code để mua gói giảm giá

## **Input**

## **Output**

Hệ thống xử lý discount code để mua gói giảm giá

## **Workflow**

### **Main flow**

1. # Tại trang \[Your plan\], người dùng nhập mã vào \[insert your coupon code\]

2. # Người dùng nhấn chọn button \[Apply\]

3. Hệ thống kiểm tra coupon code  
- Nếu đúng: hệ thống hiển thị thông tin ở phần \[Discount\]  
- Nếu sai: hệ thống hiện lỗi. Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)  
4. Người dùng nhập thêm code?  
- Nếu đúng: Quay lại bước 1  
- Nếu sai: Tiếp tục bước tiếp theo  
5. Người dùng tiếp tục thanh toán ở UC 9.2

## **Business Rule**  

1. **Quy định hiển thị \[Discount\]**

| Coupon’s name  | Stripe API |
| :---- | :---- |
| Discount price | Stripe API |
| Subtotal  | Stripe API |

# **UC 10.1. View PO list**

## **Mục tiêu**

User xem được danh sách Purchase order được sync từ ERP (Shiphero, Netsuite,...) hoặc được tạo trên Conative 

## **Input** 

PO created in Conative 

PO sync from ERP

Search PO

Filter PO

## **Output**

Danh sách PO & các field

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | PO Number (Conative) | The number of PO on Conative. Both PO created on Conative or sync from ERP will have a unique PO number (Different from PO id / number from ERP) | **Rule:**  Conative generates PO number, tiền tố C \- Tối thiểu 5 số (VD: C00001) **Sort**:  Sort A-Z và ngược lại  |
| 2 | Vendor / Supplier  | Vendor / Supplier that user sends PO to. Vendors are created on Conative or sync from Shopify, ERP.  | **Sort**  Sort A-Z và ngược lại  |
| 3 | Warehouse | Warehouse that stores PO items in PO | **Status**  Đối với warehouse sync từ Shopify hoặc ERP, chỉ hiển thị warehouse  có status \= **Active Sort**  Sort A-Z và ngược lại  |
| 4 | Created date (Generated date old system) | Created date of PO  | **Format** “10 Aug, 2023” **Sort**  Sort A-Z và ngược lại  |
| 5 | Expected arrival date | Expected arrival date of the PO | **Format** “10 Aug, 2023” **Sort**  Sort A-Z và ngược lại  |
| 6 | Received status | Number of items received in the PO | **Format  “**X of Y”  X: Number of item received Y: Total number of item in PO ***Highlight colors*** Received quantity \< Order quantity: Màu cam Received quantity \= Order quantity: Màu xanh Received quantity \= 0: Màu xám |

## 

## **Workflow** 

### **Main flow (Happy case)** 

1\. Trên sidebar menu, chọn \[Purchase Order\] 

2\. Hệ thống hiển thị danh sách PO theo các filter mặc định (Tham chiếu UC 10.4 Filter PO)

3\. Tùy chỉnh filter để lấy danh sách PO theo điều kiện mong muốn (Tham chiếu UC 10.4 Filter PO)

5\. Kết thúc Use case 

**Business Rule** 

**Quy định hiển thị và thao tác** 

**PO list**

- Mặc định sort theo PO mới nhất nằm trên cùng

**PO Status** 

| Status  | Status (DB) | Business Rules |
| :---- | :---- | :---- |
| **Draft** (Skip trong đợt release này) | **Pending** | PO has status \= **Draft** when user \[Save as Draft\]  On order & Arrival date from draft PO is not sync with data in other reports on Conative  |
| **Open** | **Accepted** | PO has status \= **Open** when user \[Create new\] successfully.  On order & Arrival date from draft PO is sync with data in other reports on Conative  PO is editable  |
| **Canceled** (Skip trong đợt release này) | **Canceled** | PO has status \= **Canceled** when user \[Create new\] successfully.  On order & Arrival date from draft PO is not sync with data in other reports on Conative  PO is not editable |
| **Closed** | **Closed** | PO has status \= **Closed** when user \[Create new\] successfully.  On order & Arrival date from draft PO is sync with data in other reports on Conative  PO is not editable |

# 

# **UC 10.2 View PO Detail**

## **Mục tiêu**

User có thể xem chi tiết PO, PO items, order quantity, received status… của 1 PO

## **Input** 

Chọn PO bất kỳ đã tạo trên Conative hoặc được sync về từ ERP

## **Output** 

PO detail bao gồm các field

Source 

PO number 

PO id

Created date 

Expected Arrival date 

Vendor 

Warehouse 

Order item (PO items)

Receive today

Note for PO

## **Workflow** 

### **Mainflow** 

1. Trên danh sách PO, chọn PO bất kỳ  
2. Hệ thống hiển thị popup PO detail của PO đó   
3. Kết thúc UC

## **Business rule** 

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | PO Number | The number of PO on Conative.  | **Rule:**  Conative generates PO number, tiền tố C \- Tối thiểu 5 số (VD: C00001) Bắt buộc nhập Cho phép user edit Cho phép user copy |
| 2 | PO ID | The id of PO on Conative | **Rule:**  PO created on Conative: Conative generate PO sync from erp: Use PO id from erp Không cho phép edit  Cho phép user copy |
| 3 | Vendor | Vendor / Supplier that user sends PO to. Vendors are created on Conative or sync from Shopify, ERP. | **Rule** Mặc định hiển thị vendor đã chọn khi create new PO (Tham chiếu UC 10.5 Create new PO) Cho edit |
| 4 | Created date (Generated date old system) | Created date of PO  | **Rule**  Ngày tạo PO Không cho edit **Format** “10 Aug, 2023” |
| 5 | Expected arrival date | Expected arrival date of the PO | **Rule**  Mặc định hiển thị vendor đã chọn khi create new PO (Tham chiếu UC 10.5 Create new PO) Cho edit Expected arrival date \>= Today **Format** “10 Aug, 2023” **Sort**  Sort A-Z và ngược lại  |
|  | Warehouse | Warehouse that stores variants in PO | **Rule**  Mặc định hiển thị warehouse đã chọn khi create new PO (Tham chiếu UC 10.5 Create new PO) Cho edit Bắt buộc nhập |
|  |  |  |  |

**Variant table**

Mặc định hiển thị PO items được update lần gần nhất của PO đó

**\[Add\] button**

- Mặc định disable  
- Enable khi user đã chọn SKU để thêm vào PO


**Edit order quantity** 

- Min quantity \= 1  
- Chọn \[+\] để tăng 1, chọn \[-\] để giảm 1


**Add new variant \- Search bar**

- Mặc định rỗng   
- Hiển thị \[x\] để xóa SKU / variant title khỏi search bar sau khi user nhập keyword search bất kỳ  
- Hệ thống hiển thị dropdown các kết quả trả về theo keyword search. Hiển thị max 6 kết quả, nếu nhiều hơn thì user scroll dropdown


**Note field** 

- Mặc định hiển thị note update lần gần nhất   
- Cho phép nhập text


**Variant checkbox**

- Ô checkbox của từng variant sẽ hiển thị ![][image2] khi user chọn variant   
- Ô checkbox All sẽ hiển thị ![][image3] nếu user select từng variant, hiển thị số lượng variant được selected (**\<number\> selected)**    
- Ô checkbox All sẽ hiển thị ![][image2]khi user chọn all, hiển thị số lượng variant ở trang hiện tại (**\<number\> selected)** 

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | SKU |  |  |
| 2 | Product title  |  |  |
| 3 | Variant title |  |  |
| 4 | Stock |  |  |
| 5 | On order  |  |  |
| 6 | Order quantity |  |  |
| 7 | Received today | Quantity of PO items that were received today.  | **Rules** Default value \= 0 Cho phép user nhập (Chỉ nhập số nguyên) Received quantity Value \<= On order value Chỉ lưu giá trị user nhập trong ngày, luôn reset về 0 mỗi ngày  Hiển thị CTA \[Save\] bên cạnh field khi user nhập. |

## 

# **UC 10.2. Archive PO (Pending)**

## **Mục tiêu**

Thay đổi status PO từ Open \> Archived, remove khỏi list PO đang Open

## **Input**

PO Status

## **Output**

Change PO status, Remove **archived PO from Open PO list** 

## **Workflow**

### **Main flow (happy case)**

1\. Trên trang PO list, user tìm PO cần archive, chọn dropdown \[Archive\]

2\. Hệ thống đổi status PO và remove PO archive khỏi danh sách Open PO

3\. User chọn \[Show archived PO\] để xem các PO archived

4\. Hệ thống hiển thị danh sách Archived PO 

## **Business Rule**

# **UC 10.4. Search PO**

## **Mục tiêu**

User có thể tìm kiếm PO bằng PO number  

## **Input**

PO number

PO item

## **Output**

Trả data theo UC 10.1

## **Workflow**

### **Main flow**

1. Trên trang Purchase Order, user bấm \[Search bar\] và nhập PO number / PO id / SKU để tìm kiếm PO chứa thông tin liên quan.

2. Hệ thống trả về danh sách PO theo điều kiện tìm kiếm: 

   1. Tìm thấy kết quả: Trả danh sách PO tương ứng 

   2. Không tìm thấy lết quả: trả về thông báo không thấy kết quả

3. Kết thúc use case

## **Business Rule**

### **Quy định hiển thị và thao tác**

- Tìm kiếm theo PO number  
  - search gần đúng  
- Tìm kiếm theo PO id   
  - search gần đúng   
- Tìm kiếm theo SKU  
  - search gần đúng (Hiển thị các PO chứa PO line item là các sku tương ứng)

Thông báo khi không tìm thấy PO khớp với điều kiện tìm kiếm:  
**You don't have any purchase order yet**

## **References** 

Design: [https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative\_New?type=design\&node-id=2170-71450\&mode=design\&t=Ne2NXWKyDomAtUNc-4](https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative_New?type=design&node-id=2170-71450&mode=design&t=Ne2NXWKyDomAtUNc-4)

# **UC 10.5. Filter PO**

## **Mục tiêu**

User có thể filter PO theo Source, Warehouse, Vendor 

## **Input**

Source

Warehouse 

Vendor

## **Output**

Trả data theo UC 10.1

## **Workflow**

### **Main flow**

1\. Trên sidebar menu, chọn \[Purchase Order\] 

2\. Hệ thống hiển thị danh sách PO đã được tạo 

3\. Chọn Quick filter Warehouse, Vendor, Status

4\. Hệ thống kiểm trả thông tin và trả về danh sách PO theo kết quả filter

5\. Kết thúc Use case

### 

### **Exceptional flow**

4\. Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

5\. Kết thúc use case.

## **Business Rule**

### **Quy định hiển thị và thao tác**

| Filters (Fields) | Conditions (Operators) | Filter value | Types |
| ----- | ----- | ----- | ----- |
| **Source**  | Is (Equal) | Conative (Mặc định) ERPs | Single selection |
| **Warehouse** | Is (Equal) | List of warehouse sync from Shopify / ERP  Mặc định (All warehouse) | Multiple selection |
| **Vendor / Supplier** | Is Is not | List of vendor created on Conative  sync from Shopify / ERP Mặc định (All supplier) | Multiple selection |
| **Status**  | Is (Equal) | Archived Unarchived | Single selection |

# **UC 10.6.1 Create new PO (Manual)**	

## **Mục tiêu**

User tạo PO mới trên Conative. On Order data của PO item sẽ đồng bộ trên các report của Conative.

## **Input**

PO Number 

Created date 

Expected arrival date 

Warehouse 

Variant

Save draft PO (Save as draft) **(Phân tích, triển khai sau 2/9)**

## **Output**

Conative tạo PO mới 

## **Workflow**

### **Mainflow**

1. User chọn \[Create New\] / \[Create New PO\] (CTA khi chưa có PO nào) ở trang Purchase order list

2. Hệ thống hiển thị dropdown để user chọn \[New PO\] / \[Upload PO\]

3. User chọn \[New PO\]

4. User chọn vendor / supplier hoặc tạo vendor / supplier mới trong Conative để thêm vào PO.

   1. Đối  với vendor tạo mới trong Conative, user chọn \[Add new vendor\] trong dropdown vendor list

   2. User nhập tên vendor và chọn \[Add\] để thêm vendor vào vendor list, \[Cancel\] để hủy thao tác, 

   3. Sau khi user add vendor, hệ thống add vendor vào vendor list và cập nhật vendor đó cho PO

5. User chọn expected arrival date cho PO.

6. User chọn warehouse để nhập hàng 

7. User add variant vào PO và chọn số lượng item cho mỗi variant / remove variant

8. User chọn \[Create new\]

9. Hệ thống validate những thông tin và thông báo

- Nếu đúng: tạo PO, thông báo user đã tạo PO thành công 

- Nếu không: hiển thị lỗi và yêu cầu người dùng nhập lại 

10. Kết thúc Use case 

## **~~Alternative flow 2 (add CSV file) \- (Phân tích, triển khai sau 2/9)~~**

1. ~~11.User chọn \[Create New PO\] ở trang Purchase order list~~

2. ~~Hệ thống hiển thị popup để user chọn \[New PO\] / \[Upload PO\]~~

3. ~~User chọn \[Upload PO\]~~

4. ~~Người dùng chọn Upload CSV file và chọn file cần import~~ 

5. ~~Hệ thống hiển thị Mapping column~~ 

6. ~~Hệ thống collect các attribute (cột) trong CSV file và cập nhật ở dropdown list~~ 

7. ~~Người dùng match đúng attribute (ở drop down list) vào SKU và Order Quantity~~

8. ~~Người dùng chọn \[Create PO\]~~

9. ~~Hệ thống validate những input thông tin~~  

- ~~Nếu đúng: tiếp tục bước sau~~ 

- ~~Nếu không: hiển thị lỗi và yêu cầu người dùng nhập lại~~ 

10. ~~Hệ thống validate CSV input~~ 

- ~~Nếu đúng: Hệ thống tạo PO và hiển thị trang chi tiết của PO~~ 

- ~~Nếu sai: Hệ thống báo lỗi ở trang pop up và hiển thị button \[Back to Purchase order\], người dùng chọn \[Back to Purchase order\] để quay lại trang PO~~

11. ~~Kết thúc Use case~~ 

    

## **Business Rule**

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | PO Number | The number of PO on Conative.  | **Rule:**  Conative generates PO number, tiền tố C \- Tối thiểu 5 số (VD: C00001) Bắt buộc nhập Cho phép user edit Cho phép user copy |
| 2 | PO ID | The id of PO on Conative | **Rule:**  PO created on Conative: Conative generate PO sync from erp: Use PO id from erp Không cho phép edit  Cho phép user copy |
| 3 | Vendor / Supplier | Vendor / Supplier that user sends PO to. Vendors are created on Conative or sync from Shopify, ERP. | **Rule** Mặc định rỗng  Bắt buộc nhập Hiển thị dropdown supplier list bao gồm supplier được tạo trên Conative, Shopify, ERP theo A-Z Cho phép chọn 1 Cho phép create new supplier  |
| 4 | Created date (Generated date old system) | Created date of PO  | **Rule**  Ngày tạo PO Không cho edit **Format** “10 Aug, 2023” |
| 5 | Expected arrival date | Expected arrival date of the PO | **Rule**  Mặc định rỗng  Bắt buộc nhập Cho edit Expected arrival date \>= Today **Format** “10 Aug, 2023” **Sort**  Sort A-Z và ngược lại  |
|  | Warehouse | Warehouse that stores variants in PO | **Rule**  Mặc định rỗng Bắt buộc nhập Lấy list warehouse status \= **active** từ Shopify, ERP Hiển thị dropdown warehouse list sync từ Shopify, ERP, theo A-Z Cho phép chọn 1 |

**Variant table**

Mặc định hiển thị “No data” khi chưa có product được add

Bắt buộc có product

**\[Add\] button**

- Mặc định disable  
- Enable khi user đã chọn SKU


**Edit order quantity** 

- Min quantity \= 1  
- Chọn \[+\] để tăng 1, chọn \[-\] để giảm 1


**Add new variant \- Search bar**

- Mặc định rỗng   
- Cho phép search tương đối theo SKU, variant title  
- Hiển thị \[x\] để xóa SKU / variant title khỏi search bar sau khi user nhập keyword search bất kỳ  
- Hệ thống hiển thị dropdown các kết quả trả về theo keyword search. Hiển thị max 6 kết quả, nếu nhiều hơn thì user scroll dropdown  
- Không được add trùng variant đã add trước đó. Nếu add trùng sẽ báo lỗi  
- Chỉ search được variant đang active trên Shopify


**Note field** 

- Mặc định rỗng  
- Cho phép nhập text  
- Max length \= 300 characters


**Variant checkbox**

- Ô checkbox của từng variant sẽ hiển thị ![][image2] khi user chọn variant   
- Ô checkbox All sẽ hiển thị ![][image3] nếu user select từng variant, hiển thị số lượng variant được selected (**\<number\> selected)**    
- Ô checkbox All sẽ hiển thị ![][image2]khi user chọn all, hiển thị số lượng variant ở trang hiện tại (**\<number\> selected)** 

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | SKU | Variant SKU |  |
| 2 | Product title  |  |  |
| 3 | Variant title |  |  |
| 4 | Stock |  |  |
| 5 | On order  |  |  |
| 6 | Order quantity |  | **Rule:**  Hiển thị mặc định  Cho phép edit  Chọn \[Add\] để thêm variant & order quantity vào PO |

## **References**

Design: [https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative\_New?type=design\&node-id=1947-70596\&mode=design\&t=RIFEMl8BZsDcdg5p-4](https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative_New?type=design&node-id=1947-70596&mode=design&t=RIFEMl8BZsDcdg5p-4)

# **UC 10.6.2 Upload PO**

## **Mục tiêu**

User tạo PO mới trên Conative. On Order data của PO item sẽ đồng bộ trên các report của Conative.

## **Input**

PO Number 

Expected arrival date 

Warehouse 

Vendor

CSV

## **Ouput**

Upload PO successfully 

## **Main flow**

1. User chọn \[Create New\] ở trang Purchase order list

2. Hệ thống hiển thị popup để user chọn \[New PO\] / \[Upload PO\]

3. User chọn \[Upload PO\]

4. Hệ thống hiển thị drawer

5. User nhập / chọn thông tin 

   1. Vendor 

   2. Expected date 

   3. Warehouse (location to receive stock)

6. Hệ thống validate những input thông tin  

- Nếu đúng: tiếp tục bước sau 

- Nếu không: hiển thị lỗi và yêu cầu người dùng nhập lại 

7. User download file PO template

8. Người dùng bấm \[+\] chọn Upload CSV file và chọn file cần upload ở mục \[File\]

9. Người dùng chọn file upload

10. Hệ thống validate định dạng file thành công

11. Hệ thống hiển thị \[Mapping Column\] 

12. Hệ thống mặc định mapping bằng field Variant id và Order quantity

13. User có thể chọn map bằng SKU (có khả năng gây lệch dữ liệu do SKU không unique) và chọn lại cột cần map trên file CSV trong dropdown list

14. Người dùng chọn   
- \[Upload PO\]: tiếp tục bước tiếp theo  
- \[Cancel\]: Hệ thống quay về trang PO

15. Hệ thống validate CSV input và hiển thị progress upload, số lượng variant upload thành công, số lượng variant upload không thành công 

16. User chọn \[View PO\] 

17. Hệ thống hiển thị popup PO chi tiết

18. Kết thúc UC 

## **Business Rule**

1. Quy định hiển thị: 

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | Vendor / Supplier | Vendor / Supplier that user sends PO to. Vendors are created on Conative or sync from Shopify, ERP. | **Rule** Mặc định rỗng  Bắt buộc nhập Hiển thị dropdown supplier list bao gồm supplier được tạo trên Conative, Shopify, ERP theo A-Z Cho phép chọn 1 Cho phép create new supplier  |
| 2 | Created date (Generated date old system) | Created date of PO  | **Rule**  Ngày tạo PO Tự generate, không cho edit **Format** “10 Aug, 2023” |
| 3 | Expected arrival date | Expected arrival date of the PO | **Rule**  Mặc định rỗng  Bắt buộc nhập Cho edit Expected arrival date \>= Today **Format** “10 Aug, 2023” **Sort**  Sort A-Z và ngược lại  |
| 4 | Warehouse  | Warehouse that stores variants in PO | **Rule**  Mặc định rỗng Bắt buộc nhập Lấy list warehouse status \= **active** từ Shopify, ERP Hiển thị dropdown warehouse list sync từ Shopify, ERP, theo A-Z Cho phép chọn 1 |

**PO csv template:**

- [Link](https://docs.google.com/spreadsheets/d/1tCQORguWXmJLl4KSdV-yVh6s_cFFPsuPd1sihgsmhuU/edit?usp=sharing)

\[CTA & Bar\] Select file to upload

- \[File selection\]: 

| Khi chưa có file  | Khi đã tải file  |
| :---- | :---- |
| No file selected  | File\_name  |

- CTA \[+\]: Người dùng nhấn chọn để tải file lên hệ thống


Mapping columns:

- Dropdown để user chọn mapping bằng field Variant ID hoặc SKU. Chỉ được chọn map bằng 1 trong 2 field. 

- Dropdown ở mục **Select Column from your file** để map với cột mong muốn


| Variant\_id / SKU (dropdown) | Mặc định map bằng Variant ID. User có thể chọn map bằng SKU Mục Column in your file Field variant id được mặc định map với cột đầu tiên của file upload  Dropdown list gồm các cột có header trong file upload Bắt buộc nhập   |
| :---- | :---- |
| order\_quantity | \- Field order quantity được mặc định map với cột thứ 3 của file upload  Mục Column in your file Field variant id được mặc định map với cột đầu tiên của file upload  Dropdown list gồm các cột có header trong file upload Bắt buộc nhập  |


Hệ thống kiểm tra các product được upload: X, Y được tính sau khi hệ thống check 

- The system successfully imported \[X\] products   
- The system failed to import \[Y\] products 

Hệ thống báo lỗi ở \[Error log\] Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

| ~~Error~~ | ~~Message~~ |
| :---- | :---- |
| ~~Missing SKU~~  | ~~Missing SKU value in line \[X\](, \[Y\], \[Z\])  in the uploaded file can not be found in the system~~ |
| ~~Duplicated SKU~~  | ~~Have duplicated SKU in the uploaded file~~  |
| ~~Order quantity invalid (không phải số/ value \<0)~~  | ~~Order quantity value in line \[X\](, \[Y\], \[Z\]) is invalid~~  |
| ~~Status của variant ở shopify khác active~~  | ~~Variant \[X\](, \[Y\], \[Z\]) status in shopify is/are inactive  Note: ít variant id \=\> is, nhiều variant id \=\> are~~  |

2. 

# **UC 10.7.1 Edit PO \- Receive PO item (PO created on Conative only)**

## **Mục tiêu**

Đối với PO được tạo trên Conative: User có thể ghi nhận nhập kho những item trên từng PO, cho phép fully receive hoặc partially receive.

Đối với PO được đồng bộ từ WMS (Warehouse Management System) hoặc ERP: Conative đồng bộ dữ liệu PO từ WMS /ERP. User chỉ xem các thông tin receive nhập kho của các PO item, không có quyền chỉnh sửa.

## **Input**

Chọn quantity receive

## **Output**

Hệ thống cập nhật số lượng PO item đã receive

Cập nhật status cho PO item

## **Workflow**

**Main flow (Fully receive for all PO items in 1 PO)**

1. User chọn 1 PO bất kỳ có status \= **Open / Draft**

2. Hệ thống hiển thị Popup PO detail

3. User chọn \[Receive\]

4. Hệ thống cập nhật received quantity và On order quantity, cập nhật status của PO item \= Fully received

5. Hệ thống cập nhật dữ liệu và cập nhật trang PO. Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

6. Kết thúc Use case 

### **Alternative flow \- Partially Receive cho 1 PO item**

1. User chọn 1 PO bất kỳ status \= **Open / Draft**

2. Hệ thống hiển thị Popup PO detail

3. User chọn 1 PO item bất kỳ trong PO, nhập số lượng item muốn Receive ở field Received today

4. User chọn icon \[Save\] để lưu

5. Hệ thống kiểm tra thông tin hợp lệ, sau đó cập nhật On order data & Received quantity và thông báo. Tham chiếu message ở file [Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

### **Alternative flow \- Receive cho nhiều PO item**

1. User chọn 1 PO bất kỳ status \= **Open / Draft**

2. Hệ thống hiển thị Popup PO detail

3. User chọn 1 hoặc nhiều PO item bất kỳ trong PO

4. Hệ thống hiển thị số lượng variant đã chọn và bulk action \[Receive\] 

5. User chọn \[Receive\] để nhận hàng cho các PO item đã chọn. 

6. Hệ thống kiểm tra thông tin hợp lệ, sau đó cập nhật On order data & Received quantity và thông báo. Tham chiếu message ở file [Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

## **Business Rule**

### **Quy định hiển thị và thao tác** 

**PO item status:** 

- Fully received: Received quantity (Không phải received today)= On order 

- Partially received: Received quantity \< On order

- Unreceived: Received quantity \= 0

**On Order**

- Default value \= Order quantity

- Khi user update Received today, On order data \- Received today

- Total On order value (for all PO items) thay đổi theo On order của từng PO item

**Field Received Quantity**

- Default value \= 0

- Cho phép user nhập (Chỉ nhập số nguyên)

- Hiển thị CTA \[Save\] bên cạnh field khi user nhập 

**Status** (Received status of the line item): 

- **Over received**: quantity received \> ordered quantity   
- **Received**: quantity received \= order quantity  
- **Under received**: quantity received \< ordered quantity   
- **Not received**: Quantity received \= 0

**CTA** \[**Save**\]

- Mặc định ẩn

- Hiển thị khi user nhập số vào field **Receive today**

**Popup** \[**Leave site**\] (Trước là Popup Save PO)

- Hiển thị khi user nhập số vào field **Receive today**, sau đó chọn \[x\] đóng trang PO detail mà không save 

- Chọn \[Leave\] để đóng PO detail, không lưu thông tin đã nhập và quay về trang PO list

**Variant Checkbox** 

- Mặc định hiển thị ![][image4]  
- Ô checkbox của từng variant sẽ hiển thị ![][image5]khi user chọn variant   
- Ô checkbox All sẽ hiển thị ![][image6]nếu user select từng variant, hiển thị số lượng variant được selected (**\<number\> selected)**  và CTA \[select all variant in store\]  
- Ô checkbox All sẽ hiển thị ![][image5]khi user chọn all, hiển thị số lượng variant ở trang hiện tại (**\<number\> selected)** và CTA \[select all variant in store\]

# **UC 10.7.2 Edit PO \- Update Vendor (PO created on Conative only)**

## **Mục tiêu**

Đối với PO được tạo trên Conative: User có thể cập nhật Vendor đối với PO draft

Đối với PO được đồng bộ từ WMS (Warehouse Management System) hoặc ERP: Conative đồng bộ dữ liệu PO từ WMS /ERP. User chỉ xem thông tin PO, không có quyền chỉnh sửa.

## **Input**

Chọn quantity receive

## **Output**

Hệ thống cập nhật Vendor 

**Workflow** 

**Mainflow** 

1. User chọn 1 PO bất kỳ có status \= Draft

2. Hệ thống hiển thị Popup PO detail

3. User chọn  \[Vendor\] 

4. Hệ thống hiển thị dropdown vendor list

5. User chọn vendor / supplier hoặc tạo vendor / supplier mới trong Conative 

   1. Đối  với vendor tạo mới trong Conative, user chọn \[Add new vendor\] trong dropdown vendor list

   2. User nhập tên vendor và chọn \[Add\] để thêm vendor vào vendor list, \[Cancel\] để hủy thao tác, 

   3. Sau khi user add vendor, hệ thống add vendor vào vendor list và cập nhật vendor đó cho PO2

6. Hệ thống cập nhật dữ liệu và cập nhật trang PO. Tham chiếu message ở file [Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

7. Kết thúc Use case 

**Business Rule** 

**Quy định phân quyền** 

PO status \= Draft

# **UC 10.7.3 Edit PO \- Update Warehouse (PO created on Conative only)**

## **Mục tiêu**

Đối với PO được tạo trên Conative: User có thể cập nhật Vendor đối với PO draft

Đối với PO được đồng bộ từ WMS (Warehosue Management System) hoặc ERP: Conative đồng bộ dữ liệu PO từ WMS /ERP. User chỉ xem thông tin PO, không có quyền chỉnh sửa.

## **Input**

Chọn quantity receive

## **Output**

Hệ thống cập nhật Vendor 

## **Workflow** 

### **Mainflow** 

1. User chọn 1 PO bất kỳ có status \= Draft

2. Hệ thống hiển thị Popup PO detail

3. User chọn  \[Warehouse\] 

4. Hệ thống hiển thị dropdown vendor list

5. User chọn warehouse đồng bộ từ Shopify hoặc ERP

6. Hệ thống cập nhật dữ liệu và cập nhật trang PO. Tham chiếu message ở file [Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

7. Kết thúc Use case 

## **Business Rule** 

**Quy định phân quyền** 

PO status \= Draft

# **UC 10.8. Export PO**

## **Mục tiêu**

User tải PO định dạng PDF hoặc định dạng csv

## **Input**

## **Output**

Export file PDF

Export file CSv

## **Workflow** 

**Main flow:** 

1. Người dùng chọn phương thức tải dữ liệu ở trang chi tiết PO

- Download PDF

- Download CSV

2. Hệ thống validate dữ liệu 

- Nếu có dữ liệu: tiếp tục bước sau 

- Nếu trống: hiển thị lỗi 

3. Hệ thống xuất list sản phẩm ở trang chi tiết PO theo đúng phương thức

4. Kết thúc Use case 

## **Business Rule**

|  | Field | Type | File name | Format |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Download PDF  | PDF | Purchase\_Order\_\<PO number\> |  |
| 2 | Download CSV  | CSV  | Purchase\_Order\_\<PO number\> | [Purchase\_Order\_\<PO Number\>](https://docs.google.com/spreadsheets/d/1-pRtVyGkmEvxmFwxE4LcsDI_weVvQQKkQtw0xfqeJzE/edit#gid=0) |

# **UC 10.9. Delete PO** 

## **Mục tiêu**

Người dùng có thể xóa PO trên Conative (Chỉ áp dụng với PO được tạo trên Conative)

## **Input**

## **Output**

PO được xóa khỏi hệ thống 

## **Workflow**

**Main flow:**

1. Người dùng chọn \[Delete PO\] tại trang chi tiết của PO

2. Hệ thống hiển thị pop up xác nhận xóa 

3. Người dùng xác nhận

- Nếu xác nhận: nhấn vào \[Delete\] hiển thị trang PO

- Nếu không thì nhấn \[Cancel\], hiển thị quay lại trang chi tiết của PO

4. Hệ thống xóa dữ liệu PO và cập nhật trang PO

5. Kết thúc Use case 

**Alternative flow**:

1\. Người dùng chọn dropdown \[Delete\] tại trang PO

2\. Hệ thống hiển thị pop up xác nhận xóa 

3\. Người dùng xác nhận

- Nếu xác nhận: nhấn vào \[Delete\] 

- Nếu không thì nhấn \[Cancel\]

4\. Hệ thống hiển thị quay lại trang chi tiết của PO

5\. Hệ thống xóa dữ liệu PO và cập nhật trang PO

6\. Kết thúc Use case 

## **Business Rule**

Quy định hiển thị và thao tác 

\[Delete\] button: 

- Enable đối với PO được tạo trên Conative  
- Disable đối với PO được sync từ ERP

# **UC 10.10 Sync Purchase Order data from Shiphero**

## **1.1. Mục tiêu**

Sau khi kết connect với Shiphero, user sẽ xem được tất cả những Purchase Order, PO status , purchase order line item đồng bộ từ Shiphero về Conative, và được cập nhật sau mỗi 4 giờ. 

## **1.2. Input** 

User hoàn thành đồng bộ Shiphero ở Integration Hub 

## **1.3. Output**

- PO list   
- PO detail  
- PO line item  
- On order 

1.5 Business rule 

**PO list**  
Thao tác xem PO list ở Shiphero: Purchase Order \> PO list hiện ra

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | PO Number | The number of PO on Shiphero | **Rule:** map với PO number trong PO list ở Shiphero Mapping theo field tương ứng trong bảng [PurchaseOrder](https://developer.shiphero.com/schema/)  Trường hợp PO number \= null, skip |
| 2 | PO ID  | The id of PO on Shiphero | **Rule:** map với **Row ID** trong PO list ở Shiphero Mapping theo field tương ứng trong bảng [PurchaseOrder](https://developer.shiphero.com/schema/)  Trường hợp Row id \= null, skip |
| 3 | Vendor / Supplier | Vendor in Shiphero | **Rule:** map với Vendor trong PO list ở Shiphero Mapping theo field tương ứng trong bảng [PurchaseOrder](https://developer.shiphero.com/schema/)  Vendor field is required Trường hợp vendor Shiphero \= null, Conative sẽ hiển thị **Multiple vendors** Trường hợp vendor id hoặc vendor name \= null, skip |
|  | Warehouse | Warehouse from Shiphero | **Rule:** map với Vendor trong PO list ở Shiphero Mapping theo field tương ứng trong bảng [PurchaseOrder](https://developer.shiphero.com/schema/)  Warehouse is required Trường hợp warehosue Shiphero \= null \= Skip |
| 4 | Created date (Generated date old system) | Created date of PO  | **Rule:** map với Date trong PO list ở Shiphero  Mapping theo field tương ứng trong bảng [PurchaseOrder](https://developer.shiphero.com/schema/)  |
| 5 | Expected arrival date | Expected date on Shiphero | **Rule:** map với Expected Date trong PO list ở ShipheroMapping theo field tương ứng trong bảng [PurchaseOrder](https://developer.shiphero.com/schema/)  **Not Required**  |
|  | Ship date | Ship date on Shiphero | **Rule:** map với ShipDate trong PO list ở ShipheroMapping theo field tương ứng trong bảng [PurchaseOrder](https://developer.shiphero.com/schema/)  **Not required** |

**View PO detail page (detail \+ line item)** 

**PO line item** 

Thao tác xem PO detail ở Shiphero: Purchase Order \> danh sách PO hiện ra

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
|  | Vendor |  | Map theo vendor của PO detail |
|  | Expected date |  | Map theo expected date của PO detail |
|  | Warehouse |  | Map theo warehouse của PO detail |
|  | PO id |  | Map theo PO id trên PO detail |
|  | PO number |  | Map theo PO number trên PO detail |
|  | Source |  | Mặc định \= Shiphero |
| 1 | SKU | Variant SKU | **Rule** Chỉ map cho các SKU có trên Shopify & Conative.  Không thấy sku, skip Mapping theo field tương ứng trong bảng [PurchaseOrder line item](https://developer.shiphero.com/schema/)e |
| 2 | Variant title | Variant title |  |
|  | Status  | Received status of the line item  | **Rule:** tính theo bên Conative **Over received**: quantity received \> ordered quantity  **Received**: quantity received \= order quantity **Under received**: quantity received \< ordered quantity  **Not received:** Quantity received \= 0 |
| 3 | Stock | Stock from Shopify  |  |
| 6 | On order  | Left quantity not coming yet  | **Formula** Ordered quantity \- Received **Rule**  Hiển thị “0” nếu On order \< 0![][image7] |
| 4 | Order quantity |  | **Rule:** map với Ordered trong PO detail ở Shiphero  Mapping theo field tương ứng trong bảng [PurchaseOrder line item](https://developer.shiphero.com/schema/) |
| 5 | **Received** | Quantity received of item | **Rule:** map với Received trong PO detail ở Shiphero Mapping theo field tương ứng trong bảng [PurchaseOrder line item](https://developer.shiphero.com/schema/) |
|  | **Status “Removed”**  | UI thể hiện line item đã bị remove khỏi Shiphero | Khi line item bị remove khỏi Shiphero \> UI Conative thể hiện trạng thái line item bị Remove.  Data Output:\- SKU\- Variant title\-Status: theo status trước khi bị remove\- Stock: theo stock hiện tại của variant\- On Order: hiển thị “0”\- Order Quantity: hiển thị value trước khi bị remove ở Shiphero\- Received: hiển thị value trước khi bị remove ở Shiphero\- Received today: hiển thị “0” \- Item status: theo status của variant |
|  | Receive Today |  |  |
|  | Item status |  |  |

## 

**PO Fulfillment Status mapping** 

**\*cần làm lại bảng status cho trạng thái PO, trạng thái nhập hàng của PO, trạng thái nhập hàng của line item** 

| Status on Conative  | Status (DB) | Status on Shiphero | Note |
| :---- | :---- | :---- | :---- |
| **Draft** (Skip trong đợt release này) |  | \- |  |
| **Pending** | **Pending**  | **Pending** |  |
| **Canceled**  | **Canceled** | **Canceled** | Skip không lấy từ Shiphero |
| **Closed** | **Closed** | **Closed** | Không tính On order cho PO có status Closed |

**Conative update dữ liệu PO cho các trường hợp sau:** 

**Frequency: 4h**

- Create new PO on Shiphero  
- Update existing PO detail  
  - PO number  
  - Ship date (có thể làm trước để sau này dùng)   
  - Expected date   
  - Fulfillment Status (pending, canceled, closed)   
- Update PO line item  
  - received status   
  - Ordered quantity  
  - Quantity received  
  - Quantity rejected (không thấy trường này trên shiphero)   
- Remove line item

**Những case lưu ý**  
**PO**

- Conative pull PO status Pending, Closed có trên Shiphero

**PO line item On order:** Missing sku on Shopify: Không cập nhật data cho các SKU không có trên Shopify, báo lỗi

- Duplicate sku on Shopify, different status: Ưu tiên cập nhật data cho các sku có st  
- atus \= Active.  
- Duplicate sku on Shopify, Status Active: Cập nhật data cho tất cả các sku duplicate   
- Removed PO line item in Shiphero: Cập nhật trạng thái “removed” của line item đó trong PO detail

# **11\. Inventory Planner \- Sales by month**

# **UC 11.1 View report Sales by month**

## **Mục tiêu**

Hiển thị danh sách các metric của variant theo input

## **Input**

- Search

## **Output**

- Time range: Year to date \+ 6 months ahead (Tháng 1 năm nay \=\> tháng hiện tại \=\> 6 tháng kế tiếp trong tương lai. Ví dụ: Tháng hiện tại là tháng 8/2023 \=\> Hệ thống trả data từ tháng 1/2023 \=\> 8/2023 \=\> 2/2024)

- Grouped by: 

  - Variant

  - Warehouse (Location) 

  - Month

    

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | Variant  | Include: \- Variant image \- Variant title \- Variant SKU | **Rule:**  Hiển thị chung 1 field **Sort**:  Theo variant title. A-Z và ngược lại  |
| 2 | ATS | The number of units of a variant that are currently for sale | **Formula:**  On order \+ Stock **Sort:**  Mặc định Theo A-Z và ngược lại  **Tooltip:**  Hiển thị khi user hover vào field header. Content dùng theo description  |
| 3 | Trend | The direction of sales in the following time period predicted by the AI model.  | **Formula**:  AI model **Tooltip**:  Hiển thị khi user hover vào field header. Content dùng theo description |
| 4 | Metric \- Forecast sales (AI) (Units) & Forecast Sales (Rule-based) | Sales forecast (AI) Sales forecast (Rule-based)  | **Rule**:  AI model & Rule-based model of variant Dropdown cho phép user thay đổi forecast method giữa AI vs Rule-based Mặc định hiển thị: Sales Forecast (AI) Hiển thị data tháng hiện tại và 6 tháng sắp tới. Không hiển thị data tháng trong quá khứ.  Hiển thị “-” nếu không hiển thị data  |
| 5 | Metric \- Target sales (Units) | Sales target that based on the forecast and allow users to edit | **Rule**: Mặc định hiển thị giá trị của  Forecast sales (AI) (Units) Cho phép user edit value tháng hiện tại và tương lai Tooltip: Hiển thị khi user hover vào input field. Hiển thị value đã cập nhật trước đó  |
| 6 | Metric \- Actual sales (Units) | The total number of variant sold by month | **Formula:**  Gross quantity of variant, grouped by month **Rule**  Hiển thị “-” nếu không hiển thị data |
| 7 | Metric \- Last year Sales (Units) | The total number of variant sold by month of the last year | **Formula:**  Gross quantity of variant , grouped by month of Last year (Vd: Actual sales tháng 3/2023 \> Last year Sales tháng 3/2022) **Rule**  Hiển thị “-” nếu không hiển thị data |

# **UC 11.2 Inventory Planner \- Filter variant in Sales by month**

## **Mục tiêu**

Trên các trang Sales by month, user có thể filter các metrics và lưu lại lại filter thành custom report.

## **Input**

Filter (select)

Condition (Operators)

Filter values 

## **Output**

Có thể filter các metrics 

## **Workflow**

### **Main flow (Happy case)**

1\. Trên trang Replenishment flow, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

\[Select Filter\] và chọn field thông tin muốn filter

Chọn \[Condition\] để chọn điều kiện filter

Nhập giá trị filter vào field \[Value\]

Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

\[Select Filter\] và chọn field thông tin muốn filter

Chọn \[Condition\] để chọn điều kiện filter

Nhập giá trị filter vào field \[Value\]

Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Chọn \[Apply Filter\]

8\. Hệ thống trả về dữ liệu theo điều kiện filter

## **Business rule** 

Quy định hiển thị và thao tác 

| Filters (Fields) | Conditions (Operators) | Types | Value |
| :---- | :---- | :---- | :---- |
| Warehouse (Location) | Equal | Single selection | Pull from Shopify  |
| Replenishable | Equal | Single selection  | Value:  \- Continue \- Discontinue Default: Continue |
| Variant title | Is Is not | Multiple selection |  |
| sku | Is Is not | Multiple selection |  |
| trend | Is Is not | Multiple selection |  |
| Channel | Is Is not | Multiple selection |  |

### **Quy định hiển thị và thao tác** 

| Filters (Fields) | Conditions (Operators) | Types | Default value |
| :---- | :---- | :---- | :---- |
| Warehouse (Location) | Is | Single selection |  |
| Replenishable | Is | Single selection | Value \= “Continued” |

# **UC 11.3 Search variant in Sales by month**

Người dùng có thể tìm kiếm sản phẩm bằng cách nhập SKU, Variant Title, Barcode. 

## **Input**

Truyền vào Barcode / Variant title / SKU

## **Output**

Trả dữ liệu theo Use case View report Sales by month

## **Workflow**

## **Main flow**

1\. Trên trang Replenishment flow, người dùng bấm vào thanh \[Search\]

2\. Hệ thống đề xuất 5 sản phẩm được tìm kiếm gần đây nhất

3\. Người dùng nhập thông tin để tìm kiếm sản phẩm 

1. Người dùng có thể tìm kiếm sản phẩm bằng cách nhập SKU, Title, Barcode. 

4\. Hệ thống trả về dữ liệu variant theo điều kiện tìm kiếm

5\. Kết thúc use case 

### **Alternative flow**

3a. Người dùng chọn sản phẩm theo đề xuất của hệ thống 

- Hệ thống trả về dữ liệu variant theo điều kiện tìm kiếm

- Kết thúc use case 

### **Exceptional flow**

4a. Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả “SORRY\! No data found \- Please try searching other keywords or adjusting your filter”

- Kết thúc use case.

## **Business Rule**

- Tìm kiếm theo Product title: search gần đúng 

- Tìm kiếm theo SKU: search gần đúng 

- Tìm kiếm theo Barcode: search gần đúng

# **UC 11.4 Update Target Sales**

# Mục tiêu

Trên trang Sales by month, field Target sales (units), user có thể cập nhật sales target 

## **Input**

Target number

## **Output**

Target number history (Phase 2\)

Target number

## **Workflow** 

1\. Trên trang Sales by month, user chọn variant muốn cập nhật và chọn field Target Sales

2\. User thay đổi Target sales value hiện tại bằng cách nhập value mới

3\. Hệ thống hiển thị CTA \[Save changes\] \- \[Discard\] khi user nhập. Sau khi nhập, User chọn:

- \[Save change\] để lưu cập nhật   
- \[Discard\] để huỷ bỏ cập nhật và quay về trang trước đó

4\. Hệ thống kiểm tra thông tin:

- Nếu user chọn \[Save changes\], hệ thống lưu Target sales mới và thông báo đã cập nhật. Tham chiếu message ở file [**Notification & Message**](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)

5\. Kết thúc use case

## **Business Rule**

### **Quy định hiển thị và thao tác** 

- Mặc định hiển thị giá trị của  Forecast sales (AI) (Units)  
- Cho phép user edit value tháng hiện tại và tương lai. Đối với tháng trong quá khứ, không hiển thị input field  
- Tooltip: Hiển thị khi user hover vào input field. Hiển thị value đã cập nhật trước đó

# **UC 11.5 View report Replenishment flow** {#uc-11.5-view-report-replenishment-flow}

## **Mục tiêu**

Hiển thị danh sách các metric của variant theo input

## **Input**

- Search

- Filter

- Select time range

- Channel settings

- Update reorder quantity

- Update lead time

- Update days of stock

## **Output**

- Trả về danh sách field 


| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | Variant title | Name of specific variant | **Default Column**  Yes |
| 2 | Variant SKU | SKU of specific variant | **Default Column**  Yes |
|  | Variant ID |  | **Default Column**  Yes |
|  | Color |  | **Default Column**  Yes  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 3 | Gross Sales | Total sales before any deductions  | **Rule**  From Shopify, grouped by variant level **Sort** Theo A-Z và ngược lại **Default Column**  Yes |
| 4 | Gross Quantity | Total units of any product before any deductions | **Rule**  From Shopify, grouped by variant level **Sort** Theo A-Z và ngược lại **Default Column**  Yes |
| 5 | Reorder quantity | Number of items suggested to fulfill future needs using Sales forecast AI  | **Formula Case 1:** forecast setting là lead time \+ days of stock  Reorder Quantity \= (sum Sales forecast từ start date của Lead Time đến end date của DOS) \- ATS **Case 2:** forecast setting là custom range Sales forecast \= (sum Sales forecast từ hôm nay đến cuối forecast range) \- ATSE.g range từ Jan 1 đến Mar 31\. Cột Sales Forecast đang trả về 300 cho dự đoán Sales của range. Tuy nhiên, Sales Forecast dùng để tính Reorder Quantity phải lấy từ hôm nay (Dec 12\) vì có Sales phát sinh từ đây đến cuối tháng **Rule** Mặc định hiển thị value theo formula của Conative Cho phép user edit value Reorder quantity  Tự động cập nhật value sau mỗi ngày theo sales forecast AI.  **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Sort** Theo A-Z và ngược lại **Default Column**  Yes |
| 6 | Lead time | The amount of days that stock arrives once user order it | **Rule**  Mặc định hiển thị value theo Lead time được set trong Settings Cho phép user edit value Lead time Start date \= Today End date \= Today \+ Lead time  *(Vd: Start date: 22 Aug \=\> End date: 06 Oct)*  *![][image8]* Khi edit Lead time thì Sales forecast sẽ thay đổi theo **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Default Column**  Yes |
| 7 | Days of stock | The amount of days the current stock of an item will last | **Rule**  Mặc định hiển thị value Days of stock \= 90 Cho phép user edit value Days of stock Khi edit Days of stock thì Sales forecast sẽ thay đổi theo **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Default Column**  Yes |
| 8 | ATS | The number of units of a variant that are currently for sale | **Formula** ATS \= Stock \+ On Order  **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Default Column**  Yes |
| 9 | Sales forecast | Total sales forecast AI based on lead time & days of stock | **Formula Case 1:** forecast setting là lead time \+ days of stock  Sales forecast \= Sum of sales forecast by lead time \+ days of stock **Case 2:** forecast setting là custom range Sales forecast \= Sum of sales forecast of the range **Rule** Tự động cập nhật value mỗi ngày theo model AI trả về **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Default Column**  Yes |
| 10 | On order  | The number of variants ordered with the supplier but not yet delivered. | **Rule**  Mapping field: Variant id **Formula** Case 1: Use ERP (eg: Shiphero)  \- Lấy dữ liệu On order của PO của ERP, có status sau.  Shiphero: PO status \= Pending Case 2: Use Conative PO  \- Lấy dữ liệu On order của Conative có status \= Open (Xem use case PO)  Case 3: Use both ERP & Conative PO \- Sum On order (Conative PO) & On order (ERP) **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Default Column**  Yes |
| 11 | Sales per day | The average number of variants sold in a day. | **Calculation** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27) **Rule** Cập nhật theo time range user chọn   **Default Column**  Yes |
| 12 | Sales per day (In stock) | The average number of variants sold in a day. (accounting only for days when the product is in stock) | **Calculation** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27) **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description  |
| 13 | Sales per day (Out of stock) | The average number of variant sold in a day. (accounting only for days when the product is out of stock) | **Calculation**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27)  **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 14 | Days until stock out  |  | **Default Column**  Yes |
| 15 | Stock  | Number of items available to sell. | **Default Column**  Yes  |
| 16 | Next arrival date  | The expected date of the next PO of the variant  | **Mapping field** Expected date  **Default Column**  Yes |
| 17 | Next arrival quantity | The order quantity of variant in the next PO | **Mapping field**  Order quantity **Default Column**  Yes |
| 18 | Balance |  | **Formula**  Stock \+ Next arrival quantity **Default Column**  Yes |
| 19 | Days since stock out  |  | **Formula** Today \- latest day when stock \<=0 **Default Column**  Yes |
| 20 | Expected stockout days |  | **Formula** Next arrival date \- latest day when stock \<= 0 **Default Column**  Yes |
| 21 | Opportunity cost | Opportunity cost when a variant is out of stock | **Formula** Price x Sum \[**forecast sales AI** of **Expected stockout days**\] *Ví dụ:  \- Mizumi variant bị stockout từ ngày 15/9 đến ngày 30/9 (Expected stockout days \= **15**.  \- Sales Forecast AI của variant theo expected stockout days 15-30/9 \= **50**. \- Price \= **70** \=\> Opportunity Cost \= 70 x 50 \= **$3500***  **Sort** Sort A-Z và ngược lại  **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Default Column**  Yes |
| 22 | Gross margin | Net Revenue minus Cost of Goods Sold | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 23 | Gross profit | Net Revenue minus Cost of Goods Sold and Operating Expenses. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 24 | Compare-at-price | The comparison of the original price and the sale price. | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 25 | Cost |  | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Chưa có content |
| 26 | Bar code |  | **Default Column**  No **Sort** Theo A-Z và ngược lại  |

# **UC 11.6 Inventory Planner \- Filter variant** 

## **Mục tiêu**

Trên trang Replenishment flow, user có thể filter các metrics và lưu lại lại filter thành custom report.

## **Input**

Filter (select)

Condition (Operators)

Filter values 

## **Output**

Có thể filter các metrics và lưu lại filter thành custom report 

## **Workflow** 

### **Main flow (Happy case)**

1\. Trên trang Replenishment flow, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

\[Select Filter\] và chọn field thông tin muốn filter

Chọn \[Condition\] để chọn điều kiện filter

Nhập giá trị filter vào field \[Value\]

Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

\[Select Filter\] và chọn field thông tin muốn filter

Chọn \[Condition\] để chọn điều kiện filter

Nhập giá trị filter vào field \[Value\]

Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Chọn \[Apply Filter\]

8\. Hệ thống trả về dữ liệu theo điều kiện filter

## 

## **Business rule** 

### **Quy định hiển thị và thao tác** 

| Filters (Fields) | Conditions (Operators) | Types | Default value |
| :---- | :---- | :---- | :---- |
| Warehouse (Location) | Is | Single selection |  |
| Replenishable | Is | Single selection | Value \= “Continued” |

# **UC 11.7 Search variant in Replenishment flow**

Ở trang Replenishment flow, người dùng có thể tìm kiếm sản phẩm bằng cách nhập SKU, Variant Title, Barcode. 

## **Input**

Truyền vào Barcode / Variant title / SKU

## **Output**

Trả dữ liệu theo Use case **View report Replenishment flow**

## **Workflow**

## **Main flow**

1\. Trên trang Replenishment flow, người dùng bấm vào thanh \[Search\]

2\. Hệ thống đề xuất 5 sản phẩm được tìm kiếm gần đây nhất

3\. Người dùng nhập thông tin để tìm kiếm sản phẩm 

1. Người dùng có thể tìm kiếm sản phẩm bằng cách nhập SKU, Title, Barcode. 

4\. Hệ thống trả về dữ liệu variant theo điều kiện tìm kiếm

5\. Kết thúc use case 

### **Alternative flow**

3a. Người dùng chọn sản phẩm theo đề xuất của hệ thống 

- Hệ thống trả về dữ liệu variant theo điều kiện tìm kiếm

- Kết thúc use case 

### **Exceptional flow**

4a. Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

- Kết thúc use case.

## **Business Rule**

- Tìm kiếm theo Product title: search gần đúng 

- Tìm kiếm theo SKU: search gần đúng 

- Tìm kiếm theo Barcode: search gần đúng

# 

# **UC 11.8 Update reorder quantity**

## **Mục tiêu**

Update reorder quantity 

## **Input**

- Number

## **Workflow**

**Main flow**

1\. Trên trang Replenishment flow, user chọn variant muốn cập nhật và chọn field Reorder quantity 

2\. User thay đổi reorder quantity value hiện tại bằng cách nhập value mới

3\. Hệ thống hiển thị CTA \[Save changes\] \- \[Discard\] khi user nhập. Sau khi nhập, User chọn:

- \[Save change\] để lưu cập nhật   
- \[Discard\] để huỷ bỏ cập nhật và quay về trang trước đó

4\. Hệ thống kiểm tra thông tin:

- Nếu user chọn \[Save changes\], hệ thống lưu reorder quantity mới và thông báo đã cập nhật. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case

### **Alternative flow 1 \- Update reorder quantity cho nhiều variant** 

1\. Trên trang Replenishment flow, user chọn checkbox những variant muốn cập nhật Reorder quantity.

2\. Hệ thống hiển thị \[Action\], user chọn \[Action\] \> \[Update Reorder quantity\] 

3\. Hệ thống hiển thị popup cập nhật Reorder quantity 

4\. User nhập value reorder quantity

5\. Sau khi nhập, User chọn:

- \[Save change\] để lưu cập nhật   
- \[Discard\] để huỷ bỏ cập nhật và quay về trang trước đó

4\. Hệ thống kiểm tra thông tin:

- Nếu user chọn \[Save changes\], hệ thống lưu reorder quantity mới và thông báo đã cập nhật. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case

## **Business Rule**

Quy định hiển thị và thao tác 

- Mặc định hiển thị value theo formula của Conative

- Cho phép user edit value Reorder quantity 

- Tự động cập nhật value sau mỗi ngày theo sales forecast AI. 

Checkbox của variant

- Checked khi user nhập value   
- Unchecked sau khi user chọn \[Save changes\] / \[Discard\]  
- Ô checkbox của từng variant sẽ hiển thị ![][image2] khi user chọn variant   
- Ô checkbox All sẽ hiển thị ![][image3] nếu user select từng variant, hiển thị số lượng variant được selected (**\<number\> selected)**  và CTA \[select all variant in store\]  
- Ô checkbox All sẽ hiển thị ![][image2]khi user chọn all, hiển thị số lượng variant ở trang hiện tại (**\<number\> selected)** và CTA \[select all variant in store\]

CTA Save changes

- Disabled khi field empty hoặc value không thay đổi so với trước đó

# **UC 11.9 Update Day of stock**

## **Mục tiêu**

Update Day of stock

## **Input**

- Number

## **Workflow**

**Main flow**

1\. Trên trang Replenishment flow, user chọn variant muốn cập nhật và chọn field **Days of stock**

2\. User thay đổi **days of stock** value hiện tại bằng cách nhập value mới

3\. Hệ thống hiển thị CTA \[Save changes\] \- \[Discard\] khi user nhập. Sau khi nhập, User chọn:

- \[Save change\] để lưu cập nhật   
- \[Discard\] để huỷ bỏ cập nhật và quay về trang trước đó

4\. Hệ thống kiểm tra thông tin:

- Nếu user chọn \[Save changes\], hệ thống lưu Days of stock mới và thông báo đã cập nhật. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case

### **Alternative flow 1 \- Update Days of stock cho nhiều variant** 

1\. Trên trang Replenishment flow, user chọn checkbox những variant muốn cập nhật Days of stock.

2\. Hệ thống hiển thị \[Action\], user chọn \[Action\] \> 

2\. User thay đổi Days of stocks value hiện tại bằng cách nhập value mới

3\. Hệ thống hiển thị CTA \[Save changes\] \- \[Discard\] khi user nhập. Sau khi nhập, User chọn:

- \[Save change\] để lưu cập nhật   
- \[Discard\] để huỷ bỏ cập nhật và quay về trang trước đó

4\. Hệ thống kiểm tra thông tin:

- Nếu user chọn \[Save changes\], hệ thống lưu Days of stocks mới và thông báo đã cập nhật. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case

## **Business Rule**

Quy định hiển thị và thao tác 

Checkbox của variant

- Checked khi user nhập value   
- Unchecked sau khi user chọn \[Save changes\] / \[Discard\]  
- Ô checkbox của từng variant sẽ hiển thị ![][image2] khi user chọn variant   
- Ô checkbox All sẽ hiển thị ![][image3] nếu user select từng variant, hiển thị số lượng variant được selected (**\<number\> selected)**  và CTA \[select all variant in store\]  
- Ô checkbox All sẽ hiển thị ![][image2]khi user chọn all, hiển thị số lượng variant ở trang hiện tại (**\<number\> selected)** và CTA \[select all variant in store\]

CTA Save changes

- Disabled khi field empty hoặc value không thay đổi so với trước đó

	

### **Alternative flow 2 \- Không cho phép chỉnh sửa Days of stock khi Forecast Settings là Custom Range**

1. Ở trang Replenishment Flow, user chọn Forecast Settings \= Custom range \> nhấn Apply  
2. Field Days of stock của tất cả variant chuyển sang status disable, không cho phép user chỉnh sửa  
3. Option thay đổi set days of stock ở Bulk Action ẩn trên UI

Business Rule

- Cho phép chỉnh sửa single/ bulk action khi user chọn lại Forecast Settings \= Lead Time \+ Days of stock

# 

# **UC 11.10 Update Lead time**

## **Mục tiêu**

Update Day of stock of ở trang Replenishment flow

## **Input**

- Number

## **Workflow**

**Main flow**

1\. Trên trang Replenishment flow, user chọn variant muốn cập nhật và chọn field **Lead time**

2\. User thay đổi **Lead time** value hiện tại bằng cách nhập value mới

3\. Hệ thống hiển thị CTA \[Save changes\] \- \[Discard\] khi user nhập. Sau khi nhập, User chọn:

- \[Save change\] để lưu cập nhật   
- \[Discard\] để huỷ bỏ cập nhật và quay về trang trước đó

4\. Hệ thống kiểm tra thông tin:

- Nếu user chọn \[Save changes\], hệ thống lưu Lead time mới và thông báo đã cập nhật. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case

### **Alternative flow 1 \- Update Lead time cho nhiều variant** 

1\. Trên trang Replenishment flow, user chọn checkbox những variant muốn cập nhật Lead time.

2\. Hệ thống hiển thị \[Action\], user chọn \[Action\] \> 

2\. User thay đổi Lead time value hiện tại bằng cách nhập value mới

3\. Hệ thống hiển thị CTA \[Save changes\] \- \[Discard\] khi user nhập. Sau khi nhập, User chọn:

- \[Save change\] để lưu cập nhật   
- \[Discard\] để huỷ bỏ cập nhật và quay về trang trước đó

4\. Hệ thống kiểm tra thông tin:

- Nếu user chọn \[Save changes\], hệ thống lưu Lead time mới và thông báo đã cập nhật. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

5\. Kết thúc use case

## **Business Rule**

Quy định hiển thị và thao tác 

Checkbox của variant

- Checked khi user nhập value   
- Unchecked sau khi user chọn \[Save changes\] / \[Discard\]  
- Ô checkbox của từng variant sẽ hiển thị ![][image2] khi user chọn variant   
- Ô checkbox All sẽ hiển thị ![][image3] nếu user select từng variant, hiển thị số lượng variant được selected (**\<number\> selected)**  và CTA \[select all variant in store\]  
- Ô checkbox All sẽ hiển thị ![][image2]khi user chọn all, hiển thị số lượng variant ở trang hiện tại (**\<number\> selected)** và CTA \[select all variant in store\]

CTA Save changes

- Disabled khi field empty hoặc value không thay đổi so với trước đó

### **Alternative flow 2 \- Không cho phép chỉnh sửa Lead time khi Forecast Settings là Custom Range**

4. Ở trang Replenishment Flow, user chọn Forecast Settings \= Custom range \> nhấn Apply  
5. Field Lead time của tất cả variant chuyển sang status disable, không cho phép user chỉnh sửa  
6. Option thay đổi set lead time ở Bulk Action ẩn trên UI

Business Rule

- Cho phép chỉnh sửa single/ bulk action khi user chọn lại Forecast Settings \= Lead Time \+ Days of stock

# **UC 11.11 Export Replenishment data**

## **Mục tiêu**

Export report Replenishment flow với các variant đã chọn hoặc all variant ra file CSV

## **Input** 

- Search  
- Select variant 

## **Output** 

- File CSV chứa các variant đã chọn và dữ liệu đã được cập nhật trên Replenishment flow 

## **Workflow** 

Mainflow 

1\. Trên trang Replenishment flow, user chọn \[Export\]

2\. Hệ thống hiển thị popup export settings

3\. User chọn số lượng variant để export: 

- Current page: export 30 variant ở page hiện tại   
- All variant: export toàn bộ variant   
- Selected variant \<number\> variant: tuỳ thuộc vào số lượng variant

4\. User chọn \[export\] 

5\. Hệ thống export file theo yêu cầu và thông báo Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

### **Alternative flow \- chọn variant để export** 

1\. Trên trang Replenishment flow, user tick checkbox những variant muốn export

2\. User Chọn \[Export\]

2\. Hệ thống hiển thị popup export settings

3\. User chọn option export theo variant để export: 

- Selected variant \<number\> variant: tuỳ thuộc vào số lượng variant đã chọn 

4\. User chọn \[export\] 

5\. Hệ thống export file theo yêu cầu và thông báo Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

## **Business rules:** 

### **Quy định hiển thị và thao tác** 

Checkbox của variant

- Ô checkbox của từng variant sẽ hiển thị ![][image2] khi user chọn variant   
- Ô checkbox All sẽ hiển thị ![][image3] nếu user select từng variant, hiển thị số lượng variant được selected (**\<number\> selected)**  và CTA \[select all variant in store\]  
- Ô checkbox All sẽ hiển thị ![][image2]khi user chọn all, hiển thị số lượng variant ở trang hiện tại (**\<number\> selected)** và CTA \[select all variant in store\]


Format file CSV khi export:

- File Name

  -  \<Replenishment export MMM dd \- MMM dd, yyyy\> (Eg: Replenishment export Jul 01 \- Jul 31, 2023\)

- Dữ liệu (Các row & column) được export và format file CSV dựa theo kết quả dữ liệu trả về khi người dùng thực hiện các use case trên trang Replenishment flow

# **UC 11.12 Config column \- Replenishment Flow**

## **Mục tiêu**

Chọn/ thay đổi metric muốn hiển thị ở trang Replenishment Flow

### **Main flow (Happy case)**

1. Trên trang Replenishment flow, user chọn **\[Config column\]**  
2. Hệ thống hiển thị popup Config column   
3. User nhập tên field vào thanh search để tìm và add / remove các field chưa có / đã có trong table   
4. User kéo thả field để thay đổi vị trí của các field đã add vào table   
5. User chọn \[x\] để remove các field không cần thiết ra khỏi table   
6. User chọn **\[Save changes\]** để cập nhật   
7. Hệ thống cập nhật thay đổi, hiển thị thông báo đến user 

2\. Người dùng search và chọn metric (chưa hiện có) để thêm vào bảng dữ liệu sản phẩm 

3\. Người dùng chọn \[Columns\] 

4\. Hệ thống trả dữ liệu theo column đã chọn 

5\. Kết thúc use case 

### **Alternative Flow 1**

2a. Người dùng chọn \[Select all\] trong \[add column\] để chọn hiển thị tất cả các metric  

### **Alternative Flow 2**

2b. Người dùng kéo thả metric để sắp xếp thứ tự cột trong bảng dữ liệu 

### **Alternative Flow 3**

2c. Người dùng chọn \[Clear all\] trong \[add column\] để xóa các metric đã chọn 

### **Alternative Flow 4**

3a. Người dùng chọn \[Restore default\] 

4\. Hệ thống trả lại dữ liệu mặc định     

## **Business rule**

Quy định hiển thị và thao tác 

**Thứ tự hiển thị field mặc định cho user mới:** 

Tham chiếu [**UC 11.5 \- View report Replenishment Flow**](#uc-11.5-view-report-replenishment-flow)

1. Variant title  
2. Variant SKU  
3. Variant ID  
4. Gross Sales  
5. Gross Quantity  
6. Reorder quantity  
7. Lead time  
8. Days of stock  
9. ATS  
10. Sales forecast  
11. On order   
12. Sales per day (ATS)  
13. Sales per day (In stock)  
14. Sales per day (Out of stock)  
15. Days until stock out   
16. Stock   
17. Next arrival date   
18. Next arrival quantity  
19. Balance  
20. Days since stock out   
21. Expected stockout days  
22. Opportunity cost

**Các field (Column) được config**

| STT | Field  | Business rules for Config column |
| :---- | :---- | :---- |
| 1 | Variant title | **Rule** Mặc định hiển thị ở đầu table  Không được remove hay thay đổi vị trí (Không có CTA \[x\] & icon kéo thả) |
| 2 | Variant SKU | **Rule** Có thể thay đổi vị trí Có thể remove |
| 3 | Gross Sales | **Rule** Có thể thay đổi vị trí Có thể remove |
| 4 | Gross Quantity | **Rule** Có thể thay đổi vị trí Có thể remove |
| 5 | Reorder quantity | **Rule** Có thể thay đổi vị trí Có thể remove |
| 6 | Lead time | **Rule** Có thể thay đổi vị trí Có thể remove |
| 7 | Days of stock | **Rule** Có thể thay đổi vị trí Có thể remove |
| 8 | ATS | **Rule** Có thể thay đổi vị trí Có thể remove |
| 9 | Sales forecast | **Rule** Có thể thay đổi vị trí Có thể remove |
| 10 | On order  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 11 | Sales per day (ATS) | **Rule** Có thể thay đổi vị trí Có thể remove |
| 12 | Sales per day (In stock) | **Rule** Có thể thay đổi vị trí Có thể remove |
| 13 | Sales per day (Out of stock) | **Rule** Có thể thay đổi vị trí Có thể remove |
| 14 | Days until stock out  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 15 | Stock  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 16 | Next arrival date  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 17 | Next arrival quantity | **Rule** Có thể thay đổi vị trí Có thể remove |
| 18 | Balance | **Rule** Có thể thay đổi vị trí Có thể remove |
| 19 | Days since stock out  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 20 | Expected stockout days | **Rule** Có thể thay đổi vị trí Có thể remove |
|  | Opportunity cost |  |

9. Người dùng click \[Clear all\], hệ thống xóa tất cả metric đã chọn nhưng giữ lại \[Product title\] 

10. Khi số lượng metric được chọn nhỏ hơn tổng metric, enable \[Select all\], \[Clear all\]

11. Khi tất cả các metric đều được chọn (số lượng metric được chọn bằng tổng metric), Enable \[Clear all\], disable\[Select all\] 

12. Khi không có metric nào được chọn (số lượng metric được chọn bằng 0), enable\[Select all\], disable\[Clear all

# **UC 12 Gap Analysis**

# **UC 12.1 View Report Gap Analysis**

## **Mục tiêu**

User xem được: 

- số ngày dự kiến out of stock  (Expected stockout days) cho đến khi nhập hàng đủ để bán và cover luôn số lượng re-order  
- Chi phí cơ hội (Opportunity cost) dựa vào AI forecast trong thời gian item đó out of stock   
- Recommended action từ Conative order thêm số lượng item hợp lý để hạn chế hết stock trong tương lai

Example of Opportunity cost (Sheet “example…formula”): 

[Copy of Understock, Overstock, Gap Discovery ](https://docs.google.com/spreadsheets/d/1yr0guJqreBFj0wc1OtuK9M_mIS2UkyIZ58Q2Y9xmh9I/edit#gid=1623522225)

[Conative - Feature checklist](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0)

## **Input** 

Search

Filter

Select time range

Channel settings

Config column 

## **Output**

Danh sách các field

| STT | Field  | Description | Formula / Business rules |
| :---- | :---- | :---- | :---- |
| 1 | Variant title |  | **Sort**:  Sort A-Z và ngược lại **Default display:** Yes |
| 2 | SKU |  | **Sort**  Sort A-Z và ngược lại  **Default display:** Yes |
| 3 | Variant ID |  | **Default display:** Yes |
|  | Color |  | **Default Column**  Yes  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 4 | Gross Sales | Total sales recorded prior to [sales discounts](https://www.accountingtools.com/articles/sales-discount) and [sales returns](https://www.accountingtools.com/articles/sales-return)  | **Sort**  Sort A-Z và ngược lại  **Default display:** Yes |
| 5 | Gross Quantity | *Total units recorded prior to sales discounts and sales returns* | **Format**  **Sort**  Sort A-Z và ngược lại  **Default display:** Yes |
| 6 | Next Arrival Date | Earliest date of delivery | **Format Sort**  Sort A-Z và ngược lại  **Default display:** Yes |
| 7 | Next Arrival Quantity  | The order quantity of variant in the next PO | **Sort**  Sort A-Z và ngược lại  **Mapping field**  Order quantity **Default display:** Yes |
| 8 | Balance | Predicted stock the item would have after next arrival PO.  | **Formula**  **Sort**  Sort A-Z và ngược lại  Stock \+ Next arrival quantity **Default display:** Yes |
| 9 | Stock | *Total quantity of product left in inventory* | **Sort**  Sort A-Z và ngược lại  **Default display:** Yes |
| 10 | On order | The number of variants ordered with the supplier but not yet delivered. | **Sort**  Sort A-Z và ngược lại  **Rule**  Mapping field: Variant id Case 1: Use ERP (eg: Shiphero)  \- Lấy dữ liệu On order của ERP Case 2: Use Conative PO  \- Lấy dữ liệu On order của Conative (Xem use case PO) **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Default display:** Yes |
| 11 | ATS | The number of units of a variant that are currently for sale | **Sort**  Sort A-Z và ngược lại  **Formula** ATS \= Stock \+ On Order  **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Default display:** Yes |
| 12 | Sales per day | The average number of items sold in a day. | **Sort**  Sort A-Z và ngược lại  **Formula** Average quantity sold per day **Rule** Cập nhật theo time range user chọn   **Default display:** Yes |
| 13  | Sales per day (In stock) | The average number of products sold in a day. (accounting only for days when the product is in stock) | **Calculation** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27) **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description  |
| 14 | Sales per day (Out of stock) | The average number of products sold in a day. (accounting only for days when the product is out of stock) | **Calculation**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B27)  **Default column** Yes  **Sort** Theo A-Z và ngược lại **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 15 | Sales days left |  | **Default display:** Yes **Sort** Theo A-Z và ngược lại |
| 16 | Days since stock out  | *Number of days since stock reached zero* | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B33) **Default column** Yes  **Sort** Theo A-Z và ngược lại |
| 17 | Expected stockout days | The period between the date when stock runs out and the date when the purchased items, including pre-sale quantities, replenish the stock. | **Case 1: On Order \+ Stock \- Sales forecast \> 0** Trả kết quả theo formula  **Case 2: On Order \+ Stock \- Sales forecast \<=0** Trả kết quả \= null **Case 3: Stock \> 0** Trả kết quả \= null **Case 4: Stock \<=0 & Sum (on order) \-  ABS(stock) \< 0**  Trả kết quả \= null **Case 5: Stock \<=0 & Sum (on order) \-  ABS(stock) \> 0** Trả kết quả theo Formula  **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B29) **Default column** Yes **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description **Sort** Theo A-Z và ngược lại |
| 18 | Opportunity cost | Opportunity cost when an item is out of stock | **Case 1: Expected Stockout days \= null** Trả kết quả null **Case 2: On Order \+ Stock \- Sales forecast \> 0** Trả kết quả theo formula  **Case 3: On Order \+ Stock \- Sales forecast \<=0** Trả null **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B30) **Default column** Yes **Sort** Sort A-Z và ngược lại  **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description |
| 19 | Expected stockout days (If reorder today) | Expected stockout period if you reorder out-of-stock item today. Calculated by summing days since stockout and lead time | **Case 1: On Order \+ Stock \- Sales forecast \> 0** Trả kết quả \= null **Case 1: On Order \+ Stock \- Sales forecast \<=0** Trả kết quả theo Formula **Formula**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B32) **Default column** Yes **Sort** Sort A-Z và ngược lại  **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description  |
| 20 | Opportunity Cost (if reorder today) | Expected retail sales loss if you reorder out-of-stock item today | **Case 2: On Order \+ Stock \- Sales forecast \> 0** Trả null **Case 3: On Order \+ Stock \- Sales forecast \<=0** Trả kết quả theo Formula **Formula**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B32) **Default column** Yes **Sort** Sort A-Z và ngược lại  **Tooltips** Hiển thị khi user hover vào field header. Content dùng theo description |
| 21 | Gross margin | Net Revenue minus Cost of Goods Sold | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 22 | Gross profit | Net Revenue minus Cost of Goods Sold and Operating Expenses. | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
| 23 | Action |  | **Case 2: On Order \+ Stock \- Sales forecast \<=0 Wording:** Order \[x+\]\* today to avoid stockout \*\[x\]: result of the Formula Nếu x \> 0 \=\> Trả kết quả theo formula  Nếu x \< 0 \=\> Trả kết quả \= null **Formula**  [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B32) **Sort** Sort A-Z và ngược lại  |
| 24 | Compare-at-price | The comparison of the original price and the sale price. | **Default Column**  No  **Sort** Theo A-Z và ngược lại  **Tooltip** Hiển thị khi user hover vào field header. Content dùng theo description |
|  | Cost |  | **Formula** [Link](https://docs.google.com/spreadsheets/d/1vJk2RCeJrFZrsF8g3a5e5ry0bphHopV4uKraTkGJxu0/edit#gid=0&range=B42) **Default Column**  No  **Sort Theo A-Z và ngược lại Tooltip** Chưa có content |
|  | Bar code |  | **Default Column**  No  **Sort** Theo A-Z và ngược lại  |

# **UC 12.5 Advanced Filter in Gap Analysis**

## **1.1. Mục tiêu**

Trên các trang Gap Analysis, user có thể filter các metrics và lưu lại lại filter thành custom report.

## **1.2. Input** 

Filter (select)

Condition (Operators)

Filter values 

## **1.3. Output**

Có thể filter các metrics và lưu lại filter thành custom report 

## **1.4. Workflow** 

### **Main flow (Happy case)**

1\. Trên trang Gap Analysis, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Chọn \[Apply Filter\]

8\. Hệ thống trả về dữ liệu theo điều kiện filter

**Alternative Flow 1**

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Người dùng xóa bớt value bằng cách tick vào \[x\] bên cạnh value 

8\. Chọn \[Apply Filter\]

9\. Hệ thống trả về dữ liệu theo điều kiện filter

### **Alternative Flow 2**

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Người dùng chọn \[+\] để thêm Metric muốn lọc 

4\. Người dùng chọn \[Add\] / \[Or\] 

5\. Người dùng tiếp tục chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

6\. Người dùng muốn tiếp tục chọn thêm Metric: quay lại step 3, nếu không sang step 7\.

7\. Chọn \[Clear All\]

8\. Xóa các filter đã lựa chọn 

### **Exceptional flow 1**

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]

2\. Người dùng không chọn filter & điều kiện filter:

* \[Select Filter\] và chọn field thông tin muốn filter

  * Chọn \[Condition\] để chọn điều kiện filter

  * Nhập giá trị filter vào field \[Value\]

  * Chọn \[Add new filter\] để thêm filter

3\. Chọn \[Apply Filter\]

4\. Hệ thống thông báo lỗi và yêu cầu user chọn filter.

### **Exceptional Flow 2** 

1\. Trên trang Product Performance / Dashboard, người dùng bấm \[Filter\]  
2\. Người dùng không chọn filter & điều kiện filter  
3\. Người dùng không tìm kiếm thấy filter value ở field \[Value\]   
4\. Hệ thống trả về thông báo lỗi. Tham chiếu message ở file **[Notification & Message](https://docs.google.com/spreadsheets/d/1Om4C5uLWiSbsgW8zE_8maZ8y_oXH-yO65g5nB4pIelA/edit#gid=435085563)**

# **UC 12.2 Search variant in Gap Analysis**

## **Mục tiêu**

Người dùng có thể tìm kiếm sản phẩm bằng cách nhập SKU, Product Title, Variant title, Barcode. 

## **Input**

Truyền vào Barcode / Product title / Variant title/  SKU

## **Output**

Trả dữ liệu theo Use case **12.1**

## **Workflow**

### **Main flow**

1\. Trên trang Gap Analysis, user bấm vào thanh \[Search\]

2\. Hệ thống đề xuất 5 sản phẩm được tìm kiếm gần đây nhất

3\. Người dùng nhập thông tin để tìm kiếm sản phẩm 

2. Shopify: Người dùng có thể tìm kiếm sản phẩm bằng cách nhập SKU, Product Title, Variant title, Barcode. 

4\. Hệ thống trả về dữ liệu sản phẩm theo điều kiện tìm kiếm

5\. Kết thúc use case 

### **Alternative flow**

3a. Người dùng chọn sản phẩm theo đề xuất của hệ thống 

- Hệ thống trả về dữ liệu sản phẩm theo điều kiện tìm kiếm

3. View Product: Trả về product 

4. View Variant: Trả về variant 

- Kết thúc use case 

### **Exceptional flow**

4a. Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

- Kết thúc use case.

## **Business Rule**

- Tìm kiếm theo Product title: search gần đúng 

- Tìm kiếm theo SKU: search gần đúng 

- Tìm kiếm theo Barcode: search gần đúng 


# **UC 12.3. Select time range**

## **Mục tiêu**

Người dùng có thể chọn thời gian mà họ muốn xem dữ liệu của sản phẩm

## **Workflow**

### **Main flow**

1\. Trên trang Gap Analysis, người dùng bấm vào \[Calendar\]

2\. Hệ thống hiển thị popup để chọn khoảng thời gian

3\. Người dùng chọn khoảng thời gian mong muốn xem dữ liệu bằng cách chọn time range \[Date range\] có sẵn hoặc chọn ngày start date / end date trên lịch 

4\. Người dùng bấm **Apply** để lưu thời gian vừa chọn

5\. Hệ thống trả về dữ liệu theo khung thời gian tương ứng 

6\. Kết thúc use case 

### **Exception flow**

3a. Người dùng chọn khoảng thời gian trong tương lai

- Disable các ngày trong khoảng thời gian đó

5a.  Hệ thống trả về dữ liệu rỗng (Không tìm thấy kết quả theo điều kiện tìm kiếm) 

- Hiển thị màn hình thông báo lỗi không tìm thấy kết quả *“SORRY\! No data found \- Please try searching other keywords or adjusting your filter”*

- Kết thúc use case.

## **Business Rule**

1\. Quy định hiển thị

5. Khoảng thời gian mặc định: Last 30 days (30 ngày gần nhất) 

6. Khi người dùng filter theo time range có sẵn của Conative, start date & end date tự động được highlight theo khoảng thời gian tương ứng, và ngược lại. 

2\. Quy định time zone mặc định trên Conative

- Default time zone: UTC \-4 (Eastern Time) 

2\. Quy định về khung thời gian có sẵn trên Conative

Time zone mặc định: 

22. Today

23. Yesterday

24. Last 7 days: 

    1. Starting date: 7 days before (including yesterday)

    2. End date: Yesterday

25. Last 30 days: 

    1. Starting date: 30 days before (including yesterday)

    2. End date: Yesterday

26. This month

27. Last month

28. Last 3 months

29. This year

30. Last year 

31. Week to date: 

    1. Starting date: ngày thứ Hai của tuần gần nhất

    2. End date: Today

32. Year to date:

    1. Starting date: ngày đầu tiên của năm gần nhất (Vd: 2023 \> Starting time là ngày 1/1/2023)

    2. End date: Today

    3. Quarter to date

    4. Starting date: ngày đầu tiên của quý gần nhất (Vd: Q2/2023 \> Starting time là ngày 1/4/2023)

    5. End date: Today

# **UC 12.4 Config column \- Gap Analysis**

## **Mục tiêu**

Chọn/ thay đổi metric muốn hiển thị ở trang Gap Analysis

### **Main flow (Happy case)**

8. Trên trang Gap Analysis, user chọn **\[Config column\]**  
9. Hệ thống hiển thị popup Config column   
10. User nhập tên field vào thanh search để tìm và add / remove các field chưa có / đã có trong table   
11. User kéo thả field để thay đổi vị trí của các field đã add vào table   
12. User chọn \[x\] để remove các field không cần thiết ra khỏi table   
13. User chọn **\[Save changes\]** để cập nhật   
14. Hệ thống cập nhật thay đổi, hiển thị thông báo đến user 

2\. Người dùng search và chọn metric (chưa hiện có) để thêm vào bảng dữ liệu sản phẩm 

3\. Người dùng chọn \[Modify columns\] 

4\. Hệ thống trả dữ liệu theo column đã chọn 

5\. Kết thúc use case 

### **Alternative Flow 1**

2a. Người dùng chọn \[Select all\] trong \[add column\] để chọn hiển thị tất cả các metric  

### **Alternative Flow 2**

2b. Người dùng kéo thả metric để sắp xếp thứ tự cột trong bảng dữ liệu 

### **Alternative Flow 3**

2c. Người dùng chọn \[Clear all\] trong \[add column\] để xóa các metric đã chọn 

### **Alternative Flow 4**

3a. Người dùng chọn \[Restore default\] 

4\. Hệ thống trả lại dữ liệu mặc định     

## **Business rule**

Quy định hiển thị và thao tác 

**Thứ tự hiển thị field mặc định cho user mới:** 

| STT | Field  | Business rules for Config column |
| :---- | :---- | :---- |
| 1 | Variant title | **Rule** Mặc định hiển thị ở đầu table  Không được remove hay thay đổi vị trí (Không có CTA \[x\] & icon kéo thả) |
| 2 | SKU | **Rule** Có thể thay đổi vị trí Có thể remove |
| 3 | Variant ID | **Rule** Có thể thay đổi vị trí Có thể remove |
| 4 | Gross Sales | **Rule** Có thể thay đổi vị trí Có thể remove |
| 5 | Gross Quantity | **Rule** Có thể thay đổi vị trí Có thể remove |
| 6 | Next Arrival Date | **Rule** Có thể thay đổi vị trí Có thể remove |
| 7 | Next Arrival Quantity  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 8 | Balance | **Rule** Có thể thay đổi vị trí Có thể remove |
| 9 | Stock | **Rule** Có thể thay đổi vị trí Có thể remove |
| 10 | On order | **Rule** Có thể thay đổi vị trí Có thể remove |
| 11 | ATS | **Rule** Có thể thay đổi vị trí Có thể remove |
| 12 | Sales per day | **Rule** Có thể thay đổi vị trí Có thể remove |
| 13 | Sales per day (In stock) | **Rule** Có thể thay đổi vị trí Có thể remove |
| 14 | Sales per day (Out of stock) | **Rule** Có thể thay đổi vị trí Có thể remove |
| 15 | Sales days left | **Rule** Có thể thay đổi vị trí Có thể remove |
| 16 | Days since stock out  | **Rule** Có thể thay đổi vị trí Có thể remove |
| 17 | Expected stockout days | **Rule** Có thể thay đổi vị trí Có thể remove |
| 18 | Opportunity cost | **Rule** Có thể thay đổi vị trí Có thể remove |

# 

#  **UC 14 \- ABC Analysis**

## **Mục tiêu**

User có thể xem được danh sách top product đóng góp nhiều nhất vào 80% gross sales. User có thể customize bằng cách nhập % gross sales khác để lọc được danh sách product tương ứng

Theo từng grade, user có thể xem được: 

- số lượng product & variant  
- tổng gross sales  
- Field Product Grade trong bảng Product Performance: Filter, Config column, export  
- Data của từng product & variant trong bảng product performance 

https://devtak.cbidigital.com/projects/conative-paas/work\_packages/29836/files

**Bổ sung**

**Phân loại nhóm sản phẩm thành 3 grade. Mặc định:**

Grade A: các sản phẩm có gross sales cao nhất tạo ra 80% gross sales cho brand

Grade B: Các sản phẩm tạo ra 15% gross sales cho brand

Grade C: Các sản phẩm có gross sales thấp nhất tạo ra 5% gross sales cho brand

User có thể tuỳ chỉnh % cho từng grade trong mục Settings của Product Grade by Revenue. Ví dụ: Grade A: 70%,  Grade B: 20%, Grade C: 10% 

### **Main flow (Happy case)**

**~~Hiển thị / ẩn block Product grade by revenue~~**

1. ~~Ở trang Product Performance, user chọn \[Insights\] bên cạnh time range để hiển thị / ẩn block Product grade by revenue (CHọn lại lần nữa thì sẽ ẩn block đi)~~  
2. ~~Hiển thị block Product Grade by revenue~~  
3. ~~Kết thúc use case~~ 

**Grade Settings**

1. Ở Block product ABC Analysis, user chọn settings  
2. User set % cho Grade A, Grade B, Grade C  
3. User chọn:  
- \[x\]: để quay lại trang  
- \[Restore Default\]: Quay trở lại setting mặc định  
- \[Apply\]: cập nhật settings  
4. Hệ thống cập nhật settings, thông báo cập nhật thành công  
5. Kết thúc use case 

### **Exceptional flow \- Để trống % gross sales trong Settings**

1. User để trống ô Set % cho một trong các grade hoặc cả 3 grade  
2. Hệ thống kiểm tra thông tin nhập vào không hợp lệ, thông báo lỗi  
3. Kết thúc use case

### **Exceptional flow \- Nhập giá trị % gross sales không đúng format trong Settings**

1. User nhập sai format ô Set %  
2. Hệ thống kiểm tra thông tin nhập vào không hợp lệ, thông báo lỗi  
3. Kết thúc use case 

### **Exceptional flow \- Nhập giá trị % gross sales cao hơn Max value hoặc thấp hơn Min value trong Settings**

1. User nhập % Gross sales của các grade ngoài khoảng Min, Max   
4. Hệ thống kiểm tra thông tin nhập vào không hợp lệ, thông báo lỗi  
5. Kết thúc use case 

### **Exceptional flow \- Tổng % gross sales của 3 grade lớn hơn hoặc bé hơn 100% trong Settings**

2. User nhập % gross sales của 1 grade làm tổng % gross sales của 3 grade \> hoặc \< 100%  
6. Hệ thống kiểm tra thông tin nhập vào không hợp lệ, thông báo lỗi  
7. Kết thúc use case 

## **Business rule**

**Quy định hiển thị và thao tác**

**Block ABC Analysis**

- Mặc định hiển thị trên trang Product Performance  
- “X” products: số lượng products / variant theo từng grade được đếm theo % trong Settings  
- Gross sales: Tổng gross sales của các products / variants theo từng grade


**Settings \- Field % of Gross sales**

- Default value:  
  - A-Grade: 80%  
  - B-Grade: 15%  
  - C-Grade: 5%  
- Max value:   
  - A-Grade: 90%  
  - B-Grade: 40%.  
  - C-Grade: 5%


- Min value:  
  - A-Grade: 50%  
  - B-Grade: 10%  
  - C-Grade: 0%  
-   
- Sum of 3 grade luôn bằng 100%  
- Luôn hiển thị “%”, user chỉ cần nhập số (Số nguyên)


Field % of Gross sales

- Default value \= 80%  
- Cho phép user thay đổi   
- Bắt buộc nhập


Design: 

# **UC 13.1 Forecasting Settings**

## **Mục tiêu**

User có thể thay đổi forecasting range (days) cho các dữ liệu AI forecast ở trang settings. 

## **Scope**

- Cấu hình ở trang settings  
- Metric Sales Forecast (AI) \+ date range ở trang Product Performance/Dashboard (product, variant level) và Sales Forecast (AI) \+ date range ở Replenishment Flow (variant level)  
  \*Sales Forecast (AI) thay cho metric Next 90-day sales (AI)  
  Công thức:

|  | Product level | Variant level |
| :---- | :---- | :---- |
| Sales Forecast (AI) \+ date range | **Date range**Format: MMM DD, YYYY \- MMM DD, YYYY Formula: lấy theo start date và end date trong setting Forecasting Range**Metric** **Output Formula:**sum AI của date range thuộc variant 1+....+sum AI của date range thuộc variant n | **Date range**Format: MMM DD, YYYY \- MMM DD, YYYY Formula: lấy theo start date và end date trong setting Forecasting Range **Metric** **Output Formula:**sum AI của date range thuộc variant  |

## **Input** 

- Forecast range (Days) ở Settings

## **Output** 

- Dashboard, Product Performance, Replenishment Flow: thay đổi dữ liệu Sales Forecast (AI) \+ Date range  
- Giá trị input thay đổi giá trị date range ở title của metric

### **Main flow (Happy case)** 

1. Ở trang settings, mục Forecasting Range user nhập số ngày forecast mong muốn (Đây là số ngày dùng để forecast từ ngày hiện tại)  
2. Hệ thống cập nhật và thông báo cập nhật thành công   
3. Ở trang Product Performance, cập nhật field Next “xx”-day forecast:   
   1. Title “Next “xx”-day forecast” sẽ được cập nhật số ngày tương ứng với forecasting range (Ví dụ: Forecasting range \= 120 days \=\> Title: Next 120-day forecast)  
   2. Data AI forecast được cộng theo số ngày mới được cập nhật

## **Business rules** 

Quy định hiển thị và thao tác 

Settings: 

- Default forecasting range: 90 days  
- Max range user được nhập: 365 days

Data Sales Forecast

- Data AI forecast (Field Next “xx”-day forecast) được cộng theo số ngày mới được cập nhật. (Áp dụng ở các trang: Dashboard, Product Performance, Overstock, Gap analysis)

## **References** 

Design: [https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative\_New?type=design\&node-id=4350-87709\&mode=design\&t=kA9YwzIg2XKecuWE-4](https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative_New?type=design&node-id=4350-87709&mode=design&t=kA9YwzIg2XKecuWE-4)

![][image9]

# **UC 13.2 Replenishment Settings    \`\`\`**

## **Mục tiêu**

User có thể thay đổi các settings liên quan đến Lead time & Days of stock của variant cho tất cả các report liên quan

## **Input** 

- Days of stock (Apply for all variants)  
- Lead time (Apply for all variants)

## **Output** 

- Days of stock (All reports)  
- Lead time (All reports)  
- Action (Lead time \- Gap Analysis)  
- Reorder quantity (Replenishment flow)  
- Sales forecast (Replenishment flow)

### **Main flow (Happy case)** 

4. Trên sidebar menu, user chọn \[Settings\]  
5. Hệ thống redirect đến trang Settings  
6. User nhập Days of stock & Lead time  
7. User chọn \[Save\] để lưu lại setting

## **Business rules** 

- Mặc định lead time=45 ngày cho brand mới  
- Mặc định days of stock \=90 ngày cho brand mới  
- Khi thay đổi lead time, days of stock ở Settings \> chỉ thay đổi lại lead time, days of stock cho các variant trong trường hợp hợp lead time, days of stock của variant đó chưa được chỉnh sửa   
- Tổng của lead time \+ days of stock \<= 365 

**Design**  
[https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative\_New?type=design\&mode=design\&t=BrxuLIdJrn8cK6sf-0](https://www.figma.com/file/C3694nRiIEv1kXmfaG6zaQ/Conative_New?type=design&mode=design&t=BrxuLIdJrn8cK6sf-0)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAMCAYAAABSgIzaAAAAlUlEQVR4XrXPMQrDIBiG4Rwza0AQ3J2dHDxANm/g5OA5vEOmDA4Oipn8SjIUNGkbAn1HPx5+HPCwoX+4239grRXOOSiloLVutq/QGAPOOdZ1xTzPzfYRllIgpUTOGeM4IsbY7JfQWgshBLz3IIT089ElpJRi2zZM03RcvuoEQwhYlgWMMaSU+vndCe5/2vGvTvBuj+ELIwSGz6xkt7kAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAaCAYAAADSbo4CAAABB0lEQVR4Xu2WPQqEMBBG90gqFhZi4yXEUvQednoIQSy8g4WNvQgexV6ZZQJukYExcZUNiw8+kMxkeP5AfIEhvOSFX/GIyCiLxHEMlmWdCu49QkmkKAoyXDc4g0NJxPd9Mlg3OINDSUQeejYc/y3SdR0kSULWOS4X8TxP7KmqitQ4LhWxbRuGYYB5nsF1XVLnuFSkrmvRHwQBqd0iUpalWJ+mCRzHgTRNYV1X2LYNsiwj/beJ4CsYx1HU+r6HZVnEdZ7npPdWEUwYhh8BpGka0iOH47QIJooi8XG2bSueklyXw/GViG44lESMOWuMOX0RI/5HdvCudF4T9h49iR0tkTt5RGSMEXkDu/T9wgXcej0AAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAiCAYAAAAkjjtxAAAArklEQVR4Xu2XsQ1DIQxE/0gMwASMwEIUDADbErlI458ourOsxJGfdA3C8GRRmOsE49ILv04Ke5PC3lDCY4xTaz2lFChSI7UWYOHe+00EjZzBAglLd/TlbNhOQ8LMM3gXOYsBEtaXWsOQwkgYUhgJg1m4tXbmnB8j+3Qtg1l4raW3vWTvfatlMAuH67AlDCmMhOG/hcMNP+HGSyHUAP8k1Bfp26SwNynsTQp7E074AUXD1HZDwJ6wAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAWCAYAAADAQbwGAAAAf0lEQVR4XmP4T2XAgC5AKRiiBp67dP3/8dMX8eKrN++gawMDFAM/fvryv3/G4v+Pn74gCoPUogMUA+cuXYfMJQqgG4pi4M59x5C5RIFRA0cNHPQGrt60C5lLFMBrICjTL1m9BVkIL0A3DAQwSpuPnz6DFRLCuPI9hoGUgsFvIAAck6l6VOaZ4QAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAfCAYAAADwbH0HAAABFklEQVR4Xu2WPQrCQBBGcwFP4AX0bp7Azs7OSg9iIyIYe2uLYKeFCIIGxZjfNSOsJN/uRt2NESQPvmaSmbfDEojFfoSFhaqoxZVRiwW2wYWtfZc5t9PHcaMAxz0pFOMg3cRJgqPVYjfyhQG6OUQejleLsdk0iFQcJLHQaBrkf8RdZ8Eakz6bHze5OlKquLOaMmvce6RSMZfSxvgMKUXctkfKTY3FNJQEy/M+V2/OBi+lRuKsgOQk4TXZgTDI22IScTGJ6B6zB8H3McjbYi7Pbk7Bd1RBPhLztOxh+r3aQr0oiJZYJ4hUHLNEaDQNIhUTh9ATmnWzC644Xi0uc+swvTpEKSbornV/eyhb/yyVEoXib1KLK+MOc8bt+jkSLWoAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB0AAAAfCAYAAAAbW8YEAAABAElEQVR4XmN4/enPf3pjBnQBeuBRS/+Xbfv932vB7/82M8jDIL3oZuK1NH3dr/+MNb/+CzX/+q/UQx4G6Zfv+vV/0VlMyzEsBSlu3PvnPzXA/Xf/wA6485qApSBF1AT77/39X74N1bcolm648uf/grN/0fVRDEDBPGrpqKUUg6FjKSiTJ6z5TRAXbMVeqJBl6ftv//+vv/oXLIcPgwoCbIAsSykFo5aOWkoVgNfSO6/+4MxrlACbmXgsBWGhll/gwoBaYMLRP/+nHCVgaes+SPsGpBiU2UEOIAevv/YXbI5C908U87FaCsKLzvwGa6AUg4L13BNM87FaSms8ailNMQCVmTYasdikvAAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,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>

[image8]: <data:image/png;base64,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>

[image9]: <data:image/png;base64,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>