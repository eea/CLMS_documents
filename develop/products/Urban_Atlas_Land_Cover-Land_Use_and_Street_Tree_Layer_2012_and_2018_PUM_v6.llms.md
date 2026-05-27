# Urban Atlas Land Cover/Land Use and Street Tree Layer 2012 and 2018 - Product User Manual

Copernicus Land Monitoring Service

This document serves as a comprehensive mapping guide for service providers involved in the Copernicus Urban Atlas project, specifically for the 2012 and 2018 reference years. It details the methodology for generating standardised land use and land cover (LU/LC) maps, including additional information layers such as the Street Tree Layer (STL) and Digital Height Model (DHM). The guide aims to ensure congruent product attributes, common nomenclature, consistent product appearance, and comparable product quality across Functional Urban Areas (FUAs) within the EU, EFTA, Western Balkans, the UK, and Turkey.

Published

December 3, 2025

Keywords

Functional Urban Area (FUA), Land Use / Land Cover (LU/LC), Street Tree Layer (STL), Digital Height Model (DHM), Imperviousness Degree (IMD), Minimum Mapping Unit (MMU), Change detection, ETRS89 Lambert Azimuthal Equal Area (LAEA), Geometric adaptation of navigation data, Overall classification accuracy

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

# 1 Executive summary

This document contains the product description, mapping guidance and class description for the product “Urban Atlas” from the Copernicus “Urban Atlas” project for the 2006 reference year and the “Urban Atlas” update and extension for the 2012 and 2018 reference years.

# 2 Scope

This mapping guide aims at supporting service providers in generating an Urban Atlas mapping product. It provides guidance to achieve:

- Congruent product attributes such as file format, file attributes.

- Common nomenclature.

- Common look and feel of the product.

- Comparable quality of the product.

# 3 Reference documents

The table below includes the different Reference Documents (RD) related to the Urban Atlas project. A list of abbreviations is provided in Annex 1.

|  | **Name** | **Issue** | **Date** | **Reference** |
|:--:|----|----|----|----|
| RD\[1\] | C5-Service Validation Protocol | 1.00 | 14/05/2008 | ITD-0421-RP-0003-C5 |
| RD\[2\] | Call for Tenders No ENTR/08/029 - Specifications | 2.00 | 07/05/2008 | Call for Tenders No ENTR/08/029 - Specs |
| RD\[3\] | Mapping Guide for a European Urban Atlas | 1.02 | 08/05/2008 | ITD-0421-GSELand-TN-01 |
| RD\[4\] | Call for Tenders No EEA/IDM/RO/16/007 - Specifications | 1.0 | 08/08/2016 | Call for Tenders No EEA/IDM/RO/16/007 - Specs |
| RD\[5\] | Urban Atlas 2012 Validation Report | 1.2 | 09/06/2017 | UA2012 Validation Report |
| RD\[6\] | Urban Atlas 2012 Extension to Western Balkan and Turkey Validation report | 1.5 | 05/11/2018 | UA2012 Extension Validation report |
| RD\[7\] | Urban Atlas 2006 Mapping Guide | 2.0 |  | UA2006 Mapping Guide |
| RD\[8\] | Urban Atlas 2012 Mapping Guide | 5.0 |  | UA2012 Mapping Guide |

# 4 Mapping guide

## 4.1 Product description

### 4.1.1 Land Use / Land Cover mapping

The Urban Atlas service offers a high-resolution land use map of urban areas. Initially covering over 300 European cities with more than 100,000 inhabitants for the 2006 reference year, the Urban Atlas is available for the 2012 and 2018 reference years over nearly 800 cities with more than 50,000 inhabitants distributed among EU, EFTA and West Balkan countries plus United Kingdom and Turkey. Each Urban Atlas product is generated over the city and its surroundings, according to the Functional Urban Area (FUA) defined by the implementation of the approach developed by the DG Regional and Urban Policy (REGIO) of the European Commission.

The product described in this mapping guide is adapted to European needs (discussed and agreed with DG REGIO) and contains information that can be derived mainly from Earth Observation (EO) data backed by other reference data, such as Commercial Off-The-Shelf (COTS) or Open Street Map (OSM) navigation data and topographic maps.

Detailed specifications of Urban Atlas LU/LC product.

[TABLE]

The table provided in Annex 5.3 gives a more detailed description of the product specifications.

![This is a detailed land use/land cover map of an urban area, likely a Functional Urban Area in Europe, displaying a comprehensive classification using 26 distinct categories. The map legend provides specific numeric codes, descriptive names, and associated colours for each land cover type. The Ground Level coverage (G.L.) percentages are included for urban fabric categories. The legend categories are: \* \*\*Urban Fabric:\*\* \* 11100: Continuous Urban Fabric (G.L. \> 80%) - Dark Red \* 11210: Discontinuous Dense Urban Fabric (G.L.: 50% - 80%) - Red \* 11220: Discontinuous Medium Density Urban Fabric (G.L.: 30% - 50%) - Light Red \* 11230: Discontinuous Low Density Urban Fabric (G.L.: 10% - 30%) - Purple \* 11240: Discontinuous Very Low Density Urban Fabric (G.L.: \< 10%) - Light Purple \* 11300: Isolated Structures - Grey \* \*\*Industrial, Commercial, Transport, and Extractive:\*\* \* 12100: Industrial, commercial, public, military and private units - Dark Grey \* 12210: Fast transit roads and associated land - Medium Grey \* 12220: Other roads and associated land - Lighter Grey \* 12230: Railways and associated land - Brown \* 12300: Port areas - Dark Brown \* 12400: Airports - Beige \* 13100: Mineral extraction and dump sites - Light Brown \* 13300: Construction sites - Yellowish Brown \* 13400: Land without current use - Pale Yellow \* \*\*Green Urban and Natural Areas:\*\* \* 14100: Green urban areas - Bright Green \* 14200: Sports and leisure facilities - Lighter Green \* 26000: Orchards - Olive Green \* 31000: Forests - Dark Green \* 32000: Herbaceous vegetation associations - Medium Green \* 33000: Open spaces with little or no vegetations - Light Greenish Yellow \* \*\*Agricultural Areas:\*\* \* 21000: Arable land (annual crops) - Pale Orange \* 22000: Permanent crops - Darker Orange \* 23000: Pastures - Light Yellow-Green \* 24000: Complex and mixed cultivation patterns - Yellow \* \*\*Water Bodies and Wetlands:\*\* \* 40000: Wetlands - Pale Blue \* 50000: Water - Bright Blue The map displays a dense urban core characterized by Continuous Urban Fabric (Dark Red) and Discontinuous Dense Urban Fabric (Red), transitioning to lower density urban fabrics (Purple, Light Purple) towards the outskirts. Extensive Green urban areas (Bright Green) and Forests (Dark Green) are interspersed within and around the urbanized zones, particularly evident in the south-east. Transport infrastructure, including fast transit roads, other roads, and railways (various shades of grey and brown), forms a prominent network. Small bodies of water (Bright Blue) and wetlands (Pale Blue) are also visible. A scale bar indicates distances up to 2 kms, with intervals at 0, 0.5, and 1 kms. A north arrow is labelled 'N'. This type of high-resolution land use/land cover data for Functional Urban Areas is a Copernicus Land Monitoring Service (CLMS) product, typically available for reference years such as 2006, 2012, and 2018.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image20.jpeg)

Example of the “look & feel“ of the final Urban Atlas 2012 product for Brussels

### 4.1.2 Additional information layers

The Urban Atlas Mapping Guide is related to the main product and by default refers to the Land Use / Land Cover (LU/LC) database. However, two additional information layers are also available starting from the 2012 reference year. A short description including the detailed specifications is proposed in this section.

The first one is called Street Tree Layer (STL), a separate layer from the Urban Atlas LU/LC map produced within the level 1 urban mask for each FUA (partial coverage for 2012 reference year). It includes contiguous rows or patches of trees along the streets.

[TABLE]

Detailed specifications of Urban Atlas STL product {.caption-top .table}

The second one is a Digital Height Model (DHM) providing building bloc height information. This consists of a 10 m x 10 m resolution raster layer containing height information generated for urban areas of selected cities (currently the core area of capitals of all countries covered by the Urban Atlas).

The building height information is derived from IRS-P5 stereo images of the reference year 2012. It contains only the heights of the building bloc itself (i.e. trees are masked out). As described in the terms of reference, the mean absolute error of the height must be below 3m. This is verified by comparing the measured values with reference values and described in a validation report.

[TABLE]

Detailed specifications of Urban Atlas DHM product {.caption-top .table}

## 6.1 General guidelines

### 6.1.1 Pre-processing and geo-coding of EO data

The EO data provided to the Service Provider should already be pre-processed. In order to reach the 1/10,000 expected scale, EO data should be provided with spatial resolution less than 5 meters. Service Provider should check the geometric quality of the delivered EO data, but no further pre-processing step is expected. The EO data for the European Urban Atlas 2012 is the optical VHR2 coverage over EU 2011-2013 (DWH_MG2b_CORE_03) available on Data Warehouse (DWH) of the European Space Agency (ESA). The EO data for the Urban Atlas 2018 is an optical VHR coverage over EU 2017-2019 also available on ESA DWH. Change detection task can be supported by Copernicus Sentinel-2 data (10 m resolution).

### 6.1.2 Pre-processing and geometric adaptation of navigation data

The EO data are the basis for interpretation and classification. In case of geometrical differences between EO data and navigation data (COTS or OSM), the navigation data has to be corrected in line with the EO data.

The pre-processing and application of the navigation data (COTS or OSM) shall be done according to the methodology defined in Annex 5.2.

### 6.1.3 Pre-processing of topographic maps

Topographic maps can be used for interpretation of objects. Topographic maps should be used in digital form with precise geo-coding. The usage of printed (analogue) maps is not recommended. In case of geometrical differences between EO data and topographic maps, the erroneous data (either EO-data or topo-maps) needs to be identified using reliable datasets providing spatial reference information. The geometry of the mapping product shall then be congruent with the correct dataset.

### 6.1.4 Classification and interpretation

Application of automatic classification routines, such as segmentation and clustering, may be applied whenever appropriate:

