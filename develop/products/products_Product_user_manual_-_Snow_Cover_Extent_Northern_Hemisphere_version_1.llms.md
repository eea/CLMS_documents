# PRODUCT USER MANUAL Snow Cover Extent Collection 1 km Northern Hemisphere

Copernicus Global Land Operations ‘Cryosphere and Water’ ‘CGLOPS-2’

This Product User Manual provides essential information for utilising the Northern Hemisphere Snow Cover Extent (SCE) product, a core component of the Copernicus Global Land Service. It details the daily fractional snow cover (FSC) mapping across the Northern Hemisphere at 0.01-degree resolution, derived from S-NPP VIIRS and Sentinel-3 SLSTR optical satellite data. The document outlines the retrieval methodology, which integrates the Normalised Difference Snow Index and the SCAmod algorithm, alongside product characteristics, coding conventions, and validation results, supporting diverse applications in cryosphere monitoring and climate science.

Published

April 17, 2020

Keywords

Snow Cover Extent (SCE), Fractional Snow Cover (FSC), Northern Hemisphere, Sentinel-3 SLSTR data, S-NPP VIIRS data, Normalised Difference Snow Index (NDSI), SCAmod algorithm, Transmissivity map, Product User Manual (PUM), Thematic accuracy assessment, Daily snow products, Cryosphere monitoring

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

|  |  |  |  |
|----|----|----|----|
| Dissemination Level |  |  |  |
| PU | Public | \(X\) |  |
| PP | Restricted to other programme participants (including the Commission Services) |  |  |
| RE | Restricted to a group specified by the consortium (including the Commission Services) |  |  |
| CO | Confidential, only for members of the consortium (including the Commission Services) |  | X |

## 0.1 Document Release Sheet

[TABLE]

## 0.2 Change Record

| Issue/Rev | Date | Page(s) | Description of Change | Release |
|----|----|----|----|----|
|  | 03.11.0217 | All | First Issue | I1.01 |
|  | 30.04.2018 | All | Final version of the document | I1.01 |
|  | 11.09.2018 | 16 | Update of metadata | I1.02 |
|  | 06.11.2019 | All | Update of document | I1.03 |
|  | 10.04.2020 | All | Update of document after external review | I1.04 |
|  | 17.04.2020 | All | Including SLSTR relevant information | I1.05 |

## 0.3 List of Acronyms

|  |  |
|----|----|
| ABBREV. | MEANING |
| ATBD | Algorithm Theoretical Basis Document |
| CCI | Climate Change Initiative |
| ESA | European Space Agency |
| ETM+ | Enhanced Thematic Mapper plus |
| EU | European Union |
| FP7 | 7th Framework Program of the European Community for research, technological development and demonstration activities |
| FSC | Fractional Snow Cover |
| IFOV | Instantaneous Field Of View |
| MODIS | Moderate Resolution Imaging Spectroradiometer |
| MSI | Multi-Spectral Instrument |
| NASA | National Aeronautics and Space Administration |
| NDSI | Normalized Difference Snow Index |
| NDVI | Normalized Difference Vegetation Index |
| NH | Northern Hemisphere |
| NIR | Near Infrared |
| NRT | Near-Real Time |
| OLI | Operational Land Imager |
| QA4EO | Quality Assessment for Earth Observation |
| PUM | Product User Manual |
| QAR | Quality Assessment Report |
| RMSE | Root Mean Square Error |
| S3 | Sentinel-3 |
| SCE | Snow Cover Extent |
| SLSTR | Sea and Land Surface Temperature Radiometer |
| SnowPEx | Satellite Snow Product Intercomparison and Validation Exercise |
| S-NPP | Suomi- National Polar-Orbiting Partnership |
| SRTM | Shuttle Radar Topography Mission |
| SWIR | Shortwave Infrared |
| TIR | Thermal Infrared |
| TIRS | Thermal Infrared Sensor |
| TM | Thematic Mapper |
| VHR | Very High Resolution |
| VIIRS | Visible Infrared Imaging Radiometer Suite |
| VIS | Visible |

# 1 Background of the document

## 1.1 Executive Summary

The Global Land (GL) Component in the framework of Copernicus is earmarked as a component of the Land service to operate “a multi-purpose service component” that will provide a series of bio-geophysical products on the status and evolution of land surface at global scale. Production and delivery of the parameters are to take place in a timely manner and are complemented by the constitution of long term time series.

The Copernicus Global Land Service contains a Snow Cover Extent (SCE) Near Real Time (NRT) product extending Northern Hemisphere (NH) at 0.01 degree resolution. The SCE product provides information on the Fraction of Snow Cover (FSC) per pixel in percentage (0% – 100%). The SCE is derived from medium resolution optical satellite data.

The service is based on data from the Suomi Near-Polar-orbiting Partnership (S-NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) and of Sentinel-3 (S3) Sea and Land Surface Temperature Radiometer (SLSTR) data. The NRT snow products provided as pre-operational service since January 2018 are based on S-NPP VIIRS data. From the winter season 2020/21 onwards, starting with 1st October 2020, the NRT service is planned to be based on the S3 SLSTR data. It is planned to continue the S-NPP VIIRS based service as backup.

The spectral capabilities of the sensor are used in combination with a digital elevation model, a transmissivity map describing the transmissivity of forest canopy, and surface classification maps to detect the fraction of snow cover per pixel in percentage. The usage of the transmissivity map allows also in forested areas to detect the snow on the ground.

The Product User Manual (PUM) is a self-contained document which gathers all necessary information to use the NH SCE product at 0.01 degree resolution on an efficient and reliable way.

## 1.2 Scope and Objectives

The Product User Manual (PUM) is the primary document that users should read before handling the products. It gives an overview of the product characteristics, in terms of algorithm, technical characteristics, and main validation results.

## 1.3 Content of the document

This document is structured as follows:

- Chapter 2 recalls the users’ requirements, and the expected performance
- Chapter 3 summarizes the retrieval methodology
- Chapter 4 describes the technical properties of the product
- Chapter 5 summarizes the results of the quality assessment

## 1.4 Related documents

### 1.4.1 Applicable documents

AD1: IGOS, 2007: Cryosphere Theme Report 2007. WMO/TD-No 1405. 100 pp.

AD2: GCOS, 2006: Systematic observation requirements for satellite-based products for climate. WMO/TD Report No. 1338, September 2006.

AD3: GCOS – 200.2016. The Global Observing System for Climate: Implementation Needs. (GOOS-214). http://unfccc.int/files/science/workstreams/systematic_observation/application/pdf/gcos_ip_10oct2016.pdf

AD4: WMO OSCAR Observing Systems Capability Analysis and Review Tool; https://www.wmo-sat.info/oscar/observingrequirements

AD5: Annex I – Technical Specifications JRC/IPR/2015/H.5/0026/OC to Contract Notice 2015/S 151-277962 of 7^(th) August 2015

AD6: Appendix 1 – Copernicus Global Land Component Product and Service Detailed Technical requirements to Technical Annex to Contract Notice 2015/S 151-277962 of 7^(th) August 2015

### 1.4.2 Input

| Document ID | Descriptor |
|----|----|
| CGLOPS2_SSD | Service Specifications of the Global Component of the Copernicus Land Service. |
| CGLOPS2_ATBD_SCE-NHEMI-1km_V1 | Algorithm Theoretical Basis Document of the SCE-NHEMI-1km_V1 product |
| CGLOPS2_QAR_SCE-NHEMI-1km_V1 | Report describing the results of the scientific quality assessment of the SCE-NHEMI-1km_V1 product |
| CGLOPS2_PRD_SCE-NHEMI-1km_V1 | Product Requirements Document of the SCE-NHEMI-1km_V1 product |
| CGLOPS2_PSD_SCE-NHEMI-1km_V1 | Product Specification Document of the SCE-NHEMI-1km_V1 product |
| CGLOPS2_PUM_SCE500-CEURO-500m_V1 | Product User Manual of the SCE500-CEURO-500m_V1 product |
| CGLOPS2_PUM_SCE-NHEMI-1km-V1 | Product User Manual (final version) describing how to use the SCE-NHEMI-1km V1 product from S-NPP VIIRS data. |

### 1.4.3 Output

| Document ID | Descriptor |
|----|----|
| CGLOPS2_PUM_SCE-NHEMI-1km-V1 | Product User Manual (final version) describing how to use the SCE-NHEMI-1km V1 product from S3 SLSTR or S-NPP VIIRS data. |

### 1.4.4 External documents

