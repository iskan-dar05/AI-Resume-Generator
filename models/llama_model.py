from groq import Groq
import os

def generate_cv(job_description):
	client = Groq(
		api_key=os.environ.get("GROQ_API_KEY")
		)

	chat_completion = client.chat.completions.create(
		messages = [
		{
			"role": "system",
			"content": f"""You are an expert resume writer. Based on the job description below and user prompt, generate a professional resume for a candidate named John Doe."""
		},
		{
			"role": "user",
			"content": f"""Create resume base on {job_description} and {user_prompt}
			The resume should include:
			- Name
			- Contact Info
			- Professional Summary
			- Relevant Skills
			- Work Experience (3+ years)
			- Education
			- Certifications

			Keep it concise, professional, and tailored to the job description.
			"""
		}	
		],
		model="llama-3.3-70b-versatile"
	)
	return chat_completion.choices[0].message.content



