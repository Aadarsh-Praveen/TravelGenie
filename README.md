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

📌 **Example for Destination: Ireland | Preferences: Nature**  

### **Accommodations:**  
1. The Merrion Hotel, Dublin - A luxurious 5-star hotel with a serene garden and Irish charm.  
2. Ashford Castle - A medieval castle-turned-hotel surrounded by stunning landscapes.  
3. Glenlo Abbey Hotel - A peaceful retreat near Galway with an old-world charm.  

### **Popular Places:**  
1. Cliffs of Moher - Spectacular sea cliffs located in County Clare offering stunning views of the Atlantic Ocean.  
2. Killarney National Park - A beautiful park in County Kerry with lakes, mountains, and woodlands perfect for hiking and wildlife spotting.  
3. The Ring of Kerry - A scenic drive around the Iveragh Peninsula with breathtaking coastal views and picturesque villages.  
4. Connemara National Park - Located in County Galway, this park offers rugged landscapes, mountains, and lakes for outdoor enthusiasts.  

### **Restaurants:**  
1. The Strawberry Tree (Wicklow) - Ireland's only certified organic restaurant offering locally sourced dishes in a beautiful setting.  
2. The Chart House (Dingle) - A seafood restaurant in County Kerry known for its fresh, locally caught seafood and stunning views of Dingle Bay.  
3. Wild Honey Inn (Clare) - A Michelin-starred restaurant in County Clare known for its creative dishes using locally sourced ingredients.  
4. The Fatted Calf (Westmeath) - A popular restaurant in County Westmeath known for its farm-to-table approach and delicious seasonal menus.  

### **Activities:**  
1. Hiking in the Wicklow Mountains - Explore the scenic trails in the Wicklow Mountains National Park for a day of hiking and enjoying nature.  
2. Kayaking in Killarney Lakes - Rent a kayak and paddle through the tranquil lakes of Killarney National Park for a unique perspective.  

