# Identifying poverty signals in cities across the US over time
### by Adam Miner, Clayton Coffman, and Chris Joyce
---
## Problem Statement

Poverty in the United States cannot be simply identified by tracking household income, it is not monolithic. Within each city, county, and state, poverty can take many forms and can overlap, from food access, to medical access, to effects on the environment. Therefore, to properly identify poverty in a cross-disciplinary matter, factors of poverty must be synthesized and analyzed together. <br>
This study attempts to create a profile of poverty in neighborhoods across the United States. Using socioeconomic data from the U.S. Census, and landcover data from the U.S. Geological Survey (USGS), and using an unsupervised learning process, we will cluster neighborhoods in U.S. cities into types of socioeconomic and environmental neighborhoods from the years 2000 to 2020. <br>
We will analyze any correlations between environmental factors and a socioeconomic indicator of poverty nationwide in an effort to interpret the impact of environmental factors on poverty. These results will be made available as a web application where users can interact and explore the relationships between these data points. <br>

---
## Data

We will be using Census data for our socioeconomic variables. These data are gathered every ten years in the U.S. Census, and also gathered during the U.S. Census’ American Community Survey (ACS). The ACS asks more questions than the regular Census. We will be using Census Tracts as our unit of analysis, due to their ubiquity in the Census data gathering process, their relative fine size, and the robustness of data available.<br>
To account for boundaries of Census Tracts changing over our study period, we will utilize the Census Tracts from the Longitudinal Census Tract Database ([LTDB](https://s4.ad.brown.edu/Projects/Diversity/researcher/bridging.htm)). This dataset interpolates past Census data from both the ten-year population counts and the ACS, and interpolates the results into 2010 Census Tracts. This allows for analysis and comparisons of similar geographic units over time. <br>
Land use data comes from the National Land Cover Database ([NLCD](https://www.usgs.gov/centers/eros/science/national-land-cover-database)) which is maintained by the USGS along with other federal agencies. It classifies land use into 16 categories at a 30m * 30m resolution. The categories include various kinds of plant cover (deciduous forest, grassland, pasture, etc.), level of urban development, and ground imperviousness. <br>
We will use a combination of GIS and Python to clean the data sources and merge together, then focus on using Scikit Learn’s Clustering Package for the unsupervised learning process. Python’s Pandas, Stats, and Matplotlib Libraries will provide the tools for our exploratory data analysis and chart generation. <br>
The charts and graphs will be shared on a website using Streamlit and Render, and interactive tools will be developed.

---
