# QUALITY ASSESSMENT REPORT

Gio Global Land Component - Lot I ‘Operation of the Global Land Component’

This Quality Assessment Report evaluates the performance of the Soil Water Index (SWI) Version 3 and its 10-day composite (SWI10), alongside the Surface State Flag (SSF) Version 3. Covering a global scale, the report rigorously compares these new products, utilising both Metop-A and -B data, against the Global Land Data Assimilation System model and International Soil Moisture Network in-situ observations. It details the methodologies, validation metrics such as Pearson’s R and RMSD, and critically assesses improvements over previous versions and the impact of potential sensor failures, ensuring robust product quality for the Copernicus Global Land Service.

Published

July 1, 2015

Keywords

Soil Water Index (SWI) Version 3, Surface State Flag (SSF) Version 3, Quality assessment report (QAR), Global Land Data Assimilation System (GLDAS), International Soil Moisture Network (ISMN), Metop-A Metop-B satellite data, Pearson’s correlation coefficient (R), Root mean square difference (RMSD), Infiltration model, Surface soil moisture (SSM), Freeze/thaw conditions, Copernicus Global Land Service

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

|  | Dissemination Level |  |
|----|----|----|
| PU | Public | X |
| PP | Restricted to other programme participants (including the Commission Services) |  |
| RE | Restricted to a group specified by the consortium (including the Commission Services) |  |
| CO | Confidential, only for members of the consortium (including the Commission Services) |  |

### 0.0.1 DOCUMENT RELEASE SHEET

|  |  |  |  |
|----|----|----|----|
| Book captain: | C. Paulik | Date: 21.07.2015 | Sig: ![](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-45c12bd3c47ec423944180bf28dc4801.png) |
| Approval: | R. Lacaze | Date: 22.07.2015 | Sign: ![](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-7cb787e28da2ff7b1568e8ef384025b5.png) |
| Endorsement: | M. Cherlet | Date: | Sign: |
| Distribution: |  |  |  |

### 0.0.2 CHANGE RECORD

| Issue/Rev | Date       | Page(s) | Description of Change        | Release |
|-----------|------------|---------|------------------------------|---------|
|           | 07.07.2014 | All     | First Issue                  | I1.00   |
| I1.00     | 21.07.2015 | All     | Update after external review | I1.10   |
|           |            |         |                              |         |
|           |            |         |                              |         |
|           |            |         |                              |         |

### 0.0.3 LIST OF FIGURES

Fig. 1: Comparison of ASCAT backscatter (sigma40) measurements, ERA Interim 2 meters air temperature and WMO Meteo snow depth data over a grid point at 66.5037°E, 66.6924°N in 2007

Fig. 2: SWI and GLDAS data for a point in France. SWI data was scaled to GLDAS data according to procedure explained in Chapter 3.6. It can be seen that for very similar input data evident in the very similar SWI values for T=1 the data is quite different for T=100 due to different initial conditions.

Fig. 3: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

Fig. 4: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

Fig. 5: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

Fig. 6: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

Fig. 7: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

Fig. 8: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

Fig. 9: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=100.

Fig. 10: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

Fig. 11: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

Fig. 12: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=100.

Fig. 13: Maps of correctly classified days in percent for SSFV3 using Metop A and B, SSFV2 using only Metop B and the differences between the two. The lower right plot shows a cumulative histogram of these differences.

Fig. 14: Maps of mean of consecutive days wrongly classified for SSFV3 using Metop A and B, SSFV2 using only Metop B and the differences between the two. The lower right plot shows a cumulative histogram of these differences.

Fig. 15: Pearson’s R between GLDAS Layer 1 (0 – 0.1m) and SWI10 T=1 with a p-value \< 0.1 (top) and histogram of R (bottom)

Fig. 16: Pearson’s R between GLDAS Layer 1 (0 – 0.1m) and SWI10 T=20 with a p-value \< 0.1 (top) and histogram of R (bottom).

Fig. 17: Pearson’s R between GLDAS Layer 3 (0.4 - 1m) and SWI10 T=100 with a p-value \< 0.1 (top) and histogram of R (bottom).

Fig. 18: RMSD between GLDAS Layer 1 (0 – 0.1m) and for SWI10 T=1 (top) and histogram of RMSD (bottom)

Fig. 19: RMSD between GLDAS Layer 1 (0 – 0.1m) and for SWI10 T=20 (top) and histogram of RMSD (bottom).

Fig. 20: RMSD between GLDAS Layer 3 (0.4 - 1m) and SWI10 T=100 (top) and histogram of RMSD (bottom)

Fig. 21: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

Fig. 22: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

Fig. 23: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

Fig. 24: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

Fig. 25: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

Fig. 26: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

Fig. 27: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=100.

Fig. 28: Maps of RMSD for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences.. All plots for T=1.

Fig. 29: Maps of RMSD for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences.. All plots for T=20.

Fig. 30: Maps of RMSD for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences.. All plots for T=100.

Fig. 31: Different SWI variants and in situ data for SNOTEL station CRAB CREEK.

Fig. 32: Different SWI variants and in situ data for USCRN station Edinburg-17-NNE.

Fig. 33: Different SWI variants and in situ data for SCAN station Pine Nut.

Fig. 34: Different SWI variants and in situ data for TERENO station Selhausen.

Fig. 35: Map and histogram of Pearson’s R (p \< 0.1) between in situ data and SWI10 of for T=1.

Fig. 36: Map and histogram of Pearson’s R (p \< 0.1) between in situ data and SWI10 of for T=20

Fig. 37: Map and histogram of Pearson’s R (p \< 0.1) between in situ data and SWI10 of for T=100

Fig. 38: Map and histogram of RMDS between in situ data and SWI10 of for T=1

Fig. 39: Map and histogram of RMDS between in situ data and SWI10 of for T=20

Fig. 40: Map and histogram of RMDS between in situ data and SWI10 of for T=100

### 0.0.4 LIST OF TABLES

Table 1: Target requirements of GCOS for soil moisture (up to 5cm soil depth) as Essential Climate Variable (GCOS-154, 2011)

Table 2: Required accuracy of SWI and SWI in 3 categories

Table 3: Possible values of the SSF and their meaning

Table 4: Available datasets for validation

Table 5: Classification scheme

Table 6: Which T-values were compared to which layer of the GLDAS model.

Table 7: Station details and climate classification.

### 0.0.5 LIST OF ACRONYMS

ASCAT  
Advanced Scatterometer (Metop)

CDF  
Cumulative Distribution Function

CEOS  
Committee on Earth Observation Satellites

ECMWF  
European Centre for Medium Range Weather Forecasting

ERA-40  
ECMWF ReAnalysis 40 data set

ERA-Interim  
ECMWF Reanalysis Interim

ERS  
European Remote Sensing Satellite

EUMETSAT  
European Organisation for the Exploitation of Meteorological Satellites

GIO  
GMES Initial Operations

GL  
Copernicus (ex GMES) Global Land service

GLDAS  
Global Land Data Assimilation System

GMES  
Global Monitoring for Environment and Security

H-SAF  
Satellite Application Facility on Hydrology

ISMN  
International Soil Moisture Network

NRT  
Near real time

PUM  
Product User Manual

QFLAG  
Quality Flag

SSF  
Surface State Flag

SSM  
Surface Soil Moisture

SWI  
Soil Water Index

WMO  
World Meteorological Organization

# 1 BACKGROUND OF THE DOCUMENT

## 1.1 EXECUTIVE SUMMARY

From 1st January 2013, the Global Land (GL) component of the Copernicus Land service is providing a series of bio-geophysical products describing the status and evolution of land surface at global scale. Essential Climate Variables like the Leaf Area Index (LAI), the Fraction of PAR absorbed by the vegetation (FAPAR), the surface albedo, the Land Surface Temperature, the soil moisture, the burnt areas, the areas of water bodies, and additional vegetation indices, are generated every hour, every day or every 10 days from Earth Observation satellite data. Production and delivery of the parameters are performed on a reliable, automatic and timely manner and are complemented by the constitution of long term time series.

Quality Assessment and continuous Quality Monitoring constitute the only means of guaranteeing the compliance of generated products with user requirements:

- The former concerns the new products which must pass an exhaustive scientific evaluation before to be implemented operationally.
- The latter concerns the operational products to check their quality keeps at the same level along the time.

Both follow, as much as possible, the guidelines, protocols and metrics defined by the Land Product Validation (LPV) group of the Committee on Earth Observation Satellite (CEOS) for the validation of satellite-derived land products.

In this QA report the test datasets of the new version (Version 3) of the Soil Water Index (SWI) (called SWIV3) and the 10-days composite SWI (SWI10) dataset are compared to the Global Land Data Assimilation System (GLDAS) land surface model and in situ data. For the SWI products also the currently operational SWI Version 2 (SWIV2) was compared against GLDAS and in situ data to have a benchmark for the SWIV3 results.

In addition to that, SWIV3 was computed with different input data. Once using both Metop-A and B surface soil moisture as input and once using only Metop-B data. This was done to check that the quality of the product does not deteriorate unreasonably if one satellite fails.

## 1.2 SCOPE AND OBJECTIVES

The aim of this document is to present the results of the Quality Assessment of the test datasets produced during the evolution of the SWI and SWI10 datasets. For the SWI, the main goal was to check the quality of the SWIV3 product against that of the operational SWIV2. For the SWI10 product, a first assessment of the quality was the focus since no previous products of this type are available.

The products used in this study were:

- SWI V2.0 (SWIV2)
- SWI V3.0 MetopA+B (SWIV3)
- SWI V3.0 MetopB (SWIV3_B)
- Surface State Flag (SSF) V2.0 (SSFV2)
- SSF V3.0 MetopA+B (SSFV3)
- SWI10 V1.0

This study covers nearly 12 months from 24.04.2013 to 21.04.2014. The reason for this validation period is that on 24th of April 2013 Metop-B became the operational satellite and the GLDAS data was only available until 21st of April 2014 when this study was conducted.

## 1.3 CONTENT OF THE DOCUMENT

This document is structured as follows:

- Chapter 2 recalls the users requirements, and the expected performance
- Chapter 3 describes the methodology for quality monitoring, the metrics and the criteria of the evaluation
- Chapter 4 presents the results of the scientific analysis
- Chapter 5 summarizes the main conclusions of the study

## 1.4 RELATED DOCUMENTS

### 1.4.1 Applicable documents

AD1: Annex II – Tender Specifications to Contract Notice 2012/S 129-213277 of 7th July 2012

AD2: Appendix 1 – Product and Service Detailed Technical requirements to Annex II to Contract Notice 2012/S 129-213277 of 7th July 2012

### 1.4.2 Input documents

GIOGL1_SVP  
Service Validation Plan of the Global Land Service

GIOGL1_ServiceSpecifications  
Service Specifications of the Global Land Service

GIOGL1_ATBD_SWIV3  
Algorithm Theoretical Basis Document of the SWI V3.0, SSF V3.0 and SWI10

### 1.4.3 Output documents

GIOGL1_PUM_SWI :Product User Manual of SWI summarizing all information about the product, including the main conclusions of the quality assessment.

# 2 USERS REQUIREMENTS

According to the applicable document \[AD2\], the user’s requirements relevant for the Soil Water Index are:

- **Definition**: Amount of water (m³/m³) contained in soil layers identified according to their depth measured from the top surface.
- **Geometric properties**:
  - Pixel size shall be defined on a per-product basis so as to facilitate the multi-parameter analysis and exploitation
  - The target baseline location accuracy shall be 1/3 of the at-nadir instantaneous field of view.
  - Pixel co-ordinates shall be given for the centre of the pixel.
- **Geographical coverage**:
  - Geographic projection: regular lat-long
  - Geodetical datum: WGS84
  - Pixel accuracy: minimum 10 digits
  - Coordinate position: centre of pixel
  - Window coordinates:
    - Upper Left:180°W-74°N
    - Bottom Right: 180°E 56°S
- **Ancillary information**:
  - the number of measurements per pixel used to generate the synthesis product
  - the per-pixel date of the individual measurements or the start-end dates of the period actually covered
  - quality indicators, with explicit per-pixel identification of the cause of anomalous parameter result
- **Accuracy requirements**: wherever applicable the bio-geophysical parameters should meet the internationally agreed accuracy standards laid down in document “Systematic Observation Requirements for Satellite-Based Products for Climate”. Supplemental details to the satellite based component of the”Implementation Plan for the Global Observing System for Climate in Support of the UNFCCC”. GCOS-#154, 2011” (Table 1).

Table 1: Target requirements of GCOS for soil moisture (up to 5cm soil depth) as Essential Climate Variable (GCOS-154, 2011)

| Variable | Horizontal Resolution | Temporal resolution | Accuracy | Stability |
|----|----|----|----|----|
| Volumetric soil moisture | 50km | Daily | 0.04 m³/m³ | 0.01m³/m³/year |

GCOS notes that the targets above “are set as an accuracy of about 10 per cent of saturated content and stability of about 2 per cent of saturated content. These values are judged adequate for regional impact and adaptation studies and verification and development of climate models. It is considered premature to consider global scale changes.” It adds that “stating a general accuracy requirement is difficult for this type of observation, as this depends not only on soil type but also on soil moisture content itself. The stated numbers thus should be viewed with some caution”.

In addition, the user requirements for the SWI and SSF variables were also defined in the FP7/geoland2 project (Table 2).

Table 2: Required accuracy of SWI and SWI in 3 categories

| Variable | Threshold | Target | Optimal |
|----------|-----------|--------|---------|
| SWI      | 20%       | 10%    | 5%      |
| SSF      | 7 days    | 3 days | 1 day   |

The above requirements are indicative. They will be adapted to the GL products and clarified by the user board of the Global Land service.

# 3 QUALITY ASSESSMENT METHOD

## 3.1 SWI DATASET

The SWI algorithm, originally developed at Vienna University of Technology (TU Wien) and later improved by other research groups, uses an infiltration model describing the relation between surface soil moisture (SSM) and profile soil moisture as a function of time. The algorithm is based on a two-layer water balance model proposed by Wagner et al. (1999) to estimate profile soil moisture from SSM retrieved from scatterometer data. The remotely sensed topsoil represents the first layer and the second layer extends downwards from the bottom of the surface layer. In this model, the water content of the reservoir layer is described in terms of an Index, which is controlled only by the past soil moisture conditions in the surface layer in a way that the influence of measurements decreases by increasing the time:

