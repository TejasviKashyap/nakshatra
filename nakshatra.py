import streamlit as st

nakshatra = [
    'Ashwini',
'Bharani',
'Krittika',
'Rohini',
'Mrigashira',
'Ardra',
'Punarvasu',
'Pushya',
'Ashlesha',
'Magha',
'Purva Phalguni',
'Uttara Phalguni',
'Hasta',
'Chitra',
'Swati',
'Vishaka',
'Anurada',
'Jyeshta',
'Mula',
'Purva Ashadha',
'Uttara Ashadha',
'Shravana',
'Dhanishta',
'Shatabhishak',
'Purva Bhadrapada',
'Uttara Bhadrapada',
'Revati'
]

results = ['Parama Mitratare', 'Janma', 'Sampattare', 'Vipattare', 'Kshematare', 'Pratyaruktare', 'Saadhakatare', 'Vadhatare', 'Mithratare']

generalResults = {'Parama Mitratare':[], 'Janma':[], 'Sampattare':[], 'Vipattare':[], 'Kshematare':[], 'Pratyaruktare':[], 'Saadhakatare':[], 'Vadhatare':[], 'Mithratare':[]}

userNakshatra = st.selectbox('Select your Nakshatra: ', nakshatra )
presentNakshatra = st.selectbox('Select today\'s Nakshatra: ', nakshatra )

userNakshatraNum = nakshatra.index(userNakshatra)
presentNakshatraNum = nakshatra.index(presentNakshatra)



for i in range(len(nakshatra)):
    result = (27 + (i - userNakshatraNum + 1)) % 9
    tare = results[result]
    generalResults[tare].append(nakshatra[i])

if st.button('Calculate'):
    result = (27 + (presentNakshatraNum - userNakshatraNum + 1)) % 9
    st.write(' Your result is : '+results[result])
    st.subheader('Good & Bad Nakshatras:')
    st.dataframe(generalResults)
    

