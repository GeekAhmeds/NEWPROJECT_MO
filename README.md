# NEWPROJECT_MO



Djoser Endpoints for Authentication
User Registration
POST /auth/users/
Endpoint for user registration. Requires user data, like username, email, and password.

User Activation
POST /auth/users/activation/
Endpoint for user account activation (if SEND_ACTIVATION_EMAIL is enabled). Requires activation token.

Token Creation (Login)
POST /auth/token/login/ (If using Token Authentication)
OR
POST /auth/jwt/create/ (If using JWT Authentication)
Endpoint for logging in. The user provides credentials and receives an authentication token in response.

Token Deletion (Logout)
POST /auth/token/logout/ (If using Token Authentication)
Endpoint for logging out. It deletes the user's authentication token (if token-based auth is used).

Password Reset
POST /auth/users/reset_password/
Endpoint for requesting a password reset.

Password Reset Confirmation
POST /auth/users/reset_password_confirm/
Endpoint for confirming a password reset. Requires the token sent by email.

User Details
GET /auth/users/me/
Retrieve or update the authenticated user's details.

Notes:
Djoser uses token-based authentication by default, but you can configure it to use JSON Web Token (JWT) authentication.
The actual endpoints might slightly vary based on your project's URL configuration and the version of Djoser.
Remember to secure your API with appropriate permissions. Djoser works well with Django's permission classes.
For JWT Authentication, you would need to install additional packages like djangorestframework-simplejwt.













### Category Endpoints
1. **List all Categories**  
   `GET /categories/`  
   Retrieves a list of all category instances.

2. **Create a New Category**  
   `POST /categories/`  
   Creates a new category instance. You need to provide the required data in the request body.

3. **Retrieve a Specific Category**  
   `GET /categories/{id}/`  
   Retrieves a specific category instance by its id.

4. **Update a Category**  
   `PUT /categories/{id}/`  
   Fully updates a specific category instance. All fields need to be provided in the request body.

5. **Partial Update of a Category**  
   `PATCH /categories/{id}/`  
   Partially updates a specific category instance. Only provide the fields that need to be updated.

6. **Delete a Category**  
   `DELETE /categories/{id}/`  
   Deletes a specific category instance.

### Books Endpoints
1. **List all Books**  
   `GET /books/`  
   Retrieves a list of all book instances.

2. **Create a New Book**  
   `POST /books/`  
   Creates a new book instance. Required data should be provided in the request body.

3. **Retrieve a Specific Book**  
   `GET /books/{id}/`  
   Retrieves a specific book instance by its id.

4. **Update a Book**  
   `PUT /books/{id}/`  
   Fully updates a specific book instance. All fields need to be provided in the request body.

5. **Partial Update of a Book**  
   `PATCH /books/{id}/`  
   Partially updates a specific book instance. Only provide the fields that need to be updated.

6. **Delete a Book**  
   `DELETE /books/{id}/`  
   Deletes a specific book instance.

### Notes:
- `{id}` in the URLs should be replaced with the actual ID of the category or book you are trying to access.
- When creating or updating records, ensure that your request body contains the necessary data formatted as JSON, and the appropriate headers are set (e.g., `Content-Type: application/json`).
- The actual path to these endpoints may vary depending on how you've set up your Django project's root URL configuration. The above paths assume that the app's `urls.py` is directly included in the project's `urls.py`.
