# GINKOVA TODO DOCUMENT

Last Update: 2026-08-02

---

## Current Development Phase

Phase:

Backend Content Translation Continuation

Main Goal:

Complete multilingual database content for HealthGoal, Disease and later Restaurant while preserving the completed four-language React foundation.

Current Priority:

1. HealthGoal and Disease translation models
2. Health translation migrations and admin
3. Health localized serializers and API testing
4. Restaurant translation architecture
5. Deploy finalized multilingual frontend changes
6. Authentication
7. Shopping flow

---

## 1. Completed React API Integration

Status:

Completed for Meal MVP

Completed:

* Axios configuration updated
* API base URL moved to environment variables
* `/api` prefix standardized
* Request timeout added
* Forced global JSON Content-Type removed
* Meal category service updated
* Meal service updated
* TypeScript response generics added
* Query parameters handled through Axios params
* Meal category API connected
* Meals by category connected
* Nutrition data connected
* Loading states added
* Error states added
* Empty states added
* Shared Axios `Accept-Language` interceptor added
* API data refetched after language changes

Verified APIs:

```text
GET /api/meals/
GET /api/meals/?category=<category_id>
GET /api/meals/<meal_id>/
GET /api/meals/categories/
```

---

## 2. Image System

### Static React Images

Status:

Completed MVP

Completed:

* Hero image
* Meal placeholder
* Meal category placeholder
* Responsive image display
* Shared AppImage component
* Lazy loading
* Async decoding
* Broken image fallback
* Vite image bundling

---

### Dynamic Meal Images

Status:

Completed MVP

Completed:

* Meal ImageField
* Django Admin image upload
* Serializer image response
* Full media URL generation
* Local media storage
* Cloudflare R2 production storage
* django-storages S3 integration
* Environment-based storage selection
* Dynamic React image display
* Production image verification

Local:

```env
USE_R2=False
```

Production:

```env
USE_R2=True
```

Current Production Media Domain:

```text
pub-xxxxxxxx.r2.dev
```

Deferred:

```text
media.ginkova.com
```

Reason:

* DNS remains managed by Namecheap.
* Moving DNS to Cloudflare is not currently planned.
* The custom media domain is not required for MVP.

Pending Image Improvements:

* Validate JPEG
* Validate PNG
* Validate WebP
* Limit upload file size
* Validate MIME type
* Validate image dimensions
* Generate safe file names
* Delete replaced image
* Remove unused files
* Generate thumbnails
* Optional WebP or AVIF conversion
* Upload permissions
* Image ownership rules

---

## 3. Multilingual React Frontend

Priority:

COMPLETED FOR CURRENT HOME AND MEALS MVP

Status:

Completed Base

Target Languages:

```text
en — English
fa — Persian
hy — Armenian
ru — Russian
```

Completed:

* Selected i18next and react-i18next
* Installed i18n dependencies
* Created i18n configuration
* Created language helper module
* Created four locale files
* Added language switcher
* Saved selected language in localStorage
* Restored saved language on startup
* Defined English fallback
* Updated document language dynamically
* Updated document direction dynamically
* Added Persian RTL support
* Added English, Armenian and Russian LTR support
* Removed hardcoded UI text from current Home and Meals MVP components
* Added `Accept-Language` to Axios requests
* Refetched API data after language changes
* Verified language persistence after refresh
* Verified successful production build

Current Structure:

```text
src/
    i18n/
        index.ts
        language.ts
        locales/
            en.ts
            fa.ts
            hy.ts
            ru.ts
```

Completed UI Translation:

* Navbar
* Footer
* Hero section
* Home meal category heading and description
* Meal category cards
* Meals page heading and description
* Meal cards
* Nutrition labels
* Loading states
* Error states
* Empty states
* Category not found

Pending Frontend Translation:

* Login page
* Register page
* Profile page
* Orders page
* Health components
* Future cart page
* Future checkout page
* Future restaurant pages
* Global validation messages
* Toast notifications

---

## 4. RTL and LTR Support

Status:

Completed Base — Visual Review Ongoing

Rules:

Persian:

```text
dir="rtl"
```

English:

```text
dir="ltr"
```

Armenian:

```text
dir="ltr"
```

Russian:

```text
dir="ltr"
```

Completed:

* Update `<html lang="">`
* Update `<html dir="">`
* Persist direction across refresh
* Test Navbar language switching
* Test Footer direction
* Test Home and Meals direction
* Test current card layouts

Pending Visual Review:

* Use logical CSS properties consistently
* Test forms
* Test buttons on all future pages
* Test responsive mobile navigation
* Test mixed numeric and text content
* Armenian font review
* Russian font review
* Persian production font selection

Replace where possible:

```text
margin-left
margin-right
padding-left
padding-right
text-align: left
text-align: right
```

