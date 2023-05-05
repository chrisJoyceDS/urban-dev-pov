# Identifying poverty signals in cities across the US over time
### by Adam Miner, Clayton Coffman, and Chris Joyce
---
## Problem Statement

Poverty in the United States is not monolithic, simply identifiable by household income. Within each city, county, and state, poverty can take many forms, in most cases overlapping, from food access, to medical access, to effects on environment. Therefore, to properly identify poverty in a cross-disciplinary matter, factors of poverty must be synthesized and analyzed together. <br>
This study attempts to create a profile of poverty in neighborhoods across the United States in three cities: Seattle, New York City, and Washington D.C. Using socioeconomic data from the U.S. Census, and landcover data from the U.S. Geological Survey (USGS), and using an unsupervised learning process, we will cluster neighborhoods in U.S. cities into types of socioeconomic and environmental neighborhoods from the years 2000 to 2019. <br>
The way these neighborhoods change their cluster profile over a time period will indicate whether socioeconomic and/or environmental factors improve the outcomes of the neighborhood.  We will analyze the percentage of change from one neighborhood to another in a city to determine if these socioeconomic or environmental are correlated with the aggregate neighborhood change in that city. <br>

**Questions to address**
1. Can we create distinct neighborhood profiles of socioeconomic and environmental variables over time using an unsupervised learning process?
2. Can we identify which clusters that come from this learning process are indicative of impoverished areas?
3. Can we analyze the change in these areas over our study period to determine if how and if neighborhoods change on aggregate in a city?
4. Can we correlate the changes in neighborhood type to the specific environmental variables? For example, is the percentage of tree cover in a neighborhood correlated with less-impoverished neighborhood clusters?

---

## Research Design

