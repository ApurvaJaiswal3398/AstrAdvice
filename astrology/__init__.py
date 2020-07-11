from flask import Flask
from flask_bcrypt import Bcrypt
import pymongo

app = Flask(__name__)
app.config['SECRET_KEY'] = '8946d71d0200e86083be400cb72e4700'

crypt = Bcrypt(app)     # For Encrypting Passwords

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection['Astrology']        # Database
Users = db['Users']                 # Collection (or Table) to store User Details
Dh = db['DailyHoroscope']           # Collection to store Daily Horoscope Details
Ast = db['Astrologers']             # Collection to store Astrologers' Details

dhdata = [
    {
        '_id': 'Aries',
        'profession': 'Plan ahead, be more organized in your finances, if troubles develop, don’t despair and take some actions. Aries natives are now put to the test, but fear not, there’s no other road but upward, things will pick up in the near future.',
        'luck': 'Fortune smiles on you today. You shall be able to achieve anything with your dedication.',
        'emotions': 'This is likely to be a time of considerable frustration and discouragement for you. Your confidence level will decrease.',
        'health': 'Your health status is heading in the right direction, keep steering down this course, it takes some effort but the rewards will come. Positive influences should be felt by natives of Aries, your strength is likely to go up and new projects can be started.',
        'love': 'Love is just the factor that might brighten your day, as the horoscope inclines to show, this factor is going for the better in spite of a rocky past. A visible improvement of your personal life is very likely today for Aries natives, having all the signs of a good day ahead in this sector.',
        'travel': 'Today is unfavorable for traveling. It would be advisable to avoid making trips. But if it’s too imperative, then travel with care.'
    },
    {
        '_id': 'Taurus',
        'profession': 'Times are changing, this is the sensation left out by today, an improvement in your capital should follow shortly. Maybe your finances have not been living up to your expectations for a while now but as far as this day is concerned Taurus native are likely to be advantaged.',
        'luck': 'Your luck will favor you today – especially in matters of wealth and fortune.',
        'emotions': 'You will move ahead with renewed vigor and confidence and achieve even the seemingly impossible tasks. Your heart will guide you in the right direction.',
        'health': 'Your health state, fitness level and overall well being status is likely to see a good improvement today. Positive influences should be felt by natives of Taurus, your strength is likely to go up and new projects can be started.',
        'love': 'This day is set out to fulfill your demanding nature, keep an open mind, embrace new people and all will go for the better. Perseverance may be rewarding, your love life is set to flourish, improvements are announced in all aspects of your personal life.',
        'travel': 'Be alert and avoid haste and carelessness while traveling.'
    },
    {
        '_id': 'Gemini',
        'profession': 'Some unexpected costs could be on the horizon, so save up so as not to be very affected if this happens. The cost of living may seem like something that keep adding up, living you little room to have fun or relax.',
        'luck': 'Today is one of your terrible days; nothing will seem to work right. Luck is not in your favor.',
        'emotions': 'Today you are more sensitive than other days. Watching comedy movies will uplift your emotions on positive side.',
        'health': 'Try and devise a long term plan regarding your health and well-being in general terms, then try and stick to it. You are ambitions, you can move past impediments with some attention to details and perseverance.',
        'love': 'Keep on the way that you have chosen, you should start noticing small improvements in your personal life. You might be after a period of uneasy calmness in terms of your personal life, time for you to take charge of things.',
        'travel': 'Today is not at all a good time for traveling. You may have to roam about aimlessly – without gaining any results. This shall result in loss of time and stamina.'
    },
    {
        '_id': 'Cancer',
        'profession': 'Your revenue management is something that requires more attention from your part, even if things pop-up to be on a positive slope, don’t let your guard down. Bills are slowly beginning to fade from your everyday habits and you might think of new investments, some for your own pleasure.',
        'luck': "Even though your luck is good, be modest and don't exceed your abilities.",'emotions': 'Keep a check on your emotions. A short journey with your family or friends will give peace and happiness.',
        'health': 'Keep your guard up, your overall health state may take some hits today, time for some changes in diet and habits. Its not easy to get on a route of healthy living, but you have to start now, try and not postpone it further.',
        'love': 'Better things are about to show up at the horizon, this day may prove to be a day of change for natives of Cancer. The horoscope for the day is full of optimism, good energy and enthusiasm in regards to your love life.',
        'travel': 'If possible, cancel all your tours for the time being as they may prove harmful or unfruitful.'
    },
    {
        '_id': 'Leo',
        'profession': 'If possible, cancel all your tours for the time being as they may prove harmful or unfruitful.',
        'luck': 'Your luck is not in your favor, so you are advised not to take any risks.',
        'emotions': 'Watch your words else you might end up hurting your loved ones. Due to illness, you might feel emotionally upset for no reason. Chances of reacting in an erratic manner are likely.',
        'health': 'This is a day in which you have to pay greater attention to the smaller things, try and get fitter, eat healthier so your immunity may deal with any threat. The horoscopes inclines for a change, a change that in terms of health will be one for the better.',
        'love': 'Most likely this will be a day in which your diplomatic abilities will be put to the test. Take caution, your Leo horoscope of the day advises attention to details in regards to your personal life.',
        'travel': 'Some impediments can postpone your trips. Even if you do travel, you will have to face discomfort and problems.'
    },
    {
        '_id': 'Virgo',
        'profession': 'Caution is advice by the horoscope for today, cut back on irrelevant expenses and pay consideration to deals that sound to good to be true. Prudence may not always be a strong characteristic of Virgo when it comes to financial matters but you have to take charge and stay strong, better days are ahead.',
        'luck': 'Some good news, for which you might be waiting eagerly for a long time, may arrive.',
        'emotions': 'You shall feel the urge to retrospect and change for good. Do not let minor things affect your emotions as they will no longer survive.',
        'health': 'Your health status is heading in the right direction, keep steering down this way, it takes some effort but the rewards will come. Positive influences should be felt by natives of Virgo, your strength is likely to go up and new projects could be started.',
        'love': 'You could have the feeling that your search has no end, stay positive, surround yourself with enthusiastic people, your Virgo horoscope recommends you to try new things. Long lasting relationships are tested, but the more stable they are, the easier it is to overcome obstacles.',
        'travel': 'Today is favorable for official trips. You will have a successful travel plan.'
    },
    {
        '_id': 'Libra',
        'profession': 'Changes up ahead for Libra natives are likely to happen today, with a bit of luck and prudence they will be for the better. Optimism should characterize your day throughout, better things are still to come so be patient, your financial status should improve.',
        'luck': 'You will be lucky today. You will be successful in whatever you wish to pursue.',
        'emotions': 'A sense of peace and happiness will prevail. With optimistic approach you will be motivated to apply your creativity in your profession and personal life.',
        'health': 'A feeling of general discomfort could accompany your morning, you most likely cant put your finger on whet that is precisely. You are ambitions, you might move past impediments with some consideration to details and perseverance.',
        'love': 'A day in which your personal life looks strong in the perspective of your horoscope, new relationships or consolidations of long lasting ones are very likely. Libra natives are set out to have a fulfilling day, hopes and aspirations can come true if you pursue them.',
        'travel': 'Trips with friends and family to nature spots will most likely make you more energetic and lively.'
    },
    {
        '_id': 'Scorpio',
        'profession': 'Reward should be the word of the day, although past weeks might have you thinking that there is no end to financial issues, today might prove a day of optimism. Have faith in your abilities and press on with your work no matter what, money is an element that is in a constructive astrological box today.',
        'luck': 'You may be surprised what today has in store for you as you meet some new and interesting people who will make a mark on your life.',
        'emotions': 'You will be experiencing unusual positive changes right now, which are changing your attitudes and feelings towards others.',
        'health': 'Your health state, fitness level and overall well being status is likely to see a good improvement today. Positive influences should be felt by natives of Scorpio, your strength is likely to go up and new projects may be started.',
        'love': 'New liaison are likely for today, chances of getting to know the true nature of some people are very high. Differences between you and a loved one might fade away, and a fresh start to that bond could prove beneficial for all sides involved.',
        'travel': 'You will feel like socializing and being friendly. You may take up a sudden journey today.'},
    {
        '_id': 'Sagittarius',
        'profession': 'Your budget status should take a turn for the better is we analyze today’s Sagittarius horoscope in detail. Your state of mind will have an influence on its own over this day and even on your finances, time to get up and be more productive.',
        'luck': 'A good day for financial gains against your investments.',
        'emotions': 'You need to control your emotions and avoid doing anything that could deteriorate the situation. You will be very short-tempered today.',
        'health': 'Remain attentive, small issues might occur in terms of your health, there is nothing to worry to much, no serious illness just things that might cause you discomfort. Reflect on the decisions that you made in the past, especially the last few weeks and draw some conclusions from that.',
        'love': 'Sagittarius will start the day off with the feeling that all is the same but steady but surely, as the day passes, the horoscope shows an improvement will arise. It’s not recommended to withdraw, surround yourself with energetic people and follow they example.',
        'travel': 'Travel, only if you must. Don’t get friendly with strangers.'
    },
    {
        '_id': 'Capricorn',
        'profession': 'Your luck should take a turn for the better, hidden traps could arise but with wisdom you can navigate easily through them. Advantages are set to spring up for you, new opportunities and an increase of income from your daily routine as well.',
        'luck': 'Today is an auspicious and promising day for all kinds of activities, be it personal or professional.',
        'emotions': 'Happiness will fill you up for the entire day. You are feeling rather good and it seems that you can place the pulse of success easily.',
        'health': 'Todays planetary alignment incline to suggest a cautionary approach in terms of your overall physical well-being. Make some changes in your diet, consider eating out less and approach home cooked food even if your time is limited, its benefits are worth it.',
        'love': 'This day should take a turn for the better in regards to your love and relationship life, not a dramatic and fast change but a stable long lasting process. Dont let life slip through your hands, its time to take charge and impose your own rules.',
        'travel': 'Short distance travels will bring you the desired benefits both in personal and professional life.'
    },
    {
        '_id': 'Aquarius',
        'profession': 'Your revenue management is something that requires more attention from your part, even if things appear to be on an effective slope, don’t let your guard down. No abrupt changes are likely to happen today, stay alert and warn off any attempts to spend on thing you don’t really need.',
        'luck': 'Luck favors your today. You will be able to fulfill your wishes and dreams with minimum efforts.',
        'emotions': 'Today is the cheerful day to spend with your friends and family. You can go on outings with your partner.',
        'health': 'More discipline in your habits is likely to bring you long term benefits, improving your life altogether. Your body is your temple, try and have more caution in dealing with every day events that may impact your health.',
        'love': 'Most likely this will be a day in which your diplomatic abilities will be put to the test. Your Aquarius horoscope for this day, in regards to our love life looks complicated to say the least, patience and perseverance is needed.',
        'travel': 'A family trip to a place of religious significance is likely. The trip is likely to make you more active, energetic and serene.'
    },
    {
        '_id': 'Pisces',
        'profession': 'Some new and interesting developments may be ahead for you in terms of money and job opportunities, try and take advantage of them. Your state of mind, will have an influence of its own over this day and even on your finances, time to get up and be more productive.',
        'luck': 'Today is your lucky day. You shall get a sudden windfall gain or an old investment will bring huge profits.',
        'emotions': 'You can be especially motivated now to apply a creative vision to your work as well as personal life. You sense of happiness will be heightened.',
        'health': 'This is a day in which you have to pay greater attention to the smaller things, try and get fitter, eat healthier so your immunity can deal with any challenge. Your body is your temple, try and have more caution in dealing with every day events that can impact your health.',
        'love': 'Your Pisces horoscope places all the stars in your favor today, you should embrace the day, new connections and relationships are on the horizon. Try and get more out of every encounter, you can never know where a new and important person may step into your life.',
        'travel': 'You might go on an unexpected tour today. Enjoy the journey.'
    }
]
Dh.delete_many({})
x = Dh.insert_many(dhdata)
# print('The Data inserted for : ',x.inserted_ids)