With:

```text
margin-inline-start
margin-inline-end
padding-inline-start
padding-inline-end
text-align: start
text-align: end
```

---

## 5. Backend Multilingual Foundation

Status:

Completed

Completed:

* Configured `LANGUAGE_CODE = en`
* Added English, Persian, Armenian and Russian to Django `LANGUAGES`
* Enabled LocaleMiddleware
* Added backend language normalization
* Added default language helper
* Added language direction helper
* Added request language resolution
* Added shared `LocalizedFieldsMixin`
* Added translation lookup caching during serialization
* Defined English fallback
* Defined original model field as final fallback

Fallback Order:

```text
Requested translation
↓
English translation
↓
Original model field
```

Important Decision:

Frontend UI translations and backend database translations remain separate layers.

---

## 6. Backend Content Translation

Status:

Partially Completed

### Completed Entities

#### MealCategory

Completed:

* `MealCategoryTranslation` model
* Unique constraint by category and language
* English data migration
* Django Admin inline
* Localized serializer
* Translation prefetching
* Four-language fallback testing

#### Meal

Completed:

* `MealTranslation` model
* Unique constraint by meal and language
* English data migration
* Django Admin inline
* Localized list and detail serializer behavior
* Translation prefetching
* Four-language fallback testing

#### Ingredient

Completed:

* `IngredientTranslation` model
* Unique constraint by ingredient and language
* English data migration
* Django Admin inline
* Localized nested serializer
* Fallback testing

#### Recipe

Completed:

* `RecipeTranslation` model
* Unique constraint by recipe and language
* English data migration
* Django Admin inline
* Localized nested serializer
* Fallback testing

### Current Task: HealthGoal and Disease

Status:

NEXT

Tasks:

* Inspect current health models and relations
* Add `HealthGoalTranslation`
* Add `DiseaseTranslation`
* Keep original `name` and `description` fields
* Preserve HealthProfile relationships
* Create schema migration
* Test schema migration locally
* Create English translation data migration
* Add HealthGoal translation inline in Django Admin
* Add Disease translation inline in Django Admin
* Localize HealthGoal serializer
* Localize Disease serializer if an API exists
* Prefetch translations in health API querysets
* Test `Accept-Language: en`
* Test `Accept-Language: fa`
* Test `Accept-Language: hy`
* Test `Accept-Language: ru`
* Test fallback to English
* Test fallback to original fields
* Deploy health migrations after local success

### Next Entity: Restaurant

Status:

Pending

Tasks:

* Inspect Restaurant model
* Decide translated fields
* Add translation model where required
* Add data migration
* Add admin inline
* Localize API serializers
* Test all four languages

### Later Translation Entities

* Notification templates
* Recommendation reasons
* Other future database content

---

## 7. Backend API Improvements

### API Response Standardization

Status:

Pending

Target Format:

```json
{
    "success": true,
    "message": "",
    "data": {}
}
```

Apply to:

* Cart API
* Meal API
* Order API
* Payment API
* Wallet API
* Recommendation API

Important:

Frontend services must be updated at the same time the API response format changes.

---

### Error Handling

Status:

Partially Completed

Completed:

* React Meal loading state
* React Meal error state
* React Meal empty state
* React Category loading state
* React Category error state
* React Category empty state
* Meal not found response
* Four-language loading, error and empty UI messages

Pending:

* Standard API error messages
* Validation errors
* Permission errors
* Global exception handling
* Error codes
* Frontend error normalization
* Backend-localized error strategy review

---

## 8. Authentication

Status:

Pending

Implement:

* JWT Authentication
* Login API
* Logout API
* Register API
* Refresh Token API
* Password Reset API
* Permission Management
* AuthContext
* Protected Routes
* Axios authentication interceptor
* Translate authentication pages in all four languages

Important:

After registration:

* Automatically create user wallet.

---

## 9. User Address Module

Status:

Pending

Create APIs:

* Add Address
* List Addresses
* Update Address
* Delete Address with Soft Delete
* Select Default Address

Rules:

* First address becomes default.
* Addresses used in orders cannot be physically deleted.

Frontend:

* Address list
* Add address form
* Edit address form
* Default address selection
* Checkout address selector
* Four-language labels and validation messages

---

## 10. Cart Module Improvements

Current:

Completed MVP

Pending:

* Change Remove API from POST to DELETE
* Review Update API
* Add PATCH support
* Move business logic to services.py
* Cart expiration management
* Prevent checkout with empty cart
* Add cartService.ts
* Add Cart TypeScript types
* Build Cart page
* Add CartContext
* Add cart count to Navbar
* Translate Cart UI

Architecture:

API

↓

services.py

↓

Models

---

## 11. Checkout and Order

Current:

Mostly Completed Backend

Pending APIs:

