import streamlit as st
import re 
  

  
def health_chatbot(user_input, health_condition):
    if health_condition == "Diabetes":
        keywords_to_check = ["Blood Pressure", "bp", "Heart Failure"]
        # do simple pattern matching for Diabetes related user queries
        if re.search(r'\b(?:I have been diagnosed with diabetes recently.Can you assist me?)\b', user_input, re.I):
            return "Of course, I'm here to help you navigate through managing diabetes. Let's start with some personalized health care"
        elif re.search(r'\b(?:How can I plan my meals to keep my blood sugar level stable?|Make a meal plan for me to keep my blood sugar level stable)\b', user_input, re.I):
            return "Focus on a balanced diet with controlled portions. Opt for whole grains, lean proteins, and plenty of vegetables. Spreading your meals throughout the day can also help maintain steady blood sugar levels."
        elif re.search(r'\b(?:what type of exercise can do?)\b', user_input, re.I):
            return "Engage in regular physical activity. Aim for at least 150 minutes of moderate-intensity exercise per week, such as brisk walking. Consult with your healthcare provider to determine a personalized exercise plan based on your health status."
        elif re.search(r'\b(?:How often should I check my blood sugar levels?)\b', user_input, re.I):
            return "Monitor your blood sugar regularly. Your target levels may vary, but generally, aim for fasting levels between 80-130 mg/dL and post-meal levels below 180 mg/dL."
        elif re.search(r'\b(?:Are there any specific medications to control Diabeties I should be aware of?)\b', user_input, re.I):
            return "Take your medications as prescribed. This may include insulin, oral medications, or both. Understand the purpose of each medication and any potential side effects. If you have concerns or experience adverse effects, inform your healthcare provider promptly."
        elif re.search(r'\b(?:How can I handle stress, and does it affect my blood sugar?)\b', user_input, re.I):
            return "Manage stress effectively. Stress can impact blood sugar levels. Practice relaxation techniques such as deep breathing, meditation, or yoga. Establish a support system to help cope with emotional challenges."
        elif re.search(r'\b(?:Can I have snacks, and if yes, what kind?)\b', user_input, re.I):
            return "Snack wisely. Opt for healthy snacks like nuts, seeds, or vegetables with hummus. Be mindful of portion sizes, and consider how snacks may affect your overall daily carbohydrate intake."
        elif re.search(r'\b(?:What should I do if my blood sugar levels are consistently high or low?)\b', user_input, re.I):
            return "Take prompt action. If your levels are consistently high or low, consult your healthcare provider. Adjust your medications or lifestyle factors as advised. Regular communication with your healthcare team is crucial."
        elif re.search(r'\b(?:How can I handle social situations, like parties or dinners, where there is a lot of food temptation?)\b', user_input, re.I):
            return "Plan ahead for social events. Eat a healthy snack before attending, so you're less tempted by unhealthy choices. Choose smaller portions, focus on vegetables and lean proteins, and be mindful of your overall carbohydrate intake."
        elif re.search(r'\b(?:Can I still enjoy sweets occasionally?)\b', user_input, re.I):
            return "Moderation is key. You can include sweets occasionally, but be mindful of portion sizes and how they fit into your overall carbohydrate intake. Consult with your healthcare provider for personalized guidance."
        elif check_keywords_regex(user_input, keywords_to_check):
            return "Please ask me about Diabetes"
        else:
            return salutations(user_input)
         
    elif health_condition == "Blood Pressure":
        keywords_to_check = ["Diabetes", "Heart Failure"]
        # do simple pattern matching for Blood Pressure related user queries
        if re.search(r'\b(?:How can I lower my blood pressure?)\b', user_input, re.I):
            return "Opt for a heart-healthy diet. Reduce sodium intake by avoiding processed foods, and focus on fruits, vegetables, whole grains, and lean proteins. This can contribute to lower blood pressure."
        elif re.search(r'\b(?:Is there a specific exercise routine that would help?)\b', user_input, re.I):
            return "Engage in regular aerobic exercise. Aim for at least 150 minutes per week, such as brisk walking or swimming. Exercise helps improve heart health and manage blood pressure."
        elif re.search(r'\b(?:How often should I monitor my blood pressure at home?)\b', user_input, re.I):
            return "Monitor regularly. Check your blood pressure at home, especially if advised by your healthcare provider. Keep a log of readings to share during your check-ups."
        elif re.search(r'\b(?:Are there specific medications I might need for managing blood pressure?)\b', user_input, re.I):
            return "Follow prescribed medications. If lifestyle changes aren't enough, your healthcare provider may recommend medications. Adhering to the prescribed regimen is essential for effective management."
        elif check_keywords_regex(user_input, keywords_to_check):
            return "Please ask me about Blood Pressure"
        else:
            return salutations(user_input)
        
    elif health_condition == "Heart Failure":
        keywords_to_check = ["Blood Pressure", "bp", "Diabetes", "blood sugar"]
        # do simple pattern matching for Heart Faliure related user queries
        if re.search(r'\b(?:How can I modify my diet to support heart failure management?)\b', user_input, re.I):
            return "Adopt a heart-healthy diet. Focus on reducing sodium intake, limit fluid retention by moderating fluid intake, and include nutrient-rich foods like fruits, vegetables, and whole grains."
        elif re.search(r'\b(?:Is exercise safe for someone with heart failure?)\b', user_input, re.I):
            return "Engage in supervised exercise. Consult your healthcare provider to create a tailored exercise plan. Activities like walking or light aerobic exercises can help strengthen the heart."
        elif re.search(r'\b(?:How does smoking impact heart failure?)\b', user_input, re.I):
            return "Quit smoking. Smoking can worsen heart failure symptoms and increase the risk of complications. Seek support to quit, and inform your healthcare provider about your efforts."
        elif re.search(r'\b(?:How can I deal with shortness of breath?)\b', user_input, re.I):
            return "Manage shortness of breath. Sit upright, use pillows to elevate your head while sleeping, and avoid extreme temperatures. Inform your healthcare provider if you experience persistent or worsening symptoms."
        elif re.search(r'\b(?:Can you suggest foods that are beneficial for heart failure?)\b', user_input, re.I):
            return "Emphasize heart-healthy nutrients. Include foods rich in potassium (e.g., bananas, oranges) and limit saturated fats. This supports overall cardiovascular health."
        elif check_keywords_regex(user_input, keywords_to_check):
            return "Please ask me about Heart Failure"
        else:
            return salutations(user_input)
    elif health_condition == "None":
        if salutations(user_input):
            return salutations(user_input)
        else:
            return "Select your preferences"
        

