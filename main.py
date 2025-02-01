from flask import Flask, request, jsonify
from flask_cors import CORS
from openai_integration import generate_travel_plan
from airtable_integration import save_to_airtable
from calendar_integration import add_to_calendar
from datetime import datetime
from calendar_integration import add_to_calendar, parse_dates
from google.oauth2.service_account import Credentials
from config import GOOGLE_CREDENTIALS_FILE, SCOPES
from googleapiclient.discovery import build
from email_integration import send_email
from recommendation_integration import fetch_recommendations
import re



app = Flask(__name__)
CORS(app)

# Function to validate email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/')
def home():
    return "TravelGenie API is running!"

#For Travel plan
@app.route('/travel-plan', methods=['POST'])
def travel_plan():
    try:
        # Extract incoming JSON
        data = request.json
        print("Request received for /travel-plan:", data)

        # Correctly map incoming keys (ensure consistency with Voiceflow variable names)
        destination = data.get('User_Destination')
        dates = data.get('Start_Dates_and_End_Dates')
        preferences = data.get('preferences')  # Lowercase as per Voiceflow JSON body

        # Validate if required fields are present
        if not destination or not dates:
            print("DEBUG: Missing required fields.")
            return jsonify({"error": "Missing required fields: destination or dates"}), 400

        # Construct the response object
        response = {
            "destination": destination,
            "dates": dates,
            "preferences": preferences
        }
        print("Travel plan generated:", response)  # Debugging log
        return jsonify({"plan": response})  # Return success response

    except Exception as e:
        print(f"Error processing /travel-plan: {str(e)}")  # Debugging log
        return jsonify({"error": str(e)}), 500


#To save plan
@app.route('/save-plan', methods=['POST'])
def save_plan():
    try:
        # Extract incoming JSON from Voiceflow
        data = request.json
        print("Request received for /save-plan:", data)  # Debugging log

        # Map Voiceflow fields to Airtable column names
        airtable_data = {
            "Destination": data.get("User_Destination"),  # Matches Airtable "Destination" field
            "Dates": data.get("Start_Dates_and_End_Dates"),  # Matches Airtable "Dates" field
            "Preferences": data.get("preferences")  # Matches Airtable "Preferences" field
        }

        # Save data to Airtable
        record = save_to_airtable(airtable_data)
        print("Record saved to Airtable:", record)  # Debugging log
        return jsonify({"record": record})  # Return successful response

    except Exception as e:
        print("Error in /save-plan:", str(e))  # Debugging log
        return jsonify({"error": str(e)}), 500



#For Calendar
@app.route('/add-calendar', methods=['POST'])
def add_calendar():
    try:
        # Receive data from the Voiceflow webhook
        data = request.json
        print("Request received for /add-calendar:", data)

        # Extract the required fields from the JSON payload
        summary = data.get('summary')
        dates = data.get('dates')

        # Validate input
        if not summary or not dates:
            print("DEBUG: Missing summary or dates.")
            return jsonify({"error": "Missing required fields: summary or dates"}), 400

        # Parse and validate the dates format
        try:
            start_date, end_date = parse_dates(dates)
        except ValueError as ve:
            print("DEBUG: Invalid dates format.")
            return jsonify({"error": str(ve)}), 400

        # Construct the start and end datetime in the required format
        start_time = f"{start_date}T00:00:00Z"
        end_time = f"{end_date}T23:59:59Z"

        # Add the event to Google Calendar using the helper function
        event = add_to_calendar(summary, start_time, end_time)
        print(f"Event successfully added to Google Calendar: {event}")

        # Return a successful response with event details
        return jsonify({
            "message": "Event successfully added to Google Calendar.",
            "event": event
        }), 200

    except Exception as e:
        print(f"Error in /add-calendar: {str(e)}")
        return jsonify({"error": str(e)}), 500


# To send mail
@app.route('/send-email', methods=['POST'])
def send_trip_email():
    try:
        # Extract data from the request
        data = request.json
        print("Request received for /send-email:", data)

        user_email = data.get("user_email")
        destination = data.get("User_Destination")  # Match key with /travel-plan
        dates = data.get("Start_Dates_and_End_Dates")  # Match key with /travel-plan
        preferences = data.get("preferences", "No specific preferences")  # Match key with /travel-plan

        # Validate the email address
        if not is_valid_email(user_email):
            return jsonify({"error": "Invalid email address"}), 400

        # Validate destination and dates
        if not destination or not dates:
            return jsonify({"error": "Missing destination or dates"}), 400

        # Fetch personalized recommendations
        if preferences.lower() != "no preference":
            recommendations = fetch_recommendations(destination, preferences)
        else:
            recommendations = "No specific recommendations available."

        # Construct the email content
        subject = "Your Travel Plan Details with Recommendations"
        body = (
            f"Hello,\n\n"
            f"Here are the details of your upcoming trip:\n"
            f"- Destination: {destination}\n"
            f"- Dates: {dates}\n"
            f"- Preferences: {preferences}\n\n"
            f"Recommendations:\n{recommendations}\n\n"
            f"Thank you for using TravelGenie!"
        )

        # Send the email
        if send_email(user_email, subject, body):
            return jsonify({"message": "Email sent successfully!"})
        else:
            return jsonify({"error": "Failed to send email"}), 500

    except Exception as e:
        print(f"Error in /send-email: {str(e)}")
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
