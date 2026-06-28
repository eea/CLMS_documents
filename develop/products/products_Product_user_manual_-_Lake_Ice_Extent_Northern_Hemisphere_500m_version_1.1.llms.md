# PRODUCT USER MANUAL LAKE ICE EXTENT NORTHERN HEMISPHERE (LIE-NH) COLLECTION 500M NORTHERN HEMISPHERE

Copernicus Global Land Operations “Cryosphere and Water” “CGLOPS-2”

This Product User Manual provides comprehensive guidance for users of the Copernicus Global Land Service’s Lake Ice Extent Northern Hemisphere (LIE-NH) 500m product. It details the product’s daily ice, open water, and cloud classification for freshwater bodies across the Northern Hemisphere, delivered at a 0.005° spatial resolution. The document elaborates on the underlying ICEmod retrieval methodology, which utilises Sentinel-3 SLSTR optical and thermal data within a Gaussian Mixture Model framework. Furthermore, it outlines data formats, access methods, and presents robust validation results demonstrating the product’s high thematic accuracy, crucial for climate monitoring and hydrological applications.

Published

May 27, 2024

Keywords

Lake Ice Extent Northern Hemisphere, ICEmod algorithm, Sentinel-3 SLSTR data, Gaussian Mixture Model, lake ice classification, 500m spatial resolution, daily product, thematic accuracy assessment, Top-of-Atmosphere reflectance, Northern Hemisphere cryosphere

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

|  |  |  |
|----|----|----|
| Dissemination Level |  |  |
| PU | Public | X |
| PP | Restricted to other programme participants (including the Commission Services) |  |
| RE | Restricted to a group specified by the consortium (including the Commission Services) |  |
| CO | Confidential, only for members of the consortium (including the Commission Services) |  |

### 0.0.1 Document Release Sheet

|               |                  |      |      |
|---------------|------------------|------|------|
| Book captain: | Kirsikka Heinilä | Sign | Date |
| Approval:     | Roselyne Lacaze  | Sign | Date |
| Endorsement:  | Nadine Gobron    | Sign | Date |
| Distribution: | Public           |      |      |

### 0.0.2 Change Record

| Issue/Rev | Date | Page(s) | Description of Change | Release |
|----|----|----|----|----|
|  | 17.11.2020 | All | First issue | I1.1 |
|  | 28.12.2022 | All | Update of document after quality assessment | I1.2 |
|  | 27.5.2024 | All | Minor updates after external review | I1.3 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

### 0.0.3 List of Acronyms

|          |                                                    |
|----------|----------------------------------------------------|
| ATBD     | Algorithm Theoretical Basis Document               |
| C-GLOPS2 | Copernicus Global Land Operations Lot 2            |
| ECMWF    | European Centre for Middle Range Weather Forecasts |
| EO       | Earth Observation                                  |
| ESA      | European Space Agency                              |
| EU       | European Union                                     |
| FCDR     | Fundamental Climate Data Records                   |
| FMI      | Finnish Meteorological Institute                   |
| FSC      | Fractional Snow Cover                              |
| GMM      | Gaussian Mixture Model                             |
| LIE      | Lake Ice Extent                                    |
| LIE-NH   | Lake Ice Extent Northern Hemisphere                |
| MODIS    | Moderate Resolution Imaging Spectroradiometer      |
| MSI      | Multi-Spectral imaging Instrument                  |
| NIR      | Near Infrared                                      |
| NRT      | Near-Real Time                                     |
| OLCI     | Ocean and Land Colour Instrument                   |
| PUM      | Product User Manual                                |
| QAR      | Quality Assessment Report                          |
| S2       | Sentinel-2                                         |
| S3       | Sentinel-3                                         |
| SCE      | Snow Cover Extent                                  |
| SLSTR    | Sea and Land Surface Temperature Radiometer        |
| Syke     | Finnish Environment Institute                      |
| TOA      | Top of Atmosphere                                  |

# 1 BACKGROUND OF THE DOCUMENT

## 1.1 EXECUTIVE SUMMARY

Copernicus Global Land Operations Lot 2 (C-GLOPS2) is an operation of the Global Land Component, thematic domain Cryosphere and Water. It is allocated as a component of the Land service to ensure the ramp-up and the operational production of “Cryosphere and Water” related bio-geophysical parameters. Lake Ice Extent Northern Hemisphere (LIE-NH) is one of the Copernicus Global Land Service products. LIE-NH product is an ice classifier for freshwater bodies and is provided on daily basis.

The LIE-NH classifies, on pixel basis, inland/freshwater bodies as 1) Ice 2) Open water and 3) Cloud-covered. A certain class is associated to a pixel following the rule of highest probability. This probability is also given per pixel to describe the uncertainty of the classification. The gridded data product covers the Northern Hemisphere \[0–180°E, 0–180°W and 25–84°N\] in WGS-84 geographical coordinate system with a resolution of 0.005° (~500m, depending on latitude). Some lakes in the southern ranges of this area are excluded, as they are not experiencing ice cover during the year.

