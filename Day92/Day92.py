# Day 92 Challenge

import requests
from flask import Flask


app = Flask(__name__)

timezone = "GMT"
latitude = 51.5002
longitude = -0.1262

weather_codes = {
  "0" : "Clear sky, no clouds visible",
  "4": "Visibility reduced by smoke, e.g. veldt or forest fires, industrial smoke or volcanic ashes",
  "5": "Haze",
  "6": "Widespread dust in suspension in the air, not raised by wind",
  "9": "Duststorm or sandstorm",
  "10": "Mist",
  "13": "isible lightning, but no thunder yet",
  "16": "It's gonna rain somewhere near you",
  "17" : "Thunderstorm, but no rain",
  "18" : "Squalls",
  "19" : "Funnel clouds",
  "22" : "Light snowfall",
  "25" : "Rain shower",
  "26" : "Snow shower, or a mix of rain & snow shower",
  "27" : "Hail shower, or a mix of rain & hail shower",
  "28": "Fog / Ice Fog",
  "29": "Thunderstorm (with or without rain)",
  "40" : "Fog or ice fog at a distance",
  "41" : "Fog or ice fog in patches",
  "76": "Diamond dust (with or without fog)",
  "77" :"Snow grains (with or without fog)",
  "78": "Isolated star-like snow crystals (with or without fog)",
  "79": "Ice pellets",
  "82" : "Violent rain shower(s)",
  "95" : "Thunderstorm, slight or moderate, without hail,but with rain and/or snow",
  "96": "Thunderstorm, slight or moderate, with hail",
  "97": "Thunderstorm, heavy, without hail, but with rain and/or snow",
  "98": "	Thunderstorm combined with duststorm or sandstorm",
  "99": "Thunderstorm, heavy, with hail"
}

for key in ["1", "2","3"]:
  weather_codes[key] = """Partly coudy, sky is unchanged as a whole, & clouds are either forming or disappearing"""

for key in ["7","8"]:
  weather_codes[key] = """Dust or sand raised by wind at or near you,or well developed dust whirl(s) or sand whirl(s) seen at or you during in the past hour"""

for key in ["11","12"]:
  weather_codes[key] = """Shallow fog or ice fog"""

for key in ["15","14"]:
  weather_codes[key] = "Expected to rain, could be at a distance from you(about 5 km)"

for key in ["20","21"]:
  weather_codes[key] = "Drizzle, light rain or snow grains"

for key in ["23","24"]:
  weather_codes[key] = "Freezing drizzle/rain, may or may not accompanied with snow or ice pellets"

for key in ["30","31","32"]:
  weather_codes[key] = "Slight or moderate duststorm or sandstorm"

for key in ["33","34","35"]:
  weather_codes[key] = "Severe duststorm or sandstorm"

for key in ["36","38"]:
  weather_codes[key] = "Slight or moderate blowing snow, could be low/high"

for key in ["37","39"]:
  weather_codes[key] = "Heavy drifting snow, could be low/high"

for key in ["42","44","46"]:
  weather_codes[key] = "Fog or ice fog, sky visible"

for key in ["43","45","47"]:
  weather_codes[key] = "Fog or ice fog, sky invisible"

for key in ["42","43"]:
  weather_codes[key] += " and the fog has become thinner"

for key in ["44","45"]:
  weather_codes[key] += " and there hasn't been any appreciable change in the fog"

for key in ["46","47"]:
  weather_codes[key] += " and the fog has begun or getting to become thicker"

for key in ["48","49"]:
  weather_codes[key] = "Fog, depositing rime, sky can be visible or invisible"

for key in ["50","51","60","61","70","71"]:
  weather_codes[key] = "Slight"

for key in ["52","53","62","63","72","73"]:
  weather_codes[key] = "Moderate"

for key in ["54","55","64","65","74","75"]:
  weather_codes[key] = "Heavy (Dense)"

for key in ["50","52","54"]:
  weather_codes[key] = " drizzle, not freezing, intermittent"

for key in ["51","53","55"]:
  weather_codes[key] = " drizzle, not freezing, continuous"

for key in ["60","62","64"]:
  weather_codes[key] = " rain, not freezing, intermittent"

for key in ["61","63","65"]:
  weather_codes[key] = " rain, not freezing, continuous"

for key in ["70","72","74"]:
  weather_codes[key] = " intermittent fall of snowflakes"

for key in ["71","73","75"]:
  weather_codes[key] = " continuous fall of snowflakes"

for key in ["56","57"]:
  weather_codes[key] = "Drizzle & freezing, could be slight, moderate or heavy"

for key in ["58","59"]:
  weather_codes[key] = "Drizzle & rain, could be slight, moderate or heavy"

for key in ["66","67"]:
  weather_codes[key] = "Rain & freezing, could be slight, moderate or heavy"

for key in ["68","69"]:
  weather_codes[key] = "Rain or drizzle & snow, could be slight, moderate or heavy"

for key in ["70","71"]:
  weather_codes[key] = "Slight "

for key in ["72","73"]:
  weather_codes[key] = "Moderate "

for key in ["74","75"]:
  weather_codes[key] = "Heavy "

for key in ["70","72","74"]:
  weather_codes[key] = "intermittent fall of snowflakes"

for key in ["71","75","73"]:
  weather_codes[key] = "continuous fall of snowflakes"