ED1: CryoLand URD 2012. CryoLand User Requirement Document, URD , Final version. 31.05.2012. http://cryoland.enveo.at/docs/publications/CryoLand_No262925_D06.1_URD.pdf

ED2: Malnes, E., Buanes, A., Nagler, T., Bippus, G., Gustafsson, D., Schiller, C., Metsämäki, S., Pulliainen, J., Luojus, K., Larsen, H.E., Solberg, R., Diamandi, A., Wiesmann, A. (2015). User requirements for the snow and land ice services – CryoLand. The Cryosphere, 9, 1191–1202, doi:10.5194/tc-9-1191-2015.

ED3: Malenovský, Z., H. Rott, J. Cihlar, M. E Schaepman, G. García-Santos, R. Fernandes and M. Berger. 2012. Sentinels for Science: Potential of Sentinel-1, -2, and -3 missions for scientific observations of ocean, cryosphere, and land. Remote Sensing of Environment, vol. 120, pp 91-101.

# 2 Review of Users Requirements

According to the applicable documents \[AD1\] to \[AD4\], and the external documents \[ED1\] to \[ED3\], the users’ requirements relevant for the Northern Hemisphere Snow Cover Extent product are:

- Definition: Northern Hemisphere (NH) Snow Cover Extent (SCE)
- Geometric properties:
  - Spatial resolution: Minimum: 4 km, Target: 500 m, 100 m in complex terrain
  - Grid / Projection: Geographic coordinates (latitude/longitude), WGS84 datum, WGS84 ellipsoid
- Geographical coverage:
  - Northern Hemisphere (84°N / 180°W – 25°N/180°E): land areas
  - Target: Global land areas
- Accuracy requirements:
  - Geometric accuracy: Minimum: 1/3 IFOV, Target: IFOV 1 km (100 m in complex terrain)
  - Thematic accuracy: Minimum: 15 %, Target: 5 %
- Temporal requirements:
  - Time period: Full year
  - Temporal frequency: Minimum: Daily, Target: 12 hours
- Delivery time:
  - Minimum: 24 hours after image acquisition, Target: 12 hours after image acquisition

# 3 Algorithm

## 3.1 Overview

The SCE product is generated daily in near-real time for the NH land areas, including Greenland, based on medium resolution optical satellite data. The snow maps since January 2018 are generated from S-NPP VIIRS data. The NRT service based on S3 SLSTR data is planned to start with the beginning of the next winter season according to the hydrological year, on 1^(st) October 2020. The production from S-NPP VIIRS data is planned to be continued then as backup service. The NH SCE product provides information on the Fraction of Snow Cover (FSC) on ground (also in forested areas) per pixel in percentage (0% – 100%), and is extending from 84°N/180°W to 25°N/180°E with a pixel size of 0.01° x 0.01° (approx. 1 km x 1 km). The product is provided within 1 day after the raw image acquisition.

## 3.2 The retrieval Methodology

The generation of the NH SCE product is based on a two-step approach: a pre-classification is performed using the Normalized Difference Snow Index (NDSI) which is based on the different reflectivity of snow and other surfaces in the visible and mid-infrared wavelengths (Hall et al. 2002), combined with a threshold applied on the brightness temperature from a thermal infrared band. The NDSI is also used as basic map for cloud screening. On all pixels identified as potentially snow covered from the pre-classification, the SCAmod (Metsämäki et al. 2005, 2012) algorithm is applied to classify fractional snow cover for the NH land areas. Further information is given in the CGLOPS2_ATBD_SCE-NHEMI-1km_V1.

## 3.3 Limitations of the Product

The SCAmod algorithm is very sensitive to the transmissivity map used as input. As the transmissivity map is derived from GlobCover data, boreal forests in Scandinavia and forests in southern latitudes or in other regions have similar transmissivity values in this map. This can partly result in misclassifications of snow.

In case of snow free ground but cold temperatures at night, which usually can occur from autumn till spring, surface hoar or hoar frost built up during night can remain until the satellite acquisition time late in the morning. Such areas often have very similar spectral signatures as snow covered areas and can thus be misclassified as snow.

During the polar night, a snow classification is not possible in the northern latitudes. All pixels with solar zenith angle greater than 80° are classified as “polar night”.

Very large sensor viewing zenith angles can introduce major errors in the snow classification or the cloud screening. Thus, pixels with sensor viewing zenith angles greater than 80° are excluded from the processing.

