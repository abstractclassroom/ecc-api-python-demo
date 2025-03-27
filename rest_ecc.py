import requests
import json

# Replace with your actual API Gateway endpoint
API_URL = "https://26uk022nra.execute-api.us-east-1.amazonaws.com/demo/cse-310"

def is_binary_string(s):
    return all(c in '01' for c in s)

def main():
    while True:
        user_input = input("\nEnter a 12-bit string to encode or a 24-bit string to decode (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            break

        if len(user_input) not in [12, 24] or not is_binary_string(user_input):
            print("❌ Invalid input. Please enter a 12-bit or 24-bit binary string.")
            continue

        payload = {"input": user_input}

        try:
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            data = response.json()

            print("\n✅ Response from server:")
            print(f"Input : {data.get('input')}")
            print(f"Output: {data.get('output')}")
            print(f"Index : {data.get('index')}")
            print(f"Errors: {data.get('errors')}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
        except Exception as ex:
            print(f"❌ Unexpected error: {ex}")

if __name__ == "__main__":
    main()

