## Library Management system.

## To run the application:

```
git clone https://github.com/himanch007/innovaccer-library-management-system.git
python app.py
```

## Tech stack:

- Flask
- Postgres
- HTML
- CSS

## Features:

- User login
- Admin login
- User Dashboard
- Admin Dashboard
- Issue Books
- Return Books

## Route 
```
/register
User can register here by using his credentials

/about
User can read about Contributors

/admin-login
Admin can login using his credentials

/user-login
User can login using his credentials

/success-login
After login User redirected to his dashboard

/success-register
User will be successfully registered and redirected to his dashboard

/adminLoginSuccess
After Admin login It will redirected to the page where he/she will add book details

/logout
When User/Admin wants to exit from his profile

/admin_dashboard
Admin will see his dashboard

/book-form-id/<book_id>/<user_id>/<numberofbooks>
User can borrow a specific book by using book id

/issued-books
When Book Issued process is complete

/viewbooks
Admin can view the existing books

/remove-book/<book_id>
Admin can remove an existing book

```

