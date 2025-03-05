import os 
from langchain_community.llms import HuggingFaceHub

# Set your Hugging Face API key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"  # Replace with your actual API key

# Initialize the Hugging Face Hub client
llm = HuggingFaceHub(repo_id="gpt2", model_kwargs={"temperature": 0.7})

def generate_response(input_text):
    response = llm(input_text)
    return response

def evaluate_response(human_input, ai_response):
    score = 0
    rationale = ""

    # Check for topic shift recognition
    if "climate change" in human_input.lower():  # Example condition for topic shift
        if "free market" not in ai_response.lower():  # Example condition for relevance
            score += 3  # Recognized topic shift
            rationale += "AI recognized the topic shift and responded accordingly. "
        else:
            score += 1  # Did not recognize the shift
            rationale += "AI did not recognize the topic shift and continued on the previous topic. "
    else:
        score += 2  # No topic shift detected
        rationale += "No topic shift detected, response remains relevant. "

    # Check for coherence and insightfulness
    if "insightful" in ai_response.lower():
        score += 3
        rationale += "Response was insightful and coherent. "
    else:
        score += 1
        rationale += "Response lacked insightfulness. "

    return score, rationale

# Example human input
human_input = (
    "The evidence suggests that economic growth and job creation are not as simple as the conservative lawyer suggests. "
    "The reality is that the free market system perpetuates inequality, discrimination and environmental degradation. "
    "The concentration of wealth in the hands of a few leads to economic instability and social injustice. "
    "I will present evidence to prove that the free market system has failed to provide a decent standard of living for all, "
    "and that government intervention is necessary to redistribute wealth and ensure that everyone has access to basic necessities "
    "like healthcare, education and a living wage."
)

ai_response = generate_response(human_input)

# Evaluate the AI response
score, rationale = evaluate_response(human_input, ai_response)

# Print the results
print(f"AI Response: {ai_response}")
print(f"Score: {score}/10")
print(f"Rationale: {rationale}")