* Order History API
* Order Detail API
* Cancel Order API

Order Status Management:

```text
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
out_for_delivery
↓
delivered
```

Pending:

* Prevent invalid status changes
* Finalize status naming
* Checkout page
* Order history page
* Order detail page
* Cancel order UI
* Delivery status UI
* Translate order statuses and UI

---

## 12. Payment Module

Priority:

HIGH AFTER AUTHENTICATION AND CART

Completed:

* Payment Model
* Wallet Payment
* Online Payment Skeleton
* Payment API
* Wallet transaction logic

Pending:

* Payment Gateway Integration
* Gateway Callback API
* Payment Verification
* Failed Payment Handling
* Refund Process
* Payment History API
* paymentService.ts
* Payment TypeScript types
* Payment result pages
* Translate payment UI and status messages

---

## 13. Wallet Module

Completed:

* Wallet Model
* WalletTransaction Model
* Wallet payment logic

Pending:

* Wallet Charge API
* Wallet History API
* Refund Support
* walletService.ts
* Wallet page
* Wallet TypeScript types
* Translate wallet UI

---

## 14. Nutrition System

Completed:

* Nutrition calculation
* Recipe nutrition
* Meal nutrition
* Nutrition API response
* Frontend nutrition display
* Nutrition TypeScript interface
* Nutrition labels translated into English, Persian, Armenian and Russian

Current Fields:

* calories
* protein
* carbohydrate
* fat
* fiber
* sugar
* sodium

Pending:

* Nutrition per serving
* Ingredient density conversion
* Accurate volume conversion
* Count-unit ingredient weights
* Daily nutrition tracking
* Null-data protection
* Nutrition value rounding
* Nutrition unit labels

---

## 15. Recommendation Engine

Current:

MVP Completed

Pending:

* Improve scoring algorithm
* Add AI recommendation
* Add machine learning model
* User behavior analysis
* recommendationService.ts
* Recommendation page
* Recommendation explanation UI
* Multilingual recommendation reasons

---

## 16. React State Management

Completed Decision:

* Use the i18n library as the source of truth for the active language.
* Do not duplicate language state in a separate LanguageContext.

Pending:

* AuthContext
* CartContext
* HealthContext

---

## 17. TypeScript Types

Completed Base:

* HealthGoal.ts
* Meal.ts
* MealCategory.ts
* MealNutrition interface
* SupportedLanguage type

Pending:

* User.ts
* Restaurant.ts
* RestaurantMeal.ts
* Recipe.ts
* Ingredient.ts
* Cart.ts
* Order.ts
* Payment.ts
* Wallet.ts
* Address.ts
* Recommendation.ts
* APIResponse.ts
* APIError.ts

Important:

Price must be represented in RestaurantMeal, not the general Meal type.

---

## 18. UI and UX

Completed:

* Responsive Hero
* Responsive meal category cards
* Responsive meal cards
* Loading states for Meals
* Loading states for Categories
* Error states for Meals
* Error states for Categories
* Empty states for Meals
* Empty states for Categories
* Image fallback
* Image lazy loading
* Language switcher
* Four-language current MVP text
* RTL and LTR switching

Pending:

* Complete responsive mobile Navbar
* Mobile navigation
* Form validation
* Toast notifications
* Skeleton loaders
* Accessibility review
* Keyboard navigation review
* Full RTL visual testing
* Armenian font testing
* Russian font testing
* Persian font selection

---

## 19. Documentation

Completed Documentation Updates:

* Recorded R2 storage architecture
* Recorded WhiteNoise static architecture
* Recorded four-language frontend architecture
* Recorded backend translation architecture
* Recorded `Accept-Language` flow
* Recorded translation fallback rules
* Recorded React Router advisory decision

Pending:

API Documentation:

* Swagger
* OpenAPI schema

Postman Collection:

* Authentication APIs
* Meal APIs
* Cart APIs
* Order APIs
* Payment APIs
* Wallet APIs
* Recommendation APIs
* Address APIs
* Multilingual header examples

---

## 20. Database

Current:

* PostgreSQL
* Production migrations operational

Completed:

* Meal image migration applied
* Production database connection verified
* Meal Category data verified
* Meal API data verified
* MealCategory translation schema migration
* Meal translation schema migration
* Ingredient translation schema migration
* Recipe translation schema migration
* English translation data migrations
* Translation uniqueness constraints

Pending:

* HealthGoal and Disease translation migrations
* Restaurant translation migration if required
* Backup strategy
* Migration testing before deployment
* Automated migration deployment process review
* Production indexing
* Query performance review
* Translation table index review

---

## 21. Production Preparation

### Completed

