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
@app.route('/citation_table', methods=['POST'])
def citation_table():
  search_citation = request.form['search_citation']
  search_citation_list = search_citation.strip().split(",")
  r = requests.get('https://api.elsevier.com/content/search/scopus?query=ref('+search_citation_list[1]+')%20and%20ref('+search_citation_list[0]+')%20and%20ref('+search_citation_list[2]+')&apiKey=2e4b9d6d318ee089e673e46b3f38493b')
  # https://api.elsevier.com/content/search/scopus?query=ref('+search_citation_list[1]+')%20and%20ref('+search_citation_list[0]+')%20and%20ref('+search_citation_list[2]+')&apiKey=2e4b9d6d318ee089e673e46b3f38493b
  json_object = r.json()
  citation_number = json_object['search-results']['opensearch:totalResults']
  #dictTuple = ((search_citation_list[1], "author"), (search_citation_list[0], "title"), (search_citation_list[2], "year"), (citation_number, "citations"))
  data = [{
  "author": search_citation_list[1],
  "title": search_citation_list[0],
  "year": search_citation_list[2],
  "citations": citation_number
}]
  
  #dataStr = str(dictTuple)

  #d = collections.OrderedDict()
  #data = dict((y, x) for x, y in dictTuple)
  return render_template("citations_table.html",
    data=data, 
    columns=columns, 
    title='Citations Table')  

"""
data = [{
  "author": "bootstrap-table",
  "title": "10",
  "year": "122",
  "citations": "An extended Bootstrap table"
}]
"""
'''
  return render_template("citations_table.html",
    data=data, 
    columns=columns, 
    title='Citations Table')	

  for ele in search_citation_list:
    search_citation_str = " "
    search_citation_str.join(ele)

'''

if __name__ == '__main__':
	app.run()