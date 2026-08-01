# GINKOVA PROJECT MASTER DOCUMENT

Last Update: 2026-08-01

---

## 1. Project Overview

### Project Name

GINKOVA

### Type

AI-Powered Health Nutrition Ecosystem

### Main Goal

GINKOVA is a smart nutrition platform designed to connect:

* Healthy Food
* Artificial Intelligence
* Personalized Nutrition
* Restaurants
* Users' Health Goals
* Diseases
* Nutrition Data

The platform helps users select suitable meals based on:

* Health goals
* Diseases
* Personal health profile
* Nutrition requirements
* Recommendation rules

---

## 2. Technology Stack

### Backend

Framework:

* Django 5.2
* Django REST Framework

Language:

* Python

Database:

* PostgreSQL

Storage:

* Local FileSystemStorage for local development
* Cloudflare R2 for production media files
* S3-compatible storage architecture through django-storages

Static Files:

* Django collectstatic
* WhiteNoise

Development:

* VS Code
* Python Virtual Environment

Deployment:

* Render Web Service
* Gunicorn

---

### Frontend

Framework:

* React 19
* TypeScript
* Vite 8

Libraries:

* Axios
* React Router
* Tailwind CSS 4
* Context API planned

Deployment:

* Render Static Site

---

### Infrastructure

Source Control:

* GitHub

Frontend Domain:

https://ginkova.com

Backend API Domain:

https://api.ginkova.com

Production Media Storage:

* Cloudflare R2
* Bucket: ginkova-media

Current Public Media URL:

* Cloudflare R2 Public Development URL
* `pub-xxxxxxxx.r2.dev`

Planned Media Domain:

* `media.ginkova.com`

Note:

The custom media domain is currently deferred because DNS for `ginkova.com` is managed by Namecheap and is not managed through Cloudflare DNS.

---

## 3. System Architecture

User

↓

React Frontend

https://ginkova.com

↓

Frontend Services

↓

Axios API Requests

↓

Django REST API

https://api.ginkova.com

↓

PostgreSQL Database

and

Cloudflare R2 Media Storage

---

## 4. File Storage Architecture

### Static Frontend Files

Examples:

* Hero image
* Placeholder images
* React JavaScript bundles
* React CSS bundles

Managed by:

* Vite
* Render Static Site

---

### Django Static Files

Examples:

* Django Admin CSS
* Django Admin JavaScript
* Django REST Framework browsable API assets

Managed by:

* Django collectstatic
* WhiteNoise
* Render Backend Service

---

### Dynamic Media Files

Examples:

* Meal images
* Future restaurant images
* Future user avatars
* Future uploaded health documents

Local Development:

* Django media directory
* FileSystemStorage

Production:

* Cloudflare R2
* django-storages S3 backend

Storage Selection:

```env
USE_R2=False
```

Local result:

* Files are stored in the local `media/` directory.

```env
USE_R2=True
```

Production result:

* Files are stored in Cloudflare R2.

Important Architecture Rule:

Models, serializers and React components must not depend directly on Cloudflare-specific APIs.

All uploaded files must use Django's default storage interface so the storage provider can be changed later without rewriting application models or frontend components.

---

## 5. Backend Architecture

Django project contains the following applications:

* common
* accounts
* users
* health
* nutrition
* ingradients
* recipes
* meals
* restaurants
* partners
* cart
* orders
* wallet
* payments
* recommandiation
* notifications
* dashboard
* core

Note:

Some app names contain spelling mistakes:

* ingradients
* recommandiation

These names are kept to avoid migration and refactoring problems.

Public API URLs must use correctly spelled names where possible.

---

## 6. Backend Modules Status

### Accounts

Status:

Completed Base

Responsibilities:

* User management
* Custom User Model
* Authentication base
* User addresses

Models:

* User
* UserAddress

Pending:

* JWT Authentication
* Register API
* Login API
* Logout API
* Password reset
* Permission management

---

### Health Module

Status:

Completed Base

Responsibilities:

* User health information
* Health goals
* Diseases
* Health profile

Models:

* HealthGoal
* Disease
* HealthProfile

Examples:

* Weight Loss
* Diabetes Control
* Hypertension Control

