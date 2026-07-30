GINKOVA TODO DOCUMENT

Last Update: 2026-07-30

---

Current Development Phase

Phase: React Frontend Integration

Main Goal:

Connect React frontend with Django REST Backend and complete MVP user flow.

Current Priority:

1. API verification
2. React service update
3. UI development
4. Authentication
5. Shopping flow

---

1. Backend API Improvements

API Response Standardization

Status: Pending

Implement standard response format:

{
    "success": true,
    "message": "",
    "data": {}
}

Apply to:

- Cart API
- Meal API
- Order API
- Payment API
- Wallet API

---

Error Handling

Status: Pending

Tasks:

- Standard API error messages
- Validation errors
- Permission errors
- Exception handling

---

2. Authentication

Status: Pending

Implement:

- JWT Authentication
- Login API
- Logout API
- Register API
- Password Reset API
- Permission Management

Important:

After registration:

Automatically create user wallet.

---

3. User Address Module

Status: Pending

Create APIs:

- Add Address
- List Addresses
- Update Address
- Delete Address (Soft Delete)
- Select Default Address

Rules:

- First address becomes default.
- Addresses used in orders cannot be physically deleted.

---

4. Cart Module Improvements

Current:

Completed MVP

Pending:

- Change Remove API:

Current:

POST

Target:

DELETE

- Review Update API:

Target:

PUT/PATCH

- Move business logic:

Current:

API View

Target:

Service Layer

Architecture:

API

|

services.py

|

Models

- Cart expiration management

- Prevent checkout with empty cart

---

5. Checkout and Order

Current:

Mostly Completed

Pending:

Order APIs

Create:

- Order History API
- Order Detail API
- Cancel Order API

Order Status Management

Implement rules:

Example:

pending_payment

↓

paid

↓

confirmed

↓

preparing

↓

ready

↓

delivering

↓

completed

Prevent invalid status changes.

---

6. Payment Module

Priority: HIGH

Completed:

✓ Payment Model

✓ Wallet Payment

✓ Online Payment Skeleton

Pending:

- Payment Gateway Integration
- Gateway Callback API
- Payment Verification
- Failed Payment Handling
- Refund Process
- Payment History API

---

7. Wallet Module

Completed:

✓ Wallet Model

✓ WalletTransaction Model

Pending:

- Wallet Charge API
- Wallet History API
- Refund Support

---

8. Nutrition System

Completed:

✓ Nutrition calculation

✓ Recipe nutrition

✓ Meal nutrition

Pending:

- Nutrition data per serving
- Ingredient density conversion
- Volume conversion
- Daily nutrition tracking

---

9. Recommendation Engine

Current:

MVP Completed

Pending:

- Improve scoring algorithm
- Add AI recommendation
- Add machine learning model
- User behavior analysis

---

10. React Frontend

Priority: CURRENT

API Integration

Pending:

- Update Axios configuration
- Verify API URLs
- Update services according to serializers

Services:

Need:

authService

healthService

mealService

cartService

orderService

paymentService

walletService

recommendationService

---

Frontend Pages

Pending:

Home:

Improve

Health:

- Health Profile
- Health Goals

Meals:

- Meal List
- Meal Detail

Cart:

- Cart Page

Checkout:

- Checkout Page

Orders:

- Order History
- Order Detail

User:

- Profile
- Address Management

Wallet:

- Wallet Page

---

11. React State Management

Pending:

Implement:

- AuthContext
- CartContext
- HealthContext

---

12. TypeScript Types

Pending:

Complete:

types/

User.ts

Restaurant.ts

Meal.ts

Recipe.ts

Ingredient.ts

Cart.ts

Order.ts

Payment.ts

Wallet.ts

---

13. UI / UX

Pending:

- Responsive design
- Loading states
- Error messages
- Empty states
- Form validation

---

14. Documentation

Pending:

API Documentation

Implement:

- Swagger / OpenAPI

Postman Collection

Create:

- Authentication APIs
- Meal APIs
- Cart APIs
- Order APIs
- Payment APIs
- Wallet APIs

---

15. Database

Current:

PostgreSQL

Pending:

- Backup strategy
- Migration testing
- Production optimization

---

16. Production Preparation

Pending:

Security:

- Production security settings
- HTTPS verification
- CSRF configuration

Deployment:

- Docker configuration
- Logging
- Monitoring

---

17. Future Modules

Not Started:

Restaurant Panel

Features:

- Restaurant management
- Meal management
- Orders

---

Courier Panel

Features:

- Delivery management
- Delivery status

---

Admin Dashboard

Features:

- User management
- Restaurant management
- Reports

---

Notification System

Features:

- Email notification
- SMS notification
- Push notification

---

AI Features

Future:

- Personalized nutrition assistant
- AI meal recommendation
- Health prediction
- Smart diet planning

---

18. Mobile Application

Future Phase:

Options:

- React Native
- Flutter

After Web MVP completion.

---

Development History

Changes are recorded in:

PROJECT_MASTER.md

Change Log section.

---

END OF TODO DOCUMENT