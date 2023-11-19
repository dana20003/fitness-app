import streamlit as st
import openai
import backoff

# Read the API key from the .env file
openai.api_key =st.secrets['API_KEY']

def calculate_calories(weight, height, age, gender,goal):
     
   if gender == "Male":
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
   else:
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    if goal == "Lose Weight":
       bmr = round(bmr * 1.2)
    
    else:
        bmr = round(bmr * 1.4)

   return bmr


def main():

    st.title("Fitness Recommendations App")

    weight = st.number_input("Enter your weight in kilograms:")
    height = st.number_input("Enter your height in meters:")
    age = st.number_input("Enter your age:")
    gender = st.radio("Select your gender:", ("Male", "Female"))
    goal = st.radio("Select your fitness goal:", ("Lose Weight", "Gain Muscle"))

      
    food_categories = {
    "Vegetables": ["Carrots", "Beets", "Potatoes", "Broccoli", "Cauliflower", "Lettuce", "Parsley", "Watercress", "Mint", "Spinach", "Cabbage", "Tomatoes", "Peppers", "Cucumbers", "Beans", "Peas"],
    "Fruits": ["Apples", "Bananas", "Oranges", "Grapes", "Strawberries", "Blueberries", "Kiwi", "Pineapple", "Mango", "Peaches"],
    "Legumes": ["Lentils", "Chickpeas", "Black Beans", "Kidney Beans", "Soybeans", "Green Peas", "Lima Beans"],
    "Milk Derivatives": ["Milk", "Cheese", "Yogurt", "Butter"],
    "Grains": ["Rice", "Pasta", "Bread", "Oats", "Quinoa", "Barley", "Couscous", "Buckwheat"],
    "Marine Food": ["Salmon", "Tuna", "Shrimp", "Cod", "Mussels", "Sardines"],
    "Meat": ["Chicken", "Beef", "Pork", "Turkey", "Lamb", "Duck"]
}
    



    disliked_foods = {}
    for category, options in food_categories.items():
           disliked_foods[category] = st.multiselect(f" foods you are allergic to or dont like in {category}:", options)

    disliked_foods_list = [f"{category} ({', '.join(disliked_foods[category])})" for category in food_categories]


    if st.button("Calculate Recommendations and Save"):
       

       prompt = f"My weight is {weight} kg, I am {height} m tall, and my goal is to {goal}.I don't like the following foods and have allergies to others: {', '.join(disliked_foods_list)}. Generate a diet and exercise schedule considering my preferences."
       response = get_response(prompt)


       calculated_calories = calculate_calories(weight, height, age, gender, goal)
       response = remove_disliked_foods(response,disliked_foods)


       st.header("Calculated Calories")
       st.write(calculated_calories)

       st.header("Diet and exrcise recommendation for you")
       st.write(response)
 

   
if __name__ == '__main__':
    main()




