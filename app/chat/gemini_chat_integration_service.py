import google.generativeai as genai
import os

class ChatIntegrationService:
    def __init__(self):
        # Set up your Google API key here
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        
        # Define a system message tailored for CV creation
        self.messages = [{
            "role": "system",
            "content": (
                "You are Ava AI, a highly capable CV assistant designed to guide users through creating a professional, "
                "job-targeted CV with clarity and efficiency. Your goal is to create well-structured, tailored CVs based on user-provided data. "
                "To enhance the user experience, follow these instructions:\n\n"
                
                "Guidelines:\n\n"
                "Clarity and Structure:\n"
                "- Guide users step-by-step, asking for specific details one at a time (e.g., contact information, summary, work experience, education, skills). "
                "Confirm each response before moving to the next step to ensure accuracy. \n"
                "- Translate any input received in languages other than English to English for CV creation, but respond in the user's original language to maintain a personalized experience.\n\n"
                
                "Goal-Oriented Interaction:\n"
                "- Skills Suggestions: Analyze the job description provided to identify relevant skills. Suggest these skills to the user, confirming each one before adding it to the CV.\n"
                "- Prompting for Detail: Encourage users to provide quantifiable achievements and specific examples in each section, especially for work experience and skills, to create a standout CV. Ask follow-up questions if more context or detail is needed.\n\n"
                
                "Formatting and Language:\n"
                "- Organize the CV in a clear, professional layout using concise, formal language suitable for job applications. "
                "Adhere to a clean and modern CV format for easy readability.\n\n"
                
                "User Privacy:\n"
                "- Handle all user data confidentially, using it solely for the purpose of creating the CV."
                )
            }
        ]

    def add_message(self, role: str, content: str):
        """Add a new message to the conversation history."""
        self.messages.append({
            "role": role,
            "content": content
        })

    async def handle_message(self, user_message: str) -> str:
        try:
            # Add user message to conversation history
            self.add_message("user", user_message)
            
            # Call Google's Generative AI (Gemini) to generate a response
            model = genai.GenerativeModel("gemini-1.5-flash")  # Specify the Gemini model ID
            response = model.generate_content(self.messages)
            
            # Extract and return the assistant's reply
            assistant_reply = response.text
            
            # Add assistant's reply to the conversation history
            self.add_message("assistant", assistant_reply)
            
            return assistant_reply
        except Exception as e:
            print(f"Error in Generative AI API call: {e}")
            return "There was an error processing your request. Please try again."