## 3.4 Differences with the previous version

This is the first version of the product.

# 4 Product Description

## 4.1 File Naming

The Snow Cover Extent (SCE)-Northern Hemisphere (NHEMI)-1km product follows the naming standard:

`c_gls_SCE_<YYYYMMDDHHmm>_<AREA>_<SENSOR>_V<VERSION>`

e.g.

`c_gls_SCE_202010010000_NHEMI_SLSTR_V1.0.1.nc`

where:

- `<YYYYMMDDHHmm>` gives the temporal location of the file. YYYY, MM, DD, HH and mm denote the year, the month, the day, the hour and the minutes respectively. The products are daily composites, so the time “0000” is used for the “HHmm” in the file name. Detailed start and end times are provided in the metadata (Table 4.3).
- `<AREA>` gives the spatial coverage of the file. In our case, `<AREA>` is NHEMI, short name for Northern Hemisphere.
- `<SENSOR>` gives the name of the sensors used to retrieve the product, with VIIRS referring to Suomi NPP Visible Infrared Imaging Radiometer Suite, and SLSTR to Sentinel-3 Sea and Land Surface Temperature Radiometer
- `<VERSION>` shows the processing line version used to generate these SCE_NRT_1km products. The version denoted as M.m.r (e.g. 1.0.1), with ‘M’ representing the major version (e.g. V1), ‘m’ the minor version (starting from 0) and ‘r’ the production run number (starting from 1) (Table 4.1).

Table 4.1: Explanation in version numbering and recommendations for using efficiently the products.

| Versions | Differences | Recommendations |
|----|----|----|
| Major | Significant change to the algorithm. | Do not mix various major versions in the same applications, unless it is otherwise stated. |
| Minor | Minor changes in the algorithm | Can be mixed in the same applications, but require attention or modest modifications |
| Run | Fixes to bugs and minor issues. Later run automatically replaces former | Consider it as a drop-in replacement |

## 4.2 File Format

The SCE-NHEMI-1km products are delivered as Network Common Data Form version 4 (netCDF4) file with metadata attributes compliant with version 1.7 of the Climate & Forecast conventions (CF V1.7) containing the following layer:

- `SCE`: Snow Cover Extent value

The coverage of the file corresponds to the spatial extent of the NH defined for cryospheric parameters (84°N/180°W – 25°N/180°E).

## 4.3 Product Content

### 4.3.1 Data File

The SCE NHEMI product, including the product coding, is a heritage of the SCE CEURO500 product (CGLOPS2_PUM_SCE500-CEURO-500m_V1) developed originally within the EU FP7 project CryoLand. We decided to continue basically with the same coding definitions also for the SCE NHEMI products (Table 4.2) to support known implementations of key users using the SCE products as input for their operational systems. Information on the water type (sea, lake, river) is only available for the Pan-European domain from the Copernicus CORINE Land Cover data set. For the NH SCE products, the water bodies are based on the ESA CCI Land Cover data set of the year 2015. All pixels classified as water are masked in the NH SCE product with the same code, independent of the water type.

Table 4.2: Description of the product coding provided for SCE-NHEMI-1km product.

| Code value | Class | Comment |
|----|----|----|
| 0 | Outside area of interest | Outside of NH |
| 20 | Sea mask | Water mask |
| 30 | Cloud mask | Generated by Single Cloud Detection Approach 2.0 (Metsämäki et al. 2015) |
| 251 | Polar night | If solar zenith angle for pixel \> 80° |
| 254 | Input data error |  |
| 255 | No data | No data within the extent of NH |
| 100 - 200 | Snow Cover Extent | For interpretation of the SCE in percent scaled between 0% and 100% use the following conversion: `SCE = CODE – 100` |

The netCDF files contain a number of netCDF metadata attributes

- on the file-level (Table 4.3 and Table 4.4);
- on the layer-level (Table 4.5);
- at the level of the standard dimension variables for latitude (‘lat’) and longitude (‘lon’), holding one value per row or column respectively (Table 4.6);
- at the level of the grid mapping (spatial reference system) variable (‘crs’) (Table 4.7).

Table 4.3: Description of netCDF file attributes, Global Land extensions.

