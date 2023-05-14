
# GPT Delivery
This repo is for a personal demo project on connecting Twilio and Langchain (OpenAI) to create a chatbot that works as the first contact of a burguer restaurant. Its written in `Python` and served with `Flask`. This bot can only handle text messages

### Loom
I have recorded a quick loom explaining how it works [here](https://youtu.be/uxY3__IkozM).

### What you will need
* OpenAI API key. Create an account [here](https://openai.com/) and access the key.
* You need a Twilio project, you can get `Account SID` and `Auth Token` for that project, we will need this to make requests. You can get it from [here](https://console.twilio.com/).
* Configure a Twilio whatsapp sender, and replace its Webhook URL for incoming message with https://{{your_url}}/twilio/receiveMessage
* NGROK for local testing.

### How to use it
* create a `.env` file inside the root directory, containing:
    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    TWILIO_ACCOUNT_SID=YOUR_ACCOUNT_SID
    TWILIO_AUTH_TOKEN=YOUR_AUTH_TOKEN
    FROM=whatsapp:YOUR_WHATSAPP_NUMBER_FROM_TWILIO
    ```
* create a virtual env and install the packages running
```python
pip install -r requirements.txt
```
*run the app
```python
python run.py
```
* run NGROK at the same port as the app
* set NGROK url on `Twilio WhatsApp Sandbox` 
* test using your whatsapp

# Who am I
I am `Lucas Motta`, a software developer from Brazil that is currently working on multiple personal projects using AI. From chatbots like this one, to onboarding tools that help your new employees to get a frictionless experience when joining a company.
I have a vast experience building apis, scrapers, and a variety of tools that could help your and your company to scale.

Unfortunately I cannot share the code from my client's projects, so I decided to create this one to finally answer the question:
"Can GPT really replace a human at work?"
For any work, reach me at:
* [LinkedIn]( https://www.linkedin.com/in/lucasvmotta/)
