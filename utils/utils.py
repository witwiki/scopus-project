# A python utilities module for excel wranging

import pandas as pd



# # Reads excel file from the path
# def readFile(file_format):
# 	if file_format is 'xlsx' or 'xlx':
# 		pass
# 	elif file_format == '.csv':
# 		pass
# 	else:
# 		print('wrong format') 	

# 	return fileRed

xlsFile = pd.ExcelFile(r'C:\Users\vicku\Anaconda3\envs\scopus-project\scopus-app\data\ScopusAPITest.xlsx')
# print(xlsFile)

# Gets the sheet names from the excel files
xlsFile.sheet_names
# print(xlsFile.sheet_names)


# Parses file into a DataFrame
df = xlsFile.parse('Sheet1')
# print(df)

# Drops all NaN values from row (axis=0)
noNanDf = df.dropna(axis=0, how='all')
# print(noNanDf)

# xlsFile.sheet_names
# def readData():
	
# Convert DataFrame to dictionary
df2dict = noNanDf.to_dict()
# print(df2dict)
# print(df2dict['Author'][0])

# for x in df2dict:
# 	# print(df2dict['Author'][x])
# 	# perform API request call with str array elements (author[1], title[0] and year[2])
# 	r = requests.get('https://api.elsevier.com/content/search/scopus?query=ref('+search_citation_list[1]+')%20and%20ref('+search_citation_list[0]+')%20and%20ref('+search_citation_list[2]+')&apiKey=2e4b9d6d318ee089e673e46b3f38493b')


for colName in df2dict:
	# print(df2dict[colName])
	if colName == 'Author':
		for element in df2dict[colName]:
			# author = {}
			author = df2dict[colName][element]
		print(author)
	# if colName == 'Title':
	# 	for element in df2dict[colName]:
	# 		print(df2dict[colName][element])
	# if colName == 'Year':
	# 	for element in df2dict[colName]:
	# 		print(df2dict[colName][element])



# for x in df2dict['Year']:
# 	print(df2dict['Year'][x])



# if __name__ == '__main__':
# 	main()