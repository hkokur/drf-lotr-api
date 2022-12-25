# LOTR API

This project aims to serve the data about middle earth.

i have deployed the project on heroku. Go and test it => https://drf-lotr-api.herokuapp.com/api/

It is an REST API and for most endpoints, it returns the data in JSON format.

## About Project(Now)

For now, it can just serve the character informations in middle earth. You can acces the character name, race, birth, death, gender, hair, height, realm and spouse information.

There is no auth system for now. You can't register or login. No need username, password or token to acces any data. Readonly acces avaible.

There is no limitation so you can make requests that you want. Pls, don't make spam requests.

## Future

I will add the more information about middle earth. There are several items, areas, characters etc. I want to be aviable all valuable informations for middle earth enthusiasts.

I will add auth sytem and with auth, sources system will be avaible. The sources can add information into api.

# Endpoints


| Endpoints   | HTTP Verb | Description                                     |
| ------------- | :---------- | ------------------------------------------------- |
| /api        | GET       | List the characters with pagination             |
| /api/{id}   | GET       | Detail page of the character                    |
| /api/{name} | GET       | List page of the characters that have same name |

Also you can acces the endpoints from '/api/doc/schema/swagger-ui/' or can download scheme from 'api/doc/schema/'

# Acknowledgement

With thanks to the scraping work of:

* Paul Mooney -[Kaggle](https://www.kaggle.com/paultimothymooney/lord-of-the-rings-data)