Automated segmentation and classification to achieve an initial differentiation between basic land cover classes (urban vs. forest vs. water vs. other land cover) is possible following a decision of the service providers.

As the backbone for the object geometry, the navigation data network (COTS or OSM) is recommended but only with the method defined in the Annex.

Manual refinement and classification at the finest level of the LU/LC classification especially within urban areas by means of visual interpretation of EO data remain necessary to be compliant with the product specifications. For this purpose, the following sections provide the rules and principles to be applied.

### 6.1.5 Use of Copernicus HRL imperviousness

Among the reference products from Copernicus Land Monitoring Services (CLMS), the pan-European High-Resolution Layer (HRL) Imperviousness (formerly named Fast Track Sealing layer, FTS) is used for the classification at level 4 of the residential or mixed use urban fabric units classified 1.1.2 from EO data

The assignment of the imperviousness/soil sealing levels or density (i.e. classes 1.1.2.1 - 1.1.2.4) shall be carried out using the HRL Imperviousness layer or similar one. The Quality Assurance (QA) process will check only if the technical approach agreed with DG REGIO is respected but will not assess the absolute accuracy of these classes.

### 6.1.6 Data format of the final product

ESRI ArcGIS compatible or open source OGC-standard vector format with polygon topology:

- Complete coverage in a single area feature layer.

- No overlapping polygons, gaps, duplicates or missing polygon labels or node overshoots.

- Final vectors need to have a smooth appearance (no pixel-shaped polygons are allowed). The smoothing shall be done by the service provider by methods preserving the geometry of objects. It is to ensure that smoothed vectors still comply with the minimum width and minimum mapping units required for objects.