|  |  |  |  |
|----|----|----|----|
| **Attribute name** | **Description** | **Data Type** | **Example(s)** |
| Conventions | Version of the CF-Conventions used | String | CF-1.7 |
| title | A description of the contents of the file | String | Fractional Snow Cover, northern hemisphere, Sentinel-3 SLSTR (0.01deg., 2020-10-01) |
| institution | The name of the institution that produced the product | String | ENVEO IT GmbH |
| source | The method of production of the original data | String | Derived from EO satellite imagery |
| history | A global attribute for an audit trail. One line, including date in ISO-8601 format, for each invocation of a program that has modified the dataset. | String | 2020-10-01 Processing line SCE |
| references | Published or web based references that describe the data or methods used to produce it. | String | http://land.copernicus.eu/global/products/sce |
| archive_facility | Specifies the name of the institution that archives the product | String | CLS |
| product_version | Version of the product (VM.m.r) | String | V1.0.1 |
| time_coverage_start | Start date and time of the total coverage of the data for the product. | String | 2020-10-01T00:55:26.4Z |
| time_coverage_end | End date and time of the total coverage of the data for the product. | String | 2020-10-01T19:49:10.2Z |
| platform | Name(s) of the orbiting platform(s) | String | Suomi_NPP, Sentinel-3 |
| sensor | Name(s) of the sensor(s) used | String | VIIRS, SLSTR |
| identifier | Unique identifier for the product | String | urn:cgls:global:sce_v1_0.01degree:SCE_202010010000_NHEMI_SLSTR_V1.0.1 |
| parent_identifier | Identifier of the product collection (time series) for the product in Copernicus Global Land Service metadata catalogue. | String | urn:cgls:global:sce_v1_0.01degree |
| long_name | Extended product name | String | Snow Cover Extent |
| orbit_type | Orbit type of the orbiting platform(s) | String | LEO |
| processing_level | Product processing level | String | L3 |
| processing_mode | Processing mode used when generating the product (Near-Real Time, Consolidated or Reprocessing) | String | Near Real Time |
| copyright | Text to be used by users when referring to the data source of this product in publications (copyright notice) | String | Copernicus Service information 2019 |

Table 4.4: Description of file-level netCDF file attributes, extensions for self-standing products.

[TABLE]

Table 4.5: Description of netCDF layer attributes.

[TABLE]

\*) Will be added from 1st October 2020 onwards.

Table 4.6: Description of netCDF attributes for coordinate dimensions (latitudes and longitudes).

