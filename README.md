# NEWPROJECT_MO


Djoser is a convenient library for handling authentication in Django Rest Framework. It works with Django's built-in authentication system and provides a set of RESTful API endpoints for registration, authentication, password reset, and other user actions. Here's how to set up Djoser for user authentication, including the login process and the relevant endpoints.



### Djoser Endpoints for Authentication

1. **User Registration**  
   `POST /auth/users/`  
   Endpoint for user registration. Requires user data, like username, email, and password.

2. **User Activation**  
   `POST /auth/users/activation/`  
   Endpoint for user account activation (if `SEND_ACTIVATION_EMAIL` is enabled). Requires activation token.

3. **Token Creation (Login)**  
   `POST /auth/token/login/` (If using Token Authentication)  
   OR  
   `POST /auth/jwt/create/` (If using JWT Authentication)  
   Endpoint for logging in. The user provides credentials and receives an authentication token in response.

4. **Token Deletion (Logout)**  
   `POST /auth/token/logout/` (If using Token Authentication)  
   Endpoint for logging out. It deletes the user's authentication token (if token-based auth is used).

5. **Password Reset**  
   `POST /auth/users/reset_password/`  
   Endpoint for requesting a password reset.

6. **Password Reset Confirmation**  
   `POST /auth/users/reset_password_confirm/`  
   Endpoint for confirming a password reset. Requires the token sent by email.

7. **User Details**  
   `GET /auth/users/me/`  
   Retrieve or update the authenticated user's details.

### Notes:
- Djoser uses token-based authentication by default, but you can configure it to use JSON Web Token (JWT) authentication.
- The actual endpoints might slightly vary based on your project's URL configuration and the version of Djoser.
- Remember to secure your API with appropriate permissions. Djoser works well with Django's permission classes.
- For JWT Authentication, you would need to install additional packages like `djangorestframework-simplejwt`.

This setup provides you with a robust authentication system for your Django Rest Framework project, leveraging Djoser's capabilities.












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




## =======================================================================





---

### API Documentation for Application
the url is ## https://movieproject0001.pythonanywhere.com/api/v1/
#### Models

1. **Category**
   - **Fields**:
     - `name`: String (max length: 200, optional)
     - `image`: Image (optional, stored in `uploads/category/`)
     - `description`: Text (max length: 200, optional)

2. **Books**
   - **Fields**:
     - `title`: String (max length: 20)
     - `author`: String (max length: 20, optional)
     - `cover`: Image (optional, stored in `uploads/books/`)
     - `description`: Text (max length: 200, optional)
     - `audio_link`: URL (max length: 200, optional)
     - `rate`: Positive Integer (default: 1, optional)
     - `cats`: ForeignKey (links to Category)
     - `publish_date`: Date

#### Endpoints

Assuming standard RESTful endpoints with Django Rest Framework:

1. **Categories**
   - List Categories: `GET /categories/`
   - Retrieve Category: `GET /categories/{id}/`
   - Create Category: `POST /categories/`
   - Update Category: `PUT /categories/{id}/`
   - Delete Category: `DELETE /categories/{id}/`

2. **Books**
   - List Books: `GET /books/`
   - Retrieve Book: `GET /books/{id}/`
   - Create Book: `POST /books/`
   - Update Book: `PUT /books/{id}/`
   - Delete Book: `DELETE /books/{id}/`

#### Example Data Structure

- **Category JSON Object**:
  ```json
  {
      "name": "Fiction",
      "image": "url_to_image",
      "description": "Fiction books category"
  }
  ```

- **Books JSON Object**:
  ```json
  {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "cover": "url_to_cover_image",
      "description": "A novel set in the Jazz Age",
      "audio_link": "url_to_audio",
      "rate": 5,
      "cats": 1,  // Category ID
      "publish_date": "2023-01-01"
  }
  ```

#### Authentication & Permissions

- Describe if and how authentication is required to access these endpoints.
- Mention any permission levels or user roles necessary for certain actions.

#### Error Handling

- Provide details on how errors are returned (e.g., status codes, error messages).

#### Pagination

- If applicable, explain how pagination is handled in list endpoints.

#### Filtering & Sorting

- Provide details on any filtering or sorting options available on list endpoints.