def salutations(user_input):
    # Simple pattern matching for user salutations queries
    if re.search(r'\b(?:hi|hello|hey|greetings)\b', user_input, re.I):
        return "Hi! I am your HealthCare chatbot, how can I help you?"
    elif re.search(r'\b(?:how are you|how are you feeling|how do you do|how are you doing)\b', user_input, re.I):
        return "I'm a chatbot.I don't have feelings, but thanks for asking!"
    elif re.search(r'\b(?:bye|see ya|goodbye|TaTa|ba ba|see ya|see you tomorrow|have a great day)\b', user_input, re.I):
        return "Goodbye! Have a great day!"
    elif re.search(r'\b(?:good morning|suba bakhair)\b', user_input, re.I):
        return "Good morning! have a good day ahead"
    elif re.search(r'\b(?:good after noon|good noon)\b', user_input, re.I):
        return "Good After noon! hope you are doing well"
    elif re.search(r'\b(?:good night!|sweet dreams)\b', user_input, re.I):
        return "Good night! have a sweet dreams"
    elif re.search(r'\b(?:thanks|thank you)\b', user_input, re.I):
            return "Your welcome! feel free ask for further assistance."
    
def check_keywords_regex(input_string, keywords):
    # Check if specific keywords are found in the input string using regular expressions.
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, keywords)) + r')\b', re.IGNORECASE)
    return bool(pattern.search(input_string))

def reset():
    st.session_state.chat_history = []
    st.session_state.pref= "None"
    
def selected():
    with st.container(): 
                for entry in st.session_state.chat_history:
                    st.markdown(f"{entry['role'].capitalize()}: {entry['message']}" )
  
def main():

    
    # Set the page title, favicon, layout, sidebar state
    st.set_page_config(
        page_title = "Health Care Chatbot App",
        page_icon = ":hospital:",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )
    
    #logo = st.image("resources/DR_bot.png")
  
    st.sidebar.title("Rule Based Chatbot")
    options = ["None", "Diabetes", "Blood Pressure", "Heart Failure"]
    st.session_state.health_condition = st.sidebar.selectbox("Select your preferances.", options,key ="pref", on_change=selected)
   
    # create a session state dictionary 
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'health_condition' not in st.session_state:
        st.session_state.health_condition = "None"

    if st.session_state.health_condition != "None": 
        # User input text box
        prompt_input = st.chat_input(f"Ask something about {st.session_state.health_condition}:")
    elif st.session_state.health_condition == "None": 
        # User input text box
        prompt_input = st.chat_input(f"Ask any health-related query")
  
   
    # Chatbot response
    if prompt_input: 
        st.session_state.chat_history.append({"role": "User", "message" : prompt_input}) 
        response = health_chatbot(prompt_input, st.session_state.health_condition)
        st.session_state.chat_history.append({"role": "Chatbot", "message" : response}) 
        if st.session_state.chat_history:
            with st.container(): 
                for entry in st.session_state.chat_history:
                    st.markdown( f"{entry['role'].capitalize()}: {entry['message']}" )


    # Button to reset the chat history and preferences
    st.sidebar.button("Reset", on_click=reset)
   
        
if __name__ == "__main__":
    main()