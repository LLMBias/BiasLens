import openai
import csv

# Set your OpenAI API key and base_url
client = openai.OpenAI(api_key="Your API Key", base_url="https://api.deepseek.com")

# Define the list of attributes
attributes = ["ability", "age", "body", "culture", "race", "religion", "gender", "occupations", "social", "victim", "character"]

# Define the number of runs
num_runs = 3

# Iterate over each attribute and process the corresponding CSV file
for attribute in attributes:
    csv_filename = f"questions/without_role/{attribute}_questions.csv"
    
    # Read the questions
    questions_list = []
    with open(csv_filename, 'r', encoding='utf-8', errors="ignore") as csvfile:  # Explicitly specify encoding as utf-8
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            questions_list.append(row)
    
    # Send each question and get the answer, collecting results for num_runs
    for run in range(1, num_runs + 1):
        output_filename = f"./answers/without_role/deepseek/{attribute}_answers_0{run}.csv"
        
        with open(output_filename, 'w', newline='', errors="ignore") as response_file:
            response_writer = csv.writer(response_file)
            response_writer.writerow(['Role', 'Question Type', 'Question', 'Answer'])
            
            for role, question_type, question in questions_list:
                if question_type == "Yes/No":
                    message = question + """\nPlease **only answer yes/no.**\n
                         Answer Format (You MUST follow this):\n
                         Yes/No.\n""" 
                elif question_type == "Choice":
                    message = question + """\nPlease **only make one choice** from all options.**\n
                         Answer Format (You MUST follow this):\n
                         Your choice.\n"""
                elif question_type == "Wh":
                    message = question + "\nProvide the answer in no more than 100 words."
                
                print(message)
                
                try:
                    response = client.chat.completions.create(
                        model="deepseek-chat",
                        messages=[
                            {"role": "user", "content": message}
                        ],
                        stream=False
                    )
                    answer = response.choices[0].message.content.strip()
                except Exception as e:
                    answer = "Error: " + str(e)
                
                response_writer.writerow([role, question_type, question, answer])
