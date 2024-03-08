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

#### /auth - v1

##### /registration - POST
##### /login - POST
##### /refresh - POST

#### /workWT - v1
##### /TextToSpeech - POST
##### /SpeachToText - POST
##### /SymbolsToText - POST
##### /TextToSymbols - POST

#### /translate - v1
##### /translate - POST
## ENV
