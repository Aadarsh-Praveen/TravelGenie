import openai
from config import OPENAI_API_KEY

# Set OpenAI API Key
openai.api_key = OPENAI_API_KEY

def generate_travel_plan(destination, dates, preferences):
    """
    Generate a travel plan using OpenAI's updated API.
    """
    try:
        # Construct the prompt
        prompt = f"Plan a trip to {destination} from {dates}. Preferences: {preferences}."

        # Call OpenAI's Chat API with the updated method
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a travel assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and return the generated travel plan
        return response['choices'][0]['message']['content']

    except openai.error.OpenAIError as e:
        # Handle OpenAI-specific errors
        print(f"OpenAI API Error: {str(e)}")
        return f"Error with OpenAI API: {str(e)}"
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected Error: {str(e)}")
        return f"Unexpected error occurred: {str(e)}"
