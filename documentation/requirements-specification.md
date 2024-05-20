# Requirements Specification

This document contains the requirements that specify, how the goals in the [context specification](./context-specification.md) will be achieved. The requirements are split between [functional](#functional-requirements) and [non-functional](#non-functional-requirements) requirements.

## Functional Requirements

The following requirements, specified in the use case format, are in scope of the **tiny-chef** system.

### Requirement 1: General navigation

This use cases serves to outline the general navigation in the graphical user interface (UI).

| R1UC1 | Landing page |
|---|---|
| Actors | User |
| Preconditions | - |
| Main Success Scenario | 1. If the user opens the application, the system displays the current list of pantry items. |
| End Condition | The most recent pantry list is displayed. |
| Extensions | - |

### Requirement 2: Managing the pantry

These use cases contribute to realizing goal G1 of the [context specification](./context-specification.md).

| R2UC1 | Adding pantry items |
|---|---|
| Actors | User |
| Preconditions | - |
| Main Success Scenario | 1. If a user presses the "Add item" button, a popup window opens containing an input form for a new item. |
| | 2. If all fields in the popup window are filled, and the user presses "Add", then the item will be added to the storage. |
| | 3. If the item type did not exist before, then a new item will appear in the list of the virtual pantry. |
| End Condition | The given amount of the item has been added to the list of items |
| Extensions | 2.b If at least one of the fields is not filled and the user presses "Add", then an error message "Please fill all input fields" will appear in red below the add button. |
| | 3.b If the item type already existed before, then the given amount will be added to the already existing amount. |

| R2UC2 | Changing pantry items |
|---|---|
| Actors | User |
| Preconditions | At least one item exists in the pantry list |
| Main Success Scenario | 1. If the user clicks on an existing item, a popup window with editable information about that item appears. |
| | 2. If the user presses "Save" and has changed the amount of the item, then the amount will be updated in the virtual pantry. |
| End Condition | The list of items shows the updated amount of the changed item. |
| Extensions | 2.b If the user presses "Save" and the new amount equals the old amount, then no changes will be applied. |
| | 2.c If the user presses "Save" and the new amount of the item is 0, then the item will disappear from the list of items. |

### Requirement 3: Obtaining recipes

These use cases contribute to realizing goal G2 of the [context specification](context-specification.md). In the scope of this requirement are two *item usage modes*:

1. **Optimal**: Here, the recipe proposal will include *as many existing pantry items* as possible.
2. **Random**: Here, the recipe proposal will include *at least one existing pantry item*.

| R3UC1 | Generating a recipe |
|---|---|
| Actors | User |
| Preconditions | At least one item exits in the pantry list |
| Main Success Scenario | 1. If the user clicks on "Get recipe proposal", a popup window opens where the user can specify dietary restrictions and which *item usage mode* the recipe proposal should use. |
| | 2. If the user presses "confirm", the system generates a recipe proposal, closes the first popup window, and opens a new popup window with the recipe and a "Get cooking"-button. |
| End Condition | A recipe proposal complying to the stated dietary restrictions and *item usage mode* which has a readiness level of at least 10% is displayed. |
| Extensions | |

| R3UC2 | Obtaining a shopping list |
|---|---|
| Actors | User |
| Preconditions | A recipe has been generated and is open in a popup window |
| Main Success Scenario | 1. If the user presses the "Get cooking"-button and at least one of the recipe items is not contained in the current pantry list, the system shows a "Shop for remaining items"-button below the recipe proposal. |
| | 2. If a user presses the "Shop for remaining items"-button and the list of missing recipe items contains 3 entries or less, the system shows a shopping list in a new popup window. |
| End Condition | A list containing the items and amounts necessary to achieve the items on the shopping list when currently having only the items from the pantry list is displayed. |
| Extensions | 1.b If the user presses the "Get cooking"-button and none of the recipe items are missing from the current pantry list, the messsage "You already have everything - get cooking!" is displayed below the recipe proposal. |
| | 2.b If a user presses the "Shop for remaining items"-button and the list of missing recipe items contains more than 3 items, the system additionally offers to download the list in PDF format. |
| | 2.c If the user presses the "Shop for remaining items"-button and their account is connected to any supported home delivery service for groceries, the system instead automatically orders the missing recipe items. |

## Non-functional Requirements

The following non-functional requirements shall be adhered to:

1. The system shall be easily maintainable.
2. The system shall be accessible to users with all types of color-blindness.
3. The system shall be scalable to any number of concurrent users.
