# Data test Import PO

> Nguồn: [Google Sheet – 75191_Import Purchase Order Updates (UC4)_Checklist](https://docs.google.com/spreadsheets/d/1lxfkZKZZ9ju53dzojPtXzRk2tfX8fazY0IrPes-6DDQ/edit?gid=125841885#gid=125841885)
> Tab: `Data test Import PO`

Tổng số dòng có dữ liệu: **241**.

## Dữ liệu

| Cột 1 | Cột 2 | Cột 3 | Cột 4 | Cột 5 | Cột 6 | Cột 7 | Cột 8 | Cột 9 | Cột 10 | Cột 11 | Cột 12 | Cột 13 | Cột 14 | Cột 15 | Cột 16 | Cột 17 | Cột 18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Case | Sub-case | Expected | Data test |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import 1 line |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import với điều kiện PO chưa tồn tại trong hệ thống |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import thành công khi nhập tất cả field thông tin |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 01 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 01 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 5 | Current date | Received | Received | 0 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 01 | Velocity | Staci Avondale | 2040 | 5 | 5 |  | 5 |  |  |  |  | Chờ confirm | 5 | Delivered |
| Import PO thành công khi file import không có data tại cột Received Qty |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Import thành công PO với status Open |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO |  | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 02 | Velocity | Staci Avondale | 2040 | 5 |  |  | 5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 02 | Velocity | Staci Avondale | 2040 | 5 |  |  | 5 | Current date | Open |  | 5 |  |  |  |
|  |  | Không tạo shipment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO |  | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 03 | Velocity | Staci Avondale | 2040 | 5 |  | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 03 | Velocity | Staci Avondale | 2040 | 5 |  |  | 5 | Current date | Open |  | 5 |  |  |  |
|  |  | Không tạo shipment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import PO thành công khi file import có data tại cột Received Qty = 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Import thành công PO với status Open |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO |  | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 04 | Velocity | Staci Avondale | 2040 | 5 | 0 |  | 2,5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 04 | Velocity | Staci Avondale | 2040 | 5 |  |  | 2,5 | Current date | Open |  | 5 |  |  |  |
|  |  | Không tạo shipment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO |  | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 05 | Velocity | Staci Avondale | 2040 | 5 | 0 | 2026-09-25 | 2,5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 05 | Velocity | Staci Avondale | 2040 | 5 |  |  | 2,5 | Current date | Open |  | 5 |  |  |  |
|  |  | Không tạo shipment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import PO thành công khi file import có data tại cột Received Qty > 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Import thành công PO với status Partially Received và số lượng Received Qty <  Order Qty |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 06 | Velocity | Staci Avondale | 2040 | 5 | 2 | 2026-09-25 | 2,5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 06 | Velocity | Staci Avondale | 2040 | 5 | 2 | 2026-09-25 | 2,5 | Current date | Partially Received | Under Received | 0 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 06 | Velocity | Staci Avondale | 2040 | 5 | 2 |  | 2,5 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  | Import thành công PO với status Received và số lượng Received Qty =  Order Qty | Đã thực hiện ở case Import thành công khi nhập tất cả field thông tin |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Import thành công PO với status Received và số lượng Received Qty >  Order Qty |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 07 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026-09-25 | 2,5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 07 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026-09-25 | 2,5 | Current date | Received | Over Received | 0 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 07 | Velocity | Staci Avondale | 2040 | 5 | 9 |  | 2,5 |  |  |  |  | Chờ confirm | 9 | Delivered |
| Import PO thành công khi file import có data tại cột Received Date hợp lệ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 08 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026-09-25 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 09 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026-9-7 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 10 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026-09-7 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 11 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026-9-07 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 20 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026/09/25 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 21 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026/9/7 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 22 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026/09/7 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 23 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026/9/07 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 24 | Velocity | Staci Avondale | 2040 | 5 | 9 | 25/09/2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 25 | Velocity | Staci Avondale | 2040 | 5 | 9 | 7/9/2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 26 | Velocity | Staci Avondale | 2040 | 5 | 9 | 7/09/2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 27 | Velocity | Staci Avondale | 2040 | 5 | 9 | 07/9/2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 28 | Velocity | Staci Avondale | 2040 | 5 | 9 | 25-09-2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 29 | Velocity | Staci Avondale | 2040 | 5 | 9 | 7-9-2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 30 | Velocity | Staci Avondale | 2040 | 5 | 9 | 7-09-2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 31 | Velocity | Staci Avondale | 2040 | 5 | 9 | 07-9-2027 | 2,5 |  |  |  |  |  |  |  |
| Kiểm tra import PO thất bị khi import thông tin invalid |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Received Qty < 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 12 | Velocity | Staci Avondale | 2040 | 5 | -5 | 2026-09-25 | 2,5 |  |  |  |  |  |  |  |
|  | Received Qty là số thập phân |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 13 | Velocity | Staci Avondale | 2040 | 5 | 2.5 | 2026-09-25 | 2,5 |  |  |  |  |  |  |  |
|  | Received Date không hợp lệ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 14 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026-25-09 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 15 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2026/25/09 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 16 | Velocity | Staci Avondale | 2040 | 5 | 9 | 09/25/2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 17 | Velocity | Staci Avondale | 2040 | 5 | 9 | 09-25-2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 18 | Velocity | Staci Avondale | 2040 | 5 | 9 | 09-2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 19 | Velocity | Staci Avondale | 2040 | 5 | 9 | 09/2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 20 | Velocity | Staci Avondale | 2040 | 5 | 9 | 2027 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 21 | Velocity | Staci Avondale | 2040 | 5 | 9 | 25/09/27 | 2,5 |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 22 | Velocity | Staci Avondale | 2040 | 5 | 9 | 25-09-27 | 2,5 |  |  |  |  |  |  |  |
| Import với điều kiện PO đã tồn tại trong hệ thống |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import thành công |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Draft -> Open |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tạo PO Draft |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 29 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Draft |  |  |  |  |  |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 29 | Velocity | Staci Avondale | 2040 | 4 |  |  | 7 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 29 | Velocity | Staci Avondale | 2040 | 9 |  |  | 7 | Current date | Open |  | 9 |  |  |  |
|  |  | Không tạo shipment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Draft -> Partial Received |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tạo PO Draft |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  | PO detail trên UI | CBI TEST DP 30 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Draft |  |  |  |  |  |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 30 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 30 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 30 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 30 | Velocity | Staci Avondale | 2040 | 10 | 5 | 2026-09-25 | 7 | Current date | Partial Received | Under Received | 5 |  |  |  |
|  |  |  | CBI TEST DP 30 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  | Received | 0 |  |  |  |
|  |  |  | CBI TEST DP 30 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  | Not Received | 3 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 30 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  |  |  | CBI TEST DP 30 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  | Draft -> Received |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tạo PO Draft |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  | PO detail trên UI | CBI TEST DP 32 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Draft |  |  |  |  |  |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 32 | Velocity | Staci Avondale | 2040 | 5 | 10 | 2026-09-25 | 7 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 32 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 32 | Velocity | Staci Avondale | 2040 | 10 | 10 | 2026-09-25 | 7 | Current date | Received | Received | 0 |  |  |  |
|  |  |  | CBI TEST DP 32 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  | Received | 0 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 32 | Velocity | Staci Avondale | 2040 | 5 | 10 | 2026-09-25 | 7 |  |  |  |  | Chờ confirm | 10 | Delivered |
|  |  |  | CBI TEST DP 32 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  | Chờ confirm | 10 | Delivered |
|  | Pending Approved -> Open |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tạo PO Pending Approved |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 33 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Pending Approved |  |  |  |  |  |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 33 | Velocity | Staci Avondale | 2040 | 4 |  |  | 7 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 33 | Velocity | Staci Avondale | 2040 | 9 |  |  | 7 | Current date | Open |  | 9 |  |  |  |
|  |  | Không tạo shipment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Pending Approved -> Partial Received |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tạo PO Pending Approved |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  | PO detail trên UI | CBI TEST DP 34 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Pending Approved |  |  |  |  |  |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 34 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 34 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 34 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 34 | Velocity | Staci Avondale | 2040 | 10 | 5 | 2026-09-25 | 7 | Current date | Partial Received | Under Received | 5 |  |  |  |
|  |  |  | CBI TEST DP 34 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  | Received | 0 |  |  |  |
|  |  |  | CBI TEST DP 34 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  | Not Received | 3 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 34 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  |  |  | CBI TEST DP 34 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  | Pending Approved -> Received |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tạo PO Pending Approved |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  | PO detail trên UI | CBI TEST DP 35 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Pending Approved |  |  |  |  |  |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 35 | Velocity | Staci Avondale | 2040 | 5 | 10 | 2026-09-25 | 7 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 35 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 35 | Velocity | Staci Avondale | 2040 | 10 | 10 | 2026-09-25 | 7 | Current date | Received | Received | 0 |  |  |  |
|  |  |  | CBI TEST DP 35 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  | Received | 0 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 35 | Velocity | Staci Avondale | 2040 | 5 | 10 | 2026-09-25 | 7 |  |  |  |  | Chờ confirm | 10 | Delivered |
|  |  |  | CBI TEST DP 35 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  | Chờ confirm | 10 | Delivered |
|  | Open -> Partial Received |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tạo PO Open nhưng không có shipment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  | PO detail trên UI | CBI TEST DP 36 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Open |  |  |  |  |  |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 36 | Velocity | Staci Avondale | 2040 | 10 | 5 | 2026-09-25 | 7 | Current date | Partial Received | Under Received | 5 |  |  |  |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  | Received | 0 |  |  |  |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  | Not Received | 3 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 36 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  | Tạo PO Open nhưng có shipment Schedule / In transit | Chờ confirm |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  | PO detail trên UI | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Open |  |  |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 | 5 |  | 7 |  |  |  |  | CBITESTDPShipment37 | 5 | Schedule |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 10 | 5 | 2026-09-25 | 7 | Current date | Partial Received | Under Received | 5 |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  | Received | 0 |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  | Not Received | 3 |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 | 5 |  | 7 |  |  |  |  | CBITESTDPShipment37 | 5 | Schedule |
|  |  | Shipment detail trên UI | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  | Open -> Received |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tạo PO Open nhưng không có shipment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  | PO detail trên UI | CBI TEST DP 36 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Open |  |  |  |  |  |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 36 | Velocity | Staci Avondale | 2040 | 10 | 5 | 2026-09-25 | 7 | Current date | Partial Received | Under Received | 5 |  |  |  |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  | Received | 0 |  |  |  |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  | Not Received | 3 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 36 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  |  |  | CBI TEST DP 36 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  | Tạo PO Open nhưng có shipment Schedule / In transit | Chờ confirm |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  | PO detail trên UI | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 |  |  | 3 | Current date | Open |  |  |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 | 5 |  | 7 |  |  |  |  | CBITESTDPShipment37 | 5 | Schedule |
|  | Sau khi import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 10 | 5 | 2026-09-25 | 7 | Current date | Partial Received | Under Received | 5 |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  | Received | 0 |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | B1463GWTCZ7.5 | 3 |  |  |  |  |  | Not Received | 3 |  |  |  |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 | 5 |  | 7 |  |  |  |  | CBITESTDPShipment37 | 5 | Schedule |
|  |  | Shipment detail trên UI | CBI TEST DP 37 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 7 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  |  |  | CBI TEST DP 37 | Velocity | Staci Avondale | PD-1002 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  | Chờ confirm | 5 | Delivered |
|  | Open |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Partially Fulfilled |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Import PO | PO Number* | Supplier* | Warehouse* | Item SKU* | Order Qty* | Received Qty | Received Date <br>(Received history) | Cost | Created Date | Status PO | Status item | On order | Shipping label | Shipment qty | Status shipment |
|  |  |  | CBI TEST DP 01 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 5 |  |  |  |  |  |  |  |
|  |  | PO detail trên UI | CBI TEST DP 01 | Velocity | Staci Avondale | 2040 | 5 | 5 | 2026-09-25 | 5 | Current date | Received | Received | 0 |  |  |  |
|  |  | Shipment detail trên UI | CBI TEST DP 01 | Velocity | Staci Avondale | 2040 | 5 | 5 |  | 5 |  |  |  |  | Chờ confirm | 5 | Delivered |
| Import thất bại |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import 2 line |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import thành công trùng với PO đã tồn tại trong hệ thống |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import thành công trùng với PO đã tồn tại trong cùng 1 file import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import không thành công trùng với PO đã tồn tại trong hệ thống |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Import không thành công trùng với PO đã tồn tại trong cùng 1 file import |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