This document presents LIE-NH product and produces all necessary guidance to the use of the 0.005° resolution LIE-NH products.

## 1.2 SCOPE AND OBJECTIVES

One of the main objectives of Copernicus programme is to provide information on several environmental variables to the scientific community as well as other stakeholders including policy makers. This has been detailed in the Service Specifications Document (GIOGL1- ServiceSpecifications). The products are then operationally generated and delivered freely through the Copernicus Global Land portal (http://land.copernicus.vgt.vito.be) in near real-time as well as in offline.

This Product User Manual (PUM) document provides user of the data with description of the algorithm and its validation and description of the data product.

## 1.3 CONTENT OF THE DOCUMENT

This document is structured as follows:

- Chapter 2 recalls the user requirements, and the expected performance
- Chapter 3 summarizes the retrieval methodology
- Chapter 4 describes the technical properties of the product
- Chapter 5 summarizes the results of the quality assessment

## 1.4 RELATED DOCUMENTS

### 1.4.1 Applicable documents

AD1: Annex I – Technical Specifications JRC/IPR/2015/H.5/0026/OC to Contract Notice 2015/S 151-277962 of 7^(th) August 2015

AD2: Appendix 1 – Copernicus Global land Component Product and Service Detailed Technical requirements to Technical Annex to Contract Notice 2015/S 151-277962 of 7^(th) August 2015

AD3: GCOS – 245 : The 2022 GCOS ECVs Requirements (GCOS 245), WMO, 2022AD4: Copernicus Global Land Component Lots 1, 2 & 3 Operation of the Global Land Component (Framework Service Contract N° 199494, 199496, 199497, 941119): Service Specifications (CGLOPS-SSD). Issue 1.00. 24th November 2016.

### 1.4.2 Input

| Document ID | Descriptor |
|----|----|
| CGLOPS2_SSD | Service Specifications of the Global Component of the Copernicus Land Service. |
| CGLOPS2_ATBD_LIE-NH_500m-V1.1 | Algorithm Theoretical Basis Document of the LIE-NH 500m product |
| CGLOPS2_QAR\_ LIE-NH_500m-V1.1 | Report describing the results of the scientific quality assessment of the LIE-NH 500m product |

### 1.4.3 Output

| Document ID | Descriptor |
|----|----|
| CGLOPS2_PUM_LIE-NH-500m-V1.1 | Product User Manual summarizing all information about the LIE-NH 500m product |

# 2 REVIEW OF USERS REQUIREMENTS

According to the applicable document \[AD2\], the user’s requirements relevant for Northern Hemisphere LIE-NH 500m are:

- **Definition**: Lake Ice Extent Northern Hemisphere (LIE-ΝΗ)
- **Geometric properties**:
  - The target baseline location accuracy shall be 1/3 of the at-nadir instantaneous field of view.
  - Pixel coordinates shall be given for centre of pixel.
- **Geographical coverage**:
  - Projection: geographical latitude, longitude
  - Geodetical datum: WGS84, EPSG:4326
  - Pixel size: 0.005° (ca 500m, depending on latitude)
  - Coordinate position: pixel centre
    - Window coordinates:
      - Upper left: 180°W, 84°N
      - Lower right: 180°E, 25°N
- **Accuracy requirements**:

Target requirements for lake ice cover based on Global Climate Observing System (GCOS) (AD4) are following:

- Spatial resolution: 300m
- Temporal resolution: daily
- Measurement uncertainty: ≤10%

User requirements related to LIE-NH products are described by the GCOS – 245 : The 2022 GCOS ECVs Requirements (GCOS 245) (AD3) and in User Requirements of CryoLand Snow and Land Ice services - Cryoland (Malnes et al. 2015).

The main user groups with an interest in these satellite products are the climate and hydrological modelling communities and weather forecasting authorities. The following paragraphs will summarize thematic, temporal, and geometrical aspects concerning the LIE-NH product.

**Thematic aspects**

The LIE-NH product classifies a section of the freshwater body as either ice, open water or cloud-covered. The class “Ice” includes various types of ice, also snow-covered ice. The extent is usually defined in terms of area (in square kilometres). The targeted minimum measurement uncertainty is 10%, while the goal is 1% according to AD3. The thematic overall accuracy for LIE-NH reaches the goal being 99% with 1% ice commission error and 1% ice omission error. In the validation process, two different thresholds were utilized in the generation of 500m comparison dataset by aggregating the S2-based 20m reference data into 500m resolution binary (water/ice) information: (1) a 500m pixel is classified as ice-covered if the proportion of 20m ice pixels is \>50%, and 2) 500m pixel is classified as ice-covered if the proportion of 20m ice pixels is \>70%.

**Geometrical aspects**

