
### Electronic Frontiers Foundation's Atlas of Surveillance 



[Electronic Frontiers Foundation (EFF)](https://www.eff.org/) is a nonprofit organization that is dedicated to defending digital privacy, free speech, and innovation. The [Atlas of Surveillance (AOS)](https://atlasofsurveillance.org/) is a database created to document police technologies in your community and a project of EFF. The AOS dataset includes 7,200 datapoints which were grouped together into 4,998 agencies across the United States to generate their Digital Force Index (DFI). 

The AOS dataset includes a number of police technologies which we have included definitions for below. For more information of each of the technologies, please visit the [AOS glossary](https://atlasofsurveillance.org/glossary). 

- Body-worn Cameras are cameras attached to officers chests or shoulders to capture ineractions with suspects at the public. 

- Ring/Neighbors Partnership are used to capture video from home surveillance devices. 

- Drones are unmanned aerial vehicles that police can remotely control to surveil crowds or locations may be difficult or dangerous to surveil by foot. 

- Automated License Plate Readers are cameras attached to patrol cars or fixed locations, such as light posts, that capture license plates as they pass and upload the incident to a database with the time, data, location, and license plate information. 

- Camera Registry are volunteered by residents or businesses to provide law enforcement with information about the security cameras they have installed. 

- Face Recognition is a technology used to identify an individual using their face. 

- Predictive Policing is a software used to predict where crime is more likely to occur based on previous records and police data.

- Gunshot Detection is a technology that uses acoustic sensors to detect loud noise and alerts to law enforcement to where a gunshot may have occured. 

- Real-Time Crime Center are hubs where police receive and analyze surveillance and intellegence data from a number of sources in real-time. These centers differ from Fusion Centers in that they focus on local level activities. 

- Fusion Center is an intelligence hub and command center that enable intelligence sharing between agencies.

- Cell-site Simulator are devices that trick phones within a certain radius into connecting to the simulator than than a tower. These devices are used to pinpoint the location of a phone. 

- Video Analytics is a technology that is used to describe the detect of anomalies in video feeds. This is often coupled with predictive algorthims and face recognition technology. 


For more information about how the EFF AOS data was collected, please visit their [methodology page](https://atlasofsurveillance.org/methodology). 
For more information about how to get involved with EFF and their AOS project, please visit their [collaborate page](https://atlasofsurveillance.org/collaborate). 


### United States Census 

For our model's features we used [Census](https://data.census.gov/cedsci/) data that was imported using the tidycensus R package. We pulled in 45 census variables collected during 2014 to 2019 looking at race, socioeconomic status, education, transportation, and other demographic factors that well-represented the general make-up of each US zip code. 


For more information on our data pipeline, visit our [Github repository](github.com). 