---

### Nutrition Module

Status:

Mostly Completed

Completed:

* Unit model
* RecipeIngredient connection
* Recipe nutrition calculation
* Meal nutrition calculation
* Weight unit conversion

Nutrition fields currently returned:

* calories
* protein
* carbohydrate
* fat
* fiber
* sugar
* sodium

Pending:

* Nutrition data per serving
* Ingredient density
* Accurate volume conversion
* Count-unit ingredient weight
* Daily nutrition tracking
* Safe handling of incomplete ingredient data

Important:

Count units currently require an ingredient weight definition before accurate nutrition conversion can be completed.

---

### Meals Module

Status:

Completed MVP

Responsibilities:

* Main meal definition
* Meal categories
* Meal recipes
* Nutrition response
* Active and featured status
* Dynamic meal images

Models:

* Meal
* MealCategory

Meal contains:

* Name
* Description
* Image
* Meal type
* Recipes
* Categories
* Featured status
* Active status
* Created date
* Updated date

Implemented APIs:

```text
GET /api/meals/
GET /api/meals/?category=<category_id>
GET /api/meals/<meal_id>/
GET /api/meals/categories/
GET /api/meals/categories/<category_name>/
```

Completed Improvements:

* Category filtering
* Serializer request context
* Full media URL generation
* Dynamic image support
* Cloudflare R2 production storage
* Query ordering
* Basic query optimization
* Production migration for Meal image field
* Meal image fallback support in React

---

### Restaurants Module

Status:

Completed Base

Architecture:

One meal can belong to multiple restaurants.

Models:

* Restaurant
* RestaurantMeal

RestaurantMeal contains:

* Price
* Availability
* Preparation time

Important:

Price belongs to RestaurantMeal, not the general Meal model.

---

## 7. Cart Module

Status:

Completed MVP

Models:

* Cart
* CartItem

Rules:

* One user has one cart
* One cart supports one restaurant

Implemented APIs:

```text
GET /api/cart/
POST /api/cart/add/
POST /api/cart/remove/
PUT /api/cart/update/
```

Pending Improvements:

* Change Remove API from POST to DELETE
* Review PUT and PATCH behavior
* Improve error handling
* Move business logic to services.py
* Cart expiration management
* Prevent checkout with empty cart

---

## 8. Order Module

Status:

Mostly Completed

Models:

* Order
* OrderItem

Completed:

* Create order from cart
* Checkout API
* Payment connection

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

Current Order Statuses:

* pending_payment
* paid
* confirmed
* preparing
* ready
* picked_up
* out_for_delivery
* delivered
* cancelled

Pending:

* Order history API
* Order detail API
* Cancel order logic
* Status transition rules
* Unified final naming for delivery and completion statuses

---

## 9. Payment Module

Status:

Partially Completed

Completed:

* Payment model
* Wallet payment
* Online payment skeleton
* Payment API
* Wallet transaction logic

Pending:

* Payment gateway integration
* Gateway callback API
* Payment verification
* Failed payment handling
* Refund process
* Payment history API

Payment Methods:

Supported Base:

* Wallet
* Online Gateway

Future:

* Bank Transfer

---

## 10. Wallet Module

Status:

Completed MVP

Models:

* Wallet
* WalletTransaction

Completed:

* Wallet model
* Wallet transaction model
* Wallet payment logic

Pending:

* Wallet charge API
* Wallet history API
* Refund support

Important:

A wallet must be created automatically after user registration.

---

## 11. Recommendation Engine

Status:

MVP Completed

Internal App Name:

* recommandiation

Public API:

```text
GET /api/recommendations/
```

Purpose:

Personalized meal recommendation.

Current Logic:

Health Goal Match:

```text
+50
```

Disease Match:

```text
+50
```

Nutrition Rules:

* Configurable

Pending:

* Improve scoring algorithm
* User behavior analysis
* AI recommendation
* Machine learning model

---

## 12. Authentication Status

Current:

* Custom user model completed
* Base user structure completed

Pending:

* JWT Authentication
* Login API
* Logout API
* Register API
* Password reset
* Refresh token logic
* Permission management
* Protected frontend routes
* AuthContext