Charting the ice on lakes over the Northern Hemisphere with a daily coverage requires the use of moderate resolution imagery. Sentinel-3 SLSTR (A/B) data provide good daily coverage over Northern Hemisphere, especially over areas where the freezing of lakes is most prominent. The current spatial resolution for global and basin-scale applications for the parameter LIE-NH is 500 m for optical data with a location accuracy of one pixel.

**Temporal aspects**

The LIE-NH 500 m is a daily product. Spatially and temporally consistent data sets are important for climate modelling and numerical weather prediction. Climate modellers need data sets over large areas (continental scale) and for long time periods (decades). Aggregated (gridded) data sets are preferred. The data sets do not need to be very frequent in time (monthly information is sufficient according to Climate modellers). For other than climatic use, Malnes et al. (2015) summarize that the majority of users request a one day temporal resolution. When often bridging the wishful thinking from users with what is actually possible to achieve with current and near future satellite sensors, it should be realistic to obtain a temporal resolution of one week, due to frequent cloud cover at high latitudes where lake ice mostly occurs. There is hence a need to also provide a level of refinement to the ice products, where temporal interpolations provide the desired temporal regularity.

**Near real-time data:**

The climate modellers have little need for real-time data: annual updates (mostly concerning ice break-up) are sufficient.

In weather prediction there is in principle a need near real time data, or at least data for the last day. The most urgent need for real time data seems to arise from the hydrological community, for whom the real time data is a pre-requisite for flood management.

**Other aspects**

Satellite data on freezing and break-up dates of lake ice is also of interest for all approached users, particularly for the validation of models. These data types can also be of interest for environmental assessment and for biological monitoring.

# 3 ALGORITHM

## 3.1 OVERVIEW

The Lake Ice Extent Northern Hemisphere (LIE-NH) product of the Copernicus Global Land Service provides three alternative classes for each pixel of a water body: 1) Ice, 2) Open water and 3) Cloud. This classification may be performed from optical satellite sensors of different resolutions. Figure 1 represents the samples of the data. The main use of the data is to define timing of events in the annual cycle of freshwater ice, i.e., the initiation of ice formation, total freeze up of lakes, initiation of melting period, and ice-out date (the day when the lake is completely ice-free). The gridded data product can also be used to monitor the extent of ice, and this is usually defined in terms of area (in square kilometers) or percentage of coverage. The LIE-NH utilizes the new *ICEmod* method to detect ice coverage (Heinilä et al. 2021). In addition to actual classification, statistical probability of the assigned class is provided for each pixel. The main advantages of the *ICEmod* are i) utilization of several spectral bands and indices, ii) inclusion of simultaneous cloud detection, iii) definition of statistical probability for each pixel, and iv) simplicity of processing and easy transition between different satellite sensors. The applied *ICEmod* algorithm currently utilizes Sentinel-3 SLSTR data in LIE-NH production.

![This map displays the Lake Ice Extent - Northern Hemisphere (LIE-NH) product, providing land cover classification for freshwater bodies. The upper map presents a broad overview of the Northern Hemisphere, including North America, Europe, and Asia. An orange bounding box highlights a specific region in Northern Europe. The lower map provides a magnified view of this highlighted area, focusing on Fennoscandia and Northwest Russia. The legend defines six categories: \* NoData: grey \* Ice: white \* Water: light blue \* Sea area: dark teal \* Cloud: yellow \* Land: tan In the Northern Hemisphere overview, white patches indicating ice are visible on lakes across northern North America and Eurasia, alongside some light blue patches for open water and yellow patches for clouds. The majority of landmass is tan, and large ocean bodies are dark teal. The magnified view shows a detailed distribution of ice (white) on numerous inland lakes in Fennoscandia and Northwest Russia. Larger areas of light blue represent open water in other inland lakes. The Baltic Sea and surrounding coastal waters are depicted as Sea area (dark teal), while the landmass is tan, with scattered small yellow patches indicating cloud cover. This map represents a daily coverage classification using satellite imagery, as used in the Copernicus Land Monitoring Service (CLMS) LIE-NH product.](products_Product_user_manual_-_Lake_Ice_Extent_Northern_Hemisphere_500m_version_1.1-media/img-668bd09261475271d19be91daaaed57f.png)

Figure 1. LIE-NH 500m product (21 March 2020). Top: the entire NH, Bottom: a closeup to Finland and its surroundings.

## 3.2 THE RETRIEVAL METHODOLOGY

### 3.2.1 Input data

The *ICEmod* algorithm uses top-of-atmosphere (TOA) data from optical satellite instruments. The classifier exploits reflectances from several bands (554 nm, 659 nm, 868 nm, 1613 nm, 2255 nm) and thermal bands (10.9 µm, 12.0 µm). Currently the LIE-NH 500m product relies on Sentinel-3 SLSTR data. Because the algorithm is based on Gaussian Mixture Model (GMM) created from representative optical satellite training dataset, it is easily transferred to any other optical satellite instrument. The algorithm benefits from the spatial averaging of medium resolution satellites (spatial resolution in the order of 100 m), but it is also applicable to higher -resolution instruments (spatial resolution of the order of 10-20 m).

