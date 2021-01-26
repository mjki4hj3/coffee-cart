---
Requirements:
  - main collection of products and couriers
  - allow for order new orders to be created on the system
  - updatet status of the order i.e. preparing, out-for-delivery, delivered
  - data persistence
  - load all persisted data
  - tested and proven to work well (unit tesing)
  - recieve regular software updates


  ## Pseudo Code
- START APP
- SHOW LIST OF OPTIONS TO USER AND ACCEPT NUMERICAL INPUT
- IF USER ENTERS 0 THEN EXIT APP
- IF USER ENTERS 1 THEN SHOW PRODUCT MENU
  - IF USER ENTERS 0 RETURN TO MAIN MENU
  - IF USER ENTERS 1 PRINT OUT PRODUCTS TO SCREEN
  - IF USER ENTER 2 CREATE NEW PRODUCT
    - ASK USER FOR THE NAME OF THE PRODUCT
    - APPEND THIS TO THE LIST OF PRODUCTS
  - STRETCH IF USER ENTERS 3 UPDATE PRODUCT
    - ASK USER TO SELECT A PRODUCT TO UPDATE
    - ASK USER FOR NEW NAME OF PRODUCT
    - REPLACE PRODUCT AT SELECTED IDX WITH NEW NAME
  - STRETCH IF USER ENTERS 4 DELETE PRODUCT
    - ASK USER TO SELECT A PRODUCT TO DELETE
    - REMOVE THIS ITEM FROM THE PRODUCT LIST
---
