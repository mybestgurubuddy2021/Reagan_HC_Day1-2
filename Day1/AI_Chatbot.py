import time  # Timestamps to the API and local files
import os  # Library giving us commands to the CLI level user
import joblib as jl  # Create a job task like make files or input something into a specific file
import google.generativeai as genai  # SDK (Software Development Kit)  supporting files for Gemini API
from dotenv import load_dotenv  # .env library support to make API usage more stable
from colorama import Fore

# MY API = 'AIzaSyAi6mhY0DBk0ergntlW92OpEDskyOd5sww'
AI_NAME = "Nebula AI"

# 1. Introduction Step
print(f"\nHello! Welcome to my program, my name is {AI_NAME}")
print("Ask me anything since AI are one of the smartest bots in this world\n")
time.sleep(2)

# 2. Setting Up a Bot
print("Before you access this AI, input your API Key")
GOOGLE_API_KEY = input("Please Enter Your API KEY : ")  # This will save API to a local variable
print("\nSetting up Engine (Powered by Gemini) ...")
time.sleep(3)
load_dotenv()
os.system("pause")

# 3. Checking API Connection to Google AI Studio
if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    print("\nConducting rerouting another API...")
    time.sleep(3)
    os.system("pause")
if not GOOGLE_API_KEY:
    print("\nError! API Key not found, restart this project or check it in `.env`")
    time.sleep(3)
    os.system("pause")
    exit(1)

# 4. Configure Gemini as our Chat Bot
genai.configure(api_key=GOOGLE_API_KEY)
print(f"\n{AI_NAME} engine (Powered by Gemini) is activated!")
time.sleep(1)

# 5. Creating unique chat session!
chat_title = input("Enter a name for your chat session (Default: \"Human\") : ") or "Human"
new_chat_id = f"{time.time()}"

# 6. Backlog
if not os.path.exists('data/'):  # checking if the folder exists or not
    os.mkdir('data/')  # if not then make 1

# Try to load previous chat if available
try:
    past_chats = jl.load('data/past_chats_list')
    print("\nPrevious chat session loaded successfully")
    time.sleep(2)
except FileNotFoundError:
    past_chats = {}
    print('\nNo previous chat sessions found. Starting a New Chat...')
    time.sleep(3)

# Initialize the chatbot model
print(f"\nInitializing {AI_NAME} platform...")
time.sleep(2)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()
print(f"{AI_NAME} Platform is Initialized!")
time.sleep(1)
try:
    messages = jl.load(f"data/{new_chat_id}-messages")
except FileNotFoundError:
    messages = []
if new_chat_id not in past_chats:
    past_chats[new_chat_id] = chat_title
    jl.dump(past_chats, 'data/past-chats-list')

# 7. Start Chat Session
print("\nYour AI platform is created, let's start discussing!")
print("type `exit` to quit chat.\n")

# 8. Loop the chat and give conditions
while True:
    print(Fore.BLUE)
    user_input = input(f"{chat_title} (You) : ")
    if user_input.lower() == 'exit':
        print(Fore.RED)
        print("\nLeaving AI platform...\n")
        break

    response = chat.send_message(user_input)
    print(Fore.GREEN)
    print(f"{AI_NAME} : {response.text}")

    messages.append({'role': 'user', 'content': user_input})
    messages.append({'role': 'ai', 'content': response.text})
    jl.dump(messages, f"data/{new_chat_id}-messages")
    print(Fore.WHITE)
    print("Chat History Saved!")
