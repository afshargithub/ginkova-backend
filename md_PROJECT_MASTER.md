# GINKOVA PROJECT MASTER DOCUMENT

Last Update: 2026-08-02

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

Internationalization:

* Django LocaleMiddleware
* Accept-Language request handling
* Explicit translation models
* Shared localized serializer logic

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
* i18next
* react-i18next
* Context API planned for authentication and cart

Internationalization:

* English
* Persian
* Armenian
* Russian
* Runtime language switching
* localStorage persistence
* RTL and LTR switching

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

React i18n Layer

↓

Frontend Services

↓

Shared Axios Instance

↓

`Accept-Language` Header

↓

Django REST API

https://api.ginkova.com

↓

LocaleMiddleware and Localized Serializers

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
* Frontend locale TypeScript files

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

### Common Module

Status:

Multilingual Foundation Completed

Implemented:

* Supported language normalization
* Default language definition
* RTL language definition
* Request language resolution
* Language direction helper
* Shared `LocalizedFieldsMixin` for serializers
* Translation lookup caching on serialized objects

Supported Languages:

```text
en — English
fa — Persian
hy — Armenian
ru — Russian
```

Fallback Order:

```text
Requested language
↓
English translation
↓
Original model field
```

---

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

Completed Base — Translation Layer Pending

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

Next Multilingual Task:

* Add `HealthGoalTranslation`
* Add `DiseaseTranslation`
* Preserve existing health profile relationships
* Add English data migration
* Add Django Admin translation inlines
* Localize serializers
* Test all four languages

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
* Multilingual static nutrition labels in React

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
* Nutrition value rounding and unit display

Important:

Count units currently require an ingredient weight definition before accurate nutrition conversion can be completed.

---

### Ingredients Module

Internal App Name:

* ingradients

Status:

Multilingual Backend Completed

Completed:

* `IngredientTranslation` model
* Translation uniqueness by ingredient and language
* English translation data migration
* Django Admin translation inline
* Localized ingredient serializer
* English fallback and original-field fallback
* Nested multilingual ingredient response through recipe and meal detail

---

### Recipes Module

Status:

Multilingual Backend Completed

Completed:

* `RecipeTranslation` model
* Translation uniqueness by recipe and language
* English translation data migration
* Django Admin translation inline
* Localized recipe serializer
* Nested multilingual recipe response through meal detail
* Recipe ingredient relations preserved

---

### Meals Module

Status:

Completed Multilingual MVP

Responsibilities:

* Main meal definition
* Meal categories
* Meal recipes
* Nutrition response
* Active and featured status
* Dynamic meal images
* Localized API content

Models:

* Meal
* MealCategory
* MealTranslation
* MealCategoryTranslation

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
* Query optimization and translation prefetching
* Production migration for Meal image field
* Meal image fallback support in React
* `MealTranslation` model
* `MealCategoryTranslation` model
* English translation data migrations
* Django Admin translation inlines
* `Accept-Language` localized responses
* Requested-language to English fallback
* English to original-field fallback
* Nested multilingual Recipe and Ingredient data
* Local API tests for English, Persian, Armenian and Russian fallback behavior

---

### Restaurants Module

Status:

Completed Base — Translation Layer Pending

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

Pending Multilingual Work:

* Inspect restaurant model fields
* Add restaurant translation model where required
* Localize restaurant serializers and admin

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
* Multilingual recommendation explanations

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

Internationalization Configuration:

```text
LANGUAGE_CODE = en
LANGUAGES = en, fa, hy, ru
LocaleMiddleware enabled
```

The Backend reads `Accept-Language` and normalizes regional values such as `fa-IR` to `fa`.

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
    i18n/
        index.ts
        language.ts
        locales/
            en.ts
            fa.ts
            hy.ts
            ru.ts
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

Language Flow:

LanguageSwitcher

↓

react-i18next

↓

localStorage and document `lang` / `dir`

↓

Axios `Accept-Language`

↓

Localized Django response

---

## 15. Frontend Components

Current Components:

```text
components/
    common/
        AppImage
        Button
        LanguageSwitcher
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

Multilingual Components Completed:

* LanguageSwitcher
* Navbar
* Footer
* HeroSection
* Home meal category section
* MealCategoryCard
* MealCategoryList loading, error and empty states
* Meals page
* MealCard buttons and nutrition labels
* MealList loading, error and empty states

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
* Four-language UI switching for current Home and Meals MVP

Pending:

* Meal detail page
* Cart page
* Checkout page
* Order history page
* Order detail page
* Health profile page
* Address management page
* Wallet page
* Translation of authentication and future pages

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
* Request interceptor for `Accept-Language`
* Automatic use of the language stored in localStorage

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

Language Header Examples:

```http
Accept-Language: en
Accept-Language: fa
Accept-Language: hy
Accept-Language: ru
```

Important:

API paths inside services must not repeat `/api` when the environment base URL already contains `/api`.

---

## 19. Multilingual System Status

### Frontend UI Translation

Status:

Completed for Current Home and Meals MVP

Implemented:

* i18next and react-i18next installed
* Four locale files created
* Runtime language switcher added to Navbar
* Language stored in localStorage
* Saved language restored on startup
* English fallback configured
* HTML `lang` updated dynamically
* HTML `dir` updated dynamically
* Persian uses RTL
* English, Armenian and Russian use LTR
* Navbar translated
* Footer translated
* Hero translated
* Home category section translated
* Meals page translated
* Loading, error and empty states translated
* Meal action buttons translated
* Nutrition labels translated
* API data refetched after language changes

Current Locale Files:

```text
src/i18n/locales/en.ts
src/i18n/locales/fa.ts
src/i18n/locales/hy.ts
src/i18n/locales/ru.ts
```

Pending Frontend Translation:

* Authentication pages
* Profile page
* Orders page
* Health components
* Cart and checkout pages
* Future restaurant pages
* Global form validation and toast messages

---

### Backend Content Translation

Status:

Partially Completed

Completed Entities:

* MealCategory
* Meal
* Recipe
* Ingredient

Pending Entities:

* HealthGoal
* Disease
* Restaurant where required
* Notifications
* Recommendation explanations
* Other future content entities

Architecture Decision:

* Explicit translation models
* Keep original model text fields for compatibility and final fallback
* Translation table has one row per entity and language
* Unique constraint on entity plus language
* English data migration from existing content
* Django Admin inline translation management
* Serializer localization by `Accept-Language`

---

## 20. Image System Status

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

## 21. Deployment Status

### Frontend

Status:

Base Production Deployment Completed

Platform:

* Render Static Site

Domain:

* https://ginkova.com

Build:

```text
npm run build
```

Build Status:

* Verified successfully after installing and configuring i18next
* Current Home and Meals multilingual build verified locally

Next Deployment Task:

* Deploy the four-language frontend changes after final local verification

---

### Backend

Status:

Completed Base Deployment

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
* Translation migrations for MealCategory, Meal, Recipe and Ingredient prepared and tested
* Localized API behavior tested with `Accept-Language`

---

## 22. Current Development Priority

Current Phase:

Backend Content Translation Continuation

Completed in Current Multilingual Phase:

1. Django language configuration
2. LocaleMiddleware
3. Shared backend language helpers
4. MealCategory translation model
5. Meal translation model
6. Recipe translation model
7. Ingredient translation model
8. English data migrations
9. Django Admin translation inlines
10. Localized serializers
11. Translation prefetch optimization
12. Accept-Language API tests
13. i18next and react-i18next installation
14. Four frontend locale files
15. Language switcher
16. localStorage persistence
17. RTL and LTR switching
18. Axios language interceptor
19. Home and Meals UI translation
20. Multilingual local build verification

Next Steps:

1. Add `HealthGoalTranslation`
2. Add `DiseaseTranslation`
3. Populate English health translations
4. Add Health Django Admin translation inlines
5. Localize Health serializers
6. Test Health data in English, Persian, Armenian and Russian
7. Add Restaurant translations where needed
8. Translate remaining frontend pages as each module is activated
9. Deploy finalized frontend multilingual changes

---

## 23. Multilingual Architecture Rules

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

6. The selected language is stored in localStorage under:

```text
ginkova_language
```

7. The HTML `lang` and `dir` attributes update when language changes.

8. CSS should prefer logical properties:

```text
margin-inline-start
margin-inline-end
padding-inline-start
padding-inline-end
text-align: start
```

9. Backend database content and frontend interface text are separate translation layers.

10. API requests send:

```text
Accept-Language
```

11. Fallback language:

```text
English
```

12. Backend fallback order:

```text
Requested translation
English translation
Original model field
```

13. Original model fields must remain until a deliberate future migration removes them.

14. Translation relations should be prefetched to avoid N+1 queries.

15. Existing model relations must not be broken when translation models are added.

---

## 24. Development Rules

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

11. Translation changes must be tested in all four language codes.

12. Database translation migrations must preserve existing data.

---

## 25. Security and Dependency Notes

### React Router Advisory

Current Audit Status:

* npm reports a high-severity advisory affecting React Router RSC mode.
* GINKOVA currently uses standard client-side routing and does not use unstable React Server Components APIs.
* The reported RSC-specific issue is not currently exploitable through the present frontend architecture.

Decision:

* Do not run `npm audit fix --force`.
* Keep the current React Router 7 setup for now.
* Review upgrade to React Router 8.3 or later in a dedicated migration task.
* Verify Node.js compatibility before the major upgrade.

Completed Dependency Maintenance:

* `brace-expansion` vulnerability fixed through regular `npm audit fix`.
* Production frontend build verified after the fix.

---

## 26. Change Log

### 2026-08-02

Completed Backend Multilingual Work:

* Configured four Django languages: English, Persian, Armenian and Russian.
* Enabled LocaleMiddleware.
* Added shared backend language normalization and direction helpers.
* Added shared localized serializer mixin.
* Added MealCategoryTranslation and MealTranslation models.
* Added IngredientTranslation and RecipeTranslation models.
* Added unique translation constraints.
* Created English translation data migrations from existing fields.
* Added Django Admin translation inlines.
* Localized MealCategory, Meal, Recipe and Ingredient serializers.
* Added requested-language, English and original-field fallback behavior.
* Added translation prefetching for list and detail APIs.
* Tested `Accept-Language` for English, Persian, Armenian and Russian fallback behavior.

Completed Frontend Multilingual Work:

* Installed i18next and react-i18next.
* Created language management helpers.
* Added English, Persian, Armenian and Russian locale files.
* Added LanguageSwitcher to Navbar.
* Added localStorage language persistence.
* Added dynamic HTML `lang` and `dir` updates.
* Added RTL support for Persian.
* Added LTR support for English, Armenian and Russian.
* Added `Accept-Language` Axios interceptor.
* Added API refetching after a language change.
* Translated Navbar, Footer and Hero.
* Translated Home category section.
* Translated Meals page and meal cards.
* Translated loading, error and empty states.
* Translated nutrition labels.
* Verified local language switching and persistence.
* Verified successful Vite production build.
* Fixed the `brace-expansion` audit issue.
* Recorded the React Router RSC advisory for later review.

Current Focus:

* HealthGoal and Disease backend translations

---

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
