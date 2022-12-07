# Django
<!-- your app is Django ? no- its Lux house ! rename this banner above -->


## General info
<!-- links to front end repo , acknowledge that i'm reading the backend docs here  -->
For this project we used React as frontend(client side) and Django as backend(API).  


<!-- user stories go in front end -->
## About
<!-- spelling : restaurant  -->
   The Lux-House app is a website of a resataurant with its specialties of coffee and tea. 
   The goal is to create that app with great design and the necessary functionality. 
   Users will be able to sign up, log in and log out. When users are signed in, they could add items to cart, and leave the comment reviews.

## Team
<!-- Sean is not the git manager, Salam is since he is the owner of the repo  -->
- Sean Pham (Full Stack Developer, Git Manager)
- Abdusalam Abdusalamov (Full Stack Developer, Git Manager)

## Technologies Used
- [Django](https://www.djangoproject.com/)
    - Django makes it easier to build better web
    - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design
- [Python](https://www.python.org/)
    - Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages
    - Python is a high-level, general-purpose programming language
- [PostgreSQL]()
    - PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance

# ERD 

![_ERD_](https://user-images.githubusercontent.com/111256827/203136165-74b76e9f-b32a-4ac0-9e28-969e369ae354.png)


## API 
### Authentication

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-up`             | `users#signup`    |
| POST   | `/sign-in`             | `users#signin`    |
| PATCH  | `/change-password/` | `users#changepw`  |
| DELETE | `/sign-out/`        | `users#signout`   |


### Cart

| Verb   | URI Pattern     | Controller#Action  |
|--------|-----------------|--------------------|
| GET    | `/cart`         | `cart#index`       |
| GET    | `/cart/:itemId` | `cart#show`        |
| POST   | `/cart`         | `cart#create`      |
| PATCH  | `/cart/:cartId` | `cart#update`      |
| DELETE | `/cart/:cartId` | `cart#delete`      |
| GET    | `/cart/status`  | `cart#checkstatus` |

### Product

| Verb   | URI Pattern   | Controller#Action |
|--------|---------------|-------------------|
| GET    | `/items`      | `items#index`     |
| GET    | `/items/mine` | `items#userIndex` |
| GET    | `/items/:id`  | `items#show`      |
| POST   | `/items`      | `items#create`    |
| PATCH  | `/items/:id`  | `item#update`     |
| DELETE | `/items/:id`  | `items#delete`    |

<!-- whats V2 look like ? whats the next step in development? -->
<!-- consider a retrospective section here discussing what you've learned  -->