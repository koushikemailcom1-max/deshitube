import streamlit as st

st.set_page_config(page_title="শিক্ষা ও জ্ঞান", layout="wide")

st.title("📚 শিক্ষা ও জ্ঞানালয়")
st.write("এখানে তুমি তোমার প্রয়োজনীয় সব শিক্ষামূলক ভিডিও একসাথে পাবে।")

# শিক্ষার বিষয়ভিত্তিক ভিডিওর তালিকা
education_data = {
    "গণিত ক্লাস": [
        {"title": "প্রাথমিক গণিত", "url": "https://www.youtube.com/watch?v=উদাহরণ১"},
        {"title": "জ্যামিতি সহজপাঠ", "url": "https://www.youtube.com/watch?v=উদাহরণ২"}
    ],
    "বিজ্ঞান ও প্রযুক্তি": [
        {"title": "বিজ্ঞান পরিচিতি", "url": "https://www.youtube.com/watch?v=উদাহরণ৩"}
    ],
    "ধর্মীয় শিক্ষা": [
        {"title": "কুরআন শিক্ষা", "url": "https://www.youtube.com/watch?v=উদাহরণ৪"}
    ]
}

# প্রতিটি ক্যাটাগরি ও ভিডিও সাজানো
for category, videos in education_data.items():
    st.header(f"--- {category} ---")
    for video in videos:
        st.subheader(video["title"])
        st.video(video["url"])
