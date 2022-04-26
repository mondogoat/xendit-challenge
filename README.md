**MANUAL TEST CASES**

**tc001**\
update qr successfully\
Given I have valid access token\
When I supplied the token in the request header\
And I call update qr endpoint with valid qr_id and valid request_body\
Then status code should be 200\
And I get the updated values back as a response


**tc002**\
update qr without providing auth token\
When I do not supply the token in the request header\
And I call update qr endpoint with valid qr_id and valid request_body\
Then status code should be 401\
And I get authentication error in the response

**tc003**\
update qr with invalid auth token\
Given I have invalid access token\
When I supplied the token in the request header\
And I call update qr endpoint with valid qr_id and valid request_body\
Then status code should be 403\
And I get authentication error that the action is forbidden

**tc004**\
update qr where qr does not exist\
Given I have a valid access token\
And I have a qr that does not exist in the system\
When I supplied the token in the request header\
And I call update qr endpoint with invalid qr_id and valid request_body\
Then status code should be 404\
And I get a qr code not found error in the response


**tc005**\
update qr where qr is already used\
Given I have a valid access token\
And I have a qr that was already used\
When I supplied the token in the request header\
And I call update qr endpoint with invalid qr_id and valid request_body\
Then status code should be 404\
And I get a qr code not found error in the response


**tc006**\
update qr validate minimum amount\
Given I have valid access token\
When I supplied the token in the request header\
And I call update qr endpoint with valid qr_id and request_body with minimum amt < 1500\
Then status code should be 422\
And I get an error message stating that the minimum amount should be 1500


**tc007**\
update qr validate maximum amount\
Given I have valid access token\
When I supplied the token in the request header\
And I call update qr endpoint with valid qr_id and request_body with max amt > 5000000\
Then status code should be 422\
And I get an error message stating that the maximum amount should be 5M\


**tc008**\
update qr validate against json schema\
Given I have valid access token\
When I supplied the token in the request header\
And I call update qr endpoint with valid qr_id and valid request_body\
Then status code should be 200\
And the schema check will not return an error


**tc009**\
update qr validate missing all fields input\
Given I have a valid access token\
When I supplied the token in the request header\
And I call update qr endpoint with valid qr_id and empty_request_body\
Then status code should be 400\
And I get an error message stating that description, callback_url and amount are required fields


**tc010**\
update qr validate missing amount field input\
Given I have a valid access token\
When I supplied the token in the request header\
And I call update qr endpoint with valid qr_id and empty_request_body\
Then status code should be 400\
And I get an error message stating that amount is a required field


**tc011**\
update qr validate missing callback_url field input\
Given I have a valid access token\
When I supplied the token in the request header\
And I call update qr endpoint with valid qr_id and empty_request_body\
Then status code should be 400\
And I get an error message stating that callback_url is a required field


**tc012**\
update qr validate missing description field input\
Given I have a valid access token\
When I supplied the token in the request header\
And I call update qr endpoint with valid qr_id and empty_request_body\
Then status code should be 400\
And I get an error message stating that description is a required field


**tc013**\
update qr validate invalid content-type\
Given I have a valid access token\
When I supply the token in the request header\
And I call update qr endpoint with valid qr_id and valid_request_body\
And I set the content-type to Text instead of JSON\
Then status code should be 400\
And I get an error message that the request passed is not a valid json format


**tc014**\
update qr validate passing a request body not in proper json format\
Given I have a valid access token\
When I supply the token in the request header\
And I call update qr endpoint with valid qr_id and a request body not in json format\
Then status code should be 400\
And I get an error message that the request passed is not a valid json format

Manual QA Engineer question 2:\
The test case we should create for that is a consumer-driven contract test case where we have a contract from microservice A(provider) and make sure that it would always return the needed fields from the response that microservice B(consumer) would need. This way, we know that for any new version of microservice A, the functionality of microservice B and all other microservices that gets a contract from the provider will not break.
