# Golay Codeword Encoder/Decoder Client

This project provides a simple Python script that interacts with a REST API to encode or decode Golay codewords. The script prompts the user for a 12-bit binary string to encode or a 24-bit binary string to decode, then sends the request to an AWS API Gateway-backed Lambda endpoint.

## Features

- Accepts 12-bit strings for Golay (24,12,8) encoding.
- Accepts 24-bit strings for decoding with up to 3-bit error correction.
- Sends data to a REST API and displays:
  - Encoded or decoded output
  - Codeword index
  - Number of corrected errors (for decoding)

---

## Prerequisites

- Python 3.x installed on your system.
- An active REST API endpoint accepting POST requests with a JSON body that includes a binary string in a field named `input`.

---

## Setting Up a Virtual Environment

Using a Python virtual environment is recommended to isolate your project dependencies.

### 1. Create a Virtual Environment

#### Mac/Linux

```bash
python3 -m venv venv
```

#### Windows

```cmd
python -m venv venv
```

---

### 2. Activate the Virtual Environment

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

#### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

---

### 3. Install Required Packages

Once the environment is activated, install the `requests` library:

```bash
pip install requests
```

---

### 4. Run the Script

Run the script:

```bash
python rest_ecc.py
```

---

### 5. Deactivate the Virtual Environment

When you're done working:

```bash
deactivate
```

---

## Usage

Follow the prompt in the script:

```
Enter a 12-bit string to encode or a 24-bit string to decode (or 'q' to quit):
```

Example output:

```
✅ Response from server:
Input : 101010101010
Output: 110011000011001100001100
Index : 2730
```

