#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask


# In[3]:


app = Flask (__name__)


# In[4]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBS")
        pred= model.predict([[float(rates)]])
        print(pred)
        s = "The predicted DBS share price is " + str(pred[0][0])
        return (render_template("index.html", result = s))
    else:
        return(render_template("index.html", result= "2"))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1", port =int("80"))


# In[ ]:




