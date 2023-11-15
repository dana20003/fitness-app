import streamlit as st
import openai

# Read the API key from the .env file
openai.api_key =st.secrets['API_KEY']

st.title("Fitness Recommendations App")


gender = st.radio("Select your gender:", ("Male", "Female"))

# Weight input
weight = st.number_input("Enter your weight in kilograms:")

# Height input
height = st.number_input("Enter your height in meters:")

# Age input
age = st.number_input("Enter your age:")

# Define food categories and their options
food_categories = {
    "Vegetables": ["Carrots", "Beets", "Potatoes", "Broccoli", "Cauliflower", "Lettuce", "Parsley", "Watercress", "Mint", "Spinach", "Cabbage", "Tomatoes", "Peppers", "Cucumbers", "Beans", "Peas"],
    "Fruits": ["Apples", "Bananas", "Oranges", "Grapes", "Strawberries", "Blueberries", "Kiwi", "Pineapple", "Mango", "Peaches"],
    "Legumes": ["Lentils", "Chickpeas", "Black Beans", "Kidney Beans", "Soybeans", "Green Peas", "Lima Beans"],
    "Milk Derivatives": ["Milk", "Cheese", "Yogurt", "Butter"],
    "Grains": ["Rice", "Pasta", "Bread", "Oats", "Quinoa", "Barley", "Couscous", "Buckwheat"],
    "Marine Food": ["Salmon", "Tuna", "Shrimp", "Cod", "Mussels", "Sardines"],
    "Meat": ["Chicken", "Beef", "Pork", "Turkey", "Lamb", "Duck"]
}

# Initialize a dictionary to store disliked foods for each category
disliked_foods = {}
for category, options in food_categories.items():
    disliked_foods[category] = st.multiselect(f" foods you are allergic to or dont like in {category}:", options)


# Fitness goal selection
goal = st.radio("Select your fitness goal:", ("Lose Weight", "Gain Muscle"))

# Calculate calorie requirements based on gender
if gender == "Male":
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
else:
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

if goal == "Lose Weight":
    calorie_requirement = bmr * 1.2  # Calorie deficit for weight loss
    
    diet_goal = "weight loss"
else:
    calorie_requirement = bmr * 1.4  # Calorie surplus for muscle gain
    diet_goal = "muscle gain"

# Initialize the chatbot
openai.api_key =st.secrets['API_KEY']

# Generate a list of disliked foods for each category
disliked_foods_list = [f"{category} ({', '.join(disliked_foods[category])})" for category in food_categories]

# Define the user message with a clear prompt for diet and exercise recommendations
user_message = f"My weight is {weight} kg, I am {height} m tall, and my goal is to {goal}. My estimated calorie requirement is {round(calorie_requirement, 2)} calories. I don't like the following foods and have allergies to others: {', '.join(disliked_foods_list)}. Generate a diet and exercise schedule considering my preferences."

# Use ChatGPT for generating recommendations
def get_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message,
            },
        ],
    )
    return response["choices"][0]["message"]["content"]



except openai.error.RateLimitError as e:
      retry_time = e.retry_after if hasattr(e, 'retry_after') else 30
      print(f"Rate limit exceeded. Retrying in {retry_time} seconds...")
      time.sleep(retry_time)
      return chat(prompt)

   except openai.error.APIError as e:
      retry_time = e.retry_after if hasattr(e, 'retry_after') else 30
      print(f"API error occurred. Retrying in {retry_time} seconds...")
      time.sleep(retry_time)
      return chat(prompt)

   except openai.error.ServiceUnavailableError as e:
      retry_time = 10  # Adjust the retry time as needed
      print(f"Service is unavailable. Retrying in {retry_time} seconds...")
      time.sleep(retry_time)
      return chat(prompt)

   except openai.error.Timeout as e:
      retry_time = 10  # Adjust the retry time as needed
      print(f"Request timed out: {e}. Retrying in {retry_time} seconds...")
      time.sleep(retry_time)
      return chat(prompt)

   except OSError as e:
      if isinstance(e, tuple) and len(e) == 2 and isinstance(e[1], OSError):
         retry_time = 10  # Adjust the retry time as needed
         print(f"Connection error occurred: {e}. Retrying in {retry_time} seconds...")
         time.sleep(retry_time)
         return chat(prompt)
      else:
         retry_time = 10  # Adjust the retry time as needed
         print(f"Connection error occurred: {e}. Retrying in {retry_time} seconds...")
         time.sleep(retry_time)
         raise e


Discover a selection of Free SEO Reports. Get your own report, delivered via email.
Check out my SEO reports

Discover my personal encyclopedia

a long term project inspired by Diderot
Read the first articles

You might also be interested in the following posts
How to fix the error OSError: ImageMagick binary cannot be found at /usr/local/bin/convert
How to fix the error OSError: ImageMagick binary cannot be found at /usr/local/bin/convert
How to identify users in PostHog, in an application built with Flask / Python & Javascript
How to identify users in PostHog, in an application built with Flask / Python & Javascript
Which cold emailing platforms can you connect to your branded email address?
Which cold emailing platforms can you connect to your branded email address?
Gandi is ending its free email offering. What can you do?
Gandi is ending its free email offering. What can you do?
How to shorten a long IPv6 IP Address to use it in Cloudflare IP lists
How to shorten a long IPv6 IP Address to use it in Cloudflare IP lists
One potential cause of inconsistencies between page views and impressions in adsense
One potential cause of inconsistencies between page views and impressions in adsense
Why do AI-generated images of hands and feet appear distorted?
Why do AI-generated images of hands and feet appear distorted?
What is the future of copywriting in the age of AI?
What is the future of copywriting in the age of AI?
How to transcribe the audio from Youtube videos with Python
How to transcribe the audio from Youtube videos with Python
Privacy policy
© 2023 Call Me Fred – Disclaimer: I am a participant in the Amazon Services Associates Program, an affiliate advertising program designed to provide a means for us to earn fees by linking to Amazon.com and affiliated sites.

 


def remove_disliked_foods(recommendations, disliked_foods):
    # Split recommendations into individual lines
    lines = recommendations.split("\n")

    # Filter out disliked foods
    filtered_lines = []
    for line in lines:
        for category in disliked_foods:
            if f"{category} (" in line:
                for food in disliked_foods[category]:
                    if food in line:
                        line = line.replace(food, "")
        filtered_lines.append(line)

    # Join the lines back into a single string
    return "\n".join(filtered_lines)



# Header
st.title("Fitness Recommendation App")
st.header("Diet and Exercise Recommendations")
st.write("Calorie Requirements for", diet_goal.capitalize(), "Goal:", round(calorie_requirement, 2), "calories")
recommendations = get_response(user_message)
recommendations_without_disliked_foods = remove_disliked_foods(recommendations, disliked_foods)
st.write(recommendations_without_disliked_foods)
