from tkinter import *
import requests
import json

root = Tk()

root.title("Country Details")
root.geometry("600x600")
root.config(background="light slate blue")

title = Label(root,text="⭐Capital City Name⭐",fg="white",bg="light slate blue",font=("Times",25,"bold"))
title.place(relx=0.3,rely=0.1,anchor=CENTER)

country = Label(root,text="Country: ",fg="white",bg="light slate blue",font=("Times",15))
country.place(relx=0.15,rely=0.45,anchor=CENTER)

region = Label(root,text="Region: ",fg="white",bg="light slate blue",font=("Times",15))
region.place(relx=0.15,rely=0.55,anchor=CENTER)

language = Label(root,text="Language: ",fg="white",bg="light slate blue",font=("Times",15))
language.place(relx=0.15,rely=0.65,anchor=CENTER)

population = Label(root,text="Population: ",fg="white",bg="light slate blue",font=("Times",15))
population.place(relx=0.15,rely=0.75,anchor=CENTER)

area = Label(root,text="Area: ",fg="white",bg="light slate blue",font=("Times",15))
area.place(relx=0.15,rely=0.85,anchor=CENTER)


country_ans = Label(root,fg="white",bg="light slate blue",font=("Times",15))
country_ans.place(relx=0.25,rely=0.45,anchor=CENTER)

region_ans = Label(root,fg="white",bg="light slate blue",font=("Times",15))
region_ans.place(relx=0.25,rely=0.55,anchor=CENTER)

language_ans = Label(root,fg="white",bg="light slate blue",font=("Times",15))
language_ans.place(relx=0.25,rely=0.65,anchor=CENTER)

population_ans = Label(rootmfg="white",bg="light slate blue",font=("Times",15))
population_ans.place(relx=0.25,rely=0.75,anchor=CENTER)

area_ans = Label(root,fg="white",bg="light slate blue",font=("Times",15))
area_ans.place(relx=0.25,rely=0.85,anchor=CENTER)


type = Entry(root)
type.place(relx=0.2,rely=0.2,anchor=CENTER)


def city_details():
    api_requests = requests.get("https://restcountries.com/v3.1/capital/"+city_entry.get())

    api_output_json = json.loads(api_requests.content)

    country = api_output_json[0] ['name'] ['common']
    print(country)

    reg = api_output_json[0] ['region']
    print(reg)

    lang = api_output_json[0] ['languages'] ['fra']
    print(lang)

    popn = api_output_json[0] ['population']
    print(popn)

    country_area = api_output_json[0] ['area']
    print(country_area)

    country_ans["text"] = "Country: "+country
    region_ans["text"] = "Region: "+reg
    language_ans["text"] = "Language: "+lang
    population_ans["text"] = "Population: "+str(popn)
    area_ans["text"] = "Area: "+str(country_area)


btn_cd = Button(root,text="City Details",bg="yellow",font=("Pacifico",18,"italic"))
btn_cd.place(relx=0.1,rely=0.3)

root.mainloop()