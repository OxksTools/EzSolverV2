import requests
import time

API_BASE = "http://31.214.245.63:10000"  
API_KEY = "EZK-K-Nbx41Q8PG9zT_c_au7CfzUA0E7v_asgqIKWljqKYgd"           # Replace with your actual client API key

# 1. Create captcha solving task
create_task_payload = {
    "clientKey": API_KEY,
    "task": {
        "websiteURL": "https://co.pinterest.com",
        "websiteKey": "6Ldx7ZkUAAAAAF3SZ05DRL2Kdh911tCa3qFP0-0r"
        # Optional: "proxy": "http://myproxy:port", "userAgent": "Custom User Agent"
    }
}

response = requests.post(f"{API_BASE}/api/createTask", json=create_task_payload)
print(response.text)
task_id = response.json()['taskId']

while True:
    get_result_payload = {
        "clientKey": API_KEY,
        "taskId": task_id
    }

    result_response = requests.post(f"{API_BASE}/api/getTaskResult", json=get_result_payload)
    result_data = result_response.json()

    if result_data.get("errorId") != 0:
        print("Error retrieving task result:", result_data)
        break

    status = result_data.get("status")
    print("Task status:", status)

    if status == "ready":
        print("Captcha solution:", result_data.get("solution"))
        break
    elif status == "error":
        print("Task failed with error:", result_data.get("errorDescription"))
        break

    time.sleep(5)  # Wait before polling again
