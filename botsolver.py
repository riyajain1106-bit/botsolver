import requests
import getpass
import os

API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = os.environ.get("GROQ_API_KEY", "")
MODEL   = "llama-3.3-70b-versatile"

WHITE  = "\033[97m"
GREEN  = "\033[92m"
PINK   = "\033[95m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def get_username():
    try:
        return os.getlogin()
    except Exception:
        return getpass.getuser()

def ai_response(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are Botsolver, a helpful CLI assistant. Keep responses concise and avoid markdown formatting.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def main():
    if not API_KEY:
        print("Error: GROQ_API_KEY environment variable is not set.")
        return
    username = get_username()
    print(f"{WHITE}{BOLD}Welcome to Botsolver!{RESET}")
    print(f"{PINK}So tell me what you wanna do today? (Type 'exit' to quit){RESET}\n")

    while True:
        try:
            user_input = input(f"{GREEN}{username}{RESET}: ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{GREEN}Goodbye!{RESET}")
            break

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print(f"{GREEN}Goodbye!{RESET}")
            break

        try:
            reply = ai_response(user_input)
            print(f"\n{PINK}{BOLD}Botsolver Says:{RESET}")
            print(f"{RED}{reply.strip()}{RESET}")
            print(f"\n{PINK}What else would you like to know? (Type 'exit' to quit){RESET}\n")
        except requests.exceptions.RequestException as e:
            print(f"Error talking to the AI: {e}\n")

if __name__ == "__main__":
    main()
