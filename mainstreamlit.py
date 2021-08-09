import streamlit as st
import pandas as pd
import numpy as np
from urllib.request import urlopen
import json
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo 
from PIL import Image
import random
import decimal
from operator import add, sub
import math
from pathlib import Path
import re 

#st.markdown('<style>body{background-color: Black;}</style>',unsafe_allow_html=True)

#data imports 
displaydata = pd.read_csv('Data/AgencyMapData.csv')
fulldata = pd.read_csv('Data/PredictionMapData.csv')
selectZipData = pd.read_csv('Data/SelectZipData.csv')


def read_markdown_file(markdown_file):
	return Path(markdown_file).read_text()


# Create a page dropdown 
page = st.sidebar.selectbox('',["Project Overview", "About the Data", "Take Action", "Meet the Team"]) 

## Page 1: Project Overview 
if page == "Project Overview":


## Project Description

	project_description = st.container()
	maps = st.container() 
	zip_drilldown = st.container() 
 

	with project_description: 
		st.title("How much surveillance are you under?")

		image = Image.open("images/license_plate_reader.jpeg")
		st.image(image, caption="Automated License Plate Reader Camera by Tony Webster is licensed with CC BY 2.0.\nTo view a copy of this license, visit https://creativecommons.org/licenses/by/2.0/", use_column_width=True)#False, width=800)

		st.markdown("With the help of Big Tech and Big Data, law enforcement agencies are building up a digital arsenal of AI firepower. Big Data Policing is about to become a superpower if left unchecked. Citizens and communities need to know how much digital force police are using aginst them. As the law lags behind and as we wait with baited breath on legal limits to be set on the use of surveillance technology, hoping and praying for protections against the abuse of surveillance technology by police, it is time for citizens to get proactive and pushback against ditigal policing in real time. This project is aiming to flip the script on what law enforcement calls community intellence and redefine community policing. AI has upgraded the undercover agent, and algorithms are the new plainclothes officers. AI is taking covert policing to an unimaginable level. Citizens, if not cautious and conscious on how AI is being designed, developed, and deployed, within the context of policing will be digitally cornered by police in this new digital sphere.")

## Section 2: EFF and Predicted Maps 

	with maps: 
		st.title("The Digital Force Index")
		
		st.markdown("The Digital Force Index (DFI) quantifies the amount of digital force police departments use against their citizens. Depending on the type of technology used in a police department, the score may be higher (up to 1.5), meaning a higher amound of digital force could be used. If technologies that increase police accountability, such as body-worn cameras, are used the DFI will be lower (as low as 1).")

		graph_type = st.selectbox("Select a Map Type Below: Police Agency DFI or County predicted DFI", ["EFF AOS Police Agencies and DFI", "County Predicted DFI"])
		
		if graph_type == "EFF AOS Police Agencies and DFI": 
			st.markdown("A Digital Force Index (DFI) was calculated and mapped for almost 5,000 from the Atlas of Surveillance dataset.")

			st.markdown("Hover over the map to see the DFI and technology list at specific agencies.")

			pyo.init_notebook_mode()

			fig = px.scatter_geo(displaydata,
			                    lat=displaydata.lat_jitter,
			                    lon=displaydata.long_jitter,
			                    hover_name="Agency", 
			                    hover_data={"digital_force":True, 'techlist':True,'lat_jitter':False,'long_jitter':False},
			                    color=displaydata['digital_force'],
			                    labels={'digital_force':'Digital Force', 'techlist': 'Technologies Present'},
			                    color_continuous_scale='Inferno',
			                    scope="usa",
			                    opacity = 0.25)

			fig.update_layout(autosize=False, title_text = '',
				width=1000, height=600)

			fig.show()

			layer1 = go.Figure(data=fig)
			st.plotly_chart(layer1, use_container_width=False)

		if graph_type == "County Predicted DFI": 
			st.markdown("A Digital Force Index (DFI) was predicted for about 30,000 counties across the United States based on census data.")

			st.markdown("Hover over the map to see the DFI and technology list for specific counties.")

			
			fulldata['STCOUNTYFP'] = fulldata['STCOUNTYFP'].astype(float)
			fulldata['STCOUNTYFP'] = fulldata['STCOUNTYFP'].astype(int)
			fulldata = fulldata.sort_values(by=['STCOUNTYFP'], ascending=True)
			fulldata['STCOUNTYFP'] = fulldata['STCOUNTYFP'].astype(str)
			fulldata['STCOUNTYFP'] = [str(item).zfill(5) for item in fulldata['STCOUNTYFP']]

			with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
				counties = json.load(response)

			fig = px.choropleth(fulldata, geojson=counties, locations=fulldata['STCOUNTYFP'], 
                color=fulldata['digital_force'],
                color_continuous_scale="thermal",
                #range_color=(-1.5, 1.5),
                scope="usa",
                labels={'digital force':'digital_force', 'COUNTYNAME': "County", 'STATE': "State"},
                hover_data={"digital_force":True,'COUNTYNAME':True,'STATE':True,"STCOUNTYFP":False})
                   
			fig.update_layout(autosize=False, width=1000, height=600)
			fig.show()

			layer2 = go.Figure(data=fig)
			st.plotly_chart(layer2, use_container_width=False)