\\ \text{SWI}(t_n) = \frac{\sum_i \text{SSM}(t_i) e^{-\frac{t_n-t_i}{T}}}{\sum_i e^{-\frac{t_n-t_i}{T}}} \quad \text{for } t_i \le t_n \quad (1) \\

In which tₙ is the observation time of the current measurement and tᵢ are the observation times of the previous measurements. These times are given in Julian days. In (Eq. 1) all Surface Soil Moisture (SSM) observations made before tₙ are exponentially weighted and summed up. The factor T determines how fast the weights become smaller and how strongly SSM observations taken in the past influence the current SWI. If e.g. the T value is 5 and a SSM measurement was taken 10 days before tₙ then this observation would receive the weight \\e^{-10/5} = 0.135\\. Using a T value of 20 in the same case would increase the weight to \\e^{-10/20}= 0.607\\.

This basic algorithm is the same for SWIV2 and SWIV3. The difference between the two datasets is the input data. Whereas SWIV2 uses data from one Metop satellite, SWIV3 uses data from both Metop-A and Metop-B. This change leads to more SSM observations being integrated into the SWI which will provide SWI estimates that are more stable. The usage of two satellites does not produce more valid SWI observations since the timestamp of the SWI is daily regardless of available input data. The use of more observations is only indicated by a higher value of the quality flag (QFLAG).

SWI10 data are produced by averaging the SWI images over three periods each month. The date ranges used for averaging are:

- 1-10^(th) day of the month
- 11-20^(th) day of the month
- 21^(st)-end of the month

## 3.2 SSF DATASET

Surface soil moisture retrieval from scatterometer data has certain limitations; it can not be retrieved when the surface is frozen or covered by snow, dense vegetation, or water. Whereas dense vegetation and water are almost static factors the freeze/thaw cycle is dynamic.

The backscattered signal depends, among other factors, on the frozen state of the surface. When the soil surface freezes, dielectric properties of the soil change significantly which usually results in low backscatter values. As snow begins to fall and accumulates over the surface, backscatter signals initially drop. In some cases it increases again in the winter months. This is due to volume scattering and depends on the structure of the snow (not visible in Fig. 1). With increasing temperature in spring, snow begins to melt and water covers the surface of the snow pack which can cause sudden drops in backscatter. After the snow melting period, soil and vegetation begin to thaw and consequently backscatter rises again. Fig. 1 shows this behavior.

![Line chart illustrating the annual variation of sigma40 (dB), ERA-Interim Temperature (°C), and Snow depth (m) over a full year, from 01 January to 31 December. The x-axis represents the Julian days of the year, with specific date labels at: 01 Jan, 19 Jan, 06 Feb, 24 Feb, 14 Mar, 02 Apr, 20 Apr, 08 May, 26 May, 13 Jun, 02 Jul, 20 Jul, 07 Aug, 25 Aug, 12 Sep, 01 Oct, 19 Oct, 06 Nov, 24 Nov, 12 Dec, and 31 Dec. The left y-axis, labelled 'sigma40 (dB)', ranges from -18.6 dB to -6.6 dB. The blue line represents sigma40 values, which fluctuate between approximately -15 dB and -9 dB. Dotted horizontal reference lines are present at -9.6 dB and -15.6 dB. sigma40 values start around -14 dB in January, drop below -15.6 dB in late March/early April, then increase to peak around -9 dB in July and August, before decreasing to below -15.6 dB in late November and December. The right y-axis for the orange line, labelled 'ERA-Interim Temp (°C)', ranges from -30 °C to 30 °C. The orange line indicates ERA-Interim Temperature, starting below -15 °C in January, rising to a peak of approximately 10-15 °C in July, and then declining back to below -15 °C by December. The right y-axis for the light blue shaded area, labelled 'Snow depth (m)', ranges from 0 m to 20 m. The light blue shaded area represents Snow depth. Snow depth is high in winter, generally between 5 m and 10 m from January to early May, decreases rapidly in May, reaches 0 m by early June, and remains at 0 m until late September. It then increases again from October onwards, reaching several metres by December. The chart shows an inverse relationship between snow depth and temperature, and a correlated trend between sigma40 and temperature. During periods of high snow depth and low temperatures (winter), sigma40 values are generally lower. During periods of low snow depth and higher temperatures (summer), sigma40 values are generally higher.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-ab6babea4983cef7c65f34547daa1533.png)

Fig. 1: Comparison of ASCAT backscatter (sigma40) measurements, ERA Interim 2 meters air temperature and WMO Meteo snow depth data over a grid point at 66.5037°E, 66.6924°N in 2007

The frozen state of the surface is recorded within the surface state flag (SSF). The SSF is calculated in 2 steps. Initially, the algorithm uses the relationship of backscatter measurements over temperature to find freeze/thaw parameters and thresholds that define the freezing characteristics of each location. In a second step, two decision trees use these parameters to find the freeze/thaw state of every soil moisture observation. In some edge cases, the SSF cannot be estimated from the backscatter. Historical probabilities for frozen temperatures and snow cover are used in those situations. Table 3 shows the possible values of the surface state flag. If the SSF has the values 2 or 3 the soil moisture measurements are not usable for SWI calculation and the SWI is kept constant at the level it had before freezing. The algorithm is explained in more detail in and the ATBD \[GIOGL1_ATBD_SWIV3\] and in Naeimi et al. (2012).

There are no algorithmic differences between SSFV2 and SSFV3. The difference is in the parameters that are used for deriving the freeze-thaw state. Whereas the parameters for the SWIV2 were derived from two years of data, the SSFV3 parameters were derived from 5 years of data which should lead to more robustly estimated freeze-thaw states.

One thing to consider when comparing SSFV2 and SSFV3 is the bug that was found in SSFV2 during the first Quality Monitoring report. This bug lead to missing SSF values when the SSF could not be derived from backscatter alone.

Table 3: Possible values of the SSF and their meaning

| SSF value | Detected surface state         |
|-----------|--------------------------------|
| 255       | Could not be determined        |
| 1         | Unfrozen                       |
| 2         | Frozen                         |
| 3         | Temporary water on the surface |

## 3.3 MODEL REFERENCE PRODUCTS

The SWI product was compared against the GLDAS (Global Land Data Assimilation System) Noah Land Surface Model.

The GLDAS Noah Land Surface Model (Rodell et al. 2004) is produced by NASA. It includes 4 soil layers with the bottom depth at 0.1, 0.4, 1 and 2 m respectively and simulates over 30 land surface parameters in total. Data is available with a temporal sampling of 3 hours on a global 0.25° grid. The model soil moisture data was converted from kg/m² to m³/m³ by using the formula \\SM\[\text{m}^3/\text{m}^3\] = SM\[\text{kg}/\text{m}^2\] \* 0.001 \* 1/d\\ where d is the thickness of the soil layer in meters. The factor 0.001 is due to the assumption that 1 kg of water represents 1000 cm³ which is 0.001 m³.

The soil moisture component of the GLDAS model is of course not error free but the authors are not aware of a comprehensive study on the global quality of the modelled soil moisture of the GLDAS model. Dorigo et al. (2010) investigated the quality of the GLDAS and ERA-Interim models with the triple collocation method using remotely sensed soil moisture datasets as the other 2 datasets. Similar error structures were found for the two models, indicating that results obtained for the ERA-Interim model can be used as a proxy for the GLDAS soil moisture output. Albergel et al. (2013) explored the performance of the ERA-Land, which is a pre operational successor to ERA-Interim, and MERRA-Land model against 196 in-situ stations from the ISMN and found mean correlation coefficients of 0.66 and 0.69 respectively. Chen et al. (2013) compared the GLDAS model output against in-situ stations on the Tibetan plateau and found that the model underestimates surface soil moisture (0-5cm) but was in good agreement with a deeper layer (10 - 40cm). Correlations of 0.69 (0-5cm) and 0.76 (10-40cm) were found.

## 3.4 IN-SITU REFERENCE PRODUCTS

