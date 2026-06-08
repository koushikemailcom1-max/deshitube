import streamlit as st

st.set_page_config(page_title="দেশী নিউজ হাব", layout="wide")

st.title("📰 দেশী নিউজ হাব")
st.write("জাতীয়, স্থানীয় এবং সব ধরণের খবরের নির্ভরযোগ্য উৎস।")

# খবরের ক্যাটাগরি অনুযায়ী ডাটা
categories = {
    "জাতীয় খবর": ["প্রথম আলো", "বিডি নিউজ ২৪", "ইত্তেফাক"],
    "খেলাধুলা": ["ক্রিকইনফো", "ডেইলি স্টার স্পোর্টস"],
    "প্রযুক্তি": ["টেকটিউনস", "প্রযুক্তি সমকাল"],
    "বিনোদন": ["কালবেলা", "বিনোদন জগৎ"]
}

# প্রতিটি ক্যাটাগরির জন্য আলাদা ট্যাব
tabs = st.tabs(list(categories.keys()))

for i, tab in enumerate(tabs):
    with tab:
        category_name = list(categories.keys())[i]
        st.subheader(f"{category_name} - এর ওয়েবসাইটসমূহ")
        
        # প্রতিটি পত্রিকার জন্য বাটন
        for paper in categories[category_name]:
            if st.button(f"📰 {paper}", key=f"{category_name}_{paper}"):
                st.info(f"আপনি {paper} পড়ার জন্য নির্বাচিত করেছেন।")
                # এখানে পত্রিকাগুলোর মূল ইউআরএল গুলো পর্যায়ক্রমে যুক্ত করবেন
                st.write(f"পড়ার জন্য এখানে যান: [লিংক](https://www.google.com)") 

st.divider()
st.write("📢 আপনার এলাকার খবর শেয়ার করতে চাইলে আমাদের গ্রুপে যোগ দিন:")
st.link_button("👥 আমাদের নিউজ গ্রুপ", "https://www.facebook.com/groups/your_group_link")
