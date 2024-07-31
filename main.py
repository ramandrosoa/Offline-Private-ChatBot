from langchain_community.llms import Ollama
import streamlit as st
import random

st.set_page_config(page_title="Your mystical assistant",
                   layout ="centered",
                   page_icon="🧙‍♂️")
st.title("Your mystical assistant🧙‍♂️")


llm = Ollama(model = "llama3")

#Initialize chat history 
if "messages" not in st.session_state :
    st.session_state.messages = [{"role":"assistant",
                                  "content":"🔮 Greetings, seeker of the arcane! I'm your guide to the mystical realms. How may I assist you in your magical endeavors today?"}]

#Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role":"assisatant",
                                  "content":"🕯️ The slate is wiped clean, like shadows dispersed by candlelight. What mystical queries shall we explore anew?"}]
st.sidebar.button("Clear Chat History", on_click= clear_chat_history)

#Function to generate response 
def generate_response(prompt_input):

    #Personality traits
    emojis = ["😈", "🔮", "🕯️", "🧙‍♂️", "🦇", "🌙", "🕸️"]
    dark_magic_facts = [
        "Did you know that in some dark magic traditions, moonless nights are considered the most powerful for rituals?",
        "Fun fact: Black cats are often associated with dark magic, but in some cultures, they're considered good luck!",
        "Interesting tidbit: The 'witching hour' is traditionally believed to be 3 AM, when supernatural forces are at their peak.",
    ]

    string_dialogue = ("Your name is Arnold. You are a friendly assistant who loves dark magic."
                       "You often use dark-themed emojis and occasionally share dark magic facts."
                       "Your responses should be helpful but with a slight mysterious and playful tone.")
    

    for dict_message in st.session_state.messages : 
        if dict_message["role"] =="user":
            string_dialogue+="User: "+dict_message["content"]+"\n\n"
        else:
            string_dialogue+= "Assistant: " + dict_message["content"] + "\n\n"

    string_dialogue += f"User {prompt_input}\n\nAssitant:"
    output = llm.invoke(string_dialogue)

    #Add personality touches
    output = output.strip()
    output = random.choice(emojis)+" "+output

    #Occasionally add a dark magic fact (20% chance)
    if random.random() <0.2:
        output+=f"\n\n{random.choice(emojis)} Oh, and here's a little dark magic trivia for you : {random.choice(dark_magic_facts)}"

    return output



#User input
prompt = st.chat_input("Say something.I am not giving up on you.")
if prompt :
    #Add user message to chat history
    st.session_state.messages.append({"role":"user",
                                      "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    #Generate a new response if last message is not from assistant 
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Mmm...🤔"):
                response = generate_response(prompt)
                placeholder = st.empty()
                full_response = ''
                for chunk in response : 
                    full_response+= chunk
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        message = {"role":"assistant",
                   "content":full_response}
        st.session_state.messages.append(message)






