import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# st.text(fruityvice_response.json())

fv_dt = st.dataframe(date=fruityvice_response.json(), use_container_width=True)