Important:

After user registration:

* Automatically create Wallet.

---

## 13. Backend Configuration

Database:

* PostgreSQL

Environment Variables:

Existing:

* SECRET_KEY
* DEBUG
* DB_NAME
* DB_USER
* DB_PASSWORD
* DB_HOST
* DB_PORT

Media Storage:

* USE_R2
* R2_ACCESS_KEY_ID
* R2_SECRET_ACCESS_KEY
* R2_BUCKET_NAME
* R2_ENDPOINT_URL
* R2_PUBLIC_DOMAIN

Production Media Configuration:

```env
USE_R2=True
R2_BUCKET_NAME=ginkova-media
```

Local Media Configuration:

```env
USE_R2=False
```

CORS Allowed Origins:

* https://ginkova.com
* https://www.ginkova.com
* http://localhost:5173

Static Files:

* STATIC_URL configured
* STATIC_ROOT configured
* collectstatic enabled
* WhiteNoise configured
* Django Admin static assets verified in production

Production Server:

* Gunicorn

---

## 14. Frontend Architecture

Project:

ginkova-frontend

Structure:

```text
src/
    assets/
    components/
    config/
    context/
    hooks/
    pages/
    services/
    styles/
    types/
    utils/
```

Architecture Rule:

Components must not call APIs directly.

Correct flow:

Component

↓

Service

↓

Axios Instance

↓

Django API

---

## 15. Frontend Components

Current Components:

```text
components/
    common/
        AppImage
        Button
        Loading

    health/
        HealthGoalCard
        HealthGoalList

    home/
        HeroSection
        MealCategoryCard
        MealCategoryList

    layout/
        Navbar
        Footer
        Layout

    meals/
        MealCard
        MealList
        FeaturedMeals
```

Image Components Completed:

* Shared AppImage component
* Image error fallback
* Lazy loading
* Async image decoding
* Local static image support
* Backend media URL support
* Placeholder support

---

## 16. Frontend Pages

Current:

* Home.tsx
* Login.tsx
* Register.tsx
* Meals.tsx
* Orders.tsx
* Profile.tsx

Connected:

* Home page
* Meal categories
* Meals by category
* Dynamic meal images
* Nutrition display

Pending:

* Meal detail page
* Cart page
* Checkout page
* Order history page
* Order detail page
* Health profile page
* Address management page
* Wallet page

---

## 17. Frontend Services

Current:

* authService.ts
* healthGoalService.ts
* mealCategoryService.ts
* mealService.ts

Completed Improvements:

* Shared Axios instance
* Environment-based API base URL
* Request timeout
* Removed forced global JSON Content-Type
* TypeScript response typing
* Axios query parameter handling
* Consistent service-based API calls

Pending Services:

* healthService.ts
* cartService.ts
* orderService.ts
* paymentService.ts
* walletService.ts
* recommendationService.ts
* addressService.ts

---

## 18. API Communication

Config File:

```text
src/config/api.ts
```

Production:

```env
VITE_API_BASE_URL=https://api.ginkova.com/api
```

Local:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

Service Example:

```text
/meals/
```

Final Production Request:

```text
https://api.ginkova.com/api/meals/
```

Important:

API paths inside services must not repeat `/api` when the environment base URL already contains `/api`.

---

## 19. Image System Status

### Static Images

Status:

Completed MVP

Implemented:

* Hero image
* Meal placeholder
* Category placeholder
* Responsive image layout
* AppImage shared component
* Image fallback behavior

Static React images are built by Vite and deployed with the React frontend.

---

### Dynamic Meal Images

Status:

Completed MVP

Implemented:

* Django ImageField
* Django Admin upload
* Local media storage
* Production Cloudflare R2 storage
* S3-compatible Django storage
* Full media URLs in API
* Dynamic image display in React
* Placeholder when image is missing
* Placeholder when image URL fails
* Production image display verified

Current Production URL:

* Cloudflare `r2.dev` public URL

Deferred:

* `media.ginkova.com` custom domain

Reason:

* DNS is managed by Namecheap.
* The domain is not currently managed through Cloudflare DNS.
* The custom media subdomain is not required for MVP functionality.

