# Python API Server

This project is created to perform simulation testing of a simple API using Postman. Additionally, this document is one of the follow-ups to the created [user stories](https://github.com/ismoyoas/python-api-server/blob/master/User_Stories.md) example.

Table of Contents
-----------------

* [Prerequisite](#prerequisite)
* [Documentation](#documentation)
    * [Create a New Account](#createanewaccount)
    * [Login & Show Account Data](#login&showaccountdata)
    * [Show a List of Users](#showalistofusers)
    * [Update Data](#updatedata)
    * [Out of Session](#outofsession)
    * [Forgot The Password](#forgotthepassword)
    * [Delete Account](#deleteaccount)

<a name="documentation"></a>
Documentation
------------

<a name="prerequisite"></a>
Prerequisite
------------

Execute the following instructions in the `command line` or `terminal` to run the API server.

```SHELL
$ git clone https://github.com/ismoyoas/python-api-server.git
$ cd python-api-server
$ python3 app.py
```

If there are no disruptions (library dependencies or others), the display in the `terminal` will look like the one below.

```SHELL
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on "your_host_address"
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx

```

In the `your_host_address` section, it will contain the IP address that will be used as the base URL in API testing.

<a name="createanewaccount"></a>
Create a New Account
------------

The following endpoint works by creating new user data in a temporary database storage based on the prepared template.

| **Content-Type** | `application/json`        |
| :--------------- | :------------------------ |
| **Endpoint**     | `<base_url>/users/signup` |
| **Method**       | `POST`                    |
| **Status**       | `201 CREATED`             |

**Request Body :**
```JSON
{
    "username": "User Friendly",
    "email": "userfriendly@api.com",
    "password": "*********"
}
```

**Response Body :**
```JSON
{
    "message": "account created successfully"
}
```

<a name="login&showaccountdata"></a>
Login & Show Account Data
------------

The endpoint functions by displaying user data that has been registered by searching for a matching `email` and `password` in the user database. Additionally, this endpoint will create and add a `session_token` to the user database as a representation of the currently active user.

| **Content-Type** | `application/json` |
| :--------------- | :----------------- |
| **Endpoint**     | `/users/signin`    |
| **Method**       | `POST`             |
| **Status**       | `200 CREATED`      |

**Request Body :**
```JSON
{
    "email": "userfriendly@api.com",
    "password": "*********"
}
```

**Response Body :**
```JSON
{
    "data": {
        "access_token": "gdTzzGBZ",
        "address": "",
        "email": "userfriendly@api.com",
        "hobby": "",
        "password": "*********",
        "session_token": "UJ18o5Y5",
        "username": "User Friendly"
    },
    "message": "log in successfully"
}
```

<a name="showalistofusers"></a>
Show a List of Users
------------

The following endpoint functions by displaying users who have registered in the user database through the existing `access_token`. The information displayed includes only the `username`, `email`, and the total `number` of registered users.

| **Content-Type** | `application/json`      |
| :--------------- | :---------------------- |
| **Endpoint**     | `/users/<access_token>` |
| **Method**       | `GET`                   |
| **Status**       | `200 OK`                |

**Request Body :**
```JSON
{}
```

**Response Body :**
```JSON
{
    "data": [
        {
            "email": "userfriendly@api.com",
            "username": "User Friendly"
        }
    ],
    "message": "success",
    "number": 1
}
```

<a name="updatedata"></a>
Update Data
------------

The following endpoint uses an access token to update data. The attributes that can be updated include `username`, `email`, `password`, `address`, and `hobby`. These attributes must be included in the request body.

| **Content-Type** | `application/json`      |
| :--------------- | :---------------------- |
| **Endpoint**     | `/users/<access_token>` |
| **Method**       | `PUT`                   |
| **Status**       | `201 CREATED`           |

**Request Body :**
```JSON
{
    "username": "Funny User",
    "email": "funnyuser@api.com",
    "password": "*********",
    "address": "East Java",
    "hobby": "Watch Movies"
}
```

**Response Body :**
```JSON
{
    "data": {
        "access_token": "gdTzzGBZ",
        "address": "East Java",
        "email": "funnyuser@api.com",
        "hobby": "Watch Movies",
        "password": "*********",
        "session_token": "UJ18o5Y5",
        "username": "Funny User"
    },
    "message": "data has been updated"
}
```

<a name="outofsession"></a>
Out of Session
------------

The following endpoint uses a `session_token` as a reference to delete the session token found in the user database. This endpoint represents a user who has logged out of the session.

| **Content-Type** | `application/json`       |
| :--------------- | :----------------------- |
| **Endpoint**     | `/users/<session_token>` |
| **Method**       | `PATCH`                  |
| **Status**       | `200 OK`                 |

**Request Body :**
```JSON
{}
```

**Response Body :**
```JSON
{
    "message": "you are logged out"
}
```

<a name="forgotthepassword"></a>
Forgot The Password
------------

This endpoint is used when a user forgets their password, preventing them from logging into the session. The attributes required are the registered `email` in the user database and the `new_password` to replace the old password. Additionally, this endpoint will automatically create a `session_token` and an `access_token`, representing that the user has logged in using the new password.

| **Content-Type** | `application/json`       |
| :--------------- | :----------------------- |
| **Endpoint**     | `/users/forgot_password` |
| **Method**       | `POST`                   |
| **Status**       | `201 CREATED`            |

**Request Body :**
```JSON
{
    "email": "funnyuser@api.com",
    "new_password": "*********"
}
```

**Response Body :**
```JSON
{
    "access_token": "pYIAnRBu",
    "message": "password has been updated",
    "session_token": "pYIAnRBu"
}
```

<a name="deleteaccount"></a>
Delete Account
------------

This endpoint is used to permanently delete all user data with the same `access_token`, requiring the user to create a new account to resume using the API service.

| **Content-Type** | `application/json`      |
| :--------------- | :---------------------- |
| **Endpoint**     | `/users/<access_token>` |
| **Method**       | `DELETE`                |
| **Status**       | `200 OK`                |

**Request Body :**
```JSON
{}
```

**Response Body :**
```JSON
{
    "message": "account has been permanently deleted"
}
```
