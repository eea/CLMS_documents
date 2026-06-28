# ALGORITHM THEORETICAL BASIS DOCUMENT Leaf Area Index (LAI) Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) Fraction of green Vegetation Cover (FCover)

Copernicus Global Land Operations ‘Vegetation and Energy’ ‘CGLOPS-1’

This Algorithm Theoretical Basis Document details Version 2.0 of the algorithm for generating Leaf Area Index (LAI), Fraction of Absorbed Photosynthetically Active Radiation (FAPAR), and Fraction of Green Vegetation Cover (FCover) 300m products. It describes the global, 10-daily retrieval from PROBA-V Collection 2 and Sentinel-3 OLCI Top-Of-Canopy reflectance data. The document covers the neural network-based estimation, advanced compositing, smoothing, and gap-filling strategies tailored for different vegetation types, along with associated quality indicators, ensuring robust and consistent bio-geophysical monitoring for the Copernicus Land Monitoring Service.

Published

April 10, 2026

Keywords

Leaf Area Index (LAI), Fraction of Absorbed Photosynthetically Active Radiation (FAPAR), Fraction of Green Vegetation Cover (FCover), Algorithm Theoretical Basis Document (ATBD), PROBA-V Collection 2, Sentinel-3 OLCI, Neural Network Techniques (NNTs), Top-Of-Canopy (TOC) reflectance, Evergreen Broadleaf Forests (EBF) processing, Global land monitoring, Quantitative quality assessment (QA), Essential Climate Variables (ECVs)

  
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

## 0.1 Document Release Sheet

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| Book captain: | Aleixandre Verger (CREAF) | Sig | ![](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-657458e207e487c2354f754f83e448f8.png) | Date | 10.04.2026 |
| Approval: | Roselyne Lacaze (HYGEOS) | Sign | ![](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-56b13a0e89bd6c5242955f16ba4126a1.png) | Date | 10.04.2026 |
| Endorsement: | N. Gobron (JRC) | Sign |  | Date |  |
| Distribution: | Public |  |  |  |  |

## 0.2 Change Record

[TABLE]

## 0.3 List of Acronyms

| Acronym | Definition |
|----|----|
| AD | Applicable Document |
| ATBD | Algorithm theoretical based Document |
| AATSR | Advanced Along Track Scanning Radiometer |
| BELMANIP | BEnchmark Land Multisite ANalysis and Intercomparison of Products |
| C6 | Collection 6 |
| CCI-LC | Climate Change Initiative-Land Cover |
| CEOS | Committee for Earth Observation Satellite |
| CG | Crops and Grassland |
| CLMS | Copernicus Land Monitoring Service |
| COG | Cloud-Optimized Geotiff |
| CYCLOPES | Carbon cYcle and Change in Land Observational Products from an Ensemble of Satellites. |
| DBF | Deciduous Broadleaf Forest |
| DN | Digital Number |
| EBF | Evergreen Broadleaf Forest |
| FAPAR | Fraction of Absorbed Photosynthetically Active Radiation |
| FCover | Fraction of vegetation cover |
| FIPAR | Fraction of Intercepted Photosynthetically Active Radiation |
| FP5/FP7 | 5^(th) and 7^(th) Framework Programme |
| JRC | Joint Research Center |
| GAUL | Global Administrative Unit Layer |
| GBOV | Ground-Based Observations for Validation |
| GCOS | Global Climate Observation System |
| GEOCLIM | Climatology of Version1 LAI, FAPAR, Fcover VGT products |
| GLASS | Global Land Surface Satellite |
| GLOBCOVER | Global land cover from MERIS |
| GMES | Global Monitoring of Environment and Security |
| IDEPIX | Identification of Pixels processor |
| ImagineS | Implementation of Multi-scale Agricultural Indicators Exploiting Sentinels |
| LAI | Leaf Area Index |
| LSA SAF | Land Surface Analysis Satellite Applications Facility |
| MERIS | Medium Resolution Imaging Spectrometer |
| MODIS | Moderate Imaging Spectrometer |
| NDVI | Normalized Difference Vegetation Index |
| NF | Needleleaf Forest |
| NIR | Near Infrared spectral domain |
| NNT | Neural Network Technique |
| NOBS | Number of observations |
| OLCI | Ocean and Land Colour Instrument |
| PROBA-V | Project of on-board autonomy – VEGETATION instrument |
| PUM | Product User Manual |
| PV | PROBA-V |
| QA | Quantitative quality assessment |
| QAR | Quality Assessment Report |
| QC | Qualitative quality index |
| R&D | Research and Development |
| RMSE | Root Mean Square Error |
| RT | Real Time |
| S3 | Sentinel-3 |
| SAA | Sun Azimuth Angle |
| SLSTR | Sea and Land Surface Temperature Radiometer |
| SMAC | Simplified Method for Atmospheric Correction |
| SPOT | Satellite Pour l’Observation de la Terre |
| SSB | Shrubs/Savana/Bare soil |
| SSD | Service Specifications Document |
| SVP | Service Validation Plan |
| SZA | Sun Zenith Angle |
| TOA | Top of Atmosphere |
| TOC | Top of Canopy |
| VAA | Viewing Azimuth Angle |
| VGT | VEGETATION instrument onboard SPOT satellite |
| VZA | Viewing Zenith Angle |
| WGS84 | World Geodetic System 1984 |

# 1 EXECUTIVE SUMMARY

The Copernicus Land Monitoring Service (CLMS) produces a series of qualified bio-geophysical products on the status and evolution of the land surface. The products are used to monitor vegetation, crops, water cycle, energy budget and terrestrial cryosphere. Production and delivery of the parameters take place in a timely manner and are complemented by the constitution of long-term time series.

From 1^(st) January 2013, the Copernicus Land Monitoring Service is providing Essential Climate Variables like the Leaf Area Index (LAI), the Fraction of Absorbed Photosynthetically Active Radiation absorbed by the vegetation (FAPAR), as well as the Fraction of Green Vegetation Cover (FCover), every 10 days over the globe, on a reliable and automatic basis from Earth Observation satellite data.