#### 3.2.1.1 Auxiliary data

Land areas are masked for better visualization and for exclusion of mixed (land/water) pixels. The land mask needs to be as accurate as possible and buffered to avoid misinterpretations for shoreline pixels and for shallow waters with vegetation. Especially small-featured water bodies, such as the lakes in Finland, require accurate masking. The current land/sea/lake mask is based on following datasets:

- European Commission Global Surface Water: Water Occurrence Data
- Global Self-consistent, Hierarchical, High-resolution Geography Database (GSHHG)

Land and sea areas are masked out from the final product.

### 3.2.2 Methodology

*ICEmod* algorithm applied in LIE-NH is based on Gaussian Mixture Model (GMM) of reflectance and index distributions derived from optical satellite data (Heinilä et al. 2021). The data from an extensive set of training images from Sentinel-3 SLSTR sensor is given to GMM -model fitting algorithm, which is used to “overclassify” the set of training data, i.e., more distributions are used in the training and actual classification than in the final product where the number of classes is three (ice, open water, cloud). (CGLOPS2_ATBD_LIE-NH_500m_V1). The *ICEmod* is applied to Sentinel-3 SLSTR (A/B) sensor, and it utilizes TOA reflectance and thermal bands. Additionally, Normalized-Difference Snow Index (NDSI) and Normalized Difference Water Index (NDWI) are used. After the training of the overall distribution, the GMM model is used to predict the classes of new S3 SLSTR images. Each of the generated 21 classes are initially labelled either as ice, open water, or cloud-covered. In LIE product generation, all initial classes representing ice are combined to one single ice class, and all open water and cloud classes are combined to one open water class and one cloud class, respectively. Correspondingly, the class-wise probability estimates given by the GMM are combined to assign the pixel its probability of belonging to ice, open water, or cloud class. Schematic diagram is given in Figure 2. Some cases were excluded from the GMM model because they can be classified with imposing additional rules with very high certainty. Such cases are a high value in the thermal band (Band8\>280K) or/and a very low reflectance in the near infrared band (Band3\<0.025). In addition, the visual investigation showed that some classifications with the 500 m resolution SLSTR data were incorrect due to e.g., high turbidity of water or haze over cold water. Thus, also a set of additional rules was defined to improve the classification). Further information is given in the CGLOPS2_ATBD_LIE-NH_500m_V1.

