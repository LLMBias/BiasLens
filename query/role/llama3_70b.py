import csv
from openai import OpenAI

# Set your API key and base_url
api_key = 'Your API Key'
base_url = "https://api.aimlapi.com/v1"

# Define the list of attributes
attributes = ["ability", "age", "body", "culture", "race", "religion", "gender", "occupations", "social", "victim", "character"]

# Define the number of runs
num_runs = 3

# Initialize the API instance
api = OpenAI(api_key=api_key, base_url=base_url)

# Iterate over each attribute and process the corresponding CSV file
for attribute in attributes:
    csv_filename = f"questions/role/{attribute}_questions.csv"
    
    # Read the questions
    questions_list = []
    with open(csv_filename, 'r', encoding='utf-8', errors="ignore") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            questions_list.append(row)
    
    # Send each question and get the answer, collecting num_runs results
    for run in range(1, num_runs + 1):
        output_filename = f"./answers/role/llama3_70b/{attribute}_answers_0{run}.csv"
        
        with open(output_filename, 'w', newline='', errors="ignore") as response_file:
            response_writer = csv.writer(response_file)
            response_writer.writerow(['Role', 'Question Type', 'Question', 'Answer'])
            
            for role, question_type, question in questions_list:
                # Generate different messages based on the question type
                if question_type == "Yes/No":
                    message = question + f"""\nPlease **only answer yes/no.**\n
                         Answer Format (You MUST follow this):\n
                         Yes/No.\n""" 
                elif question_type == "Choice":
                    message = question + f"""\nPlease **only make one choice** from all options.**\n
                         Answer Format (You MUST follow this):\n
                         Your choice.\n"""
                elif question_type == "Wh":
                    message = question + "\nProvide the answer in no more than 100 words."
                
                print(message)

                try:
                    # Call the new API for the request
                    completion = api.chat.completions.create(
                        model="meta-llama/Llama-3-70b-chat-hf",  # Model name
                        messages=[
                            {"role": "system", "content": f"You are a {role}"},
                            {"role": "user", "content": message},
                        ]
                    )
                    answer = completion.choices[0].message.content.strip()

                except Exception as e:
                    answer = "Error: " + str(e)

                # Write the answer to the CSV file
                response_writer.writerow([role, question_type, question, answer])
