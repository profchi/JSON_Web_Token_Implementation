# JSON_Web_Token_Implementation
Implementing JSON web token using Python

JSON Web Token or JWT, is a standard to create web access tokens. The code implements 
two functions to support generating and verifying a token. To give some context, 
this feature is for a web service, where:

• the backend server will call the generating function implemented and issue an
authenticated user a token when they are logged into a system; then

• the user will pass the token along with each and every API call to the system thereafter

• before processing the API calls, the system will call the verifying function implemented to
ensure the token is validate and the user has been authenticated properly.


As a very brief example, your functions may be called in a way somewhat like this:

token = generate_token()
if verify_token(token) is True:
	print(“Hello, welcome back!”)
else:
	print(“Hey, I’m not sure I know you, maybe try again?”)
