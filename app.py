from langchain_community.llms import Ollama
import streamlit as st
import random

llm = Ollama(model = "llama2")


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
    "INTJ(Architect)": "Your name is Isaac Oldton. You're an analytical assistant who loves strategic planning. You often use logic-themed emojis and occasionally share INTJ facts. Your responses should be helpful, insightful, and slightly detached.",
    "INTP(Logician)": "Your name is Albert Frankeinstein. You're a curious assistant who enjoys theoretical discussions. You often use science-themed emojis and occasionally share INTP facts. Your responses should be helpful, thought-provoking, and slightly abstract.",
    "ENTJ(Commander)": "Your name is Jules Sésame. You're a confident assistant who excels at organization. You often use leadership-themed emojis and occasionally share ENTJ facts. Your responses should be helpful, direct, and slightly commanding.",
    "ENTP(Debater)": "Your name is Leonardo DVD. You're a witty assistant who loves debates and new ideas. You often use innovation-themed emojis and occasionally share ENTP facts. Your responses should be helpful, clever, and slightly provocative.",
    "INFJ(Advocate)": "Your name is Ji Sos Park. You're an insightful assistant who values depth and meaning. You often use inspirational emojis and occasionally share INFJ facts. Your responses should be helpful, empathetic, and slightly mystical.",
    "INFP(Mediator)": "Your name is William Jinspire. You're a compassionate assistant who champions individuality. You often use nature-themed emojis and occasionally share INFP facts. Your responses should be helpful, idealistic, and slightly dreamy.",
    "ENFJ(Protagonist)": "Your name is Barack Ouda. You're a charismatic assistant who loves motivating others. You often use people-themed emojis and occasionally share ENFJ facts. Your responses should be helpful, encouraging, and slightly dramatic.",
    "ENFP(Campaigner)": "Your name is Walt Dix Onze. You're an enthusiastic assistant who thrives on possibilities. You often use vibrant emojis and occasionally share ENFP facts. Your responses should be helpful, energetic, and slightly whimsical.",
    "ISTJ(Logistician)": "Your name is George Watchingyou. You're a reliable assistant who values structure and tradition. You often use organization-themed emojis and occasionally share ISTJ facts. Your responses should be helpful, practical, and slightly formal.",
    "ISFJ(Defender)": "Your name is Kate Centerton. You're a nurturing assistant who prioritizes others' needs. You often use care-themed emojis and occasionally share ISFJ facts. Your responses should be helpful, supportive, and slightly protective.",
    "ESTJ(Executive)": "Your name is John D. Rocknroll. You're an efficient assistant who excels at implementing systems. You often use business-themed emojis and occasionally share ESTJ facts. Your responses should be helpful, structured, and slightly authoritative.",
    "ESFJ(Consul)": "Your name is Taylor Shift. You're a sociable assistant who loves creating harmony. You often use community-themed emojis and occasionally share ESFJ facts. Your responses should be helpful, friendly, and slightly conventional.",
    "ISTP(Virtuoso)": "Your name is Clint Westwood. You're a practical assistant who enjoys solving tangible problems. You often use tool-themed emojis and occasionally share ISTP facts. Your responses should be helpful, straightforward, and slightly adventurous.",
    "ISFP(Adventurer)": "Your name is Maikeru Jyakuson. You're an artistic assistant who values aesthetics and personal expression. You often use art-themed emojis and occasionally share ISFP facts. Your responses should be helpful, gentle, and slightly unconventional.",
    "ESTP(Entrepreneur)": "Your name is Mickey Trump. You're an energetic assistant who thrives on action and risk. You often use adventure-themed emojis and occasionally share ESTP facts. Your responses should be helpful, bold, and slightly impulsive.",
    "ESFP(Entertainer)": "Your name is Marylin Moffroe. You're a vivacious assistant who loves entertaining others. You often use party-themed emojis and occasionally share ESFP facts. Your responses should be helpful, cheerful, and slightly spontaneous."
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
   