The operations of the CLMS are supported by a number of research and development initiatives. Among them, the FP7 ImagineS project (http://FP7-imagines.eu) set-up the Version 1.0 of the algorithm retrieving the LAI, FAPAR, FCover 300m products from PROBA-V data The Version 1.0 of these products, produced and delivered in near Real Time (RT), were derived from PROBA-V Collection 1 data from January 2014 to June 2020, end of the operational PROBA-V mission.. The Version 1.1. of the algorithm was adapted to the imagery of the Ocean and Land Colour Instrument (OLCI) onboard the Sentinel-3 platform. The Version 1.1 Sentinel-3 products were delivered from July 2020 ensuring the continuity of PROBA-V LAI, FAPAR, and FCover 300m products. The quality assessment was reported in \[CGLOPS1_QAR_LAI\[FAPAR/FCOVER\]300m-V1.1\]. Some marginal inconsistencies were identified between PROBA-V and Sentinel-3 300m products due to the differences between Version 1.0 and Version 1.1 retrieval algorithms and input auxiliary data, and because of some issues in the implementation of Version 1.0 and Version 1.1 algorithms. Further, the Collection 2 of PROBA-V data has been released in March 2023. To improve the consistency of the long time series of LAI, FAPAR and FCover products at 300m resolution from 2014 to present, we have adapted Version 1.1 to the characteristics of PROBA-V Collection 2 input data and to the Version 2.3 of Sentinel-3 OLCI surface reflectance for the reprocessing of the entire time series, from PROBA-V and Sentinel-3, resulting in Version 2.0 algorithm.

This Algorithm Theoretical Based Document (ATBD) describes the Version 2.0 of the algorithm for the generation of LAI, FAPAR and FCover 300m products from PROBA-V Collection 2 (2014-2018) and Sentinel-3 OLCI (2019-present) data. The variables are calculated globally on a 10-daily basis and made available to the user in near-real time every 10 days. The product is projected on a regular latitude/longitude grid with a resolution of 1/336°. It is delivered covering the whole globe (from - 180°E to +180°W and from +85°N to -65°S) and provided in netCDF4-CF format (by default format) containing the variables values (LAI, FAPAR and FCover), associated with some quantitative and qualitative quality indicators.

# 2 BACKGROUND OF THE DOCUMENT

## 2.1 SCOPE AND OBJECTIVES

CLMS supports applications in a variety of domains such as spatial and urban planning, forest management, water management, agriculture and food security, nature conservation and restoration, rural development, ecosystem accounting and mitigation/adaptation to climate change. The products are then operationally generated and delivered freely in near real time through the CLMS portal (https://land.copernicus.eu).

This document provides a detailed description and justification of the algorithm proposed for Version 2.0 of the algorithm of the LAI, FAPAR and FCover 300m derived from PROBA-V and Sentinel-3 Top-Of-Canopy (TOC) reflectance.

A theoretical validation is done including a comparison with Version 1.0 of PROBA-V 300m products (Fuster et al. 2020) and MODIS Collection 6 products (Myneni et al. 2002; Yan et al. 2016a; Yan et al. 2016b). Further validation of the products is completed by a full quality assessment analysis according to the Product Quality Assurance Document \[CGLOPS1_PQAD\].

## 2.2 CONTENT OF THE DOCUMENT

This document is structured as follows:

- Chapter 2 recalls the requirements
- Chapter 3 contains the definition of the proposed products, a description of the input data and the outline of the algorithm
- Chapter 4 describes in detail the algorithm
- Chapter 5 presents the algorithm performance

## 2.3 RELATED DOCUMENTS

### 2.3.1 Applicable documents

AD1: Part 2: Technical specifications of Framework Service Contract – Operation of the bio-geophysical variables systematic monitoring of the Global Land Component of the Copernicus Land Service ‘CGLOPS’ JRC/2023/OP/0273, 19^(th) April 2023.

Available at https://etendering.ted.europa.eu/cft/cft-display.html?cftId=13795

### 2.3.2 Input

| Document ID | Descriptor |
|----|----|
| CGLOPS1_PQAD | Product Quality Assurance Document of the Copernicus Land Monitoring Service for “Vegetation and Energy” products |
| CGLOPS1_ATBD_S3-AC-V1 | Algorithm Theoretical Basis Document of the atmospheric corrections applied on the Sentinel-3 data |
| CGLOPS1_QAR_S3-CloudMask | Report presenting the evaluation of Sentinel-3 OLCI and SLSTR cloud, cloud shadow and snow masks. |
| CGLOPS1_PUM_S3-TOC-Reflectance300m-V2.3 | Product User Manual of Sentinel-3 OLCI and SLSTR Top-Of-Canopy Reflectance Version 2.3 |
| CGLOPS1_QAR_LAI\[FAPAR/FCOVER\] 300m-V1 | Quality assessment report of the LAI, FAPAR, FCover 300m Version 1.0 PROBA-V products |
| CGLOPS1_QAR_LAI\[FAPAR/FCOVER\] 300m-V1.1 | Quality assessment report of the LAI, FAPAR, FCover 300m Version 1.1 Sentinel-3 products |

These documents are available on the CLMS website, in the Technical Library: https://land.copernicus.eu/en/technical-library

### 2.3.3 Output

CGLOPS1_PUM_LAI\[FAPAR/FCOVER\] 300m-V2.0  
Product User Manual summarizing all information about LAI, FAPAR, FCover 300m Version 2.0 product

CGLOPS1_VR_LAI\[FAPAR/FCOVER\]300m-V2.0  
Validation Report of the LAI, FAPAR, FCover 300m Version 2.0 product

These documents are available on https://land.copernicus.eu/en/technical-library

### 2.3.4 External documents

| Document ID | Descriptor |
|----|----|
| ImagineS_RP2.1_ATBD-LAI300m_I1.73 | Algorithm Theoretical Basis Document describing the retrieval methodology of the Version 1.0 of LAI, FAPAR, FCover 300m from PROBA-V, set-up in the context of the FP7/ImagineS project. |

Available on: https://land.copernicus.eu/en/technical-library

PROBAV_PUM_C2  
PROBA-V Collection 2 Products User Manual v1.0, 27 March 2023

Available at https://proba-v.vgt.vito.be/sites/probavvgt/files/downloads/PROBA-V_C2_Products_User_Manual.pdf

ACRI-ST, 2017  
Product Data Format Specification – OLCI Level 1 products, available at:

https://sentinels.copernicus.eu/documents/247904/4812102/S3IPF_PDS_004.1\_-*i2r5*–*Product_Data_Format_Specification*–\_OLCI_Level_1.pdf

GCOS#245  
The 2022 GCOS ECVs Requirements

Available online at : https://library.wmo.int/records/item/58111-the-2022-gcos-ecvs-requirements-gcos-245?offset=1

# 3 REQUIREMENTS

According to the applicable document \[AD1\], the requirements relevant for LAI, FAPAR, FCover products are described below.

## 3.1 SPECIFIC TECHNICAL DETAILS AND REQUIREMENTS

|  |  |
|----|----|
| PRODUCT SPECIFICATION |  |
| Geometric Properties: |  |
| Baseline dataset pixel resolution | 300m |
| Target baseline location accuracy | Better than 0.5 pixels |
| Coordinate position | Centre of the pixel |
| Geodetical datum | WGS84 |
| Geographic projection | Regular latitude/longitude grid |
| Geographic coverage: | Global |
| Temporal resolution | 10-day period (dekad: days 1-10, 11-20, 21 end of month) |
| Timeliness | Within 2 days (optimally 1 day) after the end of each dekad |

[TABLE]

[TABLE]

[TABLE]

## 3.2 FURTHER REQUIREMENTS

### 3.2.1 Output product composition

Products may contain various information layers and ancillary information – the base reference for product packages are the operational products as on 01.03.2023.

### 3.2.2 Data structure

Data coding[^1] shall be compatible with the Global Land products as on 01.03.2023 and/or follow the INSPIRE specifications, where applicable.

Ancillary information shall be as currently used and include at least the following:

- The number of measurements per pixel used to generate any synthesis product
- The per-pixel date of the individual measurement or the start-end dates of the period covered
- Quality indicators, with explicit per-pixel identification of the cause of anomalous parameter result.

The product naming and filename conventions that are used in the Copernicus Global Land component production as on 01.03.2023 shall be followed. This may be adapted for complete product collections upon agreement with the contracting authority during the Framework.

### 3.2.3 Data format

To ensure interoperability with the current Global Land component (operational product data formats and archive data formats) and other Copernicus services, all datasets will be available in NETCDF. Additional format such as Cloud Optimized Geotiff (COG) or ZAR format can be proposed for production or could be requested by the Contracting Authority during the Framework Contract.

### 3.2.4 Uncertainties and validation

Uncertainties indicated in the product specifications above follow the threshold and goal proposed by GCOS#245.

Uncertainties estimates should account for the error propagation uncertainty coming from input data though the retrieval algorithms as during the contract period, ESA plans to imbed uncertainties in the Sentinel-3 ground segment products and, for Sentinel-2, there is an offline tool to determine Level 1 uncertainties; these can be used for propagation in the production chain.

Validation of the products shall conform to at least the CEOS LPV standards. Wherever appropriate the bio-geophysical variables shall be validated and compared to CEOS CAL/VAL data sets and/or Ground-Based Observations for Validation (GBOV) of Copernicus Global Land component of Copernicus Global Land component when biophysical parameters are available.

### 3.2.5 Input data

Copernicus sentinel data are available from https://dataspace.copernicus.eu

Bio-geophysical variable products should be based on common base reflectance data:

- Sentinel 3: Derived Top-of-Canopy reflectance may be brokered or produced as it is the case on 01.03.2023 under the CGLOPS contracts;
- Sentinel 2: the Global Land Sentinel-2 Global Mosaic (S2GM)² component provides temporal mosaic of surface spectral bands that can be brokered and/or directly used.

Up to and including 2019, products archives of the Global Land Component have been based on SPOT VGT, Proba-V, ENVISAT, MODIS, TOPEX/Poseidon, Jason-1, Jason-2, Jason-3, datasets, which are available through the https://dataspace.copernicus.eu.

LST and SWI can be based on geostationary and other satellite data.

Ancillary satellite data that is purchased through Copernicus and put at disposal of the Services is available through the Data Warehouse and will become available on the Copernicus Dataspace Ecosystem.

Ancillary data sets, other than satellite imagery described above, that might be required shall be the responsibility of the contractor.

²

### 3.2.6 Product delivery

Products shall be delivered to the Copernicus Land Component dissemination. The Copernicus Data Space Ecosystem infrastructure will be used to provide access to the final map products.

# 4 OVERVIEW

## 4.1 THE CONSIDERED PRODUCTS

The considered products correspond to actual vegetation biophysical variables that are defined below.

### 4.1.1 Leaf Area Index (LAI)

LAI is defined as one half the total green (i.e., photosynthetically active) leaf area per unit horizontal ground surface area (Chen and Black 1992). LAI is a non-dimensional quantity, although units of m²/m² are often quoted. It determines the size of the interface for exchange of energy (including radiation) and mass between the canopy and the atmosphere. This is an intrinsic canopy primary variable that should not depend on observation conditions. LAI is strongly non-linearly related to reflectance. Therefore, its estimation from remote sensing observations is scale dependent (Garrigues et al. 2006; Weiss et al. 2000). Note that vegetation LAI as estimated from remote sensing includes all the green contributors such as the understory when existing under forests canopies.

### 4.1.2 FAPAR

The FAPAR is defined as the fraction of photosynthetically active radiation (PAR; solar radiation reaching the surface in the 0.4-0.7µm spectral region) that is absorbed by vegetation. FAPAR is expressed as a unitless fraction of the incoming radiation received at the land surface. The FAPAR value results directly from the radiative transfer in the canopy. FAPAR is the sum of two terms, weighted by the diffuse fraction in the PAR domain: the ‘black sky’ FAPAR that corresponds to the direct component (collimated beam irradiance in the sun direction only) and the ‘white sky’ or the diffuse component. FAPAR can be computed at a given time (e.g instantaneous FAPAR at the actual sun position of measurement) or daily integrated.

FAPAR depends on canopy structure, vegetation element optical properties and illumination conditions (Baret et al. 2007). It is very useful as input to a number of primary productivity models based on simple efficiency considerations (McCallum et al. 2009; Prince 1991). Most of the primary productivity models using this efficiency concept are running at the daily time step. Since the CLMS FAPAR product is originally derived from CYCLOPES FAPAR at 10:00 (Baret et al. 2007) and MODIS aboard Terra FAPAR at 10:30 (Myneni et al. 2002), CLMS FAPAR product is defined as the black-sky fraction of PAR absorbed by green elements including over and understorey vegetation at 10:15 (actually between 10:00 and 10:30) which is a good approximation of the daily integrated black-sky FAPAR value (Baret et al. 2007).

FAPAR is relatively linearly related to reflectance values, and is little sensitive to scaling issues (Hilker et al. 2010; Weiss et al. 2000). Note also that the FAPAR refers only to the green parts of the canopy.

### 4.1.3 Fraction of green Vegetation Cover (FCover)

FCover is defined as the fraction of ground surface covered by green vegetation as seen from the nadir direction (Baret et al. 2013). This definition agrees with the definition of LSA SAF FCover products (https://landsaf.ipma.pt/en/products/vegetation/fvc/) as well as the GLASS FCover product (Jia et al. 2015). FCover is expressed as a unitless fraction of the ground surface.

FCover is used to separate vegetation and soil in energy balance processes, including temperature and evapotranspiration. It is computed from the leaf area index and other canopy structural variables and does not depend on variables such as the geometry of illumination as compared to FAPAR. For this reason, it is a very good candidate for the replacement of classical vegetation indices for the monitoring of green vegetation. Because of its quasi-linear relationship with reflectances, FCover is only marginally scale dependent (Weiss et al. 2000). Note that similarly to LAI and FAPAR, only the green elements are considered.

## 4.2 PROBA-V INSTRUMENTS AND DATA

The PROBA-V Collection 2 (C2) daily synthesis (S1) top of canopy (TOC) reflectance products \[PROBAV_PUM_C2\] have been used in Version 2.0 of 300m algorithm.

The PROBA-V sensor has been launched on 6^(th) May 2013 onboard the PROBA platform. It was designed to bridge the gap in space-borne vegetation measurements between SPOT-VGT (March 2018 - May 2014) and the Sentinel-3 satellites launched in 2016. The mission objective is to ensure the continuity with the heritage of the SPOT-VGT mission.

PROBA-V operated at an altitude of 820 km altitude in a sun-synchronous orbit with a local overpass time at launch of 10:45 h. Because the satellite had no onboard propellant, the overpass time was expected to gradually differ from the at-launch value. After launch, the local overpass time first increased to 10:50h in October 2014, followed by a decrease to 10:45h in June 2016. By end-of-mission in June 2020, the Local Time of Descending Node will be at ~09:30h.

The instrument had a Field of View of 102°, resulting in a swath width of 2295 km. This swath width ensured a daily near-global coverage (90%) and full global coverage is achieved every 2 days. An array of 6000x4 elements was used in the VIS-NIR (only 3 bands on the 4 potential ones are used) yielding to a ground sampling distance that varied across the swath from 100m up to 350m at the extremities of the swath (Figure 1, left). The SWIR domain was sampled using 3 arrays of 1024 elements, providing a ground sampling distance about twice as that in the VIS-NIR (Figure 1, right).

This obviously posed a problem regarding the consistency of the radiometric information between the VIS-NIR and SWIR domains.

The optical design of PROBA-V consisted of three cameras. Each camera had two focal planes, one for the short-wave infrared (SWIR) and one for the visible and near-infrared (VNIR) bands. The VNIR detector consisted of four lines of 5200 pixels. Three spectral bands were implemented, comparable with SPOT-VGT: BLUE, RED, and NIR (see Table 1). The SWIR detector was a linear array composed of three staggered detectors of 1024 pixels. The normalized spectral response functions of the four spectral bands of PROBA-V are shown in Figure 2.

The PROBA-V processing was described in Sterckx et al. (2014) and Dierckx et al. (2014). Information on the PROBA-V Collection 2 is available on https://proba-v.vgt.vito.be/en/quality/product-and-algorithm-information. The description of the PROBA-V S1 TOC products is summarized in Table 2 and detailed in the Product User Manual \[PROBAV_PUM_C2\].

![Two side-by-side line charts display GPS positional error in metres (Y-axis) against swath distance in kilometres (X-axis) for a flight altitude of 820 km. Both X-axes range from -1250 km to 1250 km. A vertical red line is present at approximately -1125 km on both charts. The \*\*left chart\*\* shows data for the Red spectral band. The Y-axis, labelled 'GPS \[m\]', ranges from 0 to 400 m. There are six data series: \* 'Red-SI1 - Across' (blue line) decreases from approximately 350 m at -1250 km swath to a minimum of about 100 m at -250 km, then increases rapidly. \* 'Red-SI2 - Across' (green line) decreases from approximately 165 m at -1250 km swath to a minimum of about 90 m at 0 km, then increases. \* 'Red-SI3 - Across' (red line) increases from approximately 100 m at 250 km swath to about 350 m at 1250 km. \* 'Red-SI1 - Along' (light blue line) shows a flatter curve, decreasing from about 165 m at -1250 km to approximately 100 m at -250 km, then increasing. \* 'Red-SI2 - Along' (light green line) is the lowest and flattest curve, decreasing from about 100 m at -1250 km to approximately 90 m at 0 km, then increasing. \* 'Red-SI3 - Along' (light red line) increases from approximately 95 m at 250 km to about 165 m at 1250 km. The 'Across' series generally exhibit higher GPS errors and steeper increases with swath distance compared to their 'Along' counterparts. Minimum GPS errors are observed around the 0 km swath. The \*\*right chart\*\* shows data for the Short-Wave Infrared (SWIR) band, with an additional specification: 'Length SWIR detector 69.55 mm'. The Y-axis, labelled 'GPS \[m\]', ranges from 0 to 700 m. There are six data series: \* 'SWIR-SI1 - Across' (dark blue line) decreases from approximately 670 m at -1250 km swath to a minimum of about 190 m at -250 km, then increases. \* 'SWIR-SI2 - Across' (dark green line) decreases from approximately 310 m at -1250 km swath to a minimum of about 180 m at 0 km, then increases. \* 'SWIR-SI3 - Across' (dark red line, which transitions to an orange line for swath values above approximately 300 km) increases from about 190 m at 250 km swath to approximately 670 m at 1250 km. \* 'SWIR-SI1 - Along' (light blue line) decreases from approximately 310 m at -1250 km to approximately 190 m at -250 km, then increases. \* 'SWIR-SI2 - Along' (light green line) decreases from approximately 200 m at -1250 km to about 180 m at 0 km, then increases. \* 'SWIR-SI3 - Along' (orange line) increases from approximately 180 m at 250 km to about 300 m at 1250 km. Similar to the Red band data, the 'Across' components for the SWIR band show significantly higher GPS errors and steeper curves than the 'Along' components, with errors peaking at the edges of the swath. The SWIR band generally exhibits higher GPS errors than the Red band for comparable swath distances and SI components.](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-5517acf30694947368d1b2005c5aaa76.png)

Figure 1: Ground sampling distance (GPS in m) as a function of the position on the swath (in km) for the VIS-NIR (left) and SWIR bands (right).

: Table 1: PROBA-V spectral characteristics: band center and width. The spectral bands selected for Version 2.0 of LAI, FAPAR, FCover 300m algorithm are highlighted in bold.

|  |  |  |  |
|----|----|----|----|
| **Acronym** | **Center (nm)** | **Width (nm)** | **Potential Applications** |
| B0 (blue) | 463 | 46 | Continental ecosystems - Atmosphere |
| **B2 (red)** | **655** | **79** | **Continental ecosystems** |
| **B3 (NIR)** | **845** | **144** | **Continental ecosystems** |
| **SWIR** | **1600** | **73** | **Continental ecosystems** |

![Line chart displaying the normalized Spectral Response Function (SRF) for four PROBA-V S1 satellite sensor bands: BLUE, RED, NIR (Near-Infrared), and SWIR (Shortwave Infrared). The Y-axis represents normalized SRF, ranging from 0 to 1.0. The X-axis represents wavelength in nanometres (nm), ranging from 400 nm to 1800 nm. The chart shows distinct spectral windows for each band: - The BLUE band (blue line) has a response from approximately 420 nm to 520 nm, peaking near 1.0 between 460 nm and 500 nm. - The RED band (red line) has a response from approximately 620 nm to 710 nm, peaking near 1.0 between 650 nm and 700 nm. - The NIR band (purple line) has a broader response, starting around 760 nm, peaking near 1.0 between 770 nm and 800 nm, and gradually decreasing to 0 around 950 nm. - The SWIR band (olive green line) shows a response from approximately 1500 nm to 1680 nm, peaking near 1.0 between 1580 nm and 1620 nm.](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-75896144cd51f83cd4b571f6f77ae4a9.png)

Figure 2: PROBA-V normalized spectral response function.

: Table 2: PROBA-V S1 data descriptor

PROBA-V planes

Description

B0

B0 spectral band, Radiometry data

B2

B2 spectral band, Radiometry data

B3

B3 spectral band, Radiometry data

SWIR

SWIR spectral band, Radiometry data

NDVI

Normalized Difference Vegetation Index data

QC

Quality Control  
Bit NR 7: Radiometric quality for B0 coded as 0 if bad and 1 if good  
Bit NR 6: Radiometric quality for B2 coded as 0 if bad and 1 if good  
Bit NR 5: Radiometric quality for B3 coded as 0 if bad and 1 if good  
Bit NR 4: Radiometric quality for MIR coded as 0 if bad and 1 if good  
Bit NR 3: land code 1 or water code 0  
Bit 2: snow/ice code 1 or code 0 if no ice/snow  

Bit 1: 0 0 1 1 0 Bit 0: 0 1 0 1 0 Clear Shadow Undefined Cloud Ice

VZA-VNIR

view zenith angles for Visible and Near Infra-Red channels

VAA-VNIR

view azimuth angles for Visible and Near Infra-Red channels

VZA-SWIR

View zenith angles for SWIR channel

VAA-SWIR

View azimuth angles for SWIR channel

SZA

sun zenith angles

SAA

sun azimuth angles

TIME

Observation timing information

## 4.3 SENTINEL-3 INSTRUMENTS AND DATA

Sentinel-3 is a constellation of at least 2 identical satellites, Sentinel-3A and 3B. Sentinel-3A was launched on 16 February 2016 with 4 instruments on board (Figure 3) followed by the launch of Sentinel-3B on 25 April 2018. Each satellite operates in a reference orbit with a repeat cycle of 27 days, with a 4-day sub-cycle. The use of Sentinel-3A and Sentinel-3B satellites in conjunction enable a short revisit time of less than two days at the equator.

![A depiction of a gold-coloured Sentinel-3 Earth observation satellite in orbit, showing a blue solar array extending to the left and a curved segment of Earth visible at the bottom. Two key instruments are highlighted and labelled: the Ocean and Land Colour Instrument (OLCI), indicated by green text 'OLCI' and a green circle around the satellite's top section; and the Sea and Land Surface Temperature Radiometer (SLSTR), indicated by red text 'SLSTR' with a red arrow pointing to and a red rectangle outlining a section on the side of the satellite body.](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-ee87b493b042bc83425dd2317df9a77f.png)

Figure 3: The Sentinel-3 platform with the Ocean and Land color Imager (OLCI) and Sea and Land Surface Temperature Radiometer (SLSTR) instruments.

![Line chart illustrating the spectral response of an instrument, likely the Sentinel-3 Ocean and Land Colour Imager (OLCI), across a wavelength range from 300 nm to 1100 nm. The Y-axis represents 'Spectral response' from 0 to 1, and the X-axis represents 'Wavelength (nm)'. The chart displays approximately 15 distinct spectral bands as narrow black lines, showing a high spectral response (close to 1) within very specific wavelength ranges, from roughly 400 nm to 900 nm. A continuous red line represents a broader spectral response curve, showing high sensitivity regions (close to 1) between 400-500 nm, 550-600 nm, and 650-800 nm, before gradually declining to zero around 950 nm. This broader curve appears to encompass or indicate the general operational sensitivity envelope for the discrete bands.](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-810a4cd96d15faa44a506ca5cdf9583a.png)

Figure 4: Spectral response of PROBA-V (red) and OLCI (black) selected bands (Oa4-12, Oa16-18; Table 3) for LAI, FAPAR, FCover 300m products.

: Table 3: Sentinel-3 OLCI spectral characteristics: band center and width. The spectral bands selected for LAI, FAPAR, FCover 300m algorithm are highlighted in bold.

|  |  |  |  |
|----|----|----|----|
| **Band** | **λ centre (nm)** | **Width (nm)** | **Potential Application** |
| Oa1 | 400 | 15 | Aerosol correction, improved water constituent retrieval |
| Oa2 | 412.5 | 10 | Yellow substance and detrital pigments (turbidity) |
| Oa3 | 442.5 | 10 | Chlorophyll absorption max., biogeochemistry, vegetation |
| **Oa4** | **490** | **10** | **High Chlorophyll, other pigments** |
| **Oa5** | **510** | **10** | **Chlorophyll, sediment, turbidity, red tide** |
| **Oa6** | **560** | **10** | **Chlorophyll reference (Chlorophyll minimum)** |
| **Oa7** | **620** | **10** | **Sediment loading** |
| **Oa8** | **665** | **10** | **Chlorophyll (2nd Chlorophyll abs. max.), sediment, yellow substance /vegetation** |
| **Oa9** | **673.75** | **7.5** | **For improved fluorescence retrieval and to better account for smile together with the bands 665 and 680 nm** |
| **Oa10** | **681.25** | **7.5** | **Chlorophyll fluorescence peak, red edge** |
| **Oa11** | **708.75** | **10** | **Chlorophyll fluorescence baseline, red edge transition** |
| **Oa12** | **753.75** | **7.5** | **Oxygen absorption/clouds, vegetation** |
| Oa13 | 761.25 | 2.5 | Oxygen absorption band/aerosol correction |
| Oa14 | 764.375 | 3.75 | Atmospheric correction |
| Oa15 | 767.5 | 2.5 | Oxygen absorption band used for cloud top pressure, fluorescence over land |
| **Oa16** | **778.75** | **15** | **Atmospheric correction/aerosol correction** |
| **Oa17** | **865** | **20** | **Atmospheric correction/aerosol correction, clouds, pixel co-registration** |
| **Oa18** | **885** | **10** | **Water vapour absorption reference band. Common reference** |
| Oa19 | 900 | 10 | Water vapour absorption, vegetation monitoring |
| Oa20 | 940 | 20 | Water vapour absorption, atmos./aerosol corr. |
| Oa21 | 1 020 | 40 | Atmospheric correction/aerosol correction |

The satellite flies at 814 km altitude on a circular sun-synchronous orbit with 10:00 am equatorial crossing time. The two optical instruments, OLCI (300m resolution) and SLSTR (500m resolution for optical bands and 1km for thermal ones) provide a common quasi-simultaneous view of the Earth. The SLSTR data is not used due to its lower spatial resolution. The OLCI has a swath of 1269 km, a field of view of 68° and 21 spectral channels (Table 3). The field-of-view is divided between five cameras on a common structure with the calibration assembly. Each camera has an optical grating to provide the minimum baseline of 16 spectral bands required by the mission together with the potential for optional bands for improved atmospheric corrections (Table 3 and Figure 4). Although preliminary designed for ocean applications, OLCI is fully suitable for land applications, considering its spectral characteristics and spatial resolution.

The instantaneous top of canopy (TOC) reflectance products \[CGLOPS1_PUM_S3-TOC-Reflectance300m-V2.3\] from OLCI in 12 spectral bands (Oa4-12 and Oa16-18, Figure 4 and Table 3) have been used in LAI, FAPAR, FCover 300m algorithm.

## 4.4 RATIONALE FOR THE ALGORITHM SELECTION AND DESIGN

The objective is to develop an algorithm dedicated to the estimation of Version 2.0 of LAI, FAPAR and FCover 300m from the PROBA-V (2014-2018) and Sentinel-3 (2019-present) series of observations. The algorithm should provide high level of consistency with Version 1.0 of PROBA-V products. The Version 2.0 of LAI, FAPAR and FCover 300m products should have the same temporal sampling frequency of 10 days. Products should also be associated with quality assessment flags as well as quantified uncertainties. The algorithm runs at the pixel level without interactions with the surrounding pixels. The algorithm should provide real time estimation. This forces to perform short term projection of the product dynamics.

Version 1.0 of 300m algorithm was set-up in the ImagineS project \[ImagineS_RP2.1_ATBD-LAI300m_I1.73\]. After the quality assessment of the 300m LAI, FAPAR, FCover Version 1.0 \[CGLOPS1_QAR_LAI\[FAPAR/FCOVER\]300m-V1\], the methodology has been adapted to reduce the noise in the product time series especially in near real time mode and to address external recommendations and operational constraints in CLMS. This ATBD describes the Version 2.0 of the retrieval algorithm. Since the performance of LAI, FAPAR, FCover estimates is highly dependent on the level of noise in the input reflectance data, Top of Atmosphere (TOA) reflectance used in Version 1.0 have been replaced by TOC reflectance in the Version 2.0 of the algorithm. Further, the parametrization of the algorithm has been adapted in Version 2.0 to the characteristics of PROBA-V Collection 2 and Sentinel-3 Version 2.3 TOC reflectances. The neural networks used to transform PROBA-V and Sentinel-3 TOC reflectance into instantaneous LAI, FAPAR and FCover estimates have been calibrated with current Version 1.0 PROBA-V 300m LAI, FAPAR, FCover products to ensure a good agreement and temporal consistency in the transition from PROBA-V to Sentinel-3. Details of the Version 2.0 of LAI, FAPAR and FCover 300m are provided in Chapter 4. The differences with previous versions are detailed in Section 4.5.

## 4.5 ALGORITHM OUTLINE

The scheme proposed for the 300m products retrieval methodology is sketched in Figure 5. The algorithm starts from instantaneous TOC reflectance products which are first transformed into instantaneous estimates of LAI, FAPAR, FCover (Step A in Figure 5). This Step A is sensor specific. Then, smoothing and gap filling is achieved over a compositing temporal window that may be dissymmetric as in the case of the near-real time situation or at the beginning of the time series (Step B in Figure 5).

Two different processing chains are applied whether the pixel’s biome is an Evergreen Broadleaf Forests (EBFs) or not to account the specific behaviors of EBFs: (i) lower near infrared reflectance level for a given LAI value mainly due to thicker leaves, and (ii) high level of noise in the time series due to the remaining atmospheric effects and cloud contamination in regions characterized by a high occurrence of clouds. Gap filling is only applied for EBFs.

![This diagram illustrates the algorithm workflow for generating Leaf Area Index (LAI), Fraction of Absorbed Photosynthetically Active Radiation (FAPAR), and Fraction of Green Vegetation Cover (FCover) products. The process begins with 'TOC reflectances' (Top Of Canopy reflectances) as a primary input. Additional inputs to the 'Instantaneous Estimates' processing step include 'Definition Domain', 'NNT coefficients', and 'Lat, Lon' (Latitude, Longitude). This 'Instantaneous Estimates' step, associated with a partially visible 'S' (likely indicating 'Step 1'), produces 'Instantaneous LAI, FAPAR, FCOVER' products. These instantaneous products, along with 'CCI-LC' (likely referring to Climate Change Initiative Land Cover data), serve as inputs to the subsequent 'Compositing, Smoothing & Gap filling' process. This step, also associated with a partially visible 'S' (likely 'Step 2'), then generates the final 'Dekadal LAI, FAPAR, Fcover' products. The 'Dekadal' term refers to a 10-day composite period.](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-6a051e2663a7dbaba5eea18d9e05a6c1.png)

Figure 5: Flow chart showing the two processing steps in Version 2.0 LAI, FAPAR, FCover 300m algorithm.

The selection of the instantaneous estimates considered as valid in the compositing window (Step B) is made based on the LAI product.

The compositing for real time estimates (Step B) is achieved according to the scheme described in Figure 6. We consider a particular dekadal date, D.

- In real time mode, RT0 (when the actual date corresponds to D, i. e. the first line in Figure 6), the compositing is achieved using only the past observations, with a maximum compositing window spanning c- days in the past (c. was set to 210 days for EBF and 60 days for nonEBF). The value of the product at dekadal date D is therefore relatively unstable in the presence of noisy and missing data.
- Then, the observations accumulate after dekadal date D when time passing. The value at dekadal date D is updated using the observations available after dekadal date D within the consolidation period. The accuracy of the product value progressively improves during this consolidation period.
- At the end of the consolidation period, the value of the product at dekadal date D has converged towards the ‘historical’ time series when, for a given dekad ‘D’ to be processed, the ‘n’ dekads before ‘D’ and after ‘D’ in the time series are available. ‘n’ is the number of dekads required for the convergence of LAI, FAPAR and FCover values. ‘n’ was fixed to 6 dekads, i.e. 60 days.

![This diagram illustrates the temporal logic of observation and compositing windows for data processing, likely within a satellite product algorithm such as for LAI, FAPAR, or FCover 300m. The horizontal axis represents time, marked with key points: \`D-c\_\` (start of the maximum compositing window in the past), \`D\` (a reference date), \`D+c\_\` (end of the consolidation period), and \`D+n\` (a generic future date). The vertical axis shows sequential processing dates, starting from \`D\`, then \`D+1\`, \`D+2\`, \`D+3\`, and continuing to \`D+n\`, representing how the processing evolves over time. The legend defines four components: \* \*\*Past observations\*\* (blue solid bars): Data collected prior to the current processing date. \* \*\*Future observations\*\* (green checkered bars): Data collected after the reference date \`D\` and increasingly available as processing progresses. \* \*\*Past compositing window\*\* (red outline box): A fixed-length window for compositing past observations, extending from \`D-c\_\` to \`D\`. \* \*\*Future compositing window\*\* (green outline box): A window that expands to include new future observations. The diagram shows: 1. For processing at date \`D\`, only past observations (blue bar) and the associated Past compositing window (red outline) are considered. 2. For processing at \`D+1\`, the same Past compositing window (red outline) ending at \`D\` is used, while one segment of future observations (green checkered bar) is available, enclosed by a Future compositing window (green outline). 3. As the processing date advances (e.g., \`D+2\`, \`D+3\`), the Future compositing window expands to incorporate more available future observations, which are part of the 'Consolidation period' spanning from \`D\` to \`D+c\_\`. 4. At \`D+n\`, the full range of past observations and the fixed Past compositing window up to \`D\` are maintained. The Future compositing window for \`D+n\` now encompasses all future observations up to \`D+n\` within the consolidation period. The diagram effectively demonstrates a sliding window approach where past data up to a reference date \`D\` is kept constant in its compositing window, and future data are progressively included in an expanding compositing window during a consolidation period.](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-158261b77e659cebbd542d3347fa7735.png)

Figure 6: Scheme showing the compositing used for near real time estimates from RT0 (in the top) to the final consolidation RT6 (in the bottom). D refers to the dekad being processed. D+n corresponds to the n dekads available after the dekad D. c- refers to the maximum semi-compositing window before date D (60 days for nonEBF and 210 days for EBF) and c+ refers to the semi-compositing window after date D (0 days for RT0, 10 days for RT1, 20 days for RT2, 30 days for RT3 and 60 days for RT6 and after if the time series are reprocessed).

Note that when working in real time estimation and updating the values for each new dekad available, the compositing period is not symmetric: the maximum compositing window in the past is longer before than after date D: c- \> c+ for RT0, RT1, RT2…RT5. The compositing period after D is limited by the length of the consolidation period that is fixed to 60 days. For nonEBFs in RT6 case or when the time series are reprocessed in ‘historical’ mode after D+6 dekads, the maximum length of the compositing period after date D should be equal to that in the period before, i.e. c+ = c- = 60 days (Figure 6). For EBFs, the compositing window is never symmetric: c-=210 days and c+=\[0,60\] days.

Once a new dekad is available after dekadal date D, the value of the RT product at dekadal date D is recomputed. Since the product value after the second consolidation (RT2) remains mostly stable (see section 5.1), the third, fourth and fifth consolidations are not distributed but only RT0, RT1, RT2 and the consolidated product after convergence, RT6, which is the final product. When the time series are reprocessed in ‘historical’ mode after D+6 dekads, only RT6 products are produced and distributed. These are the main considerations for the processing of LAI, FAPAR, FCover 300m time series from PROBA-V (2014-2018) and Sentinel-3 (2019-present):

- Processing must be done from 2014 onwards, chronologically.
- Running PROBA-V chain from start of 2014 until end of 2019.
- Running Sentinel-3 chain from start of 2019 until present. Because of the compositing process, the processing should start only when 210 days have been accumulated. In practice, this means start running Sentinel-3 chain for 1^(st) dekad 2019 using May-Dec 2018 Sentinel-3 data as input, i.e. generate daily LAI/FAPAR/FCover estimates from May 2018 (Step A of the algorithm) but generate composited values (Step B) only from start 2019 using the past May-Dec 2018 Sentinel-3 dailies for the composition.
- CCI-LC of the year 2014 is only used for the identification of EBFs at the beginning of the time series to initialize PROBA-V processing. Then the information for land cover estimation comes from the data. To initialize Sentinel-3 chain, EBF/No-EBF information from PROBA-V chain are used. This ensures the consistency in the transition from PROBA-V to Sentinel-3 at the start of 2019.

# 5 ALGORITHM DESCRIPTION

In this section, the inputs and outputs are described, along with the quality flags considered. Then, the several steps of the algorithm are presented in details.

## 5.1 INPUTS

All these inputs are required for each considered pixel.

### 5.1.1 Top of Canopy reflectance

The PROBA-V Collection 2 (C2) daily synthesis (S1) of Top of Canopy reflectance in B0: blue, B2: red and B3: near infrared bands (Table 1) are used as inputs. The SWIR band of PROBA-V sensor was not used because it is associated to a degraded spatial resolution and ground spatial sampling distance which are roughly twice that of the VIS-NIR domain (Figure 1). Note that the same spectral bands used in Version 1.0 of 300m products are used in Version 2.0.

The OLCI Top of Canopy reflectance in Oa4-12 and Oa16-18 spectral bands (Table 3) are used as inputs \[CGLOPS1_ATBD_S3-AC-V1\]. The blue bands Oa1-3 were discarded due to possible residual problems of atmospheric correction because they correspond to strong Rayleigh and aerosol scattering associated with low canopy reflectance levels (Liu et al. 2021). The narrow spectral bands Oa13-15 were discarded because they correspond to oxygen absorption bands used for aerosol, cloud and atmospheric correction. Finally, bands Oa19-21 were discarded because they are water absorption bands.

The PROBA-V and OLCI TOC reflectances should be expressed in terms of reflectance factor, mainly varying between 0.0 and 0.7 for most land surfaces outside the hot-spot or the specular directions and cloud, snow or ice cover.

### 5.1.2 Geometry of acquisition

The geometry information is required for the neural networks. It includes:

- the cosine of the view zenith angle (cos(VZA)),
- the cosine of the sun zenith angle (cos(SZA)),
- the cosine of the relative azimuth angle (cos(SAA-VAA)) where SAA corresponds to the Sun Azimuth Angle and VAA to the Viewing Azimuth Angle

### 5.1.3 Land cover

The CCI-LC (https://www.esa-landcover-cci.org) land cover map was used as auxiliary information for deciding whether a pixel belongs or not to an Evergreen Broadleaf Forest (EBF) at the beginning of the time series as described in Section 4.3.2.1. The CCI-LC (2.0.7cds) classification for the first year of time series processing is used: i.e. CCI-LC 2014. This land cover map is derived from PROBA-V data at 300m (https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview). According to CCI-LC legend, the EBF corresponds to class number 50 labeled as ‘Tree cover, broadleaved, evergreen, closed to open (\>15%)’.

### 5.1.4 Land/water mask

A mask identifying both open ocean pixels and inland water pixels as “water” must be used as auxiliary information for deciding whether a pixel belongs to land or water. This mask is inherited from the quality flags of OLCI Sentinel-3 TOC reflectance. IDEPIX_LAND flag, from Idepix cloud detection module, and ‘fresh_inland_water’ flag, from OLCI L1B data, are used to distinguish “land” and “water” pixels. Only “land” pixels are processed. One flag (QC(1) in Table 8) associated to the LAI, FAPAR, FCover products specifies if the pixel is identified as land (QC(1)=0) or water (QC(1)=1).

### 5.1.5 Algorithm parameters

The two main steps (Step A and Step B) of the algorithm as showed in Figure 5 use a series of parameters listed in Table 4 and Table 5, respectively. Their roles and usages are further described in the various paragraphs of Section 4.3. The parameters used in the calibration of the neural networks and the elaboration of the definition domain are sensor specific and are given in Annex 1: Neural Network Calibration.

Table 4: The algorithmic parameters used in Step A.

| Parameter | Descriptive Name | Type | Value | Reference section |
|----|----|----|----|----|
| Ptol^(min)_(LAI) | Tolerance limit minimum for LAI | Float | -0.2 | 4.3.1.4 |
| Ptol^(max)_(LAI) | Tolerance limit maximum for LAI | Float | 10 | 4.3.1.4 |
| Ptol^(min)_(FAPAR) | Tolerance limit minimum for FAPAR | Float | -0.1 | 4.3.1.4 |
| Ptol^(max)_(FAPAR) | Tolerance limit maximum for FAPAR | Float | 1.2 | 4.3.1.4 |
| Ptol^(min)_(FCover) | Tolerance limit minimum for FCover | Float | -0.1 | 4.3.1.4 |
| Ptol^(max)_(FCover) | Tolerance limit maximum for FCover | Float | 1.2 | 4.3.1.4 |

Table 5: The algorithmic parameters for Step B.

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| **Parameter** | **Descriptive Name** | **Type** | **Units** | **Value** | **Reference section** |
| length^(EBF)_(max_bef) | Maximum length of the half compositing window before the date being processed for EBF case | Int. | days | 210 | 4.3.2.1.1 |
| length^(EBF)_(max_aft) | Maximum length of the half compositing window after the date being processed for EBF case | Int | days | 60 | 4.3.2.1.1 |
| N_(EBF) | Number of observations required to compute products for EBF case | Int. | \- | 10 | 4.3.2.1.2 |
| f_(x)(N_(tot)) | Frequency used to consider an observation as valid for EBF case | Float | % | 70 | 4.3.2.1.2 |
| Lat^(EBF)_(max) | Latitude max at which EBF can be found (absolute value) | Float. | º | 28.5 | 4.3.2.1.3 |
| f^(min)_(EBF) | Ratio of number of dates at which the pixel is identified as EBF over the N^(max)_(EBF) dekads | Float | \- | 0.9 | 4.3.2.1.3 |
| LAI^(EBF)_(min) | Threshold LAI value required to detect EBF (EBF should have LAI\>LAI^(EBF)_(min)) | Float | \- | 4 | 4.3.2.1.3 |
| Diff^(thres) | Used to apply a threshold on the difference, δLAI_Valid between consecutive valid observations to detect EBF | Float | \- | 0.9 | 4.3.2.1.3 |
| Percent_(EBF) | Value of the percentile of difference between consecutive observations used to detect EBF | Float | % | 80 | 4.3.2.1.3 |
| N^(min)_(outlier) | Minimum number of observations required for outlier identification | Int | \- | 3 | 4.3.2.2.1 |
| tol^(abs)_(outlier) | Value of outlier threshold (absolute value) used to detect outliers | Float | \- | 0.1 | 4.3.2.2.1 |
| tol_(outlier) | Value of outlier threshold (relative value) used to detect outliers | Float | \- | 0.6 | 4.3.2.2.1 |
| length_(outlier) | Length of the half window used for outlier rejection for nonEBF case | Int. | days | 5 | 4.3.2.2.1 |
| length^(min)_(noEBF) | Minimum length of the half compositing window for nonEBF case | Int. | days | 15 | 4.3.2.2.2 |
| length^(max)_(noEBF) | Maximum length of the half compositing window for nonEBF case | Int. | days | 60 | 4.3.2.2.2 |
| N_(no_EBF) | Number of valid observations for nonEBF case in each half window used to define the length of the composition window | Int | \- | 10 | 4.3.2.2.2 |
| N_(linear) | Minimum number of valid observations for degree-2 polynomial fit; non EBF case | Int. | \- | 5 | 4.3.2.2.3 |
| k | Value of coefficient k in the weighing of observations for the polynomial fitting for non EBF case | Float | \- | 2 | 4.3.2.2.3 |
| N_(miss) | Minimum number of observations for non EBF case | Int. | \- | 3 | 4.3.2.2.3 |
| ND^(max)_(gap) | Length in dekads of period with missing data that can be filled | Int. | dekads | 6 | 4.3.2.2.3 |
| Δ^(max)_(noEBF) | Maximum distance between the date of the dekad and the nearest observations required to compute the product in the non EBF case | Int. | days | 15 | 4.3.2.2.3 |
| length_(interp) | Length of the window used to interpolate between the 2 nearest data before and after dekad when nonEBF algorithm fails | Int. | days | 15 | 4.3.2.2.3 |
| length_(nearest) | Length of the window used to select the nearest data before or after dekad when nonEBF algorithm fails and interpolation is not possible | Int. | days | 5 | 4.3.2.2.3 |
| δ_(LAI) | Threshold value for the confidence interval on the estimated value | Float | \- | 0.35 | 4.3.2.2.3 |
| tol^(min)_(FAPAR) | Tolerance minimum on FAPAR used to reject estimated values outside the expected range of variation | Float | \- | -0.1 | 4.3.2.2.4 |
| tol^(min)_(FCOVER) | Tolerance minimum on FCover used to reject estimated values outside the expected range of variation | Float | \- | -0.1 | 4.3.2.2.4 |
| tol^(min)_(LAI) | Tolerance minimum on LAI used to reject estimated values outside the expected range of variation | Float | \- | -0.2 | 4.3.2.2.4 |
| tol^(max)_(LAI) | Tolerance maximum on LAI used to reject estimated values outside the expected range of variation | Float | \- | 10 | 4.3.2.2.4 |
| tol^(max)_(FAPAR) | Tolerance maximum on FAPAR used to reject estimated values outside the expected range of variation | Float | \- | 1.2 | 4.3.2.2.4 |
| tol^(max)_(FCOVER) | Tolerance maximum on FCover used to reject estimated values outside the expected range of variation | Float | \- | 1.2 | 4.3.2.2.4 |
| N^(max)_(DEBF) | Number of dekads used to compute the fraction of EBF cases | Int. | dekads | 36 | 4.3.2.1.3 |

## 5.2 OUTPUTS

Three types of outputs are expected:

- The dekadal values of LAI, FAPAR and FCover

- Quantitative quality assessment (QA) indicators of the products

- Qualitative quality indicators (QC)

### 5.2.1 The LAI, FAPAR and FCover products

The outputs are computed by application of the algorithm over each pixel at each dekadal date. They include the LAI, FAPAR and FCover values as described previously. The range of variation and resolution are presented in Table 6. The same conventions as for 300m V1.0 products are used here. The definition of the maximum physical value of 1 for FCover is clear and corresponds to pixels with full cover green vegetation. The maximum FAPAR values are expected to be close to 0.94 (Baret and Guyot 1991) corresponding to full cover dense vegetation with albedo in the PAR domain close to 0.06. However, for LAI, the upper limit is not a physical limit, but a value just slightly higher than the maximum value that can be reached by the MODIS and CYCLOPES original products (Baret et al. 2013).

The physical values are retrieved by:

\\ \text{PhyVal} = \text{DN} \* \text{Scaling\\factor} + \text{Offset} \\

where the scaling factor and the offset are given in Table 6.

Table 6: Minimum, maximum values and associated resolution for LAI, FAPAR and FCover products.

| Product | Physical Minimum | Physical Maximum | Max DN value | Missing value | Scaling factor | Offset |
|----|----|----|----|----|----|----|
| LAI | 0.0 | 7.0 | 210 | 255 | 1/30. | 0 |
| FAPAR | 0.0 | 0.94 | 235 | 255 | 1/250. | 0 |
| FCover | 0.0 | 1.0 | 250 | 255 | 1/250. | 0 |

### 5.2.2 Quality indicators

In addition to the LAI, FAPAR and FCover values, quantitative (QA) and qualitative (QC) quality indicators are also generated. They are listed in Table 7 and Table 8, respectively.

The quantitative (QA) metrics NOBS, RMSE and LENGTH_BEFORE, LENGTH_AFTER are ancillary layers describing the quality of the product. The RMSE for each variable are calculated as the root mean square error between the instantaneous estimates in the compositing window and the final 10-day product value. See section 4.3.2 for more details.

Table 7: Minimum, maximum values and associated resolution for the quantitative quality indicators (QA) of LAI, FAPAR and FCover. D means dekadal date.

| QA | Quantitative quality indicator | Physical Minimum | Physical Maximum | Max DN value | Scaling factor | Offset | Missing Value |
|----|----|----|----|----|----|----|----|
| NOBS | Number of available valid instantaneous estimates in the compositing window | 0.0 | 60\* | 60 | 1 | 0 | 255 |
| LENGTH\_ BEFORE | Length in days of semi-period before D | 0 | 210 | 210 | 1 | 0 | 255 |
| LENGTH\_ AFTER | Length in days of semi-period after D | 0 | 60 | 60 | 1 | 0 | 255 |
| RMSE-LAI | Uncertainty on LAI value | 0.0 | 7.0 | 210 | 1/30. | 0 | 255 |
| RMSE-FAPAR | Uncertainty on FAPAR value | 0.0 | 0.94 | 235 | 1/250. | 0 | 255 |
| RMSE-FCover | Uncertainty on FCover value | 0.0 | 1.0 | 250 | 1/250. | 0 | 255 |

\* The theoretical maximum of NOBS is set to 60 to account for more than one instantaneous estimate per day in the compositing window but the typical maximum of NOBS is 10 for EBF and 20 for nonEBF.

The qualitative quality flag (QC) indicator is coded as 8-bit (1 byte) pattern shown in Table 8. Bit 1 is the least significant bit (right-most). The QC value 255, i.e. 11111111 in binary form, is used for missing (non-processed) pixels.

Table 8: Qualitative quality indicators (QC). The numbers in brackets refer to the QC bit number. QC (1:8) = 11111111 indicates non-processed pixel.

[TABLE]

## 5.3 DETAILED DESCRIPTION

As summarized in Figure 5 and detailed in Figure 7, the Version 2.0 algorithm of vegetation 300m products relies on 2 main steps:

- Step A: instantaneous estimates of LAI, FAPAR, FCover (Figure 8)
- Step B: compositing, smoothing and gap filling (gap filling is only applied for EBFs processing) (Figure 9)

The algorithm is dependent on the pixel land cover type (Figure 7). Specific Neural Network Techniques (NNTs) and dedicated smoothing procedures are applied, respectively, in steps A and B for Evergreen Broadleaf Forest (EBF) or non EBF pixels. The geographic position of the pixel is used first to trigger EBF or nonEBF branches. Only pixels located in tropical latitudes (\\-28.5º \le\\ Latitude \\\le 28.5º\\) or in Australia (\\Latitude \< 0º\\ and \\115º \le Longitude \le 155º\\) are susceptible of being EBFs.

![This workflow diagram illustrates the process for computing instantaneous and dekadal Leaf Area Index (LAI), Fraction of Absorbed Photosynthetically Active Radiation (FAPAR), and Fraction of green vegetation cover (FCover) products, distinguishing between Evergreen Broadleaf Forest (EBF) and non-Evergreen Broadleaf Forest (nonEBF) cases. 1. The process starts by taking \`Latitude\` and \`Longitude\` as input. 2. \*\*Geographical Classification:\*\* A decision point determines the initial processing path: \* IF \`(-28.5 \<= Latitude \<= 28.5)\` OR \`(Latitude \< 0 AND 115 \<= Longitude \<= 155)\`, THEN the \`EBF\` processing path (Region A) is followed. \* OTHERWISE, the \`nonEBF\` processing path (leading to Region B2) is followed. 3. \*\*Instantaneous Product Estimation (Region A for EBF path):\*\* \* For the \`EBF\` path, \`NNT_EBF coefficients\` and \`TOC reflectances\` are used for \`Instantaneous product estimation\`, which outputs \`Instantaneous LAI, FAPAR, FCover\`. \* This output then feeds into \`EBF Compositing\`. 4. \*\*Vegetation Type Decision:\*\* At \`EBF Compositing\`, a second decision point, \`Evergreen Broadleaf Forest?\`, uses \`CCI-LC\` (Climate Change Initiative Land Cover) data. \* IF \`Evergreen Broadleaf Forest?\` is TRUE (\`yes\`): \`Select EBF solution\` is performed, and its output proceeds to \`Dekadal LAI, FAPAR, FCover\`. \* IF \`Evergreen Broadleaf Forest?\` is FALSE (\`no\`): The process diverts to \`nonEBF Compositing\` (Region B2). 5. \*\*nonEBF Processing Path (Region B2):\*\* \* If the initial geographical classification led to the \`nonEBF\` path, \`NNT_nonEBF coefficients\` (along with \`TOC reflectances\`) are used for \`Instantaneous product estimation\`, resulting in \`Instantaneous LAI, FAPAR, FCover\`. This instantaneous product then feeds into \`nonEBF Compositing\`. \* \`nonEBF Compositing\` also receives input if the \`Evergreen Broadleaf Forest?\` decision was false. 6. \*\*Dekadal Product Generation:\*\* Both \`EBF Compositing\` (after \`Select EBF solution\`) and \`nonEBF Compositing\` ultimately lead to the generation of \`Dekadal LAI, FAPAR, FCover\`. 7. \*\*Feedback/Fallback Mechanisms:\*\* Dashed lines indicate alternative processing paths or feedback loops. The \`Dekadal LAI, FAPAR, FCover\` product can be fed back as input for \`NNT_nonEBF coefficients\` and directly to \`nonEBF Compositing\`, indicating a mechanism to use previous dekadal products in the computation. Similarly, the \`Instantaneous LAI, FAPAR, FCover\` from the \`nonEBF\` path feeds into \`nonEBF Compositing\` via a dashed line.](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-c718a718e9df944528b31c043c2ae41c.png)

Figure 7: Detailed flow chart of 300m V2.0 algorithm. Solid line indicates the steps applied to EBF pixels. Dashed line corresponds to the steps applied to the nonEBF pixels.

For these potential EBF pixels, the algorithm is run in two iterations (Figure 7). At the first iteration, step A with NNT coefficients for EBFs and step B1 corresponding to EBF composition are applied. In addition to the dekadal estimates of LAI, FAPAR, FCover, step B1 also determines the land cover type of each pixel: Evergreen Broadleaf Forest (EBF) or nonEBF. The algorithm only keeps as EBFs those pixels in tropical latitudes or in Australia that, according to the data, have high LAI values, low seasonality and a significant level of noise. That is the algorithm itself searches and defines whether a pixel is EBF or nonEBF based on the LAI data values. However, at the beginning of the time series, the CCI-LC land cover is used as auxiliary information for initialization EBF and nonEBF masks. Note that this external land cover map is only used for processing the first year of the time series. The processing starts with historical PROBA-V time series followed by Sentinel-3 data, then the CCI-LC 2014 must be used. The information used for initialization EBF and nonEBF masks at the first dekad of Sentinel-3 time series is the EBF/nonEBF class resulted from Version 2.0 algorithm detection for the last dekad of PROBA-V processing. Further details of EBF/nonEBF detection are provided in section 4.3.2.1.3. If the pixel is detected as nonEBF, a second run is performed, with specific nonEBF NNTs in step A and step B2 smoothing procedure.

For the pixels which are not located in tropical latitudes or Australia, the algorithm is run in one single iteration using nonEBF branch (nonEBF NNTs in step A and step B2 for the composition) (Figure 7).

### 5.3.1 Instantaneous LAI, FAPAR, FCover estimates (Step A)

It yields a first estimate of instantaneous products from the Top-of-Canopy reflectance (Figure 8).

![This algorithm workflow diagram details the process for generating instantaneous vegetation products from Top Of Canopy (TOC) reflectances. 1. The workflow begins with 'TOC reflectances' as the initial input. 2. At decision point A1, the system checks if the data is 'Inside status map?'. - If the condition is 'no', the output is 'Missing data'. - If the condition is 'yes', the process continues to decision point A2. 3. At decision point A2, the system checks if the data is 'Inside definition domain?', using the 'Definition Domain' as a reference. - If the condition is 'no', the output is 'Missing data'. - If the condition is 'yes', the process proceeds to parallel execution of three NNT (presumably a specific algorithm or model) operations (A3). 4. The parallel operations A3 involve running 'Run NNT LAI' (Leaf Area Index), 'Run NNT FAPAR' (Fraction of Absorbed Photosynthetically Active Radiation), and 'Run NNT FCOVER' (Fraction of vegetation Cover). These operations use 'NNT coeffs' as an input. 5. The outputs from these parallel operations merge and proceed to decision point A4, where the system checks if the data is 'Inside output range?', referencing 'Physical range + tolerance'. - If the condition is 'no', the output is 'Missing data'. - If the condition is 'yes', the process proceeds to step A5. 6. At step A5, the 'FCOVER' value is calculated using the formula \`FCOVER=min(FCOVER, FAPAR/0.94)\`. 7. The final output of this workflow is 'Instantaneous products'.](products_Algorithm_theoretical_basis_document_-_Fraction_of_Absorbed_Photosynthetically_Active_Radiation_300m_version_2-media/img-6b1c2f2ba79f6c60ef064cc43b21a598.png)

Figure 8: Flow chart describing the instantaneous product estimation (Step A)

#### 5.3.1.1 Rejection of input data based upon their quality status (Step A1)

The quality flags associated to PROBA-V and Sentinel-3 TOC data are first used to keep only pixels with all the selected spectral bands having good radiometric quality, located over land, not covered by ice, cloud or snow.

For PROBA-V, the QC plane (Table 2) is first used to keep only the best quality pixels i.e. pixels with status map value equal to 248 = 11111000. Only land pixels, as identified by the land/water mask (Section 4.1.4), are processed.

For Sentinel-3:

- quality_flags layer inherited from OLCI L1B data (ACRI-ST, 2017; CGLOPS1_PUM_S3-TOC-Reflectance300m-V2.3):
  - ‘saturated_Oa\*’ for bands Oa4-12 and Oa16-18, exclude when raised
  - For Sentinel-3 TOC reflectance V2.3 used in V2.0 algorithm, additional information is requested: ‘fresh_inland_water’, exclude when raised \[CGLOPS1_PUM_S3-TOC-Reflectance300m-V2.3\]. For Sentinel-3 TOC reflectances V1, used in V1.1 algorithm, this information was already included in the IDEPIX_LAND quality flag.
- pixel_classif_flags, output of Idepix cloud detection module, (CGLOPS1_QAR_S3-CloudMask, CGLOPS1_PUM_S3-TOC-Reflectance300m-V2.3):
  - IDEPIX_LAND: include when raised
  - IDEPIX_CLOUD: exclude when raised
  - IDEPIX_CLOUD_AMBIGUOUS: exclude when raised
  - IDEPIX_CLOUD_BUFFER: exclude when raised
  - IDEPIX_CLOUD_SHADOW: exclude when raised
  - IDEPIX_SNOW_ICE: exclude when raised

#### 5.3.1.2 First outlier rejection (Step A2)

A first condition is applied to verify whether the inputs of a given observation keep within the range of variation of the training dataset called here the definition domain. In order to avoid that the Neural networks would extrapolate values, only the input TOC reflectance in the selected spectral bands for a given observation which are within the definition domain (Table 9, Table 10, Annex 1: Neural Network Calibration) are kept as valid input data. The observations with TOC data values out of the definition domain are considered as outliers and rejected. Note that the definition domain is sensor specific: one domain is defined for PROBA-V and one domain for Sentinel-3.

#### 5.3.1.3 Deriving instantaneous estimates using neural networks (Step A3)

Two sets of specific neural networks for EBF and nonEBF were previously calibrated for each of the 3 variables considered (LAI, FAPAR, and FCover) (Annex 1: Neural Network Calibration). The neural networks are also sensor specific: one set of neural networks is calibrated for PROBA-V and other for Sentinel-3. Then the combination of three variables (LAI, FAPAR, FCover) per two landcover vegetation classes (EBF and nonEBF) per two sensors (PROBA-V and Sentinel-3) resulted in twelve neural networks.

For the pixels located outside the regions of the world suitable for EBF (Figure 7), nonEBF NNTs are applied to each individual observation (one pixel at a given date).

For the pixels located in a region of the world suitable for EBF, the EBF NNTs are used similarly. If the EBF identification achieved in Step B1 (Figure 7) reveals that some of these pixels are actually not EBF then, the nonEBF NNTs are used to reprocess these pixels in a second iteration (Figure 7).

The inputs of the neural networks are:

- TOC reflectance in the selected bands (the PROBA-V neural networks ingest TOC reflectance in 3 spectral bands: B0, B2 and B3, while the Sentinel-3 neural networks ingest TOC reflectance in 12 OLCI spectral bands: Oa4-12 and Oa16-18),
- the cosine of the view zenith angle (cos(VZA)),
- the cosine of the sun zenith angle (cos(SZA)),
- the cosine of the relative azimuth angle (cos(SAA-VAA)),

To apply the neural networks, the following steps must be completed:

- **Normalization of the inputs**: The inputs are normalized to prevent possible numerical problems during the training process. For all the inputs X, the following normalization equation must be applied:

  \\X\_{norm} = 2 \cdot \frac{(X - X\_{min})}{(X\_{max} - X\_{min})} - 1\\

  where Xnorm is the normalized input value, and Xmin and Xmax correspond to the minimum and maximum values of the inputs in the neural network training data set (Table 9, Table 10).

- **Run the neural network**. The neural network is described by its architecture, i.e. the number of hidden layers and the output layer. Each layer is described by its number of neurons, associated weight and biases and transfer function. A simple neural network with one hidden layer with 5 neurons and one output layer was used. For the neurons of the hidden layers, the transfer function is a tangent sigmoid function given by: \\y = \text{Tansig}(x) = 2/(1 + \exp(-2x)) - 1\\, while for the output layer the transfer function is linear (\\y = x\\) .

- **Denormalization of the output**. It simply consists in applying the inverse function used for input normalization:

  \\Y = 0.5 \cdot (Y\_{norm} + 1) \cdot (Y\_{max}^\* - Y\_{min}^\*) + Y\_{min}^\*\\

  where Ynorm is the normalized output value issued from the NNT, and Ymin\* and Ymax\* are computed over the neural network training data set (Table 9, Table 10).

Back to top

## Footnotes

## Reuse

EUPL (\>= 1.2)

[^1]: Data coding is the provision for the number of bits, range of values, usage of reserved values, content of status map,
