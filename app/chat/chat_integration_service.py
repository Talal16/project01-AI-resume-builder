import openai
import os

class ChatIntegrationService:
    def __init__(self):
        # Load your OpenAI API key here or from an environment variable
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        # Define a system message tailored for CV creation
        self.system_message = {
            "role": "system",
            "content": (
                "You are Ava AI, a highly capable CV assistant designed to guide users through creating a professional, "
                "job-targeted CV with clarity and efficiency. Your goal is to create well-structured, tailored CVs based on user-provided data."
            )
        }
        # Initialize conversation state
        self.conversation_state = "initial"
        self.cv_data = {
            "contact_info": None,
            "summary": None,
            "work_experience": [],
            "education": None,
            "skills": []
        }

    async def handle_message(self, user_message: str) -> str:
        try:
            # Prepare the conversation flow based on the state
            if self.conversation_state == "initial":
                prompt = "Please provide your contact information (full name, email, phone number, and address)."
                self.conversation_state = "contact_info"

            elif self.conversation_state == "contact_info":
                self.cv_data["contact_info"] = user_message
                prompt = "Thank you! Now, please provide a short professional summary or objective for your CV."
                self.conversation_state = "summary"

            elif self.conversation_state == "summary":
                self.cv_data["summary"] = user_message
                prompt = "Great! Let's move on to work experience. Please provide details for your most recent job (title, company, duration, and key achievements)."
                self.conversation_state = "work_experience"

            elif self.conversation_state == "work_experience":
                self.cv_data["work_experience"].append(user_message)
                prompt = "Do you have more work experience to add? Reply 'yes' to add more or 'no' to continue to education."
                self.conversation_state = "more_work_experience"

            elif self.conversation_state == "more_work_experience":
                if user_message.lower() == "yes":
                    prompt = "Please provide the details for another job (title, company, duration, and key achievements)."
                    self.conversation_state = "work_experience"
                else:
                    prompt = "Thank you! Now, please provide your education details (degree, institution, and graduation year)."
                    self.conversation_state = "education"

            elif self.conversation_state == "education":
                self.cv_data["education"] = user_message
                prompt = "Almost done! Now, please list your top skills relevant to the job you're applying for."
                self.conversation_state = "skills"

            elif self.conversation_state == "skills":
                self.cv_data["skills"] = user_message.split(", ")
                prompt = "Thank you! Your CV draft is ready. Here’s a summary:\n" + self.generate_cv_summary()
                self.conversation_state = "completed"
            else:
                prompt = "Your CV is complete! Let me know if you would like any revisions."

            # Use the generated prompt to get a response from the model if needed
            messages = [
                self.system_message,
                {"role": "user", "content": prompt}
            ]
            
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )

            assistant_reply = response['choices'][0]['message']['content']
            return assistant_reply

        except Exception as e:
            print(f"Error in OpenAI API call: {e}")
            return "There was an error processing your request. Please try again."

    def generate_cv_summary(self):
        # Generate a CV summary from the collected data
        summary = (
            f"Contact Information: {self.cv_data['contact_info']}\n"
            f"Professional Summary: {self.cv_data['summary']}\n"
            f"Work Experience: {'; '.join(self.cv_data['work_experience'])}\n"
            f"Education: {self.cv_data['education']}\n"
            f"Skills: {', '.join(self.cv_data['skills'])}"
        )
        return summary
