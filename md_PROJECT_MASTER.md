GINKOVA PROJECT MASTER DOCUMENT

Last Update: 2026-07-30

---

1. Project Overview

Project Name

GINKOVA

Type

AI-Powered Health Nutrition Ecosystem

Main Goal

GINKOVA is a smart nutrition platform designed to connect:

- Healthy Food
- Artificial Intelligence
- Personalized Nutrition
- Restaurants
- Users' Health Goals
- Diseases
- Nutrition Data

The platform helps users select suitable meals based on:

- Health goals
- Diseases
- Personal health profile
- Nutrition requirements
- Recommendation rules

---

2. Technology Stack

Backend

Framework:

- Django 5.2
- Django REST Framework

Language:

- Python

Database:

- PostgreSQL

Development:

- VS Code
- Virtual Environment

Deployment:

- Render

---

Frontend

Framework:

- React
- TypeScript
- Vite

Libraries:

- Axios
- React Router (planned)
- Context API (planned)

Deployment:

- Render

---

Infrastructure

Source Control:

- GitHub

Domains:

Frontend:

https://ginkova.com

Backend API:

https://api.ginkova.com

---

3. System Architecture

User

 |

React Frontend

https://ginkova.com

 |

Axios API Requests

 |

Django REST API

https://api.ginkova.com

 |

PostgreSQL Database

---

4. Backend Architecture

Django project contains the following applications:

common
accounts
users
health
nutrition
ingradients
recipes
meals
restaurants
partners
cart
orders
wallet
payments
recommandiation
notifications
dashboard
core

Note:

Some app names contain spelling mistakes:

- ingradients
- recommandiation

These names are kept to avoid migration and refactoring problems.

---

5. Backend Modules Status

Accounts

Status:

Completed

Responsibilities:

- User management
- Custom User Model
- Authentication base
- User addresses

Models:

- User
- UserAddress

---

Health Module

Status:

Completed

Responsibilities:

User health information.

Models:

- HealthGoal
- Disease
- HealthProfile

Examples:

Health Goals:

- Weight Loss
- Diabetes Control
- Hypertension Control

---

Nutrition Module

Status:

Mostly Completed

Features:

- Nutrition calculation
- Recipe nutrition
- Meal nutrition

Completed:

- Unit model
- RecipeIngredient connection
- Nutrition calculation

Future:

- Volume conversion
- Ingredient density
- Daily nutrition tracking

---

Meals Module

Status:

Completed

Responsibilities:

Main food definition.

Model:

Meal

Contains:

- Name
- Description
- Categories
- Recipes
- Active status

---

Restaurants Module

Status:

Completed

Architecture:

One meal can belong to multiple restaurants.

Models:

Restaurant

RestaurantMeal

RestaurantMeal contains:

- Price
- Availability
- Preparation time

---

6. Cart Module

Status:

Completed MVP

Models:

- Cart
- CartItem

Rules:

- One user has one cart
- One cart supports one restaurant

Implemented APIs:

GET /api/cart/

POST /api/cart/add/

POST /api/cart/remove/

PUT /api/cart/update/

Future Improvements:

- Change Remove API from POST to DELETE
- Improve error handling
- Move business logic to services.py
- Cart expiration management

---

7. Order Module

Status:

Mostly Completed

Models:

- Order
- OrderItem

Completed:

- Create order from cart
- Checkout API
- Payment connection

Order Flow:

Cart

↓

Checkout

↓

Order

↓

Payment

↓

Confirmation

Order Status:

pending_payment

paid

confirmed

preparing

ready

picked_up

out_for_delivery

delivered

cancelled

Pending:

- Order history API
- Order detail API
- Cancel order logic
- Status transition rules

---

8. Payment Module

Status:

Partially Completed

Completed:

- Payment model
- Wallet payment
- Online payment skeleton
- Payment API
- Wallet transaction logic

Pending:

- Payment gateway integration
- Callback API
- Verification
- Failed payment handling
- Refund process
- Payment history API

Payment Methods:

Supported:

- Wallet
- Online Gateway

Future:

- Bank Transfer

---

9. Wallet Module

Status:

Completed MVP

Models:

- Wallet
- WalletTransaction

Completed:

- Wallet payment logic

Pending:

- Wallet charge API
- Wallet history API
- Refund support

---

10. Recommendation Engine

Status:

MVP Completed

App:

recommendation

Purpose:

Personalized meal recommendation.

Logic:

Score based:

Health Goal Match:
+50

Disease Match:
+50

Nutrition Rules:

Configurable

API:

GET /api/recommendations/

Future:

- AI recommendation
- Machine Learning model

---

11. Authentication Status

Current:

Base user system completed.

Pending:

- JWT Authentication
- Login API
- Logout API
- Register API
- Password reset
- Permissions

Important:

After user registration:

Automatically create Wallet.

---

12. Backend Configuration

Current Database:

PostgreSQL

Environment Variables:

Used:

- SECRET_KEY
- DEBUG
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT

CORS:

Configured:

https://ginkova.com

https://www.ginkova.com

http://localhost:5173

---

13. Frontend Architecture

Project:

ginkova-frontend

Structure:

src/

components/

config/

context/

hooks/

pages/

services/

styles/

types/

utils/

---

14. Frontend Components

Current:

components

common
    Button
    Loading

health
    HealthGoalCard
    HealthGoalList

home
    HeroSection
    MealCategoryCard
    MealCategoryList

layout
    Navbar
    Footer
    Layout

meals
    MealCard
    MealList
    FeatureMeals

---

15. Frontend Pages

Current:

Home.tsx

Login.tsx

Register.tsx

Meals.tsx

Orders.tsx

Profile.tsx

---

16. Frontend Services

Current:

services/

authService.ts

healthGoalService.ts

mealCategoryService.ts

mealService.ts

Important Architecture Rule:

Components must not call API directly.

Correct flow:

Component

↓

Service

↓

Axios

↓

Django API

---

17. API Communication

Current:

Axios based communication.

Config:

src/config/api.ts

Production:

VITE_API_BASE_URL=https://api.ginkova.com

Local:

VITE_API_BASE_URL=http://127.0.0.1:8000

---

18. Deployment Status

Frontend

Status:

Completed

Platform:

Render Static Site

Domain:

https://ginkova.com

Backend

Status:

Completed

Platform:

Render Web Service

Domain:

https://api.ginkova.com

---

19. Current Development Priority

Current Phase:

React Integration

Next Steps:

1. Verify API contracts
2. Update React services according to Django serializers
3. Connect Health Goals
4. Connect Meals
5. Connect Categories
6. Build Cart UI
7. Build Checkout Flow
8. Authentication Integration

---

20. Development Rules

1. No API call directly inside components.

2. All API calls must exist in services folder.

3. All API URLs must come from environment variables.

4. All data models must have TypeScript types.

5. Major architectural changes must be recorded in Change Log.

---

21. Change Log

2026-07-30

Completed:

- React frontend deployed on Render.
- Django backend deployed on Render.
- Custom domains configured.
- SSL certificates issued.
- Frontend connected to backend domain.
- CORS configured.
- Project architecture reviewed.

Current Focus:

React API Integration.

---

END OF DOCUMENT