In situ data from the International Soil Moisture Network (ISMN) is used as a reference. The ISMN provides a harmonized repository of in situ soil moisture observations (https://ismn.geo.tuwien.ac.at/). This harmonization makes it feasible to use in situ data from a wide array of networks. The data quality of stations can vary widely and is not guaranteed to be consistent in time for any station. Wild animals as well as farmers or other natural phenomena can lead to sensor failure or shifts in the location which invalidate the sensor calibration. These errors are partly addressed by various quality and consistency checks that were recently introduced by Dorigo et al. (2013) which aim to automatically detect and flag jumps, plateaus and other unrealistic behaviour in the data. Also checks for realistic maximum and minimum values are performed.

Another issue when comparing remotely sensed and in situ data is spatial representativeness. This means how well an in situ observation, which is essentially a point measurement, represents the data gathered by the much larger satellite footprint. This is also different for each station and depends on topography, soil types and microclimates.

## 3.5 DATA AVAILABILITY

Table 4 shows the data availability of the SWI and the reference datasets, the availability of Metop-B and GLDAS data sets, the beginning and end of the validation period.

Table 4: Available datasets for validation

[TABLE]

An important factor to consider is that the SWI V2 NRT product started production already in June 2012, whereas the SWI V3 test dataset was initialized in April 2013. Different initial values can have a significant influence on SWI time series with high T values for a long time (see Fig. 2). Efforts were made to use the gain values from the SWI NRT processing chain (V2) when initializing the SWIV3 test product. But since this data is stored in an undocumented C++ format the effort to decode it was deemed too big for the benefit of having products that are initialized with the same values. This discrepancy does only influence high T values and since the higher T values are basically an exponentially weighted average of the SWI with T value of 1 we can be certain that they will be equivalent if the SWI with T=1 is the same.

![This is a line chart displaying soil moisture in kilograms per square metre (kg/m²) for a point at latitude 45°, longitude 2°, from May \[2013\] to April 2014. The Y-axis ranges from 10 to 100 kg/m², and the X-axis shows months from May to April, indicating a full year of data. The chart presents five data series: \* \*\*SWIV2 T=1\*\* (blue dotted line): Shows highly variable soil moisture, ranging from approximately 10 kg/m² to 99 kg/m². \* \*\*SWIV2 T=100\*\* (green solid line): Exhibits a smoother trend, starting around 45 kg/m² in May, dropping to a minimum of about 12 kg/m² in September, and rising to a peak of approximately 98 kg/m² in March 2014. \* \*\*SWIV3 T=1\*\* (red dotted line): Displays similar high variability to SWIV2 T=1, with values fluctuating between about 10 kg/m² and 99 kg/m². \* \*\*SWIV3 T=100\*\* (cyan solid line): Presents a smoother trend, starting around 75 kg/m² in May, dropping to about 15 kg/m² in June, then rising to a peak of approximately 98 kg/m² in March 2014. \* \*\*GLDAS layer 0.4-1m\*\* (magenta solid line): Represents soil moisture for the 0.4-1 metre soil layer, starting at approximately 80 kg/m² in May, dropping to a minimum of about 12 kg/m² in September/October, and rising to a peak of approximately 97 kg/m² in February 2014. Both SWIV2 T=1 and SWIV3 T=1 series show strong daily or short-term fluctuations. The SWIV2 T=100, SWIV3 T=100, and GLDAS series depict smoother seasonal trends. Notably, SWIV3 T=100 starts significantly higher than SWIV2 T=100 in May and June, but they converge and track closely from late December 2013 onwards, all reaching high soil moisture levels (above 90 kg/m²) in the winter and early spring months of 2014. All datasets generally show a decline in soil moisture during the summer/autumn period (June-October) and an increase during the winter/spring period (November-March).](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-4d50ef2a6f8b7c9abeac1ee1cebfd02d.png)

Fig. 2: SWI and GLDAS data for a point in France. SWI data was scaled to GLDAS data according to procedure explained in Chapter 3.6. It can be seen that for very similar input data, evident in the very similar SWI values for T=1, the data is quite different for T=100 due to different initial conditions.

## 3.6 SWI PROCEDURE

The aim of this validation report is to assess the performance of the SWIV3 and SWI10 products in the period from 24th of April 2013 until 21st of April 2014 (main validation period) relative to the performance of the SWI NRT product (SWIV2) available from the Copernicus Land Service in the same period.

For the SWI and SWI10 validation the following metrics are used:

- Pearson’s correlation coefficient (R) with a p value \< 0.01
- Root mean square difference (RMSD)

### 3.6.1 Temporal Matching

#### 3.6.1.1 SWI procedure

The reference dataset GLDAS and data from the International Soil Moisture Network (ISMN) were temporally matched to the SWI observation timestamp using nearest neighbour matching. This was necessary since the SWI is a daily dataset whereas the reference datasets have multiple observations per day.

#### 3.6.1.2 SWI10 procedure

SWI10 is a decadal product meaning that only 1 value every ~10 days is available. To make the GLDAS and ISMN datasets comparable, they too were averaged over the same ~10 day period than the SWI10 product.

### 3.6.2 Scaling

Since both the SWI and SWI10 are in a different unit than the reference product, scaling was necessary to ensure consistent results. The used approach was that of min-max scaling. With this method one dataset is scaled to have the same maximum and minimum values as the other dataset. This approach was taken since it does not completely remove the bias as does e.g. scaling to the same mean and standard deviation. At first also experiments with linear CDF matching after (Liu et al. 2011) were made but it was discovered that the matching failed for high T-values in very dry regions because the algorithm was unable to calculate the necessary percentiles.

The SWI products were scaled into the GLDAS or in-situ data space. This approach was taken to ensure the comparability of the RMSD results. Before the calculation of the metrics, observations where the Surface State Flag showed frozen were removed. If less than 10 observations remained for a grid point, no metrics were calculated.

## 3.7 SSF PROCEDURE

For the SSF validation the following metrics are used:

- Percentage of correctly classified observations (percent_valid)
- Period of consecutive misclassified days (mean) (wrong_days)

Temporal matching was done in the same way as described for the SWI.

Classification of the SSF values into the binary correct-incorrect form was done using the classification scheme outlined inTable 5. The soil temperature was taken from the first layer of the used land surface model. The percent_valid metric was then calculated as the percentage of correctly classified observations as a fraction of all observations. Wrong_days was calculated by finding consecutive periods of wrong classification and measuring their length in days. Since each grid point can have multiple such periods the mean length of these periods is reported.

Table 5: Classification scheme

| SSF value | Soil temperature | Classification |
|-----------|------------------|----------------|
| 1, 3      | \>= 0°C          | Correct        |
| 2         | \< 0°C           | Correct        |
| 1, 3      | \< 0°C           | Incorrect      |
| 2         | \>= 0°C          | Incorrect      |

## 3.8 COMPARISON MATRIX

The different T-values of the SWI products were compared to different layers of the GLDAS model. This was done since higher T-values represent deeper soil layers. Table 6Table 6 shows which T-values were compared to which layer of the model and to which depth of the in situ stations.

Table 6: Which T-values were compared to which layer of the GLDAS model

| SWI/SWI10 T-Value    | GLDAS layer depth | in situ observation depth |
|----------------------|-------------------|---------------------------|
| 1, 5, 10, 15, 20, 40 | 0 - 0.1 m         | 0-0.1m                    |
| 60, 100              | 0.4 - 1 m         | 0-0.1m                    |

# 4 RESULTS

The comparisons were done for all 8 T-Values but since the results are very similar for all T values we will only show the comparisons for T=1 T=20 and T=100 for products which have the same initialization.

For the comparisons with the current operational product SWIV2, only results for T=1 and T=20 will be shown. This is because the results for the higher T values are not comparable because of the different initialization times.

## 4.1 COMPARISON TO GLDAS

Al-Yaari et al. (2014) compared ASCAT and SMOS data to the MERRA land surface model and found similar results than those found for the SWIV3 in this document. Low correlations were observed in arid and semi-arid regions as well as high latitude regions whereas other areas showed high positive correlations (see Fig. 3 and Fig. 4). RMSD values are lower for arid regions because of the smaller dynamic range of soil moisture in these areas. High RMSD can be observed in northern regions where soil moisture is generally higher (see Fig. 5 and Fig. 6). In general, the GCOS requirements of 0.04 m³/m³ are not reached for all regions. This hard threshold of 0.04 m³/m³ is not applicable everywhere though. GCOS themselves state in the requirements that this number was chosen to approximately be 10% of the saturated content which varies widely between soil and climate types.

### 4.1.1 SWIV2-GLDAS compared to SWIV3-GLDAS

In this section, the results of comparing the new SWIV3 product with GLDAS data are compared to those of the SWIV2 – GLDAS comparison. Pearson correlation coefficients shown in Fig. 3 and Fig. 4 show that R of SWIV3 is very similar to the R scores of SWIV2. The observed differences of ± 0.06 are not significant within a 95% confidence interval. The results for T=20 shown in Fig. 4 show slightly higher differences which is expected since the two SWI datasets were not initialized with the same starting values which is more important for high T values.

![This figure presents a multi-panel comparison of global Pearson's R correlation for Soil Water Index (SWI) products at a T-value of 1, along with a cumulative histogram of differences. The top-left panel is a global choropleth map titled 'SWI V3 - Metop A and B', showing Pearson's R correlation values ranging from -1.0 (dark red) to 1.0 (dark blue), with 0.0 represented by white. High positive correlations (0.6 to 1.0) are widely distributed across North and South America, Northern Europe, large parts of Russia, and Australia. The top-right panel is a global choropleth map titled 'SWI V2 - Metop B', also showing Pearson's R correlation values with the same colour scale (dark red -1.0 to dark blue 1.0, white 0.0). It exhibits a similar global pattern of positive correlations in comparable regions to the SWI V3 map. The bottom-left panel is a global choropleth map titled 'SWI V3 - SWI V2', depicting the difference in Pearson's R correlation between the SWI V3 and SWI V2 products. The colour scale ranges from -0.060 (dark red) to 0.060 (dark blue), with 0.000 (white) indicating no difference. Blue areas suggest higher correlation for SWI V3, while red areas indicate higher correlation for SWI V2. Differences, both positive and negative, are observed across most land areas, without a clear global dominance of one version. The bottom-right panel is a cumulative histogram of the differences (likely corresponding to the SWI V3 - SWI V2 correlation differences). The X-axis represents the difference values from -1.5 to 1.5, and the Y-axis represents cumulative frequency from 0.0 to 1.2. The green shaded area shows a sharp increase in cumulative frequency around 0.0 to 0.2, reaching 1.0 (100% of differences) near a difference value of 0.2, indicating that a majority of the differences are concentrated around zero or slightly positive.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-05bcf12621d92c30c8d83e8286c27f04.png)

Fig. 3: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

![This image displays four panels: three global choropleth maps showing Pearson's R correlation coefficients for Soil Water Index (SWI) products at a T-value of 20, and one cumulative histogram of differences. The top-left map, titled 'SWI V3 - Metop A and B', shows the global Pearson's R for SWI Version 3, derived from Metop A and B satellite data. The colour scale ranges from dark red (-1.0) to dark blue (1.0), with white representing 0.0, in increments of 0.2. High positive correlations (blue shades) are observed across North America, Europe, northern Eurasia, parts of South America, and Australia. Negative or low correlations (red/white shades) are scattered, notably in some arid and semi-arid regions. The top-right map, titled 'SWI V2 - Metop B', shows the global Pearson's R for SWI Version 2, derived from Metop B satellite data. It uses the same colour scale as the SWI V3 map. The spatial pattern of correlations is generally similar to SWI V3, with widespread positive correlations in comparable regions. The bottom-left map, titled 'SWI V3 - SWI V2', illustrates the differences in Pearson's R between SWI V3 and SWI V2 (SWI V3 minus SWI V2). The colour scale for this map ranges from dark red (-0.08) to dark blue (0.08), with white representing 0.00, in increments of 0.02. This indicates that most differences are small. Regions with higher SWI V3 correlation (blue shades) are scattered, including parts of the Amazon basin, central Africa, and northern Australia. Regions with higher SWI V2 correlation (red shades) appear in parts of North America and Europe. The bottom-right panel, titled 'cumulative histogram of differences', is a cumulative histogram. The X-axis represents 'differences' and ranges from -2.0 to 2.0. The Y-axis (unlabelled) ranges from 0.0 to 1.0. The green-filled histogram shows that approximately 80% of the differences are positive and fall between 0.0 and 1.8, with the majority of values clustering near 0.0, indicating that the differences between the two SWI versions are mostly small and slightly positive on average.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-a592546679de80ec882e22bd5a2af466.png)

Fig. 4: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

Fig. 5 and Fig. 6 also show that in terms of RMSD the differences are small. The RMSD for T=1 seems to be slightly lower for the SWIV3 product in South America. In North America slightly higher RMSD for SWIV3 is observed but these differences are so small that interpreting them in a meaningful way is hardly possible.

Overall the differences in RMSD are higher for T=20. This is because of the different initialization times.

![This visual presents a comparison of Soil Water Index (SWI) products, including three global choropleth maps and one cumulative histogram. The overall title indicates the data is 'SWI T=1 RMSD in m³/m³'. The top-left map displays the Root Mean Square Deviation (RMSD) for 'SWI V3 - Metop A and B' over global landmasses. Its colour scale ranges from 0.03 (dark brown) to 0.11 (dark blue) m³/m³. Higher RMSD values (blue) are prevalent in northern latitudes of North America, Europe, and Asia, while lower RMSD values (brown/yellow) are seen in arid and semi-arid regions such as the Sahara Desert, Arabian Peninsula, and Australia. The top-right map shows the RMSD for 'SWI V2 - Metop B' over global landmasses, using the same colour scale and units (0.03 to 0.11 m³/m³) as the SWI V3 map. The spatial distribution of RMSD values is highly similar to the SWI V3 map, indicating consistent performance patterns between the two versions. The bottom-left map illustrates the difference between 'SWI V3 - SWI V2' for the global landmasses. This map uses a distinct colour scale ranging from -0.0045 (dark brown) to 0.0045 (dark blue) m³/m³, with 0.0000 represented by light yellow/white. Most regions show differences close to zero (light colours), while some areas, particularly in Central Asia and parts of North America, exhibit slightly positive (blue) or negative (brown) differences. The bottom-right chart is a 'cumulative histogram of differences'. The x-axis represents the differences, ranging from -0.15 to 0.20. The y-axis shows the cumulative frequency, from 0.0 to 1.0. The histogram indicates that approximately 90% of the differences between SWI V3 and SWI V2 are positive and fall within the range of 0.0 to 0.02, with the cumulative frequency sharply rising from near 0.0 to 1.0 within this interval.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-6568c6d176494e654dea2fa2b773e62c.png)

Fig. 5: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

![This image displays four plots: three global maps showing Soil Water Index (SWI) T=20 Root Mean Square Deviation (RMSD) and differences, and one cumulative histogram of differences. The top-left map, titled 'SWI V3 - Metop A and B', shows global RMSD in m³/m³ for SWI Version 3 derived from Metop A and B satellites. The colour scale ranges from 0.040 m³/m³ (dark brown) to 0.120 m³/m³ (dark blue). Regions like the Sahara Desert and Australia show lower RMSD (brown/yellow), while northern high-latitude areas and parts of Southeast Asia show higher RMSD (blue). The top-right map, titled 'SWI V2 - Metop B', shows global RMSD in m³/m³ for SWI Version 2 derived from Metop B satellites, using the same colour scale and unit (m³/m³). The spatial pattern of RMSD is similar to SWI V3, with lower values in arid regions and higher values in northern humid regions. The bottom-left map, titled 'SWI V3 - SWI V2', illustrates the difference in RMSD between SWI V3 and SWI V2 globally. The colour scale ranges from -0.010 m³/m³ (dark brown) to 0.010 m³/m³ (dark blue), with 0.000 m³/m³ represented by white. Blue areas indicate higher RMSD for SWI V3 compared to SWI V2 (e.g., parts of North America, Europe, Central Asia), while brown/yellow areas indicate lower RMSD for SWI V3 (e.g., parts of South America, Africa, Australia). The bottom-right plot is a 'cumulative histogram of differences'. The X-axis represents the differences, ranging from -0.20 to 0.20, and the Y-axis represents the cumulative frequency from 0.0 to 1.0. The histogram shows that the majority of differences are concentrated near 0.0, with the cumulative frequency reaching 0.5 (50%) slightly above 0.0, and reaching 1.0 (100%) around 0.05. This suggests that positive differences (SWI V3 having higher RMSD) are more frequent than negative differences.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-493660d0754b846742dcd6a1219f7a73.png)

Fig. 6: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

### 4.1.2 SWIV3 - GLDAS compared to SWIV3_B - GLDAS

In this section, the SWIV3 product is compared to a SWIV3 product computed only with the input data from ASCAT on board Metop-B (SWIV3_B). This was done to see if a hypothetical sensor failure would have an influence on the accuracy of the product. Fig. 7 to Fig. 12 show the results of this comparison for T values 1, 20 and 100 for both Pearson’s R and RMSD. Only very small differences can be observed in these plots. For T=1, both R and RMSD show slightly better values when both Metop A and B are used but it is hard to argue that these differences are really significant using 1 year of data. Higher T values show what seem to be random differences. This can be expected because the high T values average over time and thus an additional observation from e.g. Metop A will not have much influence.

![The image displays three global choropleth maps and one cumulative histogram, all related to Soil Wetness Index (SWI) T=1 Pearson's R correlation. The top left map, titled 'Metop A and B', shows global Pearson's R values for SWI T=1 derived from combined Metop A and Metop B satellite data. The colour scale ranges from deep red (-1.0) to deep blue (1.0), with white/light blue around 0.0. Areas with high positive correlations (0.6 to 1.0, dark blue) are observed in parts of South America, Central Africa, Eastern Europe, and Eastern Asia. Low or negative correlations (red/white) are prominent in arid regions like North Africa, the Arabian Peninsula, Central Asia, and high northern latitudes such as Canada and Russia. The top right map, titled 'Metop B', shows global Pearson's R values for SWI T=1 derived from Metop B satellite data alone, using the same colour scale. The spatial pattern of correlation closely resembles that of the 'Metop A and B' map. The bottom left map, titled 'Metop A and B - Metop B', illustrates the difference in Pearson's R values between the 'Metop A and B' product and the 'Metop B' product. This map uses a dedicated colour scale ranging from deep red (-0.04) to deep blue (0.04), with white around 0.00. Blue areas indicate higher correlation for 'Metop A and B', while red areas indicate higher correlation for 'Metop B'. Differences are generally small, mostly within ±0.04, with slightly positive differences (more blue) observed in regions such as parts of North America, North Africa, and Eastern Europe. The bottom right plot is a 'cumulative histogram of differences'. The X-axis ranges from -1.5 to 1.0, and the Y-axis represents cumulative frequency from 0.0 to 1.2. The green shaded area shows that the majority of these 'differences' (most likely referring to the Pearson's R values themselves, representing differences from zero correlation, given the overall context) are positive, primarily distributed between approximately 0.0 and 0.6, indicating a prevalence of positive correlations.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-6f1af382ded607e0be58bb511c05f384.png)

Fig. 7: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

![This figure presents three global maps displaying the Pearson's R correlation coefficient for the Soil Water Index (SWI) with a T-value of 20, derived from Metop satellite data. The fourth panel is a cumulative histogram of differences. The top-left map, titled 'Metop A and B', shows Pearson's R values globally using combined Metop A and Metop B data. The colour scale ranges from -1.0 (dark red, strong negative correlation) to 1.0 (dark blue, strong positive correlation), with 0.0 represented by white. High positive correlations (blue) are prevalent in tropical regions (e.g., Amazon basin, Central Africa, Southeast Asia) and parts of Eastern Europe. Low or negative correlations (red) are observed in arid and semi-arid regions (e.g., North Africa, Arabian Peninsula, Central Asia, Western USA) and high latitude areas. The top-right map, titled 'Metop B', shows Pearson's R values globally using only Metop B data, employing the same colour scale as the 'Metop A and B' map. The spatial pattern of correlations is largely similar to the combined Metop A and B map, with blue indicating high positive correlations and red indicating low/negative correlations in similar geographical areas. The bottom-left map, titled 'Metop A and B - Metop B', illustrates the differences in Pearson's R between the combined Metop A and B product and the Metop B product. Its colour scale ranges from -0.032 (dark red) to 0.032 (dark blue), with 0.000 as white. The map shows very small differences, mostly concentrated around 0.000, indicating high consistency between the two products. Minor positive differences (blue) are visible in some areas of Europe and North America, while minor negative differences (red) appear in parts of Africa and South America. The bottom-right panel displays a 'cumulative histogram of differences'. The X-axis spans from -1.5 to 1.5, representing the magnitude of differences (likely in soil moisture units, e.g., m³/m³, given the surrounding document context discussing RMSD and GCOS requirements). The Y-axis represents the cumulative frequency, ranging from 0.0 to 1.2. The histogram indicates that almost all differences are positive, with the cumulative frequency rising sharply from approximately 0.0 on the X-axis to 1.0 on the Y-axis, before flattening, suggesting that nearly all observed differences fall between 0.0 and 1.0.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-ca9fe3af792b63a96fb8222bb7320162.png)

Fig. 8: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

![The image presents four plots: three global choropleth maps showing Pearson's R correlation coefficients or their differences for the Soil Water Index (SWI) at T=100, and one cumulative histogram of differences. The top-left map, titled 'Metop A and B', displays global Pearson's R values. Its colour scale ranges from dark red (-1.0) for negative correlation to dark blue (1.0) for positive correlation, with 0.0 represented by white/light grey. High positive correlations (blue) are widespread across North America, Europe, parts of Russia, East Asia, and South America. Low or negative correlations (red) are prominent in arid regions like the Sahara Desert, the Arabian Peninsula, Central Asia, and high-latitude northern areas. The top-right map, titled 'Metop B', also shows global Pearson's R values using the identical colour scale (dark red to dark blue, -1.0 to 1.0). The spatial pattern of correlations closely mirrors that of the 'Metop A and B' map, indicating similar strong positive correlations in temperate and tropical zones and low/negative correlations in arid and northern high-latitude regions. The bottom-left map, titled 'Metop A and B - Metop B', illustrates the differences in Pearson's R values between the 'Metop A and B' and 'Metop B' datasets. The colour scale ranges from dark red (-0.05) through white (0.00) to dark blue (0.05). Most land areas show minimal differences clustered around 0.00, appearing as white/light grey. Scattered regions exhibit slightly positive differences (blue, up to 0.05) or slightly negative differences (red, down to -0.05). The magnitudes of these differences are significantly smaller than the absolute Pearson's R values. The bottom-right plot is a 'cumulative histogram of differences'. The X-axis spans from -2.0 to 2.0 (representing Pearson's R differences), while the Y-axis indicates cumulative frequency from 0.0 to 1.0. The histogram shows that the cumulative frequency rises sharply from approximately 0.0 on the X-axis, reaching a maximum of 1.0 by roughly X=0.2. This indicates that almost all observed differences are positive and tightly clustered near zero.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-0b883f0839f42c5b426f4058a03fde52.png)

Fig. 9: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=100.

![This image presents four panels: three global maps displaying Soil Water Index (SWI) T=1 Root Mean Square Difference (RMSD) in m³/m³, and one cumulative histogram of differences. The top-left map, titled 'Metop A and B', shows the global distribution of SWI T=1 RMSD calculated from combined Metop A and B satellite data. The top-right map, titled 'Metop B', shows the global distribution of SWI T=1 RMSD from Metop B data alone. Both maps use a common colour scale ranging from 0.03 m³/m³ (brown-yellow) to 0.11 m³/m³ (dark blue), with intermediate values 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, and 0.10 m³/m³. High RMSD values (blue) are observed in high-latitude regions such as Canada, Northern Europe, and Siberia, as well as parts of the tropics. Lower RMSD values (brown-yellow) are present in arid and semi-arid regions like the Sahara Desert, Arabian Peninsula, and Central Australia. The Global Climate Observing System (GCOS) requirement of 0.04 m³/m³ is visible on the colour scale. The bottom-left map, titled 'Metop A and B - Metop B', illustrates the difference in SWI T=1 RMSD values between the combined Metop A and B datasets and the Metop B dataset alone. This map uses a diverging colour scale from -0.0045 m³/m³ (dark brown) through 0.0000 m³/m³ (light green/white) to 0.0045 m³/m³ (dark blue), with intermediate values -0.0030, -0.0015, 0.0015, and 0.0030 m³/m³. Most land areas display differences concentrated around 0.0000 m³/m³, indicating very small changes in RMSD, though some regions show minor negative (brown) or positive (blue) differences. The bottom-right panel displays a 'cumulative histogram of differences', representing the data from the 'Metop A and B - Metop B' map. The x-axis ranges from -0.15 to 0.15, indicating the magnitude of the RMSD differences. The y-axis represents cumulative probability from 0.0 to 1.0. The histogram shows a very sharp increase in cumulative probability around the 0.00 mark, indicating that the vast majority of RMSD differences are concentrated very close to zero, suggesting high consistency between the two Metop datasets.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-f7b969d632ce1bd9e6a892822c8c29e1.png)

Fig. 10: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

![This image comprises three global maps showing Soil Water Index (SWI) T=20 Root Mean Square Deviation (RMSD) in m³/m³, and one cumulative histogram of differences. The top left map, titled 'Metop A and B', displays the global RMSD based on combined Metop A and B satellite data. The colour legend ranges from 0.040 m³/m³ (brown) to 0.120 m³/m³ (dark blue). Regions with higher RMSD (blue) include northern latitudes (e.g., North America, Europe, Siberia) and some equatorial regions (e.g., Amazon basin, Central Africa), while arid and semi-arid regions (e.g., Sahara, Arabian Peninsula, Australia) show lower RMSD (brown/yellow). The top right map, titled 'Metop B', displays the global RMSD based on Metop B satellite data alone, using the same colour legend and range (0.040 m³/m³ to 0.120 m³/m³). The spatial distribution of RMSD values is largely similar to the Metop A and B combined map. The bottom left map, titled 'Metop A and B - Metop B', shows the difference in RMSD between the combined Metop A and B data and Metop B data. The colour legend ranges from -0.004 m³/m³ (dark brown) to 0.004 m³/m³ (dark blue), with 0.000 m³/m³ represented by light blue/green. Most areas show differences close to 0.000 m³/m³, with scattered small positive (blue) or negative (brown) differences. The bottom right panel is a cumulative histogram of differences. The X-axis represents differences, ranging from -0.15 to 0.15. The Y-axis represents cumulative frequency, ranging from 0.0 to 1.0. The histogram shows that the majority of differences are clustered very close to 0.00, with cumulative frequency reaching 1.0 at approximately 0.03.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-f821193d18f8951006f2698a1a7148c7.png)

Fig. 11: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

![This image displays three global maps showing Soil Water Index (SWI) Root Mean Square Deviation (RMSD) for a T-value of 100, measured in m³/m³, alongside a cumulative histogram of the RMSD differences. The top-left map, titled 'Metop A and B', shows the global distribution of SWI T=100 RMSD, with a colour scale ranging from 0.00 (dark brown) to 0.09 (dark blue). Higher RMSD values (blue tones) are primarily visible in parts of North America, Europe, Asia, and coastal regions of South America, while lower values (brown/yellow tones) are found in areas such as North Africa, Central South America, and parts of Australia. The top-right map, titled 'Metop B', displays the global SWI T=100 RMSD using data from Metop B only, with the same colour scale (0.00 to 0.09 m³/m³). Its spatial distribution of RMSD values closely resembles that of the 'Metop A and B' map. The bottom-left map, titled 'Metop A and B - Metop B', illustrates the differences in SWI T=100 RMSD between the Metop A and B dataset and the Metop B dataset. The colour scale for differences ranges from -0.0032 (dark brown) to 0.0032 (dark blue), with 0.0000 represented by light grey. Positive differences (blue tones) indicate higher RMSD for the combined Metop A and B data, while negative differences (brown tones) indicate higher RMSD for Metop B data. Most land areas show differences close to zero (light colours), indicating small overall discrepancies. The bottom-right plot is a cumulative histogram of these differences. The X-axis represents the differences, ranging from -0.10 to 0.15. The Y-axis represents cumulative frequency, from 0.0 to 1.2. The histogram shows a sharp increase in cumulative frequency from 0.0 at approximately 0.00 to 1.0 at around 0.015, indicating that the vast majority of RMSD differences between the two Metop datasets are very small and slightly positive.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-e743e04c927ab35975a92002ad7683f8.png)

Fig. 12: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV3 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=100.

### 4.1.3 SSFV2 compared to SSFV3

In this section, the SSF from the current operational product (SSFV2) is compared to the SSF computed with the new SSFV3 processor. The basic algorithm is the same but the bugs that were found in the SSFV2 are no longer present in SSFV3. Fig. 13 and Fig. 14 show the result of this comparison. It can be seen that the bug that was present in SSFV2 until the end of 2013 affected the results. The most affected areas are the Gobi desert and parts of the Andes and a small part in Libya as well as areas in the Canadian Rocky Mountains. These are all areas where the algorithm presented in Naeimi et al. (2012) is not applicable (see Figure 5 in Naeimi et al. 2012).

The differences in Libya come from the fact that the bug in SSFV2 prevented the application of probabilistic flags included in the Surface Soil Moisture (SSM) input product. These flags give probabilities of frozen soil and snow cover for each day of the year. The probability for frozen soil were derived from the ERA40 model which indeed shows temperatures below 0°C in these regions around the end of December of each year.

In all other regions the results are almost identical.

The results for the comparison between SSFV3 and SSFV3_B (only with Metop-B data) are not shown since no systematic differences were found.

![This figure presents a set of four plots, including three global maps and one cumulative histogram, detailing the correct classification percentage of a Soil State Fraction (SSF) product. The overall title is 'SSF correct classification in %'. The top-left map, titled 'SSF V3 - Metop A and B', displays the global correct classification percentage for SSF Version 3 derived from both Metop A and Metop B satellite data. A colour scale from brown (0%) to dark blue (100%) indicates classification accuracy. Most vegetated land areas, including North America, Europe, and large parts of Africa and Asia, show high correct classification, primarily in the 80-100% range (dark blue). Arid regions tend to have lower classification percentages. The top-right map, titled 'SSF V2 - Metop B', shows the global correct classification percentage for SSF Version 2, derived solely from Metop B satellite data. The same colour scale is used. This map exhibits generally lower classification percentages compared to the V3 product, with more widespread areas in North America, Central Asia, and Australia falling into the 40-70% accuracy range (yellow to light blue). The bottom-left map, titled 'SSF V3 - SSF V2', illustrates the difference in correct classification percentage between SSF V3 (Metop A and B) and SSF V2 (Metop B). The colour scale for this map ranges from dark brown (-2.0) to dark blue (2.0), with light grey representing values around 0.0. Blue areas (positive values, up to 2.0%) indicate that SSF V3 has a higher correct classification percentage. These improvements are notable in North America, Europe, and Northern Asia. Orange/brown areas (negative values, down to -2.0%) indicate regions where SSF V2 shows slightly higher correct classification, primarily in arid zones such as the Sahara Desert, parts of Australia, and southern South America. The magnitudes of these differences are generally small, mostly within ±2.0%. The bottom-right plot is a 'cumulative histogram of differences'. The X-axis represents the magnitude of differences, ranging from -100 to 100. The Y-axis represents the cumulative frequency, from 0.0 to 1.0. The histogram shows a steep increase in cumulative frequency around 0, indicating that the vast majority of differences between SSF V3 and SSF V2 are close to zero. The curve rapidly approaches 1.0, confirming that very few large differences exist.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-b22ca87dc1c83a00ae3a69ef9876a7c8.png)

Fig. 13: Maps of correctly classified days in percent for SSFV3 using Metop A and B, SSFV2 using only Metop B and the differences between the two. The lower right plot shows a cumulative histogram of these differences.

![This image presents a comparison of the mean 'SSF Consecutive days wrongly classified' metric across two product versions and their difference, alongside a cumulative histogram of these differences. The top-left map, titled 'SSF V3 - Metop A and B', displays the global mean consecutive days wrongly classified for the SSF Version 3 product, which integrates data from both Metop A and Metop B satellites. The colour scale ranges from 1.5 (dark brown) to 12.0 (dark blue) days, with intermediate values at 3.0, 4.5, 6.0, 7.5, 9.0, and 10.5. Higher values (blue colours) indicate more consecutive days wrongly classified. Spatially, the highest values (dark blue, \>9.0 days) are observed in high northern latitudes, including Canada, Alaska, Northern Europe, and Siberia. The top-right map, titled 'SSF V2 - Metop B', shows the global mean consecutive days wrongly classified for the SSF Version 2 product, using data exclusively from the Metop B satellite. It employs the identical colour scale as the SSF V3 map, ranging from 1.5 (dark brown) to 12.0 (dark blue) days. The spatial pattern of errors is similar to that of SSF V3, with elevated classification errors (dark blue) concentrated in the northern high latitudes. The bottom-left map, titled 'SSF V3 - SSF V2', illustrates the difference in mean consecutive days wrongly classified between SSF V3 (Metop A and B) and SSF V2 (Metop B). The colour scale for differences ranges from -12 (dark brown) to 12 (dark blue) days, with intermediate values at -9, -6, -3, 0 (light blue/white), 3, 6, and 9. Positive values (blue) indicate that SSF V3 has more wrongly classified days than SSF V2, while negative values (brown) suggest SSF V2 has more. Most areas show differences close to 0 (light blue/white), indicating minimal change. Some regions in North America and Siberia show slightly higher errors for SSF V3 (blue), whereas parts of Central Asia, Eastern Europe, and the US Midwest show slightly lower errors for SSF V3 (brown). The bottom-right plot is a 'cumulative histogram of differences'. Its X-axis represents the differences, spanning approximately -400 to 400. The Y-axis represents cumulative frequency, from 0.0 to 1.0. The histogram shows that the cumulative frequency rises steeply from 0.0 to 1.0 within a narrow range, starting near 0 and reaching 1.0 around 50. This indicates that the vast majority of differences between SSF V3 and SSF V2 in consecutive days wrongly classified are small and positive, clustered closely around zero.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-d2b678f26e66836c1e325cdf5494dd24.png)

Fig. 14: Maps of mean of consecutive days wrongly classified for SSFV3 using Metop A and B, SSFV2 using only Metop B and the differences between the two. The lower right plot shows a cumulative histogram of these differences.

### 4.1.4 Comparison of GLDAS and SWI10

In 13 months of available test data for the SWIV3, 39 SWI10 products are generated which leads to a pretty small sample size for calculating the metrics. This is also the reason why for Fig. 15 to Fig. 17 the p value for R values that will be shown was increased from 0.01 to 0.1. Pearson’s correlation coefficient shows the same large scale patterns than SWIV3 or SWIV2 which gives confidence that the conversion algorithm works correctly. It is expected that the performance of SWI10 and SWIV3 is very similar as soon as sufficiently long time series are available for both products. The missing R values around zero correlation are because only correlations with ap value \< 0.1 are shown.

The RMSD values shown in Fig. 18 to Fig. 20 also show the same patterns as Fig. 10 to Fig. 12 but show higher values in parts of Africa, South America and India. These are also regions in which the correlation was not significant so this should not be taken as a real issue but is most likely related to the small sample size.

![This image displays a global map of Pearson's R correlation coefficient for the Soil Water Index (SWI10) with a characteristic time length T=1, accompanied by a histogram of these correlation values. The upper panel is a choropleth map of the world's land masses. The colour scale on the right ranges from -1.0 (dark red) to 1.0 (dark blue), representing the Pearson's R values. Values around 0.0 are depicted in white/light blue. Strong positive correlations (dark blue, 0.8 to 1.0) are visible in northern latitudes of North America (e.g., central USA, Canada), parts of Europe (e.g., Scandinavia, Eastern Europe), and Asia (e.g., Siberia). Strong negative correlations (dark red, -0.8 to -1.0) are present in specific areas such as Alaska, northern Canada, and Arctic regions of Eurasia. Tropical and arid regions, including the Sahara Desert, Amazon basin, and parts of Australia, generally show correlation values close to 0.0 or no data. The lower panel is a histogram titled 'histogram', showing the distribution of the Pearson's R values. The X-axis represents Pearson's R values from -1.0 to 1.0. The Y-axis represents frequency/density, ranging from 0.0 to 4.0. The histogram exhibits a bimodal distribution: a smaller peak is visible around -0.6 to -0.5, with frequencies up to approximately 0.7, covering values from -1.0 to about -0.1. A larger, broader peak is centred around 0.3 to 0.4, with a maximum frequency close to 4.0, covering values from about 0.1 to 1.0.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-1bf9e82c108e475bab08396fa69c3509.png)

Fig. 15: Pearson’s R between GLDAS Layer 1 (0 – 0.1m) and SWI10 T=1 with a p-value \< 0.1 (top) and histogram of R (bottom)

![This image displays a global map showing the spatial distribution of Pearson's correlation coefficient (R) for the Soil Water Index (SWI10) with a T parameter of 20, along with a histogram illustrating the distribution of these R values. The upper panel is a choropleth map of the world. The colour scale on the right ranges from dark red (-1.0) through white (0.0) to dark blue (1.0). Red tones indicate negative correlation: -1.0 (darkest red), -0.8, -0.6, -0.4, -0.2. Blue tones indicate positive correlation: 0.2, 0.4, 0.6, 0.8, 1.0 (darkest blue). Light blue/white colours represent correlation values close to zero. Spatially, strong negative correlations (dark red) are visible across large parts of northern North America (e.g., Canada, Alaska) and northern Eurasia (e.g., Russia). Strong positive correlations (dark blue) are observed in regions such as the Great Plains of North America, southern South America (e.g., Patagonia), parts of Australia, and scattered areas in Europe and Asia. Much of Africa and parts of South America show very low or near-zero correlation values (light blue/white). The lower panel is a histogram showing the frequency distribution of the Pearson's R values. The X-axis represents Pearson's R values, ranging from -1.0 to 1.0. The Y-axis represents frequency/density, ranging from 0.0 to 3.5. The histogram exhibits a bimodal distribution with two distinct clusters of values. One cluster peaks around -0.6, covering R values from approximately -1.0 to -0.2, with a maximum frequency of around 0.9. The other, more pronounced cluster peaks around 0.3, covering R values from approximately 0.2 to 1.0, and reaches a maximum frequency above 3.0. There is a clear gap in frequencies for R values between roughly -0.2 and 0.2.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-a810fef807cdace5a0006a5bf05071ba.png)

Fig. 16: Pearson’s R between GLDAS Layer 1 (0 – 0.1m) and SWI10 T=20 with a p-value \< 0.1 (top) and histogram of R (bottom)

![This image displays a global map showing the spatial distribution of Pearson's R correlation coefficients for Soil Water Index (SWI) at T=100 days (SWI10 T=100), accompanied by a histogram of these correlation values. The upper part is a world map depicting Pearson's R values using a continuous colour scale from dark blue (1.0, strong positive correlation) through white (0.0, no linear correlation) to dark red (-1.0, strong negative correlation). Regions showing strong positive correlations (blue tones, 0.2 to 1.0) are widespread across large parts of Russia, Northern and Eastern Europe, central and western North America, parts of the Amazon basin in South America, central Africa, and parts of Australia. Areas with negative correlations (red tones, -0.2 to -1.0) are patchier, appearing in scattered locations across North America, South America, Africa, the Middle East, and parts of Asia. Areas near zero correlation (white) or with no data (uncoloured) are prominent in deserts and polar regions. The lower part is a histogram titled 'histogram', showing the frequency distribution of the Pearson's R values. The X-axis ranges from -1.0 to 1.0, representing Pearson's R values, while the Y-axis indicates frequency/density, ranging from 0.0 to 3.5. The histogram exhibits a bimodal distribution with two main peaks. One peak is centred around -0.4 (extending from approximately -1.0 to -0.2) and another, more prominent peak, is centred around 0.3 (extending from approximately 0.2 to 1.0). There is a noticeable gap in the distribution between approximately -0.2 and 0.2, indicating fewer observations in this range. The highest frequency occurs around a Pearson's R value of 0.3, reaching a Y-axis value of over 3.0.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-17bf959c6c622bbdc5be5701a5ffe420.png)

Fig. 17: Pearson’s R between GLDAS Layer 3 (0.4 - 1m) and SWI10 T=100 with a p-value \< 0.1 (top) and histogram of R (bottom)

![A global choropleth map displays the Root Mean Square Deviation (RMSD) for the Soil Water Index (SWI10) calculated with a time constant T=1, measured in m³/m³. The colour scale ranges from dark brown (0.030 m³/m³) to dark blue (0.135 m³/m³), with intermediate values marked at 0.045, 0.060, 0.075, 0.090, 0.105, and 0.120 m³/m³. Regions with low RMSD (dark brown to yellow) are prominently visible in arid zones such as the Sahara Desert, Arabian Peninsula, Central Asia, parts of Australia, and the western United States. Higher RMSD values (light to dark blue) are observed in humid areas like the Amazon basin, Central Africa, Southeast Asia, Eastern Europe, and the eastern United States. Below the map, a histogram illustrates the distribution of these RMSD values. The x-axis represents RMSD values from 0.00 to 0.30 m³/m³, with major ticks at 0.05 increments. The y-axis, representing frequency, ranges from 0 to 9, with major ticks at 1-unit increments. The histogram shows a distribution heavily skewed towards lower RMSD values, peaking between approximately 0.04 and 0.07 m³/m³, then gradually decreasing towards 0.20 m³/m³.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-26b450d6c22f0d6cfa2621a9b84f8cd2.png)

Fig. 18: RMSD between GLDAS Layer 1 (0 – 0.1m) and for SWI10 T=1 (top) and histogram of RMSD (bottom)

![This image comprises two components: a global map displaying the Root Mean Square Difference (RMSD) for the Soil Water Index (SWI10) at a characteristic time length parameter T=20, and a histogram showing the distribution of these RMSD values. The RMSD is measured in m³/m³. The global map uses a colour scale ranging from 0.030 (dark brown) to 0.135 (very dark blue). Specific values along the legend are 0.030, 0.045, 0.060, 0.075, 0.090, 0.105, 0.120, and 0.135 m³/m³. Brown and orange hues indicate lower RMSD, while blue hues indicate higher RMSD. Regions showing higher RMSD (blue colours) include central North America, parts of the Amazon basin in South America, central Africa, parts of Northern Europe and Siberia, and Southeast Asia. Regions exhibiting lower RMSD (brown and orange colours) include the Sahara Desert, the Arabian Peninsula, the Gobi Desert, parts of the Andes mountain range, and Australia. The lower panel shows a histogram of the RMSD values. The X-axis represents RMSD values, ranging from 0.00 to 0.35. The Y-axis, which is unlabelled, likely represents frequency or count, ranging from 0 to 9. The distribution is skewed right, with the highest frequencies observed for RMSD values between approximately 0.04 and 0.08 m³/m³. The frequency gradually decreases for higher RMSD values, with the majority of the data concentrated below 0.15 m³/m³.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-5f6976c5d00e62f52e4e24cd74fe3204.png)

Fig. 19: RMSD between GLDAS Layer 1 (0 – 0.1m) and for SWI10 T=20 (top) and histogram of RMSD (bottom)

![This image displays a global map of SWI10 (Soil Water Index, 10-day composite) T=100 Root Mean Square Difference (RMSD) values in m³/m³, along with a histogram showing the frequency distribution of these values. The upper panel presents a world map indicating the spatial distribution of SWI10 T=100 RMSD. A continuous colour scale ranges from dark brown (0.000 m³/m³) to dark blue (0.120 m³/m³), with intermediate values of yellow (around 0.030 m³/m³) and light blue (around 0.090 m³/m³). Areas with lower RMSD values (blue tones) are observed in regions such as the Amazon basin, Eastern North America, parts of Europe, and Southeast Asia. Higher RMSD values (brown/orange tones) are prevalent in arid and semi-arid regions including the Sahara Desert, Arabian Peninsula, Gobi Desert, and parts of Australia, the Andes, and the Canadian Rocky Mountains. The legend provides exact values: 0.000, 0.015, 0.030, 0.045, 0.060, 0.075, 0.090, 0.105, and 0.120 m³/m³. The lower panel shows a histogram titled 'histogram'. The x-axis represents the SWI10 T=100 RMSD values, ranging from 0.00 to 0.30. The y-axis represents frequency, ranging from 0 to 35. The distribution is highly skewed towards lower RMSD values, with the highest frequency (approximately 31) occurring at values close to 0.00. The frequency rapidly decreases as the RMSD values increase, becoming negligible beyond 0.25.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-06a3327f21eca45f847eec4722fed715.png)

Fig. 20: RMSD between GLDAS Layer 3 (0.4 - 1m) and SWI10 T=100 (top) and histogram of RMSD (bottom)

## 4.2 COMPARISON TO INSITU DATA

The underlying ASCAT SSM product, as well as the SWI filter, has been extensively validated in the literature. Paulik et al. (2014) compared the SWIV2 product to data from 664 in situ stations using data from the ISMN and found mean R and RMSD values of 0.54 and 0.062 m³/m³ respectively. Brocca et al. (2011) compared AMSR-E and ASCAT derived SWI filtered soil moisture to 17 in situ stations across Europe and found a mean R value of 0.82 for the SWI filtered products. A similar comparison study was done by Griesfeller et al. (2015) over six in situ stations in Norway which found mean R values of 0.72 and 0.68 for ASCAT SWI descending and ascending passes respectively.

Soil moisture data from the ISMN was used to validate the SWIV3 and SWI10 products. As with the comparison to the GLDAS model, different variants of the SWIV3, the SWIV2 and SWI10 were compared to the ISMN data. The results of these comparisons are presented in the next sections.

The maps only show the parts of the Earth were data from in situ stations was available during the validation period. The results are very similar to those shown in Section 4.1.

### 4.2.1 SWIV2-insitu compared to SWIV3-insitu

In this section, the results of the validation of SWIV3 and in situ data are compared to the results obtained by validating SWIV2 with in situ data. Fig. 21 and Fig. 22 show Pearson’s correlation. Only small differences between the dataset can be observed which are not statistically significant. Also the RSMD results in Fig. 23 and Fig. 24 show very little differences.

![This multi-panel figure displays the performance and comparison of Soil Water Index (SWI) product versions, specifically SWI Version 3 (V3) and SWI Version 2 (V2), with GLDAS Layer 1 (0-0.1m soil depth) for a time constant (T) of 1. The top-left panel, 'SWI V3 Metop A and B', shows Pearson's R correlation coefficients for SWI V3 (derived from Metop A and B satellites) across various locations primarily in North America and parts of Europe. The colour scale ranges from -1.0 (dark red) to 1.0 (dark blue), with 0.0 (white). Most data points in North America and Europe exhibit positive correlations, largely above 0.4, with many in the 0.8 to 1.0 range (dark blue). Some points in the northwestern USA/Canada show negative correlations (red/orange). The top-right panel, 'SWI V2 Metop B', presents Pearson's R correlation coefficients for SWI V2 (derived from Metop B satellite) for the same regions, using the identical colour scale. The spatial pattern is highly similar to SWI V3, with most points showing positive correlations, predominantly above 0.4, and many exceeding 0.8. Negative correlations (red/orange) are visible in similar western North American locations. The bottom-left panel, 'SWI V3 - SWI V2', illustrates the differences in Pearson's R between SWI V3 and SWI V2. The colour scale ranges from -0.045 (dark red) to 0.045 (dark blue), with 0.000 (white). Many points in the central and eastern USA show positive differences (shades of blue), indicating SWI V3 has a slightly higher correlation. Conversely, some points in the western USA and parts of Europe display negative differences (shades of red/orange), suggesting SWI V2 has a marginally higher correlation. Most differences are within ±0.045. The bottom-right panel is a 'cumulative histogram of differences', showing the cumulative frequency distribution of the differences between SWI V3 and SWI V2. The Y-axis ranges from 0.0 to 1.0 (cumulative frequency), and the X-axis ranges from -0.3 to 0.3 (difference values). The green-filled curve rises from near 0.0 at X=-0.3, crosses the 0.5 cumulative frequency mark close to X=0.0, and reaches 1.0 cumulative frequency at approximately X=0.2. This indicates that most differences are centred around zero, with a slight positive bias for SWI V3.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-b943e89756f92db2a027048c9d896d07.png)

Fig. 21: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

![This composite chart displays Pearson's correlation coefficient (R) for the Soil Water Index (SWI) at a T=20 smoothing period for different product versions and their differences, alongside a cumulative histogram of these differences. All correlations are shown for points where the p-value is less than 0.1. The top-left chart, titled 'SWI V3 Metop A and B', is a spatial scatter plot showing Pearson's R values across North America and parts of Europe. The color scale ranges from -1.0 (dark red) to 1.0 (dark blue) with 0.2 increments, where red indicates negative correlation and blue indicates positive correlation. Many points in the central and eastern United States show high positive correlation (dark blue, 0.8 to 1.0), while some points in western North America and Europe show lower or negative correlations. The top-right chart, titled 'SWI V2 Metop B', is a similar spatial scatter plot for Pearson's R values across the same geographic regions. It uses the same color scale (-1.0 to 1.0). The pattern of correlations is largely consistent with SWI V3, showing high positive correlations over the central and eastern USA. The bottom-left chart, titled 'SWI V3 - SWI V2', is a spatial scatter plot illustrating the difference in Pearson's R values between SWI V3 and SWI V2. The color scale for differences ranges from -0.100 (dark red) to 0.100 (dark blue) with 0.025 increments. Dark blue points indicate SWI V3 has a higher R, while dark red indicates SWI V2 has a higher R. The differences are generally small, with many points showing slight positive differences (light blue). The bottom-right chart is a 'cumulative histogram of differences', representing the statistical distribution of the Pearson's R differences (SWI V3 - SWI V2). The X-axis spans from -1.0 to 1.5, representing the difference values, and the Y-axis ranges from 0.0 to 1.2, representing the cumulative frequency. The histogram shows that the cumulative frequency rises steeply, passing 0.5 just below 0.0 and reaching approximately 1.0 by an X-axis value of 0.3. This indicates that most differences are positive, suggesting SWI V3 generally exhibits slightly higher Pearson's R values than SWI V2, and almost all differences fall within approximately -0.1 to 0.3.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-b4b290ee87d02976c4b64e917313d4d1.png)

Fig. 22: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

![This figure presents a comparative analysis of Root Mean Square Difference (RMSD) for Soil Water Index (SWI) products at a characteristic time length T=1, measured in cubic meters per cubic meter (m³/m³) of volumetric soil moisture content. It comprises three geographic point maps showing RMSD values and one cumulative histogram of their differences. The RMSD values represent the comparison against GLDAS Layer 1 (0 – 0.1m) data, as indicated by the surrounding document context. The top-left map, titled 'SWI V3 Metop A and B', displays RMSD values for SWI Version 3, derived from Metop A and B satellites, across North America, parts of Europe, and North Africa. The colour scale ranges from 0.04 (dark brown) to 0.13 (dark blue), where brown tones (0.04–0.06) indicate lower RMSD, yellow/orange tones (0.07–0.09) moderate RMSD, and blue tones (0.10–0.13) higher RMSD. Higher RMSD values are frequently observed in the central and western United States. The top-right map, titled 'SWI V2 Metop B', shows RMSD values for SWI Version 2, derived from Metop B satellite, over the same geographic regions, utilizing the identical colour scale (0.04 to 0.13). The spatial pattern of RMSD values is largely similar to the SWI V3 map. The bottom-left map, titled 'SWI V3 - SWI V2', illustrates the differences in RMSD between SWI V3 and SWI V2. The colour scale for these differences ranges from -0.006 (dark brown, indicating SWI V2 RMSD is higher) to 0.006 (dark blue, indicating SWI V3 RMSD is higher), with 0.000 represented by yellow (no difference). Small positive differences (blue tones) are visible in some areas, such as the eastern USA, implying slightly higher RMSD for SWI V3. Small negative differences (brown tones) are scattered across other regions like the western USA and parts of Europe. The bottom-right plot is a 'cumulative histogram of differences'. Its X-axis spans from -0.04 to 0.10, representing the differences in RMSD (m³/m³). The Y-axis shows the cumulative frequency, ranging from 0.0 to 1.2. The histogram indicates that the vast majority of differences between SWI V3 and SWI V2 RMSD are positive and concentrated between 0.00 and 0.02. The cumulative frequency reaches 1.0 (100%) at approximately 0.08, suggesting that SWI V3 generally exhibits slightly higher RMSD values compared to SWI V2.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-3500ba400288eb622d09ca5ee61e17c0.png)

Fig. 23: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

![This image displays a comparison of Soil Water Index (SWI) product versions, specifically SWI Version 3 (V3) Metop A and B, and SWI Version 2 (V2) Metop B, using Root Mean Square Difference (RMSD) for a characteristic time (T) of 20. The RMSD values are in cubic metres per cubic metre (m³/m³). The image is composed of three geographic maps and one cumulative histogram: 1. \*\*Top Left Map: SWI V3 Metop A and B\*\* \* Shows the geographical distribution of SWI V3 Metop A and B RMSD values. \* Data points are primarily concentrated across the continental United States and southern Canada, with sparse points in Europe. \* The colour scale ranges from 0.04 m³/m³ (dark orange) to 0.13 m³/m³ (dark blue), with intermediate values 0.05, 0.06, 0.07 (yellow), 0.08, 0.09, 0.10, 0.11, 0.12 (light blue). 2. \*\*Top Right Map: SWI V2 Metop B\*\* \* Shows the geographical distribution of SWI V2 Metop B RMSD values. \* Data points are distributed across the same regions as SWI V3. \* The colour scale is identical to the SWI V3 map, ranging from 0.04 m³/m³ (dark orange) to 0.13 m³/m³ (dark blue). 3. \*\*Bottom Left Map: SWI V3 - SWI V2\*\* \* Displays the geographical distribution of the differences in RMSD between SWI V3 and SWI V2 (SWI V3 RMSD minus SWI V2 RMSD). \* Differences are shown as coloured points over North America and parts of Europe. \* The colour scale ranges from -0.012 m³/m³ (dark orange, indicating SWI V2 RMSD is higher) to 0.012 m³/m³ (dark blue, indicating SWI V3 RMSD is higher), with 0.000 m³/m³ (light yellow/white) indicating no difference. Intermediate values include -0.009, -0.006, -0.003 (yellow), 0.003, 0.006, 0.009. 4. \*\*Bottom Right Chart: Cumulative Histogram of Differences\*\* \* A cumulative histogram showing the statistical distribution of the differences in RMSD between SWI V3 and SWI V2. \* The X-axis represents the differences in m³/m³, ranging from approximately -0.10 to 0.15. \* The Y-axis represents the cumulative frequency, ranging from 0.0 to 1.2. \* The curve shows that approximately 20% of the differences are negative (SWI V2 RMSD is lower), while the majority (around 80%) are positive or near zero, with the cumulative frequency reaching 1.0 around a difference of 0.12 m³/m³. Overall, the image illustrates a quantitative comparison between two versions of the Soil Water Index product, highlighting regional RMSD values and the statistical distribution of their differences, particularly over North America and parts of Europe.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-f240c5a9929c59af9b0f2c1e2e94e9c3.png)

Fig. 24: Maps of RMSD for SWIV3 calculated with Metop A and B and SWIV2 calculated using Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

### 4.2.2 SWIV3-insitu compared to SWIV3_B-insitu

Also the results of the comparisons of SWIV3 with and without data from Metop-A (SWIV3_B) to in situ data are very similar to those described in Section 4.1.2. Fig. 25 to Fig. 30 show again that the benefit of having two sensors does not show itself in the validation period. There seems to be a small benefit for T=1 in both R and RMSD but the statistical significance of these results is not strong.

![This figure presents a composite of three maps displaying Pearson's R correlation coefficients at in-situ station locations, and one cumulative histogram of correlation differences, all related to the Soil Water Index (SWI) with a T parameter of 1. The top-left map, titled 'Metop A and B', shows the Pearson's R correlation of SWI T=1 values derived from combined Metop A and B satellite data. The map covers North America (USA, Canada, Mexico) and parts of Europe and Africa. Circular markers represent in-situ stations, colored according to a scale ranging from -1.0 (dark red, strong negative correlation) to 1.0 (dark blue, strong positive correlation), with increments of 0.2. Most stations in the continental USA, Canada, and Europe show positive correlations, primarily in the 0.6 to 1.0 range (blue tones). Some stations in the western and southwestern USA and Mexico show lower or negative correlations (orange/red tones, e.g., -0.2 to 0.2). The top-right map, titled 'Metop B', shows the Pearson's R correlation of SWI T=1 values derived from Metop B satellite data alone, using the same geographic coverage and color scale as the 'Metop A and B' map. The spatial pattern of correlations is largely similar to the combined Metop A and B data, with predominantly high positive correlations across North America and Europe. The bottom-left map, titled 'Metop A and B - Metop B', displays the differences in Pearson's R correlation coefficients between the combined Metop A and B data and the Metop B data. The color scale for differences ranges from -0.045 (dark red, negative difference) to 0.045 (dark blue, positive difference), with increments of 0.015. Most station points are colored white, light blue, or light orange, indicating differences close to 0.000 (no difference) or small positive/negative differences (up to ±0.015). Some areas in the central USA show slightly larger positive differences (light blue, up to 0.030). The bottom-right plot is a 'cumulative histogram of differences'. The x-axis represents the differences in Pearson's R values, ranging from -0.15 to 0.20. The y-axis represents the cumulative frequency, from 0.0 to 1.2. The green shaded area shows the cumulative distribution, indicating that the majority of differences are concentrated between approximately -0.05 and 0.10. The cumulative frequency reaches 1.0 (100%) at an x-value of approximately 0.15, suggesting that positive differences are more common than negative ones.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-1871924316eef90c76fcc4f95b9280d4.png)

Fig. 25: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

![This figure presents a multi-panel display evaluating the Soil Water Index (SWI) with a characteristic time T=20 using Pearson's R correlation coefficient against in-situ station data. The maps focus on in-situ station locations primarily in North America, with additional stations in Europe and North Africa. The top-left map, titled 'Metop A and B', shows Pearson's R values when using data from both Metop A and Metop B satellites. The correlation values range from -1.0 (dark red) to 1.0 (dark blue), with 0.0 indicated by white. Most stations in the central and eastern United States, as well as European stations, show positive correlation (blue points, 0.2 to 1.0). Stations in western North America show mixed or negative correlations (red points, -0.2 to -1.0). The top-right map, titled 'Metop B', displays Pearson's R values when using data from only the Metop B satellite, using the same colour scale of -1.0 to 1.0. The spatial pattern of correlation is largely similar to the 'Metop A and B' map, with positive correlations dominant in the central/eastern United States and Europe. The bottom-left map, titled 'Metop A and B - Metop B', illustrates the difference in Pearson's R values between the combined Metop A and B data and the Metop B-only data. This map uses a more sensitive colour scale ranging from -0.04 (dark red) to 0.04 (dark blue), with 0.00 indicated by white. Positive differences (blue points, 0.01 to 0.04) are observed where Metop A and B combined yielded higher correlation, notably in parts of the central and eastern United States. Negative differences (red points, -0.01 to -0.04) are seen in western North America and some scattered locations, indicating Metop B-only data had slightly higher correlation there. Overall, the differences are small, generally within ±0.04. The bottom-right panel displays a 'cumulative histogram of differences'. The x-axis represents the differences in Pearson's R values (likely corresponding to 'Metop A and B - Metop B') ranging from -0.3 to 0.3. The y-axis shows the cumulative frequency from 0.0 to 1.0. The histogram, filled in green, shows a steep rise around 0.0 on the x-axis, indicating that the majority of differences are very close to zero. Approximately 50% of the differences are less than 0.01, and nearly all differences fall between -0.1 and 0.2.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-002c253c6fd99126ad7d656998968a27.png)

Fig. 26: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

![The image displays three geographic maps and one cumulative histogram, illustrating the validation of the Soil Water Index (SWI) with a characteristic time length (T) of 100, using Pearson's correlation coefficient (R) compared to in-situ data, primarily across North America with scattered points in Europe, Africa, South America, and Australia. These locations correspond to available in-situ stations from the International Soil Moisture Network (ISMN). The top left map, titled 'Metop A and B', shows Pearson's R values for SWI T=100 derived from combined Metop A and Metop B satellite data. The colour scale ranges from dark red (-1.0) through white (0.0) to dark blue (1.0), indicating negative, no, and positive correlation, respectively. Most points in the central and eastern United States show positive correlations (blue tones, typically 0.6 to 1.0). The top right map, titled 'Metop B', shows Pearson's R values for SWI T=100 derived solely from Metop B satellite data, using the same colour scale. The spatial pattern of correlations is very similar to the 'Metop A and B' map, with strong positive correlations in the central and eastern United States. The bottom left map, titled 'Metop A and B - Metop B', illustrates the difference in Pearson's R values between the combined Metop A and B product and the Metop B-only product. The colour scale for differences ranges from dark red (-0.04) through white (0.00) to dark blue (0.04). Red tones indicate Metop B has higher R, while blue tones indicate Metop A and B has higher R. The differences are generally small, mostly within ±0.01 to ±0.02, with a slight prevalence of positive differences (blue tones) in the central United States, suggesting marginally higher correlations when using combined Metop A and B data in those areas. The bottom right chart is a 'cumulative histogram of differences'. The x-axis represents the differences in Pearson's R, ranging from approximately -0.3 to 0.3. The y-axis represents the cumulative proportion, from 0.0 to 1.0. The histogram shows that the majority of differences are tightly clustered around 0.0, with approximately 50% of the differences centered at zero, and over 95% of the differences falling within the range of -0.1 to 0.1. This indicates a high level of consistency between the Metop A and B and Metop B products.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-dd5fe12e1d5421d96c8c122b5874530e.png)

Fig. 27: Maps of Pearson’s correlation coefficient with a p value \< 0.01 for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=100.

![This image displays three choropleth maps showing the spatial distribution of Soil Water Index (SWI) Root Mean Square Difference (RMSD) at T=1 in m³/m³, along with a cumulative histogram of the differences between two Metop data combinations. The geographic areas covered by the in situ validation stations are primarily North America (mainly the United States) and parts of Western Europe and North Africa. The top-left map, titled 'Metop A and B', shows RMSD values for the combined Metop A and Metop B dataset. Its colour scale ranges from dark brown (0.04 m³/m³) to dark blue (0.13 m³/m³). Most stations in the central and eastern United States show RMSD values between 0.06 and 0.09 m³/m³ (orange to light yellow), with some western US and European stations showing values from 0.04 m³/m³ (dark brown) to 0.13 m³/m³ (dark blue). The top-right map, titled 'Metop B', shows RMSD values for the Metop B dataset alone, using the same colour scale (0.04 m³/m³ to 0.13 m³/m³). The spatial distribution of RMSD values is visually similar to the 'Metop A and B' map. The bottom-left map, titled 'Metop A and B - Metop B', illustrates the difference in RMSD values between the combined Metop A and B dataset and the Metop B dataset alone. Its diverging colour scale ranges from dark brown (-0.0060 m³/m³) through white (0.0000 m³/m³) to dark blue (0.0060 m³/m³). Most stations show differences close to zero, represented by light yellow (0.0015 m³/m³), white (0.0000 m³/m³), and light orange (-0.0015 m³/m³), indicating minor variations between the two datasets. The bottom-right chart is a cumulative histogram titled 'cumulative histogram of differences'. The X-axis represents the differences in RMSD, ranging from -0.05 to 0.03. The Y-axis represents cumulative frequency from 0.0 to 1.0. The histogram shows that the majority of differences are concentrated very near 0.00, with over 90% of the differences falling between approximately -0.01 and +0.02. This indicates that the RMSD performance of Metop B alone is very similar to the combined Metop A and B product.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-5e101c30ed3b0681df5379e546c8ce7b.png)

Fig. 28: Maps of RMSD for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=1.

![This figure presents three choropleth maps showing the geographic distribution of Soil Water Index (SWI) T=20 Root Mean Square Difference (RMSD) in m³/m³ and their differences, alongside a cumulative histogram of these differences. The validation data comes from in situ stations, primarily concentrated in North America (United States) and parts of Europe, with scattered points globally. The top left map, titled 'Metop A and B', displays the SWI T=20 RMSD values for combined Metop A and B satellite data. The colour scale ranges from 0.04 m³/m³ (dark brown) to 0.13 m³/m³ (dark blue), with intermediate values of 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, and 0.12 m³/m³. The top right map, titled 'Metop B', shows the SWI T=20 RMSD values for Metop B satellite data, using the identical colour scale and legend as the 'Metop A and B' map. The bottom left map, titled 'Metop A and B - Metop B', illustrates the difference in SWI T=20 RMSD between the combined Metop A and B data and the Metop B data alone. The colour scale for differences ranges from -0.0045 m³/m³ (dark brown, indicating Metop B had lower RMSD) to 0.0045 m³/m³ (dark blue, indicating Metop A and B combined had higher RMSD), with increments of 0.0015 and a central value of 0.0000 m³/m³ (light yellow/green, indicating no difference). Most data points on this map show very small differences, predominantly near 0.0000 m³/m³. The bottom right panel displays a cumulative histogram of these differences. The X-axis represents the differences, ranging from approximately -0.06 to 0.10. The Y-axis represents the cumulative frequency, ranging from 0.0 to 1.2. The green-filled histogram shows that the vast majority of differences are clustered tightly around 0.00, with the cumulative frequency reaching 1.0 (100%) by approximately 0.02. This indicates that the RMSD values from Metop A and B combined are very similar to those from Metop B alone.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-d79226f4f66566d9db08071ab1b1bd73.png)

Fig. 29: Maps of RMSD for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=20.

![This figure presents three choropleth maps and one cumulative histogram related to the Root Mean Square Difference (RMSD) of the Soil Water Index (SWI) at T=100, measured in m³/m³. The maps display point data across North America (primarily the United States) and parts of Europe and North Africa. The top-left map, titled 'Metop A and B', shows SWI T=100 RMSD values ranging from 0.045 (dark orange) to 0.150 (dark blue). Values are grouped into 7 classes: 0.045, 0.060, 0.075, 0.090, 0.105, 0.120, 0.135, and 0.150 m³/m³. The top-right map, titled 'Metop B', also displays SWI T=100 RMSD values using the same colour scale and range as the 'Metop A and B' map. Both maps show similar spatial distributions of RMSD values, with a mix of lower and higher values across the sampled stations. The bottom-left map, titled 'Metop A and B - Metop B', illustrates the differences in SWI T=100 RMSD values between the two Metop datasets. The colour scale for differences ranges from -0.0060 (dark brown) to 0.0060 (dark blue), with classes at -0.0060, -0.0045, -0.0030, -0.0015, 0.0000, 0.0015, 0.0030, 0.0045, and 0.0060 m³/m³. The map primarily shows colours around 0.0000 (yellowish tones), indicating very small differences between the two datasets across most stations. The lower-right plot is a 'cumulative histogram of differences'. The X-axis represents the differences, ranging from approximately -0.06 to 0.08. The Y-axis represents cumulative frequency, from 0.0 to 1.0. The histogram shows that approximately 95% of the differences are clustered between -0.01 and 0.02, confirming that the two Metop datasets yield very similar RMSD results, with most differences close to zero.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-3bf0c643a536d5b80d7ed00e398d3ba7.png)

Fig. 30: Maps of RMSD for SWIV3 calculated with Metop A and B and only Metop B data as well as the difference between them. The lower right plot shows a cumulative histogram of these differences. All plots for T=100.

### 4.2.3 Time series of selected in situ stations

Four in situ stations were selected to be discussed in more detail. They were selected basically at random but care was taken that bad and good results are shown and that different climate zones are represented. The four selected stations and their climate zones are listed in Table 7. For all in situ data the first layer, measured at a depth of 0.05m, is shown. For these plots SWI with T=1 and 100 is shown.

Table 7: Station details and climate classification

[TABLE]

![Scatter plot showing the temporal evolution of soil moisture for different Soil Water Index (SWI) variants and in situ measurements at the USCRN station Edinburg-17-NNE from June 2013 to April 2014. The Y-axis represents soil moisture in cubic metres per cubic metre \[m³/m³\], ranging from 0.05 to 0.35. The X-axis represents time, from June 2013 to April 2014. Five data series are plotted: \* \*\*SWIV3 T=1\*\* (red dots) \* \*\*SWIV3 T=100\*\* (light blue dots) \* \*\*SWIV2 T=1\*\* (purple dots) \* \*\*SWIV2 T=100\*\* (grey dots) \* \*\*in situ\*\* (black dots) All series show a general decrease in soil moisture from June 2013, reaching a minimum around late August to mid-September 2013, followed by an increase until late 2013, a data gap (late December 2013 to March 2014), and a subsequent increase in April 2014. The 'in situ' data starts at approximately 0.33 m³/m³ in June 2013, decreases to a minimum of about 0.06 m³/m³ in early September 2013, then increases to around 0.22 m³/m³ by December 2013. After the data gap, it rises from approximately 0.23 m³/m³ to 0.26 m³/m³ in April 2014. SWIV3 T=1 generally tracks the 'in situ' data well, particularly during the drying phase and the initial wetting phase in autumn 2013, reaching similar minimum values. SWIV2 T=1 also shows a similar trend to 'in situ' data, starting around 0.20 m³/m³ and peaking higher around 0.29 m³/m³ in late October/early November 2013. In contrast, SWIV3 T=100 consistently shows lower soil moisture values than the 'in situ' data, especially in April 2014, where its values are around 0.08–0.12 m³/m³ while 'in situ' is above 0.23 m³/m³. SWIV2 T=100 also shows lower values than 'in situ' during the drying phase but aligns more closely in April 2014.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-e6adf8608e26fd3fae392e50470d8513.png)

Fig. 31: Different SWI variants and in situ data for SNOTEL station CRAB CREEK.

The SWI time series at CRAB CREEK shown in Fig. 31 shows fair agreement with the in situ data. R between SWIV3 T=1 and in situ is 0.67 with a RMSD of 0.063 m³/m³. Wetting events in summer 2013 are generally reflected well in the SWI data but during autumn signals of different magnitude and sometimes even direction are shown. Reasons for that could be lacking spatial representativeness. No data is present during the winter period from November until April. The after winter peak in SWIV2 is due to slightly different freeze/thaw masking of SWIV2 and SWIV3.

![This is a scatter chart displaying soil moisture time series for different Soil Water Index (SWI) variants and in situ measurements at the SNOTEL station CRAB CREEK, spanning from May 2013 to April 2014. The Y-axis represents soil moisture in \[m³/m³\], ranging from 0.05 to 0.30. The X-axis represents time, marked by months (May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, Jan 2014, Feb, Mar, Apr). Five data series are plotted: 1. \*\*SWIV3 T=1\*\* (red dots): Shows moderate fluctuations, generally tracking the in situ data but often with lower magnitude. Values range approximately from 0.05 to 0.25 m³/m³. 2. \*\*SWIV3 T=100\*\* (blue dots): Displays a smoother, higher soil moisture trend, rising from approximately 0.08 m³/m³ in August 2013 to stable values around 0.25-0.27 m³/m³ from February to April 2014. 3. \*\*SWIV2 T=1\*\* (purple dots): Shows fluctuations similar to SWIV3 T=1, generally higher in value than SWIV3 T=1, and includes an 'after winter peak' around January-February 2014. 4. \*\*SWIV2 T=100\*\* (grey dots): Similar to SWIV3 T=100, but slightly lower in value from October 2013 onwards, maintaining levels around 0.22-0.25 m³/m³. 5. \*\*in situ\*\* (black dots): Shows the most volatile pattern with sharp peaks and troughs, reflecting summer 2013 wetting events. In situ data points are visible throughout the entire period shown, including winter months (November 2013 to April 2014), contrary to a claim in the surrounding text. Overall, the SWIV3 T=1 series shows fair agreement with the in situ data, with a correlation coefficient (R) of 0.67 and a Root Mean Square Difference (RMSD) of 0.063 m³/m³. Wetting events in summer 2013 are generally well-reflected by SWI data, while autumn 2013 shows signals of different magnitude and sometimes direction across the variants. The SWI T=100 variants (SWIV3 T=100 and SWIV2 T=100) exhibit significantly less variability and maintain generally higher soil moisture values during the winter period compared to the T=1 variants and in situ data.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-bb673a7272e392ad6e8e51893fd519f7.png)

Fig. 32: Different SWI variants and in situ data for USCRN station Edinburg-17-NNE.

The SWI T=1 time series shown in Fig. 32 show good agreement with the in situ data. R between SWIV3 T=1 and in situ data is 0.64 with a RMSD of 0.036 m³/m³. Soil moisture conditions of the whole year are well represented in the SWI data.

![Scatter plot comparing different Soil Water Index (SWI) variants (SWIV3 T=1, SWIV3 T=100, SWIV2 T=1, SWIV2 T=100) with in situ soil moisture data for the USCRN station Edinburg-17-NNE from June 2013 to April 2014. The Y-axis represents 'soil moisture \[m³/m³\]' ranging from 0.00 to 0.16. The X-axis represents time, marked at 'Jun 2013', 'Aug 2013', 'Oct 2013', 'Dec 2013', 'Feb 2014', and 'Apr 2014'. Five data series are plotted: 'SWIV3 T=1' (red dots), 'SWIV3 T=100' (blue dots), 'SWIV2 T=1' (purple dots), 'SWIV2 T=100' (grey dots), and 'in situ' (black dots). The 'in situ' data exhibits high variability and includes periods of no data, notably from mid-November 2013 through late March 2014, and generally low values (0.00-0.04 m³/m³) in early summer 2013. Peaks in 'in situ' data reach approximately 0.15 m³/m³ in early July 2013 and over 0.12 m³/m³ in February 2014. The SWI variants with T=1 (SWIV3 T=1 and SWIV2 T=1) generally follow the short-term fluctuations of the 'in situ' data more closely than the T=100 variants. During summer 2013 (June-August), SWI variants, especially SWIV3 T=1 and SWIV2 T=1, show higher soil moisture values (0.08-0.15 m³/m³) compared to the low 'in situ' readings. From late 2013 into early 2014, the SWI variants show continuous data, filling the gaps present in the 'in situ' measurements. Around March-April 2014, SWIV2 variants (purple and grey) show higher soil moisture values (up to 0.10 m³/m³) compared to SWIV3 variants (red and blue), which are lower, with SWIV3 T=100 dropping to near zero.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-bad6f6a35e6f6f138a80db528efbc634.png)

Fig. 33: Different SWI variants and in situ data for SCAN station Pine Nut.

Fig. 33 shows a special case. In this area negative correlations are observed between in situ soil moisture data and the SWI products. This is because of unexpected backscatter behavior of the ASCAT instrument in some areas. Hahn et al. (2013) attributed this behavior to volume scattering in very dry conditions that reverse the expected radar response to soil wetting. R of SWIV3 T=1 and in situ data is -0.66 whereas RMSD is 0.071 m³/m³.

![This scatter plot displays time series of soil moisture values in m³/m³ for different Soil Water Index (SWI) variants and in situ data, spanning from June 2013 to April 2014 at the SNOTEL station CRAB CREEK. The Y-axis represents soil moisture from 0.00 to 0.35 m³/m³, and the X-axis represents time. Five data series are plotted: SWIV3 T=1 (red dots), SWIV3 T=100 (blue dots), SWIV2 T=1 (purple dots), SWIV2 T=100 (grey dots), and in situ (black dots). The in situ data shows significant fluctuations, peaking around 0.32 m³/m³ in early July 2013 and early September 2013, then declining and showing a data gap from late November 2013 to mid-January 2014, resuming at lower values around 0.20 m³/m³ and dropping to near 0.00 m³/m³ by April 2014. The SWIV3 T=1 and SWIV2 T=1 series generally track the short-term fluctuations of the in situ data but often at lower magnitudes, with both showing gaps similar to the in situ data. The SWIV3 T=100 and SWIV2 T=100 series show smoother trends, increasing from around 0.05 m³/m³ in June 2013 to peak around 0.34 m³/m³ in late January 2014 (SWIV3 T=100) or early February 2014 (SWIV2 T=100), then declining. A noticeable 'after winter peak' for SWIV2 variants is visible in late January/early February 2014, surpassing SWIV3 values.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-4c411663ba026b4069d5cd5ee02792b1.png)

Fig. 34: Different SWI variants and in situ data for TERENO station Selhausen.

Correlation between SWIV3 T=1 and in situ for station Selhausen is 0.53 with a RMSD of 0.045 m³/m³. Fig. 34 shows that wetting and drying is well represented but also that during summer either a dry or a wet bias is observed. This time series also show the effect that different initial conditions can have on SWI with T=100. In this case the difference between the time series is exaggerated by the applied minimum-maximum scaling.

#### 4.2.3.1 Comparison of in situ data and SWI10

The SWI10 data generally shows correlations that are in line with what one would expect based on the R values achieved by the SWIV3 product (Fig. 35 to Fig. 37). RMSD for the comparison with in situ data (Fig. 38 to Fig. 40) is in the same range as the comparison with GLDAS showed.

![This image displays the spatial distribution of Soil Water Index (SWI) T=1 Pearson's R correlation coefficients at various in-situ station locations, accompanied by a histogram of these correlation values. The upper panel shows a world map with country outlines across North America, Europe, and Africa. Data points, representing in-situ station locations, are concentrated across the continental United States, Alaska, and a few locations in Europe (e.g., France, Germany). Each point is colour-coded according to its Pearson's R value, using a legend bar ranging from dark blue (1.0) through white (0.0) to dark red (-1.0). Most data points in the continental USA and Europe indicate positive Pearson's R values, predominantly ranging from 0.4 to 0.8 (shades of blue), signifying positive agreement between the SWI T=1 product and in-situ data. A smaller number of stations, particularly in the western and eastern USA and Alaska, show negative or near-zero correlations (red to light blue). The lower panel presents a histogram of all the Pearson's R values shown on the map. The x-axis ranges from -1.0 to 1.0, representing the Pearson's R value, and the y-axis indicates frequency, ranging from 0.0 to 2.5. The histogram displays a bimodal distribution: a smaller cluster of negative correlations is visible between approximately -0.7 and -0.4, with frequencies up to 0.4; and a much larger cluster of positive correlations is present between 0.3 and 0.9, with frequencies generally between 1.0 and 2.5, peaking around 0.4-0.5 and 0.6-0.8. This indicates that most monitored sites show a strong positive correlation between the SWI T=1 time series and in-situ soil moisture measurements.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-dd4e0cb1605a76990156730dd02ff89d.png)

Fig. 35: Map and histogram of Pearson’s R (p \< 0.1) between in situ data and SWI10 of for T=1

![This image consists of two main components: a map showing the spatial distribution of Pearson's R correlation coefficients for Soil Water Index (SWI10 T=20) against in-situ data, and a histogram displaying the frequency distribution of these correlation values. The map covers North America (primarily the continental United States and Alaska) and outlines of Europe, Africa, and the Middle East. Each coloured dot on the map represents a measurement station. The colour scale for Pearson's R ranges from -1.0 (dark red, strong negative correlation) to 1.0 (dark blue, strong positive correlation), with 0.0 represented by white. Most stations in the continental United States show strong positive correlation, with values predominantly between 0.4 and 1.0 (light blue to dark blue). Negative or lower positive correlations (red and orange dots) are scattered in Alaska, parts of eastern Canada, and some regions within the central and eastern US. A single blue dot, indicating positive correlation, is visible in Western Europe (Belgium/Netherlands region). The embedded histogram displays the frequency distribution of the Pearson's R values across all stations. The X-axis spans from -1.0 to 1.0, representing the Pearson's R correlation coefficient. The Y-axis represents frequency, ranging from 0.0 to 2.5. The distribution is bimodal: a dominant cluster of values is concentrated between approximately 0.2 and 1.0, with the highest frequency observed between 0.7 and 0.8. A smaller cluster of values appears between -1.0 and -0.3, peaking around -0.4 to -0.6. There is a distinct gap in frequencies for R values between approximately -0.2 and 0.2. This indicates that most measurement stations exhibit either moderate to strong positive correlation or moderate negative correlation between the SWI10 T=20 product and in-situ data.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-355de81949ec49a28133f4eafc54cf2a.png)

Fig. 36: Map and histogram of Pearson’s R (p \< 0.1) between in situ data and SWI10 of for T=20

![This image displays two plots: a choropleth map illustrating the spatial distribution of Soil Water Index (SWI10) T=100 Pearson's R correlation coefficients, and a histogram showing the frequency distribution of these values. The map covers North America (primarily the continental United States and parts of Canada and Mexico) and outlines of Europe and North Africa. Coloured dots represent in-situ station locations where SWI10 T=100 data was correlated. The colour scale ranges from dark red (-1.0 to -0.8), through orange and light blue, to dark blue (0.8 to 1.0). A vertical colour bar legend indicates Pearson's R values: 1.0, 0.8, 0.6, 0.4, 0.2, 0.0, -0.2, -0.4, -0.6, -0.8, -1.0. Most stations, particularly in the central and eastern United States, show positive correlations (blue hues, 0.2 to 1.0). Stations in Alaska, western Canada, and parts of the western United States show lower or negative correlations (red/orange hues, -1.0 to 0.0). A single blue data point is visible in Western Europe. The accompanying histogram shows the frequency or density of these Pearson's R values. The X-axis spans from -1.0 to 1.0, representing the Pearson's R coefficient. The Y-axis ranges from 0.0 to 2.5 (unlabeled, implies frequency or density). The distribution is bimodal, with a smaller cluster of values approximately between -0.7 and -0.2, and a larger, more prominent cluster of positive correlations ranging from approximately 0.2 to 0.9. The highest frequencies are observed for Pearson's R values between 0.4 and 0.7.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-b61cc19a16f9a33e09d2c2a8c46aeedb.png)

Fig. 37: Map and histogram of Pearson’s R (p \< 0.1) between in situ data and SWI10 of for T=100

![This image displays two plots: a map showing the spatial distribution of Soil Water Index (SWI) T=1 Root Mean Square Difference (RMSD) values, and a histogram of these RMSD values. The upper plot is a choropleth map illustrating SWI10 T=1 RMSD in m³/m³ across North America (primarily the United States and parts of Canada, Mexico, and Caribbean islands) and sparsely in Europe. Individual data points, representing measurement stations, are coloured according to their RMSD value. The colour scale ranges from dark brown (0.030 m³/m³) through yellow (0.075 m³/m³) and light blue to dark blue (0.150 m³/m³). The map shows a concentration of stations across the continental United States, with a few in Alaska and very few in Europe (e.g., Belgium/Netherlands region). Lower RMSD values (brown/yellow) are frequently observed in the western United States, while higher RMSD values (blue) are common in the central and eastern parts of the United States. The lower plot is a histogram showing the frequency distribution of the SWI10 T=1 RMSD values. The x-axis represents the RMSD in m³/m³, ranging from 0.02 to 0.16. The y-axis represents the frequency, ranging from 0 to 20. The histogram shows a varied distribution, with prominent peaks around 0.04-0.05 m³/m³, 0.06-0.07 m³/m³, and a notable peak around 0.09 m³/m³. The highest frequencies are generally for RMSD values below 0.1 m³/m³, and the distribution tapers off towards higher RMSD values.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-c4a562112ce46f5e27599e9779064c48.png)

Fig. 38: Map and histogram of RMDS between in situ data and SWI10 of for T=1

![This image comprises two visualisations: a map showing the geographical distribution of Soil Water Index (SWI) Root Mean Square Deviation (RMSD) values and a histogram illustrating their frequency distribution. The upper panel is a map titled 'SWI10 T=20 RMSD in m³/m³'. It displays the RMSD of SWI, calculated with a characteristic time length (T) of 20, against in situ data at various station locations across North America (primarily the continental United States, with some points in Canada and Mexico) and parts of Europe (including Scandinavia, Benelux, Germany, France, and Spain) and North Africa. The RMSD values are colour-coded according to a vertical legend ranging from 0.030 m³/m³ (dark brown) to 0.150 m³/m³ (dark blue). Intermediate colours include yellow (0.045 to 0.075 m³/m³) and light blue (0.090 to 0.105 m³/m³). The map shows a higher concentration of stations in the Western and Central United States exhibiting higher RMSD values (yellow to dark blue), while stations in the Eastern United States and Europe generally show lower to medium RMSD values (dark brown to light blue). The lower panel is a histogram titled 'histogram' which shows the frequency distribution of the SWI10 T=20 RMSD values plotted on the map. The X-axis ranges from 0.02 to 0.16, representing RMSD in m³/m³. The Y-axis represents the frequency (count) of observations, from 0 to 20. The histogram indicates that the majority of stations have lower RMSD values, with the highest frequency of approximately 19 observations occurring in the bin centered slightly above 0.03 m³/m³. The frequency generally decreases as RMSD values increase, extending to approximately 0.15 m³/m³, although several smaller peaks are present across the distribution.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-fd21733d9121ee79f259fc4af6ee915f.png)

Fig. 39: Map and histogram of RMDS between in situ data and SWI10 of for T=20

![This image displays two plots: a map showing the geographical distribution of Soil Water Index (SWI) T=100 Root Mean Square Deviation (RMSD) values, and a histogram illustrating the frequency distribution of these RMSD values. The upper plot is a world map, primarily focusing on North America, Europe, and parts of Africa. It shows numerous points, predominantly across the continental United States, southern Canada, and Mexico, along with a cluster of points in central Europe (e.g., Belgium, Netherlands, Germany, France, Switzerland, Austria, Czech Republic). Each point represents an in situ station where the SWI10 T=100 RMSD was calculated, expressed in m³/m³. The colour scale ranges from dark brown (0.045 m³/m³) to dark blue (0.150 m³/m³), with intermediate values shown as yellow (0.060 m³/m³), light blue (0.075, 0.090, 0.105, 0.120 m³/m³), and a darker blue (0.135 m³/m³). Lower RMSD values (brown/yellow) indicate better agreement with in situ data and are observed more frequently in the western and parts of the central United States. Higher RMSD values (various shades of blue) are more prevalent in the eastern United States and scattered across other regions. The lower plot is a histogram showing the distribution of these SWI10 T=100 RMSD values. The x-axis represents the RMSD in m³/m³, ranging from 0.04 to 0.16. The y-axis represents the frequency, ranging from 0 to 20. The histogram displays a wide range of RMSD values, with several peaks, notably around 0.045–0.05 m³/m³ and 0.08–0.085 m³/m³. The distribution indicates that a significant number of stations have RMSD values below 0.10 m³/m³.](products_Quality_assessment_report_-_Soil_Water_Index_0.1_version_3-media/img-9a9720d5037fbec492c72266f0d43912.png)

Fig. 40: Map and histogram of RMDS between in situ data and SWI10 of for T=100

# 5 CONCLUSIONS

SWIV3, SWI10 and SSFV3 test datasets were compared to the GLDAS model and to in situ data from the ISMN. The achieved results were put into context by using the currently operational products as a reference, when possible. The results obtained here are very similar to results obtained by published studies. Comparison with modelled data shows good agreement in all regions except arid areas and in northern latitudes. The validation with in situ observations generally shows positive correlations, but there are some stations in arid areas that show non-significant or even negative R values. The results showed that the quality of the product is essentially unchanged between SWIV2 and SWIV3 for a one year validation period. It was also shown that a sensor failure of one satellite would have very little influence on the output product.

During the regular cross cutting validation exercise performed by the Global Land service in assimilating the SWI into a Land Data Assimilation System, it has been observed that the SWIV2 product seemed to dry in the Summer of 2013 over France. The SWIV3 will probably show the same behaviour since the two products are very similar. Investigations into the cause of this behaviour are ongoing but could not be detected here because only one year of SWIV3 test data was available.

In addition, it was shown that the SWI10 product retains the basic characteristics from the SWIV3 input product. Similar spatial distribution of the error metrics was observed although the absolute values for RMSD were higher in some regions. As soon as the full SWI10 archive is available it can be checked if this is a result of the small sample size or a real feature in the dataset.

The validation of SSFV3 revealed unintuitive behaviour in Libya. This will be reported to the H-SAF team responsible for the frozen probabilities included in the SSM input data. So that it can be investigated if SSF should indeed report the frozen state in this situation or if adjustments are necessary.

# 6 REFERENCES

Al-Yaari, A., Wigneron, J.-P., Ducharne, A., Kerr, Y., Wagner, W., De Lannoy, G., Reichle, R., Al Bitar, A., Dorigo, W., & Richaume, P. (2014). Global-scale comparison of passive (SMOS) and active (ASCAT) satellite based microwave soil moisture retrievals with soil moisture simulations (MERRA-Land). *Remote Sensing of Environment*, 152, 614-626

Albergel, C., Dorigo, W., Reichle, R.H., Balsamo, G., de Rosnay, P., Muñoz-Sabater, J., Isaksen, L., de Jeu, R., & Wagner, W. (2013). Skill and Global Trend Analysis of Soil Moisture from Reanalyses and Microwave Remote Sensing. *Journal of Hydrometeorology*, 14, 1259-1277

Brocca, L., Hasenauer, S., Lacava, T., Melone, F., Moramarco, T., Wagner, W., Dorigo, W., Matgen, P., Martínez-Fernández, J., Llorens, P., Latron, J., Martin, C., & Bittelli, M. (2011). Soil moisture estimation through ASCAT and AMSR-E sensors: An intercomparison and validation study across Europe. *Remote Sensing of Environment*, 115, 3390-3408

Chen, Y., Yang, K., Qin, J., Zhao, L., Tang, W., & Han, M. (2013). Evaluation of AMSR-E retrievals and GLDAS simulations against observations of a soil moisture network on the central Tibetan Plateau. *Journal of Geophysical Research: Atmospheres*, 118, 4466-4475

Dorigo, W.A., Scipal, K., Parinussa, R.M., Liu, Y.Y., Wagner, W., de Jeu, R.A.M., & Naeimi, V. (2010). Error characterisation of global active and passive microwave soil moisture datasets. *Hydrol. Earth Syst. Sci.*, 14, 2605-2616

Dorigo, W.A., Xaver, A., Vreugdenhil, M., Gruber, A., Hegyiová, A., Sanchis-Dufau, A.D., Zamojski, D., Cordes, C., Wagner, W., & Drusch, M. (2013). Global Automated Quality Control of In Situ Soil Moisture Data from the International Soil Moisture Network. *Vadose Zone Journal*, 12

Griesfeller, A., Lahoz, W., de Jeu, R., Dorigo, W., Haugen, L., Svendby, T., & Wagner, W. (2015). Evaluation of satellite soil moisture products over Norway using ground-based observations. *International Journal of Applied Earth Observation and Geoinformation*

Hahn, S., Wagner, W., Vreugdenhil, M., Melzer, T., & Abdulrahman, A. (2013). Challenges for soil moisture retrieval from C-band backscatter measurements in arid and semi-arid environments. In, *EUMETSAT Meteorological Satellite Conference*. Vienna

Liu, Y.Y., Parinussa, R.M., Dorigo, W.A., De Jeu, R.A.M., Wagner, W., van Dijk, A.I.J.M., McCabe, M.F., & Evans, J.P. (2011). Developing an improved soil moisture dataset by blending passive and active microwave satellite-based retrievals. *Hydrol. Earth Syst. Sci.*, 15, 425-436

Naeimi, V., Paulik, C., Bartsch, A., Wagner, W., Kidd, R.A., Park, S.-E., Elger, K., & Boike, J. (2012). ASCAT Surface State Flag (SSF): Extracting Information on Surface Freeze/Thaw Conditions From Backscatter Data Using an Empirical Threshold-Analysis Algorithm. *IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING*, 50, 2566-2582

Paulik, C., Dorigo, W., Wagner, W., & Kidd, R. (2014). Validation of the ASCAT Soil Water Index using in situ data from the International Soil Moisture Network. *International Journal of Applied Earth Observation and Geoinformation*, 30, 1-8

Rodell, M., Houser, P.R., Jambor, U., Gottschalck, J., Mitchell, K., Meng, C.J., Arsenault, K., Cosgrove, B., Radakovich, J., Bosilovich, M., Entin\*, J.K., Walker, J.P., Lohmann, D., & Toll, D. (2004). The Global Land Data Assimilation System. *Bulletin of the American Meteorological Society*, 85, 381-394

Wagner, W., Lemoine, G., Rott, H. (1999): A Method for Estimating Soil Moisture from ERS Scatterometer and Soil Data. *Rem. Sens. Environ.* 70: 191-207.

Back to top

## Reuse

EUPL (\>= 1.2)
