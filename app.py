from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Flask Routes

# Query MongoDB and pass Ma
@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars = mongo.db.collection.find_one()    
    # Return template and data
    return render_template("index.html", mars=mars)

# Call scrape function from scrape_mars.
@app.route("/scrape")
def scrape():
    
    # Run the scrape function
    mars = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)