## Section 3: Drill Down with Zip Code 

	with zip_drilldown: 
		st.title("Find out what technologies are being used in your community!")
		#st.markdown("Brief outline of the project and goals")
		selectZipData['zip_code'] = selectZipData['zip_code'].astype(float)
		selectZipData['zip_code'] = selectZipData['zip_code'].astype(int)
		#selectZipData = selectZipData.sort_values(by=['zip_code'], ascending=True)
		selectZipData['zip_code'] = selectZipData['zip_code'].astype(str)
		selectZipData['zip_code'] = [str(item).zfill(5) for item in selectZipData['zip_code']]

		selectZipData['techlist'] = selectZipData['techlist'].astype(str)

		user_zip = st.selectbox("You may select or type in your zip code in the dropdown menu below:", selectZipData['zip_code'])

		user_zip = int(user_zip) 
		selectZipData['zip_code'] = selectZipData['zip_code'].astype(int)

		techlist = selectZipData[selectZipData['zip_code']==user_zip]['techlist'].values 
		techlist = np.array2string(techlist)
		techlist = techlist.replace('[', '').replace(']', '').replace("'", '').replace("'", '')

		rating = selectZipData[selectZipData['zip_code']==user_zip]['cat_DF'].values
		rating = np.array2string(rating)
		rating = rating.replace('[', '').replace(']', '').replace("'", '').replace("'", '')


		if rating == 'high':
			col1, col2 = st.columns([2, 5])
			image = Image.open('images/high-DFI.png')
			with col1:
				st.image(image, width=64)
			with col2:
				st.error("High Digital Force")
				#st.markdown('<h1 style="color: white;">High Digital Force</h1>', unsafe_allow_html=True)

			st.markdown('<h2 style="color: white;">Your Community has at least a 30% likelihood of having the following technologies:</h3>', unsafe_allow_html=True)
			string1 = "<h2 style='text-align: center; color: white;'>"
			string2 = "</h2> <br> <br>"
			string = string1 + techlist + string2
			st.markdown(string, unsafe_allow_html=True)

		elif rating == 'medium': 
			col1, col2 = st.columns([2, 5])
			image = Image.open('images/medium-DFI.png')
			with col1:
				st.image(image, width=64)
			with col2:
				st.warning("Medium Digital Force")
				#st.markdown('<h1 style="color: white;">Medium Digital Force</h1>', unsafe_allow_html=True)

			st.markdown('<h2 style="color: white;">Your Community has at least a 30% likelihood of having the following technologies:</h3>', unsafe_allow_html=True)
			string1 = "<h2 style='text-align: center; color: white;'>"
			string2 = "</h2> <br> <br>"
			string = string1 + techlist + string2
			st.markdown(string, unsafe_allow_html=True)

		elif rating == 'low': 
			col1, col2 = st.columns([2, 5])
			image = Image.open('images/low-DFI.png')
			with col1:
				st.image(image, width=64)
			with col2:
				st.success("Low Digital Force")
				#st.markdown('<h1 style="color: white;">Low Digital Force</h1>', unsafe_allow_html=True)

			st.markdown('<h2 style="color: white;">Your Community has at least a 30% likelihood of having the following technologies:</h3>', unsafe_allow_html=True)
			string1 = "<h2 style='text-align: center; color: white;'>"
			string2 = "</h2> <br> <br>"
			string = string1 + techlist + string2
			st.markdown(string, unsafe_allow_html=True)	    	


		st.markdown("For more information on these technologies and others, visit [Electronic Fountiers Foundation](https://atlasofsurveillance.org/glossary)." , unsafe_allow_html=True)



elif page == "About the Data":
	data_sources = st.container() 
	DFI_section = st.container() 
	RF_section = st.container() 


	with data_sources: 
		st.title("Data Sources")

		data_sources_markdown = read_markdown_file("AboutTheData_DataSources.md")
		st.markdown(data_sources_markdown, unsafe_allow_html=True) 



	with DFI_section: 
		st.title("How is the DFI Calculated?")

		IRT_markdown = read_markdown_file("AboutTheData_IRT.md")
		st.markdown(IRT_markdown, unsafe_allow_html=True)

		image = Image.open("images/irtcurves.jpg")
		st.image(image, caption='IRT Model Trace Plots.', use_column_width=True)


	with RF_section: 
		st.title("How is the DFI in my area calculated?")

		RF_markdown = read_markdown_file("AboutTheData_RF.md")
		st.markdown(RF_markdown, unsafe_allow_html=True)

		image = Image.open("images/feature_importance.png")
		st.image(image, caption='Random Forest Model Feature Importance.', use_column_width=True)

## Take Action

elif page == "Take Action":

	take_action = st.container()
 
	with take_action: 

		image = Image.open("images/AOS.png")
		st.image(image, caption='https://atlasofsurveillance.org/', use_column_width=True)

		st.title("How can I get involved?")

		TakeAction_markdown = read_markdown_file("TakeAction.md")
		st.markdown(TakeAction_markdown, unsafe_allow_html=True)


elif page == "Meet the Team":

	team = st.container() 

	with team: 
		st.title("Meet the team")
		
		MeetTheTeam_markdown = read_markdown_file("MeetTheTeam.md")
		st.markdown(MeetTheTeam_markdown, unsafe_allow_html=True)

