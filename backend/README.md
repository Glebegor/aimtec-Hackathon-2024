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

Type | Json | Headers
--- | --- | ---
Request | {"Username": "nameeee","Password": "123321", "email":"email@email.com"} | --
Response | {"message": "ok"} | ---

##### /login - POST
Login.

Type | Json                                                                               | Headers
--- |------------------------------------------------------------------------------------| ---
Request | {"Email": "email@email.com","Password": "123321"}                                  | ---
Response | {"refresh": "123123dwqo", "access": "123e1231", "except": 36000000 (microsec), ""} | ---

##### /refresh - POST
Refresh token.

#### /workWT - v1
Work with texts, speeches and symbols.

##### /TextToSpeech - POST
##### /SpeachToText - POST
##### /SymbolsToText - POST
##### /TextToSymbols - POST

#### /translate - v1
Working with translations.
##### /translate - POST
## ENV