|  |  |  |  |
|----|----|----|----|
| **Attribute** | **Description** | **Data Type** | **Example(s)** |
| CLASS | Dataset type | String | DIMENSION_SCALE |
| DIMENSION_LABELS | Label used in netCDF4 library | String | lon |
| NAME | Short name | String | lon |
| standard_name | A standardized name that references a description of a variable's content in CF-Convention's standard names table. Note that each standard_name has corresponding unit (from Unidata's udunits). | String | longitude |
| long_name | A descriptive name that indicates a variable's content. This name is not standardized. Required when a standard name is not available. | String | longitude |
| units | Units of the variable's content, taken from Unidata's udunits library. | String | degrees_east |
| axis | Identifies latitude, longitude, vertical, or time axes. | String | X |

Table 4.7: Description of netCDF attributes for the grid mapping variable.

|  |  |  |  |
|----|----|----|----|
| **Attribute** | **Description** | **Data Type** | **Example(s)** |
| GeoTransform | Six coefficients for the affine transformation from pixel/line space to coordinate space, as defined in GDAL's GeoTransform | String | -180 0.01 0 84 0 -0.01 |
| longitude_of_prime_meridian | Projection center line | Double | 0.0 |
| semi_major_axis | Radius of Earth used for projection (m) | Double | 6378137 |
| grid_mapping_name | Name used to identify the grid mapping | String | latitude_longitude |
| inverse_flattening | Used to specify the inverse flattening (1/f) of the ellipsoidal figure associated with the geodetic datum and used to approximate the shape of the Earth | Float | 298.257223563 |
| spatial_ref | Spatial reference system in OGC's Well-Known Text (WKT) format | String | GEOGCS\["WGS 84",DATUM\["WGS_1984",SPHEROID\["WGS 84",6378137,298.257223563,AUTHORITY\["EPSG","7030"\]\],AUTHORITY\["EPSG","6326"\]\],PRIMEM\["Greenwich",0\],UNIT\["degree",0.0174532925199433\],AUTHORITY\["EPSG","4326"\]\] |

### 4.3.2 Quicklook

A daily quicklook is provided as a GEOTIFF file.

## 4.4 Product Characteristics

### 4.4.1 Projection and Grid Information

The product is projected in a regular latitude/longitude grid with the ellipsoid WGS 1984 (Terrestrial radius=6378km, EPSG: 4326). The resolution of the grid is 0.01 degree. Coordinate reference is the upper left corner of the pixel. The origin is the upper left corner of the upper left pixel.

### 4.4.2 Spatial Information

The NH SCE product is provided from longitude 180°W to 180°E and latitude 25°N to 84°N.

### 4.4.3 Temporal Information

The SCE-NHEMI-1km is a daily product provided throughout the whole year. The NRT product generation from S-NPP VIIRS data started in January 2018. The NRT product generation from S3 SLSTR data in planned to start in October 2020.

### 4.4.4 Data Policies

Any use of the SCE-NHEMI-1km product implies the obligation to include in any publication or communication using these products the following citation:

“The product was generated by the land service of Copernicus, the Earth Observation program of the European Commission. The research leading to the current version of the product has received funding from various European Commission Research and Technical Development programs. The product is based on \[SATINFO\].”

The field \[SATINFO\] depends on the satellite data used for the product generation and can be one of the following:

- Sentinel-3 SLSTR 500 m / 1 km data (©Copernicus/ESA)
- Suomi-NPP VIIRS 750 m data (© NOAA)

The user accepts to inform Copernicus about the outcome of the use of the above-mentioned products and to send a copy of any publications that use these products to the following address gabriele.schwaizer@enveo.at.

### 4.4.5 Contacts

Accountable contact: European Commission Directorate-General Joint Research Centre

Email address: copernicuslandproducts@jrc.ec.europa.eu

Scientific, Production and Distribution contact: ENVEO IT GmbH, Austria

Email address: gabriele.schwaizer@enveo.at (primary contact)

sce.globland@enveo.at (ftp-server issues, file availability, and issues with file format)

# 5 Validation

The validation of the NH SCE products from S-NPP VIIRS data has been performed with more than 200 selected Landsat scenes acquired in between January 2018 and April 2019, and with more than 200’000 in-situ measurements of snow depth available for the periods January – June 2018 and October 2018 – June 2019. The validation of the NH SCE products from S3 SLSTR data has been performed with about 100 selected Landsat scenes acquired between November 2018 and May 2019, and with more than 60’000 in-situ measurements of snow depth available for the period January - May 2019.

For the generation of reference snow maps from Landsat data, three different snow algorithms (Dozier and Painter 2004, Klein, Hall, and Riggs 1998, Salomonson and Appel 2004, 2006) are applied on each Landsat scene. The SCE product has been validated on a pixel-by-pixel comparison using statistical measures to describe the performance of the product (CGLOPS2_QAR_SCE-NHEMI-1km_V1), following the validation protocols developed and agreed by the international snow community within the ESA QA4EO Satellite Snow Product Intercomparison and Evaluation Exercise (SnowPEx).

The mean resulting unbiased Root Mean Square Error (RMSE) derived from the validation of the SCE product with all reference snow maps is about 13%, independently of the applied snow algorithm for the generation of the reference snow map and the sensor used for the NH SCE product generation. The mean Bias derived for validation with Landsat snow maps is in slightly negative, about -3% for S-NPP VIIRS based NH SCE products, and about -4% for S3 SLSTR based NH SCE products.

Additional to the overall performance, the NH SCE products were analysed separately for different surface and terrain classes, considering forested / non-forested areas as well as mountains / plains and combinations of these classes. For all forested classes, only Landsat based reference snow maps generated with snow algorithms resulting in the same thematic information as the SCE product, namely snow on ground, are used for the validation. For non-forested classes, all algorithms used for the reference snow map generation are considered.

In forested areas, the resulting mean unbiased RMSE is about 14% for NH SCE products from both sensors. The mean Bias is about -2% for NH SCE products from S-NPP VIIRS data, while the mean Bias for NH SCE products from S3 SLSTR data is slightly more negative, about -5%.

In non-forested areas the mean unbiased RMSE for NH SCE products from S-NPP VIIRS data is slightly lower, about 12%, with a slightly more negative mean Bias values of about -4%. For NH SCE products from S3 SLSTR data, the mean unbiased RMSE for non-forested areas is only 9%, and the mean Bias value for this class is only -2%. The slightly negative bias values indicate an underestimation of snow by the NH SCE product from both sensors compared to the reference snow maps from Landsat imagery.

Additionally, the agreement of the fraction of snow cover of the SCE product with the aggregated fractional snow cover from the selected Landsat scenes is assessed. In case of fractional snow cover ≤75%, the NH SCE products rather overestimate the reference snow cover, while for areas largely covered by snow (76% - 100%), the NH SCE products tend to slightly underestimate the reference snow cover derived from Landsat data. This pattern is observed independent of the sensor used for the NH SCE product generation.

Although the range of the resulting statistics can be large for some validation cases, the overall results indicate that the product performance is meeting the user requirements of \<15% thematic accuracy for all surface classes, independent of the satellite sensor used for the product generation.

The range of the resulting statistics can be large depending on the surface class and the terrain, as also indicated by the mean results shown in Table 5.1 for S-NPP VIIRS based NH SCE products, and in Table 5.2 for S3 SLSTR based NH SCE products.

Table 5.1: Summary of statistical measures resulting from the validation of the NH SCE product from S-NPP VIIRS data with selected Landsat scenes covering various classes. Reference snow algorithms: S = Salomonson & Appel, 2006; K = Klein et al., 1998; D = Dozier and Painter, 2004.

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
| Surface class | Snow algorithm | Unbiased RMSE |  |  | Bias |  |  | Mean Correlation Coefficient | \# pixels used for validation | \# LC08 scenes |
|  |  | Min | Mean | Max | Min | Mean | Max |  |  |  |
| Total area | K | 0,04 | 12,45 | 38,89 | -48,16 | -4,08 | 14,49 | 0,45 | 8876240 | 209 |
|  | D | 0,03 | 12,93 | 36,64 | -23,24 | -1,18 | 23,96 | 0,47 |  |  |
| Total non-forested area | S | 0,04 | 11,30 | 35,22 | -30,21 | -1,97 | 7,50 | 0,53 | 5311230 | 209 |
|  | K | 0,04 | 11,86 | 36,95 | -39,95 | -5,25 | 2,65 | 0,44 |  |  |
|  | D | 0,03 | 11,63 | 36,64 | -39,14 | -3,83 | 5,09 | 0,48 |  |  |
| Total forested area | K | 0,00 | 13,95 | 39,40 | -50,24 | -4,27 | 25,00 | 0,37 | 3565010 | 200 |
|  | D | 0,00 | 14,66 | 36,37 | -26,03 | 0,63 | 40,00 | 0,39 |  |  |
| Total plains | K | 0,00 | 10,06 | 37,53 | -48,16 | -3,92 | 15,53 | 0,38 | 5519657 | 208 |
|  | D | 0,00 | 10,56 | 36,64 | -31,00 | -1,28 | 23,57 | 0,40 |  |  |
| Total mountains | K | 0,99 | 13,21 | 35,18 | -57,27 | -3,14 | 15,37 | 0,52 | 3356583 | 119 |
|  | D | 0,99 | 12,99 | 29,74 | -20,02 | -1,22 | 24,96 | 0,53 |  |  |

Table 5.2: Summary of statistical measures resulting from the validation of the NH SCE product from S3 SLSTR data with selected Landsat scenes covering various classes. Reference snow algorithms: S = Salomonson & Appel, 2006; K = Klein et al., 1998; D = Dozier and Painter, 2004.

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
| Surface class | Snow algorithm | Unbiased RMSE |  |  | Bias |  |  | Mean Correlation Coefficient | \# pixels used for validation | \# LC08 scenes |
|  |  | Min | Mean | Max | Min | Mean | Max |  |  |  |
| Total area | K | 0,19 | 12,96 | 42,28 | -38,98 | -4,77 | 4,19 | 0,43 | 5641820 | 100 |
|  | D | 0,19 | 13,10 | 43,86 | -38,09 | -3,25 | 15,39 | 0,42 |  |  |
| Total non-forested area | S | 0,66 | 9,05 | 23,32 | -21,09 | 0,29 | 13,65 | 0,53 | 3322154 | 100 |
|  | K | 0,17 | 9,32 | 25,02 | -31,31 | -3,22 | 2,97 | 0,44 |  |  |
|  | D | 0,17 | 9,10 | 24,71 | -29,99 | -2,22 | 9,46 | 0,48 |  |  |
| Total forested area | K | 0,04 | 14,24 | 44,80 | -39,66 | -5,67 | 46,50 | 0,38 | 2319666 | 97 |
|  | D | 0,03 | 14,46 | 46,34 | -38,77 | -3,53 | 54,00 | 0,38 |  |  |
| Total plains | K | 1,03 | 11,11 | 40,48 | -17,33 | -1,90 | 4,39 | 0,46 | 3256109 | 100 |
|  | D | 1,03 | 11,25 | 42,62 | -20,91 | -1,45 | 11,49 | 0,45 |  |  |
| Total mountains | K | 1,03 | 11,11 | 40,48 | -17,33 | -1,90 | 4,39 | 0,46 | 2385711 | 60 |
|  | D | 1,03 | 11,25 | 42,62 | -20,91 | -1,45 | 11,49 | 0,45 |  |  |

Further, the NH SCE products were validated with in-situ snow depth measurements. For this validation, both, the SCE and the in-situ products were translated into binary snow information. Two options were investigated to compare binary snow information from the NH SCE products from S-NPP VIIRS data and in-situ measurements: FSC \> 15% and SD \> 2cm, and FSC \> 10% and SD \> 1cm. For the S3 SLSTR based NH SCE products, the validation was performed using FSC \> 15% and SD \> 2cm, as well as FSC \> 15% and SD \> 1cm.

For the in-situ measurements, the applied snow depth thresholds were used assuming that the total surrounding area covering the associated pixel in the SCE product is snow covered. The comparison of these snow covered, and snow free pixel information resulted for the S-NPP VIIRS based NH SCE products in an overall accuracy of 92%, with the omission and commission errors \<10%. For S3 SLSTR based NH SCE products, an overall accuracy of 87% and omission and commission errors \<15% were achieved.

The overall validation results indicate that the NH SCE product matches the minimum thematic accuracy requirements of \<15% FSC defined by the users.

# 6 References

Dozier, J., and T. H. Painter. 2004. “Multispectral and Hyperspectral Remote Sensing of Alpine Snow Properties.” Annual Review of Earth and Planetary Sciences 32: 465 – 494.

Hall, D. K., G. A. Riggs, V. V. Salomonson, N. DiGiromamo, and K. J. Bayr. 2002. “MODIS Snow-Cover Products.” Remote Sensing of Environment 83: 181–94.

Klein, Andrew G, Dorothy K Hall, and George A Riggs. 1998. “Improving Snow Cover Mapping in Forests through the Use of a Canopy Reflectance Model.” Hydrological Processes 12: 1723– 44.

Metsämäki, S., S. Anttila, M. Huttunen, and J. Vepsäläinen. 2005. “A Feasible Method for Fractional Snow Cover Mapping in Boreal Zone Based on a Reflectance Model.” Remote Sensing of Environment 95 (1): 77–95.

Metsämäki, S., O.-P. Mattila, J. Pulliainen, K. Niemi, K. Luojus, and K. Böttcher. 2012. “An Optical Reflectance Model-Based Method for Fractional Snow Cover Mapping Applicable to Continental Scale.” Remote Sensing of Environment 123 (August). Elsevier Inc.: 508-21. doi:10.1016/j.rse.2012.04.010.

Metsämäki, S., J. Pulliainen, M. Salminen, K. Luojus, A. Wiesmann, R. Solberg, K. Böttcher, M. Hiltunen, and E. Ripper. 2015. “Introduction to GlobSnow Snow Extent Products with Considerations for Accuracy Assessment.” Remote Sensing of Environment 156. Elsevier Inc.: 96-108. doi:10.1016/j.rse.2014.09.018.

Salomonson, V.V., and I. Appel. 2006. “Development of the Aqua MODIS NDSI Fractional Snow Cover Algorithm and Validation Results.” IEEE Transactions on Geoscience and Remote Sensing 44 (7): 1747–56. doi:10.1109/TGRS.2006.876029.

Salomonson, V.V, and I Appel. 2004. “Estimating Fractional Snow Cover from MODIS Using the Normalized Difference Snow Index.” Remote Sensing of Environment 89 (3): 351–60. doi:10.1016/j.rse.2003.10.016.

Back to top

## Reuse

EUPL (\>= 1.2)
