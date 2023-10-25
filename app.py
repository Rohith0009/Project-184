from tkinter import *
import requests, json

root = Tk()
root.title("BBC News")
root.geometry("1600x1600")
root.configure(bg="pale turquoise")

title = Label(root, text="BBC News", bg="pale turquoise", font=("Arial", 40, "bold"))
title.place(anchor=CENTER, relx=0.5, rely=0.05)

t1 = Label(root, bg="pale turquoise", font=("Arial", 20))
d1 = Label(root, bg="pale turquoise", font=("Arial", 15))

t2 = Label(root, bg="pale turquoise", font=("Arial", 20))
d2 = Label(root, bg="pale turquoise", font=("Arial", 15))

t3 = Label(root, bg="pale turquoise", font=("Arial", 20))
d3 = Label(root, bg="pale turquoise", font=("Arial", 15))

t4 = Label(root, bg="pale turquoise", font=("Arial", 20))
d4 = Label(root, bg="pale turquoise", font=("Arial", 15))

t5 = Label(root, bg="pale turquoise", font=("Arial", 20))
d5 = Label(root, bg="pale turquoise", font=("Arial", 15))

t1.place(anchor=CENTER, relx=0.5, rely=0.15)
d1.place(anchor=CENTER, relx=0.5, rely=0.2)

t2.place(anchor=CENTER, relx=0.5, rely=0.3)
d2.place(anchor=CENTER, relx=0.5, rely=0.35)

t3.place(anchor=CENTER, relx=0.5, rely=0.45)
d3.place(anchor=CENTER, relx=0.5, rely=0.5)

t4.place(anchor=CENTER, relx=0.5, rely=0.6)
d4.place(anchor=CENTER, relx=0.5, rely=0.65)

t5.place(anchor=CENTER, relx=0.5, rely=0.75)
d5.place(anchor=CENTER, relx=0.5, rely=0.8)

api_req = requests.get(
    "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=01bdca689f5446bd915cb088b74474ca"
)
api_out = json.loads(api_req.content)

t1["text"] = api_out["articles"][0]["title"]
d1["text"] = api_out["articles"][0]["description"]

t2["text"] = api_out["articles"][1]["title"]
d2["text"] = api_out["articles"][1]["description"]

t3["text"] = api_out["articles"][2]["title"]
d3["text"] = api_out["articles"][2]["description"]

t4["text"] = api_out["articles"][3]["title"]
d4["text"] = api_out["articles"][3]["description"]

t5["text"] = api_out["articles"][4]["title"]
d5["text"] = api_out["articles"][4]["description"]

root.mainloop()
