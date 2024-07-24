# JSON: Big data sets are normally stored and extracted as JSON.
# JSON is a plain text,(object form me) but it has a formate of an object.

##Q.1) Loading the json into a dataframe:-
import pandas as pd
pb = pd.read_json('Pandas_Python_Library\data.js')
print(pb.to_string())

##Q.2) Dictonary as a JSON: if your JSON code is not in a file, but in a python dictonary, yhen you can all below:-
import pandas as pd
data = {
    "Duration":{
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":45,
        "5":60,
   },
    "Pulse":{
        "0":110,
        "1":117,
        "2":103,
        "3":109,
        "4":117,
        "5":102,
   },
  "Maxpulse":{
        "0":130,
        "1":145,
        "2":135,
        "3":175,
        "4":148,
        "5":127,
   },
  "Calories":{
        "0":409.1,
        "1":479.0,
        "2":340.0,
        "3":282.4,
        "4":406.0,
        "5":300.5,
   }
}
pbnew = pd.DataFrame(data)
print(pbnew)