astrodata = [
    {
        '_id': 1,
        'astroname': 'Santosh Shastri',
        'full_name': 'Santosh Shastri',
        'field': 'Vedic Astrology, Nadi Astrology',
        'language': 'English, Hindi',
        'experience': 10,
        'charges': 40,
        'customers': 1652,
        'image_file': '../static/images/Astrologers/santosh-shastri.png',
        'mobile': '9696453934'
    },
    {
        '_id': 2,
        'astroname': 'Acharya AK Mishra',
        'full_name': 'Ajay Kumar Mishra',
        'field': 'Vedic Astrology, Vasthu',
        'language': 'Hindi',
        'experience': 19,
        'charges': 40,
        'customers': 4163,
        'image_file': '../static/images/Astrologers/ajay-kumar-mishra.png',
        'mobile': '6085830763'
    },
    {
        '_id': 3,
        'astroname': 'Astro Poonam',
        'full_name': 'Poonam Gulati',
        'field': 'Numerology, Tarot Reading',
        'language': 'English, Hindi',
        'experience': 7,
        'charges': 60,
        'customers': 1134,
        'image_file': '../static/images/Astrologers/poonam-gulati.png',
        'mobile': '6663699985'
    },
    {
        '_id': 4,
        'astroname': 'Tarot Victor',
        'full_name': 'Victor',
        'field': 'Tarot Reading, Psychic Reader',
        'language': 'English, Hindi',
        'experience': 12,
        'charges': 50,
        'customers': 589,
        'image_file': '../static/images/Astrologers/victor.png',
        'mobile': '9513653229'
    },
    {
        '_id': 5,
        'astroname': 'Nishant Kanade',
        'full_name': 'Nishant Kanade',
        'field': 'Numerology, Tarot Reading',
        'language': 'Hindi',
        'experience': 11,
        'charges': 15,
        'customers': 4072,
        'image_file': '../static/images/Astrologers/nishant-kanade.png',
        'mobile': '7515688007'
    },
    {
        '_id': 6,
        'astroname': 'Astro Bharti',
        'full_name': 'Bharti',
        'field': 'Vedic Astrology, Numerology',
        'language': 'English, Hindi',
        'experience': 16,
        'charges': 50,
        'customers': 1588,
        'image_file': '../static/images/Astrologers/bharti.png',
        'mobile': '8509707980'
    },
    {
        '_id': 7,
        'astroname': 'Moneka Kocher',
        'full_name': 'Moneka Kocher',
        'field': 'Vedic Astrology, Vasthu',
        'language': 'English, Hindi, Punjabi, Sanskrit',
        'experience': 15,
        'charges': 40,
        'customers': 2948,
        'image_file': '../static/images/Astrologers/moneka-kocher.png',
        'mobile': '7394615063'
    },
    {
        '_id': 8,
        'astroname': 'Acharya Ganesh',
        'full_name': 'Ganesh Sharma',
        'field': 'Vedic Astrology, Prashana Astrology',
        'language': 'Hindi',
        'experience': 17,
        'charges': 30,
        'customers': 3544,
        'image_file': '../static/images/Astrologers/ganesh-sharma.png',
        'mobile': '6890633572'
    },
    {
        '_id': 9,
        'astroname': 'Dr. Ram Naresh Tripathi',
        'full_name': 'Dr. Ram Naresh Tripathi',
        'field': 'Vedic Astrology, Vasthu',
        'language': 'Hindi',
        'experience': 25,
        'charges': 100,
        'customers': 4106,
        'image_file': '../static/images/Astrologers/dr.-ram-naresh-tripathi.png',
        'mobile': '9219983243'
    },
    {
        '_id': 10,
        'astroname': 'Astro Anil',
        'full_name': 'Anil Verma',
        'field': 'Vedic Astrology, Numerology',
        'language': 'English, Hindi, Punjabi',
        'experience': 22,
        'charges': 88,
        'customers': 5187,
        'image_file': '../static/images/Astrologers/anil-verma.png',
        'mobile': '6370389981'
    },
    {
        '_id': 11,
        'astroname': 'Acharya Arun',
        'full_name': 'Arun Shastri',
        'field': 'Vedic Astrology, Medical Astrology',
        'language': 'Hindi, Sanskrit',
        'experience': 24,
        'charges': 36,
        'customers': 6508,
        'image_file': '../static/images/Astrologers/arun-shastri.png',
        'mobile': '8816365070'
    },
    {
        '_id': 12,
        'astroname': 'Acharya Shipra Kaushik',
        'full_name': 'Shipra Kaushik',
        'field': 'Vedic Astrology, Tarot Reading',
        'language': 'Hindi',
        'experience': 15,
        'charges': 50,
        'customers': 10988,
        'image_file': '../static/images/Astrologers/shipra-kaushik.png',
        'mobile': '6677724700'
    },
    {
        '_id': 13,
        'astroname': 'Acharya Sudhir Kaushik',
        'full_name': 'Sudhir Kaushik',
        'field': 'Vedic Astrology, Tarot Reading',
        'language': 'English, Hindi',
        'experience': 15,
        'charges': 50,
        'customers': 7658,
        'image_file': '../static/images/Astrologers/sudhir-kaushik.png',
        'mobile': '6804021178'
    },
    {
        '_id': 14,
        'astroname': 'Sanjeev Anand',
        'full_name': 'Sanjeev Anand',
        'field': 'Vedic Astrology, Nadi Astrology',
        'language': 'Hindi',
        'experience': 23,
        'charges': 100,
        'customers': 7164,
        'image_file': '../static/images/Astrologers/sanjeev-anand.png',
        'mobile': '7619850916'
    },
    {
        '_id': 15,
        'astroname': 'Astro Sumit',
        'full_name': 'Sumit',
        'field': 'Vedic Astrology, Tarot Reading',
        'language': 'English, Hindi',
        'experience': 10,
        'charges': 40,
        'customers': 2453,
        'image_file': '../static/images/Astrologers/sumit.png',
        'mobile': '7996312130'
    },
    {
        '_id': 16,
        'astroname': 'Acharya Shridhar',
        'full_name': 'Shridhar Tripathi',
        'field': 'Vedic Astrology, Vasthu',
        'language': 'Hindi',
        'experience': 17,
        'charges': 30,
        'customers': 5487,
        'image_file': '../static/images/Astrologers/shridhar-tripathi.png',
        'mobile': '9190889384'
    },
    {
        '_id': 17,
        'astroname': 'Acharya Rajkumar',
        'full_name': 'Rajkumar Pandey',
        'field': 'Vedic Astrology, Gemology',
        'language': 'Hindi',
        'experience': 16,
        'charges': 30,
        'customers': 6853,
        'image_file': '../static/images/Astrologers/rajkumar-pandey.png',
        'mobile': '9879851022'
    },
    {
        '_id': 18,
        'astroname': 'Acharya Shailendra',
        'full_name': 'Shailendra Jha',
        'field': 'Vedic Astrology, Prashana Astrology',
        'language': 'English, Hindi',
        'experience': 13,
        'charges': 33,
        'customers': 8767,
        'image_file': '../static/images/Astrologers/shailendra-jha.png',
        'mobile': '6813035640'
    },
    {
        '_id': 19,
        'astroname': 'Tarot Diya',
        'full_name': 'Diya',
        'field': 'Numerology, Tarot Reading',
        'language': 'English, Hindi',
        'experience': 7,
        'charges': 50,
        'customers': 2029,
        'image_file': '../static/images/Astrologers/diya.png',
        'mobile': '6627054797'
    },
    {
        '_id': 20,
        'astroname': 'Acharya Durgesh',
        'full_name': 'Durgesh',
        'field': 'Vedic Astrology, Vasthu',
        'language': 'Hindi',
        'experience': 23,
        'charges': 20,
        'customers': 1775,
        'image_file': '../static/images/Astrologers/durgesh.png',
        'mobile': '6386823912'
    },
    {
        '_id': 21,
        'astroname': 'Sandeep Yati',
        'full_name': 'Sandeep Yati',
        'field': 'Vedic Astrology, Palmistry',
        'language': 'English, Hindi, Bengali',
        'experience': 28,
        'charges': 50,
        'customers': 5199,
        'image_file': '../static/images/Astrologers/sandeep-yati.png',
        'mobile': '7699203967'
    },
    {
        '_id': 22,
        'astroname': 'Acharya Mukesh',
        'full_name': 'Mukesh Chandra',
        'field': 'Vedic Astrology, KP Astrology',
        'language': 'Hindi, Sanskrit',
        'experience': 16,
        'charges': 28,
        'customers': 11150,
        'image_file': '../static/images/Astrologers/mukesh-chandra.png',
        'mobile': '7634893687'
    },
    {
        '_id': 23,
        'astroname': 'Acharya Satyesh Pandey (Kartik)',
        'full_name': 'Satyesh Pandey (Kartik)',
        'field': 'Vedic Astrology, Gemology',
        'language': 'Hindi',
        'experience': 18,
        'charges': 30,
        'customers': 14496,
        'image_file': '../static/images/Astrologers/satyesh-pandey-(kartik).png',
        'mobile': '8662034429'
    },
    {
        '_id': 24,
        'astroname': 'Acharya Purushottam',
        'full_name': 'Purushottam Sharma',
        'field': 'Vedic Astrology, Prashana Astrology',
        'language': 'Hindi',
        'experience': 16,
        'charges': 30,
        'customers': 8188,
        'image_file': '../static/images/Astrologers/purushottam-sharma.png',
        'mobile': '6814012523'
    },
    {
        '_id': 25,
        'astroname': 'RK Sharma',
        'full_name': 'RK Sharma',
        'field': 'Vedic Astrology, Tarot Reading',
        'language': 'English, Hindi',
        'experience': 21,
        'charges': 48,
        'customers': 4421,
        'image_file': '../static/images/Astrologers/rk-sharma.png',
        'mobile': '9433627383'
    },
    {
        '_id': 26,
        'astroname': 'Acharya Saroj',
        'full_name': 'Madhvi Saroj Gupta',
        'field': 'Vedic Astrology, Tarot Reading',
        'language': 'English, Hindi, Punjabi',
        'experience': 6,
        'charges': 36,
        'customers': 3795,
        'image_file': '../static/images/Astrologers/madhvi-saroj-gupta.png',
        'mobile': '6884635663'
    },
    {
        '_id': 27,
        'astroname': 'Astro Basant',
        'full_name': 'Basant Shastri',
        'field': 'Vedic Astrology, Face Reading',
        'language': 'Hindi',
        'experience': 16,
        'charges': 20,
        'customers': 11335,
        'image_file': '../static/images/Astrologers/basant-shastri.png',
        'mobile': '9969546682'
    },
    {
        '_id': 28,
        'astroname': 'Lakshmi Shankar Shukla',
        'full_name': 'Lakshmi Shankar Shukla',
        'field': 'Vedic Astrology, Prashana Astrology',
        'language': 'Hindi',
        'experience': 31,
        'charges': 50,
        'customers': 2265,
        'image_file': '../static/images/Astrologers/lakshmi-shankar-shukla.png',
        'mobile': '9683940970'
    },
    {
        '_id': 29,
        'astroname': 'Dr, Rekha Rathi',
        'full_name': 'Dr. Rekha Rathi',
        'field': 'Tarot Reading, Psychic Reader',
        'language': 'English, Hindi, Punjabi, Bengali',
        'experience': 21,
        'charges': 111,
        'customers': 4657,
        'image_file': '../static/images/Astrologers/dr.-rekha-rathi.png',
        'mobile': '7385741801'
    },
    {
        '_id': 30,
        'astroname': 'Acharya Brijesh',
        'full_name': 'Brijesh',
        'field': 'Vedic Astrology, Nadi Astrology',
        'language': 'English, Hindi, Telugu, Kannada, Sanskrit',
        'experience': 13,
        'charges': 60,
        'customers': 809,
        'image_file': '../static/images/Astrologers/brijesh.png',
        'mobile': '6848391785'
    },
    {
        '_id': 31,
        'astroname': 'Swami Chinamani',
        'full_name': 'Swami Chintamani',
        'field': 'Vedic Astrology',
        'language': 'Hindi',
        'experience': 18,
        'charges': 40,
        'customers': 1768,
        'image_file': '../static/images/Astrologers/swami-chintamani.png',
        'mobile': '7849409178'
    },
    {
        '_id': 32,
        'astroname': 'C Kannan',
        'full_name': 'Chidambaram Kannan',
        'field': 'Vedic Astrology, Nadi Astrology',
        'language': 'English, Hindi, Tamil, Marathi, Gujarati',
        'experience': 13,
        'charges': 38,
        'customers': 8994,
        'image_file': '../static/images/Astrologers/chidambaram-kannan.png',
        'mobile': '8049518622'
    },
    {
        '_id': 33,
        'astroname': 'Acharya Namita',
        'full_name': 'Namita Sinha',
        'field': 'KP Astrology, Tarot Reading',
        'language': 'English, Hindi, Bengali',
        'experience': 10,
        'charges': 60,
        'customers': 2680,
        'image_file': '../static/images/Astrologers/namita-sinha.png',
        'mobile': '7852000205'
    },
    {
        '_id': 34,
        'astroname': 'Sweta Sinha',
        'full_name': 'Sweta Sinha',
        'field': 'Vedic Astrology, Progeny Astrology',
        'language': 'Hindi',
        'experience': 9,
        'charges': 30,
        'customers': 3594,
        'image_file': '../static/images/Astrologers/sweta-sinha.png',
        'mobile': '9297697627'
    },
    {
        '_id': 35,
        'astroname': 'Astro Simranjit',
        'full_name': 'Simranjit Singh',
        'field': 'Tarot Reading',
        'language': 'English, Hindi, Punjabi',
        'experience': 9,
        'charges': 25,
        'customers': 1509,
        'image_file': '../static/images/Astrologers/simranjit-singh.png',
        'mobile': '8231708513'
    },
    {
        '_id': 36,
        'astroname': 'Acharya  Anil Shastri',
        'full_name': 'Anil Shastri',
        'field': 'Vedic Astrology, Vasthu',
        'language': 'Hindi',
        'experience': 13,
        'charges': 24,
        'customers': 5066,
        'image_file': '../static/images/Astrologers/anil-shastri.png',
        'mobile': '9690275861'
    },
    {
        '_id': 37,
        'astroname': 'Astro Sangeeta',
        'full_name': 'Sangeeta Kumar',
        'field': 'Vedic Astrology, Prashana Astrology',
        'language': 'English, Hindi, Punjabi',
        'experience': 6,
        'charges': 28,
        'customers': 7253,
        'image_file': '../static/images/Astrologers/sangeeta-kumar.png',
        'mobile': '8197288804'
    },
    {
        '_id': 38,
        'astroname': 'Vinod Guru',
        'full_name': 'Vinod Guru',
        'field': 'Vedic Astrology, Vasthu',
        'language': 'Hindi, Sanskrit',
        'experience': 9,
        'charges': 18,
        'customers': 3661,
        'image_file': '../static/images/Astrologers/vinod-guru.png',
        'mobile': '9739729119'
    },
    {
        '_id': 39,
        'astroname': 'Acharya Brajbhushan',
        'full_name': 'Brajbhushan',
        'field': 'Vedic Astrology, Vasthu',
        'language': 'Hindi, Gujarati',
        'experience': 15,
        'charges': 30,
        'customers': 2261,
        'image_file': '../static/images/Astrologers/brajbhushan.png',
        'mobile': '9552478617'
    },
    {
        '_id': 40,
        'astroname': 'Sanjay Kumar Mishra',
        'full_name': 'Sanjay Kumar Mishra',
        'field': 'Vedic Astrology, Vasthu',
        'language': 'Hindi',
        'experience': 16,
        'charges': 20,
        'customers': 4791,
        'image_file': '../static/images/Astrologers/sanjay-kumar-mishra.png',
        'mobile': '6779100485'
    },
    {
        '_id': 41,
        'astroname': 'Mystic Akarshan',
        'full_name': 'Akarshan',
        'field': 'Western Astrology, Tarot Reading, Psychic Reader',
        'language': 'English, Hindi',
        'experience': 19,
        'charges': 70,
        'customers': 4647,
        'image_file': '../static/images/Astrologers/akarshan.png',
        'mobile': '7300132267'
    },
    {
        '_id': 42,
        'astroname': 'Astro Swati',
        'full_name': 'Swati',
        'field': 'Numerology, Tarot Reading, Palmistry, Face Reading',
        'language': 'Hindi',
        'experience': 7,
        'charges': 26,
        'customers': 1681,
        'image_file': '../static/images/Astrologers/swati.png',
        'mobile': '6637516218'
    }
]
Ast.delete_many({})
x = Ast.insert_many(astrodata)
# print('The Data inserted for : ',x.inserted_ids)

from astrology import routes