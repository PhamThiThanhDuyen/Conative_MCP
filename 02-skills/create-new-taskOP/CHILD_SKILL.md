---
name: devtak-child-testing
description: Create and configure a TESTING child work package under a specified DevTak parent ticket, especially MCP connection tests under #86216. Use when asked to add a child ticket through a work package's Relations tab.
metadata:
  short-description: Create DevTak child testing tickets
---

# Create a DevTak testing child ticket

Use this workflow when the user asks to create a TESTING ticket as a child of an existing DevTak work package. The workflow used most often here is under parent #86216, "Conative MCP Connection".

## Gather request details

Use the title, assignee, start and finish dates, and description the user supplied. If a field is omitted, do not invent task-specific content; ask only if that missing field is required to create the requested ticket. Treat "today" as the user's current local date.

## Create from Relations

1. Open the requested parent work package and its **Relations** tab; verify the parent title and ID before creating anything.
2. Open the **Relation** menu and choose **Create new child**. This opens the **New work package** dialog. Do not select ordinary related/predecessor/successor relations.
3. Enter the requested subject and choose the exact **TESTING** type. The type menu may also contain **AUTOMATION TESTING**; verify that **TESTING** itself is selected before creating.
4. Enter a description in the dialog only if the user requested one and the editor is available. Create the child and wait for the success confirmation that it was added as a child.
5. Read the new work package ID from the child list or success result and open the new ticket. Verify its parent, title, and type.

## Configure the new ticket

1. Set the Assignee to the exact requested account. For `duyenpham@chidoanh.com`, search that email, select its matching option from the dropdown, and confirm the saved field shows that email.
2. Set the start date and finish date as requested. When both are "today," set both to the same local calendar date. The date picker exposes separate start and finish fields; change both and save the picker.
3. Enter the requested description in the rich-text description editor. Preserve headings, lists, emphasis, and exact values such as organization names. Save the editor and verify the updated description is visible.
4. Verify the activity/update confirmation and the final assignee and dates. If the range has the same start and finish date, verify activity history or the date picker confirms both values.

## Interaction notes

- DevTak's UI controls may sit inside nested browser content. Use a fresh screenshot and accessibility state before coordinate interaction. On this setup, the visible screenshot coordinate for some controls differed vertically from the CUA click coordinate; calibrate against a known visible control and re-check the UI after each action.
- Keyboard navigation can be more reliable for committing inline edits: Tab to the visible Save button, verify it is focused, then press Space and check for a success message.
- A menu label can be easy to misselect. Confirm the dialog title and selected type before creating; confirm the new child appears under the intended parent afterward.
- Stop and report the precise blocker if the requested parent, type, or save action cannot be verified. Do not claim success from an attempted click alone.
