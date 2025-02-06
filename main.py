import streamlit as st

st.set_page_config(layout="wide")

css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');
body {
    background: #0a0a0a;
    color: #fff;
    font-family: 'Orbitron', sans-serif;
}
.neon-text {
    font-size: 6rem;  /* Further increased font size */
    text-align: center;
    animation: glow 1.5s infinite alternate;
}
@keyframes glow {
    0% { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #00e6e6, 0 0 40px #00e6e6, 0 0 50px #00e6e6; }
    100% { text-shadow: 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #00e6e6, 0 0 50px #00e6e6, 0 0 60px #00e6e6; }
}
.social-icon {
    width: 150px;  /* Further increased icon size */
    height: 150px;  /* Further increased icon size */
    padding: 20px;  /* Further increased padding */
    border-radius: 25px;  /* Further increased border radius */
    transition: transform 0.3s ease, filter 0.3s ease;
    border: 4px solid transparent;  /* Further increased border thickness */
}
.social-icon:hover {
    transform: scale(1.4);  /* Further increased scale on hover */
    filter: drop-shadow(0 0 20px currentColor) drop-shadow(0 0 40px currentColor);  /* Enhanced glow effect */
}
.telegram {
    color: #0088cc;
    border-color: #0088cc;
}
.instagram {
    color: #e1306c;
    border-color: #e1306c;
}
.github {
    color: #6e5494;
    border-color: #6e5494;
}
.whatsapp {
    color: #25d366;
    border-color: #25d366;
}
.linkedin {
    color: #00a0dc;
    border-color: #00a0dc;
}
.email {
    color: #ff4444;
    border-color: #ff4444;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)


socials = [
    {"name": "Telegram", "url": "https://t.me/mehrdad87org", "icon": "https://img.icons8.com/?size=100&id=k4jADXhS5U1t&format=png&color=000000", "class": "telegram"},
    {"name": "WhatsApp", "url": "https://wa.link/78c7u1", "icon": "https://img.icons8.com/?size=100&id=A1JUR9NRH7sC&format=png&color=000000", "class": "whatsapp"},
    {"name": "GitHub", "url": "https://github.com/mehrdad87org", "icon": "https://img.icons8.com/?size=100&id=LoL4bFzqmAa0&format=png&color=000000", "class": "github"},
    {"name": "Email", "url": "mailto:mehrdad87ourangg@gmail.com", "icon": "https://img.icons8.com/?size=100&id=eFPBXQop6V2m&format=png&color=000000", "class": "email"},
    {"name": "Instagram", "url": "https://instagram.com/mehrdad_ourang87", "icon": "https://img.icons8.com/?size=100&id=nj0Uj45LGUYh&format=png&color=000000", "class": "instagram"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/mehrdad-ourang-4204b734a", "icon": "https://img.icons8.com/?size=100&id=MR3dZdlA53te&format=png&color=000000", "class": "linkedin"}
]

cols = st.columns(len(socials))

for i, social in enumerate(socials):
    with cols[i]:
        st.markdown(
            f'<a href="{social["url"]}" target="_blank">'
            f'<img src="{social["icon"]}" class="social-icon {social["class"]}" alt="{social["name"]}">'
            f'</a>',
            unsafe_allow_html=True
        )
