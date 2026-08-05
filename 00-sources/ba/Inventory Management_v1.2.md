# Inventory Management_v1.2

> Nguồn: [Google Doc – Inventory Management_v1.2](https://docs.google.com/document/d/1vG0nmJnevWUEr_Fa_nCm2bZjzzoSJAibf_GWzwEUVJI/edit)
>
> Nội dung được chuyển sang Markdown theo thứ tự các đoạn trong tài liệu nguồn.


## Tab t.0

### Document Version Control

Version

Date

Author

Changes/Description

1.1

06/01/2026

Linh Tô

- Bổ sung UC13 Integration Hub: View details của Shopify source

- Bổ sung UC14 Logic Logic sync available qty Shopify ⇄ Conative

- Bổ sung tính năng link location với WH, manage inventory cho từng location ở UC2 &3

- Bổ sung stock type = available, reserved, total inventory value ở Inventory Items

- Bổ sung tính năng sales channel mapping ở details item và inventory item list: combine các variants bị trùng SKU ở SC và cho phép user bật/tắt managed inventory cho từng item ở UC4

1.2

14/01/2026

Linh Tô

- Bổ sung UC Settings: Inventory Tab cho các configuration: Low Stock, OOS, Overstock

- Bổ sung Forecast by Sales Channel section cho view inventory item details ở UC4

- Bổ sung Adjust inventory Flow ở UC4.4: Edit inventory item

1.3

07/04/2026

Linh Tô

- Bổ sung Warehouse - Location mapping section ở tính năng Manage my Shopify inventory ở UC13


### Document Reference

Document Type

Link

Author

Design

Figma

Huy Huynh

### UC-INV-001. MANAGE & VIEW WAREHOUSE LIST

User Story

As an Inventory Manager,
I want to browse & search the list of warehouses that belong to my brand,
So that I can quickly locate, audit or update any location.

Actor

Primary: Inventory Manager

Trigger

User selects menu item Inventory Management > Warehouse Management

Pre-conditions

- User is authenticated.

- Warehouse.count ≥ 0.

Post-conditions

• The latest aggregated warehouse data are displayed on screen.

Main Flow

1. View Warehouse List

Step #

Actor Action

System Response

1.

Navigates to “Warehouse list” in side-nav.

1.1 Displays the following default elements:

- Default Sort: warehouse name (alphabet A > Z)

- A Search bar to filter warehouses by name or ID.

- A Source Filter Dropdown set to "All Sources" by default.

- A Refresh data button.

- Default soft by Warehouse Name (alphabet A > Z)

- An Add New Warehouse button.

- The Last Update timestamp

- A table showing the warehouse list with columns for:

- Warehouse ID

- Warehouse Name

- Address

- Status (include: Active/Inactive)

- Total SKUs

- Source (The origin of the warehouse data, indicating whether it was created directly within the system (Conative) or imported from an external platform (e.g. NetSuite, SAP)

- Actions

2.

Clicks the Source Filter Dropdown

Shows the following options:

- All Sources (default): Displays warehouses across all connected sources.

- Show the individual source names where the user obtained warehouse data

2.1

Selects a specific source

- Filters the warehouse list, showing only warehouses associated with the selected source.

- The Source Filter Dropdown updates to reflect the selected source.

3.

Types a keyword into the Search bar to find a warehouse by name or ID

Dynamically filters the warehouse list based on the entered keywords.

4.

Clicks the Refresh icon

- Fetches the latest warehouse list data.

- Displays the updated Warehouse List table with the latest information.

2. View Warehouse Details

Step #

Actor Action

System Response

1.

Clicks View Details from the Actions menu of a warehouse or clicks on the data line

Displays the warehouse details in a read-only mode with the following fields:

- Warehouse Name: Name of the warehouse (e.g. "HCMC Distribution Center").

- Type: Type of the warehouse (e.g. "Distribution Center").

- Warehouse ID: Unique identifier for the warehouse (e.g. "WH-SIN-02").

- Status: Current status of the warehouse ("Active" or "Inactive").

- Address: Street, city, and state of the warehouse.

- Phone Number: Contact number for the warehouse.

- Linked Channel: The e-commerce or marketplace associated with the warehouse.

- Default Fulfillment Status: Indicates if the warehouse is the default fulfillment center for its linked channel.

- Variants in Warehouse: Show the user's configuration. If the toggle is enabled, all variants will be added; otherwise, it will follow the setting for the number of variants the user has added.

- Description: Additional notes or information about the warehouse.

2.1

Clicks the Cancel button

Closes the modal and returns the user to the Warehouse List page.

2.2

Clicks the Edit button

Switches into edit mode, allowing the user to modify warehouse details (See details in UC-INV-003)

2.3

Click the Sort each column

- Warehouse Name

- Total SKU

Alternative Flows

ID/ Title

Description

A1. No data Found/Empty state

• No search/filters result found:

•  Empty State: show empty-state illustration + “Create first warehouse” CTA.

A2. Service timeout / API error

• System shows toast “Unable to load data. Please try again or contact admin.”

• Retry button reloads data (returns to step 1).

A3. Add New Warehouse

• Clicking on the “Add New Warehouse” button opens a modal for adding new warehouse details.

#### 1.1 Business Rules

ID

Rule

1

For warehouse data retrieved from external sources into Conative, display the corresponding source for each warehouse. These warehouses cannot be edited or deleted

2

#### 1.2 UI & Fields Details

Element / ID

Type

Default value

Rules

Search

Search Bar

empty

Search matches contains-case-insensitive on Warehouse name & Warehouse ID

Add New Warehouse

Button

Add New

Launches UC-WH-002 in create mode.

Refresh Data

Hyperlink

N/A

- Data must be refreshed when clicked.

- The Last Update timestamp in the header is updated to reflect the most recent refresh time.

Warehouse ID

Column Header

N/A

Displays the ID of the Warehouse

Warehouse name

Column Header

N/A

Displays the name of the Warehouse

Address

Column Header

N/A

Displays the Address (City, State) of the Warehouse

Total SKU

Column Header

N/A

Displays the total SKU(s) of the Warehouse

Source

Column Header

N/A

Displays the source of the Warehouse (e.g. ShipHero)

Actions

Kebab Menu

N/A

- Opens as a dropdown when the user clicks the Actions button for a specific warehouse, showing 3 options:

- View Details: Navigates the user to the detailed view of the selected warehouse. No modifications are allowed in this mode (read-only).

- Edit: Opens a modal or form to edit the warehouse's details (See details in UC-INV-003).

- Delete: Deletes the selected warehouse after user confirmation (See details in UC-INV-003).

- Rules for Displaying Actions:

- Internal Warehouses (Created in Conative): Display all actions (View Details, Edit, Delete)

- Linked Warehouses (From External Sources - ERP or Sales Channels): Display only the View Details action. Edit and Delete are hidden. These warehouses are managed through their respective external sources and cannot be edited or deleted in the system.

### UC-INV-002. VIEW DETAILS WAREHOUSE

#### 1.1. Main flow

- Step 1: The user navigates to the Inventory management > Warehouse list section.

- Step 2: The user selects a specific warehouse from the list to view its details.

- Step 3: The system displays the detailed information for the selected warehouse, including those information mentioned above.

For warehouse created in Conative:

- Warehouse ID

- Warehouse Name

- Type

- Status

- Address 1

- Address 2

- City

- State

- Phone

- Description

- Source

For warehouses synced from other sources:

- Warehouse ID

- Warehouse Name

- Type

- Status

- Address 1

- Address 2

- City

- State

- Phone

- Linked Channel

- Channel Location/Fulfillment Center ID

- Checkbox: default fulfillment wh for channel

- Toggle add variants

#### 1.2. Alternative flow

#### 1.3 UI & fields details

Element / ID

Type

Default value

Business rule

Warehouse ID

Label

Show

Display Warehouse ID

Warehouse name

Textbox

Show

Display the Warehouse Name

Type

Textbox

Show

Display the type of warehouse

Status

dropdown

Show

Display the status of warehouse

Address 1

Textbox

Show

Display the address 1 of warehouse

Address 2

Textbox

Show

Display the address 2 of warehouse

If there is no value, show “-”

City

Textbox

Show

Display the city of warehouse

State

Textbox

Show

Display the state of warehouse

Phone

Numberic

Show

Display the phone of warehouse

If there is no value, show “-”

Linked Sales Channel Location

Dropdown

Show

Only show when the warehouse is retrieved in another source

Display linked channel of warehouse


Only show this when the warehouse is created in Conative.

Display all sales channels supported by Conative.

Current scope: one warehouse mapping with one Shopify location.

Channel location

Dropdown

Show

Display channel location/Fulfillment center ID of warehouse

Only show when the warehouse is retrieved in another source

After the user selects a sales channel, the location list will be loaded based on the selected sales channel.

Current Scope: one warehouse mapping with one shopify location

Toggle “Push Inventory to this location”

Allow users to enable or disable the toggle.

When the user turns on the toggle, the system will map the location to the warehouse and track the available quantity from Purchase Orders or manual adjustments in order to push quantity data to the corresponding Shopify location.

Checkbox Default fulfillment warehouse for channel

Display the value selected by the user.
Only show when the warehouse is retrieved in another source

Toggle: Variants in Warehouse

Display the value selected by the user.

Description

Display the description of warehouse (if available)

Edit

Only show when the warehouse is created in Conative

Cancel

Always show

#### 1.4. Business Rule

- For warehouse data retrieved from external sources into Conative, display the corresponding source for each warehouse. These warehouses cannot be edited or deleted

- For warehouse data created in Conative, user can edit or delete

### UC-INV-003. CREATE / EDIT WAREHOUSE

User Story

As an Inventory Manager,
I want to add or edit warehouse details,
so that I can keep the warehouse data up-to-date and ensure accurate inventory management.

Actor

Primary: Inventory Manager

Trigger

a. “Add New Warehouse” button in UC-WH-001
b. Kebab menu (Warehouse List View) → Edit.

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:

- The new/updated warehouse is successfully added/saved to the database.

- The warehouse list is updated to display the newly added/updated warehouse.

Failure:
- If validation fails, the form remains open, and error messages are displayed for the problematic fields.
- The warehouse is not added/saved until the errors are resolved.

Main Flow

- Add New Warehouse

Step #

Actor Action

System Response

1.

Clicks the "Add New Warehouse" button on the "Warehouse List" page.

Opens the "Add New Warehouse" modal with empty input fields.

2.

Fills out empty input fields

•  Validates all mandatory fields to ensure they are filled and adhere to input rules.

•  If any validation fails, the system displays inline error messages.

3.

Links Warehouse to Channel as Data Source

• Save the warehouse details to the database.

• Displays a success message: "Warehouse  was created successfully."

• Updates the warehouse list with the new entry.

3.1

Selects a Channel Name from the drop-down list.

3.2

Enters the Channel Location/Fulfillment Center ID.

3.3

Optionally toggles the checkbox to set this warehouse as the Default Fulfillment Warehouse for the Channel.

3.4

Clicks Save to confirm or Cancel to discard changes.

4.

Clicks the "Save" button.

- Edit Warehouse

Step #

Actor Action

System Response

1.

Click the "Edit" icon next to a specific warehouse in the warehouse list.

Open the "Edit Warehouse" modal, pre-filled with the selected warehouse's details.

2.

Update the fields

Validate the updated fields based on the same rules as the Step 2. in "Add New Warehouse" flow.

3.

Click the "Save" button

• Update the warehouse details in the database.

• Display a success message: "Warehouse details were updated successfully."

• Close the drawer of item details

• Update the warehouse list with the edited entry.

Alternative Flows

ID/ Title

Description

A1. Validation Errors (Add/Edit)

• Condition: A mandatory field is left blank or contains invalid data.

• System Response: Inline error messages are displayed for the problematic fields.

A2. Duplicate Warehouse ID (Add/Edit)

• Condition: The entered warehouse code already exists in the system.

• System Response: Displays an error message: "Warehouse code must be unique."

A3. Cancel Action (Add/Edit)

• Condition: The user clicks the "Cancel" button while there are unsaved changes.

•  System Response: Prompts a confirmation dialog:
- Message: "You have unsaved changes. Are you sure you want to cancel?"
- Options: "Yes" (closes the modal) or "No" (returns to the form).

A4. Delete Warehouse

• Condition: The user clicks the "Delete" button for a specific warehouse.

• System Response: Prompts a confirmation dialog:
- Message:
- Options: "Delete warehouse" (deletes the warehouse) or "Cancel" (cancels the action).

#### 1.1 Business Rules

ID

Rule

#### 1.2 UI & Fields Details

1.2.1 Add New Warehouse

Field Name

Type

Default value

Required?

Rules

Warehouse Name

Text Input

empty

Y

- Max 255 characters.

- Cannot contain special characters.

Warehouse ID

Button

empty

Y

- Max 255 characters.
- Must be unique.

Type

Dropdown

empty

Y

- Value: 
+ Internal
+ Fulfillment Center
+ Distribution Center
+ Factory/Supplier
+ Other: allow users to add a new warehouse name

For warehouses synced from another source, display “Synced Warehouse”.

Status

Dropdown

Active

Y

- Options: Predefined list (Active, Inactive).

Address 1

Text Input

empty

Y

- Max 255 characters.

Address 2

Text Input

empty

N

- Max 255 characters.

City

Text Input

empty

Y

- Max 255 characters.

State

Text Input

empty

Y

- Max 255 characters.

Phone

Text Input

empty

N

- Must be a valid phone number.

Linked Sales Channel Location

Dropdown

Show

N

Only show when the warehouse is retrieved in another source

Display linked channel of warehouse


Only show this when the warehouse is created in Conative.

Display all sales channels supported by Conative.

Current scope: one warehouse mapping with one Shopify location.

Channel location

Dropdown

Show

N

Display channel location/Fulfillment center ID of warehouse

Only show when the warehouse is retrieved in another source

After the user selects a sales channel, the location list will be loaded based on the selected sales channel.

Current Scope: one warehouse mapping with one shopify location

Toggle “Push Inventory to this location”

Allow users to enable or disable the toggle.

When the user turns on the toggle, the system will map the location to the warehouse and track the available quantity from Purchase Orders or manual adjustments in order to push quantity data to the corresponding Shopify location.

Default Fulfillment Warehouse for Channel

Checkbox

Unchecked

N

- Marks the created warehouse as the default fulfillment warehouse for the selected Linked Channel.
- Only one warehouse can be set as default for each channel.
- If checked, the system prompts the user if another warehouse is already set as default for the same channel.

Add All Variants in Warehouse

Toggle Switch

OFF

N

- When enabled, all variant items will be pulled back and made available in the created warehouse.
- Displays tooltips: “Enable to add all variants from the inventory list to this warehouse.”

Description

Text Area

empty

N

- Max 255 characters.


### UC-INV-004. MANAGE & VIEW INVENTORY ITEMS

User Story

As an Inventory Manager,
I want to add or edit inventory items,
so that I can keep the inventory items data up-to-date and ensure accurate inventory management.

Actor

Primary: Inventory Manager

Trigger

User selects menu item Inventory Management > Inventory Items

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:

- The user can view, search, filter, and take actions across all tabs.

- Updates or changes are saved and reflected in real-time.

Main Flows

1. View Inventory Items

Step #

Actor Action

System Response

1.

Navigates to “Inventory Items” page

Displays the Inventory Items screen, showing:

- Warehouse Filters:

- Default:

- Always show “All Warehouses” tab (fixed and cannot be removed).

- Group view by Item (default: sort A > Z by item name)

- Show up to 5 individual warehouse tabs as selected.

-  Tabs for filtering inventory by warehouse. (Dependent on Warehouse Visibility configuration)

- User clicks [Add Warehouse] button in the top bar.

- System opens dropdown/modal showing only the warehouses currently enabled (visible) in the  Warehouse Visibility settings.

- User searches and selects up to 5 warehouses (max limit).

- User clicks Apply. The selected warehouses are added as tabs.

- If the user later disables a warehouse in Visibility settings: That warehouse immediately disappears from “Add Warehouse” dropdown and from active filter tabs (if currently selected).

- Summary Metrics:

- Total Inventory Value:

- Chỉ tính On Hand

- Không bao gồm: On Order, In Transit

- On Hand:

- Tồn kho vật lý

- Read-only

- Tăng/giảm qua receive, ship, adjustment

- Available:

- Conative sẽ pull data near real time từ Sales channel

- Thay đổi nếu on hand thay đổi (qty tương ứng): thay đổi do PO được nhập hàng, adjust => push new available qty lại lên SC

- Reserved:

- Sales Order: lấy từ sales channel về. Trường hợp chưa hoặc ko có: show -

- Transfer Order: lấy từ transfer_qty TO có stt = Scheduled cho WH_from

- On Hold

- On Order

- In Transit.

- Incoming

- Outgoing

- Three tabs:

- Item List: Displays detailed inventory items based on warehouse value filter.

- Stock Movements: Tracks order stock transfers between warehouses, including Purchase Orders (Supplier/Vendor to Warehouse) and Transfer Orders (Internal Warehouse Transfer).

- History Logs: Logs historical changes and imports for audit purposes

- Actions: Options to filter, refresh data, and import items.

- Latest Update: Record the timestamp of the latest data retrieval.

2.

Selects a specific warehouse (e.g. "Melinda Retail") or All Warehouses in the Warehouse Filter Tabs

Updates the Item List/ Stock Movements/ History tab to display inventory data for the selected warehouse.

3.

Views Summary Metrics section and

Clicks on tooltips, which includes: Quantity on Hand, In Transit, On Order, On Hold

Displays Tooltips:

- Total Inventory Value: “Total monetary value of inventory currently on hand, calculated based on item cost.”

- On Hand: Physical quantity currently available in the warehouse.

- Available: Quantity available for sale.

- Reserved (SO): Quantity reserved for confirmed sales orders.

- Reserved (TO): Quantity reserved for internal warehouse transfer orders.

- On Order: Quantity ordered from suppliers but not yet received into inventory.

- In Transit:

- Incoming: Quantity currently being shipped to the warehouse.

- Outgoing: Quantity currently being shipped out from the warehouse

- On Hold: "The quantity of items that are on hold and not available for sale or fulfillment."

4.

User click on icon

The system displays a 'Warehouse Visibility' popup showing all warehouses in the system. It allows users to configure which warehouses are visible in each tab

- User clicks [Show All] in the Warehouse Visibility popup, the system will enable all warehouse toggles.

- User clicks [Save Changes], the system will close the popup and display all warehouses under the Inventory Item section, each warehouse will appear as a separate tab.

- User click [Hide All] in the Warehouse Visibility popup, the system will disable all warehouse toggles.

- User clicks [Save Changes], the system will close the popup and hide all warehouse tabs in Inventory Items. (No data screen)

4.1 Manage Warehouse Visibility:

System opens the modal Warehouse Visibility.

User can:

- Search for warehouses by name or ID.

- Toggle each warehouse (ON/OFF) to control visibility.

- Use quick actions: Show All / Hide All.

User clicks [Save Changes].

The system saves visibility preferences to the per organization.

Inventory Items (top cards + tabs) and “Add Warehouse” filter dropdown automatically refresh to include only visible warehouses.

#### 1.1 Alternative Flows:

#### 1.2 Business Rules

ID

Rule

#### 1.2 UI & Fields Details

1.2.1 View Inventory Items

Field Name

Type

Default value

Rules

Latest Update Timestamp

Text with Icon (Inline)

N/A

- Indicates the most recent action, update, or synchronization within the system.

- The text must always display the label "Latest Update:" followed by the date and time in the format MMM D, YYYY, hh:mm AM/PM.

- Content of Tooltip:

"This timestamp shows the most recent system update or synchronization. It reflects changes made to the data or settings."

- Ensure the date/time updates dynamically based on the latest system update.

Warehouse Filters

Tab

All Warehouses

- Tabs Displayed:

- All Warehouses: Always displayed (fixed). Aggregates data across all visible warehouses.

- Individual warehouse tabs (1–5):

Shown according to Add Warehouse selection.

- Behavior:

- Clicking a tab filters the Item List/ Stock Movements/ History Logs for inventory data specific to the selected warehouse.

- The All Warehouses tab shows a consolidated view of inventory across all warehouses.

- Add Warehouse Dropdown:

- Displays only warehouses that have is visible = true from warehouse visibility

- Search field: Filters visible warehouses only.

- Checkbox list: User can check up to 5 warehouses. After 5 are checked, remaining become disabled (greyed out).

Warehouse Visibility Modal

- Search Bar: Search warehouses by name or ID.

- Warehouse list: List all warehouses includes source = Conative and external source. Toggle switch (ON/OFF).

- Show All/Hide All: Bulk toggle actions.

- No limit: Users can enable any number of warehouses here (visibility only).

Summary Metrics

Numeric

Show

- Metrics Displayed:

- Total Items: Number of distinct SKUs in the inventory.

- Total Inventory Value: Total monetary value of inventory currently on hand, calculated based on item cost.

- Chỉ tính On Hand x Cost

- On Hand: Physical quantity currently available in the warehouse.

- Tồn kho vật lý

- Read-only

- Tăng/giảm qua receive, ship, adjustment

- Available:

- Conative sẽ pull data near real time từ Sales channel

- Thay đổi nếu on hand thay đổi (qty tương ứng): thay đổi do PO được nhập hàng, adjust => push new available qty lại lên SC

- Reserved:

- Sales Order: lấy từ sales channel về. Trường hợp chưa hoặc ko có: show -

- Transfer Order: lấy từ TO có stt = Scheduled cho WH_from

- In Transit: Items currently being transferred to the warehouse(s).

- Incoming: Total Items on the way TO this warehouse.

- Outgoing: Total items being sent FROM this warehouse.

- On Order: Items ordered but not yet received.

- On Hold: Items reserved or blocked from use.

Icon

- Enable

- Popup Warehouse Visibility:

Display all warehouses (warehouse name & warehouse ID) of system

Allow user enable/disable warehouse appear in inventory items report

### UC-INV-004.1. MANAGE & VIEW ITEM LIST ON INVENTORY ITEMS PAGE

User Story

As an Inventory Manager, 
I want to view, search, filter, and manage inventory items across warehouses,
So that I can maintain accurate stock levels, monitor item statuses, and ensure availability for sales and operations.

Actor

Primary: Inventory Manager

Trigger

User selects menu item Inventory Management > Inventory Items > Item List tab

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:

- The user can view an updated inventory list reflecting any applied filters, searches, or actions.

- Any changes (e.g. item updates, imports) are saved and reflected in real-time.

Main Flows

1. View Item List

Step #

Actor Action

System Response

1.

Navigates to the Inventory Items and selects the Item List tab (default).

Displays:

- Header section (Warehouse filters & Summary metrics - See UC-INV-004 for details).

- A table listing inventory items with columns for:

- Item Name

- SKU

- Warehouse

- On Hand

- Available

- Reserved

- Sales Order

- Transfer Order

- On Order

- In Transit

- Incoming

- Outgoing

- On Hold

- Linked Sales Channel:

- Count số lượng variant trùng SKU được link ở cùng sales channel (view Business Rules)

- Alert

- Status

- Action:

- If items is created in Conative: 3 actions: View details, edit, delete

- If the user clicks [Delete], the system will check whether any Transfer Orders (TO) or Purchase Orders (PO) have been created for this item.

=> If yes, the system will display a notification message: Cannot delete item: open {Transfer Orders/or Purchase Orders} (ID: ...)

- If warehouses synced from another source: View details

- Refresh Data and Import Items buttons.

2. View Item Details

Step #

Actor Action

System Response

1.

Clicks on an item in the Item List table or selects View Details from Actions menu

Opens the View Details modal, displaying the following sections:

- Name of items

- Item Information: General details about the item, including:

- SKU: Unique identifier for the item.

- UOM: Unit of Measure for the item.

- Status: Status of item

- Type: Item type

- Category: Category under which the item is classified.

- Price: Selling price of the item.

- Cost: Purchase cost of the item.

- Supplier: Supplier associated with the item.

- If there is no value, show '-'

- Inventory: Stock details for the item across warehouses, including:

- Warehouse: Name of the warehouse.

- On Hand: Quantity available in the warehouse.

- Available

- Reserved

- Reserved: Quantity that’s already set aside for orders or transfers, so it’s not available for new sales.

- In Transit: Quantity currently being transferred to the warehouse.

- Incoming: Total Items on the way TO this warehouse

- Outgoing: Total items being sent FROM this warehouse.

- On Order: Qty ordered from vendor/supplier but not yet received.,

- On Hold: Quantity blocked or reserved for special purposes

Sales Channel Mapping:

- Liệt kê channel - location hiện tại mà item này được pull về từ Shopify

- Current Scope: pull data product từ Shopify và xử lý combine các SKUs bị trùng lại thành 1 inventory item

- Channel: Hiển thị SC mà item được pull về

- SKU: Hiển thị SKU của item

- Location: Hiển thị location được link từ Shopify

- Variant Linked: Conative xử lý các variant có trùng SKU, UPC, barcode. Các variants trùng ở Conative sẽ được xem là 1 inventory items. Và các variant được link chung với 1 inventory items. Số liệu tồn kho được push lên Shopify sẽ cho cả các variants trùng.

- User có thể bật/tắt toggle về Managed: khi user tắt Conative sẽ không tự động push data available qty lên Shopify cho item tương ứng

Forecast by Sales channel:

After mapping the inventory item with the sales channels where the brand sells, display the corresponding sales channels along with the forecast generated by Conative AI.
 Default forecast period is 90 days.

Users can edit the forecast period to view the corresponding forecast.

Lot Section: Default sort by expiration date nearest to today first.

- Warehouse: Show the warehouse location that the lot number belongs to

- Lot Number:

- Show the lot number of item on warehouse

- If there is no value, show “-”

- Expiration Date:

- Show the expiration date of lot on warehouse

- If there is no value, show “-”

- Action Buttons: Options to close or edit the item.

2.

Clicks the Edit button at the bottom of the modal

Switches the modal to an editable mode (See flow #4. Edit an Item Details for details).

3.

Clicks the Close button or the X icon at the top of the modal

The modal closes, and the user is returned to the Item List screen.

3. Import Items

Step #

Actor Action

System Response

1.

Clicks the Import Items button

Opens the Import Items modal (See UC-INV-004.2 for details).

4. Edit an Item Details

Step #

Actor Action

System Response

1.

Clicks the Edit Icon in the Action column for a specific item

Open the Edit Item modal with pre-filled item details.

2.

Update the fields

Validate the updated fields.

3.

Click the "Save" button

• Update the item details.

• Reflect changes in the Item List table.

• Display a success message: "Your changes have been saved."

5. Filter and Search Items

Step #

Actor Action

System Response

1.1

Enter a search term in the Search Bar to find items by name or SKU.

Dynamically update the Item List view to display matching results.

1.2

Click Filter to apply additional filters, such as:
- Warehouse.

- Status (e.g. Active).
- Source

- Quantity range (e.g. On Hand > 10).

1.3

Sort

- SKU

- On hand

- On Order

- In Transit

- On Hold

6. Synchronize Items Data

Step #

Actor Action

System Response

1.

Click the Refresh Data button.

Fetch the latest inventory data, including:

- Quantity updates.

- Status changes (e.g. items marked as Low Stock or Out of Stock).

Refresh the Item List table.

Alternative Flows

ID/ Title

Description

5A. No Data/Search Results Found

• Trigger: The search or filter criteria return no matching items.

• System Response:

- No Data Found

- No Search Results Found

#### 1.1 Business Rules

ID

Rule

#### 1.2 UI & Fields Details

1.2.1 View Items List

Field Name

Type

Default value

Rules

Items List

Default sort by On hand Qty (largest to smallest)

Select Item

Checkbox

Unchecked

- Allows users to select one or multiple rows for bulk actions (e.g. delete).
- If all rows are selected, the header checkbox is checked.

Item Name

Text

N/A

- Displays the name of the items of each warehouse.

Image

Thumbnail

Default placeholder image

- Displays a thumbnail of the product image.
- If no image is uploaded, a default placeholder image is shown.
- Clicking the image opens a product details page.

SKU

Text

N/A

- Displays the unique SKU for the item.

Warehouse

Displays the warehouse of items

On Hand

Numeric

0

- Represents the number of items available in the warehouse.

On Order

Numeric

0

- Represents the number of items currently ordered but not yet received.

In Transit

Numeric

0

- Represents the number of items being transferred between warehouses.

- Incoming: Show the total items on the way TO this warehouse.

- Outgoing: Show the total items being sent FROM this warehouse.

On Hold

Numeric

0

- Represents the number of items held (e.g. reserved for orders or unavailable).

Status

Badge (Text)

Active

- Displays the status of the item

Alert

Badge (Text/Empty)

empty

- Displays alerts for specific conditions:

- Low Stock: Triggered when On Hand quantity is below the threshold.

- Out of Stock: Triggered when On Hand is < = 0.

- Overstock: Triggered when On Hand exceeds the maximum threshold. 
(based on setting of user)

- Expired Lot: Trigger when an item in a warehouse has a lot that is about to expire (based on the user’s settings)

- No badge displayed if no alert conditions are met.

Actions

Action Buttons

N/A

- Buttons available:

- View Details: Opens a detailed product modal displaying all information about the selected item. (See flow #2 above)

- Edit: Opens the Edit Item modal for the selected row. (See flow #3 above). Only enabled for Items created in Conative.

- Delete: Only enabled for Items created in Conative. Prompts the user to confirm deletion of the item.

Items Per Page Dropdown

Dropdown (Select)

10 rows per page

- Allows the user to select how many rows to display on each page.

- Options: 10, 25, 50, 100.

Page Summary

Text

Dynamically updated

- Displays the range of rows currently shown (e.g. "Showing 1 to 10 of 64 records") and the total record count.

Page Navigation

Buttons (Links)

Starts on Page 1

- Includes navigation buttons for moving between pages:
- First Page (<<) (if available).
- Previous Page (<). 
- Page Numbers (e.g. 1, 2, 3).

- Next Page (>).
- Last Page (>>) (if available).


1.2.2 History Tab:

Field Name

Type

Default value

Rules

Textbox search

textbox

Search matches contains-case-insensitive on

### UC-INV-004.2. IMPORT INVENTORY ITEMS

User Story

As an Inventory Manager, 
I want to import multiple inventory items at once using a file upload feature,
So that I can quickly update or add new invent

ory data without entering it manually.

Actor

Primary: Inventory Manager

Trigger

User selects menu item Inventory Management > Inventory Items > Item List > Import Items

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:

- The inventory file is successfully uploaded, processed, and imported into the system.

- Any errors or warnings during the import process are displayed, and the user can download error files for review and correction.

Main Flows

Step #

Actor Action

System Response

1.

Clicks the Import Items button on the Item List screen.

Opens the Import Inventory Items modal with the first step: Upload File with instruction to Download Template File link.

2.

Clicks the Download Template File link

Downloads a pre-filled template file (e.g. CSV or Excel) with the correct column headers:

- Item Name, SKU, Unit of Measure, Category, Warehouse, On Hand, On Order, In Transit, Reserved, On Hold, Cost, Price, and Status

3.

Prepares the data using the downloaded template.

4.

Clicks the Click to Upload area or drags and drops a file into the upload zone.

Validates the uploaded file:

- If valid, the file is accepted and the progress bar tracks the upload.

- If invalid, see Alternative Flow 2A.

4.1

The file is uploaded, the system proceeds to the Map Column step.

4.2

Displays a list of required fields (e.g. Item Name, SKU, etc.) and their corresponding columns from the uploaded file.

5.

Maps the columns manually (or the system auto-detects matches where possible)

Highlights required fields with a warning if any of them are missing.

6.

Clicks Continue to proceed to the next step.

Begins processing the file, displaying a progress bar (e.g. "Processing: 10%").

6.1

Upon completion, the system displays the import summary:

- Successful Rows: Number of rows successfully imported.

- Errors: Number of rows with issues (e.g. missing data, invalid values).

- Warnings: Rows with non-critical issues.

6.2

Provides options to Download Result File  or View Successful Items if there are errors or warnings

6.3

Clicks View Imported Items to review the imported data on the Item List screen.

Alternative Flows

ID/ Title

Description

4A. Invalid File Format

• Trigger: The user uploads an unsupported file format (e.g. PNG instead of CSV)

• System Response: Displays an error message:

"The file format is not supported."

The user must upload a valid file to proceed.

5A. Missing Required Columns

• Trigger: If the uploaded file is missing required columns (e.g. SKU or Item Name)

• System Response: View error messages
 Displays a critical error message:
 "Required columns are missing. Please add the following columns: SKU, Item Name."

The user can download the template file to correct the issue and try again.

6A. Partial Success

• Trigger: If some rows are imported successfully while others fail due to validation issues
• System Response: Displays a summary of successful rows, errors, and warnings.

The user can download the error file to review and fix the problematic rows.

6B. Import Failed

• Trigger: If the entire import fails (e.g. Due to critical errors like missing required columns):
• System Response: Displays a failure message with the reason: "Required columns are missing.

The user can download the template file to correct the issue and try again.

- Button [Try Again]: user click on button, system displays step 1: upload file of Import Inventory Items

#### 1.1 Business Rules

ID

Rule

1

When a line of data is missing required fields while other information is complete, the system skips that line and logs an error.

2

When both the item and warehouse exist in the system, the system must update the related inventory data.

3

When the item exists but the warehouse does not, the system must create a new record of the item under that warehouse.

4

When the warehouse does not exist in the system, the system must log an error message:
 "Warehouse does not exist in the system. Please create the warehouse first.

#### 1.2 UI & Fields Details

Field Name

Type

Default value

Rules

Step Indicator

Progress Indicator

Step 1: Upload File

- Highlights the current step (1, 2, or 3).

Instructions

Text

"Get started by adding multiple items..."

- Static informational text; no interaction.

Download Template File

Link/Button

Link to download template file

- Clicking downloads a pre-filled template with required headers.

File Upload Area

Drag-and-Drop Zone

Empty upload zone

- Accepts files in CSV, Excel formats.

- Max file size: 3MB.
- Shows an error if file format or size is invalid.

Uploaded File Name

Text

N/A

- Displays the name of the uploaded file.

- Shown after a successful upload.

Upload Progress Bar

Progress Bar

Hidden

- Displays upload progress as a percentage.

- Becomes visible after the user uploads a file.

Error Message

Text (Error State)

N/A

- Displays an error message if the uploaded file format or size is invalid: "File format is not supported."

Cancel Button

Button

N/A

- Clicking closes the modal without saving changes.

- Confirmation required if the user has unsaved changes.

Map Column Button

Button

Disabled

- Becomes enabled only after a valid file is uploaded.

- Clicking proceeds to Step 2: Map Column.

Mapped Fields

Dropdown (per field)

Unmapped

- Dropdowns for required fields (e.g. SKU, Item Name).

- Auto-maps columns where possible.

- Highlights missing mappings with a warning.

Column Mapping Warning

Text (Warning State)

N/A

- Displays a message if required fields are not mapped (e.g."12 of 13 fields mapped, 1 missing.").

Continue Button

Button

Disabled

- Becomes enabled only after all required fields are mapped.

- Clicking proceeds to Step 3: Import.

Processing Progress Bar

Progress Bar

Hidden

- Displays the progress of the import process as a percentage (e.g."10% Processing").

Import Summary

Text/Icons

N/A

- Displays statistics post-import:

- Number of rows successfully imported.

- Number of errors and warnings.

- Icons for success.

View Successful Items

Button

Enabled

- Clicking navigates to the Item List screen with successfully imported records highlighted.

Download Error File

Button

Hidden

- Becomes visible if there are errors.

- Clicking downloads a file with failed rows and error descriptions.

Import Another File

Button

Enabled

- Clicking restarts the import process from Step 1: Upload File.

### UC-INV-004.2. IMPORT INVENTORY ITEMS

#### 1.1. Main flow

- User opens Inventory  List and clicks Import Items.

- System displays the Import Inventory Items modal (Step 1: Upload file) with a link to Download template file and a drag-and-drop / click upload area.

- User downloads the template (optional), fills it and uploads a CSV or XLSX file (or directly uploads a prepared file).

- System accepts the file (valid type/size), shows the uploaded file name and enables Map column button.

- System creates an import job ID and persists uploaded file.

- User clicks Map column. System advances to Step 2: Map columns.

- System displays the list of Conative fields (Item Name*, SKU*, UoM, Category, Location/Warehouse, Status, On Hand, On Hold, Cost, Price) with a dropdown for each to select the corresponding column from the uploaded file.

- User maps required fields (at minimum: SKU and Item Name, Warehouse/Location) and any optional fields they want to import, then clicks Continue.

- System validates mapping: all required fields are mapped, numeric columns are valid number formats. If validation passes, system advances to Step 3: Import.

- System processes the file (row-level processing). Progress indicator is shown.

- On completion the system shows an Import Result summary:

- If all rows succeed → “Import Successful (N rows added)” with options Import Another File / View Imported Items.

- If some rows failed or warnings → show counts: Successful / Errors / Warnings and two buttons: View Successful Items and Download Result File.

- If critical failure (missing required columns or unrecoverable error) → show Import Failed with the reason and action (Download template / Try Again).

- If user clicks View Imported Items, system navigates or refreshes Item List with imported rows visible; import audit log accessible in Item history or Import Jobs panel.

#### 1.2. Alternative flow

A1 — File rejected on upload

- If user uploads unsupported file type or size > limit → show inline error: “Supported formats: .csv, .xlsx. Max size: 10MB.” User corrects and re-uploads.

A2 — Required columns not mapped

- On Map step, user tries to Continue without mapping required columns (SKU, Item Name, Location/Warehouse). System prevents continue and shows inline error and disable button [Continue]

A3 — Mapping contains unknown warehouse/location

- If mapped Location/Warehouse column contains values not found in the system, the system processes: Row fails with error {unknown {warehouse/location_field}. User fixes file or creates new warehouse}.

A4 — Partial success (warnings/errors)

- If some rows succeed and some fail, system completes and shows counts. User may download error file (failed rows + error reasons). Successful rows are committed. Warnings (e.g., field mismatches) are shown but commit proceeds.

A5 — Duplicate SKU rows in file

- If same SKU appears multiple times:

- If entries are for different warehouses → treated as separate location records; import proceeds.

- If entries are for same SKU+same warehouse → the system processes them sequentially from top to bottom and always applies the data from the latest row (the last one in the file).

- Earlier rows are ignored (overwritten) for that SKU–Warehouse combination.

- No aggregation or summation is performed — the last occurrence determines the final values.

- For numeric fields (On Hand, On Hold), the value from the last row overwrites all previous values.

A6 — Existing SKU in database

- If SKU exists - Warehouse is new (different warehouse):

- The system will create a new inventory link between the item and that warehouse.

- It initializes the warehouse-level inventory record using the values from the import file (On Hand, On Order, etc.).

- If SKU exists and Warehouse already exists in database:

- The system applies the same “last-row-wins” rule as A5.

- It overwrites the existing record for that SKU–Warehouse pair with the data from the latest row in the import file (sequential order).

#### 1.3 UI & Fields Details:

Step 1 - Upload file:

- Elements:

- Title: Import Inventory Items

- Instruction text + Download template file link.

- Dropzone area: clickable + drag-and-drop.

- Supported formats note: csv, xlsx

- After upload: show uploaded filename, success icon, delete (trash) icon to remove file.

- Buttons: Cancel, Map column (disabled until file uploaded).

Step 2 - Map column:

- Layout: left column = Conative field, right column = Select column from your file (dropdown showing uploaded file columns).

- Required fields are marked with (SKU*, Item Name*, Location/Warehouse*).

- Fields available (example list shown in UI):

- Item Name*

- SKU*

- Unit Of Measure

- Category

- Location / Warehouse*

- Status

- On Hand

- On Hold (integer)

- Cost

- Price

- Top status bar: shows mapping progress (e.g., 12 of 13 mapped — 1 missing) and tooltip listing missing required fields.

- Buttons: Back, Continue (disabled until required fields mapped).

Step 3 - Import & Results:

On completion:

- Import Successful (all rows) → show count and actions: Import Another File, View Imported Items.

- Import Partial (some errors/warnings) → show summary: Success: X rows, Errors: Y rows, Warnings: Z rows. 
Buttons: View Successful Items, Download Result File.

- Import Failed (critical) → show reason, link to template, Try Again button.

Error file: CSV containing only the failed rows with an additional error_reason column for each failed row.

#### 1.4 Business Rules:

1. File/Format rules:

- BR-F01: Supported file types: .csv, .xlsx. Files > 10 MB are rejected. Error message: “File too large - maximum 10MB.”

- BR-F02: Maximum rows per file: 10,000 rows. If exceeded, the system warns and rejects upload (ask to split file). Error message: “File too large. The import file exceeds the 10,000-row limit.”

- BR-F03: Header row required. Column headers are case-insensitive; leading/trailing whitespace trimmed.

- BR-F04: If there are duplicate column names in file, the system appends index (1), (2) in dropdown on step 2 to help mapping.

2. Required Field Rules:

- BR-R01: Required fields: Item Name, SKU, Location/Warehouse. Map-step cannot continue without them.

- BR-R02: If required columns missing from the file during initial validation, import is blocked and the user sees Import Failed — Required columns missing with a link to download the template.

3. Type & format validation:

- BR-T01: Numeric fields (On Hand, On Hold, Cost, Price) must be valid integer numbers (decimals). Commas as thousand separators allowed but must be parsed.

- BR-T02: String trimming: system trims leading/trailing whitespace from mapped string fields (SKU, Item Name, Category). Matching is case-insensitive for lookup purposes.

4. SKU uniqueness:

- BR-S01:

When a SKU already exists in the database:

- If the Warehouse is new (SKU–Warehouse pair not found):

- Create a new inventory record linking the SKU to that warehouse.

- Apply all mapped quantity and attribute values.

 If the Warehouse already exists for that SKU:

- Apply the last-row-wins rule (view BR-D01)

- Overwrite existing values with the final occurrence from the import file.

5. Duplicate rows inside the same file:

- BR-D01: Duplicate rows inside the same file (same SKU + same Warehouse): If the uploaded file contains multiple rows for the same SKU and Warehouse, the system processes them sequentially and applies the latest row (the bottom-most entry in the file).

- BR-D02: Same SKU across different warehouses: Rows with the same SKU but different warehouses are treated as separate inventory records (each SKU–Warehouse pair is distinct). The system imports or updates each warehouse independently

- BR-D03: If there are multiple rows for the same SKU and conflicting non-numeric fields (e.g., two different Item Name values), the system resolves using: Use the last non-empty value encountered (top-down)

6. Warehouse/Location mapping:

- BR-W01: Location/Warehouse values in the file must match an existing Warehouse code/name in Conative (case-insensitive, trimmed).

- BR-W02: If mapped warehouse not found: auto-create warehouse and link inventory to item

- BR-W03: Input: warehouse_name e.

Step A: Query warehouses WHERE name = input AND source = 'conative'.

- Nếu trả về exactly 1 → chọn warehouse này.

- Nếu trả về 0 → goto Step B.

- Nếu trả về >1 → BLOCK this shipment/row (or group) and log error .

Step B: Query warehouses WHERE name/code = input AND source != 'conative' (all other sources).

- If returns exactly 1 → select that warehouse.

- If returns 0 → log error: Warehouse not found (existing rule).

- If returns >1 → BLOCK this shipment/row (or group) and log error

7. Status:

- BR-E01: Acceptable status: Active, Archived, Deleted, Draft. If user does not input, Default = Active

8. Transactionality:

- BR-A01: Import job is row-level atomic:

- Successful rows are committed; failed rows are rejected and written to error file.

- The job is not fully-rolled-back because we support partial success.

- BR-A02: Import engine logs each row result (success/error/warning) with reason.

###  UC-INV-004.3. MANAGE INVENTORY ITEMS HISTORY

User Story

As a warehouse operator or inventory manager,
I want to view the history of changes for inventory items,
So that I can track stock movements, identify discrepancies, and ensure inventory accuracy.

Actor

Primary: Inventory Manager, Warehouse Operator

Trigger

User selects menu item Inventory Management > Inventory Items > History

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:

- The user successfully reviews the inventory item’s history.

Main Flows

1. View Inventory Items History

Step #

Actor Action

System Response

1.

Navigates to the Inventory Items/ History tab

Displays a history table summarizing key details:

- Event type: the type of inventory event including: Import, Transfer, Adjustment, Sync Update.

- Items: The total number of unique SKUs affected by the event.

- Quantity: The total quantity of all items affected by the event.

- Description: A brief description of the event:

- Import: “Inventory updated via import file {new_products_oct26.csv}"

- Transfer: "Transferred from [sourceWarehouseName] → [destinationWarehouseName] <Transfer Order ID>."

- Adjustment:

- Description Template “Adjustment: updated [Field Name] from [Old Value] to [New Value].”

- Fields to Include: On Hand, On Order, In Transit, Reserved, On Hold, SKU, UOM, Status, Type, Category, Cost, Price, Vendor

- Sync Update:

- Description Template "Stock synced from [Source] • [Field Name]=[Value]."

- Fields to Include: On Hand, On Order, In Transit, Reserved, On Hold, SKU, UOM, Status, Type, Category, Cost, Price, Vendor

- Change By: The user or system responsible for the event (e.g. "John Doe" or "System").

- Change Date: The timestamp of when the event occurred in YYYY-MM-DD HH:mm:ss format.

- Action column with a "View Details" button.

2. Search/Filter/Sort History

Step #

Actor Action

System Response

1.

Search, filters or sorts the history by various criteria, such as:

- Event Type

- Changed By (filter not available)

- Change Date (start and end dates).

- Warehouse (specific origin or destination location).

- Item SKU/Name (searching for specific inventory items).

- Quantity (sorting by total quantity moved).

Dynamically updates the displayed results to match the applied filter, searching keywords or sorting criteria. If no results match, the system displays a message such as:

"No events match your criteria. Please adjust your filters."

Alternative Flows

3. View Details of an Event

Step #

Actor Action

System Response

1.

Clicks "View Details" for a specific event in the table.

Displays detailed information about the event, including:

- Transfer event:

- Item & Quantity:

- Displays the SKU, Item Name

- Shows the total units moved of each item

- Transfer Details:

- From Warehouse: Displays the origin warehouse ID and name.

- To Warehouse: Displays the destination warehouse ID and name.

- Transfer Order ID: Unique reference to the transfer transaction (e.g. TO#4421).

- Status: Displays the current status of the transfer (Scheduled, In Transit, Delivered, Cancelled).

- Audit Information:

- Change By: Shows the user/system who triggered the transfer.

- Change Date: Timestamp of when the transfer occurred (YYYY-MM-DD HH:mm:ss).

- Adjustment event:

- Item: Displays the SKU, Item name

- Quantity: Shows the signed quantity change (+10, -5).

- Warehouse & Warehouse ID: Displays the location where the adjustment was made.

- Stock Change Details: Displays a snapshot of stock levels before and after the adjustment for traceability.

- Change By: Shows the user/system who performed the adjustment.

- Change Date: Timestamp of when the adjustment occurred (e.g. YYYY-MM-DD HH:mm:ss).

- Sync Update event:

- Sync Details:

- External Source: Indicates the source of the sync update (e.g. Amazon FBA, Shopify, 3PL name, API).

- Warehouse Updated: Display warehouse is mapped

- Warehouse ID: Display Warehouse ID

- Total Items Synced: Count items is synced

- Stock Change Details:

- Default: Sort by Item field (alphabet A > Z)

- Item: Displays the SKU, item name

- Stock Type: List the stock breakdown by status of inventory item: on hand, in transit, on order, on hold,...

- Before: Shows the old value or delta of stock type

- After: Shows the new value or delta applied (based on the design, snapshot vs. diff).

- Change: Record increase or decrease based on the following formula:

After – Before: positive → increase

After – Before: negative → decrease

- Audit Trail:

- Change By: Always displays "System" to indicate the sync was triggered by automation.

- Change Date: Timestamp of the sync job that triggered the update (YYYY-MM-DD HH:mm:ss).

- Import event: Redirects the user to the Import History page, where the existing implementation displays the import details

ID/ Title

Description

4A. No History Records Found

• Trigger: The user applies filters or searches for criteria that yield no matching results.

• System Response: displays a message: "No history records match your search criteria."

#### 1.1 Business Rules

Type

Trigger Action

Description

Transfer

Create Transfer Order

Transfer order <transferOrderID> created: <itemsCount> items scheduled from <sourceWarehouse> → <destinationWarehouse>

When TO has first shipment is In Transit

Transferred from <sourceWarehouse> → <destinationWarehouse>: <itemsCount> items are in transit (Order <transferOrderID>)

When TO has status = Partially Fulfilled or Fulfilled

Transfer <transferOrderID> delivered: <itemsCount> items received at <destinationWarehouse>

TO has status = Cancelled

Transfer <transferOrderID> is cancelled

Adjustment

Item Information: Update SKU / name / category / vendor / UOM / Status / cost / price

Updated item SKU <SKU>: <field> changed (<old> → <new>) by <user>

Item Inventory: Manual stock adjustment

Adjusted qty for SKU <SKU>: <stock_type> (<before> → <after>) by <user>

Sync Update

Sync product info from external system (e.g. Amazon, Shopify, ERP)

Synced total <count_item> items from <sourceSystem>

Sync on-hand / reserved / in-transit qty

Updated <stockType> for <SKU> via sync (<old> → <new>) from <sourceSystem>

Quantity sync from sales channel (Amazon FBA, Shopify, etc.)

Synced inventory for <SKU> from <sourceSystem>: <before> → <after>

Import

Upload and import new items by CSV

Imported new items from file <fileName> (<totalItems> records)

Import inventory of item

Inventory updated via import file {new_products_oct26.csv}

#### 1.2 UI & Fields Details

Field Name

Type

Rules

Event Type

Text

- Displays the event type, must be one of the predefined event types: Import, Transfer, Adjustment, Sync Update.

Items

Integer

- Displays the total number of unique SKUs affected.

- Must be a non-negative integer.

Quantity

Integer

- Displays the total quantity of items affected in the event.

- Must be a non-negative integer.

Description

Text

- Dynamically generated based on the event type: follow Business Rule table.
Example:

- Import: "Inventory updated via import file {new_products_oct26.csv}"

- Transfer:  "Transferred from [sourceWarehouseName] → [destinationWarehouseName] <Transfer Order ID>."

- Adjustment: "Adjustment: updated on-hand quantity from [Old Quantity] to [New Quantity]."

- Sync Update: "Stock synced from [Source] • Available=[Available Qty], Reserved=[Reserved Qty]."

- Must not exceed 255 characters.

Change By

Text

- Displays the user or system responsible for the event.

Change Date

Datetime

- Displays the timestamp when the event occurred.

Button

Click on the line event, opens a modal of “View Details” or redirects to a detailed page for the specific event. See details in Flow 3. View Details of an Event.

### UC-INV-004.4. EDIT INVENTORY ITEM (EVENT = ADJUSTMENT)

User Story

As an Inventory Manager,
I want to edit item details and inventory data, so that I can keep accurate and up-to-date records of stock levels and item attributes.

Actor

Primary: Inventory Manager

Trigger

- User selects menu item Inventory Management > Inventory Items > Item List > Edit Item Details

- User selects one inventory items and clicks [Adjust]

- Inventory Items list → Row action Adjust

- User click [Import Adjustments]

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:

- The updated item information and inventory data are saved and reflected in the system.

Failure: 
- Validation errors are displayed, and the user is prompted to make corrections before saving.

Main Flows

Step #

Actor Action

System Response

1.

Clicks the Edit Icon in the Action column for a specific item

• Opens the Edit Item modal with pre-filled item details.

• Editable fields are enabled, while non-editable fields are displayed as read-only.

• Editable Fields: All the fields except “Source”, this field is read-only.

2.

Updates the fields

Validate the updated fields.

3.1

Clicks the "Save" button

• Updates the item details.

• Reflects changes in the Item List table.

• Displays a success message: "Your changes have been saved."

3.2

Clicks the Close button or the X icon at the top of the modal

The modal closes, and the user is returned to the Item List screen.

Alternative Flows

ID/ Title

Description

2A. Validation Errors

• Trigger: If a required field is missing or invalid.

• System Response: Highlights the field(s) and displays an error message: "This field is required".

1A

User selects one or more inventory items and clicks Adjust.

System opens the Adjust Inventory modal.

User selects:

- Item (pre-filled)

- Location (Warehouse): pre-filled

- Adjustment mode: Increase / Decrease / Set to exact

- Quantity (for Increase/Decrease/  New Quantity

- Reason (required)

- Note (Optional)

System displays a real-time preview:

- Current On Hand

- New On Hand after adjustment

- Warnings if the adjustment affects availability or causes negative inventory

User clicks Submit adjustment.

- System validates input.

- System creates an Inventory Adjustment record (audit trail).

System updates:

- On Hand quantity

- Available quantity

- Inventory Status

System logs the change in Stock Movements / History.

System triggers inventory sync to connected sales channels if applicable.

System shows success notification and refreshes inventory

1B

##### Step 1 - Upload File

- User opens Inventory Items → Import → Import inventory adjustments

- System displays Step 1: Upload file

- User can:

- Download the CSV template

- Upload a CSV/XLSX file (max size defined by system)

- System validates file format and size

- If valid, system proceeds to Map column

##### Step 2 - Map Columns

- System displays detected columns from the uploaded file

- User maps required system fields:

- Item SKU *

- Warehouse *

- Adjustment Type *

- Quantity *

- Reason *

- System validates that all required fields are mapped

- User clicks Continue

- System proceeds to Preview

##### Step 3 - Preview Adjustments

- System parses the file and simulates adjustments row by row

- System displays preview table including:

- SKU

- Warehouse

- Current Stock

- Adjustment Input

- Final Stock

- Status

- System assigns Preview Status per row:

- Valid – can be applied safely

- Warning - can be applied but has risk (e.g. negative inventory)

- Invalid – cannot be applied

- System displays summary:

- Total rows

- Valid / Warning / Invalid counts

- User chooses how to proceed:

- Apply Valid rows only

- Apply Valid + Warning rows

- Stop import if any Invalid exists

- User clicks Import

##### Step 4 – Import Processing

- System starts processing adjustments

- Progress indicator is shown

- For each row:

- System creates one inventory adjustment record

- Updates On Hand and Available

- Recalculates Inventory Status

- Logs stock movement and audit data

- Processing is transactional per row (errors do not stop valid rows)

##### Step 5 – Import Result

Success (All rows processed)

- System shows: view design

- Actions:

- Import another file

- View inventory history

Partial Success

- System shows:

- X adjustments processed successfully

- Y rows failed and were skipped

- System provides:

- Download result file (with error reasons)

- View successful items

Failure (Blocking error)

- System shows: view design

- Reason is displayed (e.g. missing required column)

- User can download template and retry

#### 1.1 Business Rules

ID

Rule

Just edit when item is created in Conative

##### BR2 - Quantity Calculation

Increase:

New On Hand = Current On Hand + Quantity

Decrease:

New On Hand = Current On Hand − Quantity

Set to Exact:

New On Hand = New Quantity

##### BR3 - Inventory Status Recalculation

After adjustment:

- Available quantity is recalculated.

- Inventory Status is recalculated and updated.

##### BR4 - Negative Inventory Policy

Negative inventory is controlled by system configuration: adjustments resulting in negative On Hand are blocked and warned.

##### BR5 - Integration Sync

Adjustments affecting managed warehouses trigger inventory sync to sales channels.

##### BR6 - Concurrency Control

- System validates inventory values before committing.

- Conflicts must be resolved before proceeding.

##### BR7 - Bulk Adjustment

- User adjusts multiple items in one action.

- System creates a separate adjustment record for each item and location.


Import Adjustments:

ID

Rule

BR1 - One Row = One Adjustment

Each CSV row creates exactly one inventory adjustment record.

BR2 - Audit Trail

Every adjustment logs:

BR3 - Inventory Recalculation

After each adjustment:

- Recalculate On Hand

- Recalculate Available

- Recalculate Inventory Status

BR4 - Transaction Safety

- Adjustments are processed per row

- Failed rows do not roll back successful ones

BR5 - Integration Sync

Adjustments trigger inventory sync to connected sales channels

#### 1.2 UI & Fields Details

Adjust Inventory Modal

Field

Type

Description

Item

Dropdown

Inventory item to adjust

Location (Warehouse)

Dropdown

Warehouse where adjustment applies

Adjustment Mode

Tabs

Increase / Decrease / Set to exact

Quantity / New Quantity

Number

Adjustment value

Live Preview

Info Panel

Current vs New On Hand

Reason

Dropdown

Reason for adjustment

Note

Textarea

Optional comments

Submit / Cancel

Buttons

Confirm or discard changes

Import Adjustments Modal:

Field

Required

Description

Item SKU

Yes

Identifies inventory item

Warehouse

Yes

Warehouse/location

Adjustment Type

Yes

INCREASE / DECREASE / SET

Quantity

Yes

Adjustment quantity

Reason

Yes

Reason

##### Preview Status Definitions

Status

Meaning

Importable

Valid

Fully valid, no risk

Yes

Warning

Valid but risky

Yes

Invalid

Invalid data or blocked rule

No

Field Name

Type

Required?

Rules

SKU

Text Input

Y

- Must be unique and not exceed 50 characters.

UOM

Text Input

N

- Must not exceed 50 characters.

Status

Dropdown

Y

- Only enable to select from the predefined values: Active, Archived, Deleted, Draft.

- If the user doesn't select it. Default status = Active

Type

Text Input

N

- Must not exceed 50 characters.

- Can’t edit

- Default value: Finished Good

Category

Text Input

N

- Must not exceed 50 characters.

- Can’t edit

Cost

Numeric Input

N

- Must be a valid positive numeric value.

Price

Numeric Input

N

- Must be a valid positive numeric value.

Vendor

Dropdown

N

- List all vendor of brand

Source

Text field

-

- Read-only. Predefined or system-generated value.

Warehouse

Text Input (Read-Only)

Y

- Predefined warehouse names linked to the brand.

On Hand

Numeric Input

-

- Must be a non-negative integer

On Order

Numeric Input

-

- Must be a non-negative integer

In Transit

Numeric Input

-

- Must be a non-negative integer

On Hold

Numeric Input

-

- Must be a non-negative integer

Lot Number

Text Input

-

- Must not exceed 50 characters and must be unique.

Expiration Date

Date

-

- Must be a valid date in the future.

Save

Button

N

- Validates inputs, saves data, and displays a success message: “Your changes have been saved.” (or highlights errors if invalid).

Log the adjustment under the History tab.

Cancel

Button

N

- Discards unsaved changes and closes the modal.

### UC-INV-005. MANAGE STOCKMOVEMENTS TAB

User Story

As an inventory manager,
I want to view, search, filter, and manage stock movements,
So that I can track incoming and outgoing inventory efficiently.

Actor

Primary: Inventory Manager

Trigger

User selects menu item Inventory Management > Inventory Items > Stock Movements

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:

- New stock movements are added to the system.

- The stock movements List reflects the changes if any.

- The stock movements data is updated with the latest info.

Main Flow

1. View Stock Movements

Step #

Actor Action

System Response

1.

Navigates to the Stock Movements tab in the Inventory Items.

-  Defaults to this month in the Date Selector.

-  Displays the list of orders (PO & TO) of warehouse (TO include TO outbound & inbound), including the following columns:

- Type: Type of movement (Purchase Order, 
Transfer Order (Outbound)
Transfer Order (Inbound).

- Shipping ID: Unique identifier for the movement.

- From/To: Source and destination locations.

- Quantity: Number of items in the stock movement.

- Total SKU(s): Items included in the movement.

- Expected Ship Date

- Expected Arrival Date

- Actual Received Date

- Source: Source of orders type

- Status: Current status of the movement (Scheduled, In Transit, Delivered, Cancelled).

- Action: Available actions based on the current status. (See Business Rules: BR-SM-001, BR-SM-002, BR-SM-003, BR-SM-004 for details).

2. Search or Filter Data

Step #

Actor Action

System Response

1.

Enter a keyword in the Search Bar (e.g. e.g. Shipping ID, WH from, WH to).

Dynamically updates the table view based on the input.

2.

Clicks the Filter button on the Stock Movements screen.

Opens the Manage Filters modal, displaying the following filter sections:

- Type

- From

- To

- Source

- Status

2.1

Selects values for one or more filters:

- Type: Checkboxes for Purchase Order and Transfer Order.

- Warehouse:

- Warehouse From: Dropdown to specify the source warehouse.

- Warehouse To: Dropdown to specify the destination warehouse.

- Source: Checkboxes for available sources (e.g. Conative AI, NetSuite, and Amazon Seller).

- Status: Checkboxes for Draft, Pending approval, Rejected, Open,
Scheduled, In Transit, Partially Fulfilled, Fulfilled, Cancelled, Closed

Automatically validates user input for dropdown selections (e.g. ensure a valid warehouse is selected).

2.2

Clicks the Apply button

Closes the Manage Filters modal and updates the stock movements table to display only rows matching the selected criteria.

2.2.1

Displays a filter icon with an indicator to signal that filters are active.

2.2.2

The applied filter criteria are persisted until cleared or reset by the user.

2.3

Clicks the Clear All button in the Manage Filters modal.

Deselects all filter criteria and resets the modal to its default state.

2.3.1

Clicks Apply

Updates the table to show all stock movements with no filters applied.

3. Edit Transfer Order

Step #

Actor Action

System Response

1.

Click the Edit Icon in the Action column for a specific stock movement

Open the Edit Stock Movement modal with pre-filled stock movement details.

2.

Update the fields

Validate the updated fields based on the same rules as in "Create Transfer Order" flow.

3.

Click the "Save" button

• Update the stock movement details.

• Reflect changes in the Stock Movement List table.

• Display a success message: "Stock Movement successfully updated."

4. Refresh Data

Step #

Actor Action

System Response

1.

Clicks the Refresh Data button

Performs the following tasks:

- Fetches the latest stock movement data from the server or database.

- Applies any active filters to the refreshed data.

- Updates the table to display the latest stock movements while retaining the user's current sort and pagination settings.

Alternative Flows

ID/ Title

Description

2A. No Search/Filters Results

• Trigger: The search or filter criteria return no matching items or no data found

• System Response:

- No Search/Filter results

- No Data Found

#### 1.1 Business Rules

Rule ID

Rule Title

Rule Description

BR-SM-001

Action Restriction for Scheduled

Stock movements with the "Scheduled" status allow the following actions:

- In Transit: Moves the stock movement to the next status “In Transit”.

- View Details: Enables modification of stock movement details (e.g. quantity, ship-on date).

- Editable fields: Tracking ID, Expected Ship Date, Expected Arrival Date, Notes for Shipment, Requested Qty, Attachments.

- Read-only fields: Source (From), Destination (To), Status, Order Total Cost, SKU, Item Name, Shipment Qty, Receive Qty, Cost

- Cancel Order: Cancels the scheduled stock movement and changes its status to "Cancelled."

BR-SM-002

Action Restriction for In Transit, Partially Fulfilled, Cancelled, Closed

Stock movements with the "In Transit" status allow the following actions:

- Edit: Enables modification of in-transit details (e.g. arrival date).

- Mark as Delivered: Updates the status to "Delivered" once the items are received.

- View Details

BR-SM-003

Action Restriction for Delivered Fulfilled

Stock movements with the "Fulfilled" status allow the following action:

- Duplicate: Creates a new stock movement using the details of the delivered movement as a template.

- View Details

- Close Order

BR-SM-004

Action Restriction for Cancelled

Stock movements with the "Cancelled" status allow the following actions:

- Duplicate: Creates a new stock movement using the details of the canceled movement as a template.

- Reopen: Changes the status back to "Scheduled," enabling the stock movement to be processed again.

#### 1.2 UI & Fields Details

1.2.1 Stock Movements List View

Field Name

Type

Default value

Rules

Search Bar

Input Field

N/A

- Allows partial matches for Shipping ID, SKU, From/To locations.

Filter

Button

N/A

- Opens the Manage Filters modal for selecting and applying filters.

Refresh Data

Button

N/A

- Fetches the latest stock movement data and applies any active filters.

Type

Text

N/A

- Displays the type of stock movement (Purchase Order, Transfer Order).

ID

Text

N/A

- Displays the unique shipping identifier for the stock movement.

From

Text

N/A

- Displays the source warehouse names for the stock movement.

To

Text

N/A

- Displays the destination warehouse names for the stock movement.

Total Quantity

Numeric

0

- Displays the total quantity of the item in the stock movement.

- Must be a non-negative integer.

Total SKU

Numeric

0

- Displays the total number of unique SKUs in the stock movement.
- Must be a non-negative integer.

Expected Ship Date

Date

N/A

- Displays the date when the stock is expected to ship.

- Must be in DD-MMM-YYYY format.

Expected Arrival Date

Date

N/A

- Displays the date when the stock is expected to arrive.

- Must be in DD-MMM-YYYY format.

Actual Received Date

Date

N/A

- Displays the actual date the stock was received.
- Blank if not yet received.

Source

Icon + Text

Integration Source

- Displays the source system (e.g., Conative AI, NetSuite, Amazon Seller).

Status

Badge (Text/Empty)

empty

- Displays the current status of the stock movement:

- Scheduled: Indicates that the stock movement is planned but not yet shipped.

- In Transit: Indicates that the stock has been shipped but has not yet been received.

- Delivered: Indicates that the stock has been successfully received.

- Cancelled: Indicates that the stock movement is stopped and will not proceed. It can be duplicated or reopened if needed.

- Check status of PO & TO in this file:

Actions

Action Buttons

All buttons enabled

- Displays relevant actions based on the stock movement status. See restrictions in Business Rules: BR-SM-001, BR-SM-002, BR-SM-003, BR-SM-004 for details.

Items Per Page Dropdown

Dropdown (Select)

10 rows per page

- Allows the user to select how many rows to display on each page.

- Options: 10, 25, 50, 100.

Page Summary

Text

Dynamically updated

- Displays the range of rows currently shown (e.g. "Showing 1 to 10 of 64 records") and the total record count.

Page Navigation

Buttons (Links)

Starts on Page 1

- Includes navigation buttons for moving between pages:
- First Page (<<) (if available).
- Previous Page (<). 
- Page Numbers (e.g. 1, 2, 3).

- Next Page (>).
- Last Page (>>) (if available).

1.2.2 Manage Filters

Field Name

Type

Default value

Rules

Type

Purchase Order

Checkbox

Unchecked

- Allows filtering by Purchase Order stock movements.

Transfer Order

Checkbox

Unchecked

- Allows filtering by Transfer Order stock movements.

Warehouse

Warehouse From

Dropdown

"Select source warehouse(s)"

- Multi-select dropdown for selecting source warehouses.

Warehouse To

Dropdown

"Select destination warehouse(s)"

- Multi-select dropdown for selecting destination warehouses.

Source

All available sources

Checkbox

All available sources checked

- Allows filtering by stock movements based on their integration source. Displays all available sources dynamically.

Status

Scheduled

Checkbox

Unchecked

- Allows filtering by "Scheduled" stock movements.

In Transit

Checkbox

Unchecked

- Allows filtering by "In Transit" stock movements.

Delivered

Checkbox

Unchecked

- Allows filtering by "Delivered" stock movements.

Cancelled

Checkbox

Unchecked

- Allows filtering by "Cancelled" stock movements.

CTA

Close

Button

Enabled

- Closes the modal without applying changes.

Clear All

Button

Enabled

- Clears all selected filters and resets to defaults.

Apply

Button

Disabled (until filters set)

- Applies the selected filters and refreshes the stock movement table.

### UC-INV-006. MANAGE & VIEW TRANSFER ORDERS

User Story

As an inventory manager,
I want to view, search, filter, and manage stock movements,
So that I can track incoming and outgoing inventory efficiently.

Actor

Primary: Inventory Manager

Trigger

User selects menu item Inventory Management > Inventory Items > Stock Movements > Transfer Order

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:

- The user has successfully viewed, searched, filtered, or navigated through transfer orders.

- If the user clicks the "Create Transfer Order" button, the system redirects to the Create Transfer Order screen.

Main Flow

1. View Transfer Orders

Step #

Actor Action

System Response

1.

Navigate to the Transfer Order screen

• Display a default list of transfer orders, including:

- Shipping Transfer Order ID

- From and To (source and destination warehouses)

- Total Quantity

- Total SKU

- Expected Ship Date

- Expected Arrival Ship Date

- Status

• Display Filters and a Search Bar.

• Display a "Create Transfer Order" button at the top-right corner of the screen.

2. Search or Filter Transfer Orders

Step #

Actor Action

System Response

1.

Enter a keyword in the Search Bar (e.g. Shipping ID, WH from, WH to).

Dynamically updates the table view based on the input.

2.

Clicks the Filter button on the Stock Movements screen.

Opens the Manage Filters modal, displaying the following filter sections:

- Type

- Warehouse

- Source

- Status

2.1

Selects values for one or more filters:

- Type: Checkboxes for Purchase Order and Transfer Order.

- Warehouse:

- Warehouse From: Dropdown to specify the source warehouse.

- Warehouse To: Dropdown to specify the destination warehouse.

- Source: Checkboxes for available sources (e.g. Conative AI, NetSuite, and Amazon Seller).

- Status: Checkboxes for Scheduled, In Transit, Cancelled, Partially Fulfilled, Fulfilled, Closed

Automatically validates user input for dropdown selections (e.g. ensure a valid warehouse is selected).

2.2

Clicks the Apply button

Closes the Manage Filters modal and updates the stock movements table to display only rows matching the selected criteria.

2.2.1

Displays a filter icon with an indicator to signal that filters are active.

2.2.2

The applied filter criteria are persisted until cleared or reset by the user.

2.3

Clicks the Clear All button in the Manage Filters modal.

Deselects all filter criteria and resets the modal to its default state.

2.3.1

Clicks Apply

Updates the table to show all stock movements with no filters applied.

3. Trigger the Create Transfer Order Process

Step #

Actor Action

System Response

1.

Click the "Create Transfer Order" button

Redirect the user to the Create Transfer Order screen (handled in a separate use case: UC-INV-007).

Alternative Flows

ID/ Title

Description

2A. No Search/Filters Results

• Trigger: The search or filter criteria return no matching items or no data found

• System Response:

- No Search/Filter results

- No Data Found

#### 1.1 Business Rules

Rule ID

Rule Title

Rule Description

#### 1.2 UI & Fields Details

1.2.1 Manage Filters

See 1.2.2 Manage Filters in UC-INV-005

1.2.1 Transfer Orders List View

Field Name

Type

Default value

Rules

Sort Fields

- TO ID

- Total Qty

- Total SKU

- Expected Ship Date

- Expected Arrival Date

Shipping Transfer Order ID

Text

N/A

- Displays a unique ID for each order.

From

Text

N/A

- Displays the source warehouse or location.

To

Text

N/A

- Displays the destination warehouse or location.

Total Quantity

Numeric

0

- Displays the total number of items in the transfer order.

- Must be a non-negative integer.

Total SKU

Numeric

0

- Displays the total number of unique SKUs in the transfer order.
- Must be a non-negative integer.

Expected Ship Date

Date

N/A

- Displays the date when the stock is expected to ship.

- Must be in MM-DD-YYYY format.

Expected Arrival Date

Date

N/A

- Displays the date when the stock is expected to arrive.

- Must be in MM-DD-YYYY format.

Status

Badge (Text)

empty

- Displays the current status of the stock movement:

- Scheduled: Indicates that the stock movement is planned but not yet shipped.

- In Transit: Indicates that the stock has been shipped but has not yet been received.

- Delivered: Indicates that the stock has been successfully received.

- Cancelled: Indicates that the stock movement is stopped and will not proceed. It can be duplicated or reopened if needed.

- Check status of TO in this file:

Actions

Action Buttons

All buttons enabled

- Displays relevant actions based on the stock movement status. See restrictions in Business Rules: BR-SM-001, BR-SM-002, BR-SM-003, BR-SM-004 for details.

Items Per Page Dropdown

Dropdown (Select)

10 rows per page

- Allows the user to select how many rows to display on each page.

- Options: 10, 25, 50, 100.

Page Summary

Text

Dynamically updated

- Displays the range of rows currently shown (e.g. "Showing 1 to 10 of 64 records") and the total record count.

Page Navigation

Buttons (Links)

Starts on Page 1

- Includes navigation buttons for moving between pages:
- First Page (<<) (if available).
- Previous Page (<). 
- Page Numbers (e.g. 1, 2, 3).

- Next Page (>).
- Last Page (>>) (if available).

### UC-INV-007. CREATE TRANSFER ORDERS

User Story

As an Inventory manager,
I want to create a new transfer order by specifying the source and destination warehouses, adding order items, and scheduling the shipment,
So that I can ensure accurate and efficient inventory movement between locations.

Actor

Primary: Inventory Manager

Trigger

User selects menu item Inventory Management > Inventory Items > Stock Movements > Transfer Order

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:
- A new transfer order is successfully created and saved in the system.
- The transfer order's status is updated to one of the following:

- Scheduled

- In Transit

Main Flow

Step #

Actor Action

System Response

1.

Navigate to the Create Transfer Order screen

• Display a default list of transfer orders, including:

- Shipping Transfer Order ID

- From and To (source and destination warehouses)

- Total Quantity

- Total SKU

- Expected Ship Arrival Date

- Status

• Display Filters for Source, Warehouse, and a Search Bar.

• Display a "Create Transfer Order" button at the top-right corner of the screen.

2.

Input Transfer Order Details: Shipping ID, Tracking ID, Ship From, Ship To, Expected Ship Date, Expected Arrival Date

3.

Add Order Items

3.1

Click Add Item Button

Open Add Item Modal

3.2

Add item details to the transfer order: Title, UOM, Type, On Hand Qty Requested Qty, Shipment Qty, Received Qty, Expiration Date, Cost

Dynamically calculates and displays the Total Quantity and Total Cost based on the added items and their requested quantities.

4.

Input Additional Information: Notes for Shipment, Attachments

4.1

Add notes or instructions for the shipment.

4.2

Drag and drop files or click to upload additional documents

5.

Finalize and Save the Transfer Order

5.1

Cancel

Discard all inputs and returns to the previous screen.

5.2

Schedule

Save the transfer order with status Scheduled.

5.3

In Transit

Save the transfer order and immediately update the status to In Transit.

5.4

Create Transfer Order

Enable when all required fields already

Alternative Flows

ID/ Title

Description

2A. Missing or Invalid Input

• Trigger: User attempts to save the transfer order with incomplete or invalid data.

• System Response: Displays an in-line error message: "This field is required”.

2B. Transfer order ID already exists

“Transfer order ID must be unique.”

3A. No Items Added

• Trigger: User tries to save without adding any items to the order.

• System Response: Displays an error message: "Please add at least one item to the transfer order before saving."

#### 1.1 Business Rules

Case ID

Condition

Inventory Impact

TO Status

System Action / Rule (dev)

Flags / Audit

UI message

1

Create TO: transfer_qty ≤ on_hand_from

No immediate change

Scheduled

Allow create.

Validate transfer_qty > 0.

audit create TO

-

2

Create TO: transfer_qty > on_hand_from

-

N/A (rejected)

Reject create. Error.

none

Error: "Insufficient stock. Available {A}, Requested {R}."

3

Create Shipment (Scheduled): shipment_qty ≤ transfer_qty and ≤ on_hand_from

No immediate change until In Transit

TO stays Scheduled

Allow create. Mark shipment Scheduled.

audit

-

4

Create Shipment: shipment_qty > transfer_qty and shipment_qty ≤ on_hand_from

No immediate change until In Transit

TO remains (or can be auto-updated later)

create shipment

audit

-

5

Create Shipment: shipment_qty > on_hand_from

-

Block

Block creation. Hard rule.

none

Error: "Cannot create: available {A} < requested {S}."

6

Shipment → In Transit (status change)

on_hand_from -= shipment_qty

in_transit_from +=shipment_qty

TO → In Transit (if ≥1 in transit)

On status change do stock move and record inventory transaction. Can't shipment_qty edits after this.

create stock-move audit

-

7

Receive (Delivered) partial: received_qty < shipment_qty

on_hand_to += received_qty

in_transit_from -= received_qty

TO → Partially Fulfilled (if total_received < total_planned)

Accept partial receive. Update shipment.received_qty.

Keep shipment open or Delivered (per UX).

audit receive

-

8

Receive equal: received_qty == shipment_qty and total_received == total_planned

on_hand_to += received_qty

TO → Fulfilled

Accept. Update shipment.received_qty. If sum(received) == sum(transfer) → TO = Fulfilled.

audit

-

9

Receive greater than shipment: received_qty > shipment_qty

on_hand_to += received_qty

TO → Fulfilled (after confirm)

Warning and need to confirm

none

Warning: "Receive quantity > shipped. Please enable Over-Receive or adjust shipment."

10

After receives: sum(received) < sum(transfer) and no shipments in transit

on_hand_to updated per receives

Partially Fulfilled

Compute totals; set TO status = Partially Fulfilled.

audit

11

After receives: sum(received) == sum(transfer)

on_hand_to updated

Fulfilled

Compute totals; set TO status = Fulfilled.

audit

12

After receives: sum(received) > sum(transfer)

on_hand_to updated

TO = Fulfilled

set flags; audit; notify

Highlight: received_qty > transfer_qty

#### 1.2 UI & Fields Details

1.2.1 Transfer Order Details

Field Name

Type

Default value

Required? (Y/N)

Rules

Shipping Label

Text Input

empty

Y

- Users can manually enter a shipping label.

- Accepts alphanumeric characters only.

Transfer Order ID

Text Input

empty

Y

- Users can manually enter a transfer order ID.

- Accepts alphanumeric characters only.

Search Bar

Text Input

N/A

N/A

- Accepts keywords to search by Shipping ID, Warehouse Source, or Warehouse Destination. 
Title or SKU of item

Ship From

Dropdown

"Select Source Warehouse"

Y

- Lists all available source warehouses owned or managed by the brand owner.

Ship To

Dropdown

"Select Destination Warehouse"

Y

- Lists all internal warehouses owned by the brand owner and external warehouses/fulfillment centers (if the brand owner is allowed to transfer inventory to external parties).

- A warehouse selected as the Source should not appear in the Destination dropdown to prevent self-transfers.

Expected Ship Date

Date Picker

Current Date

Y

- Default to the current date.

- Must be today or a future date.

Expected Arrival Date

Date Picker

empty

Y

> = Today. 
Message inline: Expected arrival date cannot be in the past.

Actual Ship Date

Date Picker

Current Date

Y

- Default to the current date.

- Must be today or earlier if the transfer order is created post-shipment.

Actual Received Date

Date Picker

empty

N

- Must be the same or later than the Expected Ship Date.

1.2.2 Add Items Modal

Field Name

Type

Rules

List Item

List of items will be retrieved based on the “ship/warehouse from”
Status of items = Active, Archived, Draft.

Title

Show name and SKU of Item

UOM

Show UOM of item
If it not available, show “-”

Type

Show type of item

On Hand Qty

Show current stock of item on ship/warehouse from

1.2.3 Order Items List View Tab:

Field Name

Type

Rules

Search Bar

Search bar

- Allows searching for items by title or SKU.

- Filters results dynamically.

Add Item

Button

- Opens a modal to add items to the transfer order.

- The list of items will be retrieved based on the “Ship From”

Title

Text

- Displays the name and SKU of the item selected from the inventory.

UOM

Text

- Displays the unit of measure for the item (e.g. pieces, cartons).

- If not available, show “-”

Current Qty

Numeric

- Displays the quantity of source stock (ship from) & destination stock (ship to)

Transfer Qty

Numeric

- Defaults to the Transfer Qty but can be edited.

- Default value = 0

Received Qty

Numeric

Expiration Date

Date

- Displays the expiration date for perishable items.

Cost

Text

- Populated based on the item's unit cost and requested quantity.

Total Cost

Text

- Automatically calculated as the sum of individual item costs.

Actions

Action Buttons

- Contains buttons to perform actions:

- View: Opens a detailed view modal.

- Edit: Opens a modal to modify item details.

- Delete: (Visible after adding an item) Removes the selected item from the order.

Total

Text

- Displays the total cost of all added/edited items.

- Updates dynamically.

1.2.4 Additional Info

Field Name

Type

Rules

Note for Transfer Order

Text Area

- Allows users to enter optional comments or instructions for the transfer order.

- Prevents the entry of special characters like <, >, or & to avoid potential issues with HTML.

- Maximum character limit: 1024

- If the text exceeds the character limit, display an in-line error message:

"Maximum character limit of 1024 exceeded."

Attachments

File Upload Area

- Users can upload multiple files at once.

- Supported file formats: .pdf, .docx, .xlsx, .png, .jpg.

- Maximum file size per file: 5 MB.

- Maximum number of files: 10.

- Files exceeding size limits or unsupported formats trigger an error message:

"File exceeds maximum size of 5 MB" or "Unsupported file format."

- Displays the uploaded file name and size in a list below the upload area.

- Includes a Remove File (X) button to delete individual files.

- Displays a dashed border with the placeholder text: "Drag files or click here."

- Supports drag-and-drop functionality for file uploads.

- Clicking anywhere in the drag-and-drop area opens a file selection dialog box to upload files manually.

- If a file upload fails, display an error message below the file name:

"Upload failed. Please try again."

1.2.5 Add Shipment in Transfer Order:

WorkFlow:

- Step 1:
 In the Shipment tab of the Transfer Order, the user clicks the [Create Shipment] button.
 The system displays the Create Shipment drawer.

- Step 2:
 The user enters all required information and adds items to the shipment.

- Step 3:
 The user can save the shipment by clicking either the [Schedule] or [In Transit] button.
 The system records the shipment’s current status based on the button selected.

Field Name

Default value

Required? (Y/N)

Rules

Shipping Label

yes

- Shipping label is unique

Tracking ID

no

- User can input

Transfer Order ID

- Disable field

- Show transfer order ID of shipment

- Can’t edit

Ship From

- Disable field

- Show source warehouse from transfer order

- Can’t edit

Ship To

- Disable field

- Show destination warehouse from transfer order

- Can’t edit

Expected Ship Date

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

- Expected ship date >= {Today date}

- Error message under the fields when selecting the past “Expected date cannot be in the past.”

Expected Arrival Date

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

- Expected arrival date >= {Today date}

- Error message under the fields when selecting the past “Expected date cannot be in the past.”

Actual Received Date

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

Actual Ship Date

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

Create Date

- After the shipment is created, the date is recorded and shown when the user views shipment details.

- Format: MMM DD, YYYY

Shipment Items

Search item

- The user can search the title, SKU, ASIN of the item on the transfer order items list.

- If the organization settings has Lot Tracking = Yes, systems expands the item line to display available lots under that SKU:

- Table of add shipment items:

- Title: Item name & SKU

- UOM: UOM of item (if not available, show “-”)

- Type: Type of item (if not available, show “-”)

- Lot:

- Visible only when the brand has lot tracking enabled

- Count the number of lots of items

- Expiration Date:

- Visible only when the brand has lot tracking enabled

- Get the expiration date closest to today

- On hand Qty

- Expandable row (Lot view):

- When clicked, expands to list all available lots for that SKU, with fields: Lot Code, Expiration Date, Quantity.

- User can selects one or more lots of items

- System updates after add items on shipment items Table:

- Shipment Qty: on shipment items table will set default = sum qty of lot item. Editable

- Lot code: Count the number of lots of items that user selected

- Expiration Date: Get the expiration date closest to today

- When no result is matched to searching value, show message like this:

(follow design system - Search_No data match)
Text: Please try searching other keywords or adjusting your filter

Title

Name + SKU of the selected item is shown

UOM

The system fills the UOM of the item.

If none, display "-".

Transfer Qty

- The system auto-fills the Transfer Qty from the selected TO

- View Only

Shipment Qty

- Required fields

- User can update the shipment qty

- Default: show = 0

Received Qty

- The user can input the received qty

- Quantity must be a positive number > = 0

- Type: int

Lot Code

- The user can input the lot code of the SKU

Expiration Date

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

Cost

The system auto-fills the Cost from the selected TO.

Total cost

The total cost per item is calculated based on shipment qty

Total cost = Shipment qty * Cost

The user can’t update.

Action

Delete item

1.2.6 Shipment Tab:

Field Name

Type

Default value

Required? (Y/N)

Rules

Button [Create Shipment]

- Always enable

- Display popup create shipment

Shipping label

yes

- Users can manually enter a shipping label.

Tracking ID

no

- User can manually enter a tracking ID

Transfer Order ID

- Show TO ID

Ship From

- Show ship from of TO

Ship To

- Show ship to of TO

Expected Ship Date

yes

- Allow user input date

Expected Arrival Date

yes

- Allow user input date

Actual Received Date

- Allow user input date

Actual Ship Date

- Allow user input date

Shipment Items

- Button [Add Item]: always enable

- Add Items modal: show only items from the transfer order.

- When user selected item on add item modal, get the items on shipment items table

Search bar

- Accepts keywords to search by Title or SKU

Title

- Display the title and SKU of the item that the user selected from the "Add Item" modal.

UOM

- Display the UOM of item

- If not available, show “-”

Transfer Qty

- Display the transfer qty of item

Shipment Qty

yes

- User can input shipment qty of shipment

Received Qty

no

- User can input received qty of shipment

Lot Code

no

- User can input lot code of item

Expiration Date

no

- User can input expiration date of lot code

Cost

- Show cost of item

Total Cost

- Show cost of shipment qty of item

Action

- Delete item

Note for shipment

- Allows users to enter optional comments or instructions for the shipment.

- Prevents the entry of special characters like <, >, or & to avoid potential issues with HTML.

- Maximum character limit: 1024

- If the text exceeds the character limit, display an in-line error message:

"Maximum character limit of 1024 exceeded."

Attachments

- Users can upload multiple files at once.

- Supported file formats: .pdf, .docx, .xlsx, .png, .jpg.

- Maximum file size per file: 5 MB.

- Maximum number of files: 10.

- Files exceeding size limits or unsupported formats trigger an error message:

"File exceeds maximum size of 5 MB" or "Unsupported file format."

- Displays the uploaded file name and size in a list below the upload area.

- Includes a Remove File (X) button to delete individual files.

- Displays a dashed border with the placeholder text: "Drag files or click here."

- Supports drag-and-drop functionality for file uploads.

- Clicking anywhere in the drag-and-drop area opens a file selection dialog box to upload files manually.

- If a file upload fails, display an error message below the file name:

"Upload failed. Please try again."

Button [Close]

- Always Enable

- Show popup confirm close if data already

Button Schedule

- Enable only when all required fields have been filled in.

Button In Transit

- Enable only when all required fields have been filled in.

1.2.6 History Tab: Hide tab

-  Show no history record in create view (view design)

### UC-INV-008. View Transfer Order Details

#### 1.1. Main flow

- Step 1:In the Inventory Management menu, go to Transfer Order. The user clicks on any transfer order, and the system displays the Transfer Order Detail page.

- Step 2: The user clicks [Edit] to edit the transfer order. The system checks the current status of the transfer order.

- Step 3: If the status = Scheduled, the user enters the necessary information in the detail view and clicks Save.

- Step 4: The system validates all required fields and saves the updated transfer order information.

#### 1.2. Alternative flow

- If the status of TO = Scheduled, user [Cancel Order], the system will update status of TO = Cancelled. 
- Message: Transfer order cancelled successfully.

- If the status of TO != Scheduled, user click [View Details] to view the information of TO

#### 1.3 UI & fields details

##### 1.3.1 Transfer Order Information:

Element / ID

Type

Default value

Business rule

Transfer Order ID

- Display the transfer order ID of order

- Disable, user can’t edit

Ship From

- Display the ship from of order

- Disable, user can’t edit

Ship To

- Display the ship to of order

Expected Arrival Date

- Display the expected arrival date of transfer order

- User can update the field

##### 1.3.2 Order Items Tab:

Element / ID

Type

Default value

Business rule

Search bar

- Accepts keywords to search by Title or SKU

Button [Add Item]

- When user click add item, system will open add item modal

Title

- Display the title and SKU of item

UOM

- Display the UOM of item

- If not available, show “-”

Current Qty

- Display the current qty of source warehouse & destination warehouse

Transfer Qty

- Display the transfer qty of transfer order

- User can edit if the status of transfer order = Scheduled

Received Qty

- Display the received qty of transfer order

- The received quantity of an item is based on the shipments of the transfer order that include the corresponding item.

Cost

- Display the cost of item

Total Cost

- Display the total cost of item

- Formula: cost x transfer qty

Action

- Delete item (when TO status = Scheduled)

##### 1.3.3 Shipment Tab:

Element / ID

Type

Default value

Business rule

Shipment List

- Display all shipments created for the transfer order.

- Sort by newest created date

Button Create Shipment

- Always Enable

Shipment Label

- Display the shipment label

Tracking ID

- Display the tracking ID

- If the value is not available, show “-”

Expected Ship date

- Display the expected ship date of shipment

Expected Arrival Date

- Display the expected arrival date of shipment

Created Date

- Display the created date of shipment

Status

- Display the current status of shipment

Action

- If the status of shipment = Scheduled:

- View Details

- In Transit

- Cancel Shipment

- Delete

- If the status of shipment = In Transit:

- View Details

- Mark as Delivered (status of shipment will update to Delivered)

- If the status of shipment = Delivered:

- View details

- Duplicate: Copy the information of shipment to a new shipment

- If the status of shipment = Cancelled or Closed:

- View Details

- Duplicate

- Delete

##### 1.3.4 History Tab:

Element / ID

Type

Default value

Business rule

History List

List all history records related to this transfer order, sorted in descending order (newest first).


 Log Event Categories:

Event

Description Log

User

Create Transfer Order

Created transfer order {id} from {source_Warehouse: Factory} → {distination_Warehouse}

Cancel TO

Transfer Order {id} has been canceled.

Edit/Update Transfer Order

Added item {sku}: 
Transfer Qty {qty}

Item {sku} removed

Transfer quantity of [SKU] updated from {old} → {new}.

Update the expected arrival date from {} to {}

Created new shipment {shipment_label}

System Updates

{transfer_order_ID} automatically changed from Scheduled → In Transit

{transfer_order_ID} automatically changed from In Transit → Partially Fulfilled

{transfer_order_ID} automatically changed from Partially Fulfilled → Fulfilled

{transfer_order_ID} automatically changed from In Transit → Fulfilled

{transfer_order_ID} automatically changed from Fulfilled → Closed

Update status of shipment

Shipment {shipment_label} is in transit

Shipment {shipment_label} marked as Delivered

Shipment {shipment_label} is cancelled

### UC-INV-009. SHIPMENT MANAGEMENT

#### 1.1 Main flow

- Step 1:The user navigates to the “Inventory Management" > "Shipment" section.

- Step 2: The system displays a list of shipments with details (Shipping Label, Tracking ID, Ship From, Received Warehouse, Type, Expected Ship Date, Expected Arrival Date, Created Date, Status, Action).

- Step 3: Users can

- Filter shipments based on criteria like Status, Warehouse, Date, etc.

- Search for specific shipments using the search bar.

- Sort shipments by clicking on column headers.

- Step 4: Users can perform bulk actions like selecting multiple shipments and applying actions (e.g., delete).

- Step 5: Users can click on an individual shipment to view details.

- Step 6: The system loads shipment details.

#### 1.2 Alternative flow

- 3a. User doesn’t input filters → System displays all available Shipments by default.

- 3b.  If no shipments match the filter, a message "No shipments found" is displayed.

#### 1.3 UI & fields details

Element / ID

Type

Default value

Business rule

Filter: Status

Filter

Multiple selection

Value: In transit, Scheduled, Delivered, Cancelled, Closed

Type

Filter

Multiple selection

Value: Purchase Order, Transfer Warehouse

Lists shipments corresponding to the shipment type

Search

Input

null

Information in the placeholder: Search Shipment label

Allow users to search reports based on the following logic

Shipment label - Fuzzy search
Returns Shipment with the searched Shipment label.

When no result is matched to searching value, show message like this:

(follow design system - Search_No data match)
Text: Please try searching other keywords or adjusting your filter

Create shipment

Button

Enable

onClick: Display a dropdown list:

- Create new shipment: Open a new page to create a shipment.

- Upload shipment: Display the UI to import Shipment list.

Column (Sort)

Button

By default: Show sort icon on “Created date” column (from newest to oldest)

The sort icon will be shown when clicking on the columns:

- Expected ship date

- Expected arrival date

- Created date

Bulk Action

Button

Hidden

Default: Hidden

Show and Enable: Display and enable the feature when at least one row is selected in the table.

onClick: Display a dropdown list (Option: delete)

Delete action: Display message log M01 with deletion reference conditions:

- If the status of shipment = Scheduled:

- View Details

- In Transit

- Cancel Shipment

- Delete

- If the status of shipment = In Transit:

- View Details

- Mark as Delivered (status of shipment will update to Delivered)

- If the status of shipment = Delivered:

- View details

- Duplicate: Copy the information of shipment to a new shipment

- If the status of shipment = Cancelled or Closed:

- View Details

- Duplicate

- Delete

Table

Table

-

Show information:

- Shipment Label

- Tracking ID

- Ship From

- Received Warehouse

- Type: Transfer Order/Purchase order

- Expected Ship Date: MMM DD, YYYY

- Created Date: MMM DD, YYYY

- Expected Arrival Date: MMM DD, YYYY

- Status: current status of the Shipment

- Action:

- If the status of shipment = Scheduled:

- View Details

- In Transit

- Cancel Shipment

- Delete

- If the status of shipment = In Transit:

- View Details

- Mark as Delivered (status of shipment will update to Delivered)

- If the status of shipment = Delivered:

- View details

- Duplicate: Copy the information of shipment to a new shipment

- If the status of shipment = Cancelled or Closed:

- View Details

- Duplicate

- Delete

Business rule for filter

Condition is displayed with “is” by default

Rule ID

Rule Title

Type

Condition

Rule Description

F01

Ship From

Multiple select

Is

Is Not

2 options:

- Vendor/Supplier:

- List all vendor/supplier created on Conative or sync from another ERP

- Multiple selection

- Warehouse:

- List all warehouses of user

- Multiple selection

Use just can selected only 1 option

F02

Received Warehouse

Multiple select

Is

Is Not

List of warehouse

By default - All warehouses

F03

Shipment Label

Multiple select

Is

Is Not

List: all Shipment Label

By default - All Shipment Label

F04

Type

Multiple select

List: Warehouse transfer, Purchase order

By default - both

F05

Status

Multiple select

List all statuses of shipment

By default: all values

F05

Expected Ship Date

Single-numeric

Equal

Before

After

Between

Enter or pick the date/date range

- If the user selects "After" / “Before” / “Equal” , he/she can input the specific date.

- If the user selects “between”, he/she can choose a specific date range.

F06

Created Date

Single-numeric

Equal

Before

After

Between

Enter or pick the date/date range

- If the user selects "After" / “Before” / “Equal” , he/she can input the specific date.

- If the user selects “between”, he/she can choose a specific date range.

F07

Expected Arrival Date

Single-numeric

Equal

Before

After

Between

Enter or pick the date/date range

- If the user selects "After" / “Before” / “Equal” , he/she can input the specific date.

- If the user selects “between”, he/she can choose a specific date range.

### UC-INV-010. CREATE SHIPMENT FROM SHIPMENT MANAGEMENT

#### 1.1 Main flow

- The user navigates to “inventory management” > "Shipment" and clicks "Create shipment".

- The system displays the "Create Shipment" form.

- The user selects the shipment type (Purchase Order or Transfer Order).

- User enters needed information:

- Required details (such as Shipping Label, PO ID, Warehouse, Vendor, Dates). The required fields based on this file.

- Other fields (as in the design).

- User adds shipment items by clicking on the “Add item”

- For the 'Transfer Order' type, the system displays a list of items on Inventory Items

- User selects “Schedule” or “In Transit” to create a shipment

- The system processes the request and confirms the shipment creation if all required fields are filled based on the selected status.

#### 1.2. Alternative flow

- If required fields are missing, the system shows validation errors.

- If the user cancels, a message is shown

- Title: You have not saved all changes

- Content: Do you still want to continue closing this shipment without saving?

- onClicks “Cancel”: the shipment is not created and the system returns to the previous page.

- For the type “Transfer Order”:

- If the user switches the status to 'Transit' or 'Delivered' status, it means the packages have been issued from the 'Ship-from' warehouse. The system will then deduct the stock quantity of the shipped items.

#### 1.3 UI & fields details

Tab

Element

Mandatory

Type

Default value

Business rule

Type of shipment

Yes

Single Selection

Purchase Order

- Value: Purchase Order / Transfer Order

- Required

Basic information

Shipping label

Yes

Text

Null

- Required field

- Show on both type (PO + transfer order)

- Shipping label is unique

Tracking ID

No

Text

Null

- Show on both types (PO + TO)

Transfer Order ID

Yes

Single selection

Null

- Placeholder: Select TO ID

- Display a dropdown list of TO ID that is created on Conative or pull from another source, sorted from A-Z.

- required field

- Only visible when the "Transfer order" option is selected.

Ship From

-

-

Null

- After selecting the TO ID, the Warehouse is displayed (pulled from the selected TO). The user can’t edit.

- Only visible when the "Transfer order" option is selected.

Ship To

-

-

Null

- After selecting the TO ID, the warehouse is displayed (pulled from the selected TO). The user can’t edit.

- Only visible when the "Purchase order" option is selected.


Expected ship date

Yes

Datepicker

Null

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

- Required Field

- Expected ship date >= {Today date}

- Error message under the fields when selecting the past “Expected date cannot be in the past.”

Expected arrival date

Yes

Datepicker

Null

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

- Required Field

- Expected arrival date >= {Today date}

- Error message under the fields when selecting the past “Expected date cannot be in the past.”

Actual ship date

No

Datepicker

Null

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

Actual received date

No

Datepicker

Null

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

Create Date

-

Date

Null

- After the shipment is created, the date is recorded and shown when the user views shipment details.

- Format: MMM DD, YYYY

Shipment items

Search item

-

Search

Null

- The user can search the title, SKU, ASIN of the item on the order items list.

- If the organization settings has Lot Tracking = Yes, systems expands the item line to display available lots under that SKU:

- Table of add shipment items:

- Title: Item name & SKU

- UOM: UOM of item (if not available, show “-”)

- Type: Type of item (if not available, show “-”)

- Lot:

- Visible only when the brand has lot tracking enabled

- Count the number of lots of items

- Expiration Date:

- Visible only when the brand has lot tracking enabled

- Get the expiration date closest to today

- On hand Qty

- Expandable row (Lot view):

- When clicked, expands to list all available lots for that SKU, with fields: Lot Code, Expiration Date, Quantity.

- User can selects one or more lots of items

- System updates after add items on shipment items Table:

- Shipment Qty: on shipment items table will set default = sum qty of lot item. Editable

- Lot code: Count the number of lots of items that user selected

- Expiration Date: Get the expiration date closest to today

- When no result is matched to searching value, show message like this:

(follow design system - Search_No data match)
Text: Please try searching other keywords or adjusting your filter

Add item

-

Button

-

- The user can click on the button “Add item” → a popup is shown to allow the user to select items from the selected TO. 
Sort item by title from A > Z

- Shipment type = transfer order: List all items of Conative is sorted by title form A -> Z

Sort:
- Title
- On hand Qty

Item line

Yes

-

The item has been added following the 'Add Item' step

Note: The user can scroll horizontally to view all columns, but the 'Title' column is fixed.

Title

-

Text

-

Name & SKU of the selected item is shown

UOM

-

Text

-

The system fills the UOM of the item.

If none, display "-".

Transfer Qty

-

Number

Value of the field “Transfer Qty”

- The system auto-fills the Order Qty from the selected TO

- Only visible when the "Transfer Order" option is selected.

Shipment Qty

Number

0

- Shipment Type = transfer order

- Required fields

- User can update the shipment qty

- Default: show = 0

Received Qty

Depends on the status

Number

0

- The user can input the received qty

- Quantity must be a positive number > = 0

Lot Code

No

Text

Null

- The user can input the lot code of the SKU

Expiration Date

No

Datepicker

Null

- Functionality: The system displays a datepicker to allow the user to select dates.

- Format: MMM DD, YYYY

Cost

-

Number

Cost of item

The system auto-fills the Cost from the selected TO.

The user can’t update.

Total Cost

-

Number

0

The total cost per item is calculated based on shipment qty

Total cost = Shipment qty * Cost

The user can’t update.

Total line

-

Number

0

Total order qty = SUM of all items ordered qty

Total shipment qty = SUM of all items shipment qty

Total received qty = SUM of all items received qty

Total is the total cost of all items on the shipment

- Total = Total_cost_1 + Total_cost_2 + …. Total_cost_n

Delete icon

-

Button

Enable

The delete icon (Trash icon) is on each row item allows the user remove item

Note for shipment

No

Text

Null

Placeholder: Type here

Limit characters - GR03

Attachments

No

File

Null

The user can upload a file with format: .xls, .xlsx, .pdf, .csv, .doc, .docx

Maximum - 5MB

- If the file > 5MB → raise error message in the toast “The attachment exceeds the size limit of 5MB. Please upload a smaller file."

Remove

-

Button

Hidden

Enable when the user selects at least one row in the order items table.

onClick: Remove the selected items

Cancel

Button

-

Enable

Rule BR1 - UC 2

#### 1.4 Business Rule:

Rule ID

Rule Title

Rule Description

BR01

Required fields

The following fields are mandatory: Shipping Label, Ship From, Ship To, Expected Ship Date, and Expected Arrival Date. 
Missing required fields trigger inline errors with the message: “This field is required.”

BR02

Date validation

BR03

Transfer order linkage

When a Transfer Order ID is selected, the system auto-fills Ship From, Ship To, and related item data based on the transfer order. If the Transfer Order is Closed or Cancelled, a warning message is shown: “Cannot create shipment for closed or cancelled transfer orders.”

BR04

Unique shipping label

Each shipping label must be unique across all shipments. If the entered value already exists, the system displays an inline error: “This shipping label already exists.”

BR05

Quantity validation

- Transfer Qty: show from TO
- Shipment Qty > 0
- Received Qty ≥ 0

BR07

Lot Code validation

If a Lot Code is entered for a SKU, it must already exist for that item in the system. When users input a new expiration date for an existing (item + lot code) pair, show inline error: “Expiration date mismatch with existing lot code.”

BR08

Expiration date rule

- Each (Item + Lot Code) must have only one expiration date in the system.

BR09

Cost calculation

- Total Cost = Shipment Qty × Cost (per item).
- Summary row automatically sums all item-level total costs.
- User cannot manually edit the calculated Total Cost field.

BR11

File upload validation

- Accepted file types: .pdf, .csv, .xls, .xlsx, .docx.- Maximum file size: 5MB.If limit is exceeded, show toast: “The attachment exceeds the size limit of 5MB.”

BR12

Status change rule

- User can Schedule only if required fields and at least one line item are valid.
- User can Set to “In Transit” only when Shipment Qty > 0 for all active line items

BR13

Inline error behavior

All inline errors appear directly beneath the related field and disappear automatically after corrections are made.

BR14

Note character limit

The “Note for Shipment” field allows up to 5000 characters. Exceeding this limit shows inline error: “The input exceeds 5000 characters.”

BR15

Auto-filled fields

When Shipment is created from a Transfer Order, the following fields are auto-populated and non-editable: Transfer Qty, Ship From, Ship To, Cost, and UOM.

BR17

Activity logging

The system records every change to the shipment, including:• Creation date/time• User who created or modified• Status change (e.g., “Shipment marked as In Transit by {User} on {DateTime}”).

BR18

Status restrictions

- Shipment cannot be deleted when status = In Transit or Delivered.
- Only “Scheduled” or “Cancelled” shipments can be deleted. 
If attempted, show error: “Cannot delete a shipment that has already been shipped.”

BR19

Data synchronization

Upon saving or scheduling a shipment, the system updates related Transfer Order and Inventory data in real-time, ensuring stock movements and quantities are consistent across warehouses.

BR20

Total consistency validation

Before saving, the system verifies that total shipment and received quantities across all items align with expected totals from the linked order. Inconsistencies trigger a validation popup: “Shipment quantities do not match the transfer order.”

### UC-INV-011. View & edit shipment

#### 1.1 Main flow

- Step 1: User logs into the system and navigates to the Shipment page. → The system displays a list of shipments with their current status (Scheduled, In Transit, Delivered).

- Step 2: The user selects an existing shipment to update

- Step 3: The system loads shipment details and then

- ​​For the type "Transfer Order" & status shipment = Scheduled, The user can update all fields

- Shipment labels

- Tracking ID

- Ship from

- Ship to

- Expected ship date

- Expected arrival date

- Actual ship date

- Actual received date

- Add more/Remove item

- Shipment quantities for each item.

- Received qty

- Lot Number & Expiration Date.

- Note for shipments & upload attachments (e.g., invoices, packing lists).

- For the  type "Transfer Order" & status shipment = In Transit, The user can update:

- Expected ship date

- Expected arrival date

- Actual ship date

- Actual received date

- Received qty

- Lot Number & Expiration Date.

- Note for shipments & upload attachments (e.g., invoices, packing lists).

- For the  type "Transfer Order" & status shipment = Delivered, The user can update:

- Actual ship date

- Actual received date

- Received qty

- Lot Number & Expiration Date.

- Note for shipments & upload attachments (e.g., invoices, packing lists).

- Step 4: When the user attempts to save changes, the system checks all required fields are filled.

- Step 5: If there are no errors, The system updates the shipment and displays a confirmation message: “Shipment updated successfully.”

- Step 6: The user can return to the shipment list or select another shipment for processing.

#### 1.2 Alternative Flow:


#### 1.3 UI & fields details

Tab

Element

Mandatory

Business rule

Type of shipment

Yes

- View type of shipment

- Can’t edit

Basic information

Shipping label

Yes

- View shipping label of shipment

- Can edit

- Required field

Tracking ID

No

- View tracking ID of shipment

- Can edit

TO ID

Yes

- View data TO ID

Ship from

Yes

- Only visible when the "transfer order" option is selected.

- Display ship from information

- Required field

- Can edit when shipment status = Scheduled

- The value in the 'Ship from’  field cannot be the same as 'Ship to’.

- If the user selects the same value, display an error message below: “The selected warehouses must be different.”

Ship to

Yes

- Only visible when the "transfer order" option is selected.

- Display ship to information

- Required field

- Can edit when shipment status = Scheduled

- The value in the 'Ship to' field cannot be the same as 'Ship from'.

- If the user selects the same value, display an error message below: “The selected warehouses must be different.”

Status

Yes

- Display current status of shipment

- Can edit

- The mandatory fields for each status here

Expected ship date

No

- Display expected ship date

- Can edit

- Expected ship date >= {Today date}

- Error message under the fields when selecting the past “Expected date cannot be in the past.”

Expected arrival date

Yes

- Display expected arrival date

- Can edit

- Expected arrival date >= {Today date}

- Error message under the fields when selecting the past “Expected date cannot be in the past.”

Actual ship date

No

- Display actual ship date (if any)

- Can edit

Actual received date

No

- Display actual received date (if any)

- Can edit

Create Date

-

- Display created date

- Can’t edit

Shipment items

Search item

-

- Placeholder: Search for Title, SKU, ASIN

- The user can search the title, SKU, ASIN of the item on the order items list.

- When no result is matched to searching value, show message like this:

(follow design system - Search_No data match)
Text: Please try searching other keywords or adjusting your filter

Add item

-

The user can click on the button “Add item” → a popup is shown to allow the user to select items from the selected TO.

- Shipment type = transfer order: List all items of Conative is sorted by title form A -> Z

Item line

Yes

The item has been added following the 'Add Item' step

Note: The user can scroll horizontally to view all columns, but the 'Title' column is fixed.

Title

-

Name & SKU of the selected item is shown

UOM

-

The system fills the UOM of the item.

If none, display "-".

Transfer Qty

-

- Only visible when the "Transfer Order" option is selected.

- The system auto-fills the Transfer Qty from the selected TO

Shipment Qty

Depends on the status

Shipment Type = Warehouse transfer

- Show the shipment quantity of shipment

- User can update the shipment qty when status of shipment = Scheduled

Received Qty

Depends on the status

- Show the received qty of shipment

- The user can input the received qty

- Quantity > = 0

- Type: int

- Raise error message when the user input qty = 0 - “Quantity must be greater than 0.“

- Based on the shipment status to check the required fields.  Missing required field → show M04

Lot Code

No

- Show the lots code of items

- The user can select lots code information

Expiration Date

No

- Show expiration date

- The user can input/edit expiration date

Cost

-

- Show the cost of item

- The user can’t update.

Total Cost

-

- Show the total cost of shipment

- The user can’t update.

Delete icon

-

The delete icon (Trash icon) is on each row item allows the user remove item

Note for shipment

No

Show note data of shipment (if any)

Attachments

No

- Show attachment data of shipment

- The user can upload a file with format: .xls, .xlsx, .pdf, .csv, .doc, .docx

Maximum - 5MB

- If the file > 5MB → raise error message in the toast “The attachment exceeds the size limit of 5MB. Please upload a smaller file."

Cancel

Button

Rule BR1 - UC 2


### 


UC-INV-012. INVENTORY DATA SOURCE CONFIG

User Story

As a user responsible for inventory management,
I want to configure the primary data source for syncing inventory and fulfillment data,
So that the system can pull accurate inventory information from my preferred platform (ERP or sales channel).

Actor

Primary: Warehouse/Inventory Manager

Trigger

User selects menu item Settings > Inventory

Pre-conditions

The user is authenticated and logged into Conative.

Post-conditions

Success:
- The selected data source is registered and saved in the system.
- The system begins syncing inventory data from the selected platform.

Failure:
- The data source configuration remains unchanged.
- The user is informed of the error and can attempt to fix or retry.

Main Flow

Step #

Actor Action

System Response

1.

Access Configuration Options

• Display available options represented as a selectable card with a brief description for inventory data source platforms:

- ERP Platform: Sync data from systems like SAP, Oracle NetSuite, or Microsoft Dynamics.

- Sales Channel: Sync data from e-commerce platforms like Shopify or Amazon.

2.

Click on a card to select a data source.

• The selected card is visually highlighted with:

- A green border.

- A checkmark icon.

3.

Click the Save Changes button.

Validate the selection and attempt to save the configuration.

3.1

If the settings are successfully saved, the system displays a success message:
 "Settings saved successfully."

3.2

If an error occurs during the save process, the system displays an error message:
 "Failed to save settings. Please try again."

Alternative Flows

ID/ Title

Description

2A. No Selection Made

• Trigger: User clicks Save Changes without selecting a data source.

• System Response: The system prevents saving and displays an error message:

"Please select a data source before saving."

#### 1.1 Business Rules

Rule ID

Rule Title

Rule Description

#### 1.2 UI & Fields Details

1.2.1 Question Section

Field Name

Type

Rules/ Contents

Question Text

Text

"Which platform do you currently use to manage your inventory and fulfillment?"

Instruction Text

Text

"Select your primary platform to manage your inventory. This will determine how Conative AI syncs your data."

1.2.2 Platform Options

Field Name

Type

Default value

Rules

Platform Cards

Selectable Cards

Unselected

- Only one platform can be selected at a time.

- Clicking a card highlights it with a border or checkmark to indicate selection.

- Including 3 cards:

- Connect an ERP Platform: Displays an ERP platform description (e.g. SAP, Oracle, NetSuite, Microsoft Dynamics).

- Connect a Sales Channel: Displays a sales channel description (e.g. Shopify, Amazon).

- Connect Conative: Allows integration with the Conative ERP system for inventory and fulfillment.

Guideline Section

Text

N/A

- Displays as a non-interactive section.

Save Changes

Button

Disabled

- Enabled only when a platform and a connection method are selected

- Saves the selected platform and connection method.

### UC-INV-013. Integration Hub:

Goal: When a Shopify store is connected and the “Manage my Shopify inventory” feature is enabled, Conative will pull products & locations from Shopify, map them to Conative warehouses and push calculated available stock back to Shopify

#### 1.1 Main flow - Enable inventory sync and complete mapping

- User truy cập vào integration of Shopify.

- Hệ thống hiển thị thông tin store connection:

- Shopify store URL

- Store name

- Connection status

- Last sync

- User bật toggle Manage my Shopify inventory.

- Hệ thống hiển thị popup confirm Enable Shopify inventory sync?

- User chọn Enable sync.

- Hệ thống bắt đầu:

- Pull Shopify locations

- Pull Shopify products / inventory-related data cần thiết

- Hệ thống hiển thị trạng thái cấu hình inventory sync trên trang.

- Ở section Warehouse → Location mapping, hệ thống hiển thị danh sách warehouse của Conative.

- Nếu chưa có warehouse nào, hệ thống hiển thị empty state và CTA Add first mapping.

- User chọn Add first mapping hoặc Add another warehouse.

- Hệ thống mở form thêm warehouse / linking warehouse.

- User nhập thông tin warehouse và chọn Linked sales channel location là Shopify location tương ứng.

- User bật/tắt option Push inventory to this location nếu có.

- User lưu warehouse mapping.

- Hệ thống validate dữ liệu.

- Hệ thống tạo mapping giữa Conative warehouse và Shopify location.

- Hệ thống hiển thị mapping đã được tạo trong section Warehouse → Location mapping.

- Hệ thống hiển thị cấu hình mặc định ở section Starting inventory for warehouse: Match existing Shopify quantity

- Sau khi có ít nhất 1 mapping hợp lệ và sync đang bật, hệ thống bắt đầu dùng mapping này để đồng bộ inventory từ Conative sang Shopify.

- Hệ thống cập nhật Last sync khi quá trình sync chạy thành công.

- User navigates to Integration Hub → Shopify and clicks Connect (OAuth).

- Conative obtains required scopes (read_products, read_inventory, read_locations, write_inventory, webhooks). UI shows Connected.

- User click on Shopify source, user enables the toggle Manage my Shopify inventory.

- Hệ thống tiến hành:

- Pull data products & locations ở shopify

- Ghi nhận qty cho từng item tương ứng như dữ liệu hiện tại trên Shopify

#### 1.2 Alternative Flow:

AF1: User cancel ở popup confirm: hệ thống đóng popup, toggle trở về sn tt =OFF

AF2: Chưa có warehouse nào ở Conative tại thời điểm setting:

- Hệ thống hiển thị empty state (View design) & btn [Add first mapping]

- User click btn hệ thống hiển thị drawer add new WH tương ứng


AF3: Warehouse đã tồn tại trong hệ thống nhưng chưa link Shopify location:

- Ở section WH - location mapping: hiển thị warehouse với stt = Not linked

- Btn [Link now] enable

AF4: User xóa mapping:

- Ở drawer warehouse: User đã có warehouse-location mapping.

- User bấm icon X/Delete ở dòng mapping.

- Hệ thống xóa liên kết giữa Conative warehouse và Shopify location & nhấn [Save].

- Hệ thống dừng push inventory cho mapping đó.

- Nếu không còn mapping nào hợp lệ, inventory sync không thể tiếp tục hoạt động cho bất kỳ warehouse nào.

#### 1.3 UI & fields details

##### Integration main card (top)

- Store connection (URL): Ghi nhận URL store của user ở Shopify

- Store name: Ghi nhận store name của user

- Last sync timestamp:

- Ghi nhận thời gian mà Conative sync dữ liệu available_qty lên Shopify

- Format: MM/DD/YYYY HH:MM AM/PM

- Connection status badge (Connected / Disconnected)

##### Inventory management section (toggle)

- Toggle: Manage my Shopify inventory (ON/OFF)

- Auto-behavior information block: Hiển thị các tác vụ hệ thống sẽ làm khi feature được bật:

- Download products created in Shopify

- Push inventory updates to Shopify

- Warehouse → Location mapping section:

- Section này hoạt động tương tự & song song với trang Warehouse list

- Btn [Add first mapping]: Hiển thị khi chưa có WH nào được tạo ở Conative

- Btn [Add another warehouse]: luôn enable

- Btn [Link now]: Hiển thị cho các WH đã tạo ở Conative nhưng chưa có mapping location Shopify

- Checkbox: Download products created in Shopify (auto-create)

- Value: Match existing Shopify quantity (initial starting inventory sync): Conative sẽ tiến hành pull qty hiện tại của item ở Shopify và ghi nhận qty này làm starting inventory cho item đó ở Conaitve

- Button: Location mapping: redirect đến trang Warehouse list để user mapping location tương ứng

#### 1.4 Business Rules

- Trường hợp sau khi connected Shopify xong:

- User không bật toggle “Manage my Shopify inventory”: Hệ thống hoạt động theo flow cũ, vẫn pull data product và stock near real time từ Shopify về để phục vụ cho các tính năng report của Conative Analytics

- User bật toggle “Manage my Shopify inventory”: Ngoài hoạt động theo flow cũ. Hệ thống tiến hành pulls data locations & product/variant từ Shopify cho Warehouse list (mapping location) & Inventory Items

### UC-INV-014. Logic sync available qty Shopify ⇄ Conative

#### 1.1 Nguyên tắc tổng quát:

- Conative là hệ thống quản lý tồn kho trung tâm khi user bật tính năng inventory management ở details connected source Shopify

- Shopify location phải được map 1–1 với warehouse của Conative.

- Số available qty ban đầu của warehouse Conative = available qty hiện có trên Shopify tại thời điểm mapping.

- Conative không cho nhập tay on hand / available, tất cả thay đổi phải qua event.

- Sync 2 chiều:

- Shopify → Conative: near real-time để hiển thị & kiểm soát sai lệch

- Conative → Shopify: chỉ push khi có event phát sinh trong Conative (PO or tạo adjust), và luôn pull Shopify trước khi push

#### 1.2 Onboarding Phase:

##### 1.2.1 User mapping location:

- Warehouse được tạo ở Conative

- Map với Shopify Location (được pull từ Shopify về)

- Rule:

- 1 Shopify location ↔ 1 Conative warehouse

- Không cho map nhiều location vào 1 warehouse (tránh lệch tồn) (Chưa làm ở phase hiện tại)

##### 1.2.2 Conative pull product & available qty từ Shopify:

- Sau khi mapping:

- Conative gọi Shopify API:

- Pull tất cả product variant

- Pull available qty theo location đã map

- Với mỗi variant:

- Lưu available_shopify

- Lưu shopify_variant_id, shopify_location_id

##### 1.2.3 Tạo tồn kho ban đầu trong Conative:

- Không set trực tiếp On Hand

- Tồn kho ban đầu được tính như sau:

- On hand = available_shopify

- Available (Conative) = available_shopify

- Available (Shopify snapshot) = available_shopify

#### 1.3 Cơ chế Shopify → Conative (near real-time pull):

=> là workflow mà trước giờ L2 xử lý, giữ nguyên flow này

#### 1.4 Cơ chế Conative → Shopify (push available_qty):

##### 1.4.1 Khi nào Conative push qty lên Shopify:

Khi có event làm thay đổi tồn kho trong Conative, ví dụ:

- Receive PO

- Manual adjustment

- Release on hold (on hold được chuyển thành on hand)

##### 1.4.2 Required Logic:

- Trước khi push phải luôn pull data available_qty ở Shopify về trước (tránh overwrite sai khi shopify vừa bán hàng)

##### 1.4.3 Flow Details: example case for spec

- Step 1: Event xảy ra trong Conative:

- Ví dụ: Receive PO +50 (delta_quantity = +50)

- Conative sẽ tạo inventory movement và recalculate: Available_conative

- Step 2: Pull Shopify qty latest:

- Gọi Shopify API

- Update snapshot

- Step 3: Compare & xác định qty cần push

- Available_conative = new_shopify_available = available_shopify_latest + delta_quantity


Inventory Event

Ảnh hưởng thực tế

delta_quantity

Receive Purchase Order

Hàng nhập kho

+received_qty

Manual Adjustment (+)

Điều chỉnh tăng

+adjusted_qty

Manual Adjustment (−)

Điều chỉnh giảm

-adjusted_qty

Release On Hold

Mở khóa hàng

+onhold_qty được move qua on_hand

Put On Hold

Khóa hàng

-onhold_qty (move từ on_hand qu)_

Với delta_quantity = available_after_event − available_before_event

- Step 4: Push lên Shopify

- Push available_Conative lên Shopify location đã map

- Có: Lock theo SKU + Location

- Step 5: Update snapshot:

Update:

- available_shopify = available_conative

- last_push_at

- push status

### UC-INV-015. Settings - Inventory Tab:

#### 1.1 Objective:

Cho phép user cấu hình các ngưỡng (threshold) để hệ thống tự động xác định trạng thái tồn kho cho từng Inventory Item, bao gồm:

- Out of Stock

- Low Stock

- Overstock

Sau khi cấu hình và lưu, các rule này sẽ được apply tự động và hiển thị tại cột Inventory Status trong danh sách Inventory Items.

#### 1.2 Main Flow:

- User truy cập Settings → Inventory → Inventory Status

- Hệ thống hiển thị:

- Expiration date alert

- Inventory status configuration

- User cấu hình Low Stock Detection

- Chọn Threshold Type (Absolute units / Percentage of target)

- Nhập Threshold Value (qty or %)

- (Nếu chọn Percentage of target) user cần nhập thêm Default Target Stock Level

- User cấu hình Out of Stock Detection

- Nhập OOS Threshold

- User cấu hình Overstock Detection

- Chọn Threshold Type (Absolute units / Percentage of target)

- Nhập Threshold Value

- (Nếu chọn Percentage of target) user cần nhập thêm Default Target Stock Level

- Hệ thống hiển thị Configuration Preview (diễn giải logic bằng text)

- User click Save all changes

- Hệ thống:

- Validate dữ liệu

- Lưu cấu hình

- Recalculate inventory status cho toàn bộ Inventory Items

- Inventory Status của từng item được cập nhật và hiển thị tại:

- Inventory list

- Inventory item detail

#### 1.3 Alternative Flow:

##### AF1 – Restore Default

- User click Restore default

- Hệ thống reset toàn bộ rule về giá trị mặc định

- Configuration Preview cập nhật theo default

- Inventory status chưa thay đổi cho đến khi user click Save all changes

##### AF2 – Invalid Configuration

- Threshold value < 0

- Percentage > 1000% (hoặc vượt giới hạn cho phép)

- Percentage selected nhưng Default Target Stock Level = 0

Hệ thống hiển thị error message và không cho save

##### AF3 – Change Threshold Type

- User đổi Threshold Type (Absolute ↔ Percentage)

- Hệ thống:

- Reset giá trị mà user đã nhập trước đó

- Hiển thị / ẩn field liên quan (ví dụ: Default Target Stock Level)

##### AF4 – Zero Inventory Scenario

- Nếu Available = 0. Item luôn được đánh dấu Out of Stock, bất kể cấu hình Low Stock hay Overstock

#### 1.4 UI & Fields Details

##### 1. Low Stock Detection

Field

Type

Description

Threshold Type

Dropdown

Absolute units / Percentage of target

Threshold Value

Number / %

- Giá trị ngưỡng

- Không nhập giá trị âm

Default Target Stock Level

Number

Chỉ hiển thị khi Threshold Type = Percentage

##### 2. Out of Stock Detection

Field

Type

Description

OOS Threshold

Number

- Ngưỡng xác định Out of Stock

- Default: 0

##### 3. Overstock Detection

Field

Type

Description

Threshold Type

Dropdown

Absolute units / Percentage of target

Threshold Value

Number / %

- Giá trị ngưỡng

- Không nhập giá trị âm

Default Target Stock Level

Number

Chỉ hiển thị khi Threshold Type = Percentage

##### 4. Configuration Preview

- Hiển thị rule dưới dạng human-readable, tuỳ thuộc configuration của user ở trên, ví dụ:

- Out of Stock: Available ≤ 0

- Low Stock: Available < 50 units

- Overstock: On Hand > 200% of target (200 units)

#### 1.4 Business Rules:

##### BR1 - Thứ tự ưu tiên Inventory Status

- Out of Stock

- Low Stock

- Overstock

- In Stock

Một item chỉ có 1 trạng thái duy nhất tại 1 thời điểm.

##### BR2 - Logic xác định status

- Out of stock:

If Available ≤ OOS Threshold

→ Status = OOS

- Low Stock:

- Absolute units: If Available < LowStockThreshold

- Percentage of target: If Available < (Threshold % × Target Stock Level)

- Overstock

- Absolute units: If On Hand > OverstockThreshold

- Percentage of target: If On Hand > (Threshold % × Target Stock Level)

##### BR3 - Target Stock Level

- Dùng cho tất cả phép tính theo Percentage

- Nếu item không có target riêng → dùng Default Target Stock Level

- Nếu target = 0 → không cho dùng Percentage rule

##### BR4 - Apply Scope

Rule được apply cho:

- Tất cả Inventory Items

- Tất cả locations