for key in ["80","81","82"]:
  weather_codes[key] = "Slight, Moderate or Heavy rain shower(s)"

for key in ["83","84"]:
  weather_codes[key] = "Slight, Moderate or Heavy shower(s) of rain and snow mixed"

for key in ["85","86"]:
  weather_codes[key] = "Slight, Moderate or Heavy snow shower(s)"

for key in ["87","88"]:
  weather_codes[key] = "Slight, Moderate or Heavy shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed"

for key in ["89","90"]:
  weather_codes[key] = "Slight, Moderate or Heavy shower(s) of hail, with or without rain or rain and snow mixed, not associated with thunder"

for key in ["91","92"]:
  weather_codes[key] = "Slight, Moderate or Heavy rain, and thunderstorm during the preceding hour"

for key in ["93","94"]:
  weather_codes[key] = "Slight, Moderate or Heavy rain or/and snow or hail, and thunderstorm during the preceding hour"

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()

weather_code = str(user["daily"]["weathercode"][0])


max_temp = f"🥵 : {user['daily']['temperature_2m_max'][0]}"

min_temp = f"🥶 : {user['daily']['temperature_2m_min'][0]}"

temp = f"{max_temp}  {min_temp}"

@app.route('/')
def index():
  f = open("template/html/weather.html","r")
  page = f.read()
  f.close()
  page = page.replace("{weather}",weather_codes[weather_code])
  page = page.replace("{temp}",temp)
  
  url = ""
  if weather_code == "0": 
    url = "https://media1.tenor.com/m/L4rosl2oeG4AAAAd/clear-sky-no-clouds.gif"
    
  elif 1<=int(weather_code)<4:
    url = "https://media.tenor.com/_mO9zQsDjKwAAAAM/tauben-nebel.gif"

  elif 4<=int(weather_code)<8:
    url = "https://tenor.com/view/fog-smoke-mystery-gif-14830316.gif"

  elif 8<=int(weather_code)<10:
    url= "https://media.tenor.com/YOnJvnjvmsIAAAAM/mad-max-sand-storm.gif"

  elif 10<=int(weather_code)<13:
    url ="https://media.tenor.com/DTp0irTS_WgAAAAM/foggy-fog.gif"

  elif 13<=int(weather_code)<17:
    url="https://media.tenor.com/Skj1cFlDFmsAAAAM/lightning-storm.gif"

  elif 17<=int(weather_code)<20:
    url="https://media.tenor.com/FACj-DgV2dMAAAAM/tornado-viralhog.gif"

  elif 20<=int(weather_code)<25:
    url="https://media.tenor.com/ixUbTxnyD2wAAAAM/damla-dropping.gif"

  elif 25<=int(weather_code)<27 or 80<=int(weather_code)<83 or 91<=int(weather_code)<95:
    url="https://media.tenor.com/DYJfoYgJbFwAAAAM/shummer-rainfall.gif"

  elif 27<=int(weather_code)<29:
    url="https://media.tenor.com/EBPJwGhAlTkAAAAM/souronesss.gif"

  elif weather_code == "29" or 95<=int(weather_code)<98 or 87<=int(weather_code)<89:
    url="https://media.tenor.com/YmZl-fJFjTMAAAAM/storm.gif"

  elif 30<=int(weather_code)<36:
    url="https://media.tenor.com/ly68T2PnHzgAAAAM/the-storm.gif"

  elif 36<=int(weather_code)<40 or 83<=int(weather_code)<87:
    url="https://media.tenor.com/OsrzwLe4KvkAAAAM/snowstorm-primal-survivor.gif"

  elif 40<=int(weather_code)<50:
    url = "https://media.tenor.com/hN8ma5kfmF0AAAAM/fog-mountains.gif"

  elif 50<=int(weather_code)<56:
    url="https://media.tenor.com/Twl-lCp6QqoAAAAM/rain-aesthetic.gif"

  elif 56<=int(weather_code)<59:
    url="https://media.tenor.com/w1SOc9LzLhAAAAAM/snowing-winter.gif"

  elif 59<=int(weather_code)<68:
    url="https://reneedezvous.wordpress.com/wp-content/uploads/2013/07/rain-gif.gif"

  elif 68<int(weather_code)<70:
    url="https://media.tenor.com/nXDbAHh2NF0AAAAM/winter-is-here-snow-storm.gif"

  elif 70<=int(weather_code)<76:
    url="https://media.tenor.com/iZIPcW8cMCMAAAAM/snow-plow.gif"

  elif 76<=int(weather_code)<79:
    url="https://media.tenor.com/c73ilc7btrAAAAAM/craciun.gif"

  elif weather_code == "79":
    url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQaYNaSOnYd7Kmxqjpume6luk6TmV3MMZUEg&usqp=CAU"

  elif 89<=int(weather_code)<91:
    url="https://media.tenor.com/RO0pokQ2mwgAAAAM/hail-hail-storm.gif"

  elif weather_code == "98":
    url="https://i.gifer.com/Ux3z.gif"

  elif weather_code == "99":
    url="https://cloudfront-us-east-1.images.arcpublishing.com/gmg/NIKADMYL4FEZFHI3OFPXM5PW34.gif"
    
  page = page.replace("{url}",url)
  return page


app.run(host='0.0.0.0', port=81)
