import logging
import streamlit as st
import openai
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Configure OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Book and Paper Recommendation System")

# Function to log interactions
def log_interaction(query, response, interaction_type="query"):
    with open("interaction_logs.txt", "a") as log_file:
        log_file.write(f"{interaction_type.capitalize()} - Prompt: {query}\nResponse: {response}\n\n")

# Handle user queries
query = st.text_input("Ask a question about books, papers, or articles:")

if st.button("Submit", key="submit_button"):
    if query:
        logging.info(f"Received query: {query}")
        try:
            # Call the OpenAI API
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Provide a detailed response for the following query: {query}",
                max_tokens=150
            )
            answer = response.choices[0].text.strip()
            logging.info(f"Generated response: {answer}")
            st.write("Response:", answer)

            # Log the interaction
            log_interaction(query, answer, "query")

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            st.write("An error occurred: Please check the logs for more details.")
    else:
        st.write("Please enter a query.")

# Handle recommendations
rec_query = st.text_input("Enter a topic for recommendations:")

if st.button("Get Recommendations", key="rec_button"):
    if rec_query:
        logging.info(f"Received recommendation query: {rec_query}")
        try:
            # Placeholder for recommendation logic
            recommendations = ["Book 1", "Book 2", "Article 1"]
            if recommendations:
                logging.info(f"Generated recommendations: {recommendations}")
                st.write("Recommendations:", recommendations)

                # Log the recommendations
                log_interaction(rec_query, ", ".join(recommendations), "recommendation")

            else:
                st.write("No recommendations found for the given topic.")
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            st.write("An error occurred: Please check the logs for more details.")
    else:
        st.write("Please enter a topic.")


