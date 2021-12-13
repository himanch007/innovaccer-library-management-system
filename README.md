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
![Admin_dashboard](https://user-images.githubusercontent.com/92020620/145753940-7cd45c4e-6510-4aa3-a299-cfa19db62476.png)
![Remove books](https://user-images.githubusercontent.com/92020620/145753943-a06f75dc-3bc1-4161-9ea9-858296862049.png)
![Screenshot from 2021-12-12 19-27-15](https://user-images.githubusercontent.com/92020620/145715410-699255ab-65ab-41da-b752-5c74cb85c39a.png)
![Screenshot from 2021-12-13 10-16-24](https://user-images.githubusercontent.com/92020620/145753956-a00810fd-4097-4721-b48d-31867d0fd561.png)



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
API 1
/register
User can register here by using his credentials

/about
User can read about Contributors

API 2
/admin-login
Admin can login using his credentials

/user-login
User can login using his credentials

API 3
/success-login
After login User redirected to his dashboard

API 4
/success-register
User will be successfully registered and redirected to his dashboard

API 5
/adminLoginSuccess
After Admin login It will redirected to the page where he/she will add book details

/logout
When User/Admin wants to exit from his profile

API 6
/admin_dashboard
Admin will see his dashboard

API 7
/book-form-id/<book_id>/<user_id>/<numberofbooks>
User can borrow a specific book by using book id

/issued-books
When Book Issued process is complete

API 8
/viewbooks
Admin can view the existing books

API 9
/remove-book/<book_id>
Admin can remove an existing book

API 10
/issued-books/<user_id>
Can view all the books requested by the user

```

