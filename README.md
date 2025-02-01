# 📌 TravelGenie - AI-Powered Travel Planner 🚀

## 🌍 Overview  
TravelGenie is an AI-driven travel assistant that streamlines travel planning by integrating **Google Calendar, Airtable, OpenAI’s recommendation API, and Email services**. Users can input their **destination, dates, and preferences**, and the system automatically handles:  

✔ **Trip Planning** (via OpenAI for recommendations)  
✔ **Storing Travel Details** (via Airtable)  
✔ **Adding Events to Google Calendar**  
✔ **Sending Personalized Travel Emails**  

🔗 **Live Website:** [TravelGenie Chatbot](https://sites.google.com/view/travelgenie-chatbot/home)

---

## ✨ Features
1. **📅 Travel Planning:**  
   - Captures **destination, dates, and user preferences**.  
   - Generates **personalized recommendations** using OpenAI.  

2. **🗄 Save Plan (Airtable Integration):**  
   - Stores travel plans in **Airtable** for record-keeping.  

3. **📆 Google Calendar Integration:**  
   - Automatically **adds travel dates** as events in Google Calendar.  

4. **📧 Email Notifications:**  
   - Sends a **detailed travel itinerary** via email, including OpenAI-generated recommendations.  

---

## 🛠 API Endpoints

### 1️⃣ **/travel-plan** - Capture Travel Details  
**Method:** `POST`  
**Request Body:**  
```json
{
  "User_Destination": "Ireland",
  "Start_Dates_and_End_Dates": "2025-04-04 to 2025-05-05",
  "preferences": "nature"
}
```
📌 **Response Example:**  
```json
{
  "plan": {
    "destination": "Ireland",
    "dates": "2025-04-04 to 2025-05-05",
    "preferences": "nature"
  }
}
```

---

### 2️⃣ **/save-plan** - Save Travel Plan to Airtable  
**Method:** `POST`  
**Request Body:**  
```json
{
  "User_Destination": "Ireland",
  "Start_Dates_and_End_Dates": "2025-04-04 to 2025-05-05",
  "preferences": "nature"
}
```
📌 **Response Example:**  
```json
{
  "record": {
    "id": "rec12345",
    "fields": {
      "Destination": "Ireland",
      "Dates": "2025-04-04 to 2025-05-05",
      "Preferences": "nature"
    }
  }
}
```

---

### 3️⃣ **/add-calendar** - Add Event to Google Calendar  
**Method:** `POST`  
**Request Body:**  
```json
{
  "summary": "Trip to Ireland",
  "dates": "2025-04-04 to 2025-05-05"
}
```
📌 **Response Example:**  
```json
{
  "message": "Event successfully added to Google Calendar.",
  "event": {
    "id": "event123",
    "htmlLink": "https://www.google.com/calendar/event?eid=abc123"
  }
}
```

---

### 4️⃣ **/send-email** - Send Personalized Travel Plan via Email  
**Method:** `POST`  
**Request Body:**  
```json
{
  "user_email": "example@example.com",
  "User_Destination": "Ireland",
  "Start_Dates_and_End_Dates": "2025-04-04 to 2025-05-05",
  "preferences": "nature"
}
```
📌 **Response Example:**  
```json
{
  "message": "Email sent successfully!"
}
```

---

## 🧠 **AI-Generated Recommendations**
Upon entering a **destination & preferences**, OpenAI generates **detailed recommendations** for places, hotels, and restaurants.

---


##📸 **Snapshots of TravelGenie Setup**
Below are snapshots of how the TravelGenie system is structured and works:

1️⃣ Voiceflow Chatbot Setup
💬 This shows the Voiceflow conversation flow, how the bot interacts with the user, and API calls.
📌 Snapshot:

2️⃣ Airtable Data Storage
🗂 This displays how user travel plans are stored in Airtable after using the bot.
📌 Snapshot:

3️⃣ Google Calendar Integration
📅 This confirms that the travel dates are successfully added to Google Calendar.
📌 Snapshot:

4️⃣ Email Confirmation
📧 A snapshot of the email sent by the bot containing the trip details & recommendations.
📌 Snapshot:

