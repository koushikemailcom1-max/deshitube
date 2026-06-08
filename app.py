import streamlit as st

# অ্যাপের কনফিগারেশন
st.set_page_config(page_title="বাংলাদেশী নিউজ পোর্টাল", layout="centered")

st.title("📰 বাংলাদেশের খবরের কাগজ")
st.write("এই প্ল্যাটফর্মটি শুধুমাত্র বাংলাদেশের সর্বশেষ খবর পড়ার জন্য তৈরি।")

# খবরের কাগজের তালিকা ও লিংক
news_papers = {
    "প্রথম আলো": "https://www.prothomalo.com",
    "ডেইলি স্টার": "https://www.thedailystar.net",
    "কালের কণ্ঠ": "https://www.kalerkantho.com",
    "বিডি নিউজ ২৪": "https://bdnews24.com",
    "যুগান্তর": "https://www.jugantor.com",
    "সমকাল": "https://samakal.com",
    "ইনকিলাব": "https://www.dailyinkinlab.com",
    "ইত্তেফাক": "https://www.ittefaq.com.bd"
}

# প্রতিটি পত্রিকার জন্য বাটন তৈরি করা
st.subheader("আপনার পছন্দের পত্রিকা বেছে নিন:")

for name, url in news_papers.items():
    if st.button(f"👉 {name}"):
        st.markdown(f"আপনি {name} পড়ার জন্য লিংকে ক্লিক করুন: [এখানে ক্লিক করুন]({url})")

st.divider()
st.write("দ্রষ্টব্য: এই লিংকে ক্লিক করলে আপনি সরাসরি পত্রিকার ওয়েবসাইটে চলে যাবেন।")
