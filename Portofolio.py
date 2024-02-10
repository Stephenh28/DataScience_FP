from pathlib import Path

import streamlit as st
from PIL import Image


# Set Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles"/"main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir /"assets"/"profile_pic.png"

#General Settings
PAGE_TITLE = "CV | Stephen Hendry"
PAGE_ICON = ":wave:"
NAME = "Stephen Hendry"
DESCRIPTION = """
Microsoft Dynamics AX Developer, Supporting Industry and Operational Process.
"""
EMAIL = "sh720163@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/stephen-hendry-6b5636263",
    "Instagram" : "https://www.instagram.com/stephenh_28?igsh=OGk4b2IwNjZzejR5&utm_source=qr",
    
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# st.title("Hello there!")

# Load css dan data lainnya
with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.subheader(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📃 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("✉️", EMAIL)
    
# LINKS
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("---")

# Bio
st.subheader("Bio")
st.markdown('''
    <p>Name : STEPHEN HENDRY</p>
    <p>Birth Date : 28 September 2000</p>
    <p>Gender : Male </p>
    <p>Citizenship : Indonesia</p>
    <p>Phone Number : 0813-4843-3076</p>
    ''',
    unsafe_allow_html=True
)
st.write("---")


# Education
st.write("#")
st.subheader("Education")
st.write("👨🏼‍🎓", "**Bachelor Degree of Informatic Engineering | STMIK Widya Cipta Dharma**")
st.write("09/2018 - 09/2023")
st.write("---")

# Work History
st.write("#")
st.subheader("Work Experience")
# st.write("---")

# Job 1
st.write("🖥", "**IT Hardware Staff | PT. Perusahaan Pelayaran Rusianto Bersaudara**")
st.write("04/2019 - 07/2021")
st.write(
    """
    - Eﬃcient problem solver for hardware and network issues
    - Ensuring network security and opmizing performance
    - Proven track record in resolving hardware and network Problems
    - Resolved Dynamics AX ERP errors through data entry and problem-solving
    """
)

# Job 2
st.write("💻", "**IT Supervisor | PT. Perusahaan Pelayaran Rusianto Bersaudara**")
st.write("07/2021 - Present")
st.write(
    """
    - Managed budget and administrative tasks eﬃciently
    - Implemented Microsoft Dynamics AX ERP System to streamline operations and improve productivity
    - Develop web applications using CodeIgniter and Laravel frameworks for enchanced user experience
    - Resolved all technical issues promptly, ensuring smooth functioning of hardware and software
    - Managed network, server, and hardware maintenance to optimize efficiency and reduce costs
    """
)
st.write("---")


# EXPERIENCE & QUALIFICATIONS
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✅ 4+ Years Experience in Microsoft Dynamics AX ERP and Hardware or Network Troubleshooting
    - ✅ Strong hands on experience and knowledge in X++ for Dynamics AX Development
    - ✅ Good understanding of budget planning and efficiency method
    - ✅ Fundamentals of DataScience data visualization and data prediction
    - ✅ Web Development and Troubleshooting with Laravel and CodeIgniter Framework
    """
)
st.write("---")

# Projects/Portofolio
st.write("#")
st.subheader("Courses")
st.write("- **IDN.ID (MTCNA)**")
st.write("Mar 2022")
st.write("- **ITBOX (Fullstack Web Development Beginner)**")
st.write("May 2023")
st.write("- **Sanbercode (Fullstack Web Development)**")
st.write("Oct 2023 - Present")

st.write("---")

# Skills 
st.write("#")
st.subheader("Skills")
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), X++, CodeIgniter, Laravel
    - Data Visulization: Matplotlib, Pyplot
    - Modeling: Logistic regression, linear regression
    - Databases: MySQL
    - Network : Mikrotik
    """
)
st.write("---")




# PAGE 1 CV
# PAGE 2 Portofolio