![This histogram with overlaid curves illustrates the distribution of pixel reflectance values and their decomposition into three statistical components using a Gaussian mixture model. The Y-axis, labeled 'Number of pixels', ranges from 0 to 20x10⁵ (2,000,000). The X-axis, labeled 'Reflectance', ranges from 0.0 to 1.0. The chart displays five data series: \* 'data' (light blue shaded bars): represents the observed frequency distribution of pixel reflectance values. \* 'model' (thick red line): shows the overall fitted model curve, representing the sum of the three components. \* 'component1' (orange line): represents a unimodal distribution peaking around a reflectance of 0.3. \* 'component2' (green line): represents a unimodal distribution peaking around a reflectance of 0.45. \* 'component3' (thin red line): represents a unimodal distribution peaking around a reflectance of 0.7. The 'data' histogram shows a trimodal distribution: \* The first and highest peak is observed at approximately 0.3 reflectance, with about 21x10⁵ pixels. \* The second peak is observed at approximately 0.45 reflectance, with about 12.5x10⁵ pixels. \* The third peak is observed at approximately 0.7 reflectance, with about 9x10⁵ pixels. The 'model' curve accurately fits the combined distribution of the 'data' histogram. This decomposition into components is used by the \*ICEmod\* method for classifying pixels, likely corresponding to categories such as Ice, Open water, and Cloud, as per the Copernicus Global Land Service's Lake Ice Extent Northern Hemisphere (LIE-NH) product.](products_Product_user_manual_-_Lake_Ice_Extent_Northern_Hemisphere_500m_version_1.1-media/img-2b7765677c858a6cded92115883efb24.png)

Figure 2: Simulated example of the principle of using GMM fitting (in one dimension). For clarity, only three components are used. In ICEmod algorithm used in S3 SLSTR -based LIE, the initial number of classes (fitted distributions) is 21 and the number of dimensions is 9: SLSTR channels 1, 2, 3, 5, 6, 8 and 9 and the indices NDSI and NDWI.

### 3.2.3 Processing chain

The processing chain of LIE-NH is displayed in Figure 3. The chain takes in pre-processed top-of-atmosphere (TOA) reflectance and thermal brightness temperature data. The data is pre-processed to calibrated top-of-atmosphere (TOA) reflectance and emissivity data by ENVEO IT GmbH. Some of the southernmost areas in Northern Hemisphere are excluded from the processing to reduce the amount of processed data. These areas are excluded since the temperature does not ever draw near minus Celsius degrees. After the pre-processing the data is collected to the LIE-NH processing server. The pre-processed data is filtered by rejecting data from sun elevation \< 17° and view angle \>45°. The data is combined with the land/sea mask and the calculation is done only for lake pixels.

The processing uses channels from 500m reflectance bands (SLSTR bands: 1, 2, 3, 5 and 6), 1km thermal bands (SLSTR bands: 8 and 9) as well as indices NDWI and NDSI. The classification is made using the methodology described in section 3.2.2. After classifying the individual swaths, they are mosaicked. The result is written to a netCDF4 with associated metadata for the Copernicus Global Land Service distribution environment. Then the data is pushed to FTP server for ftp-pull from the services’ side.

![This workflow diagram outlines the two main phases for generating the Lake Ice Extent Northern Hemisphere (LIE-NH) product: \`LIE-NH GMM training\` and \`LIE-NH production\`. The \`LIE-NH GMM training\` phase consists of: 1. \`Create training data\`, which uses \`Selected SLSTR scenes\` (Sentinel-3 Sea and Land Surface Temperature Radiometer) and the \`Northern hemisphere water mask\` as inputs. 2. \`Train GMM\` (Gaussian Mixture Model) using the created training data. The output of this phase is the trained \`Gaussian Mixture Model\`, which is then used in the production phase. The \`Northern hemisphere water mask\` is also directly provided to the production phase. The \`LIE-NH production\` phase begins with \`Trigger processing\`, which consumes \`Pre-processed SLSTR Data\`. The core \`LIE-NH estimate\` process involves: 1. \`Filter pre-processd data\`, which includes parallel sub-steps: \`Select water pixels\`, \`Select valid data\`, and \`Filter with solar and viewing geometry\`. 2. \`Initial classification (21 classes)\` is performed, incorporating the \`Gaussian Mixture Model\`, \`GMM - classification\` results, a \`Check for 'True cloud'\`, and a \`Check for 'True water'\`. 3. The classification is then \`Reduce\[d\] classification to ice, cloud and open water\`. 4. \`Check additional rules\`. 5. \`Write output data\` in three formats: \`Netcdf\`, \`png\`, and \`tiff\`, corresponding to the \`LIE-NH netcdf\`, \`LIE-NH png\`, and \`LIE-NH tiff\` data products. 6. \`Archive input SLSTR data\`, which results in \`SLSTR - archived pre-processing data\`. This archived data can feed back into \`Pre-processed SLSTR Data\` for subsequent \`Trigger processing\`, forming a feedback loop.](products_Product_user_manual_-_Lake_Ice_Extent_Northern_Hemisphere_500m_version_1.1-media/img-7a33005f824ff36f6e9f9c9aaa56c697.png)

Figure 3. Processing chain for LIE-NH 500m.

## 3.3 LIMITATIONS OF THE PRODUCT

Lake Ice Extent for Northern Hemisphere (LIE-NH) is monitored daily using optical satellite data. Observations from optical satellite sensors are restricted by cloud cover as well as low light conditions from late autumn to early spring in the high northern latitudes due to the polar night. The validation of LIE-NH product revealed that almost all the inaccuracies occurred during low light conditions in late autumn and mid-winter.

Mapping of ice on lakes requires, especially in Scandinavia and North-East of North America, a fine spatial resolution watermask due to the small size of the lakes and relatively high number of islands and narrow parts in some lakes. The gridded LIE-NH data product covers the Northern Hemisphere (see geographical coverage above) with 0.005° (~500m) resolution. The shores (also in case of island) are not included in the product to avoid mixed pixels, i.e., containing both land and water/ice). Sometimes the water body dries out, which can lead incorrect ice interpretations. This risk is minimized by frequent quality assurance.

Validation results indicates that the thematic overall accuracy requirement of GCOS (AD3) can be achieved. The user is good to be aware that during the freezing and break-up of ice the method cannot always detect whether the target represents water on dark (thin, semitransparent) ice or open water. Same goes for fact that the small white ice floes within a single pixel may results the pixel being classified as ice. However, in these cases the lake ice is already fragmented and/or dark and weak and thus does not always cause disadvantage for the end users depending on the user case. The LIE-NH product itself does not contain lake morphological etc. data. If such information is desired, it is recommended that the user combines the product with another water body dataset.

## 3.4 DIFFERENCES WITH THE PREVIOUS VERSION

LIE-NH is a new product in Copernicus Global Land Service cryosphere portfolio. The *ICEmod* algorithm utilized in LIE-NH was developed at Syke and is based on a statistical analysis on the multi-spectral space. The Copernicus Global Land LIE-NH product and service builds on the legacy of the pre-operational Copernicus Global Land LIE-NE product and service for Europe, developed and implemented within the EU FP7 project (EU FP7 No 262925) (Heinilä et al. 2017). However, the *ICEmod* algorithm utilized in LIE-NH is a novel approach and does not have similarities with the previous algorithms. Likewise LIE-NE, the LIE-NH can be used to monitor the extent of ice (‘ice’ class includes various types of ice, also snow-covered), but the main use of the data is to define timing of events in the annual cycle of freshwater ice: the initiation of ice formation; freezing up of lakes; initiation of melting; ice-out date.

# 4 PRODUCT DESCRIPTION

## 4.1 FILE NAMING

The **Lake ice Extent (LIE-NH) 500m** daily product follows the naming standard: `c_gls_LIE500_<YYYYMMDD>_<AREA>_<SOURCE>_V<VERSION>`.

Example: `c_gls_LIE500_20190702_NH_S3-SLSTR_V1.1`

where,

- first `<YYYYMMDD>` gives the date of the product. YYYY, MM and DD denote the year, the month and the day, respectively.
- `<AREA>` gives the spatial coverage of the file. In LIE-NH, `<AREA>` is NH as it covers the Northern Hemisphere.
- `<SOURCE>` gives the name of the sensor used to retrieve the product. S3-SLSTR referring to Sentinel-3 SLSTR satellite sensor
- `<VERSION>` shows the processing line version used to generate these LIE-NH 500m products. The version denoted as M.m.r (e.g., 1.0.1), with ‘M’ representing the major version (e.g. V1), ‘m’ the minor version (starting from 0) and ‘r’ the production run number (starting from 1) (Table 1).

Table 1. Description of version numbering

| Version | Differences | Recommendations | Announcement |
|----|----|----|----|
| Major | Significant change to the algorithm. | Do not mix various major versions in the same applications, unless it is otherwise stated. | Via technical mailing list / website |
| Minor | Minor changes in the algorithm | Can be mixed in the same applications, but require attention or modest modifications | Via technical mailing list / website |
| Run | Fixes to bugs and minor issues. Later run automatically replaces former | Consider it as a drop-in replacement. | To affected users |

## 4.2 FILE FORMAT

The LIE-NH 500m products are delivered as a set of files:

- Single-band Network Common Data Form version 4 (netCDF4) file with metadata attributes compliant with version 1.6 of the Climate & Forecast conventions (CF V1.6) and containing the following layers:
  - LIE-NH: Lake ice extent; The LIE layer also includes flag values for sea pixels, cloud pixels and land pixels as well as statistical probability for each pixel
- A quicklook in a coloured GeoTIFF format (see Figure 4).

## 4.3 PRODUCT CONTENT

### 4.3.1 Data File

The data is a classification of lake ice state. The classes are described in Table 2.

Table 2. Classification values and descriptions for LIE-NH 500m

| Variable | Class value | Description | Scaling factor | Offset |
|----------|-------------|-------------|----------------|--------|
| LIE      | 10          | Ice cover   | NA             | NA     |
|          | 30          | Open water  | NA             | NA     |
|          | 40          | Cloud       | NA             | NA     |

The LIE-NH data layer also contains flag values (Table 3) to describe missing data (no satellite image data available), sea areas and land pixels.

Table 3. Flag values and description in the LIE 500m data product

| Variable | Flag value | Flag name       | Description             |
|----------|------------|-----------------|-------------------------|
| LIE      | 50         | not_interpreted | No satellite image data |
|          | 60         | sea_pixel       | Sea area                |
|          | 70         | land_pixel      | Land area               |

The netCDF files contain a number of netCDF metadata attributes

- on the file-level (Table 4);
- on the variable-level (Table 6);

Also, the file level variables are given in Table 5.

Table 4. Description of netCDF file attributes

[TABLE]

Table 5. Description of file-level netCDF file attributes, extensions for self-standing products.

[TABLE]

Table 6. Description of netCDF layer attributes

[TABLE]

Table 7. Description of netCDF attributes for coordinate dimensions (latitudes and longitudes).

| Attribute | Description | Data Type | Example(s) |
|----|----|----|----|
| CLASS | Dataset type | String | DIMENSION_SCALE |
| DIMENSION_LABELS | Label used in netCDF4 library | String | lon |
| NAME | Short name | String | lon |
| standard_name | A standardized name that references a description of a variable’s content in CF-Convention’s standard names table. Note that each standard_name has corresponding unit (from Unidata’s udunits). | String | longitude |
| long_name | A descriptive name that indicates a variable’s content. This name is not standardized. Required when a standard name is not available. | String | longitude |
| units | Units of the variable’s content, taken from Unidata’s udunits library. | String | degrees_east |
| axis | Identifies latitude, longitude, vertical, or time axes. | String | X |

Table 8. Description of netCDF attributes for the grid mapping variable.

[TABLE]

### 4.3.2 Quicklook

The quicklook is a GeoTIFF file (Figure 4).

![This world map provides a quicklook visualization of land and ocean, highlighting specific inland water bodies and northern regions with blue and yellow/white features. The map uses a teal colour for water bodies and a tan colour for landmasses. Prominent blue areas are visible in North America, specifically around the Great Lakes and further north in Canada, and in Central Asia, encompassing the Caspian Sea and the Aral Sea region. Smaller, more scattered yellow/white features are also visible within these blue regions and across other northern landmasses, including Siberia and the Canadian Arctic. The map covers the entire globe and is rendered in a plate carrée projection based on WGS 1984 (EPSG:4326) with a 0.005° grid resolution. This quicklook is a GeoTIFF file, representing daily composite data from the Copernicus Land Monitoring Service (CLMS) LIE-NH product collection, with prototype products having started in November 2019. The map does not include an explicit legend to specify the meaning of the blue and yellow/white features.](products_Product_user_manual_-_Lake_Ice_Extent_Northern_Hemisphere_500m_version_1.1-media/img-ecafb37fbc2ca717ebb270c149d88cb7.png)

Figure 4. Quicklook of the LIE-NH product, 27 April 2022

## 4.4 PRODUCT CHARACTERISTICS

### 4.4.1 Projection and Grid Information

The product is displayed in a regular latitude/longitude grid (plate carrée) with the ellipsoid WGS 1984 (Terrestrial radius=6378km), EPSG:4326. The resolution of the grid is 0.005°. Coordinate reference is the upper left corner of the pixel. It means that the longitude of the upper left corner of the pixel is (pixel_longitude – angular_resolution/2.)

### 4.4.2 Temporal Information

The LIE-NH products are daily composites. The generation of prototype products started in November 2019.

### 4.4.3 Data Policies

Any use of the LIE-NH 500m Product Collection implies the obligation to include in any publication or communication using these products the following citation:

“The LIE-NH product was generated by the land service of Copernicus, the Earth Observation program of the European Commission. The research leading to the current version of the product has received funding from various European Commission Research and Technical Development programs. The product is based on Sentinel-3/LSTR 500m data ((c) ESA and downlinked and distributed by Copernicus programme).”

The user accepts to inform Copernicus about the outcome of the use of the above-mentioned products and to send a copy of any publications that use these products to the following address global-land@groupcls.zohodesk.eu

### 4.4.4 Contacts

**Accountable contact**: European Commission Directorate-General Joint Research Centre

Email address: copernicuslandproducts@jrc.ec.europa.eu

**Scientific, Production and Distribution contact**: Flemish Institute for Technological Research (VITO), Belgium

Email address: global-land@groupcls.zohodesk.eu

# 5 VALIDATION

The validation was conducted in the context of comparing 20-m high resolution Lake Ice Extent (LIE) products with the LIE-NH 500m products. The dataset was spatially and temporally extensive, covering all valid cloud-free data between January 2020 to May 2022 from 45 lakes (15 lakes per each continent; Asia, Europe, North America) (Figure 5). The total number of validated cloud-free LIE-NH 500m resolution lake pixels were over ten million. The utilized images are described below:

- 44.5% of the data represent lakes that had both ice-covered and open-water pixels in the same observing time
- 32.5% of the data represent lakes that had only ice pixels in the same observing time
- 23.0% of the data represent lakes that had only water pixels in the same observing time

![A global satellite imagery map displaying the spatial distribution of selected validation locations for Lake Ice Extent (LIE-NH) products, primarily in the Northern Hemisphere. The map shows land areas in green, brown, and white (ice/snow), and oceans in dark blue. Validation locations are marked with red square and circular points. Key clusters of these points are visible across Canada, Alaska, Greenland, the Nordic countries (Norway, Sweden, Finland), and extensively across northern and central Russia. Additional scattered points appear in other regions of North America and Asia. This map illustrates the spatial coverage for the validation activities of the daily composite LIE-NH 500m products, which started in November 2019 and are compared with 20-m high-resolution Lake Ice Extent products.](products_Product_user_manual_-_Lake_Ice_Extent_Northern_Hemisphere_500m_version_1.1-media/img-dd2e25b066acd8535f43fc13dd23ecae.png)

Figure 5. Map representing the spatial coverage of selected lakes. Bounding boxes illustrate the footprint of the reference scenes.

The 20m high resolution LIE products were converted to 500m binary (ice/no-ice) by aggregating in two different ways: 1) the aggregated 500m pixel is classified as ice-covered if the proportion of 20m ice pixels is \> 50% and, 2) the aggregated 500m pixel is classified as ice-covered if the proportion of 20m ice pixels is \>70%. Considering the dataset consists mostly of complex cases (partly ice-covered lakes), the performance of the LIE-NH product was very good. The overall accuracy was 99% for both the above-mentioned thresholds (Table 9). The *ICEmod* algorithm utilized in the LIE-NH product detect different kinds of ice very well. The algorithm is also applicable to distinguish turbid cold water from ice. Almost all the inaccuracies were found during the low light conditions in late autumn and mid-winter and for the complex case lakes. For fully open lakes the ice commission error is as low as 0.05%. These rare instances of False Positives occur due to extremely cold and highly turbid water or fog over very cold water. In the case of lakes fully covered by ice, the ice omission error is 0.5%. False classifications in such cases are primarily caused by the presence of a water layer atop dark ice cover when the ice has begun melting but remains unbroken. During the freezing and break-up of ice, the product tends to exhibit a higher commission error (3.2%) than omission error (1.7%) for ice. Even rather small pieces of white ice within a 500 m S3 SLSTR pixel may increase the visible reflectance and the pixel is classified as ice. Though, even during the time the lake is only partly ice-covered the over-all accuracy is as high as over 98%. The omission errors occur when the method fails to determine whether a case represents water on dark ice or open water. A more detailed investigation on these omission errors revealed that there were no 500m reference pixels that had ice fraction of 100%. In other words, all true ice pixels incorrectly classified as water included some 20m open water pixels. Concerning the end-use of the LIE information, this is likely not crucial because in those cases, the ice is already weak (citizens), dark (earth energy budget), and partly melted (ecologist, weather modelers).

Table 9. The binary statistics with two alternative thresholds applied in generation of 500m reference ice pixels (the better ones in bold).

| Metrics | Ice if 50% or more of the high-resolution pixels are ice-covered | Ice if 70% or more of the high-resolution pixels are ice-covered |
|----|----|----|
| **Recall** | 98.9% | **99.1%** |
| **Overall accuracy, Hit rate** | **99.1%** | 99.0% |
| **Omission error** | 1.1% | **1.0%** |
| **Commission error, FAR** | **0.6%** | 1.0% |
| **Precision** | **99.7%** | 99.4% |
| **F-score** | **99.3%** | 99.2% |

The validation of cloud class was performed by visually comparing dozens of LIE-NH products with S3 OLCI/SLSTR images. The validation indicated that the *ICEmod* method distinguishes different kind of cloud covers very well from ice and water, but also gave evidence of the algorithm’s sensitivity to detect thin cloud layers especially over ice. The *ICEmod* is not very prone to classify haze or fog over open water as cloud, especially when the water is not cold. This characteristic is advantageous to the areal coverage of the ice information and is due to the utilization of thermal bands in the algorithm. Incorrect classifications (between ice and water) due to the cloud cover were very rarely found, but low light conditions and turbid water increases the possibility of errors at the edge of clouds where e.g., fog can be present.

More detailed description of the validation and the results can be found in the validation report `CGLOPS2_QAR_LIE-NH_500m-V1.1`.

# 6 REFERENCES

Doxaran, D., D., Froidefond, J. M., Lavender, S., & Castaing, P. (2002). Spectral signature of highly turbid waters: Application with SPOT data to quantify suspended particulate matter concentrations. *Remote sensing of Environment* 81(1), 2002: 149-161. doi.org/10.1016/S0034-4257(01)00341-8

Heinilä, K., Mattila, O-P., Metsämäki, S., Väkevä, S., Luojus, K., Schwaizer, G, and Koponen, S. (2021). A novel method for detecting lake ice cover using optical satellite data. *International Journal of Applied Earth Observation and Geoinformation*, 104, 102566. doi.org/10.1016/j.jag.2021.102566.

Latifovic, R., & Pouliot, D. (2007). Analysis of climate change impacts on lake ice phenology in Canada using the historical satellite data record. *Remote Sensing of Environment*, 106(4), 492–507. doi.org/10.1016/j.rse.2006.09.015

Malnes, E., Buanes, A., Nagler, T., Bippus, G., Gustafsson, D., Schiller, C., Metsämäki, S., Pulliainen, J., Luojus, K., Larsen, H.E., Solberg, R., Diamandi, A., & Wiesmann, A. (2015). User requirements for the snow and land ice services CryoLand. *The Cryosphere*, 9, 1191-1202. doi.org/10.5194/tc-9-1191-2015

Metsämäki, S., Mattila, O.-P., Pulliainen, J., Niemi, K., Luojus, K., & Böttcher, K. (2012). An optical reflectance model-based method for fractional snow cover mapping applicable to continental scale. *Remote Sensing of Environment*, 123, 508-521. doi.org/10.1016/j.rse.2012.04.010

Metsämäki, S.J., Anttila, S.T., Markus, H.J., & Vepsäläinen, J.M. (2005). A feasible method for fractional snow cover mapping in boreal zone based on a reflectance model. *Remote Sensing of Environment*, 95, 77-95. doi.org/10.1016/j.rse.2004.11.013

Perovich, D.K. (1996). *The optical properties of sea ice / Donald K. Perovich ; prepared for Office of Naval Research*. \[Hanover, N.H.\]: US Army Corps of Engineers, Cold Regions Research & Engineering Laboratory ; Springfield, Va. : Available from National Technical Information Service

Ritchie, J. C., Zimba P. V., and Everitt, J. H. (2003). Remote sensing techniques to assess water quality. *Photogrammetric Engineering & Remote Sensing* 69(6): 695-704. DOI:10.14358/PERS.69.6.695

Back to top

## Reuse

EUPL (\>= 1.2)
