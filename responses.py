import openai



def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
        ],
    )
    return response["choices"][0]["message"]["content"]






def remove_disliked_foods(response, disliked_foods):
    # Split recommendations into individual lines
    lines = response.split("\n")

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

