<h1 align="center"> CAFE_API </h1>


You can find the [Documentation](https://documenter.getpostman.com/view/17439736/U16jP6Hp) here

## Overview

This is an API that collects and show information on nearby cafes.

Feel free to create an issue if you find any bugs.

## Design

This API is made using flask and the requests are then stored in database inside the web server

## Items

An example on how an item in this API would look like in a table form:

Field | Description
------|------------
name | Timberyard
map_url | https://goo.gl/maps/myxuSp44xB46Bp2v6
coffee_price | 32.75
img_url | https://goo.gl/maps/A5DHNT3kuppcDLwa7
name | Tim Hortons
seats | 20
location | 209 Glenridge Ave, St. Catharines, ON L2T 3J6
has_wifi | True
has_toilet | True
has_sockets | False
can_take_calls | True

Parameters in this API: 

Field | Description
------|------------
loc | Peckham
new_price | $31
api_key | ijwbcowbvouwyebrvouwbeocuhospkax


**EXAMPLES**

Request[GET]: https://cafeapi-flask-app.herokuapp.com/search?loc=Peckham

```javascript
{
    "cafe": {
        "can_take_calls": false,
        "coffee_price": "£2.75",
        "has_sockets": true,
        "has_toilet": true,
        "has_wifi": true,
        "id": 2,
        "img_url": "https://images.squarespace-cdn.com/content/v1/5734f3ff4d088e2c5b08fe13/1555848382269-9F13FE1WQDNUUDQOAOXF/ke17ZwdGBToddI8pDm48kAeyi0pcxjZfLZiASAF9yCBZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpzV8NE8s7067ZLWyi1jRvJklJnlBFEUyq1al9AqaQ7pI4DcRJq_Lf3JCtFMXgpPQyk/copeland-park-bar-peckham",
        "location": "Peckham",
        "map_url": "https://g.page/CopelandSocial?share",
        "name": "Social - Copeland Road",
        "seats": "20-30"
    }
}
```

Request[GET]: https://cafeapi-flask-app.herokuapp.com/all

```javascript
{
    "cafe": [
        {
            cafe1
        },
        {
            cafe2
        },
        {
            cafe3
        }
        ]
}
      
```

Request[GET]: https://cafeapi-flask-app.herokuapp.com/random

```javascript
{
    "cafe": {
        "can_take_calls": false,
        "coffee_price": "$31",
        "has_sockets": true,
        "has_toilet": true,
        "has_wifi": true,
        "id": 3,
        "img_url": "https://lh3.googleusercontent.com/p/AF1QipOMzXpKAQNyUvrjTGHqCgWk8spwnzwP8Ml2aDKt=s0",
        "location": "Peckham",
        "map_url": "https://g.page/one-all-cafe?share",
        "name": "One & All Cafe Peckham",
        "seats": "20-30"
    }
}
```

Request[POST]: https://cafeapi-flask-app.herokuapp.com/add

Pass the body in the request as described in [Documentation](https://documenter.getpostman.com/view/17439736/U16jP6Hp)

```javascript
{
    "response": {
        "success": "Successfully added new cafe"
    }
}
```


Request[PATCH]: https://cafeapi-flask-app.herokuapp.com/update-price/3?new_price=$31

```javascript
{
    "Success": "Successfully updated the price"
}
```

Request[DELETE]: https://cafeapi-flask-app.herokuapp.com/report-closed/21?api_key=ijwbcowbvouwyebrvouwbeocuhospkax

```javascript
{
    "Success": "Successfully deleted the cafe"
}
```


## Authentication
This API is open and thus do no require any authentication in any request except in delete request where you have to provide the given API key.

## Rate limit
No rate limit

[Documentation](https://documenter.getpostman.com/view/17439736/U16jP6Hp)

