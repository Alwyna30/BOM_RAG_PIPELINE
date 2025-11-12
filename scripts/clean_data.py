import pandas as pd 
import re

df = pd.read_csv("data/raw/bom_loan_data.csv")
#print(df.head(4))

df.drop_duplicates(subset="content", inplace=True)
df.dropna(subset=["content"], inplace=True)


def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = re.sub(r'[^\x00-\x7F]+',"", text)
    text = re.sub(r'\s+', ' ',text)
    text = text.replace("Â", "").replace("©", "").replace("â","")
    
    remove_phrases = [
        "Home About Us", "Locate Us", "Careers", "Contact Us", "Skip to Content", 
        "Menu Personal", "Digital Banking", "Deposits", "Corporate", 
        "Treasury", "Accessibility Menu", "Scroll to Top", "Privacy Policy", 
        "Cookies Policy", "Disclaimer", "Sitemap", "Bank of Maharashtra never ask"
    ]

    for phrase in remove_phrases:
        text = text.replace(phrase, "")
    
    start_patterns = [
        "Features", "Benefits", "Documents", "Eligibility", "Interest", 
        "How to Apply", "FAQs", "Interest Rate"
    ]

    for pattern in start_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            text = text[match.start():]
            break
    
    return text.strip()
    
df["cleaned_content"] = df['content'].apply(clean_text)

#Keyword based cleaning
irrelevant_patterns=[
    "Home About Us", "Locate Us", "Careers", "Contact US",
    "Bank of Maharashtra never ask", "Disclaimer", "Privacy Ploicy",
    "Cookies Policy", "Sitemap", "Scroll to Top"
]

def remove_irrelevant_sections(text):
    for pattern in irrelevant_patterns:
        text = text.replace(pattern,"")
    return text

df["cleaned_content"] = df["cleaned_content"].apply(remove_irrelevant_sections)

#finding meaningful words
from collections import Counter

all_text = " ".join(df["content"].astype(str))

words = re.findall(r'\b\w+\b', all_text.lower())
common_words = Counter(words).most_common(10)
#print(common_words)

#I have kept only meaningful words in the below section

important_keywords = [
    "features", "benefits", "documents", "eligibility", "interest",
    "rate", "apply", "application", "scheme", "repayment", "tenure",
    "fees", "charges", "criteria", "loan", "car", "education", "housing"

]

def extract_relevant(text):
    lines=re.split(r'[.?!]', text)
    filtered = [
        line.strip() for line in lines
        if any(word.lower() in line.lower() for word in important_keywords)]
    return ".".join(filtered)

df["filtered_content"] = df["cleaned_content"].apply(extract_relevant)

import os
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/bom_loan_clean.csv", index=False)
print("Cleaned data saved to data/processed/bom_loan_clean.csv")

print(df.head(2))