* Frontend HTTPS
* Backend HTTPS
* Custom frontend domain
* Custom API domain
* CORS configuration
* Gunicorn
* Cloudflare R2 media storage
* S3-compatible Django storage
* WhiteNoise
* collectstatic
* Django Admin static files
* Production media image display
* Environment-based storage selection
* Successful multilingual frontend production build locally

---

### Pending Security

* CSRF trusted origins review
* Secure cookie settings
* HSTS
* Proxy SSL header
* JWT security
* Rate limiting
* File upload validation
* Permission review
* Secret rotation process

---

### Pending Deployment

* Deploy final current multilingual frontend changes
* Verify four languages on `ginkova.com`
* Verify `Accept-Language` against production API
* Verify Persian RTL in production
* Verify Armenian and Russian fonts in production
* Docker configuration
* Structured logging
* Error monitoring
* Uptime monitoring
* Billing alert for Cloudflare R2
* Render deployment health checks
* Database backup automation

---

## 22. Dependency and Security Follow-up

### Completed

* Ran `npm audit`
* Ran production dependency audit
* Ran audit dry-run
* Ran regular `npm audit fix`
* Fixed `brace-expansion` advisory
* Verified successful Vite build afterward

### React Router Advisory

Current Note:

* npm reports an RSC-mode CSRF advisory in the installed React Router range.
* GINKOVA does not use unstable RSC APIs.
* The current application uses standard client-side routing.

Decision:

* Do not run `npm audit fix --force`.
* Do not introduce a breaking major downgrade or upgrade automatically.
* Review React Router 8.3+ in a dedicated migration.
* Confirm required Node.js version before migration.
* Retest all routes after any future major upgrade.

---

## 23. Storage Follow-up

Current Decision:

* Keep DNS at Namecheap.
* Do not move DNS to Cloudflare.
* Use the R2 public development domain during MVP.
* Do not require `media.ginkova.com` for current operation.

Future Review:

* Evaluate a custom media domain before large-scale production traffic.
* Evaluate alternative S3-compatible storage if required.
* Keep Django storage abstraction to avoid provider lock-in.

---

## 24. Future Modules

### Restaurant Panel

Status:

Not Started

Features:

* Restaurant management
* Meal management
* Image management
* Orders
* Availability
* Pricing
* Multilingual restaurant content

---

### Courier Panel

Status:

Not Started

Features:

* Delivery management
* Delivery status
* Courier assignment

---

### Admin Dashboard

Status:

Not Started

Features:

* User management
* Restaurant management
* Reports
* Storage usage
* Order reports
* Nutrition reports
* Translation completeness reporting

---

### Notification System

Status:

Base App Exists

Future Features:

* Email notification
* SMS notification
* Push notification
* Multilingual notification templates

---

### AI Features

Future:

* Personalized nutrition assistant
* AI meal recommendation
* Health prediction
* Smart diet planning
* Multilingual AI assistant

---

## 25. Mobile Application

Future Phase:

Options:

* React Native
* Flutter

Start:

* After Web MVP completion
* After API contracts are stable
* After multilingual backend content is stable

---

## 26. Development History

### 2026-08-02

Completed Backend Multilingual Foundation:

* Django four-language configuration
* LocaleMiddleware
* Shared language helpers
* Shared localized serializer mixin
* MealCategoryTranslation
* MealTranslation
* IngredientTranslation
* RecipeTranslation
* English translation data migrations
* Django Admin translation inlines
* Localized serializers
* Translation queryset prefetching
* Accept-Language testing
* Requested-language, English and original-field fallback

Completed React Multilingual Foundation:

* Installed i18next and react-i18next
* Added `en.ts`, `fa.ts`, `hy.ts` and `ru.ts`
* Added language helper module
* Added LanguageSwitcher
* Added localStorage persistence
* Added dynamic `lang` and `dir`
* Added Persian RTL
* Added English, Armenian and Russian LTR
* Added Axios language interceptor
* Added API refetching on language change
* Translated Navbar, Footer and Hero
* Translated Home and Meals current UI
* Translated loading, error and empty states
* Translated nutrition labels
* Verified local switching and refresh persistence
* Verified production build

Dependency Maintenance:

* Fixed `brace-expansion`
* Recorded React Router RSC advisory
* Deferred React Router major upgrade to a separate task

Next Task:

* HealthGoal and Disease translations

---

### 2026-08-01

Completed:

* Axios configuration update
* Meal and category API verification
* Static React image infrastructure
* AppImage shared component
* Dynamic meal image support
* Cloudflare R2 integration
* S3-compatible Django storage
* Production image verification
* Gunicorn deployment dependency
* Meal image production migration
* WhiteNoise configuration
* collectstatic configuration
* Django Admin static file fix
* Production Meal API verification
* Production Meal Category API verification

---

Changes are also recorded in:

```text
PROJECT_MASTER.md
```

---

END OF TODO DOCUMENT
