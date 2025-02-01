import openai
from config import OPENAI_API_KEY

# Set OpenAI API Key
openai.api_key = OPENAI_API_KEY

def fetch_recommendations(destination, preferences):
    """
    Fetch recommendations based on user destination and preferences.
    """
    try:
        # Construct the prompt
        prompt = (
            f"Suggest some popular places, restaurants, and activities in {destination} "
            f"that align with these preferences: {preferences}."
        )

        # Call OpenAI's Chat API using gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the latest recommended model
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )

        # Extract and return the recommendations
        return response['choices'][0]['message']['content'].strip()

    # Handle OpenAI-specific errors
    except openai.error.OpenAIError as openai_error:
        print(f"OpenAI API Error: {openai_error}")
        return f"Error with OpenAI API: {openai_error}"

    # General exception for any unexpected errors
    except Exception as general_error:
        print(f"Unexpected Error: {general_error}")
        return f"Unexpected error occurred: {general_error}"
