# GINKOVA
## Project Status

Last Update: 2026-07-16

---

# Completed Modules

## Accounts
- User
- UserAddress
- Authentication

---

## Meals

- Meal
- Categories

---

## Cart

### Models
- Cart
- CartItem

### APIs
- GET /api/cart/
- POST /api/cart/add/
- POST /api/cart/remove/

Status:
✅ Completed

---

## Orders

### Models
- Order
- OrderItem

### Services
- create_order_from_cart()
- update_order_status()

### APIs
- POST /api/checkout/
- POST /api/checkout/status/

Status:
✅ Completed

---

## Wallet

### Models
- Wallet
- WalletTransaction

Status:
✅ Completed

---

## Payments

### Models
- Payment

### Services
- Wallet Payment
- Online Payment (Skeleton)
- Mixed Payment

### APIs
- POST /api/payments/create/

Status:
🟡 Wallet Completed
🟡 Online Pending

---

# Not Started

- Recommendation Engine
- Nutrition Engine
- Health Analysis
- Dashboard
- Restaurant Panel
- Courier Panel
- Admin Dashboard
- Notification System
- AI Recommendation




---

## Recommendation Engine

### Models
- MealRecommendationRule

### Services
- recommend_meals(user)

### API

GET /api/recommendations/

### Features

- Recommendation based on Health Goals
- Recommendation based on Diseases
- Meal scoring system

Status:
✅ MVP Completed


## Nutrition System
Completed:
- Unit model created
- RecipeIngredient connected to Unit
- Recipe nutrition calculation implemented
- Meal nutrition calculation implemented
- Nutrition API created

TODO:
- Support volume conversion using ingredient density
- Add nutrition data per serving
- Add nutrition fields to Meal API
- Add daily nutrition tracking


--------------------------------------------------
07/24/2026
--------------------------------------------------
GINKOVA Project Context

Project Overview

Project Name: GINKOVA

Type:
AI-powered Health Nutrition Ecosystem

Main Goal:

Create a smart nutrition platform that connects:

- Healthy Food
- Artificial Intelligence
- Personalized Health Recommendations
- Restaurants
- Users' health goals and diseases

The system helps users choose suitable meals based on:

- Health goals
- Diseases
- Nutrition requirements
- Personal profile

---

Part 1 - Backend

Technology Stack

Framework:

- Django
- Django REST Framework (DRF)

Database:

- PostgreSQL

Development Environment:

- Python
- VS Code
- Docker (planned for deployment)

---

Backend Architecture

The backend is organized as Django applications.

Current apps:

accounts
health
ingredients
recipes
meals
restaurants
cart
orders
payments
wallet
recommendation
notifications
common

---

Backend Modules Status

Accounts

Responsibilities:

- User management
- Authentication
- User addresses

Important models:

- User
- UserAddress

---

Health

Responsibilities:

Stores user health information.

Models:

HealthGoal

Examples:

- Weight Loss
- Diabetes Control
- Hypertension

Disease

Examples:

- Diabetes
- Fatty Liver
- High Blood Pressure

HealthProfile

Connected to User.

Contains:

- Height
- Weight
- Birth date
- Diseases
- Health goals

---

Meals

Responsibilities:

Main food definition.

Models:

Meal

Contains:

- Name
- Description
- Meal type
- Recipes
- Categories
- Active status

Meal is independent from restaurants.

---

Restaurants

Responsibilities:

Restaurant-specific meals and pricing.

Models:

Restaurant

Restaurant information.

RestaurantMeal

Connection between:

Restaurant + Meal

Contains:

- Price
- Availability
- Preparation time

Reason:

One meal can be provided by multiple restaurants with different prices.

---

Recommendation Engine

App:

recommendation

Purpose:

Suggest meals according to user profile.

Current logic:

Score calculation:

Health Goal Match     +50
Disease Match         +50
Nutrition Rules       configurable score

Models:

MealRecommendationRule

Connects:

Meal

with:

- HealthGoal
- Disease
- Score

NutritionRule

Defines nutrition constraints:

Examples:

- Maximum calories
- Minimum protein
- Maximum fat

