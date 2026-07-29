# GINKOVA Project TODO

## 1. API / REST Improvements

### Cart API

- [ ] Change CartRemoveAPIView method:
      Current: POST
      Final: DELETE

- [ ] Review CartUpdateAPIView method:
      Current: PUT/POST (depending on final implementation)
      Final: PUT or PATCH

- [ ] Add proper REST API error handling

- [ ] Add API response standard format:
      {
          "success": true,
          "message": "",
          "data": {}
      }


---

# 2. Authentication

- [ ] Implement DRF Authentication

Options:
- Token Authentication
- JWT Authentication (Recommended)

Tasks:
- User login API
- User logout API
- User registration API
- Password reset API
- Permission management


---

# 3. Cart Module

Completed:

[x] GET Cart API

      GET /api/cart/


[x] Add Item API

      POST /api/cart/add/


[x] Update Cart API


[x] Remove Cart API


Future:

- [ ] Move Cart Business Logic from API Views to cart/services.py

Reason:
Keep architecture clean:

API
 |
Service
 |
Models


- [ ] Add cart expiration management

- [ ] Prevent checkout with empty cart


---

# 4. Checkout Module

To Do:

- [ ] Create Checkout API

Flow:

Cart
 |
Check Address
 |
Create Order
 |
Create Payment
 |
Payment Confirmation


- [ ] Validate cart before creating Order

Checks:
- Meal availability
- Price validation
- Quantity


---

# 5. Order Module

To Do:

- [ ] Create Order API

- [ ] Convert Cart to Order

- [ ] Save OrderItems from CartItems

- [ ] Clear Cart after successful Order creation

- [ ] Connect Order with Payment


Order Status:

Current:

pending_payment

paid

confirmed

preparing

delivering

completed

cancelled


---

# 6. Payment Module

Completed:

[x] Payment Model design

[x] Wallet payment logic design


To Do:

- [ ] Complete online payment service

- [ ] Add payment gateway integration

- [ ] Save gateway reference number

- [ ] Save gateway response

- [ ] Handle failed payment

- [ ] Handle refund process


Payment methods:

- Online Gateway
- Wallet
- Bank Transfer (Future)


---

# 7. Wallet Module

Completed:

[x] Wallet Model

[x] WalletTransaction Model


To Do:

- [ ] Create Wallet Charge API

- [ ] Connect Online Payment with Wallet Charge

- [ ] Add Wallet History API

- [ ] Add Refund to Wallet


---

# 8. User Address

Completed:

[x] UserAddress model design

[x] Soft delete approach


Rules:

- First address becomes default

- Address with previous orders cannot be deleted physically

- Use soft delete


To Do:

- [ ] Address API

Functions:

- Add Address
- List Addresses
- Select Default Address
- Soft Delete Address


---

# 9. Database

Current:

SQLite


Future:

- [ ] Migrate to PostgreSQL

Tasks:

- Database settings
- Migration testing
- Data transfer


---

# 10. Frontend

Current:

API First


Future:

Options:

- React Web Application
- Mobile Application


To Do:

- [ ] Build Frontend after Backend stabilization


---

# 11. Development Tools

To Do:

- [ ] Setup Postman Collection

Include:

- Authentication API
- Cart API
- Order API
- Payment API
- Wallet API


- [ ] Add API documentation

Possible:
- Swagger / OpenAPI


---

# 12. Architecture Improvements

To Do:

- [ ] Separate Business Logic into Services

Structure:

apps/
 |
 services.py
 |
 api.py
 |
 models.py


Apply to:

- Cart
- Order
- Payment
- Wallet


---

# 13. Production Preparation

To Do:

- [ ] Environment variables

- [ ] Security settings

- [ ] Docker setup

- [ ] Logging

- [ ] Backup strategy

- [ ] Deployment


---

# Current Development Status

Completed:

[x] User Model

[x] UserAddress Model

[x] Meal Model

[x] Order Model

[x] Payment Model

[x] Wallet Model

[x] Cart Model

[x] DRF Setup

[x] Cart GET API

[x] Cart Add API

[x] Cart Update API

[x] Cart Remove API


Current Step:

➡ Checkout API

Cart → Order → Payment



# 14. Authentication

To Do: هنگام ثبت نام کاربر wallet به صورت خودکار ساخته شود


# 15. Payment Module -------------- مهم --------------------- درگاه مانده است
### Completed ✅
- [x] Payment model created
- [x] Wallet model created
- [x] WalletTransaction model created
- [x] Wallet payment service implemented
- [x] Online payment service skeleton created
- [x] Mixed payment logic implemented
- [x] Payment API connected to wallet payment service
- [x] Successful wallet payment tested
### Pending ⏳
- [ ] Online payment gateway integration
- [ ] Gateway callback API
- [ ] Payment verification
- [ ] Failed payment handling
- [ ] Payment refund process
- [ ] Payment history API


## 16. Order Module
### Completed ✅
- [x] Order model created
- [x] OrderItem model created
- [x] Create order from cart
- [x] Checkout API implemented
- [x] Order payment connection
### In Progress 🚧
- [ ] Order status flow
- [ ] Order status transition rules
### Pending ⏳
- [ ] Customer order history API
- [ ] Order detail API
- [ ] Cancel order logic


## 17. Addd nutration_base_unit to Ingredient
