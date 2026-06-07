import streamlit as st

st.title("🇧🇩 দেশীটিউব (DeshiTube) সার্চ")

# সার্চ বক্স
query = st.text_input("আপনি কী খুঁজতে চান? (যেমন: বাংলাদেশের ইতিহাস, শিক্ষা ক্লাস)")

if query:
    # এখানে আমরা ইউটিউবের সার্চ লিংকে একটি ফিল্টার যুক্ত করে দিচ্ছি
    # এতে রেজাল্টগুলো বাংলাদেশের কনটেন্টের কাছাকাছি থাকবে
    search_url = f"https://www.youtube.com/results?search_query={query}+bangladesh+education+culture"
    
    st.write(f"অনুসন্ধানের ফলাফল দেখতে এখানে ক্লিক করুন:")
    st.markdown(f"[{query} - এর ফলাফল দেখুন]( {search_url} )")
    
    st.info("আপনার সুবিধার্থে আমরা অনুসন্ধানে 'বাংলাদেশ' ফিল্টারটি যুক্ত করে দিয়েছি।")

st.divider()
st.subheader("জনপ্রিয় ক্যাটাগরি:")
st.write("১. শিক্ষা ও ক্লাস | ২. বাংলাদেশের সংস্কৃতি | ৩. খবরের আপডেট")
