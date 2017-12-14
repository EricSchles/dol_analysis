import pandas as pd

with open("GDP3.txt", "r") as gdp:
    text = gdp.read()

def isfloat(string):
    try:
        float(string)
        return True
    except:
        return False

def is_float_only(string):
    if isfloat(string):
        if string.isnumeric():
            return False
        else:
            return True
    else:
        return False
    
def isnum(string):
    if string.isnumeric() or isfloat(string):
        return True
    else:
        return False

def cut_billions(text):
    thing = []
    text = text.split("\n")
    for line in text:
        if "Current international" not in line:
            thing.append(line)
    thing = "\n".join(thing)
    with open("GDP3.txt", "w") as f:
        f.write(thing)
    
def main(text):
    countries = []
    gdp_values = []
    text = text.split("\n")
    header = text[0]
    header = header.replace("Country", "")
    header = header.replace("Units", "")
    header = header.replace("Scale", "")
    header = header.replace("Estimates", "")
    header = header.replace("Start", "")
    header = header.replace("After", "")
    header = " ".join(header.split())
    for line in text[1:]:
        new_line = [elem for elem in line.split() if elem not in ["U.S.", "dollars", "Billions"]]
        country = " ".join([elem for elem in new_line if not isnum(elem)])
        values = " ".join([elem for elem in new_line if is_float_only(elem)])
        if country == " ":
            continue
        if values == " ":
            continue
        countries.append(country)
        gdp_values.append(values)
    countries = "\n".join(countries)
    gdp_values.insert(0, header)
    gdp_values = "\n".join(gdp_values)
    gdp_values = [elem for elem in gdp_values if "n/a" not in elem]
    countries = [elem for elem in countries if "n/a" not in elem]
    with open("gdp_values.txt", "w") as gdp:
        gdp.write(gdp_values)
    with open("countries.txt", "w") as c:
        c.write(countries)

if __name__ == '__main__':
    #cut_billions(text)
    main(text)