This study uses a similar research design process that was employed by Delmelle (2015; https://www.sciencedirect.com/science/article/abs/pii/S0143622814002860?via%3Dihub). The research design is as follows:
1. Identify the variables for the study
2. Identify cities to study
3. Gather the data for each time period and join it to geographic Census boundaries
4. Conduct a K-Means or similar unsupervised learning process on the entire dataset for all years (separated by city)
5. Identify the generated clusters to construct neighborhood profiles
6. Identify the clusters most indicative of impoverished areas in cities
7. Determine how these neighborhoods change over time, and calculate the percentage of areas that transition out of poverty (or into poverty). We can facilitate this by using a Markov Chain process (https://math.libretexts.org/Bookshelves/Applied_Mathematics/Applied_Finite_Mathematics_(Sekhon_and_Bloom)/10%3A_Markov_Chains/10.01%3A_Introduction_to_Markov_Chains)
8. Generate individual city landscapes using these changes in poverty. Have we seen cities construct more green space and is that correlated with a decrease in the number of impoverished areas, for example?
9. Correlate socioeconomic variables to environmental variables using a supervised learning process (test the variables to percent of land use in a neighborhood).
10. Depict findings in charts, graphs, and written form.

---

## Data

We will be using Census data for our socioeconomic variables. These data are gathered every ten years in the U.S. Census, and also gathered during the U.S. Census’ American Community Survey (ACS). The ACS asks more questions than the regular Census. We will be using Census Tracts as our unit of analysis, due to their ubiquity in the Census data gathering process, their relative fine size, and the robustness of data available.<br>
To account for boundaries of Census Tracts changing over our study period, we will utilize the Census Tracts from the Longitudinal Census Tract Database ([LTDB](https://s4.ad.brown.edu/Projects/Diversity/researcher/bridging.htm)). This dataset interpolates past Census data from both the ten-year population counts and the ACS, and interpolates the results into 2010 Census Tracts. This allows for analysis and comparisons of similar geographic units over time. <br>
Land use data comes from the National Land Cover Database ([NLCD](https://www.usgs.gov/centers/eros/science/national-land-cover-database)) which is maintained by the USGS along with other federal agencies. It classifies land use into 16 categories at a 30m * 30m resolution. The categories include various kinds of plant cover (deciduous forest, grassland, pasture, etc.), level of urban development, and ground imperviousness. <br>
We will use a combination of GIS and Python to clean the data sources and merge together, then focus on using Scikit Learn’s Clustering Package for the unsupervised learning process. Python’s Pandas, Stats, and Matplotlib Libraries will provide the tools for our exploratory data analysis and chart generation. <br>
The charts and graphs will be shared on a website using Streamlit and Render, and interactive tools will be developed.

---

## Methods and Analysis

We used 16 socioeconomic and land-cover variables to analyze our problem. The socioeconomic variables came from the U.S. Census and were ones indicative of poverty, such as population, percent of people living in poverty, household income, percent of home ownership, and median home value and median rent. The land-cover variables were aggregated from different iterations of similar land-cover variables (forested regions, barren regions, etc.), and referred to the proportion of the Census Tract that made up that land cover. We identified four aggregated land cover variables: open urban spaces (parking lots, industrial areas), low-developed urban spaces (parks, industrial areas, suburbs), medium-developed urban spaces (suburban-style places, outer cores of cities), and highly-developed urban spaces (cities proper), unclassified or barren regions (including open water), forested areas, and cultivated areas (farmland).<br>
After combining and standardizing the variables, making sure to standardize after segmenting by three snapshot year study periods (2000, 2012, and 2019) and the city MSAs, we ran a K-means unsupervised learning algorithm on each of the three study cities for the entire time period. Through multiple iterations of the K-means and analysis of the silhouette scores at each neighbor cluster, we identified eight clusters as the most optimal neighbor count for the three MSAs. The silhouette score was on average about 0.26, for the clusters, signifying a model that was performing a tad bit above average.<br>
We then analyzed the centroids of each of the clusters for each of the MSAs and analyzed their relative values in each of the variables to each other.<br>

### Seattle:

Seattle had two clusters that were indicative of impoverished areas. These have high percent of people living in poverty, low household income, and low rent values and home ownership values. The distinguishing feature between these two clusters is the land cover usage of them. One cluster was indicative of an impoverished core within Seattle, and the other cluster was indicative of more rural forested and cultivated areas. Spatial analysis confirmed that by looking at the census tracts in the areas surrounding the city were poor and had land cover higher in the forested and cultivated areas. <br>
Seattle also had more rural clusters higher that would not be classified as poor. They do not have as high household income as other clusters, but they do have high rates of home ownership and present the trademark rural locations through analysis of land cover and spatial analysis.<br>
Finally, Seattle had a cluster associated with richer suburbs, and a cluster associated with higher income neighborhoods within the core part of the city.<br>
We analyzed the change in proportion of Census Tract cluster classifications over time, to determine if the city landscape has adjusted on aggregate since 2000. Due to the relative time constraints of the data, we only found that the rural cluster associated with higher income had begun to decrease since 2000, signifying lost land to more city development as the Seattle MSA expanded. The other clusters held constant through this time period.<br>

### New York City:

New York City was noteworthy for having a highly impoverished cluster largely contained in the most urban core of the MSA, and an impoverished cluster contained in the outer core of the city area. New York City also had a high-income urban core, a high income suburban center, and a high income rural area.<br>
New York City does not have a rural poor cluster like Seattle did. Its rural areas behaved more like the richer rural cluster in Seattle.<br>
Through analyzing the Clusters’ changes over time, New York’s clusters were remarkably stagnant, with only marginal changes in proportion of clusters. The only noteworthy change is that the impoverished inner core cluster seems to have increased ever so slightly since 2000.  It could mean that more urban areas have transitioned to this type of profile, or the areas in the NY MSA just improved across the board and dropped more census tracts into this category in later years.<br>

### DC: 

Washington D.C. has one distinctly poor cluster in the urban core, one distinctly poor cluster in the suburbs, and one distinctly poor cluster in the outermost suburbs (but probably not rural areas). Like New York City, and unlike Seattle, we do not see a rural poor cluster in the DC MSA, and do have one average and one high income cluster in the rural part of the MSA. <br>
DC has a few more noteworthy transitions. The suburban less-developed cluster has increased, likely as that urban sprawl has enveloped more census tracts in the MSA. In addition the profile of sparsely populated forested and agricultural areas has decreased, signifying transitions into more urbanized spaces in these former lands. Finally, Cluster 1 has increased and Cluster 2 has decreased. The delineation between these urbanized poor areas is how developed the census tracts are. Cluster 1 increasing signifies the MSA having more numerous urban inner core poor areas, and less numerous populated outer core areas.<br>

### Linear Regression

We wanted to establish a relationship between land cover and poverty, as studies have shown (most recently in Seattle: https://www.kuow.org/stories/seattle-considers-fees-to-support-trees-in-low-canopy-neighborhoods, https://www.sciencedirect.com/science/article/pii/S1353829216301332) that access to green spaces in cities is correlated with lower rates of poverty. This is due to the emphasis on this land use being part of a package of urban development. We tested the correlation between all types of land cover and its effect on poverty levels by creating a multivariate linear regression model, where the dependent variable was the percent of people living in poverty, and the independent variables were the land cover variables. The study design was done in the same manner as the K-means, with each year study period standardized, the only difference was the variable selection, and that the entire U.S. was covered.<br>
We could not establish a relationship between land cover use and its effects on poverty. The R-squared value was a tad above zero, and the P-value was significant, meaning that we could not disprove our hypothesis that land cover did matter when observing poverty.

## Conclusions and Recommendations

Analyzing cities using unsupervised learning is an efficient and low-cost method to profiling cities. As established, care must be taken to properly process and clean the data, establish the study location, time periods, and geographic boundaries, before conducting the analysis.<br>
What comes from this analysis are highly useful heuristics for profiling city areas, in both space and time. In our example, we wanted to identify impoverished rural and urban census tracts, that could then be given to policymakers, urban developers, and other interested stakeholders to focus urban development efforts on these areas, or rural development efforts to uplift the areas with low poverty.<br>
It also allows analysts to quickly profile different MSAs and compare them to each other. Policymakers can take these findings and communicate with peers in exemplar cities to see how these places focused their urban development efforts.<br>
More work needs to be done on picking variables indicative of poverty, better defining what constitutes a “city”, gathering more recent data, and establishing a study design on land cover and poverty that can help analysts arrive at more significant results. <br>

## Data Table

|Feature|Type|Description|
|:---|:---:|:---|
|**tractid**|*object*|ID of Census Tract|
|**GEOID10**|*object*|ID of Census Tract for 2010|
|**pop**|*object*|Population of the Census Tract|
|**incpc**|*object*|Per capita household income|
|**ppov**|*object*|Percent of people living in poverty|
|**hinc**|*object*|Household income|
|**phs**|*object*|Percent of people graduating with a high school degree|
|**mrent**|*object*|Median Rent|
|**mhmval**|*object*|Median Household Income|
|**pown**|*object*|Percent of people owning a house|
|**pmulti**|*object*|Percent of people living in multi-family houses|
|**open_urban_space**|*object*|Proportion of census tract covered by open urban spaces|
|**low_development**|*object*|Proportion of census tract covered by low developement|
|**medium_development**|*object*|Proportion of census tract covered by medium developement|
|**high_development**|*object*|Proportion of census tract covered by high developement|
|**unclassified**|*object*|Proportion of census tract covered by unclassified and barren land|
|**forested**|*object*|Proportion of census tract covered by forest|
|**cultivated**|*object*|Proportion of census tract covered by agriculatural land|
|**cluster**|*object*|K-Means cluster output|

## Repository Structure

```
├── data
│   ├── all_data.csv
│   ├── dc_clusters.csv
│   ├── dc_ltdb_nanda.csv
│   ├── dc_metro_census_tracts.csv
│   ├── dcnyse_metro_census_tracts.zip
│   ├── ny_metro_census_tracts.csv
│   ├── nyc_clusters.csv
│   ├── nyc_ltdb_nanda.csv
│   ├── seattle_clusters.csv
│   ├── seattle_ltdb_nanda.csv
│   ├── seattle_metro_census_tracts.csv
├── 01_census_api_pulldown_tracts.ipynb
├── 02_kmeans_preprocessing_modeling.ipynb
├── 03_clustering_modeling_three_cities.ipynb
├── 04_linear_regression_modeling_eda.ipynb
├── app.py
├── choropleths.ipynb
├── LICENSE
├── README.md
├── requirements.txt
```
