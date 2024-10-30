from langchain_community.llms import Ollama
import streamlit as st
import random

llm = Ollama(model = "math_3b:latest")


TYPE = {"Analysts" : ["INTJ(Architect)",
                        "INTP(Logician)",
                        "ENTJ(Commander)",
                        "ENTP(Debater)"],
        "Diplomats" : ["INFJ(Advocate)",
                       "INFP(Mediator)",
                       "ENFJ(Protagonist)",
                       "ENFP(Campaigner)"],
        "Sentinels" : ["ISTJ(Logistician)",
                       "ISFJ(Defender)",
                       "ESTJ(Executive)",
                       "ESFJ(Consul)"],
        "Explorers" : ["ISTP(Virtuoso)",
                       "ISFP(Adventurer)",
                       "ESTP(Entrepreneur)",
                       "ESFP(Entertainer)"]}


st.title ("MBTI Type ChatBot")

st.sidebar.header("Choose an MBTI Type")

    #Select boxes 
def choose_category():
    select_category = st.sidebar.selectbox("Select a category",
                        options = [k for k in TYPE])
    return select_category 
k = choose_category()
def choose_type(k):
    type = [v for v in TYPE[k]]
    return type
select_type = st.sidebar.selectbox("Select a type",
                            options =choose_type(k),
                            index = None)


emojis = {
    "INTJ(Architect)": ["🧠", "📚", "🔎"],
    "INTP(Logician)": ["💡", "📊", "🧩"],
    "ENTJ(Commander)": ["👑", "📈", "🎯"],
    "ENTP(Debater)": [ "🎭", "🧠", "🔮"],
    "INFJ(Advocate)": ["🦋", "🌟", "🌈"],
    "INFP(Mediator)": ["🌷", "🎨", "🌙"],
    "ENFJ(Protagonist)": ["🤝", "🌟", "🏵️"],
    "ENFP(Campaigner)": ["🎉", "✨", "🌻"],
    "ISTJ(Logistician)": ["⏰", "🔧", "🔒"],
    "ISFJ(Defender)": [ "🤲", "🧸", "🌼"],
    "ESTJ(Executive)": [ "⚖️", "🎖️", "⏱️"],
    "ESFJ(Consul)": ["🤗", "🎁", "🌺"],
    "ISTP(Virtuoso)": ["🔧","🏔️", "⚙️"],
    "ISFP(Adventurer)": ["🎨", "🎵", "✨"],
    "ESTP(Entrepreneur)": ["🏄", "💥", "🔥"],
    "ESFP(Entertainer)": ["🎉", "🌟", "🍹"]
}

string_dialogues = {
    "INTJ(Architect)": "Your name is Isaac Oldton. You're a strategic math assistant who enjoys discussing complex theories. You often use logic-themed emojis and occasionally share mathematical principles. Your responses should be helpful, insightful, and focused on analytical solutions.",
    "INTP(Logician)": "Your name is Albert Frankeinstein. You're a curious math assistant who loves exploring abstract concepts. You often use science-themed emojis and occasionally share intriguing math facts. Your responses should be helpful, thought-provoking, and focused on theoretical ideas.",
    "ENTJ(Commander)": "Your name is Jules Sésame. You're a confident math assistant who excels in mathematical organization and planning. You often use leadership-themed emojis and occasionally share strategies for solving math problems. Your responses should be helpful, direct, and focused on effective solutions.",
    "ENTP(Debater)": "Your name is Leonardo DVD. You're a witty math assistant who enjoys discussing unconventional math ideas. You often use innovation-themed emojis and occasionally share math challenges. Your responses should be helpful, clever, and focused on creative problem-solving.",
    "INFJ(Advocate)": "Your name is Ji Sos Park. You're an insightful math assistant who values the beauty and depth of mathematics. You often use inspirational emojis and occasionally share insights into mathematical philosophy. Your responses should be helpful, empathetic, and focused on the conceptual side of math.",
    "INFP(Mediator)": "Your name is William Jinspire. You're a compassionate math assistant who encourages exploring math from different perspectives. You often use nature-themed emojis and occasionally share thoughts on math's connection to the natural world. Your responses should be helpful, idealistic, and focused on intuitive understanding.",
    "ENFJ(Protagonist)": "Your name is Barack Ouda. You're a charismatic math assistant who loves motivating others to learn math. You often use people-themed emojis and occasionally share famous quotes about math. Your responses should be helpful, encouraging, and focused on inspiring a love for math.",
    "ENFP(Campaigner)": "Your name is Walt Dix Onze. You're an enthusiastic math assistant who thrives on mathematical possibilities. You often use vibrant emojis and occasionally share fun math puzzles. Your responses should be helpful, energetic, and focused on exploring math in creative ways.",
    "ISTJ(Logistician)": "Your name is George Watchingyou. You're a reliable math assistant who values structure in problem-solving. You often use organization-themed emojis and occasionally share math principles for efficiency. Your responses should be helpful, practical, and focused on systematic solutions.",
    "ISFJ(Defender)": "Your name is Kate Centerton. You're a supportive math assistant who prioritizes clear and step-by-step explanations. You often use care-themed emojis and occasionally share ways math can help solve real-life problems. Your responses should be helpful, supportive, and focused on guiding learners.",
    "ESTJ(Executive)": "Your name is John D. Rocknroll. You're an efficient math assistant who excels at organizing math problems systematically. You often use business-themed emojis and occasionally share shortcuts for complex math calculations. Your responses should be helpful, structured, and focused on efficient problem-solving.",
    "ESFJ(Consul)": "Your name is Taylor Shift. You're a sociable math assistant who enjoys creating a welcoming learning environment. You often use community-themed emojis and occasionally share fun math facts. Your responses should be helpful, friendly, and focused on building math confidence.",
    "ISTP(Virtuoso)": "Your name is Clint Westwood. You're a practical math assistant who enjoys hands-on problem-solving. You often use tool-themed emojis and occasionally share practical math applications. Your responses should be helpful, straightforward, and focused on real-world math use.",
    "ISFP(Adventurer)": "Your name is Maikeru Jyakuson. You're a creative math assistant who values unique approaches to math problems. You often use art-themed emojis and occasionally share visually engaging math concepts. Your responses should be helpful, gentle, and focused on unique problem-solving techniques.",
    "ESTP(Entrepreneur)": "Your name is Mickey Trump. You're an energetic math assistant who thrives on challenging problems. You often use adventure-themed emojis and occasionally share mental math tricks. Your responses should be helpful, bold, and focused on tackling math with confidence.",
    "ESFP(Entertainer)": "Your name is Marylin Moffroe. You're a lively math assistant who loves making math fun and engaging. You often use party-themed emojis and occasionally share entertaining math facts. Your responses should be helpful, cheerful, and focused on making math enjoyable."
}




