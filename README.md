# 🔐 EzSolverV2 — CAPTCHA Solving API

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)  
[![Discord](https://img.shields.io/discord/1387190222164463706?color=blue&label=Discord&logo=discord)](https://discord.gg/yourdiscordlink)  
[![API Status](https://img.shields.io/badge/API-Online-brightgreen)](http://31.214.245.63:10000)  

---

🚀 **Get Started Instantly:**  
👉 [http://31.214.245.63:10000/register](http://31.214.245.63:10000/register)

---

## 📌 Features

- ⚡ **Lightning-fast CAPTCHA solves**  
- 🔑 Unique API keys per user for secure access  
- 🎁 Free credits on signup to try the service  
- 🧠 Supports multiple CAPTCHA types: hCaptcha, reCAPTCHA v2/v3, FunCaptcha, etc.  
- 📊 Detailed usage logs and statistics per user  
- 🤖 Discord bot integration for linking accounts and checking balance  
- 💳 Simple credit-based pricing for predictable cost  
- 🔄 Easy API for integrating into your projects or bots  

---

## 💳 Pricing & Credit System

EzSolverV2 uses a **credit-based model**:

| Feature                 | Cost                           |
|-------------------------|--------------------------------|
| 🎁 **New user bonus**   | `0.500 credits` (≈ 71 solves)  |
| 🔐 **1 solve**           | `0.007 credits` (`$0.007`)      |
| 📦 **1,000 solves**      | `7.0 credits` (`$7.00`)         |
| 💳 **$1 USD**            | ≈ **143 solves**               |

- **1 credit = $1.00 USD**  
- **1 solve = 0.007 credits** (less than 1 cent per solve)  

### 🔁 Example Usage

| Credits | Approximate Solves | Cost (USD) |
|---------|---------------------|------------|
| 0.500   | ~71 (free on signup) | $0.50      |
| 1.000   | ~143                 | $1.00      |
| 5.000   | ~714                 | $5.00      |
| 10.000  | ~1,428               | $10.00     |

---

## 🧪 Quick Start

1. **Register an account:**  
   Visit 👉 [http://31.214.245.63:10000/register](http://31.214.245.63:10000/register)

2. **Get your API key:**  
   After registering, you can link your Discord via the bot command `!register` or view your key in the dashboard.

3. **Make your API requests:**  
   Use your API key with the provided endpoints to submit CAPTCHA solving tasks.

---

## 📖 API Example

**Request:**

```http
POST /api/solveCaptcha
Content-Type: application/json

{
  "clientKey": "EZK-xxxxxxx",
  "websiteURL": "https://target.com",
  "websiteKey": "sitekey-here",
  "type": "HCaptchaTask"
}

Response:
{
  "errorId": 0,
  "taskId": "f98f7dc9d6b7438bb5ef68e6d..."
}
