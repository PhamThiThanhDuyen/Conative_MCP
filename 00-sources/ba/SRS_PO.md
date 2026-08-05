# SRS_PO

> Nguồn: [Google Doc SRS_PO](https://docs.google.com/document/d/1V_HqeYuUsi1heLM0Cq3uncJhzGg59KfTBXtuvUlWfHg/edit)
>
> Tài liệu được chuyển sang Markdown từ bản nguồn; nội dung được giữ theo thứ tự đoạn và tab.


## Tab t.0

SOFTWARE REQUIREMENT SPECIFICATION

Purchase order

Document control

Date

Version

PIC - Person in charge

Note

15/1/2025

1.0

Hien Nguyen

In the light ERP package

23/1/2025

1.1

Hien Nguyen

Update based on final design

18/03/2025

1.2

Linh To

Update change status flow of PO

19/11/2025

1.3

Linh To

Update UC 4. Import purchase order

### Introduction

#### Description

The Purchase Order (PO) feature allows users to create, manage, and track purchase orders seamlessly across multiple platforms. This feature integrates data from systems such as Shopify, Conative, and ERP, ensuring a centralized and streamlined process for procurement operations.

#### Scope

Apply for all Org

This improvement version will affect on some fields:

- On order

- Next arrival date

- Next arrival quantity

(Defined later on PDP SRS docs)  - Attached file here

#### General rule - GR

Rule ID

Description

GR01

Edit and Delete Actions:

- Can only be performed on POs created/imported from Conative.

- And based on each status: we have allowed action for each status  (ref:  )

- Disabled for POs synchronized from ERP.

GR02

Search Rules:

- Case-insensitive relative search (IgnoreCase):

- Example: Searching for "C00" will return results like C001, c002, C00, etc.

- Trim()  leading and trailing spaces:

- Example: Searching for " C001 " will return the result "C001".

- No keyword splitting for comparison:

- Example: Searching for "The Snowboard" will only return results like "The Snowboard: Hydrogen" and not "The Collection Snowboard".

- Exact match search:

- Example: Searching for "The Collection Snowboard" will only return "The Collection Snowboard".

Note: When searching for SKU, in addition to the PO list, the system will display all POs containing PO line items matching the corresponding SKU(s).

GR03

Text Input Length Rules

- Regular type (e.g., name): Maximum 255 characters

- Show error message “The input exceeds 255 characters.” when the user input exceeds the limit.

- Note type: Maximum 5000 characters

- Show error message “The input exceeds 5000 characters.” when the user input exceeds the limit.

GR04

We will standardize the headers/titles of table columns by capitalizing the first letter of each word. As for field names in forms, we will keep them as they are, only capitalizing the first letter of the phrase.

Example:

- Field name “PO number” on the creating PO form.

- Column name on the table - PO Number

#### Document

Document

Reference

User Interface

Wireframe: 

Final design: 

Basic workflow - PO

https://g4cc04q89x9.sg.larksuite.com/docx/BYVkd7VxmoRctCxD98nl5knIgSn

Overall flow in SCM

https://g4cc04q89x9.sg.larksuite.com/docx/KY1OdJI2yo2n1Lxa1UNlZvqQghA

PO status

PO item status

Shipment status

#### Message log

ID

Type

Message

Action

M01

Pop-up confirm

Are you sure to delete these purchase orders?

Delete: Delete the PO if it satisfies the condition.

Cancel: Close the modal

M02

Pop-up confirm

Are you sure to delete this purchase order?

Delete: Delete the PO if it satisfies the condition.

Cancel: Close the modal

M03

Pop-up error

You cannot delete the selected PO(s). It has already been processed or received.

Close: Close the modal

M04

In-line error

The field is required

M05

Pop-up error

There are selected items with received quantities already recorded in the inventory. You cannot remove those items.

Close: Close the modal

M07

Pop-up confirm

Do you still want to continue closing this PO without saving?

Leave: close PO without saving
Cancel: Close modal

M08

In-line error

This PO number already exists

M09

Message

Purchase order saved successfully

M10

Message

Purchase order created successfully

M11

Message

Purchase order deleted successfully

### UC 1. View purchase order list

User story

As an inventory staff

I want to view Purchase order list which is sync form ERP (Shiphero, Netsuite,...) or be created on Conative

So that I can manage PO

Actor:

Active user account on Conative (suggested role: Procurement staff, inventory staff)

Trigger:

User click on “Inventory management” > “Purchase Order” on the menu bar in the left side of the screen

Pre-condition:

After login successfully, user is in “Dashboard” Screen

Post-condition:

Users see the PO list

#### 1.1 UI & fields details

LINK: 

Element / ID

Type

Default value

Business rule

Status

Dropdown list

All status

Multiple selection

Value: Draft, Pending approval, Rejected, Open, Partially Fulfilled, Fulfilled, Closed, Canceled.

By default - All statuses.

UI card:

Warehouse

Dropdown list

All warehouses

Multiple selection

Value includes: All created warehouses

By default - All warehouses.

UI & behavior of the dropdown list: 

Search

Input

null

Search rules for item BR01.

Information in the placeholder: Search PO number, item title, SKU, ASIN…

Allow users to search reports based on the following logic:

- Product Title - Fuzzy search
Returns POs containing variants belonging to the searched product.

- Variant Title - Fuzzy search
Returns POs containing the searched variant.

- SKU - Fuzzy search
Returns POs containing the searched variant.

- ASIN (if the product is synced from Amazon) - Fuzzy search
Returns POs containing the searched variant.

- PO Number - Fuzzy search
Returns POs with the searched PO number.

- PO ID - Fuzzy search
Returns POs with the searched PO ID.

When no result is matched to searching value, show message like this:

Create new

Button

Enable

onClick: Display a dropdown list:

- Create new PO: Open a new page to create a PO.

- Import: Display the UI to import PO list.

Filter

Button

Enable

Rule is mentioned below (Business rule for filter)

Column (Sort)

Button

By default: Show sort icon on “Created date” column (from newest to oldest) - BR02

The sort icon will be shown when clicking on the column

Bulk Action

Button

Hidden

Default: Hidden

Show and Enable: Display and enable the feature when at least one row is selected in the table.

onClick: Display a dropdown list (Option: delete)

Delete: Display message log M01 with deletion reference conditions:

- Main flow: The system allows deleting the PO if it meets the following conditions:

- The PO has a status of Draft / Pending Approval / Rejected.

- Display message M11 if deleted successfully.

- Exceptional cases: For other cases, display message M03.

Impact handling after deletion: All information related to the SKUs on that PO will be removed.

PO ID

Text

-

Value: PO ID

Click to open PO detail in new page (Applies to clicking on a table row)

Table

Table

-

Show information:

- PO ID (For purchase orders (POs) obtained from other sources, the PO ID is shown 6 latest characters of the string).

- PO number

- Vendor

- Warehouse (For warehouse sync from Shopify or ERP, only display warehouses with status = Active.)

- Created date: MMM DD, YYYY

- Expected arrival date: MMM DD, YYYY

- Status: status of the PO

- Received status: {received_qty} of {ordered_qty}

- If the PO hasn’t received yet → the card is grey

- If the received qty ≠ ordered qty  → the card is orange

- If the received qty = ordered qty → the card is green

- Action: Show “Delete” (if the POs meet the conditions for deletion) → onClick “Delete” - Show message log M02

- Disable if the PO doesn’t meet conditions for deletion.

Pagination

Text

-

Format show:  Select all Y orders 
Showing X of Y results >

- X: The number of POs displayed on the current page. Normally, we fix 100 results per page.

- Y: The total number of orders that match the selected filters.

In the case where at least one row is selected in the table, the following will be displayed: X selected. Select all Y orders → Clicking this will select all POs and show “All Y results are selected. Clear selection”.

- X: The number of POs/rows selected.

- Y: The total number of orders that match the selected filters.

- If clicking on “Clear selection” → back to default state.

- If at least one row is not selected, the button will be shown again.

#### 1.2. Main flow

- Step 1: User enters credentials to login.

- Step 2: User navigates to the Inventory management section > Purchase order list

- Step 3: The user can filter by status, vendor… → The system displays filtered POs with basic details.

- Step 4: Click to see more info on individual POs.

- Step 5: Take action: Delete or export POs if permissions allow.

#### 1.3. Alternative flow

- 3a. User doesn’t input filters → System displays all available POs by default.

- 3b. When no POs match filters → System displays a message like "You don't have any purchase order yet."

- 3c. User update status of PO from “Draft” to “Open” or “Pending” but there are no items on PO → System displays an error message like “Please add at least one item to the purchase order.”

#### 1.4. Business rule

Rule ID

Rule Title

Rule Description

BR01

Search

Search by PO number, PO ID, SKU, ASIN with criteria according to general rule GR02.

BR02

Display default

Display based on “Created date” -  from newest to oldest

Business rule for filter

Condition is displayed with “is” by default

Rule ID

Rule Title

Type

Condition

Rule Description

F01

Supplier

Multiple select

Is

Is Not

List of vendors created on Conative sync from Shopify / ERP

By default - All vendor

F03

PO ID

Multiple select

Is

Is Not

List: all PO ID

By default - All PO ID

F04

PO Number

Multiple select

Is

Is Not

List: all PO ID

By default - All PO Number

F05

Created date

Single-numeric

Equal

Before

After

Between

Enter or pick the date/date range

- If the user selects "After" / “Before” / “Equal” , he/she can input the specific date.

- If the user selects “between”, he/she can choose a specific date range.

F06

Expected arrival date

Single-numeric

Equal

Before

After

Between

Enter or pick the date/date range

- If the user selects "After" / “Before” / “Equal” , he/she can input the specific date.

- If the user selects “between”, he/she can choose a specific date range.

F07

Received status

Multiple select

Is

Is Not

List: Not received, Under received, Received, Over received.

- Not received: When {received_qty} = 0

- Under received: when {received_qty} < {order_qty}

- Received: when {received_qty} = {order_qty}

- Over received: when {received_qty} > {order_qty}

By default - All statuses

F08

Source

Single

Is

Is Not

By default, the ERP selected by the user during onboarding will be used. If no selection is made, Conative will be displayed.

Note: In the next version, we will introduce a setting for selecting the source. Until then, only one ERP will be applied per organization, so the 'Source' filter will be removed.

### UC 2. Create purchase order

User story

As an inventory staff

I want to create a PO to request purchase when stock levels are low

So that I can ensure that we have enough items in stock to meet future demand.

Actor:

Active user account on Conative

Trigger:

User click Create new > Create new PO on PO list screen

Pre-condition:

User is in “Purchase Order List” Screen

Post-condition:

- Success: The PO is saved in the database and is accessible for further processing.

- Failure: The PO is not created, and the user is informed of the issues.

#### 2.1 UI & fields details

LINK: 

Element / ID

Type

Mandatory

Default value

Business rule

PO ID

Label

-

Auto Generated

The system will automatically generate the PO ID after creating PO according to Conative’s rule (Cxxxxx).

For purchase orders (POs) obtained from other sources, the PO ID is generated using UUID.

PO number

Textbox

Yes

Null

Placeholder: Enter PO number

Tooltip: A number you can create or customize to identify the purchase order on the platform.

Rule:

- There is no space between characters.

- The number of characters <= 50. If the user inputs more than 50 characters → raise error message under the field “This PO ID is not over 50 characters”

- Missing required field → show M04

- PO number is unique

Created date

Datepicker

-

PO’s created date

The system will log the date after the PO is created.

- Uneditable

Expected arrival date

Datepicker

No

Null

Placeholder: Select the date

Functionality: The system displays a datepicker to allow the user to select dates.

Format: MMM DD, YYYY

Expected arrival date >= {Today date}

- Error message under the fields when selecting the past “Expected day should not be in the past”

Vendor

Single selection

Yes

Null

Placeholder: Select vendor

Display a dropdown list of vendors, including vendors created on Conative, Shopify, and ERP, sorted from A-Z.

Allow the user to create a new vendor (as per the current version).

Missing required field → show M04

Warehouse

Single selection

Yes

Null

Placeholder: Select warehouse

Fetch the list of warehouses with status = active from user’s ERP and warehouse from Conative.

Display a dropdown list of warehouses synced from Shopify and ERP, sorted from A-Z.

Missing required field → show M04

Search item

Search

-

-

Placeholder: Search for Title, SKU, ASIN

The user can search the title, SKU, ASIN of the item on the order items list.

When no result is matched to searching value, show message like this:

Add item

Button

-

-

The user can click on the button “Add item” → a popup is shown to allow user selects item

On the popup, a list of item types “variant” and “component” is mixed and sorted by title from A → Z.

- Fields in the popup: Title, SKU, UOM, Type (Variant / Component) & Item status (Draft / Active / Archived) On hand qty

- For the “variant” item, UOM is blank → show “-”

- The user can search by Title and SKU using the criteria defined in general rule GR02 (adding Title search compared to the current version).

- When selecting the checkbox, the system will count the number of items with the format:

- "X selected”

- Where X is the number of items selected.

Item line

-

Yes (depends on next status)

-

The item has been added following the 'Add Item' step

Note: The user can scroll horizontally to view all columns, but the 'Title' column is fixed.

Title

Text

-

-

Name of the selected item is shown

Stock

Number

-

-

The system shows the number of stock items in the selected warehouse

If no warehouse is selected, stock = 0. Once a warehouse is selected, stock updates based on the selected warehouse.

MOQ

Number

-

-

The system fills the MOQ data in the MOQ fields from the Vendor price list.

Order Qty

Number

Yes

Null

Placeholder: Input order qty

The user can input the order qty

Quantity must be a positive number > 0

- Type: int

- Raise error message when the user input qty = 0 - “Quantity must be greater than 0.“

Missing required field → show M04

UOM

Text

-

-

The system fills the UOM of the item.

Production start date

Datepicker

No

Null

Placeholder: Select the date

Functionality: The system displays a datepicker to allow the user to select dates.

Format: MMM DD, YYYY

Estimated completion

Datepicker

NO

Null

Placeholder: Select the date

Functionality: The system displays a datepicker to allow the user to select dates.

Format: MMM DD, YYYY

Completion date

Datepicker

No

Null

Placeholder: Select the date

Functionality: The system displays a datepicker to allow the user to select dates.

Format: MMM DD, YYYY

Cost

Number

Yes

Null

Placeholder: Input item cost

The user can input the cost of the item. The unit is fixed - dollar ($)

The amount  must be a positive number

- The cost >= 0

- Type: decimal (The separator between the integer part and the decimal part is a period (.).

- Allowed characters: up to 131072 digits before the decimal point; up to 16383 digits after the decimal point

- If the user input more than allowance → raise error message under the fields “Please limit the integer part to 131072 digits and the decimal part to 16383 digits.”

- Missing required field → show M04

The cost is autofilled based on settings (sẽ bsung link docs sau)

Total cost

Number

-

0

The total cost per item is calculated based on order qty

Total cost = Order qty * Cost

The user can’t input manually

Total line

Hidden

Total order qty = SUM of all items ordered qty

Total is the total cost of all items on the PO

- Total = Total_cost_1 + Total_cost_2 + …. Total_cost_n

Delete icon

Button

-

Enable

The delete icon (Trash icon) is on each row item allows the user remove item

Note for PO

Text

No

Null

Placeholder: Type here

Limit characters - GR03

Attachments

File

No

Null

The user can upload a file with format: .xls, .xlsx, .pdf, .csv, .doc, .docx

Maximum - 5MB

- If the file > 5MB → raise error message in the toast “The attachment exceeds the size limit of 5MB. Please upload a smaller file."

- If the user selects invalid format file: display message error: Invalid file format.

- If File size exceeds the allowed limit: display message error: The files exceed the allowed size limit.

Remove

Button


Hidden

Enable when the user selects at least one row in the order items table.

onClick: Remove the selected items

Example of the UI:

Cancel

Button

-

Enable

Rule BR1 - UC 2

Save as draft

Button

-

Enable

Create new PO with status Draft, return to PO list page

Issue PO

Button

-

Enable

Create new PO with status Open, return to PO list page

Request approval

Button

-

Enable

Create new PO with status Pending approval, return to PO list page

#### 2.2. Main flow

- Step 1: The user navigates to the "Create Purchase Order" page.

- Step 2: The user input the following details:

- Input the PO number

- Selects a vendor from the dropdown list.

- Selects a warehouse

- Expected arrival date

- Order items: The user selects the item from the popup and then inputs fields:

- Order qty

- Production start date

- Estimated completion

- Completion date

- Cost

- Note for PO

- Attachments

- Step 4: The system calculates the total cost for item line + total for the PO

- Step 5: The user reviews the PO details.

- Step 6: The user selects an action:

- Step 6.1: Save as Draft

- The system validates the PO details. Ensures all mandatory fields are filled.

- If validation passes, the system saves the PO with a “Draft” status  and generates a unique PO ID.

- A success message is displayed: "Purchase order saved as draft successfully."

- Step 6.2: Issue PO

- The system validates the PO details. Ensures all mandatory fields are filled.

- If validation passes, the system saves the PO with an “Open” status and generates a unique PO ID.

- A success message is displayed: "Purchase order created successfully."

- Step 6.3: Pending Approval

- The system validates the PO details. Ensures all mandatory fields are filled.

- If validation passes, the system saves the PO with an “Pending Approval” status and generates a unique PO ID.

- A success message is displayed: "Purchase Order submitted for approval successfully."

#### 2.3. Alternative flow

- 6a. Missing or Invalid Data

- Condition: One or more mandatory fields are missing or invalid.

- Steps: The system highlights the invalid fields and raise message M04

- Creating PO from Replenishment flow:

- Step 1: Go to Replenishment flow menu

- Step 2: Select variant through checking the checkbox on each row

- Step 3: Click on “Bulk action” > “Create new PO”

- Step 4: The order quantity of each variant will be recommended based on the sales forecast displayed on the replenishment flow. Users can change it if needed

- Step 5: Click on the “Confirm” button and then the user is redirected to creating a new PO page with pre-filled order items and ordered quantity.

- Step 6: Update some information on the PO and then create new PO - the flow & rules of creating a new PO follows the main flow

- Alternative flow: When clicking on the button “Cancel”, the creating process is cancelled and the user is redirected to Replenishment flow page.

- Step 7: After creating a new PO successfully, the message M10 is shown and the user is redirected to the PO list

#### 2.4. Business rule

Rule ID

Rule Title

Rule Description

BR01

Leaving page

Case 1: When the user has edited the PO and attempts to exit the page, the system will display the message log M07.

Case 2: When the user has not edited the PO, the system allows closing the PO without displaying a confirmation pop-up.

BR02

Generate PO ID

The system will automatically generate the PO ID after creating PO according to Conative’s rule (Cxxxxx).

BR03

Create PO

- Beside the required fields are mentioned above, the PO must include at least one item, depending on the status the user wants to change:

- If the user selects "Issue PO" or "Request Approval" and doesn’t add an item, a toast message will appear: “Please add at least one item to the purchase order before creating it.”

UI:

- If PO is status = Draft or Open, user tick all & select bulk action remove all items of PO, a toast message will appear: 
“This PO does not contain any items. Please add items before issuing”

### UC 3. View & Edit PO

User story

As a user,

I want to view, edit, and change the status of a purchase order (PO),

So that I can ensure POs are up-to-date, accurate, and properly tracked through their lifecycle.

Actor:

Active user account on Conative (suggested role: Procurement staff, inventory staff)

Trigger:

User click on Purchase order row on the PO list table

Pre-condition:

- User is in “Purchase Order List” Screen

- Allowed action - Refer to GR01

Post-condition:

- The PO's details are updated and saved in the system, with the most recent changes reflected immediately.

- The PO's status is changed as requested, and the new status is displayed throughout the system.

- The system logs any changes made to the PO (for auditing purposes).

- The user receives feedback confirming successful completion of the action (save or status change).

#### 3.1 UI & fields details

LINK:  / History tab - 

*Note: The default value of each field depends on the PO’s source + PO’s status

Tab

Element / ID

Type

Default value

Business rule

Basic information

PO ID

Label

Show

Display PO ID

Format: Conative’s rule (Cxxxxx)

PO number

Textbox

Enable

Display the PO number entered by the user.

Editable - based on the general rule GR01

Created date

Datepicker

Disable

Show created date (MMM DD, YYYY)

Expected arrival date

Datepicker

Enable

Show expected arrival date selected by user from the most recent update (MMM DD, YYYY)

Editable - based on the general rule GR01

When updating, Expected arrival date >= Created date

Vendor

Single selection

Enable

Show the vendor name selected by the user from the most recent update.

- Editable: when PO status = Draft

Warehouse

Single selection

Enable

- Show the warehouse name selected by the user from the most recent update.

- Can edit:

- If shipment is created before editing the warehouse: It is not affected.

- The shipment is created after updating the warehouse, taking the latest warehouse information

Status

Single selection

Enable

Enable in some status, the follow status can be changed is listed on the file -

Popup reason reject

Input

Disable

Display when user change status is Reject. 
Reason rejection is required.

Order item

Search

Input

-

Search by Title, SKU on the PO with criteria according to general rule GR02

Add item

Button

Disable

Enable - based on the general rule GR01

Same as field “Add item” on the UC2

Pagination

Text

Hidden

Show and enable when the number of item > 100

Format show:  Select all Y orders 
Showing X of Y results >

- X: The number of POs displayed on the current page. Normally, we fix 100 results per page.

- Y: The total number of orders that match the selected filters.

In the case where at least one row is selected in the table, the following will be displayed: X selected. Select all Y orders → Clicking this will select all POs and show “All Y results are selected. Clear selection”.

- X: The number of POs/rows selected.

- Y: The total number of orders that match the selected filters.

- If clicking on “Clear selection” → back to default state.

- If at least one row is not selected, the button will be shown again.

Title

Text

-

Display the item name and SKU of items selected by the user.

On Hand

Number

Show

Only show this column when the PO has status “Draft”/  “Pending approval”/”Rejected” / “Open”

Display the stock of the item in the warehouse.

MOQ

Number

Show

Only show this column when the PO has status “Draft” / “Pending approval”/”Rejected” / “Open”

Display the MOQ (if have)

Status

Label

-

Only show this column for the statuses 'Partially Fulfilled,' 'Fulfilled,' 'Closed,' or 'Canceled' (if the PO was in 1 of the 3 mentioned statuses before being canceled).

- Received: Received Qty = Order Qty

- Over received:  Received Qty > Order Qty

- Under received:  Received Qty < Order Qty

- Not received: Received Qty = 0

On order

Number

Show

Only show this column for the statuses 'Partially Fulfilled,' 'Fulfilled,' 'Closed,' or 'Canceled' (if the PO was in 1 of the 3 mentioned statuses before being canceled).

Only show the number

On order  = Order Qty - Received Qty

If Received qty > Order Qty → On order = 0

Order qty

Number

Enable

Editable - based on the general rule GR01

Override old data when save PO

Type - describe on the UC2

UOM

Text

-

The UOM is retrieved from the item details.

Received qty

Number

Disable

Showing when one of the order items is received.

Received qty = Total number of items received from the shipments linked to the PO.

Received history

Date

Disable

Showing when one of the order items is received.

- Received date is retrieved from field “actual received date” in each shipment linked to the PO.

- Format: MMM DD, YYYY

- Sorting: Display the most recent history at the top.

- If the number of received times = 1 → don’t show any icon

- If the number of received times > 1 → show a dropdown icon. Clicking the dropdown icon will display the full history

- The user can delete/update the “Actual received date” on the shipments to change the received history on the PO (click here to view how to delete shipment) → After deleting, the system update:

- Received Qty = Received Qty - Received History deleted

- On order = On order + Received History deleted

- Status

- Impact: When the user uploads shipments that link to the PO ID/PO number, the system will also add a received history entry for the corresponding PO line item (the date will be recorded as the import date).

- Hide this field if the PO is from other ERP

Production start date

Datepicker

Enable

- Editable - based on the general rule GR01

- Format: MMM DD, YYYY

Estimated completion

Datepicker

Enable

- Editable - based on the general rule GR01

- Format: MMM DD, YYYY

Completion date

Datepicker

Enable

- Editable - based on the general rule GR01

- Format: MMM DD, YYYY

Remove

Button

Hide

Enable when the user selects at least one row in the Items table.

Main flow: The system allows deleting the item if it meets the following conditions:

- The item hasn’t received yet

Exceptional cases: For other cases, display message M05.

Impact handling after deletion: The item will be removed from the PO.

Summary

Number

Disable

Update the total order quantity and received quantity and Total when the user modifies the Order or linked shipments.

Cost

Number

Enable

The cost depends on the settings, specifying the source from which the user wants to retrieve the cost per item.

Editable  - based on the general rule GR01

Type - describe on the UC2

Total cost

Number

Disable

Total cost = Cost x Order Qty

The system will automatically update the Total cost when the user updates the Order Quantity / Cost

Total line

Number

Disable

Total on order = The sum of the 'on order' quantities of all items.

Total received qty = SUM of all received qty

Total order qty = SUM of all items ordered qty

Total cost of all items on the PO

- Total = Total_cost_1 + Total_cost_2 + …. Total_cost_n

- The system will automatically update the Total when the user updates the Order Quantity / Cost.

Icon delete PO line item

Button

Disable

- Show and editable - based on the general rule GR01

- Show message M05 if any item has a Received Qty.

Note for PO

Text

Enable

Limit characters - GR03

Attachments

File

Enable

The user can upload a file with format: .xls, .xlsx, .pdf, .csv, .doc, .docx

Maximum - 5MB

- If the file > 5MB → raise error message in the toast “The attachment exceeds the size limit of 5MB. Please upload a smaller file."

- If the user selects invalid format file: display message error: Invalid file format.

- If File size exceeds the allowed limit: display message error: The files exceed the allowed size limit.

Shipment

Shipment

Button

Enable

Direct to Shipment tab

Shipment list

List all shipments of PO. 
By default: sort by “Created date” from newest to oldest

Add shipment

Button

Enable

Defined on Shipment feature - SRS

Shipping label

Text

Editable

Defined on Shipment feature - SRS

Tracking ID

Text

Disable

Defined on Shipment feature - SRS

Expected ship date

Datepicker

Disable

Defined on Shipment feature - SRS

Expected arrival date

Datepicker

Disable

Defined on Shipment feature - SRS

Created date

Date

Disable

Defined on Shipment feature - SRS

Status

Label

Disable

Defined on Shipment feature - SRS

History

History

Button

Enable

When the user clicks on “History” button → the user is redirected to the “History” tab

Record

Label

-

The user can view the record history, where each change is saved and then logged as a record. A record may have multiple rows, depending on the updated fields.

The list is sorted by the most recent update first.

The template of log is demonstrated as below in this UC (BR03)

Cancel

Button

Enable

Refer to BR01 - UC2

Save

Button

Disable

- Enable when the user performs the edit PO action.

- Save the changes → The system will retain the Edit UI and display Message M09 → After that, the button will return to its default (Disable) state.

#### Table rule of status field:

Status

Next Status

Trigger

Rule of status field on PO details

New PO

Draft

When user click [Save as draft]

- Just view

- Show status = Draft

Open

When user click [Issue PO]

- Just view

- Show status = Open

Pending Approval

When user click [Request Approval]

- Just view

- Show status = Pending Approval

Draft

Pending Approval

When user click [Request Approval]

- Just view

- Show status = Pending Approval

Open

When user click [Issue PO]

- Just view

- Show status = Open

Pending Approval

Rejected

When user click [Reject]

- Just view

- Show status = Reject

Open

When user click [Approve]

- Just view

- Show status = Open

Rejected

Pending Approval

Open

Partially Fulfilled

Based on received status of PO items: auto changes when received status = Received/Under received/ Over received

- Just view

- Show status = Partially Fulfilled

Fulfilled

Based on received status of PO items: auto changes when received status = Received/Over received

- Just view

- Show status = Fulfilled

Partially Fulfilled

Fulfilled

Based on received status of PO items: auto changes when received status = Received/Over received

- Just view

- Show status = Fulfilled

Closed

When user click [Close PO]

- Just view

- Show status = Closed

Fulfilled

Closed

When user click [Close PO]

- Just view

- Show status = Closed

Closed

Cancelled

#### 3.2 Main flow

- Step 1: The user navigates to the Inventory management > Purchase Orders section.

- Step 2: The user selects a specific PO from the list to view its details.

- Step 3: The system displays the detailed information for the selected PO, including those information mentioned above.

- Step 4: The system enables the input fields for editing, allowing the user to modify details such as:

- PO number

- Vendor

- Warehouse

- Expected arrival date

- Status

- Order item

- Order quantity

- Production start date

- Estimated completion

- Completion date

- Cost

- Note for PO

- Attachments

NOTE: The editable fields depends on the status - GR01

- Step 4: The user clicks the "Save" button to confirm the changes.

- Step 5: The system validates the updated information to ensure that all fields are correct and meet the required criteria (e.g., file type, missing required fields on each status).

- Step 6: If validation passes, the system saves the updated PO details and displays a confirmation message "Purchase order updated successfully"

- Step 7: Each time the PO is updated, it would be recorded as a log on history tab (follow rule BR03 below to view the log format)

- Step 8: The system disables the "Save" button to prevent further edits unless a new change is made.

#### 3.3 Alternative flow

- Update and missing required fields

- Step 4a: The user tries to save the PO, but if there is any invalid data (e.g., missing required fields like cost or order qty), the system prevents the save and highlights the required fields.

- Step 5: The user corrects the error and saves again, following the main flow.

- Add item to existing PO through Replenishment flow:

- Step 1: Go to Replenishment flow menu

- Step 2: Select variant through checking the checkbox on each row

- Step 3: Click on “Bulk action” > “Add to existing PO”

- Step 4: The system shows a list of PO with status “Draft” / “Pending approval” / “Open” only

- Step 5: The user selects 1 PO and then clicks “Next” button

- Step 6: The order quantity of each variant will be recommended based on the sales forecast displayed on the replenishment flow. Users can change it if needed

- Step 7: Click on the “Confirm” button and then the user is redirected to the PO detail page with pre-filled adding items and ordered quantity.

- If the item already exist on the PO → adding more order qty into this item

- Step 8: The user continues updating some information on the PO if needed and “Save” the PO - follows the business rules of updating PO on this UC.

- Alternative flow: When clicking on the button “Cancel”, the updating process is cancelled and the user is redirected to Replenishment flow page.

- Step 9: After updating PO successfully, the message M09 is shown and the user is redirected to the PO list

- Meet conditional to change status:

- Step 1: The user selects the new status from the field  “Status”

- Step 2: The user update other fields and clicking on the “Save” button

- Step 3: The system performs validation checks - depending on the BR02 (below)

- Step 4: The user adjusts the status and shows the message M09, following the main flow again.

- Download PO

- Step 1: On the PO detail page, The user clicks on the "Download CSV" / “Download PDF”  button on the PO details page.

- Step 2: The system generates the PO in a downloadable format once the PO has at least 1 item.

- If the user clicks on “Download CSV" button → a CSV file is downloaded

- If the user clicks on “Download PDF" button → a PDF file is downloaded

- The format of the file here

- View shipment detail

- Step 1: On the PO detail page, go to tab “Shipment”

- Step 2: Select a shipment to view the shipment detail

- View history

- Describe BR03 below.

- Add shipment (follow SRS-Shipment - UC 2 to add shipment) -

- Change Status:

- When PO status = Pending Approval, user click [Reject] to reject PO, system display popup request user provide reason for rejection.

- User input reason and click [Save], the system proceeds to:

- Save and log reason information

- Change the status to “Rejected”

- Display message: PO [PO Number] has been successfully rejected.

- When PO status = Pending Approval, user click [Approve] to approve PO, system display popup confirm.

- User click [Confirm], the system proceeds to:

- Save and log information

- Change the status to “Open”

- Display message: PO [PO number] has been successfully approved.

#### 3.4 Business rule

Rule ID

Rule Title

Rule Description

BR01

Allowed action

Refer to

BR02

Change status

Refer to

Special case 1: The PO status changes from 'Partially Fulfilled' to 'Closed' if there are items that have not been received in the full ordered quantity.

- Alternative Flow: The user tries to change the status to "Closed" if there are items that have not been received in the full ordered quantity,  the system displays a popup:

- Title “Change status”

- Content: Some items have not been fully received. Closing this purchase order may impact inventory and reporting. Are you sure you want to close it?

- Button “Close PO” : The system changes the status to “Closed” and the 'On order' quantity is excluded from the statistics report (On order = 0). The total cost is calculated based on received items.

- Button “Cancel”: The change status action would be canceled.

BR03

History log

MMM DD, YYYY HH:MM:SS

{User_name}

Note: Some actions that the system automatically updates (e.g., item status, PO status). The {user_name} is shown as 'Conative'.

1. Change basic information of PO:

Field

Log Format

PO Number

PO number changed from {old_value} to {new_value}”

Vendor

Vendor updated from {old_value} to {new_value}

Warehouse

Warehouse updated from {old_value} to {new_value}

Expected Arrival Date

Expected arrival date changed from {old_value} to {new_value}

2. Change information for each order item:

Field

Log Format

Order Quantity

Quantity of {item_name} changed from {old_quantity} to {new_quantity}

Received Quantity

Received quantity of {item_name} changed from {old_quantity} to {new_quantity}

Cost

Cost of {item_name} changed from {old_cost} to {new_cost}

Status

Status of {item_name} changed from {old_status} to {new_status}

Production Start Date

Production start date of {item_name} changed from {old_date} to {new_date}

Estimated Completion

Estimated Completion of {item_name} changed from {old_date} to {new_date}

Completion Date

Completion date of {item_name} changed from {old_date} to {new_date}

Delete Item

Item {item_name} is deleted

Remove item in bulk action

Item {item_name1}, {item_name2},..., {item_namen} are deleted

Add item

Added item {item_name} to PO:

- Order Qty: {order_qty}

- Production Start Date: {production_start_date}

- Estimated Completion: {estimated_completion}

- Completion Date: {completion_date}

- Cost: {cost}

If there is a blank field → don’t show this field on the log.

3. Change Attachments & note:

Action

Log Format

Add Attachment

Attachment {file_name} has been added

Remove Attachment

Attachment {file_name} has been removed

Update note

The note for PO has been updated from ‘{old_note_content}’ to ‘{new_note_content}’

4. Overall Status Changes:

Action

Log Format

Creating a new PO

Purchase order has been created with status {status}

Reject the PO

Purchase order has been rejected with the following reason: “{Reason_to_reject}”

Update Status

PO status updated from {old_status} to {new_status}

- If a log timestamp has several changes, we arrange them with order 1,2,3 as described above

- If this log has generated a PDF file, display the PDF file first.

- Each time the user changes the status (except when changing to 'Cancel' or 'Reject'), a PDF file is generated, with the version starting from 1 and incrementing sequentially.

- Format file name:  Purchase_Order_{PO_ID}_v{Version_number}

- The download template:

- UI:

- History log is being updated based on the further features.

### UC 4. Import purchase order

User story

As a procurement Staff

I want to import PO in bulk using a template file (csv).

So that I can save time and ensure accurate data entry for large orders.

Actor:

Active user account on Conative

Trigger:

User click on Import PO

Pre-condition:

- User is in “Purchase Order List” Screen

- The import template file is prepared and follows the required format - CSV.

- All mandatory fields in the template are correctly populated.

Post-condition:

- The PO is successfully imported, and the system validates and stores the data.

- If errors occur, the system provides feedback on invalid or missing fields.

#### 4.1 UI & fields details

LINK: https://www.figma.com/design/C3694nRiIEv1kXmfaG6zaQ/Conative_New?node-id=1-5042&p=f&t=cEtULfqAZr5nwwsR-0

- UI Upload file

- The required (mandatory) fields has a tag “Required” like this

- UI Mapping column

- UI import result

#### 4.2. Main flow

##### 4.2.1. Main flow

- Step 1: Go to PO list page

- Step 2: Click on “Create new” > “Import”

- Step 3: Select imported file

- Step 4: User clicks “Map column” button to be directed to step 2 - mapping column

- Step 5: The system loads the columns from the imported CSV file.

- Step 6: For each field, it needs to be mapped to PO data in Conative. The user selects a dropdown and then chooses the corresponding fields to map.

- Step 7: For "Mapping Warehouse" and "Mapping PO Status," the system displays warehouse names available in the database.

- Step 8: The user selects a dropdown and chooses the warehouse to map to the "Warehouse" in Conative, and the PO status to map to the corresponding PO status in Conative.

- Step 9: The user selects “Import.” and then the system automatically syncs data from the CSV file to Conative.

- Step 10: The user receives a confirmation message once the import is successfully completed.

- Step 11: The system displays a results page.

- Step 12: The user selects “View PO” to navigate to the PO listing page.

##### 4.2.1. Acceptance criteria

No.

Acceptance criteria

Note

Upload file

Given

- Select “ Import PO”

- Display popup process” Step by step”

- Default “Step 1- Upload file” with action

- Download PO template

- Select file to upload file (Required)

- Show uploaded file

- Click action “ icon Edit" to change file

- Cancel ~ Close popup

- Map Column ~ Move to next step

When

- User  selects  file and click “Map column” button

- User doesn’t upload  files

Then

- Result 1: System chuyển tiếp sang mapping data

- Result 2: Display message error if users don't select file import:

This field is required

- Result 3: Invalid file uploaded, display message error: Invalid file format.

And disable button" Mapping column"

Position error: inline message

Map Column

Given

- User upload  CSV file successfully

- The system displays the PO columns available in Conative.

- The system loads the column names from the uploaded file.

When

- The user maps the required columns correctly according to the format specified in the table above.

- The user then selects the “Map Column” button.

Then

- Result 1: The system navigates to the warehouse and status mapping page.

- Result 2: The system displays an error message if the user does not select enough columns to map.

This field is required

Position error: inline message

Given

- User upload  CSV file successfully

- The system displays the PO columns available in Conative.

- The system loads the column names from the uploaded file.

When

- The user maps 1 column in the file to 2 fields in the Conative column.

- The user then selects the “Map Column” button.

Then

- The system displays a red error message for the two conflicting mapped fields: “Unfortunately, the data mapping was incorrect. Please attempt it again.”

- The user must complete the mapping correctly before proceeding.

Position error: inline message

Map Warehouse

Given

- The system navigates to warehouse and status mapping.

- If the organization has warehouse data, the system loads a dropdown list of active warehouses from Conative.

- If there is no warehouse data, the dropdown is left blank.

When

- The user selects a warehouse from the Conative dropdown and chooses the corresponding warehouse value.

- The user selects “Add warehouse” if they want to map additional warehouse values.

- The user maps the PO status.

- The user clicks on “Import.”

Then

- The system displays the results screen.

Given

- The system navigates to the warehouse and status mapping.

- If the organization has warehouse data, the system loads a dropdown list of active warehouses from Conative.

- If there is no data, the dropdown is left blank.

- The user selects a warehouse from Conative and chooses the corresponding warehouse value.

When

- The user clicks the   icon to remove the mapped warehouse value.

Then

- The system removes the selected warehouse value from the warehouse field.

- The system displays the deleted value again in the warehouse dropdown list.


Given

- The system navigates to the warehouse and status mapping.

- If the organization has warehouse data, the system loads a dropdown list of active warehouses from Conative.

- If there is no data, the dropdown is left blank.

When

- The user selects a warehouse from Conative and chooses an incorrect warehouse value.

- The user maps the status.

Then

- System display error message  “The entered data is invalid. Please try again!”

Position error: inline message

##### 4.2.2. Mapping data

4.2.2.1 Map column, Select warehouse & PO status

- Ensure that the column headers in the uploaded file match the keys used for mapping (this should cover cases of uppercase, lowercase, and spaces to minimize human errors during the file upload).

- When no mapping is selected by default, the fields in the "Column in your file" section will display the hint text/placeholder  "Select column."

Field

Rule

Note

PO number

- For the "Column in your file" section:

- If the user uses the Conative template, the column is automatically mapped with a default value, such as “PO/Cut Ticket #.”

- If the user uses a different spreadsheet, no column mapping will be applied by default.

- The dropdown is enabled once the column has been mapped by default.

- The field is required.

PO status

- For the "Column in your file" section:

- If the user uses the Conative template, it is automatically mapped to the column "PO status."

- If the user uses a different spreadsheet, no mapping will be applied by default.

- The dropdown is enabled once the column is mapped by default.

- The field is required.

- Overwrite new data.

PO status includes 8 statues

Expected arrival date

- For the "Column in your file" section:

- If the user uses the Conative template, it is automatically mapped to the column "Expected arrival date."

- If the user uses a different spreadsheet, no mapping will be applied by default.

- The dropdown is enabled once the column is mapped by default.

- The field is required.

- Overwrite new data.

Created date =< Expected arrival date

Vendor name

- For the "Column in your file" section:

- If the user uses the Conative template, it is automatically mapped to the column “Vendor Name.”

- If the user uses a different spreadsheet, no mapping will be applied by default.

- The dropdown is enabled once the column is mapped by default.

- The field is required.

- Overwrite new data.

SKU

- For the "Column in your file" section:

- If the user uses the Conative template, it is automatically mapped to the column “SKU.”

- If the user uses a different spreadsheet, no mapping will be applied by default.

- The dropdown is enabled once the column is mapped by default.

- The field is required.

- Overwrite new data.

Ordered quantity

- For the "Column in your file" section:

- If the user uses the Conative template, it is automatically mapped to the column “Ordered quantity.”

- If the user uses a different spreadsheet, no mapping will be applied by default.

- The dropdown is enabled once the column is mapped by default.

- This field is required.

- Overwrite new data.

Warehouse name

- If the user uses the Conative template, it is automatically mapped to the column “Warehouse name.”

- If the user uses a different spreadsheet, no mapping will be applied by default.

- The dropdown is enabled once the column is mapped by default.

- This field is required.

- Mapping rule:

- Skip if Warehouse code = null

- Overwrite new data.

Warehouse id

- If the user uses the Conative template, it is automatically mapped to the column “Warehouse id.”

- If the user uses a different spreadsheet, no mapping will be applied by default.

- The dropdown is enabled once the column is mapped by default.

- This field is required.

- Mapping rule:

- Skip if Warehouse code is null.

- Overwrite new data.

4.2.2.2. Define case type mistake when import

No

Term

Action system

Note

1

Column name in uppercase/lowercase

Format: pOid

The system should ignore case sensitivity differences in the field name.

2

Column name with partial capitalization

The system should ignore differences in capitalization of characters within the column name.

3

Column name with one or more spaces at the beginning

Format: Dấu_cách_PO number

The system will remove spaces and map the two columns if only the column name in the upload file matches the column name in Conative.

4

Column name with one or more spaces between characters

Format: P dấu cách O_2_dấu_cách_ID

The system will remove spaces and map the two columns if only the column name in the upload file matches the column name in Conative.

5

Column name with one or more spaces at the end

Format: P dấu cách O_2_dấu_cách_ID_dấu_cách

The system will remove spaces and map the two columns if only the column name in the upload file matches the column name in Conative.

#### 4.3. Business rule

Rule ID

Rule Title

Rule Description

BR-001

Download PO template

- CSV

BR-002

Refresh data

Format:  Month DD, YYYY

BR-003

Mapping warehouse

Warehouse Conative = A

Warehouse file upload = X

Based on defined data type:

- Condition 1: A = X → Mapping: All values in A and X should be mapped correctly.

- Condition 2: A > X → Mapping: Map all available values in X (the warehouse data in the file).

- Condition 3: A < X → Mapping: Map all available values in A (Conative warehouse data).

BR-004

Mapping status

Status PO Conative = B

Status PO file upload = Y

Based on defined data type:

Các status PO (list as above)

- Condition 1: B = Y → Mapping: All values in B and Y should be mapped correctly.

- Condition 2: B > Y → Mapping: Map all available values in Y (the PO status in the file).

- Condition 3: B < Y → Mapping: Map all available values in B (Conative PO status).

BR-005

Overwrite data

- Same POID, different PO status >> Log error

- Same POID, different expected arrival date >> Log error

- Same POID, same SKU, different order quantity, different received quantity >> Log error

Note: Error log format

- Column name

- X - the position line (line number)  in the sheet

No.

Define error

Error log

Type

Empty

Missing values in some columns in line X in the upload file

Missing error

Wrong data

Invalid A in line X in the upload file

Format error

Wrong date format

Date format error on field A in line X in the upload file

Date format

Duplicate

Duplicate

BR-006

Mapping warehouse/ status

If the file upload contains empty fields for PO status, warehouse name, or warehouse id →  The corresponding dropdown option will not be displayed for mapping. An error message stating missing will be shown to the user.

Data validation between file and system:

Error Case

Action

Content

Invalid file uploaded

Error

Invalid file format. Please upload a file in .csv format.

PO number is empty

Error

Line <number> PO number is required.

Vendor name is empty

Error

Line <number> Vendor name is required

Vendor name is not found

Error

Line <number> Vendor name does not exist

Warehouse name is empty

Error

Line <number> Warehouse name is required

Item SKU is empty

Error

Line <number> Item SKU is required

PO number already exists, other information is different.

Update data:
- If PO number is duplicated and SKU is different: add new line on PO details

Same PO number, different expected arrival date

Overwrite: Update expected arrival date according to the latest line data.

PO number does not exists

Add new PO

Same PO number, same SKU, different order quantity

Overwrite: Update order quantity according to the latest line data.

Expected arrival date: Invalid Date Format

Error

Line <number> Invalid date format for expected arrival date. Expected format: MM-DD-YYYY

Invalid Item SKU

Error

Line <number> SKU does not exist.

Duplicate Line Items in a PO

Warning & Overwrite data

Line <number> & <number> duplicate item [Item SKU] found in PO.

Negative Order Quantity

Error

Line <number> Invalid quantity for item.



Import Results::

- If the system has multiple corresponding SKUs, map any 1 item with SKU

- If the PO number already exists, other information is different. Ignore Created Date info and update corresponding information.

- If the PO number does not exists, system add new record with Created Date as the date it was successfully imported, PO Status = Open

### UC 4. Import purchase order

User story

As a procurement Staff

I want to import PO in bulk using a template file (csv).

So that I can save time and ensure accurate data entry for large orders.

Actor:

Active user account on Conative

Trigger:

User click on Import PO

Pre-condition:

- User is in “Purchase Order List” Screen

- The import template file is prepared and follows the required format - CSV.

- All mandatory fields in the template are correctly populated.

Post-condition:

- The PO is successfully imported, and the system validates and stores the data.

- If errors occur, the system provides feedback on invalid or missing fields.

#### 4.1. Main flow

- User mở màn hình Purchase Order → nhấn nút Import → mở modal import wizard (Step 1: Upload file).

- User tải template (tùy chọn) và upload file CSV/XLSX.

- Hệ thống kiểm tra format file, số dòng, tổng dung lượng. Nếu hợp lệ, chuyển sang bước Mapping.

- Wizard Step 2 hiển thị danh sách field của Conative và dropdown list các header trong file của user. Các field bắt buộc hiển thị tag “Required”.

- User tiến hành chọn cột tương ứng (map column). Hệ thống kiểm tra xem các required fields đã map đầy đủ chưa.

- Nếu hợp lệ → User nhấn Continue → Step 3.

- Hệ thống xử lý file:

- Gom dòng theo PO number → tạo PO header & các line item tương ứng.

- Tạo mới hoặc cập nhật PO hiện có theo Business Rule.

- Hệ thống kiểm tra Received Qty của từng PO line:

- Nếu không có Received Qty hoặc Received Qty = 0: chỉ tạo PO và PO line items.

- Nếu Received Qty > 0: hệ thống tự động tạo shipment tương ứng cho PO line đó.

- Import hoàn tất → hiển thị:

- Bao nhiêu dòng import thành công

- Bao nhiêu dòng lỗi

- Bao nhiêu dòng warning

- Button: Download Error File, View Import Results

- User tải error file (nếu có), sửa file và import lại.

#### 
4.2. Alternative flow:

A1 - File format or extension invalid

- Condition: user uploads unsupported file extension or corrupted file.

- Behavior: show error: "Unsupported file type. Please upload CSV." Import aborted.

A2 - Missing header row / first row is not header

- Condition: no headers detected.

- Behavior: Disable Continue button

A3 - Required mappings not provided

- Condition: mapping step missing one or more required Conative fields.

- Behavior: Disable continue button; show tooltip listing missing required mappings.

A4 - Row count exceeds maximum (BR-F02)

- Condition: file contains > 10,000 rows.

- Behavior: reject upload on step 3 and show:
 BR-F02 Error — "Maximum rows per file: 10,000 rows. Your file contains X rows. Split your file into multiple files (≤10,000 rows each) and try again."

A5 - Validation rule failures per-row (non-critical)

- Examples: invalid date format, non-numeric Order Qty,..

- Behavior: import runs but rows with validation errors are failed and returned in the error file. Successful rows are created/updated.

A6 - Duplicate rows inside file (same SKU + same Warehouse on same PO)

- Rule: When duplicate line rows are present for the same PO that have same SKU & Warehouse, system will merge by using the last occurrence (bottom-most) in the file as authoritative for fields that are non-additive (e.g., expected arrival date), and will sum additive numeric fields (order qty)

- UI: show a warning

A7 - Duplicate SKU in database: same SKU but different Warehouses

- If row SKU exists in system but not for the specified Warehouse:

- Create a new inventory link (item-warehouse)

- If SKU exists in DB and same Warehouse:

- Merge line into existing PO if updating; treat as same item line per A6.

A8 - PO number already exists in system

- Update existing PO when PO number matches and PO status allows update (Draft, Pending Approved, Open, Partially Fulfilled). System merges/updates line items (see Business Rules).

- If the existing PO is Closed, Fulfilled, or Canceled → do not update: treat rows as errors

A9 - Supplier not found

- If Supplier column contains a name not found:  fail rows referencing that supplier -  include in error file with message "Supplier not found."

A10 - Warehouse not found

- If Warehouse does not exist: fail row with reason "Warehouse not found".

A11 - Partial success

- If some rows succeed and some fail, the import should be partially committed (successful rows persisted) and error file downloadable.

#### 4.3. UI & Fields Details:

Step 1 - Upload file:

- Elements:

- Title: Import Purchase Order

- Instruction text + Download template file link.

- Dropzone area: clickable + drag-and-drop.

- Supported formats note: csv

- After upload: show uploaded filename, success icon, delete (trash) icon to remove file.

- Buttons: Cancel, Map column (disabled until file uploaded).

Step 2 - Map Column:

- Layout: left column = Conative field, right column = Select column from your file (dropdown showing uploaded file columns).

- Required fields are marked with *

- Fields available (example list shown in UI):

- PO Number*

- Supplier*

- Warehouse*

- Warehouse ID

- Status

- Expected Arrival Date*

- Item SKU*

- Order Qty*

- Received Qty

- Received Date

- Cost

- Top status bar: shows mapping progress (e.g., 12 of 13 mapped — 1 missing) and tooltip listing missing required fields.

- Buttons: Back, Continue (disabled until required fields mapped).

Step 3 - Import & Results:

On completion:

- Import Successful (all rows) → show count and actions: Import Another File, View Imported Items.

- Import Partial (some errors/warnings) → show summary: Success: X rows, Errors: Y rows, Warnings: Z rows. 
Buttons: View Successful Items, Download Result File.

- Import Failed (critical) → show reason, link to template, Try Again button.

Error file: CSV containing only the failed rows with an additional error_reason column for each failed row.

#### 
4.4. Business Rule:

- File & Operational rules:

- BR-F02 (Max rows): Maximum rows per file = 10,000. If exceeded → upload rejected with message and suggestion to split file.

- Row commit mode: Per-row commit (valid rows imported; invalid rows rejected individually).

- Grouping & header rules:

- Group by PO Number. All rows with same PO Number are ONE PO.

- Header consistency: all rows in PO number must share same Supplier and Warehouse. If conflict → fail PO group.

- If some rows lack Expected Arrival Date but at least one row in group has it → use that date. If none provided → fail (Expected Arrival Date required), log error.

- Create/Update rules:

- Creating new PO: if PO Number not found → create new with header values from file. PO initial status = mapped status or default Open.

- Updating existing PO: allowed only if existing status ∈ {Draft, Pending Approved, Open, Partially Fulfilled}. For other statuses → reject update.

- Header updates: by default do NOT allow Supplier or Warehouse overwrite for existing PO → Log error. Allow Expected Arrival Date and Status update

- Line Item Rules:

- Duplicate SKU within same PO: Aggregate duplicate rows into single line: sum(Order Qty). For other columns (Cost) use last non-empty value

- SKU exists in DB but not linked to Warehouse: → create item-warehouse link automatically

- Status Rules:

- Default status mapping if blank → Open.

- PO Status dựa trên tình trạng nhận hàng (apply cho luồng import):

- Chưa có item nào được nhận: Open

- Đã nhận một phần: Partially Received

- Tất cả item đã được nhận đủ: Received

- Unknown status → log error

- Resolved status but precondition fails (Nghĩa là: status hợp lệ nhưng update level status thấp hơn level hiện tại): → downgrade and warning

- Inventory Impact:

- On Order impact: when PO status is Open (or when import creates PO with status Open), increase On Order at the PO's Warehouse by the sum Order Qty for each SKU. If PO is Draft → do not affect On Order.

- Validation specifics:

- Order Qty: integer >= 0 . Zero allowed: Accept but warn: Order Qty = 0

- Expected Arrival Date: required, parseable. Acceptable formats: YYYY-MM-DD, DD/MM/YYYY

- Supplier/Warehouse is not found: fail→ log error

- SKU resolution: exact match by SKU code (case-insensitive). If not found → fail row

- Error reporting & error file:

- Error CSV includes original row + Result row

- Provide Download Error File

### UC 5. Export purchase order

#### 5.1 Mục tiêu:

Cho phép user xuất toàn bộ thông tin của một Purchase Order ra file CSV hoặc PDF để:

- Chia sẻ với supplier / internal team

- Lưu trữ chứng từ

- Đối soát số lượng – chi phí – shipment

- Làm việc offline (Excel, Accounting, Audit)

#### 5.2. Phạm vi dữ liệu được export:

Export áp dụng cho 1 PO cụ thể (PO Detail page).

Bao gồm 3 nhóm dữ liệu chính:

- PO Header

- Order Items

- Shipments

#### 5.3 Pre-condition:

- PO đã tồn tại

- User có quyền View PO

- PO ở bất kỳ status nào (Draft → Closed)

#### 5.4 Trigger

User click:

- Download CSV

- Download PDF

#### 5.5 Main Flow

Step 1:

User mở PO Detail page

Step 2:

User chọn:

- Download CSV hoặc

- Download PDF

Step 3:

System thu thập dữ liệu:

- PO Header

- Order Items (bao gồm Summary + Line items)

- Shipments (nếu có)

Step 4:

System generate file theo format tương ứng:

- CSV → dữ liệu dạng bảng, machine-friendly

- PDF → layout đẹp, human-friendly

Step 5:

System download file về máy user

#### 5.6 Business Rules:

- Export snapshot tại thời điểm click

- Không phụ thuộc tab đang mở (Order Item / Shipment)

- PO bị Cancel vẫn export được (phục vụ audit)

- Dữ liệu hiển thị = dữ liệu export

### UC 6. Receive Items trong Purchase Order

#### 6.1 Main Flow:

##### Ghi nhận hàng đã nhận từ Purchase Order

Actor: User có quyền quản lý Purchase Order / Inventory Receiving
Trigger: User mở một PO và chọn Receive items.

Preconditions:

- PO đã tồn tại.

- PO chưa ở trạng thái Cancelled hoặc Fully Received.

- PO có ít nhất một order item còn số lượng chưa nhận.

- PO đã có Supplier và Warehouse nhận hàng.

##### Main flow

- User mở màn hình chi tiết PO.

- Hệ thống hiển thị danh sách order items và thông tin hiện tại của PO:

- PO Number

- Supplier

- Warehouse

- Expected arrival date

- Order Qty

- Received Qty

- User nhấn Receive items.

- Hệ thống mở modal Receive items.

- Hệ thống tự động hiển thị:

- Supplier của PO

- Warehouse của PO

- Received date mặc định là ngày hiện tại

- Danh sách các item thuộc PO

- MOQ

- Order Qty

- Received Qty input

- User điều chỉnh Received Qty thực tế cho từng item.

- User nhấn Approve.

- Hệ thống validate dữ liệu.

- Nếu dữ liệu hợp lệ, hệ thống:

- Tạo một Receive Record.

- Cộng Received Qty vào tổng số lượng đã nhận của từng PO line.

- Cập nhật inventory tại Warehouse nhận hàng.

- Tạo stock movement loại Shipment PO với status shipment = Delivered

- Tự động tạo Shipment tương ứng với lần nhận hàng.

- Ghi nhận transaction vào tab History.

- Hệ thống cập nhật trạng thái PO:

- Partially Received nếu vẫn còn item chưa nhận đủ.

- Received nếu tất cả item đã nhận đủ.

- Hệ thống đóng modal và hiển thị toast:

Receive recorded - Shipment #[Shipment ID] created.

- User có thể mở tab Shipment để xem shipment vừa được tạo.

#### 6.2. Alternative flow:

##### AF-01: Chỉ nhận một số item trong PO

- User nhập Received Qty cho các item đã nhận.

- Với item chưa nhận, user nhập 0.

- Hệ thống chỉ tạo inventory transaction cho các item có Received Qty lớn hơn 0.

#### 6.3 UI & Fields

6. 3.1 Receive Items modal

Nếu user chọn checkbox một số order items trước khi nhấn Receive items, hệ thống chỉ đưa các item đã chọn vào modal. Nếu không có item nào được chọn, hệ thống hiển thị toàn bộ item còn quantity cần nhận.

Receiving information

Field

Type

Required

Editable

Logic

Supplier

Text/Dropdown

Yes

No

Kế thừa từ PO

Warehouse

Text/Dropdown

Yes

Yes

Warehouse nhận inventory

Received Date

Date Picker

No

Yes

Mặc định ngày hiện tại

Supplier:

- Hiển thị supplier của PO.

- Không cho thay đổi trong receive modal.

Warehouse:

- Phải lưu warehouse ở level Receive Record hoặc Shipment.

- Inventory được cộng vào warehouse được chọn.

- PO có thể có nhiều receive records tại nhiều warehouse.

Received Date

- Mặc định: ngày hiện tại theo brand timezone.

- Có thể chọn ngày trong quá khứ.

6. 3.2 Item table

Column

Mô tả

Title

Product/variant title và SKU

MOQ

Minimum Order Quantity của item

Order Qty

Số lượng đặt trong PO line

Previously Received

Tổng quantity đã nhận trước lần hiện tại

Remaining Qty

Quantity còn cần nhận

Receive Now

Quantity được nhận trong transaction hiện tại

- Title:

- Hiển thị item title.

- Hiển thị SKU ở dòng phụ.

- Không editable.

- MOQ

- Hiển thị MOQ tại thời điểm PO được tạo hoặc MOQ hiện tại, tùy thiết kế dữ liệu.

- Không sử dụng MOQ để chặn receiving vì hàng thực nhận có thể thấp hơn MOQ.

- Order Qty

- Không editable trong Receive Items.

- Là ordered quantity của PO line.

- Previously Received

- Công thức: Previously Received = Tổng quantity của tất cả receive records đã hoàn thành cho PO line

- Receive Now

- Input dạng number.

- Giá trị mặc định: 0

- Cho phép user nhập 0.

- Không cho số âm.

#### 6.4 Business Rules:

BR-01: Shipment creation

Khi receive thành công, hệ thống tự động tạo một Shipment liên kết với:

- PO

- Supplier

- Warehouse

- Item quantities của lần nhận này

Một PO có thể có nhiều shipments tương ứng với nhiều lần nhận hàng.

- 1 PO → N Receive Records

- 1 Receive Record → 1 auto-generated Shipment

### UC 7. View & Update Reference trong PO Detail

#### 7.1 Main Flow:

Actor: User có quyền xem hoặc chỉnh sửa Purchase Order
Trigger: User mở PO Detail và nhấn Reference.

##### Preconditions

- Purchase Order đã tồn tại.

- User có quyền truy cập PO Detail.

- Các dữ liệu liên quan như Supplier, Warehouse và Currency đã được cấu hình trong hệ thống.

##### Main flow

- User mở màn hình PO Detail.

- User nhấn Reference.Hệ thống hiển thị action Reference ở góc phải màn hình.

- Hệ thống mở side panel Reference từ bên phải.

- Hệ thống tải và hiển thị thông tin hiện tại của PO theo các nhóm:

- General

- Supplier

- Reference

- User xem hoặc chỉnh sửa các field được phép.

- User nhấn Save changes.

- Hệ thống validate dữ liệu.

- Nếu dữ liệu hợp lệ, hệ thống:

- Lưu thông tin mới vào PO.

- Cập nhật các field tương ứng trên màn hình PO Detail nếu có.

- Hệ thống đóng panel và hiển thị toast: Purchase order reference updated.

#### 7.2. Alternative flow:

#### 7.3 UI & Fields

##### 1. Reference side panel

Item

Description

Panel title

Reference

Open behavior

Slide in from the right side

Close action

X icon or Cancel button

Primary action

Save changes

Save button state

Enabled only when at least one editable field has changed

Unsaved changes

Show a discard confirmation when the user closes the panel after making changes

##### 2. General section

- Type: Purchase Order

- Status = {current_status}

- Payment Term:

- Hiển thị thông tin hiện tại

- Trường hợp chưa có thông tin: hiển thị placeholder: eg. Credit Card, Cash

- Cho phép user edit

##### 3. Supplier section

- Email:

- Hiển thị email hiện tại

- Trường hợp chưa có thông tin: hiển thị placeholder: Supplier email

- Currency:

- Hiển thị mặc định theo currency đã config cho brand

- Address:

- Hiển thị thông tin hiện tại

- Trường hợp chưa có thông tin: hiển thị placeholder: Supplier address

#### 7.4 Business Rules:


## Tab t.1fxbgmxaooml

##### 1. General Procurement Process

- What are the primary challenges you face when creating or managing purchase orders on Conative?

- Are there specific manual tasks you’d like to automate?

##### 2. Purchase Order Creation & Management

- What kind of approvals are required before issuing a purchase order?

- Are there any challenges with purchase order revisions or cancellations?

- Do you use the reorder qty from Replenishment flow or or you need to create PO manually from the PO list?

- How do you determine the expected arrival date from the beginning?

- Are there any challenges with automating or tracking the approval workflow?

##### 3. Supplier Collaboration

- How do you currently communicate with suppliers about purchase orders and updates?

- What are the common issues you encounter with supplier responses or confirmations?

- Do you need to track supplier lead times & cost? How do you do this right now?

- Are there any challenges in maintaining supplier performance records?

##### 4. Purchase Order Status & Workflow Automation

- How do you monitor the status of open purchase orders?

- Do you receive real-time updates on order confirmations, production, or shipping from suppliers?

- How do you handle delays or discrepancies in orders?

- Would automated notifications or escalations help improve your workflows?

##### 5. Shipment Management & Tracking

- Are there challenges in receiving order quantities?

- How do you currently track shipments from suppliers?

- What information do you need to capture for each shipment? (e.g., tracking number, carrier details, ETA)

- Do you have visibility into shipment delays, damages, or discrepancies?

- How do you manage partial shipments or split deliveries?

- Are there challenges in reconciling shipment details with purchase orders?

##### 6. Receiving and Updating Quantities

- How do you verify the received quantity against the purchase order?

- What are your pain points in managing discrepancies between ordered and received quantities?

- Is there a process to handle damaged goods, returns, or shortages?

- How do you ensure received goods are recorded promptly and accurately in inventory?

##### 7. Inventory Transfers

- How do you manage inventory transfers between warehouses or distribution centers?

- Do you track transfers manually, or is there a system in place?

- What are the challenges in maintaining visibility of inventory in transit?

- How do you handle errors or delays in stock transfers?

##### 8. Reporting & Analytics

- What key metrics do you track for purchase orders, shipments, and inventory transfers?

- How do you identify inefficiencies or bottlenecks in your procurement and shipment processes?

- Would dashboards or analytics features help you track performance and make decisions?

- What types of reports or insights would be most valuable to your team?

##### 9. Integration Needs

- What systems do you currently use for procurement, inventory management, and logistics?

- Are there challenges in integrating your purchase order and shipment processes with other systems (e.g., ERP, WMS, TMS)?

- Would integration with supplier systems or carriers improve your operations?

##### 10. Pain Points and Improvement Areas

- What are the biggest frustrations your team faces in managing purchase orders and shipments?

- Are there specific manual tasks you’d like to automate?

- How do these issues impact your overall supply chain efficiency and costs?