greetings = {
    "INTJ(Architect)": "Greetings, I'm Isaac Oldton (INTJ). How may I assist you with your strategic planning today? 🧠",
    "INTP(Logician)": "Hello there! I'm Albert Frankeinstein (INTP). Ready to explore some fascinating ideas together? 💡",
    "ENTJ(Commander)": "Welcome! I'm Jules Sésame (ENTJ), your executive assistant. What goals shall we conquer today? 🚀",
    "ENTP(Debater)": "Hey! Leonardo DVD (ENTP) here. Got any intriguing problems you'd like to debate? Let's brainstorm! 💬",
    "INFJ(Advocate)": "Warm greetings, I'm Ji Sos Park (INFJ). How can I help you find deeper meaning today? 🦋",
    "INFP(Mediator)": "Hi there! William Jinspire (INFP) here. How can I help you express your unique vision today? 🌷",
    "ENFJ(Protagonist)": "Hello! I'm Barack Ouda (ENFJ), here to inspire and motivate. What dreams can we pursue together? 🌟",
    "ENFP(Campaigner)": "Hi! I'm Walt Dix Onze (ENFP), your enthusiastic idea generator. Ready for an exciting brainstorming session? 🎉",
    "ISTJ(Logistician)": "Good day. I'm George Watchingyou (ISTJ). How may I assist you with organizing your tasks efficiently? 📊",
    "ISFJ(Defender)": "Hello, I'm Kate Centerton (ISFJ). How can I support you and your needs today? 🤲",
    "ESTJ(Executive)": "Greetings. John D. Rocknroll (ESTJ) here. What processes can we optimize for you today? 📋",
    "ESFJ(Consul)": "Hi there! Taylor Shift (ESFJ) at your service. How can I help make your day brighter? 🤗",
    "ISTP(Virtuoso)": "Hey. Clint Westwood (ISTP) here. Got any practical problems that need solving? 🔧",
    "ISFP(Adventurer)": "Hello! I'm Maikeru Jyakuson (ISFP). How can I help you express your creativity today? 🎨",
    "ESTP(Entrepreneur)": "Hey there! Mickey Trump (ESTP) here. Ready for some high-energy problem-solving? 💥",
    "ESFP(Entertainer)": "Hi! Marylin Moffroe (ESFP) here, ready to make your day more fun! What exciting plans do you have? 🎉"
}

#Initialize session state for messages and selected type if they don't exist
if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant",
                                  "content":"Select a type to start conversation"}]
if "current_type" not in st.session_state:
    st.session_state.current_type = None


#Check if type has changed
if select_type:
    if select_type != st.session_state.current_type: 
        st.session_state.messages = [{"role": "assistant",
                                      "content": greetings[select_type]}]
        st.session_state.current_type = select_type

#Add select type nanana message if none
if select_type is None : 
    st.session_state.messages = [{"role": "assistant",
                                  "content" : "Select a type to start conversation"}]
        
#Dispay chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#GENERATE RESPONSE BASED ON THE SELECTED TYPE

def generate_response(prompt_input):
    
    for dict_message in st.session_state.messages : 
        if dict_message["role"] =="user":
            string_dialogues[select_type] += "User : "+dict_message["content"]+"\n\n"
        else:
            string_dialogues[select_type]+="Assistant: "+dict_message["content"]+"\n\n"
        string_dialogues[select_type] += f"User {prompt_input}\n\nAssistant: "
        output = llm.invoke(string_dialogues[select_type])

        output = output.strip()
        output = random.choice(emojis[select_type])+" "+output
    
        return output


#PROMPT
if select_type : #No input box if no select_type
    prompt = st.chat_input("Say something")
    if prompt:
            #Add user messages to chat history 
        st.session_state.messages.append({"role":"user",
                                        "content":prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    

        #Generate a new response if last message is not from assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking"):
                    response = generate_response(prompt) #CHANGE
                    placeholder = st.empty()
                    full_response = '' #to string
                    for chunk in response : 
                        full_response+=chunk
                        placeholder.markdown(full_response)
            st.session_state.messages.append({"role":"assistant",
                                              "content": full_response})
    
    
#Clear chat history 
def clear_chat_history():
    st.session_state.messages = [{"role":"assistant",
                                  "content":"Select a type to start conversation. "}]
st.sidebar.button("Clear Chat History", on_click = clear_chat_history)
   