![A simple two-row table defining a land cover classification code. The header row is labelled 'CODE_yyyyy'. The data row contains the value '11210\*'. This code likely represents a specific land use/land cover class, such as 'Industrial or commercial units' based on the CORINE Land Cover (CLC) nomenclature for urban areas, as hinted by the document's surrounding context.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image1.jpg)

Example provided of the number for UA class 1.1.2.1

![\| CODE \| Legend code \| \|---\|---\| \| yyyy \| Reference year (e.g. 2006, 2012 or 2018) \| This table defines the code \`yyyy\` as a representation for a 'Reference year' within technical documentation, providing examples such as 2006, 2012, and 2018.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image2.jpg)

Column data format:

CODE_yyyyy: 5 digits in Long Integer format without decimal places (values allowed: 11100 to 92000 (all class codes))

The complete description of the data format is provided in section 5.4.

### 6.1.7 Interpretation rules

- The delineation is to be done on the EO data. EO data should be considered as the primary (guiding) data source.

- The interpretation of the object is done using:

  - The EO data, topographic maps, navigation data (COTS or OSM) and other relevant ancillary data.

  - Auxiliary information including local expertise.

- The interpreted area should be interpreted with a minimum 100 m extension (100 m buffer) to ensure accuracy and continuity of polygons. During the post-processing phase, a subset with the spatial extent of the final product will be generated. At the borders of this subset (i.e. the final product), polygons smaller than the MMU may be present. To be in line with this rule, please note that a 100m extension buffer has been applied over sea / ocean for the coastal FUAs for the 2012 & 2018 products.

- In areas where two or more scenes overlap, the most recent data must be used for delineation and interpretation.

- In case of cloud coverage over the most recent scene, the affected part (only this part!) shall be interpreted using a cloudless alternative scene.

&nbsp;

- If two or more objects are overlapping at different levels, the top level is mapped continuously, e.g. road bridge over railway is mapped as seen, the railway polygon is split in two parts and the road is mapped as a continuous feature.

- In case of two or more objects overlapping at the same height level, the visually dominant and complete object (in use and shape) is mapped continuously. For example, a road / railway crossing viewed at the same height level: the railway shall be mapped continuously to maintain the network. The road shall be split in two parts.

- Analysis scale : 1:5 000

### 6.1.8 LU/LC change detection and layer generation

In case of the required production of an update of the Urban Atlas LU/LC database for a historic or new reference year, change detection task shall be performed and an additional layer shall be produced by the service provider, the Land Use / Land Cover (LU/LC) change layer. For the European Urban Atlas, following the LU/LC product generation for the 2006 reference year, change detection were performed successively for generating the 2012 and 2018 products.

Change detection and characterization shall be performed considering the VHR ortho-rectified optical satellite imagery as the reference. Adopting a manual methodological approach based on the visual comparison between the images from two different reference years is always required, but it can also be combined with automatic change detection approaches (image-to-image or map-to-image) which should improve the performances. Otherwise, as the change layer shall *only contain real changes* between two reference years, any inconsistencies of LU/LC codes will not be considered as a change if due to thematic misclassification inherited from the LU/LC information related to the first reference year already available. In such a case, it is worth to correct LU/LC misclassifications related to this year and generate a revised status layer accordingly.

In the specific case of the change detection between 2012 and 2018 for the European Urban Atlas, LU/LC misclassifications from 2012 are corrected but only in the immediate surroundings of the actual LU/LC change area, which led to produce a revised LU/LC 2012 status layer. Otherwise, LU/LC changes from, to, or within urban areas are detected, extracted and characterized at the finest level of the nomenclature, in accordance with the MMUs listed below. However, LU/LC changes occurring within rural/natural areas are mapped only if the change occurs at level 1 of the nomenclature, then well characterized at the finest level (ex: change from 31000 to 23000). In other words, changes that occur within the same rural/natural areas are not mapped (for instance, changes from 21000 to 22000 are not identified and therefore not included in the change layer).

Changes are firstly reported in an intermediate layer identified as Urban Atlas 2012-2018 LU/LC which contains the LU/LC information for both reference dates, 2012 and 2018. More concretely, based on the 2012 LU/LC information, polygon features of detected changes are delineated and characterized for 2018. Then, the change layer is generated, but it is worth to highlight that it is not performed by a fully blind extraction of all area features for which LU/LC classification codes are different. Indeed, there are one exception for which the area features are not considered for generating the change layer: isolated structures logically classified as 11300 for 2012 reference year and classified as continuous or discontinuous urban fabric unit (11100 or 11200) for 2018 only because of urban expansion over the period but without any actual LU/LC change (contextual reason). This means that for getting real changes occurred between 2012 and 2018, the 2012-2018 change layer shall be used; combining both status layers and extracting the features which have different LU/LC classifications overtime will not provide this information.

A particular case : forest cuts.

As it is often quite difficult to predict the future LU/LC over an area resulting from a forest cut, the rule applied is the following:

- Forest cuts are included in Class 31000 named ‘Forests’ by default as it is mentioned in Section 4.6, and systematically in case such areas are fully surrounded by wooded area.

- Forest cuts are included in another class as soon as they occur at the edge of the forest and that the context given by VHR reference imagery justifies such a choice (e.g. pastures, orchards, future construction site, etc.).

![This map illustrates Land Use / Land Cover (LULC) changes in the FR010L2 Montpellier area of France between 2012 and 2018, using Copernicus Urban Atlas data. The image is divided into three main sections: 'Urban Atlas 2012', 'Urban Atlas 2018', and 'Changes between 2012 and 2018'. A scale bar is present indicating 0, 0.5, and 1 km, along with a north arrow. The 'Urban Atlas 2012' section displays a false-colour infrared satellite image (Image source: Spot5 - 13/08/2011) and its corresponding LULC map. On the 2012 LULC map, classes include: urban fabric (dark red), industrial/commercial/transport units (purple), agricultural areas (light yellow), forests/semi-natural areas (dark green), water bodies (light blue), roads/railways (grey), green urban areas (brownish), and sport/leisure facilities (pinkish). The 'Urban Atlas 2018' section displays a false-colour infrared satellite image (Image source: Pléiades 1B - 06/08/2018) and its corresponding LULC map. Compared to 2012, the 2018 imagery and LULC map show a prominent new linear feature, likely a major transport corridor, extending through what was previously agricultural land, appearing as a dark grey area. The 'Changes between 2012 and 2018' section specifically highlights the transformations using the following legend: \* Dark red: 'Urban expansion from agricultural areas' \* Red: 'Urban expansion from natural areas' \* Purple: 'Internal urban changes' \* Orange: 'Urban conversion to agriculture' The map of changes indicates significant urban expansion, predominantly from agricultural areas (dark red), concentrated along the newly developed linear transport infrastructure. Smaller, dispersed patches of urban expansion from natural areas (red) and internal urban changes (purple) are also visible. 'Urban conversion to agriculture' (orange) appears to be a very minor change in this specific geographical view.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image21.png)

Change Dynamics over FR010L2 Montpellier (2012-2018)

### 6.1.9 Street tree layer

The Street Tree Layer 2012 (STL2012) and Street Tree Layer 2018 (STL2018) are separate layers from respectively the UA2012 and UA2018 LU/LC Layers, which are produced within the level 1 urban mask for each FUA. They include contiguous rows or patches of trees covering 500m² or more and with a minimum width (MinMW) of 10 m over “Artificial surfaces” (nomenclature class 1) inside FUA (i.e. rows of trees along the road network outside urban areas or forest adjacent to urban areas should not be included).

The following specific rules have to be applied:

- Exception to the 10 m MinMW rule: in order to maintain continuity, units smaller than 10 m over a distance up to 10 m can still be included in STL (see figures below).  

![This conceptual diagram illustrates geometric criteria, specifically a 10-meter (10 m) threshold, for delineating and representing Land Use / Land Cover (LULC) features in spatial data products, likely related to the Copernicus Land Monitoring Service (CLMS) Urban Atlas. The left panel depicts a linear feature, initially 10 m wide, which narrows to less than 10 m over a segment before expanding back to 10 m. This illustrates a condition where a linear feature's width drops below a 10 m threshold, which may necessitate specific mapping rules, such as generalization or merging, in LULC product generation. The right panel shows an area feature (green polygon) surrounded by another land cover class (red polygon). A narrow connection or intrusion of the green class into the red area, or vice-versa, is highlighted by a yellow square. Blue arrows extending from the square towards the surrounding features are each labelled '\< 10 m', indicating that the dimension of this narrow neck or small feature is less than 10 m. This illustrates a common scenario where a feature's size falls below the Minimum Mapping Unit (MMU) for area features, influencing its representation in a LULC database.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image22.jpg)

- Border effect correction: road network crossing wooded area and connecting cities and villages is fully classified as STL due to tree crown cover by default. Therefore, post-processing step needs to be implemented for correcting this misclassification.  

![A spatial map illustrating the distribution of features labelled 'S T L before post processing' and an area marked as 'Border effect'. The map shows a white background with irregular patches and linear elements rendered in dark green, representing the 'S T L before post processing' features. These features are denser on the left side of the map. An irregularly shaped polygon outlined in red, located in the upper-central part of the map, highlights an area designated as a 'Border effect'. This red-outlined area also contains green 'S T L' features, which appear to be less dense or more fragmented compared to the dense concentration on the far left. The legend on the right indicates: a solid dark green square for 'S T L before post processing' and a red outlined square for 'Border effect'. The map does not include a scale bar, compass, or explicit reference year, but the surrounding context refers to the European Urban Atlas.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image24.png)

An urban mask analysis to exclude road and railway networks connecting cities and villages shall be applied to solve this border effect. Urban Mask analysis needs to define a tolerance fixed to 50 m that well differentiate urban and interurban networks. Large railway infrastructures may be excluded from the mask, but this is not an issue knowing that trees are very rare in such areas.

![This image displays two conceptual map segments illustrating Land Use / Land Cover (LULC) masking rules for delineating artificial areas around linear transport infrastructure, relevant to the Copernicus Urban Atlas program. The left map segment shows a narrow linear feature (grey) labelled as '\< 50m width'. Surrounding polygons are hatched red and hatched light green, likely representing different LULC classes. An annotation states: 'The mask outline go straight and cut the road.' This indicates that if a road or similar linear feature is less than 50 metres wide, the LULC mask boundary for adjacent areas should extend straight across it, effectively including the narrow feature within the surrounding LULC polygon (e.g., an artificial area). The right map segment shows a wider linear feature (dark grey) labelled 'RAILWAYS' with a width indicated as '\> 50m width'. Surrounding polygons are hatched red, hatched purple, and hatched light green. A small hatched dark red polygon is also visible. An annotation states: 'The mask outline exclude the railways from the artificial area.' This implies that if a railway or similar linear feature is greater than 50 metres wide, the LULC mask boundary should delineate around it, excluding the wider feature from the adjacent artificial LULC polygons. The maps demonstrate different Minimum Mapping Unit (MMU) or delineation rules based on the width of transport infrastructure when creating or updating Urban Atlas LULC layers.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image25.jpg)

STL patches do not cover roads (codes 12210 and 12220) or railways (code 12230) connecting cities, that are outside the urban mask.

- MMU rule (\>500 m²) is applied to STL polygons (STL = 1)

- The STL layer contains trees (STL = 1) or No data (STL= 99).

![This image illustrates the extraction of a Street Tree Layer (STL) from very high resolution (VHR) satellite imagery, specifically demonstrating an exception to the Minimum Mapping Width (MinMW) rule. The left panel shows a false-colour composite of an urban area, featuring roads, buildings (turquoise/greenish-blue), and vegetation highlighted in bright red. A large body of water appears dark blue on the left. The right panel displays the corresponding extracted Street Tree Layer as irregular green polygons on a white background, delineating the tree patches and linear tree features. This visual comparison highlights how smaller or narrower patches of trees, which might typically be excluded by a 10-metre Minimum Mapping Width rule, are retained in the Street Tree Layer product to ensure the continuity of tree lines and patches within urban areas.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image27.jpg)

Comparison between VHR2018 scene (left) and STL2018 product (right)

### 6.1.10 Digital Height Model layer (DHM)

A 10 m raster layer containing height information is generated for core urban areas of capital cities of the EEA38 and the United Kingdom as part of the Urban Atlas project (see table 2), based on the methodology described hereafter.

1.  Base data  

The input data source of stereo data is the IRS-P5 Cartosat-1. In May 2005, the Indian Space Research Organisation (ISRO) had launched the IRS-P5 Cartosat-1 satellite, equipped with the PAN-Aft and PAN-Fore instruments that form a dual-optics 2-line (forward and backward looking) along-track stereoscopic push broom scanner with a stereo angle of 31°, an original spatial resolution of 2.5 m and a swath width of 27 km. The satellite covers the entire globe in 1867 orbits on a 126-day cycle.

Because of its optimized stereo configuration (stereo acquisitions within seconds and optimized acquisition angles), IRS-P5 Cartosat-1 high-resolution stereo satellite imagery has proven to be perfectly suited for the creation of the digital surface models in the resolution and quality requested.

The very comprehensive data situation and the unique specifications guarantee a very good coverage of urban areas in Europe by one single data source.

2.  DSM generation  

Based on the stereo images, a digital surface model (DSM) is generated, which represents the height of all objects above the earth’s surface, i.e. plant/ forest canopy or the top of artificial constructions such as buildings.

The major steps are:

- Selection of suitable stereo images

- Pixel-wise matching approach

- Bundle block adjustment and RPC improvement

- Automated outlier detection

- Void filling

- Process QA

The result of the DSM processing chain is an accurate and reliable 3 m DSM (to get the full advantages of the higher resolution, e.g. for a better delineation of buildings), which will be further regularised to the final 10 m resolution in the nDSM generation step, to fit the product requirements.

3.  DTM generation  

Digital terrain models (DTMs) represent the height of the bare earth’s surface. In this case, the DTMs are generated from a DSM and non-ground features such as buildings, trees, bushes and vehicles have to be identified and their height measurements be removed from the data before interpolation.

In order to ensure meeting the DTM quality requirements even in complicated terrain situations and to ensure best possible accuracy of generated DTMs, it is useful to combine the extracted ground point results of different filter methods or apply regionally adjusted algorithm parameterizations.

The interpolation approach carried out in this project is ordinary Kriging. It is the most commonly used Kriging method, used in simulations for spatial data, commonly considered to best minimizes the variance of the estimation error.

4.  nDSM generation and refinement  

The next step towards finally retrieving building block heights is the creation of a normalized Digital Surface Model (nDSM). An nDSM is the difference between a DTM and a DSM used to show height values of buildings, vegetation and other objects.

***nDSM = DSM – DTM***

![This conceptual diagram illustrates the definitions and relationship between three types of digital elevation models: Digital Surface Model (DSM), Digital Terrain Model (DTM), and normalized Digital Surface Model (nDSM). The top panel displays a terrain profile, represented by a black line, with three grey objects: a building, a tree, and another building. The DSM, marked by a blue dashed line, represents the elevation of the terrain including all features on its surface, such as buildings and trees. The DTM, marked by a red dashed line, represents the bare earth's surface, excluding the height of non-ground features. The bottom panel demonstrates the derivation of the nDSM. The nDSM, indicated by an orange dashed line, is calculated by subtracting the DTM from the DSM (nDSM = DSM - DTM), thereby representing the height of features (buildings, trees) above the ground.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image29.png)

DSM computation principle (http://www.stadtentwicklung.berlin.de/umwelt/umweltatlas/ed610_03.htm)

As there are vegetation and other untilled areas included in the raw nDSM, hence a substantial further quality refinement with different ancillary datasets is necessary to generate a sharp and error-free digital building block height model.

Ancillary datasets consist of (i) built-up area, water and street classes of Urban Atlas 2012 and (ii) NDVI map for vegetation removal, calculated from Spot 5 seamless mosaics.

The nDSM at this stage is a 3 m resolution intermediate product that is then resampled with a maximum upscaling process to the final 10 m horizontal resolution, and which is then finally sharpened by using the borders of the built-up area classes from Urban Atlas 2012. Values outside these classes are set to Zero. Each pixel represents a height value and no statistics have been calculated based on the building block heights.

In a last refinement step the accuracy specifications are checked and if necessary, heights are adapted.

![Choropleth map depicting the distribution of non-ground features within an unlabelled urban area. The boundary of the urban area is delineated by a thin red line. Areas shaded in purple represent 'non-ground features', which, based on the surrounding text, include buildings, trees, bushes, and vehicles. White areas indicate ground features or absence of non-ground features. The scale bar at the bottom indicates distances from 0 km to 10 km, with intermediate markings at 2 km, 4 km, 6 km, and 8 km. The map shows a dense concentration of non-ground features in the central and western parts of the urban area. A prominent diagonal band running from the northwest to the southeast shows a significant absence of these features, likely representing a river or major transport corridor. The eastern and northern regions show a sparser, more fragmented distribution of non-ground features.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image30.jpg)

Coverage of Vienna core area with relevant UA 2012 built-up classes

5.  Post processing and product finalization  

In the final post-processing and product package generation step, the properly refined nDSM with building block heights, which are considered the final product (Digital Height Models – DHM) are checked by an automated routine for adherence to the following basic technical and formal product specifications:

- 10 m spatial resolution.

- ETRS89 – Lambert Azimuthal Equal Area (LAEA) projection.

- Consistent file format, naming and structure, class legends and color codes.

- Correct height values / background values.

Each Building Block Height model (DHM) is clipped exactly to the AOI and assigned a folder with a corresponding name. As a further automated step, an INSPIRE compliant metadata file is generated for every product and a template for the delivery report is created for each DU and stored in the respective folder.

![A coloured choropleth map illustrating a Normalized Digital Surface Model (nDSM) of an urban area, identified as the Vienna core area, with object heights derived using Urban Atlas 2012 built-up classes. The map displays height values in metres (m) using a multi-colour gradient, with a final horizontal resolution of 10 m. The legend defines the height categories: \* Dark blue: \]-∞; 0\] m (likely water bodies and terrain at or below the Digital Terrain Model) \* Green: \]0; 10\] m \* Light yellow: \]10; 20\] m \* Orange: \]20; 30\] m \* Red: \]30; ∞\[ m (tallest structures) The map shows a river (dark blue) winding through a densely built-up urban landscape. Buildings appear in various shades of green, light yellow, orange, and red, indicating their relative heights. Taller structures (orange and red) are concentrated in several distinct blocks along the river and throughout the urban fabric. Peripheral areas show lower heights (green and light yellow), representing vegetation or smaller buildings. A distinctive circular/oval structure is visible on the far right, predominantly in orange.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image31.jpg)

Final Digital Height Model (height values in m)

### 6.1.11 Minimum mapping units and exceptions

[TABLE]

Exception of MMU 0.25 / 1 ha: in case of a homogeneous area \> MMU but divided in 2 or more polygons by the road or railway network, each part can be smaller to preserve the land cover information. However, no polygon can be smaller than 500 m² (e.g. a 1 ha forest divided in 4 polygons by the road network has to be mapped) except for polygons at the border of the FUA (\>100 m²).

The minimum mapping width (MinMW) between 2 objects for distinct mapping is 10 m.

Exception of minimum width 10m of a mapping unit: class 12220 (MMW = 6m).

Exception of minimum width 10m of a mapping unit: to maintain continuity of linear structures, they can be mapped smaller than 10 m over a distance up to 50 m (see figure below).

![This diagram illustrates a mapping rule for a linear feature with varying width and a maximum length. The feature is bounded by two black lines on a light yellow background. At its widest points, indicated by vertical double-headed arrows on the left and right, the feature has a width of 10 m. The central portion of the feature narrows significantly. A horizontal double-headed arrow below the feature indicates a length of '≤ 50 m', encompassing the section from where the feature begins to narrow to where it regains its 10 m width. This geometric configuration is labelled as 'Mapped as 1.2.2.3', suggesting a classification code within a land cover mapping system like CORINE Land Cover (CLC).](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image36.png)

Priority mapping rules for areas smaller than the MMU:

1.  Smaller areas are visually added to the adjacent unit with the thematically closest class. Rule used for the artificial codes (1xxxx).

2.  Smaller areas are added to the adjacent unit with the longest common border line, except to railways or roads (exception here: if an object is below the MMU size and completely surrounded by e.g. road or railway network it shall be aggregated with that surrounding traffic line). Rule used for the natural / semi-natural codes (2xxxx, 3xxxx, 4xxxx, 5xxxx) and all the polygons \< 100m².

**Specific Minimum Mapping Units for LULC CHANGE layer :**

In order to ensure that relevant LU/LC changes are appropriately extracted, the MMUs for the LU/LC change layer (e.g. 2012-2018) are defined as below:

- Urban (class 1) to urban (class 1) = 0.1 ha

- Rural/natural (classes 2-5) to urban (class 1) = 0.1 ha

- Rural/natural (classes 2-5) to rural/natural (classes 2-5) = 0.25 ha

- Urban (class 1) to rural/natural (classes 2-5) = 0.25 ha

Considering this MMUs, exceptions are made in case of areas where changes involve road and railway networks (classes 12210, 12220, 12230); polygon features classified as road or railway for one date or directly connected to such element are extracted even if area is lower than MMU in order to keep consistency of the transportation network.

### 6.1.12 Accuracy assessment and validation

In addition to the usual QA/QC procedure implementation, which implies visual checks for ensuring thematic and geometric positional accuracies and automatic checks for ensuring completeness and logical consistency during the post-processing phase of the production, accuracy assessment and validation must be performed independently from the production for providing the evidence that the results are fully compliant with the product specifications.

Thus, accuracy assessment follows a “double-blind” approach which means that production team and reference data team work completely independently. Reference database is obtained through the interpretation of samples which are selected based on a stratified random sampling of EEA 1km grid cell. The number of samples for each FUAs varies depending on the FUA size. The results of the reference interpretation provide the material to derive confusion matrixes, which are used to assess the accuracies.

[TABLE]

For the DHM layer, Quality controls are conducted for each stage of the production: the DSM and DTM generation, the nDSM production, the masking and the nDSM / Building Block Height refinement. Thus, the emerging dataset is quality checked several times throughout the process.

Every product is accompanied by a DHM QC Report, which shows the results of the external Quality Check and an INSPIRE compliant xml file: [Building Height 2012 — Copernicus Land Monitoring Service](https://land.copernicus.eu/local/urban-atlas/building-height-2012?tab=download).

## 6.2 LU/LC nomenclature

The Urban Atlas Land Use / Land Cover classification is derived from CORINE Land Cover and is composed of 27 classes distributing among 5 thematic groups, namely:

1.  Artificial surfaces

2.  Agricultural areas

3.  Natural and (semi-)natural areas

4.  Wetlands

5.  Water

Four hierarchical levels are defined in the nomenclature for artificial surfaces (class 1) while only two are defined for the non-artificial ones (classes 2-5). The table below shows the LU/LC nomenclature providing class codes and descriptions and any information or ancillary data source useful for the product generation in addition to EO data.

A decision matric below illustrate the rules followed to apply LULC nomenclature to each identified feature.

[TABLE]

UA LULC nomenclature (in bold, classes without any further subdivision) {.caption-top .table}

## 7.2 Decision rules

Affectation of LULC classes follow the below decision matrix. A detailed matrix concerning artificial areas is illustrated next page.

![This diagram, titled 'Decision Matrix', illustrates a hierarchical classification process for land cover and land use (LULC) categories. The initial step branches into 'Land' or 'Water'. 1. \*\*IF\*\* an area is classified as 'Land': \* \*\*IF\*\* it exhibits 'Human activity non-agricultural', \*\*THEN\*\* it is categorised as '1. Artificial Surfaces'. \* \*\*IF\*\* it shows 'Little / non human influence, agriculture, forestry', \*\*THEN\*\* it branches into two distinct categories: '2. Agricultural + semi-natural areas + wetlands' and '3. Forests'. 2. \*\*IF\*\* an area is classified as 'Water': \* \*\*IF\*\* it consists of 'Flooded areas', \*\*THEN\*\* it is categorised as '4. Wetland'. \* \*\*IF\*\* it consists of 'Water bodies / courses', \*\*THEN\*\* it is categorised as '5. Water'. The decision matrix results in five final land cover categories: 1. Artificial Surfaces, 2. Agricultural + semi-natural areas + wetlands, 3. Forests, 4. Wetland, and 5. Water.](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image37.png)

Urban Atlas LULC decision matrix

![This diagram presents a hierarchical land cover classification scheme, detailing the '1. Artificial Surfaces' category and its sub-classes within the Copernicus Land Monitoring Service (CLMS). The scheme begins with input data sources on the left, including 'Ref. Data', 'Additional data req.', 'Sat. Image TK COTS navigation data', and 'HRL IMD sealing' (High Resolution Layer Imperviousness Density). The top-level class is '1. Artificial Surfaces', which is broadly defined by four main types of areas: 1. Urban areas with dominant residential use or inner-city areas with central business district and residential use, which lead to '1.1 Urban Fabric'. 2. Industrial, commercial, public, military and private units or transport units are predominant, which lead to '1.2 Industrial, commercial, public, military and private units'. 3. Strong human influence on soil surface, but buildings not dominant, which lead to '1.3 Mine, dump and construction site'. 4. Leisure and recreation use dominates, which lead to '1.4 Artificial non agricultural vegetated areas'. The classification further breaks down these categories: \* '1.1 Urban Fabric' is divided into: \* '1.1.1 Continuous Urban Fabric' \* '1.1.2 Discontinuous Urban Fabric' \* '1.1.3 Isolated Structures' \* '1.1.2 Discontinuous Urban Fabric' is further specified by Surface Sealing (S.L.) percentages, using 'HRL IMD sealing' data: '1.1.2.1 (S.L. 50% - 80%)', '1.1.2.2 (S.L. 30% - 50%)', '1.1.2.3 (S.L. 10% - 30%)', and '1.1.2.4 (S.L. 0% - 10%)'. \* '1.2 Industrial, commercial, public, military and private units' is divided into: \* '1.2.1 Industrial, commercial, public, military and private units' \* '1.2.2 Road and rail network and associated land' \* '1.2.3 Port areas' \* '1.2.4 Airports' \* '1.2.2 Road and rail network and associated land' is further detailed, also using 'HRL IMD sealing' data: '1.2.2.1 Fast transit roads and associated land', '1.2.2.2 Other roads and associated land', and '1.2.2.3 Railways and associated land'. \* '1.3 Mine, dump and construction site' is divided into: \* '1.3.1 Mineral extraction and dump sites' \* '1.3.3 Construction sites' \* '1.3.4 Land without current use' \* '1.4 Artificial non agricultural vegetated areas' is divided into: \* '1.4.1 Green urban areas' \* '1.4.2 Sports and leisure facilities'](Urban_Atlas_Land_Cover-Land_Use_and_Street_Tree_Layer_2012_and_2018_PUM_v6-media/image38.png)

Urban Atlas Decision Matrix for Artificial Surfaces

## 7.3 Description of LU/LC thematic classes

### 1. Artificial surfaces

Surfaces with dominant human influence and without agricultural land use.

These areas include all artificial structures and their associated non-sealed and vegetated surfaces.

Artificial structures are defined as buildings, roads, all constructions of infrastructure and other artificially sealed or paved areas.

**Associated non-sealed and vegetated surfaces** are areas functionally related to human activities, except agriculture.

Also, the areas where the natural surface is replaced by extraction and / or deposition or designed landscapes (such as urban parks or leisure parks) are mapped in this class.

The land use is dominated by permanently populated areas and / or traffic, exploration, non-agricultural production, sports, recreation and leisure.

**1.1 URBAN FABRIC**

Built-up areas and their associated land, such as gardens, parks, planted areas and non-surfaced public areas and the infrastructure, if these areas are not suitable to be mapped separately regarding the minimum mapping unit size.

Basically, the classes 1.1.1 and 1.1.2. are distinguished by their degree of soil sealing.

Residential structures and patterns are predominant, but also downtown areas and city centres, including the Central Business Districts (CBD) and areas with partial residential use, are included.

The urban fabric classes (1.1) are distinguished only by their degree of soil sealing not by their type of buildings (single family houses or apartment blocks).

The detailed descriptions of the different classes below are given to the interpreters to support the delineation of mapping objects with homogeneous sealing density (without being required to assign the exact density classes).

Using the navigation data as a skeleton for the urban area, in many cases it is necessary to subdivide the blocks formed by the navigation data due to the different sealing density of the residential areas or different functions of the buildings and their associated land.

After completion of the interpretation, the sealing level information from the IMD sealing layer is integrated into the data.

***1.1.1 CONTINUOUS URBAN FABRIC***

Special note:

Mapping the 3rd level is done only with the defined application of the IMD sealing layer.

> *MMU 0.25 ha, MinMW: 10 m*

Land Cover:

Average degree of soil sealing:   80%

Built-up areas and their associated land, if these areas are not suitable to be mapped separately regarding the minimum mapping unit size.

Buildings, roads and sealed areas cover most of the area; non-linear areas of vegetation and bare soil are exceptional.

Land Use:

Predominant residential use: areas with a high degree of soil sealing, independent of their housing scheme (single family houses or high-rise dwellings, city centre or suburb).

Included are downtown areas and city centres, and Central Business Districts (CBD) if there is partial residential use.

***1.1.2 DISCONTINUOUS URBAN FABRIC***

Special note:

Mapping the 4th level of density classes is done only with the defined application of the imperviousness / soil sealing layer.

Land Cover:

Average degree of imperviousness / soil sealing: 0 - 80%

Built-up areas and their associated land (small roads, sealed areas including non-linear areas of vegetation and bare soil), if these areas are not suitable to be mapped separately regarding the minimum mapping unit size.

This type of land cover can be distinguished from continuous urban fabric by a larger fraction of non-sealed and / or vegetated surfaces: gardens, parks, planted areas and non-surfaced public areas.

Land Use:

Predominant residential usage. Contains more than 20% non-sealed areas, independent of their housing scheme (single family houses or high-rise dwellings, city centre or suburb).

The non-sealed areas might be private gardens or common green areas.

Not included are:

Farms with large buildings (agro-industrial production), → class 1.2.1.

Nurseries with dominant areas of greenhouses (no or only small fields) → class 1.2.1.

Allotment gardens → class 1.4.2.

Holiday villages (“Club Med”) → class 1.4.2.

*1.1.2.1 DISCONTINUOUS DENSE URBAN FABRIC*

> *MMU 0.25 ha, MinMW: 10 m*

Average degree of soil sealing: \> 50 - 80%

Residential buildings, roads and other artificially surfaced areas.

*1.1.2.2 DISCONTINUOUS MEDIUM DENSITY URBAN FABRIC*

> *MMU 0.25 ha, MinMW: 10 m*

Average degree of soil sealing: \> 30 - 50%

Residential buildings, roads and other artificially surfaced areas. The vegetated areas are predominant, but the land is not dedicated to forestry or agriculture.

*1.1.2.3 DISCONTINUOUS LOW DENSITY URBAN FABRIC*

> *MMU 0.25 ha, MinMW: 10 m*

Average degree of soil sealing: 10 - 30%

Residential buildings, roads and other artificially surfaced areas. The vegetated areas are predominant, but the land is not dedicated to forestry or agriculture.

*1.1.2.4 DISCONTINUOUS VERY LOW DENSITY URBAN FABRIC*

> *MMU 0.25 ha, MinMW: 10 m*

Average degree of soil sealing: \<10 %

Residential buildings, roads and other artificially surfaced areas. The vegetated areas are predominant, but the land is not dedicated to forestry or agriculture. Example: exclusive residential areas with large gardens.

***1.1.3 ISOLATED STRUCTURES***

> *MMU 0.25 ha, Maximum Mapping Unit 2 ha, MinMW: 10 m*

Isolated artificially structures with a **residential component**, such as (small) individual farmhouses and related buildings.

It must contain only a few houses (1 to 5 houses: depending on the size of the houses and the number of associated buildings), otherwise it should be included in class 1.1.2.

**The mapping unit is no larger than 2 ha**, otherwise it should also be included in class 1.1.2.

To be in line with this eligibility rule (regarding level 1 of the nomenclature, artificialized areas), if the considered feature is neighbouring another urban class polygon(s) other than transportation network, and the total surface of the considered polygons is above 2 ha, the area should be considered as class 1.1.2 rather than 1.1.3”

Comment : In this kind of areas under development, some small areas are considered as class 1.1.2 (and not 1.1.3) because of the presence of neighbouring areas classified as 1.3.4 (artificial areas).

**1.2 INDUSTRIAL, COMMERCIAL, PUBLIC, MILITARY, PRIVATE AND TRANSPORT UNITS**

At least 30% of the ground is covered by artificial surfaces. More than 50% of those artificial surfaces are occupied by buildings and / or artificial structures with non-residential use, i.e. industrial, commercial or transport related uses are dominant.

***1.2.1 INDUSTRIAL, COMMERCIAL, PUBLIC, MILITARY AND PRIVATE UNITS***

> *MMU 0.25 ha, MinMW: 10 m*

Land cover:

Artificial structures (e.g. buildings) or artificial surfaces (e.g. concrete, asphalt, tar, macadam, tarmac or otherwise stabilized surface, e.g. compacted soil, devoid of vegetation), occupy most of the surface. Included are associated areas, such as roads, sealed areas and vegetated areas, if these areas are not suitable to be mapped separately regarding the MMU size.

Land use:

Industrial, commercial, public, military or private units. The administrative boundaries of the production or service unit are mapped, including associated features larger than the MMU (e.g. sports areas or transport structures).

Also included are:

\> Bare soil and/or grassland potentially used for storage of material or as enclosures for livestock.

\> Compounds with significant amounts of green or natural areas but with industrial, commercial, military or public use. Example: communication tower, antennas or wind motors and their associated land.

This class contains:

1.  Industrial uses and related areas

\> Sites of industrial activities, including their related areas such as storage areas.

\> Production sites.

\> Energy plants: nuclear, solar, hydroelectric, thermal, electric and wind farms.

\> Sewage treatment plants.

\> Farming industries (farms with large buildings and / or greenhouses).

\> Antennas, even with predominant vegetated areas. The vegetated areas may be predominant, but the land is not dedicated to forestry or agriculture.

\> Water treatment plants.

\> Sewage plants.

\> Seawater desalination plants.

The industrial units can be distinguished from residential built-up areas by the type of buildings, their access to transport features and the surroundings:

\> Buildings with large surface areas (inside, not all rooms need daylight, as in dwelling houses).

\> Good access to roads and parking for customers.

\> Industrial areas are often outside the historical city centre.

2.  Commercial uses, retail parks and related areas

\> Surfaces purely occupied by commercial activities, including their related areas (e.g. parking areas even larger than the MMU).

\> High-rise office buildings.

\> Petrol and service stations within built-up areas.

The commercial units can be distinguished from residential built-up areas by the type of large buildings, their access to transport features and the surroundings:

\> Buildings with large surface areas (inside, not all rooms need daylight, as in dwelling houses).

\> Good access to roads and parking for customers.

\> Pure commercial areas are often outside the historical city centre.

Not included are:

Petrol stations along fast transit and main roads with access only from these roads. They are mapped together with the road transport system → class 1.2.2.1 or 1.2.2.2.

3.  Public, military and private services not related to the transport system

Surfaces purely occupied by general government, public or private administrations including their related areas (access ways, lawns, military training areas, parking areas).

Included are:

\> Schools and universities.

\> Hospitals and other health services or buildings.

\> Places of worship (churches / cathedrals / religious buildings).

\> Archaeological sites and museums.

\> Administration buildings, ministries.

\> Penitentiaries.

\> Military areas including bases and ports.

\> Military exercise areas fenced and under current use.

\> Castles, etc. not primarily used for residential purposes (building management, gardeners, etc…. living there is not residential use in this sense).

\> Private storage areas without a residential component, such as compounds of garages.

Not included are:

\> Public parks → class 1.4.1.

\> Holiday resorts including their hotels → class 1.4.2.

\> Sport centres or bathing centres → class 1.4.2.

\> Cemeteries → class 1.4.1 (note: for the “UA 2006” LULC production, the cemeteries were classified in class 1.2.1, they are now included in class 1.4.1 in “UA 2006 Revised” and “UA 2012” LCLU).

\> Military airports → class 1.2.4.

4.  Civil protection and supply infrastructure

\> Dams, dikes, irrigation and drainage canals and ponds and other technical public infrastructure, to be mapped with the roads, embankments and associated land included.

\> Includes also breakwaters, piers and jetties, sea walls and flood defenses.

\> (Ancient) city walls, other protecting walls, bunkers.

\> Avalanche barriers.

Not included are:

Noise barriers → class 1.2.2.

Water courses (within e.g. diked canals) if the water area is wider than 10 m → class 5; Reservoirs along natural water courses → class 5.

***1.2.2 ROAD AND RAIL NETWORK AND ASSOCIATED LAND***

> *MMU 0.25 ha, MinMW: 6 m (Road) - 10 m (Rail)*

Special Note:

The road and railway network (COTS or OSM data) is ingested into the classification database according to the method given in the Annex.

Parts of the navigation data that are obviously not congruent with the corresponding traffic line in the EO data and ancillary map need to be corrected.

Roads which are not contained in the navigation data are mapped by the service provider according to the mapping criteria defined in this mapping guide.

Roads or railways do not necessarily have to form a closed network. Isolated traffic lines are possible, but they are to be mapped regarding the MMU criterion.

Associated land is mapped with the roads / railways as it is visible in the EO data and topographic maps.

Associated lands are:

\> Slopes of embankments or cut sections.

\> Areas enclosed by roads or railways, without direct access and without agricultural land use.

\> Fenced areas along roads (e.g. as for protection against wild animals).

\> Areas enclosed by motorways, exits or service roads with no detectable access.

\> Noise barriers (fences, walls, earth walls).

\> Rest areas, service stations and parking areas only accessible from the fast transit roads.

\> Railway facilities including stations, cargo stations and service areas.

\> Foot- or bicycle paths parallel to the traffic line.

\> Green strips, alleys (with trees or bushes).

*1.2.2.1 FAST TRANSIT ROADS AND ASSOCIATED LAND*

> *MMU 0.25 ha, MinMW: 6 m*

Roads defined as “motorways” in the navigation data, including motorway rest, service areas, tolls, parking areas, only accessible from the motorways.

Areas surrounded by highway or railway junctions have to be included in the corresponding network.

Motorways that are not included in the navigation data are to be mapped by the service provider.

*1.2.2.2 OTHER ROADS AND ASSOCIATED LAND*

> *MMU 0.25 ha, MinMW: 6 m*

Roads, crossings, intersections and parking areas, including roundabouts and sealed areas with “road surface”.

*1.2.2.3 RAILWAYS AND ASSOCIATED LAND*

> *MMU 0.25 ha, MinMW: 10 m*

Railway facilities including stations, cargo stations and service areas.

***1.2.3 PORT AREAS***

> *MMU 0.25 ha, MinMW: 10 m*

Special Note:

Ancillary data is recommended for identifying the administrative boundary of the port area. The delineation itself is to be done on the EO data:

\> Detailed city / tourist maps or

\> Field check (on site visit) or

\> Local zoning data

Administrative area of inland harbours and seaports.

Infrastructure of port areas, including quays, dockyards, transport and storage areas and associated areas.

Not included are:

Marinas → class 1.4.2.

Industrial areas directly located in a port.

***1.2.4 AIRPORTS***

> *MMU 0.25 ha, MinMW: 10 m*

Special Note:

Ancillary data is recommended for identifying the administrative boundary of the airport area. The delineation itself is to be done on the EO data:

\> Detailed city / tourist maps or

\> Field check (on site visit) or

\> Local zoning data

Administrative area of airports mostly fenced.

Included are all airport installations: runways, buildings and associated land.

Military airports are also included (included in class 1.2.1. for UA2006).

Not included are:

Aerodromes without sealed runway → class 1.4.2.

**1.3 MINE, DUMP AND CONSTRUCTION SITES**

***1.3.1 MINERAL EXTRACTION AND DUMP SITES***

> *MMU 0.25 ha, MinMW: 10 m*

Special Note:

Ancillary data is recommended for identifying the administrative boundary. The delineation itself is to be done on the EO data:

\> Detailed city / tourist maps or

\> Field check (on site visit) or

\> Local zoning data

Included are:

\> Open pit extraction sites (sand, quarries) including water surface, if \< MMU, open-cast mines, **inland salinas**, oil and gas fields.

\> Their protecting dikes and / or vegetation belts and associated land such as service areas, storage depots.

\> Public, industrial or mine dump sites, raw or liquid wastes, legal or illegal, their protecting dikes and / or vegetation belts and associated land such as service areas.

Not included are:

Water bodies \> MMU → class 5.

Exploited peat bogs → class 4 (only for UA2012).

Coastal salinas → class 4 (only for UA2012).

Re-cultivated areas (mapped according to their actual land cover) → class 2 or 3.

Riverbed extraction → class 4 for wetlands or 3.3 for rocks (only for UA2012).

Decanting basins of biological water treatment plants → class 1.2.1.

***1.3.3 CONSTRUCTION SITES***

> *MMU 0.25 ha, MinMW: 10 m*

Spaces under construction or development, soil or bedrock excavations for construction purposes or other earthworks visible in the image.

Clear evidence of actual construction needs to be identifiable in the data, such as actual excavations and machinery on site, or ongoing construction of any stage, land under development, etc.

In case of doubt → class 1.3.4.

***1.3.4 LAND WITHOUT CURRENT USE***

> *MMU 0.25 ha, MinMW: 10 m*

Areas in the vicinity of artificial surfaces still waiting to be used or re-used. The area is obviously in a transitional position, “waiting to be used”.

Waste land removed former industry areas, (“brown fields”) gaps in between new construction areas or leftover land in the urban context (“green fields”).

No actual agricultural or recreational use.

No construction is visible, without maintenance, but no undisturbed fully natural or semi-natural vegetation (secondary ruderal vegetation).

Also, areas where the street network is already finished, but actual erection of buildings is still not visible.

Not included are:

“Leftover areas”, areas too small / narrow for any construction regarding the MMU size → map to the appropriate neighbour class as associated land.

**1.4 ARTIFICIAL NON-AGRICULTURAL VEGETATED AREAS**

Vegetation planted and regularly worked by humans; strongly human-influenced. Sporting facilities as functional units independent of being non-sealed, sealed or built-up.

***1.4.1 GREEN URBAN AREAS***

> *MMU 0.25 ha, MinMW: 10 m*

Public green areas for predominantly recreational use such as gardens, playgrounds, zoos, parks, castle parks and cemeteries (cemeteries were included in class 1.2.1 for UA2006). Suburban natural areas that have become and are managed as urban parks.

Forests or green areas extending from the surroundings into urban areas are mapped as green urban areas when at least two sides are bordered by urban areas and structures, and traces of recreational use are visible.

Not included are:

Private gardens within housing areas → class 1.1.

Buildings within parks, such as castles or museums → class 1.2.1.

Cases of patches of natural vegetation or agricultural areas, enclosed by built-up areas without being managed as green urban areas :

\> under 0,25 ha → merged with the surrounding classes

\> between 0,25 ha and 1 ha → class 1.3.4.

\> above 1ha → classified in their own LC/LU

***1.4.2 SPORTS AND LEISURE FACILITIES***

> *MMU 0.25 ha, MinMW: 10 m*

All sports and leisure facilities including associated land, whether public or commercially managed: e.g. Theresienwiese (Munich), public arenas for any kind of sports including associated green areas, parking places, etc.:

- Golf courses.

- Sports fields (also outside the settlement area).

- Campgrounds.

- Leisure parks.

- Riding grounds.

- Racecourses.

- Amusement parks.

- Swimming resorts etc.

- Holiday villages (“Club Med”).

- Allotment gardens[^1].

- Glider or sports airports, aerodromes without sealed runway.

- Marinas.

Not included are:

Private gardens within housing areas → class 1.1.

Motor racing courses within industrial zone used for test purposes → class 1.2.1.

Caravan parking used for commercial activities → class 1.2.1.

Soccer fields, etc. within e.g. military bases or within university campuses → class 1.2.1.

### 2. Agricultural

Please note that Classes 2.1 to 2.4 are grouped together in Class 2 in UA2006.

> *MMU 1 ha*

**2.1 ARABLE LAND**

- Fields under rotation system. Can be non-irrigated or permanently irrigated. Also includes rice fields.

- Fields laid in fallow are included.

**2.2 PERMANENT CROPS**

- Orchards

- Vineyards and their nurseries

- Roses

- Olive groves

- Berries and hop plantations

**2.3 PASTURES**

- Pasture and meadow under agricultural use, grazed or mechanically harvested.

- Wooded meadows, pastures with scattered trees.

**2.4 COMPLEX AND MIXED CULTIVATION PATTERNS**

- Annual crops associated with permanent crops such as orchards.

- Complex cultivation patterns.

- Land principally occupied by agriculture, with significant areas of natural vegetation.

- Agroforestry areas.

### 3. Natural and semi-natural areas

Please note that Class 3.1 are included into class 3 and classes 3.2 and 3.3 are included into class 2 in UA2006.

> *MMU 1 ha*

**3.1 FORESTS**

- Broad leaved forest, coniferous forest and mixed forest.

- Transitional woodland and shrub (clear cut, new plantations and regeneration, or damage forest).

- With ground coverage of tree canopy \> 30%, tree height \> 5 m, including bushes and shrubs at the fringe of the forest.

- Included tree nurseries, *Populus* plantations, Christmas tree plantations.

- Forest regeneration / re-colonisation: clear cuts, new forest plantations.

Not included are:

Forests within urban areas and/or subject to high human pressure → class 1.4.1

**3.2 HERBACEOUS VEGETATION ASSOCIATION**

- Vegetation cover more than 50%, ground coverage of trees with height \>5 m: \<30%, areas with minor / without artificial or agricultural influence.

- Sclerophyllous vegetation.

- Bushy sclerophyllous vegetation (e.g. maquis, garrigue).

- Abandoned arable land with bushes.

- Woodland degradation: storm, snow, insects or air pollution.

- Areas under power transmission lines inside forest.

- Fire breaks.

- Steep bushy slopes of eroded areas.

- Abandoned vineyards or orchards, arable land and pastures under natural colonisation.

- Herbaceous area with bush proliferation indicating no agricultural or farming use for a rather long time.

- Bushy areas along creeks.

- Bushes, shrubs and herbaceous plants, dwarf forest in alpine or coastal regions  
  (Pinus Mugo forests). Height is maximum 3 m in climax stage.

- Natural grassland.

**3.3 OPEN SPACES WITH LITTLE OR NO VEGETATION**

1.  Beaches, dunes, sand:  

- \< 10% vegetation cover.

- Beaches, dunes and sand plains, (coastal or inland location), gravel along rivers.

- Seasonal rivers, if water is characteristic for a shorter part of the year (\< 2 months).

2.  Bare rocks:  

- \> 90% of the land surface of bare rocks, (i.e. \< 10% vegetation).

- Rocks, gravel fields, landslides.

- Scree (fragments resulting from mechanical and chemical erosion. Weathering rocks forming heaps of coarse debris at the foot of steep slopes), cliffs, rocks.

3.  Sparsely vegetated areas:  

- Steppes, tundra, badlands, scattered high altitude vegetation. Bare soils inside military training areas. Vegetation cover 10 - 50%.  

4.  Burnt areas:  

- Recently burnt forest or shrubs (but not natural grassland), still mainly black on EO data.  

5.  Snow and ice:  

- Glacier and perpetual snow.  

### 4. Wetlands

Please note that Class 4 is included into Class 2 in UA2006.

1.  Inland wetlands:  

- Areas flooded or liable to flooding during a large part of the year by fresh, brackish or standing water with specific vegetation coverage made of low shrub, semi-ligneous or herbaceous species.

- Water fringe vegetation, reed beds of lakes, rivers and brooks. Sedge and fen-sedge beds, swamps.

- Peat bogs, with or without peat extracting areas.

- Shallow water areas covered with reed.

- Seasonal rivers, if water course is not visible in the EO data.

2.  Coastal wetlands:  

- Areas flooded or liable to flooding during a large part of the year by brackish or saline water, susceptible to flooding by sea water. Often in the process of fi in and gradually being colonized by halophytic plants.

- Specific vegetation coverage made of low shrub, semi-ligneous or herbaceous species.

- Alluvial planes, marshes and intertidal flats

- Salinas (salt production sites by evaporation).

Not included are:

Military exercise areas fenced and under current use → class 1.2.1.

Greenhouses → class 1.2.1.

Inland salinas → class 1.3 1.

### 5. Water

> *MMU 1 ha*

The visible water surface area on the EO data is delineated. EO data should be considered as a primary (guiding) data source.

- Sea.

- Lakes.

- Fishponds (natural, artificial)

- Rivers, including channeled rivers.

- Canals.

The default source for delineation is the EO data. If no clear delineation is possible using EO data, the other reference datasets may be used for that. Examples are:

- Reservoirs.

- Water courses or ponds with a strongly variable surface level.

All water bodies and water courses visible in the imagery are mapped as long as they exceed an extent of 1 ha.

Water courses are mapped continuously also when water surface is covered by vegetation. If the water is partly obscured, e.g. by vegetation, the delineation shall be oriented to other parts of the water where it is not obscured.

Included are:

- Seasonal rivers, if the water course is visible in the EO data, otherwise → class 2.

- Fishponds with distance \< 10 m are mapped together.

The navigation (COTS or OSM) data water layer may be used as a reference for interpretation. However, delineation of water areas must be done using the EO data, as the geometric accuracy of a OSM data water object is too rough for mapping on the scale 1:10 000.

Not included are:

Shallow water areas covered with reed \> MMU → class 2 Seasonal rivers, if the water course is not visible in the EO data → class 2.

### 6. Miscellaneous

Concerning the UA2006 products, areas with EO data provision problems were classified in separate classes described below.

1.  No data (Clouds and shadows)  

Areas affected by clouds or shadows on the EO data have to be mapped with ancillary data if the cloud or/and shadow overlays with the “CGC_RG_LAEA” layer (priority areas corresponding to the cities and greater cities according to the EC/OECD definition of cities (2011) provided by DG REGIO). An additional layer called “CGC_CLOUD_CAPI” delineating the areas classified by other data sources (Google Earth or other relevant available data sources) than the VHR2 coverage (DWH_MG2b_CORE_03) will be produced.

Outside these priority areas, class 9.1 (code 91000) will be used for areas covered by clouds and shadows over the satellite images where land use/land cover is not possible to be determined.

2.  No data (Missing imagery)  

This class 9.2 (code 92000) includes areas without available satellite image or inadequate imagery (e.g. no STL data can be produced as the image acquisition is outside the vegetation period).

# 8 List of abbreviations

| **Abbreviation** | **Full Form** |
|----|----|
| CBD | Central Business Districts |
| CLMS | Copernicus Land Monitoring Service |
| CORINE | COoRdination of INformation on the Environment |
| COTS | Commercial Off-The-Shelf |
| DG REGIO | European Commission Directorate-General for Regional and Urban Policy |
| DHM | Digital Height Model |
| DWH | Data WareHouse |
| EC | European Commission |
| EEA | European Environment Agency |
| EFTA | European Free Trade Association |
| EO | Earth Observation |
| EU | European Union |
| ESA | European Space Agency |
| FTS | Fast Track Sealing layer |
| FUA | Functional Urban Areas |
| HRL | High Resolution Layer |
| IMD | IMperviousness Degree |
| INSPIRE | INfrastructure for SPatial InfoRmation in Europe |
| LULC | Land Use / Land Cover |
| MinMW | Minimum Mapping Width |
| MMU | Minimum Mapping Unit |
| OA | Overall Accuracy |
| OECD | Organization for Economic Co-operation and Development |
| OSM | Open Street Map |
| QA | Quality Assurance |
| QC | Quality Check |
| RD | Reference Document |
| RPC | Rational Polynomial Coefficient |
| SL | Sealing Layer |
| STL | Street Tree Layer |
| UA | Urban Atlas |
| VHR | Very High Resolution |

# 9 Annex

## 9.1 Pre-processing and geometric adaptation of navigation data

The navigation datasets (COTS or OSM) by default include a specific and hierarchical classification of the road network. Two basic categories are important within the context of the Urban Atlas. The first category gives information about the Functional Road Class (FRC), i.e. the road type, the second one gives information about the importance of each road within the city traffic network (Net2Class).

The navigation data currently used shows the following categories for FRC/type and Net2Class:

| **FRC (COTS)** | **Type (OSM)** | **Full name** |
|:--:|:--:|----|
| **0** | motorway | Motorway, Freeway or another Major Road |
| **1** | trunk | Major Road less important than a Motorway |
| **2** | trunk_link | Other Major Road |
| **3** | primary | Secondary Road |
| **4** | secondary | Local Connecting Road |
| **5** | secondary_link | Local Road of high importance |
| **6** | tertiary | Local Road |
| **7** | residential, service, unclassified | Local Road of minor importance |
| **8** | track, path, steps, cycleway | Other Road |

| **Net2Class** | **Importance Level**   |
|---------------|------------------------|
| **0**         | First class (Highest)  |
| **1**         | Second class           |
| **2**         | Third class            |
| **3**         | Fourth class           |
| **4**         | Fifth class            |
| **5**         | Sixth class            |
| **6**         | Seventh class (Lowest) |

USAGE OF NAVIGATION DATA FOR THE URBAN ATLAS

The navigation data (COTS or OSM) will be used to generate the street and railroad network of the mapping product. This network will serve as a “backbone” and is decisive for the look and feel of the final product.

The data is delivered in line vector format by the data provider. These lines need to be widened so that the traffic line network of the final product covers the transport areas in the EO data.

For that purpose, a usage and buffering strategy was developed to implement the navigation data into the product.

The integration of the traffic network shall be done in advance of all other visual or (semi) automatic delineation and labelling of objects.

The goal of the traffic line implementation process is to ingest a traffic line network into the mapping product that covers all traffic lines wider than 10 m (including their associated land – see traffic line description: class 1.2.2) and – on the other hand – is COTS-efficient to integrate.

To achieve that goal the following strategy was developed:

- The railway network is delineated individually if it exceeds a minimum width of 10 m including its associated land.

- The most important roads (FRC classes 0, 1) will be delineated individually.

- Most of the roads (FRC classes 2 to 5) will be ingested by buffering the line vectors. The buffered roads will have an overall width of at least 10 m. The buffering width for each FRC class will be adapted to the local conditions of each individual city to resemble the overall characteristics of the local traffic network.

- Certain roads (FRC class 6 and above) will be mapped if available (by buffering) or left out according to the decision of the service provider. This is to preserve a common look and feel of the mapping products of different cities.

The following table gives an overview of the road network processing approach:

| **FRC** | **Net2Class 1** | **Net2Class 2** | **Net2Class 3** | **Net2Class 4** |
|----|----|----|----|----|
| **0** | Manual |  |  |  |
| **1** | Manual |  |  |  |
| **2** | Estimated buffer width | Estimated buffer width | Estimated buffer width | Estimated buffer width |
| **3** | Estimated buffer width | Estimated buffer width | Estimated buffer width | Estimated buffer width |
| **4** | Estimated buffer width | Estimated buffer width | Estimated buffer width | Estimated buffer width |
| **5** | Estimated buffer width | Estimated buffer width | Estimated buffer width | Estimated buffer width |
| **6 and above** | Mapping decided on city by city basis |  |  |  |

The general procedure for the road buffering is as follows:

PRE-PROCESSING

- Identification of the different combinations for fields Net2Class and FRC.

- Decision whether to include FRC=6 or not based on visual inspection.

- Sampling of several streets (up to service provider) for each combination.

- Estimation of mean width for each combination.

- The use of VHR imagery (e.g. Google Earth) is recommended. If the city is not available in VHR, a city with similar morphology in the same country may be used along with the EO data for production.

PROCESSING

- Buffering implementation.

- Manual delineation of streets FRC=0 and 1.

POST-PROCESSING

- Manual delineation of streets wider than 10 m that have not been buffered previously (i.e. not present in the street network layer or belonging to combinations not considered for buffering).

- Correction (elimination / edition) of errors due to inaccuracies of the line street network or buffering process.

Post-processing will be implemented according to service provider’s production chain.

## 9.2 Detailed product specification table

**Product features**

- Digital thematic map.

- Thematic classes based on CORINE LC nomenclature and Copernicus Urban Service Legend

**Input data sources**

- Earth Observation (EO) data with 2 to 4 m spatial resolution multispectral or pan-sharpened (multispectral merged with panchromatic) data. Multispectral data includes near-infrared band.10m resolution Sentinel-2 EO data for the rural 2012-2018 change detections.

- Topographic Maps at a scale of 1: 50 000 or larger.

- Navigation data (COTS or OSM) for the road network.

- Areas of Interest for Urban Atlas (UA) Mapping are determined by DG REGIO.

- Soil Sealing / Imperviousness Degree (IMD) based on HRL Imperviousness specifications for degree of sealed soils (IMD 0-100%) for level 3 classes 1.1.1 and 1.1.2 and level 4 classes 1.1.2.1, 1.1.2.2, 1.1.2.3 and 1.1.2.4.

- All input data should be described by metadata according to the INSPIRE metadata profile specifications and guidelines.

**Ancillary data optional for all classes**

- Navigation data (COTS or OSM): points of interest, land use, land cover, water areas.

- Google Earth or other relevant available database (only for interpretation, not for delineation).

- Local city maps

- Local zoning data (e.g. cadastral data). Field check (on-site visit).

- Very high resolution imagery (better than 1 m ground resolution, e.g. aerial photographs).

**Geometric resolution (Scale)**

- 1:10 000  

**Geographic projection / Reference System**

- ETRS_1989_LAEA (for UA2012)  

**Positional accuracy**

- ± 5 m  

**Thematic accuracy (in %)**

- Minimum Overall Accuracy (OA) for level 1 class 1 “Artificial surfaces: 85%

- Minimum OA (Rural surfaces and Overall): 80%.

- Methodology for quality control has to be performed according to RD\[1\].

- The minimum OA for level 1 class 1 “Artificial surfaces” must include both omission and commission errors with other classes within the Functional Urban Areas (FUA).

**Update frequency**

- Every 6 years  

**Base data topicality**

- Not specified  

**Delivery format**

- Topologically correct GIS files.

- Single part features.

**Data type**

- Vector  

## 9.3 Product types and attricute field descriptions

The different types of cartographic products available in the Urban Atlas are described below.

### 9.3.1 UA 2006 LULC

This data corresponds to the reviewed version of 305 FUAs produced for the Urban Atlas Land Use/Land Cover for the 2006 reference year.

| **Field Name** | **Description** | **Type** | **Length** | **Precision** | **Scale** |
|----|----|:--:|:--:|:--:|:--:|
| **COUNTRY** | country 2-letter code (e.g. DK) | String | 50 | 0 | 0 |
| **CITIES** | FUA Name (e.g. København) | String | 254 | 0 | 0 |
| **FUA_OR_CIT** | FUA ID (e.g. DK001L2) | String | 254 | 0 | 0 |
| **CODE2006** | 2006 LULC code (e.g. 50000) | String | 7 | 0 | 0 |
| **ITEM2006** | 2006 LULC class (e.g. water) | String | 150 | 0 | 0 |
| **PROD_DATE** | Map production year (e.g. 2015) | String | 4 | 0 | 0 |
| **Shape_Length** | Length of the polygon (in m) | Double | 8 | 0 | 0 |
| **Shape_Area** | Area of the polygon (in m²) | Double | 8 | 0 | 0 |

UA 2006 LULC FIELD DESCRIPTION {.caption-top .table}

### 9.3.2 UA 2012 LULC

This data corresponds to the reviewed version of the FUAs produced for the Urban Atlas Land Use/Land Cover for the 2012 reference year.

| **Field Name** | **Description** | **Type** | **Length** | **Precision** | **Scale** |
|----|----|:--:|:--:|:--:|:--:|
| **country** | country 2-letter code (e.g. DK) | String | 2 | 0 | 0 |
| **fua_name** | FUA Name (e.g. København) | String | 150 | 0 | 0 |
| **fua_code** | FUA ID (e.g. DK001L2) | String | 7 | 0 | 0 |
| **code_2012** | 2012 LULC code (e.g. 50000) | String | 5 | 0 | 0 |
| **class_2012** | 2012 LULC class (e.g. water) | String | 150 | 0 | 0 |
| **prod_date** | Map prod year-month (e.g. 2018-07) | String | 7 | 0 | 0 |
| **identifier** | Unique ID (e.g. 12-FR073L2) | String | 30 | 0 | 0 |
| **perimeter** | Length of the polygon (in m) | Double | -1 | 0 | 0 |
| **area** | Area of the polygon (in m²) | Double | -1 | 0 | 0 |
| **comment** | mmu exceptions regarding changes | String | 100 | 0 | 0 |

UA 2012 LULC FIELD DESCRIPTION {.caption-top .table}

### 9.3.3 UA 2006-2012 LULC change map

The change 2006-2012 layer is derived from the combined 2006 and 2012 UA data products and corresponds *only to the changes of Land use/Land cover* between those two dates. It concerns 305 FUAs produced for both the 2006 and 2012 reference years. The MMU is reduced up to 0.1 ha with some exceptions (see Section 4.7 LULC change layer).

| **Field Name** | **Description** | **Type** | **Length** | **Precision** | **Scale** |
|----|----|:--:|:--:|:--:|:--:|
| **COUNTRY** | country 2-letter code (e.g. DK) | String | 50 | 0 | 0 |
| **CITIES** | FUA Name (e.g. København) | String | 254 | 0 | 0 |
| **FUA_OR_CIT** | FUA ID (e.g. DK001L2) | String | 254 | 0 | 0 |
| **CODE2006** | 2006 LULC code (e.g. 50000) | String | 7 | 0 | 0 |
| **ITEM2006** | 2006 LULC class (e.g. water) | String | 150 | 0 | 0 |
| **CODE2012** | 2012 LULC code (e.g. 50000) | String | 7 | 0 | 0 |
| **ITEM2012** | 2012 LULC class (e.g. water) | String | 150 | 0 | 0 |
| **PROD_DATE** | Map production year (e.g. 2015) | String | 4 | 0 | 0 |
| **IDENT** | Unique ID (e.g. 16-DK001L2) | String | 30 | 0 | 0 |
| **Shape_Length** | Length of the polygon (in m) | Double | 8 | 0 | 0 |
| **Shape_Area** | Area of the polygon (in m²) | Double | 8 | 0 | 0 |

UA 2006-2012 LULC CHANGE FIELD DESCRIPTION {.caption-top .table}

### 9.3.4 UA 2018 LULC

This data corresponds to the Urban Atlas Land use/Land cover over 788 FUAs for the 2018 reference year.

| **Field Name** | **Description** | **Type** | **Length** | **Precision** | **Scale** |
|----|----|:--:|:--:|:--:|:--:|
| **country** | country 2-letter code (e.g. DK) | String | 2 | 0 | 0 |
| **fua_name** | FUA Name (e.g. København) | String | 150 | 0 | 0 |
| **fua_code** | FUA ID (e.g. DK001L2) | String | 7 | 0 | 0 |
| **code_2018** | 2018 LULC code (e.g. 50000) | String | 5 | 0 | 0 |
| **class_2018** | 2018 LULC class (e.g. water) | String | 150 | 0 | 0 |
| **prod_date** | Map prod year-month (e.g. 2018-07) | String | 7 | 0 | 0 |
| **identifier** | Unique ID (e.g. 12-FR073L2) | String | 30 | 0 | 0 |
| **perimeter** | Length of the polygon (in m) | Double | -1 | 0 | 0 |
| **area** | Area of the polygon (in m²) | Double | -1 | 0 | 0 |
| **comment** | mmu exceptions regarding changes | String | 100 | 0 | 0 |

UA 2018 LULC FIELD DESCRIPTION {.caption-top .table}

### 9.3.5 UA 2012-2018 LULC change map

The 2012-2018 LU/LC change layer is derived from the combined UA2012 and UA2018 data products with exceptions in order to correspond *only to the actual changes of Land Use / Land Cover* between those two dates. The MMU is reduced up to 0.1 ha with some exceptions (see further information provided in Section 4.7 LULC change layer).

| **Field Name** | **Description** | **Type** | **Length** | **Precision** | **Scale** |
|----|----|:--:|:--:|:--:|:--:|
| **country** | country 2-letter code (e.g. DK) | String | 2 | 0 | 0 |
| **fua_name** | FUA Name (e.g. København) | String | 150 | 0 | 0 |
| **fua_code** | FUA ID (e.g. DK001L2) | String | 7 | 0 | 0 |
| **code_2012** | 2012 LULC code (e.g. 50000) | String | 5 | 0 | 0 |
| **class_2012** | 2012 LULC class (e.g. water) | String | 150 | 0 | 0 |
| **code_2018** | 2018 LULC code (e.g. 50000) | String | 5 | 0 | 0 |
| **class_2018** | 2018 LULC class (e.g. water) | String | 150 | 0 | 0 |
| **prod_date** | Map prod year-month (e.g. 2018-07) | String | 7 | 0 | 0 |
| **identifier** | Unique ID (e.g. 12-FR073L2) | String | 30 | 0 | 0 |
| **perimeter** | Length of the polygon (in m) | Double | -1 | 0 | 0 |
| **area** | Area of the polygon (in m²) | Double | -1 | 0 | 0 |
| **comment** | mmu exceptions regarding changes | String | 100 | 0 | 0 |

UA 2012-2018 LULC CHANGE FIELD DESCRIPTION {.caption-top .table}

### 9.3.6 UA 2012 STL (street tree layer)

This data corresponds to the Urban Atlas - Street Tree Layer (STL) for the 2012 reference year.

| **Field Name** | **Description** | **Type** | **Length** | **Precision** | **Scale** |
|----|----|:--:|:--:|:--:|:--:|
| **COUNTRY** | country 2-letter code (e.g. DK) | String | 50 | 0 | 0 |
| **CITIES** | FUA Name (e.g. København) | String | 254 | 0 | 0 |
| **FUA_OR_CIT** | FUA ID (e.g. DK001L2) | String | 254 | 0 | 0 |
| **STL** | Legend code (0, 1, 99) | Integer | 2 | 0 | 0 |
| **Shape_Length** | Length of the polygon (in m) | Double | 8 | 0 | 0 |
| **Shape_Area** | Area of the polygon (in m²) | Double | 8 | 0 | 0 |

UA 2012 STL FIELD DESCRIPTION {.caption-top .table}

### 9.3.7 UA 2018 STL (street tree layer)

This data corresponds to the Urban Atlas - Street Tree Layer (STL) for the 2018 reference year.

| **Field Name** | **Description** | **Type** | **Length** | **Precision** | **Scale** |
|----|----|:--:|:--:|:--:|:--:|
| **country** | country 2-letter code (e.g. DK) | String | 2 | 0 | 0 |
| **Fua_name** | FUA Name (e.g. København) | String | 150 | 0 | 0 |
| **fua_code** | FUA ID (e.g. DK001L2) | String | 7 | 0 | 0 |
| **STL** | Legend code (1, 99) | Integer | 2 | 0 | 0 |
| **perimeter** | Length of the polygon (in m) | Double | -1 | 0 | 0 |
| **area** | Area of the polygon (in m²) | Double | -1 | 0 | 0 |

UA 2018 STL FIELD DESCRIPTION {.caption-top .table}

## 9.4 Urban Atlas mapping guide - change records

[TABLE]

# 11 Change Log

| Date       | Version | Summary         |
|------------|---------|-----------------|
| 2025-12-02 | 6.3.0   | Initial release |

Back to top

## Footnotes

## Reuse

EUPL (\>= 1.2)

[^1]: Allotment gardens are complexes of a few up to hundreds of land parcels assigned to residential people.

    Most of the parcels contain individual cultivation areas with fruits or vegetables, as well as a shed for tools and shelter
