import streamlit as st
import string
import random
import re
import pyperclip

def calculate_password_strength(password):
    strength = 0
    remarks = []
    
    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long")
    
    # Check for uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Include at least one uppercase letter")
    
    # Check for lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Include at least one lowercase letter")
    
    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Include at least one number")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Include at least one special character")
    
    # Bonus for length
    if len(password) > 12:
        strength += 1
    
    return strength, remarks

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")
    
    st.markdown("""
        <style>
            .password-box {text-align: center; padding: 10px; background: #f4f4f4; border-radius: 10px;}
            .stTextInput > div > div > input {border-radius: 10px; padding: 10px; border: 2px solid #ddd;}
            .stButton > button {border-radius: 10px; background-color: #4CAF50; color: white; padding: 10px; transition: 0.3s;}
            .stButton > button:hover {background-color: #45a049; transform: scale(1.05);}
            .generated-password {font-weight: bold; font-size: 16px; background: #eef; padding: 10px; border-radius: 5px; text-align: center; word-break: break-all;}
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🔒 Password Strength Meter")
    st.markdown("Check the strength of your password and generate a secure one!")
    
    password = st.text_input("Enter your password", type="password")
    
    if password:
        strength, remarks = calculate_password_strength(password)
        
        # Display strength meter with colors
        st.markdown("### Strength Meter")
        st.progress(strength / 6)
        
        if strength <= 2:
            st.error("Weak password ❌")
        elif strength <= 4:
            st.warning("Moderate password ⚠️")
        else:
            st.success("Strong password ✅")
        
        # Display suggestions
        if remarks:
            st.markdown("### Password Suggestions 🛠️")
            for remark in remarks:
                st.write(f"- {remark}")
        else:
            st.success("Your password meets all security requirements! ✅")
    
    st.markdown("---")
    st.subheader("🔑 Password Requirements:")
    st.write("✔️ At least 8 characters long")
    st.write("✔️ Contains uppercase and lowercase letters")
    st.write("✔️ Contains numbers")
    st.write("✔️ Contains special characters")
    st.write("✔️ Avoid using common words or sequences")
    
    st.markdown("---")
    st.subheader("🛠️ Generate a Strong Password")
    
    password_length = st.slider("Select Password Length", min_value=8, max_value=32, value=16)
    
    if st.button("Generate Secure Password"):
        generated_password = generate_password(password_length)
        st.markdown(f"<div class='generated-password'>{generated_password}</div>", unsafe_allow_html=True)
        st.info("Copy and use this password securely!")
        
        # Copy to clipboard button
        if st.button("Copy to Clipboard"):
            pyperclip.copy(generated_password)
            st.success("Password copied to clipboard!")
    
    # Dark mode toggle
    if st.checkbox("🌙 Enable Dark Mode"):
        st.markdown("""
            <style>
                body {background-color: #121212; color: white;}
                .stTextInput > div > div > input {background-color: #333; color: white; border: 2px solid #555;}
                .stButton > button {background-color: #2196F3;}
                .stButton > button:hover {background-color: #1976D2;}
            </style>
        """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()