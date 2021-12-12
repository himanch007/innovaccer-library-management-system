## Library Management system.

## To run the application:

```
git clone https://github.com/himanch007/innovaccer-library-management-system.git
python app.py
```

## Screenshots
![Screenshot from 2021-12-12 19-23-50](https://user-images.githubusercontent.com/92020620/145715401-b60ba66e-360a-498c-9c1b-0bb70b2c5530.png)
![Screenshot from 2021-12-12 19-24-10](https://user-images.githubusercontent.com/92020620/145715419-9a0080fe-9ac9-472a-a5c9-6c9b86e59452.png)
![Screenshot from 2021-12-12 19-24-22](https://user-images.githubusercontent.com/92020620/145715417-664ba21c-c4be-452c-abc6-916412c7cf9d.png)
![Screenshot from 2021-12-12 19-26-59](https://user-images.githubusercontent.com/92020620/145715413-88f2c813-ad55-4da6-a754-0ee1d99482e8.png)
![Screenshot from 2021-12-12 19-24-39](https://user-images.githubusercontent.com/92020620/145715416-ed1d6e3b-fd6e-46fd-b013-79ba12e88e19.png)
![Screenshot from 2021-12-12 19-27-15](https://user-images.githubusercontent.com/92020620/145715410-699255ab-65ab-41da-b752-5c74cb85c39a.png)


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

## Routes 
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

