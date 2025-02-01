from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from config import GOOGLE_CREDENTIALS_FILE, SCOPES

def add_to_calendar(summary, start_time, end_time, calendar_id='praveen.aadarsh@gmail.com'):
    """
    Adds an event to Google Calendar.
    """
    try:
        # Load service account credentials
        creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
        service = build('calendar', 'v3', credentials=creds)

        # Define the event details
        event = {
            'summary': summary,
            'start': {'dateTime': start_time, 'timeZone': 'UTC'},
            'end': {'dateTime': end_time, 'timeZone': 'UTC'},
        }

        # Insert the event
        event_result = service.events().insert(calendarId=calendar_id, body=event).execute()
        print(f"Event created: {event_result.get('htmlLink')}")
        return event_result
    except Exception as e:
        print(f"Error adding to Google Calendar: {str(e)}")
        raise

def parse_dates(dates):
    """
    Parses a date range string in the format '[YYYY-MM-DD] to [YYYY-MM-DD]'
    and returns a tuple of start_date and end_date.
    """
    try:
        start_date, end_date = dates.split(" to ")
        return start_date.strip(), end_date.strip()
    except ValueError:
        raise ValueError("Dates must be in '[YYYY-MM-DD] to [YYYY-MM-DD]' format")
