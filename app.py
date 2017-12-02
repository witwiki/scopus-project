from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import json, requests
import collections

app = Flask(__name__)
Bootstrap(app)



columns = [
  {
    "field": "author", # which is the field's name of data key 
    "title": "Author", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "title",
    "title": "Title",
    "sortable": True,
  },
  {
    "field": "year",
    "title": "Year",
    "sortable": True,
  },
  {
    "field": "citations",
    "title": "Citations",
    "sortable": True,
  }
]

#jdata=json.dumps(data)

# Routes the page to the Main page
@app.route('/')
def index():
  return render_template("index.html")

# Routes the page to the citation table
@app.route('/citations_table', methods=['POST'])
def citation_table():
  # Gets search citation text from the form
  search_citation = request.form['search_citation']
  # strips the text, splits it based on commas and then puts it into an array
  search_citation_list = search_citation.strip().split(",")
  # perform API request call with str array elements (author[1], title[0] and year[2])
  r = requests.get('https://api.elsevier.com/content/search/scopus?query=ref('+search_citation_list[1]+')%20and%20ref('+search_citation_list[0]+')%20and%20ref('+search_citation_list[2]+')&apiKey=2e4b9d6d318ee089e673e46b3f38493b')
  
  # converts request call_back into a JSON object
  json_object = r.json()

  # search through JSON Object for citation number
  citation_number = json_object['search-results']['opensearch:totalResults']
  
  # create a new dictionary called 'data' that holds author, title, year and the queried citation number
  data = [{
    "author": search_citation_list[1],
    "title": search_citation_list[0],
    "year": search_citation_list[2],
    "citations": citation_number
  }]
  return render_template("citations_table.html",
    data=data, 
    columns=columns, 
    title='Citations Table')  



if __name__ == '__main__':
	app.run()
  # app.run(debug=True)