Pending Image Improvements:

* Upload file size validation
* MIME type validation
* File extension validation
* Image dimension validation
* Safe replacement of existing images
* Deleting unused images
* Thumbnail generation
* WebP or AVIF conversion
* User upload permissions

---

## 20. Deployment Status

### Frontend

Status:

Completed

Platform:

* Render Static Site

Domain:

* https://ginkova.com

Build:

```text
npm run build
```

Build Status:

* Verified successfully

---

### Backend

Status:

Completed

Platform:

* Render Web Service

Domain:

* https://api.ginkova.com

Production Components:

* Gunicorn
* PostgreSQL
* WhiteNoise
* Cloudflare R2
* django-storages
* collectstatic

Resolved Deployment Issues:

* Gunicorn dependency added
* Meal migration 0004 applied
* Static files collected
* Django Admin assets served
* Dynamic meal images stored in R2
* Meal and category APIs verified

---

## 21. Current Development Priority

Current Phase:

Multilingual Frontend and Backend Foundation

Target Languages:

* Persian — fa
* English — en
* Armenian — hy
* Russian — ru

Next Steps:

1. Install and configure React i18n library
2. Create language resource structure
3. Implement LanguageContext or i18n configuration
4. Add language switcher
5. Save selected language
6. Implement RTL and LTR switching
7. Translate shared UI components
8. Translate Navbar and Footer
9. Translate Home page
10. Translate Meal list and cards
11. Translate loading, error and empty states
12. Define backend content translation strategy
13. Add Accept-Language support
14. Translate MealCategory data
15. Translate Meal data
16. Translate HealthGoal data

---

## 22. Multilingual Architecture Rules

1. UI text must not be hardcoded inside components.

2. React UI translations must be stored in locale files.

3. Supported language codes:

```text
fa
en
hy
ru
```

4. Persian uses RTL.

5. English, Armenian and Russian use LTR.

6. The selected language must be stored in localStorage.

7. The HTML `lang` and `dir` attributes must update when language changes.

8. CSS must prefer logical properties:

```text
margin-inline-start
margin-inline-end
padding-inline-start
padding-inline-end
text-align: start
```

9. Backend database content and frontend interface text must be treated separately.

10. API requests should eventually send:

```text
Accept-Language
```

11. A fallback language must be defined.

Recommended fallback:

```text
English
```

---

## 23. Development Rules

1. No API calls directly inside components.

2. All API calls must exist in the services folder.

3. All API URLs must come from environment variables.

4. All API data models must have TypeScript types.

5. Uploaded files must use Django Storage.

6. Frontend components must not depend on a specific storage provider.

7. Static frontend images must be managed by Vite.

8. Django Admin static files must be managed by collectstatic and WhiteNoise.

9. Major architectural changes must be recorded in the Change Log.

10. Old code versions must be stored in Git history, not as duplicate files inside `src`.

---

## 24. Change Log

### 2026-08-01

Completed:

* Standardized frontend Axios base URL.
* Updated meal and meal category services.
* Added typed Axios responses.
* Added shared AppImage component.
* Added meal and category placeholders.
* Added Hero static image support.
* Added dynamic meal image display.
* Added backend media URL handling.
* Added Serializer request context.
* Added Cloudflare R2 production storage.
* Added django-storages S3-compatible backend.
* Added environment-based Local and R2 storage selection.
* Added Gunicorn dependency for Render.
* Applied missing Meal image migration in production.
* Added WhiteNoise.
* Configured collectstatic.
* Fixed Django Admin and DRF static asset delivery.
* Verified production Meal API.
* Verified production Meal Category API.
* Verified production image display.
* Confirmed Namecheap remains the DNS provider.
* Deferred custom `media.ginkova.com` domain.
* Completed the MVP image infrastructure phase.

Current Focus:

* Four-language support
* Persian, English, Armenian and Russian
* RTL and LTR support

---

### 2026-07-30

Completed:

* React frontend deployed on Render.
* Django backend deployed on Render.
* Custom domains configured.
* SSL certificates issued.
* Frontend connected to backend domain.
* CORS configured.
* Project architecture reviewed.

---

END OF DOCUMENT