---

Cart Module

Purpose:

Temporary shopping basket.

Rules:

- Each user has one cart.
- One cart supports only one restaurant.

Reason:

MVP simplification.

Models:

Cart

OneToOne with User

CartItem

Contains:

- RestaurantMeal
- Quantity
- Price
- Consumed By

Consumed By:

- Self
- Someone else

---

Order Module

Purpose:

Convert cart into final order.

Models:

Order

Contains:

- User
- Restaurant
- Status
- Total price
- Delivery address

Order Status Flow:

pending_payment

paid

confirmed

preparing

ready

picked_up

out_for_delivery

delivered

cancelled

OrderItem

Stores purchased items.

Important:

Price is copied from CartItem.

Reason:

Historical price preservation.

---

Payment Module

Payment Strategy Decision

Payment is NOT combined.

Supported methods:

1. Online Payment
2. Wallet Payment

No mixed payment.

Example:

Not supported:

Wallet 5000
Online 3000
Total 8000

Supported:

Online 8000

or

Wallet 8000

---

Wallet Payment Flow

User selects Wallet.

System checks balance.

If:

Wallet balance >= Order amount

Then:

Pay Order
Update Wallet
Create WalletTransaction
Change Order status to paid

If:

Wallet balance < Order amount

Flow:

User -> Wallet Charge

Bank Gateway

Wallet Balance Increased

Pay Order From Wallet

---

Notifications

Purpose:

Send notifications for events.

Examples:

- Order confirmed
- Order preparing
- Order ready
- Delivery started
- Payment successful

---

Backend API Status

Implemented:

- Cart APIs
- Order APIs
- Payment APIs
- Wallet APIs
- Recommendation API

Pending:

- Final API documentation
- Authentication API refinement
- Frontend integration APIs

---

Part 2 - Frontend (React)

Technology Stack

Framework:

React

Planned:

- React Router
- Axios
- Context API
- TypeScript (recommended)

---

Frontend Project Structure

Project:

ginkova-frontend

Main structure:

src/

components/

    common/
    health/
    home/
    layout/
    meals/


config/

context/

hooks/

pages/

services/

styles/

types/

utils/

---

Frontend Architecture

Components

Reusable UI components.

Examples:

- Header
- Footer
- Meal Card
- Restaurant Card
- Health Goal Card

---

Pages

Main application pages.

Planned pages:

Home

Login

Register

Health Profile

Health Goals

Meal List

Meal Detail

Cart

Checkout

Orders

Order Detail

Wallet

Profile

---

Services Layer

Purpose:

Central place for API communication.

Example:

services/

authService.js

mealService.js

cartService.js

orderService.js

paymentService.js

walletService.js

Axios configuration will be centralized.

---

Context

For global states.

Examples:

AuthContext

CartContext

HealthContext

---

Types

For shared data structures.

Examples:

User

Meal

Restaurant

CartItem

Order

Payment

---

Current Frontend Status

Completed:

✓ React project created

✓ Folder structure created

Pending:

- Create API service layer
- Connect Django APIs
- Create authentication flow
- Create layout
- Create pages
- Implement UI

---

Next Development Steps

Phase 1

Connect React to Backend:

- Axios setup
- API configuration
- Authentication

Phase 2

Create Main UI:

- Home page
- Health goals
- Meal browsing

Phase 3

Shopping Flow:

- Meal selection
- Cart
- Checkout

Phase 4

Payment:

- Online payment
- Wallet payment

Phase 5

AI Recommendation:

- Personalized meals
- Health insights

---

Important Architecture Decisions

1. Backend:
   Django REST Framework

2. Frontend:
   React

3. Database:
   PostgreSQL

4. Cart:
   One restaurant per cart

5. Payment:
   Online OR Wallet

6. Recommendation:
   Rule-based engine first, AI enhancement later

7. Mobile App:
   Future phase after Web MVP

---

Document Maintenance

Every major architectural decision should be added to this document.

Format:

Decision:

Reason:

Date:

Impact:

-----------------------------------------------------
mm/dd/2026
-----------------------------------------------------