# BACKEND
## DESCRIPTION
## API
### Responses
Success response [200]
```json
{
    "message": "Success message"
}
```
Error response [404, 500, 402, 401]
```json
{
    "message": "Error message"
}
```
### Endpoints
/api/v1 - public routes</br>
/api/v2 - private routes</br>
Example: {HOSTING}/api/v1/auth/registration

#### /auth - v1
Working with authorization and authentication.

##### /registration - POST
Registration.

Type | Json                                                                    | Headers
--- |-------------------------------------------------------------------------| ---
Request | {"username": "nameeee","password": "123321", "email":"email@email.com"} | --
Response | {"message": "ok"}                                                       | ---

##### /login - POST
Login.

 Type     | Json                                                                                                                      | Headers 
----------|---------------------------------------------------------------------------------------------------------------------------|--------
 Request  | {"email": "email@email.com","password": "123321"}                                                                         | ---    
 Response | {"refresh": "123123dwqo", "access": "123e1231", "except": 36000000 (microsec), "exceptTime": 1231908402213912 (microsec)} | ---

##### /refresh - POST
Refresh token.

#### /workWT - v1
Work with texts, speeches and symbols.

##### /TextToSpeech - POST
Type | Json                                                                             | Headers
--- |----------------------------------------------------------------------------------| ---
Request | {"text":"Some text", "textLanguage": "EN", "textToLanguage": "CZ"}               | --
Response | {"speech": "1230809481092834", "speechLanguage": "EN"} | ---

##### /SpeachToText - POST
Type | Json                                                                             | Headers
--- |----------------------------------------------------------------------------------| ---
Request | {"speech": "1230809481092834", "speechLanguage": "GE", "speechToLanguage": "EN"} | --
Response | {"text":"Some text", "textLanguage": "EN"}                                       | ---

##### /SymbolsToText - POST
Type | Json                          | Headers
--- |-------------------------------| ---
Request | {"image": "1230809481092834"} | --
Response | {"text":"Some text", "textLanguage": "EN"} | ---

##### /TextToSymbols - POST
Type | Json                                              | Headers
--- |---------------------------------------------------| ---
Request | {"text": "Some text", "textLanguage": "EN", "textToLanguage": "CZ"}} | --
Response | {"image":"1230809481092834"}                      | ---

#### /translate - v1
Working with translations.
##### /translate - POST

Type | Json                                                                | Headers
--- |---------------------------------------------------------------------| ---
Request | {"text": "Some text", "textLanguage": "EN", "textToLanguage": "CZ"} | --
Response | {"text": "Some text", "textLanguage": "EN"}                                        | ---
## ENV
