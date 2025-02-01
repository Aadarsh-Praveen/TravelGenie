# TravelGenie


**#Overview

TravelGenie is an interactive API-driven project designed to streamline travel planning by
integrating user input with Google Calendar, Airtable, OpenAI’s recommendation API, and email
services. Users can input their destination, dates, and preferences, and the system handles trip
planning, storing data, generating recommendations, and sending personalized emails.
Features
1. Travel Plan
○
Captures user input for destination, dates, and preferences.
○
Validates and processes user-provided details.
2. Save Plan
○
Stores the user’s travel details in Airtable for record-keeping.
3. Add Calendar
○
Adds travel dates to Google Calendar for easy tracking.
4. Send Email
○
Sends a personalized email to the user with their travel details and
OpenAI-generated recommendations.
Endpoints
1. Travel Plan Endpoint
URL: /travel-plan
Method: POST
Description: Processes user travel details.
Request Body:
{
"User
_
Destination": "Paris"
,
"Start
_
Dates
_
and
_
End
_
Dates": "2025-05-10 to 2025-05-20"
,
"preferences": "food and culture"
}
Response:
{
"plan": {
"destination": "Paris"
,
"dates": "2025-05-10 to 2025-05-20"
,
"preferences": "food and culture"
}
}
2. Save Plan Endpoint
URL: /save-plan
Method: POST
Description: Saves the travel plan in Airtable.
Request Body:
{
"User
_
Destination": "Paris"
,
"Start
_
Dates
_
and
_
End
_
Dates": "2025-05-10 to 2025-05-20"
,
"preferences": "food and culture"
}
Response:
{
"record": {
"id": "rec12345"
,
"fields": {
"Destination": "Paris"
,
"Dates": "2025-05-10 to 2025-05-20"
,
"Preferences": "food and culture"
}
}
}
3. Add Calendar Endpoint
URL: /add-calendar
Method: POST
Description: Adds the trip to Google Calendar.
Request Body:
{
"summary": "Paris"
,
"dates": "2025-05-10 to 2025-05-20"
}
Response:
{
"message": "Event successfully added to Google Calendar.
"
,
"event": {
"id": "event123"
,
"htmlLink": "https://www.google.com/calendar/event?eid=abc123"
}
}
4. Send Email Endpoint
URL: /send-email
Method: POST
Description: Sends a personalized email to the user with travel details and recommendations.
Request Body:
{
"user
_
email": "example@example.com"
,
"User
_
Destination": "Paris"
,
"Start
_
Dates
_
and
_
End
_
Dates": "2025-05-10 to 2025-05-20"
,
"preferences": "food and culture"
}
Response:
{
"message": "Email sent successfully!"
}
Key Functionalities
1. OpenAI Integration
●
Used to generate travel recommendations based on user preferences.
●
Recommendations include activities, restaurants, and local highlights.
Code Reference: recommendation_integration.py
2. Airtable Integration
●
Stores travel data for future reference.
●
Utilizes the Airtable API.
Code Reference: airtable_integration.py
3. Google Calendar Integration
●
Adds events to the user’s Google Calendar.
●
Uses Google Calendar API.
Code Reference: calendar_integration.py
4. Email Integration
●
Send travel details and recommendations via email.
●
Uses SMTP for email delivery.
Code Reference: email_integration.py
Setup Instructions
1. Environment Variables
●
Airtable:
○
AIRTABLE_ACCESS_TOKEN: API key for Airtable.
○
AIRTABLE_BASE_ID: Base ID for Airtable.
○
AIRTABLE_TABLE_NAME: Name of the table.
●
Google Calendar:
○
GOOGLE_CREDENTIALS_FILE: Path to Google credentials JSON file.
○
SCOPES: Google API scopes.
●
OpenAI:
○
OPENAI_API_KEY: API key for OpenAI.
●
Email:
○
SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD.
2. Dependencies
Install dependencies using:
pip install flask flask-cors openai google-api-python-client requests python-dotenv
3. Running the Application
Start the Flask server:
python main.py
Testing
Using Postman
●
Add JSON payloads to respective endpoints.
●
Verify the responses.
Logging
●
Check logs in the console for detailed debugging information.
Future Enhancements
●
User Authentication: Add authentication for enhanced security.
●
Multi-Language Support: Allow users to select their preferred language.
●
Payment Integration: Add payment options for booking.
