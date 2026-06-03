# CLCplus Backbone 2023 – Product User Manual

2026-06-03

- [<span class="toc-section-number">1</span> Executive
  summary](#sec-executive-summary)
- [<span class="toc-section-number">2</span> Scope of the
  document](#sec-scope-of-the-document)
- [<span class="toc-section-number">3</span> Lineage of
  product](#sec-lineage-of-product)
- [<span class="toc-section-number">4</span> Review of user
  requirements](#sec-review-of-user-requirements)
- [<span class="toc-section-number">5</span> Product application areas
  and exemplary use
  cases](#sec-product-application-areas-and-examplary-use-cases)
  - [<span class="toc-section-number">5.1</span> Use case on climate
    change mitigation and the policy support for LULUCF via the CLCplus
    LULUCF
    Instance](#use-case-on-climate-change-mitigation-and-the-policy-support-for-lulucf-via-the-clcplus-lulucf-instance)
  - [<span class="toc-section-number">5.2</span> Thematic application
    areas](#sec-thematic-application-areas)
- [<span class="toc-section-number">6</span> Product
  description](#sec-production-description)
  - [<span class="toc-section-number">6.1</span> CLCplus Backbone 2023
    Raster](#sec-CLCplus-Backbone-2023-Raster)
    - [<span class="toc-section-number">6.1.1</span> Technical
      specifications of CLCplus Backbone
      2023](#sec-technical-specifications-of-CLCplus-Backbone-2023)
    - [<span class="toc-section-number">6.1.2</span> Nomenclature
      concept and class
      definitions](#sec-nomenclature-concept-and-class-definitions)
    - [<span class="toc-section-number">6.1.3</span> Decision tree for
      area thresholds](#sec-decision-tree-for-area-thresholds)
    - [<span class="toc-section-number">6.1.4</span> Examples for class
      assignment](#sec-examples-for-class-assignment)
  - [<span class="toc-section-number">6.2</span> Auxiliary
    layers](#auxiliary-layers)
    - [<span class="toc-section-number">6.2.1</span> Raster Data Score
      Layer](#raster-data-score-layer)
    - [<span class="toc-section-number">6.2.2</span> Raster Confidence
      Layer](#raster-confidence-layer)
    - [<span class="toc-section-number">6.2.3</span> Raster
      Post-processing Layer](#raster-post-processing-layer)
- [<span class="toc-section-number">7</span> Product methodology and
  workflow](#sec-product-methodology-and-workflow)
  - [<span class="toc-section-number">7.1</span> Input
    data](#input-data)
  - [<span class="toc-section-number">7.2</span> Production
    units](#sec-production-units)
  - [<span class="toc-section-number">7.3</span> Time series
    classification](#time-series-classification)
  - [<span class="toc-section-number">7.4</span>
    Post-processing](#post-processing)
- [<span class="toc-section-number">8</span> Terms of use and product
  technical support](#sec-terms-of-use-and-product-technical-support)
  - [<span class="toc-section-number">8.1</span> Terms of
    use](#terms-of-use)
  - [<span class="toc-section-number">8.2</span> Citation](#citation)
  - [<span class="toc-section-number">8.3</span> Product technical
    support](#product-technical-support)
- [<span class="toc-section-number">9</span> List of abbreviations &
  acronyms](#sec-list-of-abbreviations-and-acronyms)
- [<span class="toc-section-number">10</span> References
  {sec-references}](#references-sec-references)
- [<span class="toc-section-number">11</span> Annexes](#annexes)
  - [<span class="toc-section-number">11.1</span> Annex 1: Colour
    palettes](#annex-1-colour-palettes)
    - [<span class="toc-section-number">11.1.1</span> Raster Product
      (RAS)](#raster-product-ras)
    - [<span class="toc-section-number">11.1.2</span> Data Score Layer
      (RASDL)](#data-score-layer-rasdl)
    - [<span class="toc-section-number">11.1.3</span> Raster Confidence
      Layer (RASCL)](#raster-confidence-layer-rascl)
    - [<span class="toc-section-number">11.1.4</span> Post-Processing
      Layer (RASPL)](#post-processing-layer-raspl)
  - [<span class="toc-section-number">11.2</span> Annex 2: Projection
    parameters](#annex-2-projection-parameters)
- [<span class="toc-section-number">12</span> Document
  history](#sec-document-history)
- [<span class="toc-section-number">13</span> Applicable
  documents](#sec-applicable-documents)

# Executive summary

The Copernicus Land Monitoring Service (CLMS) provides geospatial
information on land cover and its changes, land use, vegetation state,
water cycle and Earth’s surface energy variables to a broad range of
users in Europe and across the World in the field of environmental
terrestrial applications. It supports applications in a variety of
domains such as spatial and urban planning, forest management, water
management, agriculture and food security, nature conservation and
restoration, rural development, ecosystem accounting and
mitigation/adaptation to climate change. CLMS is jointly implemented by
the European Environment Agency (EEA) and the European Commission DG
Joint Research Centre (JRC) and has been operational since 2012.

The ‘CLCplus Backbone’ constitutes the first component of the CLMS’s
‘CLCplus Product Suite’, which represents a true paradigm change in
European land cover/land use monitoring, building on the rich legacy of
the European CORINE Land Cover (CLC) flagship product. The CLCplus
Backbone is a large scale, seamless and high-resolution inventory of
European land cover. It covers the whole of EEA38 territory, the United
Kingdom (UK) and the French Overseas Departments (DOMs). The CLCplus
Backbone products are freely available, enabling the use by a broad
audience, for a wide range of applications.

The CLCplus Backbone 2023 is a geospatial raster product containing 11
basic land cover classes and is based on a time series of
high-resolution Sentinel-2 satellite imagery. The input timeseries for
this 2023 production covers the reference year ± three months,
i.e. 01.10.2022 to 31.03.2024, which is needed to enable the distinction
of the 11 land cover classes. CLCplus Backbone maps the dominant
(spatially and temporally throughout the specific reference year) land
cover for each 10m-raster cell (pixel), applying specific rules
according to a comprehensive decision tree. The product has first been
produced for the reference year 2018, has been updated for 2021
(excluding the UK) and now as well for 2023, switching to a biennial
update cycle and re-including the UK.

This main product is accompanied by three auxiliary layers. The Raster
Data Score Layer provides information about the quality of the
Sentinel-2 time series data by mapping the number of available cloud
free acquisitions within the input time window (i.e. 2023 ± 3 months).
The Raster Confidence Layer provides information about the confidence of
the initial class assignment and the Raster Post-processing Layer flags
all pixels, that underwent a class change during the postprocessing.

This document constitutes the Product User Manual for the CLCplus
Backbone 2023. It is intended to provide all product information to
users that may be required for successful furtherreaching analyses and
applications. It describes the class nomenclature in detail, defining
which land cover elements are included or excluded for specific classes
and provides a reference to their embedding in the respective EAGLE Land
Cover Components. Further, it provides the full technical specifications
for the CLCplus Backbone 2023, as well as the additional products,
together with discussions of the strengths and limitations of the
products to be considered for any derived applications.

# Scope of the document

This Product User Manual (PUM) is the primary document that users are
recommended to read before using the CLCplus Backbone 2023 product. It
provides a description of the product and layer characteristics and a
guidance on lineage and usage of product. The PUM summarizes product
requirements and the methodologies applied in its production.
Furthermore, it provides information about expected product quality as
well as information on the terms of use and product technical support.

# Lineage of product

The CLCplus Backbone 2023 is the third product of its kind and extends
the time series of the existing 2018 and 2021 products. Since the first
production for the 2018 reference year the nature of the product is
largely unchanged, i.e. mapping 11 land cover classes with consistent
definitions in a raster at 10m spatial resolution. Nevertheless, there
have been some technical changes and adaptations on the way to the most
recent product update for the reference year 2023, as follows:

- The time window for the Sentinel-2 input data has been shortened from
  2 years for the 2018 production (i.e. 2018 ±6 months) to 1.5 years for
  the 2021 and 2023 productions (i.e. reference year ±3 months) to
  enable a timelier production that is closer to the actual reference
  year.

- A separate technical class has been introduced for the seawater areas
  in the buffer around the production AOI since the 2021 production (see
  <a href="#sec-product-methodology-and-workflow"
  class="quarto-xref">Section 7</a> and AD-1).

- The United Kingdom (UK) has been excluded for the 2021 production,
  while it has been re-introduced in the 2023 production. The 2021 gap
  for the UK remains and at this stage there are no plans for
  post-production.

- Since the 2023 reference year, the file naming has been adapted as
  described in <a href="#sec-CLCplus-Backbone-2023-Raster"
  class="quarto-xref">Section 6.1</a>

- The format of the product has been changed from a single pan-European
  mosaic to a tiled format with 100 x 100km tile size. Nevertheless, the
  French DOMs are still available as national mosaics.

# Review of user requirements

The following key user requirements were considered in the concept and
design of CLCplus BB. Each CLCplus Backbone production is expected to
comply with these original user requirements and compliance of the
product shall be ensured. User requirements may be reviewed as needed
and production shall account for altered requirements where possible.

Table 1: User requirements for CLCplus Backbone (CLCplus BB) products

| No. | Description | Comment |
|----|----|----|
| R01 | CLCplus BB must cover entire European territory | EEA38+UK, French DOMs |
| R02 | The data record offered by CLCplus BB must be seamless, complete and harmonized over the European territory. |  |
| R03 | CLCplus BB must make use of state-of-the-art and technology (methodology, satellite imagery). | Sentinel-2 |
| R04 | CLCplus BB shall complement and extend the existing CLMS portfolio in a useful and efficient manner. |  |
| R05 | CLCplus BB methodology and workflow must allow full-area production within one year to facilitate timely availability needed for downstream applications. |  |
| R06 | CLCplus BB periodic status updates shall facilitate a consistent data record over time. |  |
| R07 | CLCplus BB must at least comply with common thematic accuracy levels for large-area land cover models. |  |
| R08 | CLCplus BB must be accompanied by comprehensive information that allows users to understand the accuracy of the classification. | Confidence layer |
| R09 | Product metadata of CLCplus BB must be compliant with accepted standards. | INSPIRE |
| R10 | Land cover units contained by CLCplus BB must be described with a code list and associated names |  |
| R11 | CLCplus BB must have a well-documented data model and data dictionary. | EAGLE data model |
| R12 | CLCplus BB shall allow a separation of vegetation classes based and common and major structural and morphological properties. |  |
| R13 | CLCplus BB must allow full integration to the database component of CLCplus Core. |  |
| R14 | CLCplus BB must support independent assessments and the modelling of carbon pool dynamics in the context of the EU’s Regulation on the Inclusion of Greenhouse Gas emissions and Removals from Land use, Land Use Change and Forestry (LULUCF) by the provision of baseline geospatial inputs. |  |

# Product application areas and exemplary use cases

Land cover is the result of complex interactions and dynamics between
and among human activities (land use) and natural conditions
(e.g. climate, biota, soil, hydrology, topography). Land cover is
potentially a bulk proxy of all the processes involved. To this end, a
geospatial land cover dataset at continental scale provides the baseline
information to serve a diverse range of disciplines and domains. Key
features of CLCplus Backbone comprise:

- High-accuracy and high-detail land cover data record at continental
  scale,

- Thematically consistent and harmonized data record,

- Regular and frequent status updates,

- Timely availability of status updates,

- Transparent and consistent data model (EAGLE) that enables combined
  use with other land cover and thematic datasets, and

- Open and documented production system and data quality.

From the above, CLCplus Backbone enables applications in the following
domains – among others (see also
<a href="#sec-thematic-application-areas"
class="quarto-xref">Section 5.2</a>):

- Traditional land cover monitoring incl. spatial assessments and
  planning,

- Transnational resource management (e.g. catchment hydrology) and
  conservation,

- Environmental policy monitoring and reporting at different spatial
  scales,

- Support to large-scale economic modelling and risk assessment
  (e.g. natural capital, climate vulnerability),

- Model parametrization and improved spatial-temporal estimation of
  meteorological land surface variables.

## Use case on climate change mitigation and the policy support for LULUCF via the CLCplus LULUCF Instance

Countries reporting to the United Nations Framework Convention on
Climate Change (UNFCCC) must prepare annual National Inventory Reports
of their greenhouse gas emissions, reporting on six land use categories
(Forestland, Cropland, Grassland, Wetland, Settlements, Other land) and
changes from one to the other. In addition, reporting contains detailed
information on subcategories (in total: 26 classes) that exceed a
threshold share of the countries’ reported greenhouse gas emissions. In
the European Union, the activities are governed by the Regulation on the
Inclusion of Greenhouse Gas emissions and Removals from Land Use, Land
Use Change and Forestry (LULUCF) (European Commission, 2018, 2023).
CLCplus Backbone supports the implementation of the LULUCF Regulation by
readily providing the baseline land cover information that is ingested
to the CLCplus Core database. Within CLCplus Core, CLCplus Backbone land
cover and other geospatial datasets (e.g. from CLMS, national datasets)
are harmonized using the EAGLE data model and combined to extract
geospatial datasets with tailored thematic content at 100m. In the
context of LULUCF, the derived CLCplus LULUCF Instance, serves as an
operationally produced, independent geospatial proxy to LULUCF reporting
from EU member states.

## Thematic application areas

**Environmental Monitoring**

- **Habitat Assessment**: Conservationists and ecologists will find it
  useful to apply CLCplus Backbone to assess the distribution of certain
  habitats that can be related to land cover, helping to monitor their
  health and biodiversity.

- **Water Quality Assessment**: CLCplus Backbone can be used to identify
  areas with a high risk of water pollution, such as areas of
  agricultural activity or urban development.

**Agriculture and Forestry**

- **Crop Management**: Farmers and agricultural researchers can use
  CLCplus Backbone to monitor and relate land cover information to
  aspects of land management and potentially land use and to assess
  e.g. the suitability of land for specific crops.

- **Forest Management**: Foresters can use CLCplus Backbone to monitor
  the patterns and extent of different basic tree covers, aiding in
  sustainable forestry practices and combating illegal logging.

**Natural Disaster Management**

- **Flood Risk Assessment**: CLCplus Backbone can help to identify
  flood-prone areas and design flood mitigation strategies.

- **Wildfire Risk Assessment**: CLCplus Backbone may be useful to assess
  the risk of wildfires by identifying landscape patterns of vegetation
  structure or urban-rural interfaces.

**Climate Change Studies**

- **Carbon Sequestration**: Researchers can use CLCplus Backbone to
  estimate the potential for carbon sequestration in different land
  cover types, aiding in climate change mitigation efforts.

- **Climate Adaptation**: Urban heat island studies will benefit from
  CLCplus Backbone to analyse the impact of land cover on local
  temperatures and recommend adaptation strategies in cities.

**Infrastructure Development**

- **Energy Planning**: CLCplus Backbone can help energy companies and
  communities to identify suitable areas for renewable energy projects
  such as wind farms and solar installations.

- **Industrial Site Selection**: Businesses and communities could use
  CLCplus Backbone to assist assessments on the suitability of locations
  for industrial facilities based on land cover and other data sources.

**Tourism and Recreation**

- **Tourism Planning**: Tourism agencies may find CLCplus Backbone
  useful to identify areas of natural beauty or recreational value,
  helping to promote tourism and outdoor activities.

- **Nature Conservation**: Conservation organizations can use CLCplus
  Backbone to identify and protect areas of ecological importance.

**Research and Education**

- **Academic Research**: Researchers across various disciplines will
  befit from CLCplus Backbone to study land cover dynamics and their
  implications for the environment and society.

- **Educational Tools**: CLCplus Backbone aims to be comprehensive for
  everyone and can thus support educational materials and tools to raise
  awareness about land-related topics and phenomena as well as
  environmental concepts.

# Product description

The CLCplus Backbone 2023 product comprises an updated layer of the main
land cover raster layer, as well as three auxiliary layers (see
<a href="#fig-figure1" class="quarto-xref">Figure 1</a>).

<div id="fig-figure1">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-3ae7a950b89b88ab5164a45a96c174e993f664d9.png"
style="width:3.08in"
data-fig-alt="This diagram illustrates the structure and accompanying layers of the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone (BB) Raster Update product for 2023. The primary product, the CLCplus BB Raster Update 2023, is characterised by 11 land cover classes and a 10-metre spatial resolution. Associated with this main product are three complementary layers: a Confidence Layer, a Data Score Layer, and a Post-Processing Layer."
alt="This diagram illustrates the structure and accompanying layers of the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone (BB) Raster Update product for 2023. The primary product, the CLCplus BB Raster Update 2023, is characterised by 11 land cover classes and a 10-metre spatial resolution. Associated with this main product are three complementary layers: a Confidence Layer, a Data Score Layer, and a Post-Processing Layer." />

Figure 1: Overview of CLCplus Backbone layers produced for the reference
year 2023

</div>

This diagram illustrates the structure and accompanying layers of the
Copernicus Land Monitoring Service (CLMS) CLCplus Backbone (BB) Raster
Update product for 2023. The primary product, the CLCplus BB Raster
Update 2023, is characterised by 11 land cover classes and a 10-metre
spatial resolution. Associated with this main product are three
complementary layers: a Confidence Layer, a Data Score Layer, and a
Post-Processing Layer.

The following subchapters describe each of the layers, including
detailed technical specifications.

## CLCplus Backbone 2023 Raster

The following chapter describes the CLCplus Backbone 2023 raster layer
(RAS), its technical specifications
(<a href="#sec-technical-specifications-of-CLCplus-Backbone-2023"
class="quarto-xref">Section 6.1.1</a>), as well as the nomenclature
(<a href="#sec-nomenclature-concept-and-class-definitions"
class="quarto-xref">Section 6.1.2</a>), the decision tree for the class
assignment (<a href="#sec-decision-tree-for-area-thresholds"
class="quarto-xref">Section 6.1.3</a>) and provides some examples for
the class assignment (<a href="#sec-examples-for-class-assignment"
class="quarto-xref">Section 6.1.4</a>).

The CLCplus Backbone 2023 is a 10m pixel-based land cover map (see
<a href="#fig-figure2" class="quarto-xref">Figure 2</a>) based on
Sentinel-2 (S-2) data for the reference year 2023 ±3 months. The product
has no defined MMU but maps the dominant land cover among 11 thematic
land cover classes (see Table 2) for individual raster cells (i.e. 1
pixel = 10 x 10m = 100m²). The applied class nomenclature is based on
the EAGLE Land Cover Components (LCC), whereas there are slight
deviations for some classes, as described in detail in chapter
<a href="#sec-nomenclature-concept-and-class-definitions"
class="quarto-xref">Section 6.1.2</a>. CLCplus Backbone 2023 is
available for the territory of the 38 EEA member and cooperating
countries and the United Kingdom (i.e. EEA38 + UK), including the French
DOMs, and maps an area of approximately 6 million km².

Table 2: Thematic raster classes of CLCplus Backbone 2023, their class
codes and colours
<img src="CLCplus_Backbone_2023_PUM_v1-media/Table2.png"
style="width:3.59in"
data-fig-alt="This table presents the 11 thematic raster classes used in the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone product, as defined for the reference year 2023. Each entry includes a &#39;Class code and colour&#39; and a &#39;Class Name&#39;. | Class code and colour | Class Name | | :-------------------- | :-------------------------------- | | 1 (Red) | Sealed | | 2 (Dark Forest Green) | Woody needle leaved trees | | 3 (Lime Green) | Woody broadleaved deciduous trees | | 4 (Bright Green) | Woody broadleaved evergreen trees | | 5 (Brown) | Low-growing woody plants | | 6 (Pale Yellow-Green) | Permanent herbaceous | | 7 (Yellow) | Periodically herbaceous | | 8 (Magenta) | Lichens and mosses | | 9 (Grey) | Non- and sparsely vegetated | | 10 (Blue) | Water | | 11 (Cyan) | Snow and ice | The table serves as a categorical legend for the main land cover raster layer of the CLCplus Backbone 2023 product, classifying various land cover types from sealed surfaces to water and snow/ice." />

This table presents the 11 thematic raster classes used in the
Copernicus Land Monitoring Service (CLMS) CLCplus Backbone product, as
defined for the reference year 2023. Each entry includes a “Class code
and colour” and a “Class Name”.

| Class code and colour | Class Name                        |
|:----------------------|:----------------------------------|
| 1 (Red)               | Sealed                            |
| 2 (Dark Forest Green) | Woody needle leaved trees         |
| 3 (Lime Green)        | Woody broadleaved deciduous trees |
| 4 (Bright Green)      | Woody broadleaved evergreen trees |
| 5 (Brown)             | Low-growing woody plants          |
| 6 (Pale Yellow-Green) | Permanent herbaceous              |
| 7 (Yellow)            | Periodically herbaceous           |
| 8 (Magenta)           | Lichens and mosses                |
| 9 (Grey)              | Non- and sparsely vegetated       |
| 10 (Blue)             | Water                             |
| 11 (Cyan)             | Snow and ice                      |

The table serves as a categorical legend for the main land cover raster
layer of the CLCplus Backbone 2023 product, classifying various land
cover types from sealed surfaces to water and snow/ice.

<div id="fig-figure2">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-9df408152771d42bb0f22ad96081a803854b9e76.png"
style="width:6.27in"
data-fig-alt="Choropleth map displaying the main land cover raster layer from the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone 2023 product for Europe, with a reference year of 2023. The map covers a geographical area from approximately 10°W to 40°E longitude and 30°N to 60°N latitude, including specific insets for Azores Is. and Canary and Madeira Is. The map uses a colour-coded legend to represent 11 distinct land cover types: * Red: Sealed * Dark Green: Woody needle leaved trees * Light Green: Woody broadleaved deciduous trees * Brown: Woody broadleaved evergreen trees * Light Brown: Low-growing woody plants * Yellow: Permanent herbaceous * Pink: Periodically herbaceous * Light Pink/Purple: Lichens and mosses * Grey: Non and sparsely vegetated * Blue: Water * Light Blue/Cyan: Snow and ice The spatial pattern reveals a predominance of woody needle leaved trees (dark green) in Northern Europe (Scandinavia) and woody broadleaved deciduous trees (light green) across much of Central and Western Europe. Permanent herbaceous land (yellow) is widespread, particularly in agricultural regions and parts of Southern Europe. Sealed surfaces (red) appear as small, concentrated areas indicating urbanisation. Low-growing woody plants (light brown) are more visible in Mediterranean regions. Water bodies (blue) are distributed throughout. Iceland shows significant areas of lichens and mosses and non and sparsely vegetated land. A scale bar indicates distances of 0, 250, 500, and 1,000 km."
alt="Choropleth map displaying the main land cover raster layer from the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone 2023 product for Europe, with a reference year of 2023. The map covers a geographical area from approximately 10°W to 40°E longitude and 30°N to 60°N latitude, including specific insets for Azores Is. and Canary and Madeira Is. The map uses a colour-coded legend to represent 11 distinct land cover types: * Red: Sealed * Dark Green: Woody needle leaved trees * Light Green: Woody broadleaved deciduous trees * Brown: Woody broadleaved evergreen trees * Light Brown: Low-growing woody plants * Yellow: Permanent herbaceous * Pink: Periodically herbaceous * Light Pink/Purple: Lichens and mosses * Grey: Non and sparsely vegetated * Blue: Water * Light Blue/Cyan: Snow and ice The spatial pattern reveals a predominance of woody needle leaved trees (dark green) in Northern Europe (Scandinavia) and woody broadleaved deciduous trees (light green) across much of Central and Western Europe. Permanent herbaceous land (yellow) is widespread, particularly in agricultural regions and parts of Southern Europe. Sealed surfaces (red) appear as small, concentrated areas indicating urbanisation. Low-growing woody plants (light brown) are more visible in Mediterranean regions. Water bodies (blue) are distributed throughout. Iceland shows significant areas of lichens and mosses and non and sparsely vegetated land. A scale bar indicates distances of 0, 250, 500, and 1,000 km." />

Figure 2: CLCplus Backbone 2023 for the EEA38+UK (note: French DOMs are
not shown)

</div>

Choropleth map displaying the main land cover raster layer from the
Copernicus Land Monitoring Service (CLMS) CLCplus Backbone 2023 product
for Europe, with a reference year of 2023. The map covers a geographical
area from approximately 10°W to 40°E longitude and 30°N to 60°N
latitude, including specific insets for Azores Is. and Canary and
Madeira Is.

The map uses a colour-coded legend to represent 11 distinct land cover
types: \* Red: Sealed \* Dark Green: Woody needle leaved trees \* Light
Green: Woody broadleaved deciduous trees \* Brown: Woody broadleaved
evergreen trees \* Light Brown: Low-growing woody plants \* Yellow:
Permanent herbaceous \* Pink: Periodically herbaceous \* Light
Pink/Purple: Lichens and mosses \* Grey: Non and sparsely vegetated \*
Blue: Water \* Light Blue/Cyan: Snow and ice

The spatial pattern reveals a predominance of woody needle leaved trees
(dark green) in Northern Europe (Scandinavia) and woody broadleaved
deciduous trees (light green) across much of Central and Western Europe.
Permanent herbaceous land (yellow) is widespread, particularly in
agricultural regions and parts of Southern Europe. Sealed surfaces (red)
appear as small, concentrated areas indicating urbanisation. Low-growing
woody plants (light brown) are more visible in Mediterranean regions.
Water bodies (blue) are distributed throughout. Iceland shows
significant areas of lichens and mosses and non and sparsely vegetated
land. A scale bar indicates distances of 0, 250, 500, and 1,000 km.

### Technical specifications of CLCplus Backbone 2023

#### Download content

CLCplus Backbone 2023 is available as 100 x 100km tiles, based on the
EEA grid. Each of the tiles has a unique identifier, referring to its
spatial extent (e.g. ‘E44N36’). In total, the EEA38+UK is represented by
897 raster tiles, each of them accompanied by an INSPIRE compliant
metadata file (.xml) and an attribute table in aux.xml format. For tile
E44N36 for example the following files are available:

- Raster classification file:
  *CLMS_CLCPLUS_RAS_S2023_R10m_E44N36_03035_V01_R00.tif*

- Attribute table file:
  *CLMS_CLCPLUS_RAS_S2023_R10m_E44N36_03035_V01_R00.tif.aux.xml*

- Metadata file: *CLMS_CLCPLUS_RAS_S2023_R10m_E44N36_03035_V01_R00.xml*

Additionally, symbology files in .lyr, .qml and .sld are available in
order to ease the visualization in specific software applications.

<div id="fig-figure3">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-66b2331d63fc430e212e30aa8999c547d0b8dc82.png"
style="width:6.27in"
data-fig-alt="This is a 10-meter pixel-based land cover map, part of the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone 2023 raster layer, showing a coastal region within the E44N36 grid tile. The map displays 12 thematic land cover classes, as well as an &#39;Outside area&#39; class. The legend, with colour codes and descriptions, is as follows: * Sealed (red) * Woody needle leaved trees (dark green) * Woody broadleaved deciduous trees (medium green) * Woody broadleaved evergreen trees (light green) * Low-growing woody plants (dark olive green) * Permanent herbaceous (light yellow) * Periodically herbaceous (yellow-orange) * Lichens and mosses (pink) * Non and sparsely vegetated (light grey-green) * Water (dark blue) * Snow and ice (light blue) * Coastal seawater buffer (very light blue-grey) * Outside area (light grey) The map depicts a variegated landscape dominated by Permanent herbaceous (light yellow) and Woody broadleaved deciduous trees (medium green). Significant areas of Sealed surfaces (red) are concentrated on the largest landmass in the south-eastern part of the tile. Multiple inland Water bodies (dark blue) are visible. The map includes a scale bar indicating distances of 0, 10, and 20 km. Coordinate grid lines are shown, with a horizontal line labeled &#39;0°0&#39;N&#39; and a vertical line, likely &#39;0°0&#39;E&#39; at the top edge, indicating a local grid origin. The grey areas surrounding the mapped region are designated as &#39;Outside area.&#39;"
alt="This is a 10-meter pixel-based land cover map, part of the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone 2023 raster layer, showing a coastal region within the E44N36 grid tile. The map displays 12 thematic land cover classes, as well as an &#39;Outside area&#39; class. The legend, with colour codes and descriptions, is as follows: * Sealed (red) * Woody needle leaved trees (dark green) * Woody broadleaved deciduous trees (medium green) * Woody broadleaved evergreen trees (light green) * Low-growing woody plants (dark olive green) * Permanent herbaceous (light yellow) * Periodically herbaceous (yellow-orange) * Lichens and mosses (pink) * Non and sparsely vegetated (light grey-green) * Water (dark blue) * Snow and ice (light blue) * Coastal seawater buffer (very light blue-grey) * Outside area (light grey) The map depicts a variegated landscape dominated by Permanent herbaceous (light yellow) and Woody broadleaved deciduous trees (medium green). Significant areas of Sealed surfaces (red) are concentrated on the largest landmass in the south-eastern part of the tile. Multiple inland Water bodies (dark blue) are visible. The map includes a scale bar indicating distances of 0, 10, and 20 km. Coordinate grid lines are shown, with a horizontal line labeled &#39;0°0&#39;N&#39; and a vertical line, likely &#39;0°0&#39;E&#39; at the top edge, indicating a local grid origin. The grey areas surrounding the mapped region are designated as &#39;Outside area.&#39;" />

Figure 3: CLCplus Backbone 2023 for tile E44N36 (Copenhagen)

</div>

This is a 10-meter pixel-based land cover map, part of the Copernicus
Land Monitoring Service (CLMS) CLCplus Backbone 2023 raster layer,
showing a coastal region within the E44N36 grid tile. The map displays
12 thematic land cover classes, as well as an “Outside area” class. The
legend, with colour codes and descriptions, is as follows: \* Sealed
(red) \* Woody needle leaved trees (dark green) \* Woody broadleaved
deciduous trees (medium green) \* Woody broadleaved evergreen trees
(light green) \* Low-growing woody plants (dark olive green) \*
Permanent herbaceous (light yellow) \* Periodically herbaceous
(yellow-orange) \* Lichens and mosses (pink) \* Non and sparsely
vegetated (light grey-green) \* Water (dark blue) \* Snow and ice (light
blue) \* Coastal seawater buffer (very light blue-grey) \* Outside area
(light grey)

The map depicts a variegated landscape dominated by Permanent herbaceous
(light yellow) and Woody broadleaved deciduous trees (medium green).
Significant areas of Sealed surfaces (red) are concentrated on the
largest landmass in the south-eastern part of the tile. Multiple inland
Water bodies (dark blue) are visible. The map includes a scale bar
indicating distances of 0, 10, and 20 km. Coordinate grid lines are
shown, with a horizontal line labeled ‘0°0’N’ and a vertical line,
likely ‘0°0’E’ at the top edge, indicating a local grid origin. The grey
areas surrounding the mapped region are designated as “Outside area.”

<a href="#fig-figure3" class="quarto-xref">Figure 3</a> displays a
single tile (E44N36) of the CLCplus Backbone 2023, showing the area
around Copenhagen. Besides the tiles for the EEA38+UK extent, the
CLCplus Backbone 2023 is available in the national projections for the
French DOMs.

#### File naming convention

The filenames for the CLCplus Backbone 2023 are composed of the
following elements:

*Prefix_DataTheme_DataSub-Theme_TemporalReference_DataTypeSpatialResolution_SpatialExtent_EPSGCode_VersionNumber_RevisionNumber*

**➔ CLMS_CLCPLUS_RAS_S2023_R10m_EXXNXX_03035_V01_R00**

Where:

|  |  |
|----|----|
| Prefix: CLMS | SpatialResolution (SpatialResolutionUnit): 10m |
| DataTheme: CLCPLUS | SpatialExtent: EXXNXX or GF, GP, MQ, RE, YT for French DOMs |
| DataSub-Theme: RAS | EPSGCode: 03035 (or EPSG codes for national projections of DOMs) |
| TemporalReference: S2023 | VersionNumber: V01 |
| DataType: R; V | RevisionNumber: R00 |

The product specifications for the CLCplus Backbone for the reference
year 2023 are summarized in Table 3. Further product details and
information on nomenclature etc. can be found in the following
sub-sections.

Table 3: Technical specifications of the CLCplus Backbone

| CLCplus Backbone Raster / Acronym: RAS / Product family: CLMS_CLCplus |
|----|
| **Summary**: CLCplus Backbone is a spatially detailed, large scale, EO-based land cover inventory. The CLCplus Backbone RAS layer is a 10m pixel-based land cover map based on a Sentinel-2 time series from October 2022 to March 2024 and auxiliary features. For each pixel it shows the dominant land cover among the 11 basic land cover classes |
| **Reference year**: 2023 |
| **Geometric resolution**: Pixel resolution 10m x 10m, fully conform with the EEA reference grid |
| **Coordinate Reference System**: European ETRS89 LAEA projection / WGS84 and the respective UTM zone for French DOMs |
| **Coverage**: 6.002.105 km² (covering the full EEA38 + UK) |
| **Geometric accuracy (positioning scale)**: Equals Sentinel-2 positional accuracy in 2023 (\<9m at 95.5 % confidence level) |
| **Thematic accuracy**: 90 % overall accuracy, not more than 15 % omission errors and 15 % commission errors per class (the amount of omission and commission errors for particular difficult classes such as Low-growing woody plants and Lichens and Mosses might regionally exceed those thresholds) |
| **Data type**: 8bit unsigned raster with LZW compression |
| **Minimum Mapping Unit (MMU)**: Pixel-based (no MMU) |
| **Necessary attributes**: Value, Count, Class_name, Area_km2, Area_perc |
| **Raster coding (thematic pixel values)**: <br> 1: Sealed <br> 2: Woody needle leaved trees <br> 3: Woody broadleaved deciduous trees <br> 4: Woody broadleaved evergreen trees <br> 5: Low-growing woody plants <br> 6: Permanent herbaceous <br> 7: Periodically herbaceous <br> 8: Lichens and mosses <br> 9: Non and sparsely vegetated <br> 10: Water <br> 11: Snow and ice <br> 253: Coastal seawater buffer <br> 254: Outside area <br> 255: No data |
| **Metadata**: XML metadata files according to INSPIRE metadata standards |
| **Delivery format**: Cloud optimized GeoTIFFs as 100x100km tiles incl. pyramids and embedded colour map (\*.tif), attribute table (\*.aux.xml), and INSPIRE-compliant metadata in XML format (\*.xml) |

### Nomenclature concept and class definitions

Most of the class definitions for the CLCplus Backbone 2023 comprise a
50% area threshold to express that the dominant land cover should be
assigned. While this is a plausible approach there are many situations
where the land cover within a single 10m pixel comprises a spatial mix
of different classes and no single class reaches an absolute majority of
50%. A simple example is provided in
<a href="#fig-figure4" class="quarto-xref">Figure 4</a>.

<div id="fig-figure4">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-0f13569c926a8fcffb56ce87a86f6969e7efe854.png"
style="width:2.63in"
data-fig-alt="This conceptual map illustrates the spatial distribution of three basic land cover types within an unspecified square area, likely representing a pixel or larger land unit in a land cover inventory like the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone. The land cover types are colour-coded and labelled: &#39;Woody&#39; areas are depicted in dark green and are located in the top right portion of the square. &#39;Permanent herbaceous&#39; areas are shown in light green, forming a diagonal band that separates the &#39;Woody&#39; and &#39;Water&#39; areas. &#39;Water&#39; areas are represented in blue and occupy the bottom left portion of the square. The boundaries between these land cover classes are curved. The map lacks a scale bar, compass, or specific geographic reference."
alt="This conceptual map illustrates the spatial distribution of three basic land cover types within an unspecified square area, likely representing a pixel or larger land unit in a land cover inventory like the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone. The land cover types are colour-coded and labelled: &#39;Woody&#39; areas are depicted in dark green and are located in the top right portion of the square. &#39;Permanent herbaceous&#39; areas are shown in light green, forming a diagonal band that separates the &#39;Woody&#39; and &#39;Water&#39; areas. &#39;Water&#39; areas are represented in blue and occupy the bottom left portion of the square. The boundaries between these land cover classes are curved. The map lacks a scale bar, compass, or specific geographic reference." />

Figure 4: Exemplary 10x10m plot illustration of a situation where no
single land cover class covers 50% of the area

</div>

This conceptual map illustrates the spatial distribution of three basic
land cover types within an unspecified square area, likely representing
a pixel or larger land unit in a land cover inventory like the
Copernicus Land Monitoring Service (CLMS) CLCplus Backbone. The land
cover types are colour-coded and labelled: “Woody” areas are depicted in
dark green and are located in the top right portion of the square.
“Permanent herbaceous” areas are shown in light green, forming a
diagonal band that separates the “Woody” and “Water” areas. “Water”
areas are represented in blue and occupy the bottom left portion of the
square. The boundaries between these land cover classes are curved. The
map lacks a scale bar, compass, or specific geographic reference.

To address this issue, a relative majority is used in most cases for the
class assignment. This logic is implemented in detail through a decision
tree approach (see
<a href="#fig-figure6" class="quarto-xref">Figure 6</a>) which does not
only define the area threshold but further clarifies and limits for each
class the EAGLE Land Cover Component (see
<a href="#fig-figure5" class="quarto-xref">Figure 5</a>) and EAGLE Land
Characteristics (LCH, where needed) considered with the evaluation of
the area threshold. The approach is detailed in section
<a href="#sec-decision-tree-for-area-thresholds"
class="quarto-xref">Section 6.1.3</a>. In general, the area fractions of
different land cover classes are to be understood as what can be
reasonably evaluated in HR and VHR remote sensing imagery at nadir.

<div id="fig-figure5">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-eeda59c50bb28bb4c441bd411b0a293d236bdfac.png"
style="width:6.27in"
data-fig-alt="This diagram presents a hierarchical classification of Land Cover Components structured across five levels, from broad categories to specific land cover types. **Level 1** divides land cover into three broad, colour-coded categories: 1. **Abiotic, Non-Vegetated Surfaces and Objects** (red) 2. **Biotic, Vegetation** (green) 3. **Water** (blue) **Level 2** refines these categories: - **Abiotic, Non-Vegetated Surfaces and Objects** is subdivided into: Artificial Surfaces and Constructions, and Natural Material Surfaces. - **Biotic, Vegetation** is subdivided into: Woody Vegetation, Herbaceous Vegetation, and Lichens, Mosses, Algae. - **Water** is subdivided into: Liquid Water Bodies, and Solid Waters. **Level 3** provides further detail: - Under **Artificial Surfaces and Constructions**: Sealed Artificial Surfaces and Constructions, and Non-Sealed Artificial Surfaces. - Under **Natural Material Surfaces**: Consolidated Surfaces, and Unconsolidated Surfaces. - Under **Woody Vegetation**: Trees, and Bushes, Shrubs. - Under **Herbaceous Vegetation**: Graminoids, Grass-Like, and Non-Graminoids, Succulen. - Under **Lichens, Mosses, Algae**: Lichens, Mosses, and Algae. - Under **Liquid Water Bodies**: Inland Water Bodies, and Marine Waters. - Under **Solid Waters**: Snow, and Ice, Glaciers. **Level 4** expands on selected Level 3 categories: - Under **Sealed Artificial Surfaces and Constructions**: Buildings, Specific Structures and Facilities, and Open Sealed Surfaces. - Under **Non-Sealed Artificial Surfaces**: Open Non-Sealed Artificial Surfaces, and Waste Materials. - Under **Consolidated Surfaces**: Bare Rock, and Hard Pan. - Under **Unconsolidated Surfaces**: Mineral Fragments, Bare Soils, and Natural Deposits. - Under **Bushes, Shrubs**: Regular Bushes, and Dwarf Shrubs. - Under **Graminoids, Grass-Like**: Grasses, Sedges, Rushes, Cereals, and Reeds, Bamboos, Canes. - Under **Algae**: Macro Algae, and Micro Algae, Plankton. - Under **Inland Water Bodies**: Water Course, and Standing Water. **Level 5** offers the most granular classification for specific categories: - Under **Buildings**: Conventional Buildings, and Specific Buildings. - Under **Mineral Fragments**: Boulders, Stones, Pebbles, Gravel, Tuff; Sand, Grit; Clay, Silt; and Mixed Unsorted Material. - Under **Natural Deposits**: Inorganic Deposits, and Organic Deposits, Peat. - Under **Grasses, Sedges, Rushes, Cereals**: Poaceae, Grasses, Cereals, and Cyperaceae, Sedges, Rushes."
alt="This diagram presents a hierarchical classification of Land Cover Components structured across five levels, from broad categories to specific land cover types. **Level 1** divides land cover into three broad, colour-coded categories: 1. **Abiotic, Non-Vegetated Surfaces and Objects** (red) 2. **Biotic, Vegetation** (green) 3. **Water** (blue) **Level 2** refines these categories: - **Abiotic, Non-Vegetated Surfaces and Objects** is subdivided into: Artificial Surfaces and Constructions, and Natural Material Surfaces. - **Biotic, Vegetation** is subdivided into: Woody Vegetation, Herbaceous Vegetation, and Lichens, Mosses, Algae. - **Water** is subdivided into: Liquid Water Bodies, and Solid Waters. **Level 3** provides further detail: - Under **Artificial Surfaces and Constructions**: Sealed Artificial Surfaces and Constructions, and Non-Sealed Artificial Surfaces. - Under **Natural Material Surfaces**: Consolidated Surfaces, and Unconsolidated Surfaces. - Under **Woody Vegetation**: Trees, and Bushes, Shrubs. - Under **Herbaceous Vegetation**: Graminoids, Grass-Like, and Non-Graminoids, Succulen. - Under **Lichens, Mosses, Algae**: Lichens, Mosses, and Algae. - Under **Liquid Water Bodies**: Inland Water Bodies, and Marine Waters. - Under **Solid Waters**: Snow, and Ice, Glaciers. **Level 4** expands on selected Level 3 categories: - Under **Sealed Artificial Surfaces and Constructions**: Buildings, Specific Structures and Facilities, and Open Sealed Surfaces. - Under **Non-Sealed Artificial Surfaces**: Open Non-Sealed Artificial Surfaces, and Waste Materials. - Under **Consolidated Surfaces**: Bare Rock, and Hard Pan. - Under **Unconsolidated Surfaces**: Mineral Fragments, Bare Soils, and Natural Deposits. - Under **Bushes, Shrubs**: Regular Bushes, and Dwarf Shrubs. - Under **Graminoids, Grass-Like**: Grasses, Sedges, Rushes, Cereals, and Reeds, Bamboos, Canes. - Under **Algae**: Macro Algae, and Micro Algae, Plankton. - Under **Inland Water Bodies**: Water Course, and Standing Water. **Level 5** offers the most granular classification for specific categories: - Under **Buildings**: Conventional Buildings, and Specific Buildings. - Under **Mineral Fragments**: Boulders, Stones, Pebbles, Gravel, Tuff; Sand, Grit; Clay, Silt; and Mixed Unsorted Material. - Under **Natural Deposits**: Inorganic Deposits, and Organic Deposits, Peat. - Under **Grasses, Sedges, Rushes, Cereals**: Poaceae, Grasses, Cereals, and Cyperaceae, Sedges, Rushes." />

Figure 5: Levels 1-5 of the EAGLE Land Cover Components (LCC) v3.21. The
hierarchical levels allow for resolving the LCC assignment in the most
suitable way. In case level 1 is too general, the most suitable lower
level is chosen

</div>

This diagram presents a hierarchical classification of Land Cover
Components structured across five levels, from broad categories to
specific land cover types.

**Level 1** divides land cover into three broad, colour-coded
categories: 1. **Abiotic, Non-Vegetated Surfaces and Objects** (red) 2.
**Biotic, Vegetation** (green) 3. **Water** (blue)

**Level 2** refines these categories: - **Abiotic, Non-Vegetated
Surfaces and Objects** is subdivided into: Artificial Surfaces and
Constructions, and Natural Material Surfaces. - **Biotic, Vegetation**
is subdivided into: Woody Vegetation, Herbaceous Vegetation, and
Lichens, Mosses, Algae. - **Water** is subdivided into: Liquid Water
Bodies, and Solid Waters.

**Level 3** provides further detail: - Under **Artificial Surfaces and
Constructions**: Sealed Artificial Surfaces and Constructions, and
Non-Sealed Artificial Surfaces. - Under **Natural Material Surfaces**:
Consolidated Surfaces, and Unconsolidated Surfaces. - Under **Woody
Vegetation**: Trees, and Bushes, Shrubs. - Under **Herbaceous
Vegetation**: Graminoids, Grass-Like, and Non-Graminoids, Succulen. -
Under **Lichens, Mosses, Algae**: Lichens, Mosses, and Algae. - Under
**Liquid Water Bodies**: Inland Water Bodies, and Marine Waters. - Under
**Solid Waters**: Snow, and Ice, Glaciers.

**Level 4** expands on selected Level 3 categories: - Under **Sealed
Artificial Surfaces and Constructions**: Buildings, Specific Structures
and Facilities, and Open Sealed Surfaces. - Under **Non-Sealed
Artificial Surfaces**: Open Non-Sealed Artificial Surfaces, and Waste
Materials. - Under **Consolidated Surfaces**: Bare Rock, and Hard Pan. -
Under **Unconsolidated Surfaces**: Mineral Fragments, Bare Soils, and
Natural Deposits. - Under **Bushes, Shrubs**: Regular Bushes, and Dwarf
Shrubs. - Under **Graminoids, Grass-Like**: Grasses, Sedges, Rushes,
Cereals, and Reeds, Bamboos, Canes. - Under **Algae**: Macro Algae, and
Micro Algae, Plankton. - Under **Inland Water Bodies**: Water Course,
and Standing Water.

**Level 5** offers the most granular classification for specific
categories: - Under **Buildings**: Conventional Buildings, and Specific
Buildings. - Under **Mineral Fragments**: Boulders, Stones, Pebbles,
Gravel, Tuff; Sand, Grit; Clay, Silt; and Mixed Unsorted Material. -
Under **Natural Deposits**: Inorganic Deposits, and Organic Deposits,
Peat. - Under **Grasses, Sedges, Rushes, Cereals**: Poaceae, Grasses,
Cereals, and Cyperaceae, Sedges, Rushes.

**Remark on the temporal dimensions of the land cover classes**: In
cases of land cover changes during the reference year and unless stated
otherwise in the class definitions below (i.e. Permanent herbaceous
vs. Periodically herbaceous, Snow and Ice), the dominant land cover
(i.e. present \>6 months per year) shall be mapped.

Textual descriptions of the main land cover components and land
characteristics included in each of the 11 classes are provided in the
following paragraphs and respective area thresholds are explained in
more detail in section 6.1.3.

**1. Sealed (CLCplus BB class code 1; EAGLE LCC 1.1.1 Sealed Artificial
Surfaces and Constructions)**

Sealed artificial surfaces include all impervious and sealed surfaces
that are covered mainly by features with a specific height above ground
(buildings and artificial constructions) or features without a specific
height above ground (flat impervious surfaces). Flat surfaces covered by
any type of impervious material that is used for artificial surface
pavements (e.g. asphalt, concrete, tarmacadam).

- Includes: All sealed artificial surfaces and constructions including
  Buildings, Specific structures and facilities, and open sealed
  surfaces (in accordance with respective EAGLE LCC). Also vegetated
  rooftops are to be mapped under this class. Deviating from the EAGLE
  LCC 1.1.1.3, railway tracks are also considered as part of this class
  since they typically comprise impervious structural elements (which
  makes them spectrally hardly separable) and a highly compacted
  subsoil. Further elements to be included are permanent and temporary
  (foil covered) greenhouses (if present for more than 50% of the
  reference year) and solar parks (if applicable, considering the area
  threshold).

- Excludes: Waste materials (e.g. communal / industrial waste),
  non-sealed and semisealed artificial surfaces (e.g. natural materials
  displaced from original place, artificially consolidated,
  e.g. logistic and storage areas, festive squares, non-vegetated sport
  fields, grass pavers, permeable paving. Such areas are to be mapped as
  Non- and sparsely vegetated since biotic land cover components do
  typically not exceed 30%.

**2. Woody – trees**

Perennial woody plants with single, self-supporting main stem or trunk,
containing woody tissue and branching into smaller branches and shoots.

| Excluded                                   | Destination class        |
|--------------------------------------------|--------------------------|
| Pinus mugo and Alnus viridis               | Low-growing woody plants |
| Ephedra                                    | Low-growing woody plants |
| Shrub forms of Taxus, Juniperus and Betula | Low-growing woody plants |
| Musa                                       | Permanent herbaceous     |

**2. 1. Woody needle leaved trees (CLCplus BB class code 2; EAGLE LCC
2.1.1, LCH 3.1.1)**

Needle leaved trees: referring to trees of the botanical group
Gymnospermae (Ford-Robertson, 1971) carrying typical needle-shaped
leaves. An exception is Ginkgo biloba which belongs to the Gymnospermae
but is considered here as Broadleaved deciduous tree.

**2. 2. Broadleaved trees (see BB classes below)**: referring to trees
of the botanical group Angiospermae, with the exception of ginkgo
(Ginkgo biloba), which belongs to the Gymnospermae taxonomically:

**2. 2. 1 Woody broadleaved deciduous trees (CLCplus BB class code 3;
EAGLE LCC 2.1.1, LCH 3.2.2)**: broadleaved trees which are leafless for
a certain period of the year;

**2. 2. 2 Woody broadleaved evergreen trees (CLCplus BB class code 4;
EAGLE LCC 2.1.1, LCH 3.2.1)**: trees that are never entirely without
green foliage (includes palm-leaved species).

**5. Low-growing woody plants (CLCplus BB class code 5; EAGLE LCC 2.1.2
Bushes, Shrubs)**

Perennial woody plants with shrub growth form, i.e. multiple stems
arising at or near the base, and height usually less than 5 metres. Leaf
type can be needle leaf, broadleaf or palm leaf, phenology is either
evergreen or deciduous, and leaf surface type can be regular or
sclerophyllous.

- Includes: regular bushes and dwarf shrubs, species such as Pinus mugo,
  Alnus viridis, shrub forms from the genus Ephedra, Taxus, Juniperus
  and Betula, and subshrubs such as Thymus spec., Salvia, Rosmarinus,
  Calluna vulgaris, Erica spec. The class also includes Vitis spec. and
  Humulus spec., which are typically permanent crops, as well as Opuntia
  ficus-indica. Individual small trees in shrub-dominated areas are
  allowed in this class.

- Excludes: Low-growing fruit trees (e.g. apple plantations), tree cover
  regrowth (e.g. after clear cuts) with sufficient density and trees in
  nurseries, which should be classified according to the definitions for
  Woody-trees (i.e. CLCplus codes 2, 3 and 4).

Remark: Due to the difficulty of differentiating class 5 Low-growing
woody plants from woody trees (class 2 Woody needle leaved trees, class
3 Woody broadleaved deciduous trees or class 4 Woody broadleaved
evergreen trees) and herbaceous vegetation (class 6 Permanent herbaceous
or class 7 Periodically herbaceous), the accuracies could be regionally
below the defined target accuracies.

**6. Permanent herbaceous (CLCplus BB class code 6; EAGLE LCC 2.2
Herbaceous Vegetation)**

Permanent herbaceous areas are characterized by a continuous vegetation
cover (i.e. \>30%areal cover) throughout a year. No bare soil occurs
within a year. These areas are either unmanaged or extensively managed
natural grasslands or permanently managed grasslands, or arable areas
with a permanent vegetation cover (e.g. fodder crops) or even set-aside
land in agriculture. For managed grasslands, the biomass will vary over
the year, depending on the number of mowing (grassland cuts) or grazing
events. The class includes regular graminaceous (grasses), reeds and
forbs, notably also natural dry grassland in Southern, South-Eastern
Europe and Turkey, as well as banana plantations (Musa spec.).

Remark: According to the Integrated Administration and Control System
(IACS) and the Land Parcel Identification System (LPIS), permanent and
managed grassland may be ploughed every 3-5 years for amelioration
purposes followed by an artificial seeding phase and a renewal of
vegetation cover, thus potentially showing a phase of bare soil within a
time frame of 5-6 years. Given that the observation period considered
for the CLCplus Backbone is 1.5 years and its focus is on land cover,
such longer-term land use patterns cannot be considered and therefore
grasslands which underwent ploughing within the reference year are
typically mapped as class 7 Periodically herbaceous.

**7. Periodically herbaceous (CLCplus BB class code 7; EAGLE LCC 2.2
Herbaceous Vegetation)**

Periodically herbaceous areas are characterized by at least one land
cover change between bare soil and herbaceous vegetation within the
observation period. Depending on the prevailing management intensities,
these areas can also have more than one land cover change within the
observation period. In many cases, the areas mapped under class 7 are
managed arable lands.

**8. Lichens and mosses (CLCplus BB class code 8; EAGLE LCC 2.4 Lichens,
Mosses, Algae)**

- Any type of lichens: composite organisms formed by a symbiotic
  relationship of a fungus and a photosynthetic partner (usually green
  algae or cyanobacteria);

- Mosses: Non-vascular plants in the land plant division Bryophyta. They
  are small (a few centimetres tall) herbaceous (non-woody) plants that
  absorb water and nutrients mainly through their leaves and but also
  photosynthesis;

- Typical vegetation class of northern European Tundra vegetation.

Remark: The mapping of this class is focused on larger areas in northern
Europe where sufficient in situ data is available. Due to the difficulty
to distinguish Lichens and Mosses from herbaceous vegetation and dwarf
shrubs lower accuracies for this class are to be expected.

**9. Non and sparsely vegetated (CLCplus BB class code 9; EAGLE LCC 1.2
Natural Material Surfaces; EAGLE LCC 1.1.2 Non-Sealed Artificial
Surfaces)**

Contains consolidated and unconsolidated materials as well as permanent
bare soils, where non-vegetated areas cover ≥70% of the land surface,
such as:

- Consolidated surfaces (rocks):

  - The rock surface is largely continuous except individual cracks in
    the consolidated material. Some areas may be covered by shallow
    layers of soil or there could be isolated pockets of soil or a
    mixture of both;

  - Examples: solid (closed) rock formations, fresh lava flows,
    quarries, mineral extraction sites, open pit mines.

- Unconsolidated surfaces (screes, sand, permanent bare soil):

  - Mineral fragments are the result of physical and chemical
    disintegration and the processes involved most often cover
    geological timespans under natural conditions. The contained
    materials accumulate on site due to sedimentary processes and/or
    human activity;

  - Includes variable particle sizes: boulders, stones, pebble, gravel,
    sand and clay

  - Examples of typical formations: mountain slope debris, gravel
    riverbanks, open pit pebble mining of fossil riverbanks or fluvial
    sediments, volcanic lapilli fields, sand dunes, sand beaches, river
    sand banks, volcanic ash.

- Permanent bare soil:

  - Mixture of mineral and organic material that is fertile enough and
    capable of sustaining plant life but continuously un-vegetated
    during the entire observation period.

- Sparsely vegetated areas:

  - Sparsely vegetated on unstable areas (stones, boulders, rubble on
    steep slopes, or anthropogenic activity), due to harsh environmental
    conditions or anthropogenic interference. Vegetation covers \<30% of
    the area.

- Any other non-sealed artificial surfaces and constructions with a
  vegetation cover \<30%.

- Organic and in-organic deposits with a vegetation cover \<30%.

**10. Water (CLCplus BB class code 10; EAGLE LCC 3.1 Liquid Water
Bodies)**

- Inland water in liquid state of aggregation, regardless of its shape,
  salinity and origin (natural or artificial);

- Includes: running water (water courses) and standing water (natural
  lakes, fishponds, man-made reservoirs, pools, irrigation ponds, etc.);

- Excludes: Seawater that is included in a buffer around the coastline.
  All water pixels beyond the coastline are classified as “coastal
  seawater buffer” (class code 253). This distinction is made to enable
  the derivation of reliable water statistics, especially for countries
  with long coastlines, where the area of seawater would distort any
  derived water statistics, otherwise. For more details on the
  methodology for the coastal seawater buffer derivation see AD-1.

Remark: Regarding the temporal coverage the area should be under water
at least 50% of the observation period; temporary ice cover of water
bodies is included.

**11. Snow and ice (CLCplus BB class code 11; LCC 3.2 Solid Waters)**

- Snow: areas covered permanently (\>90% of observation period) with
  snow throughout the year;

- Ice: persistent ice cover formed by accumulation of snow (up to 100%
  of observation period);

- and combinations of both (e.g. in case of glaciers being covered by
  snow for parts of the year).

### Decision tree for area thresholds

The CLCplus Backbone decision tree
(<a href="#fig-figure6" class="quarto-xref">Figure 6</a>) complements
the class definitions in
<a href="#sec-technical-specifications-of-CLCplus-Backbone-2023"
class="quarto-xref">Section 6.1.1</a> and the EAGLE LCC matrix (cf.
<a href="#fig-figure5" class="quarto-xref">Figure 5</a>), to ensure a
seamless definition of the classes not only for ‘pure’ pixels, but also
in cases of mixed land cover at the scale of the product’s 10m spatial
resolution. At each decision level in
<a href="#fig-figure6" class="quarto-xref">Figure 6</a>, the decision
tree defines the reference area which should be considered (blue text
next to the rhombus) and the area threshold for a specific land cover
class as percentage of the reference area (white text in rhombus).
Generally, the decision tree targets to define an unambiguous assignment
of pixels with (pure or) mixed land cover to the dominant land cover
class. In accordance with the EAGLE concept, it refers to the dominant
land cover independent of the land use. Pixels which are for example
dominated by Permanent herbaceous (class 7) land cover should be
considered as such, even though the dominant land use might be an
orchard, fruit plantation or Dehesa. Further examples are given in
sub-section <a href="#sec-examples-for-class-assignment"
class="quarto-xref">Section 6.1.4</a>.

<div id="fig-figure6">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-dc7fffd1594ddeea432815b9578cf21c994675b4.png"
style="width:6.27in"
data-fig-alt="This diagram illustrates a hierarchical decision tree for land cover classification, likely for a Copernicus Land Monitoring Service (CLMS) product such as CLC+. The classification proceeds by evaluating the percentage cover of various land components using a series of &#39;Decision threshold&#39; (diamond-shaped) nodes, leading to &#39;Resulting class&#39; (rectangular) outcomes. The process begins by considering &#39;Water U Biotic U Abiotic&#39; components: 1. **IF** &#39;Water &gt; 50%&#39; **THEN**: * **IF** &#39;Liquid water &gt; 50%&#39; **THEN** the class is &#39;Water&#39; (blue box)."
alt="This diagram illustrates a hierarchical decision tree for land cover classification, likely for a Copernicus Land Monitoring Service (CLMS) product such as CLC+. The classification proceeds by evaluating the percentage cover of various land components using a series of &#39;Decision threshold&#39; (diamond-shaped) nodes, leading to &#39;Resulting class&#39; (rectangular) outcomes. The process begins by considering &#39;Water U Biotic U Abiotic&#39; components: 1. **IF** &#39;Water &gt; 50%&#39; **THEN**: * **IF** &#39;Liquid water &gt; 50%&#39; **THEN** the class is &#39;Water&#39; (blue box)." />

Figure 6: Decision tree for the usage of area thresholds for pixels with
(pure or) spatially mixed land cover in the CLCplus Backbone

</div>

This diagram illustrates a hierarchical decision tree for land cover
classification, likely for a Copernicus Land Monitoring Service (CLMS)
product such as CLC+. The classification proceeds by evaluating the
percentage cover of various land components using a series of “Decision
threshold” (diamond-shaped) nodes, leading to “Resulting class”
(rectangular) outcomes.

The process begins by considering “Water U Biotic U Abiotic”
components: 1. **IF** “Water \> 50%” **THEN**: \* **IF** “Liquid water
\> 50%” **THEN** the class is “Water” (blue box).

### Examples for class assignment

Some concrete examples for the usage of the decision tree are provided
in the following:

Example 1 – Hypothetical example, considering the mix which was already
presented in <a href="#fig-figure4" class="quarto-xref">Figure 4</a>:

<img src="CLCplus_Backbone_2023_PUM_v1-media/Example1.png"
style="width:5.73in"
data-fig-alt="This diagram presents a decision tree for classifying land cover types based on area thresholds, exemplified by a visual representation and a sequence of conditions. The small conceptual map on the left shows three distinct land cover types: Water (blue), Permanent herbaceous (light green), and Woody (dark green). The decision tree on the right outlines a sequential classification process: 1. **IF** Water covers more than 50% of the total area sum of Water, Biotic, AND Abiotic, **THEN** it&#39;s classified as Water. **OTHERWISE** (NO, as per the example path), proceed to step 2. 2. **IF** Biotic (Woody or herbaceous vegetation) covers more than 50% of the area sum of Biotic AND Abiotic, **THEN** proceed to step 3. **OTHERWISE** (YES, as per the example path), the area is likely Abiotic or a mix where Biotic is not dominant. 3. **IF** Woody cover is more than 50% of the Biotic area sum, **THEN** it&#39;s classified as Woody. **OTHERWISE** (NO, as per the example path), proceed to step 4. 4. **IF** Herbaceous vegetation covers more than 50% of the &#39;Not Woody&#39; vegetation area sum, **THEN** proceed to step 5. **OTHERWISE** (YES, as per the example path), the area is dominated by other &#39;Not Woody&#39; vegetation. 5. **IF** Periodically herbaceous cover is more than 50% of the Herbaceous vegetation area sum, **THEN** it&#39;s classified as Periodically herbaceous. **OTHERWISE** (NO, as per the example path), proceed to step 6. 6. **IF** Permanent herbaceous cover is more than 50% of the Herbaceous vegetation area sum, **THEN** proceed to step 7. **OTHERWISE** (YES, as per the example path), the area is classified otherwise within the Herbaceous category. 7. The final classification for this specific example path (NO, YES, NO, YES, NO, YES) is &#39;Permanent herbaceous&#39;. The visual map on the left illustrates a scenario where &#39;Permanent herbaceous&#39; is the dominant land cover class, consistent with the decision tree&#39;s resulting classification." />

This diagram presents a decision tree for classifying land cover types
based on area thresholds, exemplified by a visual representation and a
sequence of conditions. The small conceptual map on the left shows three
distinct land cover types: Water (blue), Permanent herbaceous (light
green), and Woody (dark green).

The decision tree on the right outlines a sequential classification
process: 1. **IF** Water covers more than 50% of the total area sum of
Water, Biotic, AND Abiotic, **THEN** it’s classified as Water.
**OTHERWISE** (NO, as per the example path), proceed to step 2. 2.
**IF** Biotic (Woody or herbaceous vegetation) covers more than 50% of
the area sum of Biotic AND Abiotic, **THEN** proceed to step 3.
**OTHERWISE** (YES, as per the example path), the area is likely Abiotic
or a mix where Biotic is not dominant. 3. **IF** Woody cover is more
than 50% of the Biotic area sum, **THEN** it’s classified as Woody.
**OTHERWISE** (NO, as per the example path), proceed to step 4. 4.
**IF** Herbaceous vegetation covers more than 50% of the ‘Not Woody’
vegetation area sum, **THEN** proceed to step 5. **OTHERWISE** (YES, as
per the example path), the area is dominated by other ‘Not Woody’
vegetation. 5. **IF** Periodically herbaceous cover is more than 50% of
the Herbaceous vegetation area sum, **THEN** it’s classified as
Periodically herbaceous. **OTHERWISE** (NO, as per the example path),
proceed to step 6. 6. **IF** Permanent herbaceous cover is more than 50%
of the Herbaceous vegetation area sum, **THEN** proceed to step 7.
**OTHERWISE** (YES, as per the example path), the area is classified
otherwise within the Herbaceous category. 7. The final classification
for this specific example path (NO, YES, NO, YES, NO, YES) is “Permanent
herbaceous”.

The visual map on the left illustrates a scenario where ‘Permanent
herbaceous’ is the dominant land cover class, consistent with the
decision tree’s resulting classification.

Example 2 – Real world example extracted from
<a href="#fig-figure7" class="quarto-xref">Figure 7</a> (Row 2, Column
5):

<img src="CLCplus_Backbone_2023_PUM_v1-media/Example2.png"
style="width:5.73in"
data-fig-alt="This diagram illustrates a sequential decision tree for classifying land cover based on area thresholds of different components (Water, Biotic, Abiotic, Sealed). An accompanying example shows an area composed of Sealed: 0 m², Broadleaved evergreen trees: 17.54 m², Permanent herbaceous: 2.34 m², and Non-vegetated: 80.12 m². The classification process follows these steps: 1. **Water Coverage Check:** If the area covered by Water is more than 50% of the sum of Water, Biotic, and Abiotic areas, then the classification is implied to be Water. If NO, proceed to Step 2. 2. **Biotic Coverage Check (50%):** If the area covered by Biotic components is more than 50% of the sum of Biotic and Abiotic areas, then the classification is implied to be Biotic. If NO, proceed to Step 3. 3. **Sealed Coverage Check:** If the area covered by Sealed surfaces is more than 50% of the sum of Abiotic areas, then the classification is implied to be Sealed. If NO, proceed to Step 4. 4. **Biotic Coverage Check (30%):** If the area covered by Biotic components is more than 30% of the sum of Biotic and Abiotic areas, then the classification is implied to be Biotic. If NO, proceed to Step 5. 5. **Default Classification:** If all previous conditions are NO, the area is classified as &#39;Non- and sparsely-vegetated&#39;. For the example area provided (0 m² Sealed, 19.88 m² Biotic, 80.12 m² Non-vegetated/Abiotic, 0 m² Water), the process would yield &#39;Non- and sparsely-vegetated&#39; as the classification." />

This diagram illustrates a sequential decision tree for classifying land
cover based on area thresholds of different components (Water, Biotic,
Abiotic, Sealed). An accompanying example shows an area composed of
Sealed: 0 m², Broadleaved evergreen trees: 17.54 m², Permanent
herbaceous: 2.34 m², and Non-vegetated: 80.12 m². The classification
process follows these steps: 1. **Water Coverage Check:** If the area
covered by Water is more than 50% of the sum of Water, Biotic, and
Abiotic areas, then the classification is implied to be Water. If NO,
proceed to Step 2. 2. **Biotic Coverage Check (50%):** If the area
covered by Biotic components is more than 50% of the sum of Biotic and
Abiotic areas, then the classification is implied to be Biotic. If NO,
proceed to Step 3. 3. **Sealed Coverage Check:** If the area covered by
Sealed surfaces is more than 50% of the sum of Abiotic areas, then the
classification is implied to be Sealed. If NO, proceed to Step 4. 4.
**Biotic Coverage Check (30%):** If the area covered by Biotic
components is more than 30% of the sum of Biotic and Abiotic areas, then
the classification is implied to be Biotic. If NO, proceed to Step 5. 5.
**Default Classification:** If all previous conditions are NO, the area
is classified as “Non- and sparsely-vegetated”.

For the example area provided (0 m² Sealed, 19.88 m² Biotic, 80.12 m²
Non-vegetated/Abiotic, 0 m² Water), the process would yield “Non- and
sparsely-vegetated” as the classification.

Example 2 illustrates the application of the decision tree over an area
with olive groves in Southern Spain. Since the growth of the understorey
is largely suppressed (tillage and use of herbicides are common) and the
tree cover is relatively sparse, the Biotic coverage percentage for most
pixels does not exceed the 30% threshold and the pixel should hence be
considered as Non- and sparsely-vegetated (class 9). In cases where the
suppression of the herbaceous understorey is not continuous
(i.e. alteration between herbaceous cover and bare soil within one
year), such areas should be mapped as Periodically Herbaceous instead.

As illustrated in
<a href="#fig-figure7" class="quarto-xref">Figure 7</a>, the same will
apply for wide areas where such land cover characteristics are dominant,
in line with the key paradigm of the EAGLE concept to disentangle land
cover and land use.

<div id="fig-figure7">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-6da642a32873d2a2093d4a1d5bcd39ed8e6f2d52.png"
style="width:6.27in"
data-fig-alt="This image illustrates the application of CLC+ (Copernicus Land Monitoring Service CORINE Land Cover plus) land cover classification, showing an aerial view and a ground-level photograph of a rural landscape with olive groves and a road. The image is divided into four panels. The top-left panel displays an aerial photograph of a landscape featuring a road, numerous trees, and sparse reddish-brown soil. The top-right panel superimposes a grid over the aerial photograph, conceptually outlining areas as &#39;Sealed&#39; (red, the road), &#39;Permanent herbaceous&#39; (yellow, road verges/fields), and &#39;Woody broadleaved evergreen trees&#39; (green, individual tree canops). The bottom-left panel shows the same aerial view with a detailed land cover classification grid. This grid uses four colours defined by the legend at the bottom: - Red: Sealed (representing the road surface) - Green: Woody broadleaved evergreen trees (individual tree canopies) - Light green/yellow: Permanent herbaceous (sparse vegetation and field areas) - Grey: Non and sparsely vegetated (bare soil or very sparse cover). The bottom-right panel displays a ground-level photograph from &#39;© Google Street View&#39; showing a paved road with white lines, and an adjacent field of olive trees with reddish soil. The classification grids exemplify how mixed land cover at the 10m spatial resolution scale can be assigned to dominant land cover classes, as per the CLC+ backbone definitions."
alt="This image illustrates the application of CLC+ (Copernicus Land Monitoring Service CORINE Land Cover plus) land cover classification, showing an aerial view and a ground-level photograph of a rural landscape with olive groves and a road. The image is divided into four panels. The top-left panel displays an aerial photograph of a landscape featuring a road, numerous trees, and sparse reddish-brown soil. The top-right panel superimposes a grid over the aerial photograph, conceptually outlining areas as &#39;Sealed&#39; (red, the road), &#39;Permanent herbaceous&#39; (yellow, road verges/fields), and &#39;Woody broadleaved evergreen trees&#39; (green, individual tree canops). The bottom-left panel shows the same aerial view with a detailed land cover classification grid. This grid uses four colours defined by the legend at the bottom: - Red: Sealed (representing the road surface) - Green: Woody broadleaved evergreen trees (individual tree canopies) - Light green/yellow: Permanent herbaceous (sparse vegetation and field areas) - Grey: Non and sparsely vegetated (bare soil or very sparse cover). The bottom-right panel displays a ground-level photograph from &#39;© Google Street View&#39; showing a paved road with white lines, and an adjacent field of olive trees with reddish soil. The classification grids exemplify how mixed land cover at the 10m spatial resolution scale can be assigned to dominant land cover classes, as per the CLC+ backbone definitions." />

Figure 7: Illustration of the CLCplus Backbone decision tree approach to
evaluate area thresholds for mixed land cover at olive groves,
Castile-La Mancha, Spain <br> Upper left: 100x100m plot overlaid on
aerial imagery <br> Upper right: Outlines of surfaces which are covered
by Sealed, Permanent herbaceous, Broadleaved evergreen trees and Non-
and sparsely vegetated 10m pixel grid overlaid on top <br> Lower left:
Resulting class attribution of the 10m pixels when applying the
threshold of Biotic \>30% to decide between Non- and sparsely vegetated
vs. one of the vegetation classes <br> Lower right: ©Google Street View
of the area, showing the four dominant land cover classes

</div>

This image illustrates the application of CLC+ (Copernicus Land
Monitoring Service CORINE Land Cover plus) land cover classification,
showing an aerial view and a ground-level photograph of a rural
landscape with olive groves and a road. The image is divided into four
panels. The top-left panel displays an aerial photograph of a landscape
featuring a road, numerous trees, and sparse reddish-brown soil. The
top-right panel superimposes a grid over the aerial photograph,
conceptually outlining areas as “Sealed” (red, the road), “Permanent
herbaceous” (yellow, road verges/fields), and “Woody broadleaved
evergreen trees” (green, individual tree canops). The bottom-left panel
shows the same aerial view with a detailed land cover classification
grid. This grid uses four colours defined by the legend at the bottom: -
Red: Sealed (representing the road surface) - Green: Woody broadleaved
evergreen trees (individual tree canopies) - Light green/yellow:
Permanent herbaceous (sparse vegetation and field areas) - Grey: Non and
sparsely vegetated (bare soil or very sparse cover). The bottom-right
panel displays a ground-level photograph from “© Google Street View”
showing a paved road with white lines, and an adjacent field of olive
trees with reddish soil. The classification grids exemplify how mixed
land cover at the 10m spatial resolution scale can be assigned to
dominant land cover classes, as per the CLC+ backbone definitions.

Example 3 below
(<a href="#fig-figure8" class="quarto-xref">Figure 8</a>) shows the map
result for a rural area in France, illustrating some interruptions of
small linear landscape elements (rural road in this case). The apparent
omission of such narrow linear elements (e.g. narrow roads and water
courses, narrow tree lines and hedge rows) is a common feature of the
CLCplus Backbone, since a) such narrow landscape elements do often not
occupy the majority of the pixels and b) are registered in the time
series with a mixed spectral signal due to the sensor point spread
function and imprecisions in the multi-temporal spatial co-registration.

Example 4 (<a href="#fig-figure9" class="quarto-xref">Figure 9</a>)
illustrates the largely correct mapping of an area with sparse
coniferous tree cover and herbaceous understorey as class 6 (Permanent
herbaceous). While the mapping of such mixed areas might be unexpected
for some users and might not be reflected in national or regional land
cover maps, it correctly represents the dominant land cover and its
spectraltemporal properties.

Example 5 concerns the mapping of the classes Water and Snow and Ice,
which are defined according to their spatial-temporal extent throughout
the reference year, with at least 50% spatial coverage and 90%
permanence within the period. As illustrated in
<a href="#fig-figure10" class="quarto-xref">Figure 10</a> and
<a href="#fig-figure11" class="quarto-xref">Figure 11</a>, the
production has taken these thresholds into account, considering temporal
profiles of the Normalized Difference Vegetation Index (NDVI) and
Normalized Difference Snow Index (NDSI) during the generation of
training data, quality control and internal verification. It is
therefore important to note that single satellite images at deliberate
times can suggest different spatial extents for these two classes,
depending on the time of acquisition. Time-series should be consulted
for assessing the correctness of the class extents of water or snow/ice
in CLCplus Backbone products.

Example 6 (<a href="#fig-figure12" class="quarto-xref">Figure 12</a>)
illustrates the correct mapping of agricultural parcels in the
Mediterranean as class Non- and sparsely vegetated as suggested from the
underlying NDVI time series, i.e. the absence of cultivation (and
irrigation) during the main growing season (here: October - July). The
contrast is particularly clear, when compared with the temporal
trajectory of neighbouring parcels, which were cultivated in the growing
season (<a href="#fig-figure12" class="quarto-xref">Figure 12</a>).

<div id="fig-figure8">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-068eceacd6f1cfc264cf28f6dd69504dd62b4432.png"
style="width:6.27in"
data-fig-alt="The image displays a side-by-side comparison of land cover classification from the Copernicus Land Monitoring Service plus Backbone (CLCplus BB RAS) raster product with its corresponding high-resolution ESRI World Imagery. Both panels are overlaid with a grid representing spatial resolution. The left panel, labelled &#39;CLCplus BB RAS&#39;, shows a classified grid with four land cover types: * Red: &#39;Sealed&#39; surfaces, forming a diagonal feature suggesting a linear infrastructure like a road or path. * Green: &#39;Woody broadleaved deciduous trees&#39;, forming a vertical line along the right edge and some pixels in the top-right corner, indicating a tree line. * Light Green: &#39;Permanent herbaceous&#39; vegetation, visible in the bottom-left corner. * Yellow: &#39;Periodically herbaceous&#39; vegetation, covering the majority of the grid cells. The right panel, labelled &#39;ESRI World Imagery&#39;, presents the satellite imagery of the same area, showing visual evidence that correlates with the CLCplus BB RAS classification. It clearly depicts a diagonal road or track, a large agricultural field, and a distinct line of trees along the right edge, validating the classified land cover elements on the left. This comparison illustrates how CLCplus Backbone pixels, potentially representing mixed land cover, are assigned to a dominant land cover class."
alt="The image displays a side-by-side comparison of land cover classification from the Copernicus Land Monitoring Service plus Backbone (CLCplus BB RAS) raster product with its corresponding high-resolution ESRI World Imagery. Both panels are overlaid with a grid representing spatial resolution. The left panel, labelled &#39;CLCplus BB RAS&#39;, shows a classified grid with four land cover types: * Red: &#39;Sealed&#39; surfaces, forming a diagonal feature suggesting a linear infrastructure like a road or path. * Green: &#39;Woody broadleaved deciduous trees&#39;, forming a vertical line along the right edge and some pixels in the top-right corner, indicating a tree line. * Light Green: &#39;Permanent herbaceous&#39; vegetation, visible in the bottom-left corner. * Yellow: &#39;Periodically herbaceous&#39; vegetation, covering the majority of the grid cells. The right panel, labelled &#39;ESRI World Imagery&#39;, presents the satellite imagery of the same area, showing visual evidence that correlates with the CLCplus BB RAS classification. It clearly depicts a diagonal road or track, a large agricultural field, and a distinct line of trees along the right edge, validating the classified land cover elements on the left. This comparison illustrates how CLCplus Backbone pixels, potentially representing mixed land cover, are assigned to a dominant land cover class." />

Figure 8: CLCplus Backbone (CLCplus BB RAS; left) and ESRI World Imagery
(right) for a rural area in France illustrating the interruptions of
narrow linear elements which do not reach the majority per 10 m pixels
(black grid lines) and typically show mixed spectral signals in the
Sentinel-2 time series

</div>

The image displays a side-by-side comparison of land cover
classification from the Copernicus Land Monitoring Service plus Backbone
(CLCplus BB RAS) raster product with its corresponding high-resolution
ESRI World Imagery. Both panels are overlaid with a grid representing
spatial resolution.

The left panel, labelled “CLCplus BB RAS”, shows a classified grid with
four land cover types: \* Red: “Sealed” surfaces, forming a diagonal
feature suggesting a linear infrastructure like a road or path. \*
Green: “Woody broadleaved deciduous trees”, forming a vertical line
along the right edge and some pixels in the top-right corner, indicating
a tree line. \* Light Green: “Permanent herbaceous” vegetation, visible
in the bottom-left corner. \* Yellow: “Periodically herbaceous”
vegetation, covering the majority of the grid cells.

The right panel, labelled “ESRI World Imagery”, presents the satellite
imagery of the same area, showing visual evidence that correlates with
the CLCplus BB RAS classification. It clearly depicts a diagonal road or
track, a large agricultural field, and a distinct line of trees along
the right edge, validating the classified land cover elements on the
left. This comparison illustrates how CLCplus Backbone pixels,
potentially representing mixed land cover, are assigned to a dominant
land cover class.

<div id="fig-figure9">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-a93dca86901c4474ae268aa397725acf111896c1.png"
style="width:6.27in"
data-fig-alt="This image displays two gridded panels illustrating land cover classification. The left panel shows a classified land cover map with a grid overlay, depicting two land cover classes: &#39;Woody needle leaved trees&#39; (dark green) and &#39;Permanent herbaceous&#39; (light yellow/lime green). These classes are distributed in a mixed pattern across the grid cells, with a notable light yellow/lime green &#39;Permanent herbaceous&#39; area forming a large central shape. The right panel shows the corresponding underlying satellite imagery, likely in false-color infrared, also with a grid overlay. This imagery displays vibrant red and magenta tones, indicating areas of healthy vegetation with high infrared reflectance, along with some green-toned areas. Both panels are divided into a regular grid of uniform cells, illustrating pixel-based land cover analysis. This example is used to demonstrate the application of area thresholds for mixed land cover classification within the Copernicus Land Monitoring Service (CLMS) CLC+ Backbone methodology."
alt="This image displays two gridded panels illustrating land cover classification. The left panel shows a classified land cover map with a grid overlay, depicting two land cover classes: &#39;Woody needle leaved trees&#39; (dark green) and &#39;Permanent herbaceous&#39; (light yellow/lime green). These classes are distributed in a mixed pattern across the grid cells, with a notable light yellow/lime green &#39;Permanent herbaceous&#39; area forming a large central shape. The right panel shows the corresponding underlying satellite imagery, likely in false-color infrared, also with a grid overlay. This imagery displays vibrant red and magenta tones, indicating areas of healthy vegetation with high infrared reflectance, along with some green-toned areas. Both panels are divided into a regular grid of uniform cells, illustrating pixel-based land cover analysis. This example is used to demonstrate the application of area thresholds for mixed land cover classification within the Copernicus Land Monitoring Service (CLMS) CLC+ Backbone methodology." />

Figure 9: CLCplus Backbone (CLCplus BB RAS) superimposed on ESRI World
Imagery (left) and VHR IMAGE 2018 (right) for an area with sparse tree
cover in the Alps. Sparse tree canopies dominated by herbaceous
understory are largely mapped correctly as class 6

</div>

This image displays two gridded panels illustrating land cover
classification. The left panel shows a classified land cover map with a
grid overlay, depicting two land cover classes: “Woody needle leaved
trees” (dark green) and “Permanent herbaceous” (light yellow/lime
green). These classes are distributed in a mixed pattern across the grid
cells, with a notable light yellow/lime green “Permanent herbaceous”
area forming a large central shape. The right panel shows the
corresponding underlying satellite imagery, likely in false-color
infrared, also with a grid overlay. This imagery displays vibrant red
and magenta tones, indicating areas of healthy vegetation with high
infrared reflectance, along with some green-toned areas. Both panels are
divided into a regular grid of uniform cells, illustrating pixel-based
land cover analysis. This example is used to demonstrate the application
of area thresholds for mixed land cover classification within the
Copernicus Land Monitoring Service (CLMS) CLC+ Backbone methodology.

<div id="fig-figure10">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-98583661b85263bfd1ff845c5fc0d163486f6b3c.png"
style="width:6.27in"
data-fig-alt="The image presents an illustration of land cover (LC) classification and Normalised Difference Vegetation Index (NDVI) time series data for specific locations within the context of olive groves in Castile-La Mancha, Spain. The upper-left panel is a CLCplus (Copernicus Land Cover Plus) Backbone Raster (BB RAS) map, displaying a heterogeneous landscape. The legend defines 11 land cover classes by colour: Sealed (red), Woody needle leaved trees (dark green), Woody broadleaved deciduous trees (green), Woody broadleaved evergreen trees (lime green), Low-growing woody plants (brown), Permanent herbaceous (light green), Periodically herbaceous (yellow), Lichens and mosses (pink), Non and sparsely vegetated (grey), Water (blue), and Snow and ice (light blue). The visible map area shows dominant regions of Water (blue), Non and sparsely vegetated (grey), Sealed (red), and Permanent herbaceous (light green). The upper-right panel is a Sentinel-2 (S-2) seasonal composite satellite image of the same area, rendered in false colour. It features a large water body (dark blue), land areas with varying vegetation (shades of red/pink/white), and three specific locations marked by numbered boxes: 1, 2, and 3. Location 1 appears as a light-toned area adjacent to or within the water body, while locations 2 and 3 are darker, possibly engineered features within the water body. The lower three panels are line charts showing Normalised Difference Vegetation Index (NDVI) values over time, corresponding to the marked locations 1, 2, and 3 on the S-2 composite. Each chart shares the following characteristics: * The Y-axis represents NDVI values, ranging from -1.0 to 1.0, with increments of 0.2. A dotted horizontal line marks NDVI = 0. * The X-axis represents time, from May 2017 (`2017-05"
alt="The image presents an illustration of land cover (LC) classification and Normalised Difference Vegetation Index (NDVI) time series data for specific locations within the context of olive groves in Castile-La Mancha, Spain. The upper-left panel is a CLCplus (Copernicus Land Cover Plus) Backbone Raster (BB RAS) map, displaying a heterogeneous landscape. The legend defines 11 land cover classes by colour: Sealed (red), Woody needle leaved trees (dark green), Woody broadleaved deciduous trees (green), Woody broadleaved evergreen trees (lime green), Low-growing woody plants (brown), Permanent herbaceous (light green), Periodically herbaceous (yellow), Lichens and mosses (pink), Non and sparsely vegetated (grey), Water (blue), and Snow and ice (light blue). The visible map area shows dominant regions of Water (blue), Non and sparsely vegetated (grey), Sealed (red), and Permanent herbaceous (light green). The upper-right panel is a Sentinel-2 (S-2) seasonal composite satellite image of the same area, rendered in false colour. It features a large water body (dark blue), land areas with varying vegetation (shades of red/pink/white), and three specific locations marked by numbered boxes: 1, 2, and 3. Location 1 appears as a light-toned area adjacent to or within the water body, while locations 2 and 3 are darker, possibly engineered features within the water body. The lower three panels are line charts showing Normalised Difference Vegetation Index (NDVI) values over time, corresponding to the marked locations 1, 2, and 3 on the S-2 composite. Each chart shares the following characteristics: * The Y-axis represents NDVI values, ranging from -1.0 to 1.0, with increments of 0.2. A dotted horizontal line marks NDVI = 0. * The X-axis represents time, from May 2017 (`2017-05" />

Figure 10: Example of the mapping of ephemeral classes in the CLCplus
Backbone (CLCplus BB RAS). Water is mapped according to its
spatial-temporal coverage during the reference year. In the given
example from the 2018 production, areas which are more than 50% of the
reference year (blue box) covered by water (i.e. NDVI typically below 0;
dotted line), are correctly mapped as Water. Areas with shorter water
coverage show an NDVI slightly above 0 for most of the time in this
example and are correctly mapped as Non- and sparsely vegetated

</div>

The image presents an illustration of land cover (LC) classification and
Normalised Difference Vegetation Index (NDVI) time series data for
specific locations within the context of olive groves in Castile-La
Mancha, Spain.

The upper-left panel is a CLCplus (Copernicus Land Cover Plus) Backbone
Raster (BB RAS) map, displaying a heterogeneous landscape. The legend
defines 11 land cover classes by colour: Sealed (red), Woody needle
leaved trees (dark green), Woody broadleaved deciduous trees (green),
Woody broadleaved evergreen trees (lime green), Low-growing woody plants
(brown), Permanent herbaceous (light green), Periodically herbaceous
(yellow), Lichens and mosses (pink), Non and sparsely vegetated (grey),
Water (blue), and Snow and ice (light blue). The visible map area shows
dominant regions of Water (blue), Non and sparsely vegetated (grey),
Sealed (red), and Permanent herbaceous (light green).

The upper-right panel is a Sentinel-2 (S-2) seasonal composite satellite
image of the same area, rendered in false colour. It features a large
water body (dark blue), land areas with varying vegetation (shades of
red/pink/white), and three specific locations marked by numbered boxes:
1, 2, and 3. Location 1 appears as a light-toned area adjacent to or
within the water body, while locations 2 and 3 are darker, possibly
engineered features within the water body.

The lower three panels are line charts showing Normalised Difference
Vegetation Index (NDVI) values over time, corresponding to the marked
locations 1, 2, and 3 on the S-2 composite. Each chart shares the
following characteristics: \* The Y-axis represents NDVI values, ranging
from -1.0 to 1.0, with increments of 0.2. A dotted horizontal line marks
NDVI = 0. \* The X-axis represents time, from May 2017 (\`2017-05

<div id="fig-figure11">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-082a32f172f34d5101c5571c51dee124b3dd1c0c.png"
style="width:6.27in"
data-fig-alt="This image is a composite illustration showing the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone Raster (BB RAS) land cover classification, corresponding Very High Resolution (VHR) imagery, and Normalised Difference Snow Index (NDSI) time series data for two specific points. The top left panel displays a CLCplus BB RAS map. A legend below the map lists 11 land cover classes with their corresponding colours: Sealed (Red), Woody needle leaved trees (Dark green), Woody broadleaved deciduous trees (Lime green), Woody broadleaved evergreen trees (Green), Low-growing woody plants (Brown), Permanent herbaceous (Yellow), Periodically herbaceous (Light yellow), Lichens and mosses (Pink), Non and sparsely vegetated (Grey), Water (Blue), and Snow and ice (Cyan). On the map, large areas are dominated by Snow and ice (cyan) and Non and sparsely vegetated (grey), with smaller extents of Water (blue), Woody broadleaved evergreen trees (green), and Woody needle leaved trees (dark green). Two points, labelled &#39;1&#39; and &#39;2&#39;, are marked; point &#39;1&#39; is located within a Snow and ice area, and point &#39;2&#39; is within a Non and sparsely vegetated area. The top right panel presents a &#39;VHR IMAGE 2018,&#39; which is a very high resolution satellite image from 2018. It shows a mountainous or glacial landscape with bright white/light blue areas (likely snow or ice), reddish-brown and darker green tones indicating rocky or vegetated terrain, and visible water bodies. The bottom section consists of two line charts, labelled &#39;1&#39; and &#39;2&#39;, corresponding to the points on the map. Both charts display the Normalised Difference Snow Index (NDSI) on the Y-axis, ranging from 0.1 to 1.0, plotted over time on the X-axis, from May 2017 (2017-05) to September 2020 (2020-09). Each chart shows two data series: &#39;Index_orig&#39; (original NDSI values, grey dots) and &#39;Index_interp&#39; (interpolated NDSI values, represented by a blue line with empty circles). A horizontal dashed reference line is present at NDSI = 0.4. A shaded blue vertical box on both charts highlights the period from approximately January 2018 to January 2019. Chart 1, for point &#39;1&#39; (classified as Snow and ice on the map), shows the interpolated NDSI (&#39;Index_interp&#39;) consistently above the 0.4 threshold, generally ranging between 0.6 and 0.9 throughout the 2017–2020 period. Chart 2, for point &#39;2&#39; (classified as Non and sparsely vegetated on the map), exhibits strong seasonal variation. The interpolated NDSI values drop significantly below 0.4 during the summer months (e.g., reaching approximately 0.1 in late 2018 and late 2019) and rise above 0.8 in winter."
alt="This image is a composite illustration showing the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone Raster (BB RAS) land cover classification, corresponding Very High Resolution (VHR) imagery, and Normalised Difference Snow Index (NDSI) time series data for two specific points. The top left panel displays a CLCplus BB RAS map. A legend below the map lists 11 land cover classes with their corresponding colours: Sealed (Red), Woody needle leaved trees (Dark green), Woody broadleaved deciduous trees (Lime green), Woody broadleaved evergreen trees (Green), Low-growing woody plants (Brown), Permanent herbaceous (Yellow), Periodically herbaceous (Light yellow), Lichens and mosses (Pink), Non and sparsely vegetated (Grey), Water (Blue), and Snow and ice (Cyan). On the map, large areas are dominated by Snow and ice (cyan) and Non and sparsely vegetated (grey), with smaller extents of Water (blue), Woody broadleaved evergreen trees (green), and Woody needle leaved trees (dark green). Two points, labelled &#39;1&#39; and &#39;2&#39;, are marked; point &#39;1&#39; is located within a Snow and ice area, and point &#39;2&#39; is within a Non and sparsely vegetated area. The top right panel presents a &#39;VHR IMAGE 2018,&#39; which is a very high resolution satellite image from 2018. It shows a mountainous or glacial landscape with bright white/light blue areas (likely snow or ice), reddish-brown and darker green tones indicating rocky or vegetated terrain, and visible water bodies. The bottom section consists of two line charts, labelled &#39;1&#39; and &#39;2&#39;, corresponding to the points on the map. Both charts display the Normalised Difference Snow Index (NDSI) on the Y-axis, ranging from 0.1 to 1.0, plotted over time on the X-axis, from May 2017 (2017-05) to September 2020 (2020-09). Each chart shows two data series: &#39;Index_orig&#39; (original NDSI values, grey dots) and &#39;Index_interp&#39; (interpolated NDSI values, represented by a blue line with empty circles). A horizontal dashed reference line is present at NDSI = 0.4. A shaded blue vertical box on both charts highlights the period from approximately January 2018 to January 2019. Chart 1, for point &#39;1&#39; (classified as Snow and ice on the map), shows the interpolated NDSI (&#39;Index_interp&#39;) consistently above the 0.4 threshold, generally ranging between 0.6 and 0.9 throughout the 2017–2020 period. Chart 2, for point &#39;2&#39; (classified as Non and sparsely vegetated on the map), exhibits strong seasonal variation. The interpolated NDSI values drop significantly below 0.4 during the summer months (e.g., reaching approximately 0.1 in late 2018 and late 2019) and rise above 0.8 in winter." />

Figure 11: Example of the mapping of ephemeral classes in the CLCplus
Backbone (CLCplus BB RAS). Class Snow and Ice is mapped according to its
spatial-temporal coverage during the reference year. In the given
example from the 2018 production, areas which are more than 90% of the
reference year (blue box) covered by snow or ice (i.e. NDSI typically
above 0.4; dotted line), are correctly mapped as Snow and Ice. Adjacent
areas with shorter snow or ice coverage are correctly mapped as Non- and
sparsely vegetated

</div>

This image is a composite illustration showing the Copernicus Land
Monitoring Service (CLMS) CLCplus Backbone Raster (BB RAS) land cover
classification, corresponding Very High Resolution (VHR) imagery, and
Normalised Difference Snow Index (NDSI) time series data for two
specific points.

The top left panel displays a CLCplus BB RAS map. A legend below the map
lists 11 land cover classes with their corresponding colours: Sealed
(Red), Woody needle leaved trees (Dark green), Woody broadleaved
deciduous trees (Lime green), Woody broadleaved evergreen trees (Green),
Low-growing woody plants (Brown), Permanent herbaceous (Yellow),
Periodically herbaceous (Light yellow), Lichens and mosses (Pink), Non
and sparsely vegetated (Grey), Water (Blue), and Snow and ice (Cyan). On
the map, large areas are dominated by Snow and ice (cyan) and Non and
sparsely vegetated (grey), with smaller extents of Water (blue), Woody
broadleaved evergreen trees (green), and Woody needle leaved trees (dark
green). Two points, labelled ‘1’ and ‘2’, are marked; point ‘1’ is
located within a Snow and ice area, and point ‘2’ is within a Non and
sparsely vegetated area.

The top right panel presents a “VHR IMAGE 2018,” which is a very high
resolution satellite image from 2018. It shows a mountainous or glacial
landscape with bright white/light blue areas (likely snow or ice),
reddish-brown and darker green tones indicating rocky or vegetated
terrain, and visible water bodies.

The bottom section consists of two line charts, labelled ‘1’ and ‘2’,
corresponding to the points on the map. Both charts display the
Normalised Difference Snow Index (NDSI) on the Y-axis, ranging from 0.1
to 1.0, plotted over time on the X-axis, from May 2017 (2017-05) to
September 2020 (2020-09). Each chart shows two data series: ‘Index_orig’
(original NDSI values, grey dots) and ‘Index_interp’ (interpolated NDSI
values, represented by a blue line with empty circles). A horizontal
dashed reference line is present at NDSI = 0.4. A shaded blue vertical
box on both charts highlights the period from approximately January 2018
to January 2019.

Chart 1, for point ‘1’ (classified as Snow and ice on the map), shows
the interpolated NDSI (‘Index_interp’) consistently above the 0.4
threshold, generally ranging between 0.6 and 0.9 throughout the
2017–2020 period. Chart 2, for point ‘2’ (classified as Non and sparsely
vegetated on the map), exhibits strong seasonal variation. The
interpolated NDSI values drop significantly below 0.4 during the summer
months (e.g., reaching approximately 0.1 in late 2018 and late 2019) and
rise above 0.8 in winter.

<div id="fig-figure12">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-d71809d087019e8c85f1a87d240a2fd2d2e06bfb.png"
style="width:6.27in"
data-fig-alt="This visual illustrates the application of the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone decision tree approach for evaluating land cover characteristics at olive groves in Castile-La Mancha, Southern Spain, using Normalised Difference Vegetation Index (NDVI) time series. The upper-left panel displays a CLCplus Backbone Raster (RAS) classification for a 100x100m plot. The legend defines 11 land cover classes with corresponding colours: Sealed (Red), Woody needle leaved trees (Dark Green), Woody broadleaved deciduous trees (Medium Green), Woody broadleaved evergreen trees (Light Green), Low-growing woody plants (Olive Green), Permanent herbaceous (Pale Yellow), Periodically herbaceous (Pale Pink), Lichens and mosses (Light Grey), Non and sparsely vegetated (Yellow), Water (Blue), and Snow and ice (Cyan). The plot shows a linear feature (classified as Sealed and Non and sparsely vegetated) surrounded by a predominantly Non and sparsely vegetated area. A distinct band of Woody broadleaved evergreen trees and Woody broadleaved deciduous trees lines a Water body. Two numbered arrows indicate specific sampling locations. Arrow 1 points to an area primarily classified as Non and sparsely vegetated (yellow). Arrow 2 points to an area classified as Permanent herbaceous (pale yellow). The upper-right panel shows the corresponding Google Earth aerial imagery of the same area, depicting agricultural fields with circular irrigation patterns, a road, and tree-lined features. The lower section presents two line charts displaying NDVI values over time from 2020-01-01 to 2024-01-01, each corresponding to a numbered sampling location. The Y-axis represents NDVI, ranging from -0.1 to 1.0. A horizontal dotted blue line at NDVI = 0.2 indicates a threshold. The period from 2023-01-01 to 2024-01-01 is highlighted with a light blue shaded rectangle on both charts. The first chart, labelled &#39;1,&#39; corresponds to the Non and sparsely vegetated area. Its NDVI values generally fluctuate between 0.0 and 0.2, consistently staying at or below the 0.2 threshold, with only slight occasional peaks exceeding it, particularly within the 2023–2024 highlighted period. The second chart, labelled &#39;2,&#39; corresponds to the Permanent herbaceous area. It shows strong annual seasonality with distinct peaks in NDVI (reaching up to 0.9) during warmer months and troughs near 0.0 during winter. The NDVI values frequently and significantly exceed the 0.2 threshold for extended periods each year."
alt="This visual illustrates the application of the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone decision tree approach for evaluating land cover characteristics at olive groves in Castile-La Mancha, Southern Spain, using Normalised Difference Vegetation Index (NDVI) time series. The upper-left panel displays a CLCplus Backbone Raster (RAS) classification for a 100x100m plot. The legend defines 11 land cover classes with corresponding colours: Sealed (Red), Woody needle leaved trees (Dark Green), Woody broadleaved deciduous trees (Medium Green), Woody broadleaved evergreen trees (Light Green), Low-growing woody plants (Olive Green), Permanent herbaceous (Pale Yellow), Periodically herbaceous (Pale Pink), Lichens and mosses (Light Grey), Non and sparsely vegetated (Yellow), Water (Blue), and Snow and ice (Cyan). The plot shows a linear feature (classified as Sealed and Non and sparsely vegetated) surrounded by a predominantly Non and sparsely vegetated area. A distinct band of Woody broadleaved evergreen trees and Woody broadleaved deciduous trees lines a Water body. Two numbered arrows indicate specific sampling locations. Arrow 1 points to an area primarily classified as Non and sparsely vegetated (yellow). Arrow 2 points to an area classified as Permanent herbaceous (pale yellow). The upper-right panel shows the corresponding Google Earth aerial imagery of the same area, depicting agricultural fields with circular irrigation patterns, a road, and tree-lined features. The lower section presents two line charts displaying NDVI values over time from 2020-01-01 to 2024-01-01, each corresponding to a numbered sampling location. The Y-axis represents NDVI, ranging from -0.1 to 1.0. A horizontal dotted blue line at NDVI = 0.2 indicates a threshold. The period from 2023-01-01 to 2024-01-01 is highlighted with a light blue shaded rectangle on both charts. The first chart, labelled &#39;1,&#39; corresponds to the Non and sparsely vegetated area. Its NDVI values generally fluctuate between 0.0 and 0.2, consistently staying at or below the 0.2 threshold, with only slight occasional peaks exceeding it, particularly within the 2023–2024 highlighted period. The second chart, labelled &#39;2,&#39; corresponds to the Permanent herbaceous area. It shows strong annual seasonality with distinct peaks in NDVI (reaching up to 0.9) during warmer months and troughs near 0.0 during winter. The NDVI values frequently and significantly exceed the 0.2 threshold for extended periods each year." />

Figure 12: Example from the 2023 production of the mapping of
temporarily barren agricultural fields in contrast to cultivated fields
in the CLCplus Backbone (CLCplus BB RAS) in Spain. The parcels that are
cultivated during the reference year (point 2 in the image) show at
least one strong NDVI peak in 2023 (blue box) and a drop in the NDVI,
referring to ploughing (bare soil) and are therefore correctly
classified as periodically herbaceous. In contrast, parcels which are
not cultivated during the reference year (point 1 in the image) show a
very faint NDVI signal, peaking around 0.2 (dotted line) and are hence
correctly mapped as class Non and sparsely vegetated

</div>

This visual illustrates the application of the Copernicus Land
Monitoring Service (CLMS) CLCplus Backbone decision tree approach for
evaluating land cover characteristics at olive groves in Castile-La
Mancha, Southern Spain, using Normalised Difference Vegetation Index
(NDVI) time series.

The upper-left panel displays a CLCplus Backbone Raster (RAS)
classification for a 100x100m plot. The legend defines 11 land cover
classes with corresponding colours: Sealed (Red), Woody needle leaved
trees (Dark Green), Woody broadleaved deciduous trees (Medium Green),
Woody broadleaved evergreen trees (Light Green), Low-growing woody
plants (Olive Green), Permanent herbaceous (Pale Yellow), Periodically
herbaceous (Pale Pink), Lichens and mosses (Light Grey), Non and
sparsely vegetated (Yellow), Water (Blue), and Snow and ice (Cyan). The
plot shows a linear feature (classified as Sealed and Non and sparsely
vegetated) surrounded by a predominantly Non and sparsely vegetated
area. A distinct band of Woody broadleaved evergreen trees and Woody
broadleaved deciduous trees lines a Water body. Two numbered arrows
indicate specific sampling locations. Arrow 1 points to an area
primarily classified as Non and sparsely vegetated (yellow). Arrow 2
points to an area classified as Permanent herbaceous (pale yellow).

The upper-right panel shows the corresponding Google Earth aerial
imagery of the same area, depicting agricultural fields with circular
irrigation patterns, a road, and tree-lined features.

The lower section presents two line charts displaying NDVI values over
time from 2020-01-01 to 2024-01-01, each corresponding to a numbered
sampling location. The Y-axis represents NDVI, ranging from -0.1 to 1.0.
A horizontal dotted blue line at NDVI = 0.2 indicates a threshold. The
period from 2023-01-01 to 2024-01-01 is highlighted with a light blue
shaded rectangle on both charts.

The first chart, labelled “1,” corresponds to the Non and sparsely
vegetated area. Its NDVI values generally fluctuate between 0.0 and 0.2,
consistently staying at or below the 0.2 threshold, with only slight
occasional peaks exceeding it, particularly within the 2023–2024
highlighted period.

The second chart, labelled “2,” corresponds to the Permanent herbaceous
area. It shows strong annual seasonality with distinct peaks in NDVI
(reaching up to 0.9) during warmer months and troughs near 0.0 during
winter. The NDVI values frequently and significantly exceed the 0.2
threshold for extended periods each year.

Example 7 (<a href="#fig-figure13" class="quarto-xref">Figure 13</a>)
illustrates the mapping of dry grasslands (widespread in Southern Europe
and Turkey) as class Permanent herbaceous. Though the vegetation signal
is rather subtle, when compared to Permanent herbaceous for example in
Central Europe, it is still sufficient to correctly distinguish such
areas from class Non- and sparsely vegetated areas in those regions. In
the given example the area, classified as Non- and sparsely vegetated is
characterized by an NDVI, being constantly below 0.2, while the
Permanent herbaceous area slightly exceeds this value for a certain part
of the year, peaking around 0.3.

<div id="fig-figure13">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-1d3f8f304c690bb32de051c3385d01ae46c01b08.png"
style="width:6.27in"
data-fig-alt="This image illustrates the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone (BB) Raster (RAS) land cover classification, alongside a Very High Resolution (VHR) image from 2018 and two Normalised Difference Vegetation Index (NDVI) time series charts for specific points. The upper-left panel displays a CLCplus BB RAS land cover map. The legend defines 11 land cover classes by colour: - Red: Sealed - Dark green: Woody needle leaved trees - Light green: Woody broadleaved deciduous trees - Bright green: Woody broadleaved evergreen trees - Dark brown: Low-growing woody plants - Greenish-yellow: Permanent herbaceous - Light yellow: Periodically herbaceous - Pink: Lichens and mosses - Grey: Non and sparsely vegetated - Blue: Water - Cyan: Snow and ice The map highlights two numbered points, &#39;1&#39; and &#39;2&#39;, both located within areas classified as &#39;Non and sparsely vegetated&#39; (grey) or &#39;Permanent herbaceous&#39; (greenish-yellow). The upper-right panel shows a VHR IMAGE from 2018, providing an aerial view of the same area. This image displays agricultural fields, including distinctive reddish-brown tilled areas, and naturalized vegetation along a gully, visually confirming an olive grove context in Southern Spain. The lower section presents two line charts, both showing NDVI values over time from May 2017 to September 2020. The Y-axis represents NDVI, ranging from 0.1 to 1.0. The X-axis represents time, by month and year (YYYY-MM). Each chart plots &#39;Index_orig&#39; (original NDVI values as grey dots) and &#39;Index_interp&#39; (interpolated NDVI values as a blue line). A horizontal dashed blue line at NDVI 0.2 serves as a threshold. A light blue shaded box highlights the period from 2018-01 to 2019-01 on both charts. - Chart 1, corresponding to map point &#39;1&#39;, shows NDVI values primarily fluctuating around or below the 0.2 threshold, particularly within the highlighted 2018-01 to 2019-01 period. - Chart 2, corresponding to map point &#39;2&#39;, shows slightly higher NDVI values than point &#39;1&#39;, with several instances exceeding the 0.2 threshold, especially during seasonal peaks within the highlighted 2018-01 to 2019-01 period. These charts help evaluate biotic coverage thresholds for land cover classification, particularly distinguishing between &#39;Non and sparsely vegetated&#39; and &#39;Periodically herbaceous&#39; in olive groves where understorey growth is often suppressed."
alt="This image illustrates the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone (BB) Raster (RAS) land cover classification, alongside a Very High Resolution (VHR) image from 2018 and two Normalised Difference Vegetation Index (NDVI) time series charts for specific points. The upper-left panel displays a CLCplus BB RAS land cover map. The legend defines 11 land cover classes by colour: - Red: Sealed - Dark green: Woody needle leaved trees - Light green: Woody broadleaved deciduous trees - Bright green: Woody broadleaved evergreen trees - Dark brown: Low-growing woody plants - Greenish-yellow: Permanent herbaceous - Light yellow: Periodically herbaceous - Pink: Lichens and mosses - Grey: Non and sparsely vegetated - Blue: Water - Cyan: Snow and ice The map highlights two numbered points, &#39;1&#39; and &#39;2&#39;, both located within areas classified as &#39;Non and sparsely vegetated&#39; (grey) or &#39;Permanent herbaceous&#39; (greenish-yellow). The upper-right panel shows a VHR IMAGE from 2018, providing an aerial view of the same area. This image displays agricultural fields, including distinctive reddish-brown tilled areas, and naturalized vegetation along a gully, visually confirming an olive grove context in Southern Spain. The lower section presents two line charts, both showing NDVI values over time from May 2017 to September 2020. The Y-axis represents NDVI, ranging from 0.1 to 1.0. The X-axis represents time, by month and year (YYYY-MM). Each chart plots &#39;Index_orig&#39; (original NDVI values as grey dots) and &#39;Index_interp&#39; (interpolated NDVI values as a blue line). A horizontal dashed blue line at NDVI 0.2 serves as a threshold. A light blue shaded box highlights the period from 2018-01 to 2019-01 on both charts. - Chart 1, corresponding to map point &#39;1&#39;, shows NDVI values primarily fluctuating around or below the 0.2 threshold, particularly within the highlighted 2018-01 to 2019-01 period. - Chart 2, corresponding to map point &#39;2&#39;, shows slightly higher NDVI values than point &#39;1&#39;, with several instances exceeding the 0.2 threshold, especially during seasonal peaks within the highlighted 2018-01 to 2019-01 period. These charts help evaluate biotic coverage thresholds for land cover classification, particularly distinguishing between &#39;Non and sparsely vegetated&#39; and &#39;Periodically herbaceous&#39; in olive groves where understorey growth is often suppressed." />

Figure 13: Example of the mapping of dry grasslands as class Permanent
herbaceous in the CLCplus Backbone (CLCplus BB RAS) in Turkey. While in
Central European and Northern Europe, permanently herbaceous areas are
typically characterized by a strong NDVI peak during the vegetation
season, dry grasslands in Southern Europe and Turkey are characterized
by far fainter vegetation signals, exceeding the value of 0.2 (dotted
line) only slightly for a certain part of the reference year (blue box)

</div>

This image illustrates the Copernicus Land Monitoring Service (CLMS)
CLCplus Backbone (BB) Raster (RAS) land cover classification, alongside
a Very High Resolution (VHR) image from 2018 and two Normalised
Difference Vegetation Index (NDVI) time series charts for specific
points.

The upper-left panel displays a CLCplus BB RAS land cover map. The
legend defines 11 land cover classes by colour: - Red: Sealed - Dark
green: Woody needle leaved trees - Light green: Woody broadleaved
deciduous trees - Bright green: Woody broadleaved evergreen trees - Dark
brown: Low-growing woody plants - Greenish-yellow: Permanent
herbaceous - Light yellow: Periodically herbaceous - Pink: Lichens and
mosses - Grey: Non and sparsely vegetated - Blue: Water - Cyan: Snow and
ice The map highlights two numbered points, ‘1’ and ‘2’, both located
within areas classified as “Non and sparsely vegetated” (grey) or
“Permanent herbaceous” (greenish-yellow).

The upper-right panel shows a VHR IMAGE from 2018, providing an aerial
view of the same area. This image displays agricultural fields,
including distinctive reddish-brown tilled areas, and naturalized
vegetation along a gully, visually confirming an olive grove context in
Southern Spain.

The lower section presents two line charts, both showing NDVI values
over time from May 2017 to September 2020. The Y-axis represents NDVI,
ranging from 0.1 to 1.0. The X-axis represents time, by month and year
(YYYY-MM). Each chart plots “Index_orig” (original NDVI values as grey
dots) and “Index_interp” (interpolated NDVI values as a blue line). A
horizontal dashed blue line at NDVI 0.2 serves as a threshold. A light
blue shaded box highlights the period from 2018-01 to 2019-01 on both
charts. - Chart 1, corresponding to map point ‘1’, shows NDVI values
primarily fluctuating around or below the 0.2 threshold, particularly
within the highlighted 2018-01 to 2019-01 period. - Chart 2,
corresponding to map point ‘2’, shows slightly higher NDVI values than
point ‘1’, with several instances exceeding the 0.2 threshold,
especially during seasonal peaks within the highlighted 2018-01 to
2019-01 period. These charts help evaluate biotic coverage thresholds
for land cover classification, particularly distinguishing between “Non
and sparsely vegetated” and “Periodically herbaceous” in olive groves
where understorey growth is often suppressed.

Example 8 (<a href="#fig-figure14" class="quarto-xref">Figure 14</a>)
illustrates uncertainties in the mapping of intensively managed
grassland (e.g. fodder crops) as either class Permanent herbaceous or
class Periodically herbaceous. While the exposure of bare soil within
the reference years can be clearly detected in most ploughed parcels
(i.e. to be mapped as Periodically herbaceous), there can be border
cases where drought events and mowing events under rather dry conditions
are not fully distinguishable from a bare soil exposure.

<div id="fig-figure14">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-76dd48cc30f1b40d1cb9671545ebffd6778fb65c.png"
style="width:6.27in"
data-fig-alt="This illustration demonstrates the Copernicus Land Monitoring Service (CLMS) CLC+ Backbone Raster (BB RAS) classification approach for evaluating land cover thresholds, specifically for olive groves in Castile-La Mancha, Spain. The top-left panel, labelled &#39;CLCplus BB RAS&#39;, displays a 20x20 grid of 10-metre (m) pixels, representing the resulting land cover class attribution. Pixel &#39;1&#39; is classified as &#39;Non and sparsely vegetated&#39; (yellow), and pixel &#39;2&#39; is classified as &#39;Permanent herbaceous&#39; (light green). Other visible classes include &#39;Sealed&#39; (red) and &#39;Woody broadleaved evergreen trees&#39; (dark green). This classification applies a threshold where a biotic coverage percentage greater than 30% differentiates between &#39;Non and sparsely vegetated&#39; and other vegetation classes. The top-right panel, labelled &#39;VHR IMAGE 2018&#39;, shows a Very High Resolution (VHR) aerial image from 2018, overlaid with the same 20x20 grid, providing visual context for the classified area. A legend to the left of the image defines the land cover classes: * Sealed (red) * Woody needle leaved trees (dark green) * Woody broadleaved deciduous trees (medium green) * Woody broadleaved evergreen trees (dark green) * Low-growing woody plants (light brown) * Permanent herbaceous (light green) * Periodically herbaceous (yellow-green) * Lichens and mosses (purple) * Non and sparsely vegetated (yellow) * Water (light blue) * Snow and ice (white) Below the top panels are two line charts displaying Normalised Difference Vegetation Index (NDVI) values over time, ranging from 2017-05 to 2020-09, for the specific pixels labelled &#39;1&#39; and &#39;2&#39;. The Y-axis for both charts represents NDVI, from 0.1 to 1.0. Each chart shows &#39;Index_orig&#39; (original NDVI values as grey dots) and &#39;Index_interp&#39; (interpolated NDVI values as a blue line with circles). Both charts highlight the period from early 2018 to early 2019 with a light blue shaded rectangle. * Chart &#39;1&#39; (Pixel 1, &#39;Non and sparsely vegetated&#39;) shows a distinct seasonal pattern with low NDVI values (around 0.2-0.3) in early 2018, peaking near 0.8 in mid-2018, and dropping to 0.1 by early 2019, indicative of sparse or tilled vegetation. * Chart &#39;2&#39; (Pixel 2, &#39;Permanent herbaceous&#39;) shows generally higher NDVI values (around 0.7-0.8) with similar seasonal fluctuations as pixel 1, suggesting a more persistent herbaceous cover with seasonal growth and decline. The bottom section, titled &#39;Google Earth time line&#39;, presents six aerial images from Google Earth, showing the same area over different dates: 2018-02-19, 2018-05-14, 2018-05-27, 2018-05-30, 2018-07-20, and 2019-02-15. These images visually illustrate the temporal changes in land cover and vegetation state, corresponding to the NDVI time series."
alt="This illustration demonstrates the Copernicus Land Monitoring Service (CLMS) CLC+ Backbone Raster (BB RAS) classification approach for evaluating land cover thresholds, specifically for olive groves in Castile-La Mancha, Spain. The top-left panel, labelled &#39;CLCplus BB RAS&#39;, displays a 20x20 grid of 10-metre (m) pixels, representing the resulting land cover class attribution. Pixel &#39;1&#39; is classified as &#39;Non and sparsely vegetated&#39; (yellow), and pixel &#39;2&#39; is classified as &#39;Permanent herbaceous&#39; (light green). Other visible classes include &#39;Sealed&#39; (red) and &#39;Woody broadleaved evergreen trees&#39; (dark green). This classification applies a threshold where a biotic coverage percentage greater than 30% differentiates between &#39;Non and sparsely vegetated&#39; and other vegetation classes. The top-right panel, labelled &#39;VHR IMAGE 2018&#39;, shows a Very High Resolution (VHR) aerial image from 2018, overlaid with the same 20x20 grid, providing visual context for the classified area. A legend to the left of the image defines the land cover classes: * Sealed (red) * Woody needle leaved trees (dark green) * Woody broadleaved deciduous trees (medium green) * Woody broadleaved evergreen trees (dark green) * Low-growing woody plants (light brown) * Permanent herbaceous (light green) * Periodically herbaceous (yellow-green) * Lichens and mosses (purple) * Non and sparsely vegetated (yellow) * Water (light blue) * Snow and ice (white) Below the top panels are two line charts displaying Normalised Difference Vegetation Index (NDVI) values over time, ranging from 2017-05 to 2020-09, for the specific pixels labelled &#39;1&#39; and &#39;2&#39;. The Y-axis for both charts represents NDVI, from 0.1 to 1.0. Each chart shows &#39;Index_orig&#39; (original NDVI values as grey dots) and &#39;Index_interp&#39; (interpolated NDVI values as a blue line with circles). Both charts highlight the period from early 2018 to early 2019 with a light blue shaded rectangle. * Chart &#39;1&#39; (Pixel 1, &#39;Non and sparsely vegetated&#39;) shows a distinct seasonal pattern with low NDVI values (around 0.2-0.3) in early 2018, peaking near 0.8 in mid-2018, and dropping to 0.1 by early 2019, indicative of sparse or tilled vegetation. * Chart &#39;2&#39; (Pixel 2, &#39;Permanent herbaceous&#39;) shows generally higher NDVI values (around 0.7-0.8) with similar seasonal fluctuations as pixel 1, suggesting a more persistent herbaceous cover with seasonal growth and decline. The bottom section, titled &#39;Google Earth time line&#39;, presents six aerial images from Google Earth, showing the same area over different dates: 2018-02-19, 2018-05-14, 2018-05-27, 2018-05-30, 2018-07-20, and 2019-02-15. These images visually illustrate the temporal changes in land cover and vegetation state, corresponding to the NDVI time series." />

Figure 14: Example of the mapping of intensively used grassland
(e.g. fodder crops). The distinction between the classes Permanent
herbaceous and Periodically herbaceous depends on whether the bare soil
is exposed (e.g. ploughed parcel on the right, mapped as Periodically
herbaceous) within the reference year (blue box) or not. Especially
under extensive dry conditions, the distinction of mowing events
(i.e. no ploughing on the left parcel, mapped as class Permanent
herbaceous) and actual exposure of bare soil is challenging

</div>

This illustration demonstrates the Copernicus Land Monitoring Service
(CLMS) CLC+ Backbone Raster (BB RAS) classification approach for
evaluating land cover thresholds, specifically for olive groves in
Castile-La Mancha, Spain.

The top-left panel, labelled “CLCplus BB RAS”, displays a 20x20 grid of
10-metre (m) pixels, representing the resulting land cover class
attribution. Pixel ‘1’ is classified as “Non and sparsely vegetated”
(yellow), and pixel ‘2’ is classified as “Permanent herbaceous” (light
green). Other visible classes include “Sealed” (red) and “Woody
broadleaved evergreen trees” (dark green). This classification applies a
threshold where a biotic coverage percentage greater than 30%
differentiates between “Non and sparsely vegetated” and other vegetation
classes.

The top-right panel, labelled “VHR IMAGE 2018”, shows a Very High
Resolution (VHR) aerial image from 2018, overlaid with the same 20x20
grid, providing visual context for the classified area.

A legend to the left of the image defines the land cover classes: \*
Sealed (red) \* Woody needle leaved trees (dark green) \* Woody
broadleaved deciduous trees (medium green) \* Woody broadleaved
evergreen trees (dark green) \* Low-growing woody plants (light brown)
\* Permanent herbaceous (light green) \* Periodically herbaceous
(yellow-green) \* Lichens and mosses (purple) \* Non and sparsely
vegetated (yellow) \* Water (light blue) \* Snow and ice (white)

Below the top panels are two line charts displaying Normalised
Difference Vegetation Index (NDVI) values over time, ranging from
2017-05 to 2020-09, for the specific pixels labelled ‘1’ and ‘2’. The
Y-axis for both charts represents NDVI, from 0.1 to 1.0. Each chart
shows “Index_orig” (original NDVI values as grey dots) and
“Index_interp” (interpolated NDVI values as a blue line with circles).
Both charts highlight the period from early 2018 to early 2019 with a
light blue shaded rectangle. \* Chart ‘1’ (Pixel 1, “Non and sparsely
vegetated”) shows a distinct seasonal pattern with low NDVI values
(around 0.2-0.3) in early 2018, peaking near 0.8 in mid-2018, and
dropping to 0.1 by early 2019, indicative of sparse or tilled
vegetation. \* Chart ‘2’ (Pixel 2, “Permanent herbaceous”) shows
generally higher NDVI values (around 0.7-0.8) with similar seasonal
fluctuations as pixel 1, suggesting a more persistent herbaceous cover
with seasonal growth and decline.

The bottom section, titled “Google Earth time line”, presents six aerial
images from Google Earth, showing the same area over different dates:
2018-02-19, 2018-05-14, 2018-05-27, 2018-05-30, 2018-07-20, and
2019-02-15. These images visually illustrate the temporal changes in
land cover and vegetation state, corresponding to the NDVI time series.

Example 9 (<a href="#fig-figure15" class="quarto-xref">Figure 15</a>)
illustrates the challenges associated with the mapping of the class
Lowgrowing woody plants (bushes, shrubs) versus tree classes. The main
defining characteristics for the class Low-growing woody plants comprise
the habitus (i.e. growth forms with multiple stems emerging from the
ground) and the typical height (i.e. below 5m), both of which are
criteria which are typically difficult to evaluate from Sentinel-2 time
series alone. While the spectraltemporal signature of shrubs allows a
distinction from other land cover types to some degree (e.g. vineyards),
there are many cases where this is less obvious. Typical regional
examples comprise sparse woody canopies in Nordic countries with
mixtures of shrubs and trees even at the species level, the
Mediterranean Macchia where shrubs and trees can co-occur or heathlands
with mixtures of dwarf shrubs and herbaceous species.

<div id="fig-figure15">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-98f8fc0c2616e39680f4446b5be599320c5a71ab.png"
style="width:6.27in"
data-fig-alt="The image illustrates the uncertainty in mapping &#39;Low-growing woody plants&#39; by comparing a Copernicus Land Monitoring Service (CLMS) CORINE Land Cover plus Backbone (CLCplus BB RAS) classification with a Very High Resolution (VHR) image and a Google Earth Street View photograph. The upper left panel, labelled &#39;CLCplus BB RAS&#39;, presents a gridded land cover map with the following legend: - Red: Sealed - Dark Green: Woody broadleaved deciduous trees - Brown: Low-growing woody plants - Light Green: Permanent herbaceous - Grey: Non and sparsely vegetated This panel shows a linear feature classified as &#39;Sealed&#39; (red) running vertically, bordered by &#39;Permanent herbaceous&#39; (light green) and areas of &#39;Woody broadleaved deciduous trees&#39; (dark green) and &#39;Low-growing woody plants&#39; (brown) to the right. The upper right panel, labelled &#39;VHR IMAGE 2018&#39;, displays the same gridded area as a false-colour composite Very High Resolution image from 2018. A prominent cyan linear feature corresponds to the red &#39;Sealed&#39; class in the CLCplus map. Adjacent areas show spectral variations in shades of red, with patches of lighter red and some cyan tones, representing various vegetation types or sparse cover. The lower panel, labelled &#39;Google Earth – Street View 2009-06&#39;, is a ground-level photograph showing a landscape with sparsely distributed deciduous trees (consistent with &#39;Low-growing woody plants&#39; or &#39;Woody broadleaved deciduous trees&#39;), rocky ground, and dry herbaceous vegetation. This photograph provides a ground truth perspective to contextualize the land cover classifications. The overall image highlights that the gridded CLCplus BB RAS classification provides a generalized view of the complex and mixed land cover, particularly demonstrating the challenges and potential uncertainties in precisely mapping and differentiating &#39;Low-growing woody plants&#39; from other vegetation types or non-vegetated areas when compared to detailed VHR imagery and ground-level observations."
alt="The image illustrates the uncertainty in mapping &#39;Low-growing woody plants&#39; by comparing a Copernicus Land Monitoring Service (CLMS) CORINE Land Cover plus Backbone (CLCplus BB RAS) classification with a Very High Resolution (VHR) image and a Google Earth Street View photograph. The upper left panel, labelled &#39;CLCplus BB RAS&#39;, presents a gridded land cover map with the following legend: - Red: Sealed - Dark Green: Woody broadleaved deciduous trees - Brown: Low-growing woody plants - Light Green: Permanent herbaceous - Grey: Non and sparsely vegetated This panel shows a linear feature classified as &#39;Sealed&#39; (red) running vertically, bordered by &#39;Permanent herbaceous&#39; (light green) and areas of &#39;Woody broadleaved deciduous trees&#39; (dark green) and &#39;Low-growing woody plants&#39; (brown) to the right. The upper right panel, labelled &#39;VHR IMAGE 2018&#39;, displays the same gridded area as a false-colour composite Very High Resolution image from 2018. A prominent cyan linear feature corresponds to the red &#39;Sealed&#39; class in the CLCplus map. Adjacent areas show spectral variations in shades of red, with patches of lighter red and some cyan tones, representing various vegetation types or sparse cover. The lower panel, labelled &#39;Google Earth – Street View 2009-06&#39;, is a ground-level photograph showing a landscape with sparsely distributed deciduous trees (consistent with &#39;Low-growing woody plants&#39; or &#39;Woody broadleaved deciduous trees&#39;), rocky ground, and dry herbaceous vegetation. This photograph provides a ground truth perspective to contextualize the land cover classifications. The overall image highlights that the gridded CLCplus BB RAS classification provides a generalized view of the complex and mixed land cover, particularly demonstrating the challenges and potential uncertainties in precisely mapping and differentiating &#39;Low-growing woody plants&#39; from other vegetation types or non-vegetated areas when compared to detailed VHR imagery and ground-level observations." />

Figure 15: Example of the uncertainty in the mapping of Low-growing
woody plants. This example from Northern Sweden illustrates that a sharp
distinction of shrubs and trees is often difficult and sometimes remains
fuzzy even at the level of the same species (here different specimens of
Betula with sometimes more tree-like, sometimes more shrub-like
habitus). In addition, the canopy is rather sparse and the understorey
comprises a mix of herbaceous species, dwarf shrubs as well as mosses
and lichens

</div>

The image illustrates the uncertainty in mapping ‘Low-growing woody
plants’ by comparing a Copernicus Land Monitoring Service (CLMS) CORINE
Land Cover plus Backbone (CLCplus BB RAS) classification with a Very
High Resolution (VHR) image and a Google Earth Street View photograph.

The upper left panel, labelled “CLCplus BB RAS”, presents a gridded land
cover map with the following legend: - Red: Sealed - Dark Green: Woody
broadleaved deciduous trees - Brown: Low-growing woody plants - Light
Green: Permanent herbaceous - Grey: Non and sparsely vegetated This
panel shows a linear feature classified as ‘Sealed’ (red) running
vertically, bordered by ‘Permanent herbaceous’ (light green) and areas
of ‘Woody broadleaved deciduous trees’ (dark green) and ‘Low-growing
woody plants’ (brown) to the right.

The upper right panel, labelled “VHR IMAGE 2018”, displays the same
gridded area as a false-colour composite Very High Resolution image from
2018. A prominent cyan linear feature corresponds to the red ‘Sealed’
class in the CLCplus map. Adjacent areas show spectral variations in
shades of red, with patches of lighter red and some cyan tones,
representing various vegetation types or sparse cover.

The lower panel, labelled “Google Earth – Street View 2009-06”, is a
ground-level photograph showing a landscape with sparsely distributed
deciduous trees (consistent with ‘Low-growing woody plants’ or ‘Woody
broadleaved deciduous trees’), rocky ground, and dry herbaceous
vegetation. This photograph provides a ground truth perspective to
contextualize the land cover classifications.

The overall image highlights that the gridded CLCplus BB RAS
classification provides a generalized view of the complex and mixed land
cover, particularly demonstrating the challenges and potential
uncertainties in precisely mapping and differentiating ‘Low-growing
woody plants’ from other vegetation types or non-vegetated areas when
compared to detailed VHR imagery and ground-level observations.

Example 10 (<a href="#fig-figure16" class="quarto-xref">Figure 16</a>)
illustrates the typical similarity between surfaces covered by class
Lichens and mosses versus areas of class Non and sparsely vegetated with
some fractions of sparse herbaceous vegetation. Both land cover
compositions occur in the same biogeographic regions and are nearly
indistinguishable in VHR imagery or NDVI time-series. In areas, where
street view imagery and auxiliary data sources are available, it is
possible to map and verify larger occurrences of this class, however,
large uncertainties remain, in remote areas with no or little adequate
reference data.

<div id="fig-figure16">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-a9cf10eb70724ae6bb7b176893dc961c52570f04.png"
style="width:6.27in"
data-fig-alt="This image presents two examples (1 and 2) illustrating land cover classification by the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone Raster (BB RAS) product, comparing it with Google Earth Street View images, Very High Resolution (VHR) satellite imagery from 2018, and Normalized Difference Vegetation Index (NDVI) time series. **Example 1:** - **Google Earth – Street View:** Displays a close-up of a rocky, barren landscape dominated by pale, light-coloured lichens and mosses, with sparse reddish-brown vegetation. - **VHR IMAGE 2018:** Shows a grid of pixels (likely 20 m resolution) in shades of bluish-green and darker green/brown, representing the same area as the street view. - **CLCplus BB RAS:** Classifies the area within the pixel grid. The majority is magenta, labelled &#39;Lichens and mosses&#39;, with some pixels in the bottom left classified as yellow &#39;Permanent herbaceous&#39;. - **NDVI Chart for Example 1:** A line chart showing NDVI values on the Y-axis (ranging from -0.2 to 1.0) against time on the X-axis (from 2017-09 to 2020-09). Two data series are plotted: &#39;Index_orig&#39; (grey diamonds for original NDVI values) and &#39;Index_interp&#39; (blue line with white circles for interpolated NDVI values). The chart displays a distinct annual seasonality, with peaks around 0.4 in late spring/early summer (e.g., May 2018, May 2019, May 2020) and troughs near 0.0 in winter (e.g., January 2018, January 2019, January 2020). A light blue shaded rectangle highlights the 2018-01 to 2019-01 period. **Example 2:** - **Google Earth – Street View:** Presents a wider view of an undulating, rocky landscape with visible wind turbines in the background. The foreground is mostly bare rock with sparse, low-lying vegetation. - **VHR IMAGE 2018:** Shows a grid of pixels for the second area in reddish-brown and dark green tones, reflecting sparse vegetation and bare ground. - **CLCplus BB RAS:** Classifies the area within the pixel grid. The majority is grey, labelled &#39;Non and sparsely vegetated&#39;, with some pixels in the top right classified as yellow &#39;Permanent herbaceous&#39;. - **NDVI Chart for Example 2:** Similar line chart to Example 1, with NDVI on the Y-axis (-0.2 to 1.0) and time on the X-axis (2017-09 to 2020-09). It also plots &#39;Index_orig&#39; (grey diamonds) and &#39;Index_interp&#39; (blue line with white circles). This chart shows lower overall NDVI values compared to Example 1, with annual peaks around 0.2 to 0.3 in late spring/early summer and winter values closer to -0.1 to 0.0. A light blue shaded rectangle highlights the 2018-01 to 2019-01 period. **Shared Legend:** The CLCplus BB RAS classification uses three colours and labels: - Yellow: Permanent herbaceous - Magenta: Lichens and mosses - Grey: Non and sparsely vegetated"
alt="This image presents two examples (1 and 2) illustrating land cover classification by the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone Raster (BB RAS) product, comparing it with Google Earth Street View images, Very High Resolution (VHR) satellite imagery from 2018, and Normalized Difference Vegetation Index (NDVI) time series. **Example 1:** - **Google Earth – Street View:** Displays a close-up of a rocky, barren landscape dominated by pale, light-coloured lichens and mosses, with sparse reddish-brown vegetation. - **VHR IMAGE 2018:** Shows a grid of pixels (likely 20 m resolution) in shades of bluish-green and darker green/brown, representing the same area as the street view. - **CLCplus BB RAS:** Classifies the area within the pixel grid. The majority is magenta, labelled &#39;Lichens and mosses&#39;, with some pixels in the bottom left classified as yellow &#39;Permanent herbaceous&#39;. - **NDVI Chart for Example 1:** A line chart showing NDVI values on the Y-axis (ranging from -0.2 to 1.0) against time on the X-axis (from 2017-09 to 2020-09). Two data series are plotted: &#39;Index_orig&#39; (grey diamonds for original NDVI values) and &#39;Index_interp&#39; (blue line with white circles for interpolated NDVI values). The chart displays a distinct annual seasonality, with peaks around 0.4 in late spring/early summer (e.g., May 2018, May 2019, May 2020) and troughs near 0.0 in winter (e.g., January 2018, January 2019, January 2020). A light blue shaded rectangle highlights the 2018-01 to 2019-01 period. **Example 2:** - **Google Earth – Street View:** Presents a wider view of an undulating, rocky landscape with visible wind turbines in the background. The foreground is mostly bare rock with sparse, low-lying vegetation. - **VHR IMAGE 2018:** Shows a grid of pixels for the second area in reddish-brown and dark green tones, reflecting sparse vegetation and bare ground. - **CLCplus BB RAS:** Classifies the area within the pixel grid. The majority is grey, labelled &#39;Non and sparsely vegetated&#39;, with some pixels in the top right classified as yellow &#39;Permanent herbaceous&#39;. - **NDVI Chart for Example 2:** Similar line chart to Example 1, with NDVI on the Y-axis (-0.2 to 1.0) and time on the X-axis (2017-09 to 2020-09). It also plots &#39;Index_orig&#39; (grey diamonds) and &#39;Index_interp&#39; (blue line with white circles). This chart shows lower overall NDVI values compared to Example 1, with annual peaks around 0.2 to 0.3 in late spring/early summer and winter values closer to -0.1 to 0.0. A light blue shaded rectangle highlights the 2018-01 to 2019-01 period. **Shared Legend:** The CLCplus BB RAS classification uses three colours and labels: - Yellow: Permanent herbaceous - Magenta: Lichens and mosses - Grey: Non and sparsely vegetated" />

Figure 16: Example of the uncertainty in the mapping of the class
Lichens and mosses in the CLCplus Backbone (CLCplus BB RAS). These two
examples from Southern Norway illustrate the typical similarity between
surfaces covered by class Lichens and mosses versus class Non- and
sparsely vegetated areas with sparse herbaceous vegetation. Both land
cover compositions occur under similar biogeographic conditions and are
nearly indistinguishable in VHR imagery or NDVI time-series (blue box
indicates reference year)

</div>

This image presents two examples (1 and 2) illustrating land cover
classification by the Copernicus Land Monitoring Service (CLMS) CLCplus
Backbone Raster (BB RAS) product, comparing it with Google Earth Street
View images, Very High Resolution (VHR) satellite imagery from 2018, and
Normalized Difference Vegetation Index (NDVI) time series.

**Example 1:** - **Google Earth – Street View:** Displays a close-up of
a rocky, barren landscape dominated by pale, light-coloured lichens and
mosses, with sparse reddish-brown vegetation. - **VHR IMAGE 2018:**
Shows a grid of pixels (likely 20 m resolution) in shades of
bluish-green and darker green/brown, representing the same area as the
street view. - **CLCplus BB RAS:** Classifies the area within the pixel
grid. The majority is magenta, labelled “Lichens and mosses”, with some
pixels in the bottom left classified as yellow “Permanent herbaceous”. -
**NDVI Chart for Example 1:** A line chart showing NDVI values on the
Y-axis (ranging from -0.2 to 1.0) against time on the X-axis (from
2017-09 to 2020-09). Two data series are plotted: “Index_orig” (grey
diamonds for original NDVI values) and “Index_interp” (blue line with
white circles for interpolated NDVI values). The chart displays a
distinct annual seasonality, with peaks around 0.4 in late spring/early
summer (e.g., May 2018, May 2019, May 2020) and troughs near 0.0 in
winter (e.g., January 2018, January 2019, January 2020). A light blue
shaded rectangle highlights the 2018-01 to 2019-01 period.

**Example 2:** - **Google Earth – Street View:** Presents a wider view
of an undulating, rocky landscape with visible wind turbines in the
background. The foreground is mostly bare rock with sparse, low-lying
vegetation. - **VHR IMAGE 2018:** Shows a grid of pixels for the second
area in reddish-brown and dark green tones, reflecting sparse vegetation
and bare ground. - **CLCplus BB RAS:** Classifies the area within the
pixel grid. The majority is grey, labelled “Non and sparsely vegetated”,
with some pixels in the top right classified as yellow “Permanent
herbaceous”. - **NDVI Chart for Example 2:** Similar line chart to
Example 1, with NDVI on the Y-axis (-0.2 to 1.0) and time on the X-axis
(2017-09 to 2020-09). It also plots “Index_orig” (grey diamonds) and
“Index_interp” (blue line with white circles). This chart shows lower
overall NDVI values compared to Example 1, with annual peaks around 0.2
to 0.3 in late spring/early summer and winter values closer to -0.1 to
0.0. A light blue shaded rectangle highlights the 2018-01 to 2019-01
period.

**Shared Legend:** The CLCplus BB RAS classification uses three colours
and labels: - Yellow: Permanent herbaceous - Magenta: Lichens and
mosses - Grey: Non and sparsely vegetated

## Auxiliary layers

The CLCplus Backbone raster classification layer (RAS) is accompanied by
three auxiliary layers, which are described in the following
subsections. For more information on the methodologies applied in
creation of the auxiliary layers please refer to the Algorithm
Theoretical Basis Document \[AD-1\].

### Raster Data Score Layer

The Data Score Layer (RASDL) quantifies the number of available
observations in the Sentinel-2 (S-2) data time series, which was used as
input for the CLCplus Backbone classification approach. The RASDL is
therefore a basic quality indicator of the input time series for the
raster classification.

<div id="fig-figure17">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-957b567d0ef07f50f054c5cee41babd5cf0d641d.png"
style="width:6.27in"
data-fig-alt="Choropleth map displaying the &#39;Data Score Layer 2023&#39;, showing the number of cloudfree observations across Europe. The main map covers longitudes from 10°W to 70°E and latitudes from 40°N to 60°N, encompassing Iceland, the British Isles, Fennoscandia, and continental Europe down to the Mediterranean and parts of Turkey. Two inset maps show the Azores Islands and the Canary and Madeira Islands. The colour scale indicates the number of cloudfree observations: * Red: Low (0 observations) * Green: High (&gt;200 observations) Intermediate values are represented by yellow and orange hues. The main map includes a scale bar from 0 to 1000 km, with increments at 250 km and 500 km. Each inset map includes a scale bar from 0 to 300 km, with an increment at 150 km. The map shows that large parts of Europe, including Iceland, the British Isles, Scandinavia, and central/western Europe, generally have intermediate numbers of cloudfree observations, depicted in orange and yellow colours. Higher numbers of cloudfree observations (green) are visible in scattered regions, notably along parts of the Mediterranean coast, Southern Spain, Italy, Greece, and parts of Turkey. The data is presented in distinct diagonal stripes, reflecting the acquisition paths of the underlying satellite imagery."
alt="Choropleth map displaying the &#39;Data Score Layer 2023&#39;, showing the number of cloudfree observations across Europe. The main map covers longitudes from 10°W to 70°E and latitudes from 40°N to 60°N, encompassing Iceland, the British Isles, Fennoscandia, and continental Europe down to the Mediterranean and parts of Turkey. Two inset maps show the Azores Islands and the Canary and Madeira Islands. The colour scale indicates the number of cloudfree observations: * Red: Low (0 observations) * Green: High (&gt;200 observations) Intermediate values are represented by yellow and orange hues. The main map includes a scale bar from 0 to 1000 km, with increments at 250 km and 500 km. Each inset map includes a scale bar from 0 to 300 km, with an increment at 150 km. The map shows that large parts of Europe, including Iceland, the British Isles, Scandinavia, and central/western Europe, generally have intermediate numbers of cloudfree observations, depicted in orange and yellow colours. Higher numbers of cloudfree observations (green) are visible in scattered regions, notably along parts of the Mediterranean coast, Southern Spain, Italy, Greece, and parts of Turkey. The data is presented in distinct diagonal stripes, reflecting the acquisition paths of the underlying satellite imagery." />

Figure 17: CLCplus Backbone Data Score Layer (RASDL) of the reference
year 2023 (±3 months)

</div>

Choropleth map displaying the “Data Score Layer 2023”, showing the
number of cloudfree observations across Europe. The main map covers
longitudes from 10°W to 70°E and latitudes from 40°N to 60°N,
encompassing Iceland, the British Isles, Fennoscandia, and continental
Europe down to the Mediterranean and parts of Turkey. Two inset maps
show the Azores Islands and the Canary and Madeira Islands.

The colour scale indicates the number of cloudfree observations: \* Red:
Low (0 observations) \* Green: High (\>200 observations) Intermediate
values are represented by yellow and orange hues.

The main map includes a scale bar from 0 to 1000 km, with increments at
250 km and 500 km. Each inset map includes a scale bar from 0 to 300 km,
with an increment at 150 km.

The map shows that large parts of Europe, including Iceland, the British
Isles, Scandinavia, and central/western Europe, generally have
intermediate numbers of cloudfree observations, depicted in orange and
yellow colours. Higher numbers of cloudfree observations (green) are
visible in scattered regions, notably along parts of the Mediterranean
coast, Southern Spain, Italy, Greece, and parts of Turkey. The data is
presented in distinct diagonal stripes, reflecting the acquisition paths
of the underlying satellite imagery.

The clearly visible stripe patterns (see
<a href="#fig-figure17" class="quarto-xref">Figure 17</a>) from SW to NE
correctly represent the different data quantities between the
overlapping areas of the S-2 swaths. Besides this normal general pattern
of the RASDL, there are some patterns that are worth further explaining:
S-2 GRANULE overlaps are often visible as horizontal and vertical
stripes with slightly higher observation counts. This is because there
is a higher chance in the overlap areas that one of the GRANULES fulfils
the cloud cover threshold used in scene selection.

#### File naming convention

The filenames for the Raster Data Score Layer are composed of the
following elements:

*Prefix_DataTheme_DataSubTheme_TemporalReference_DataTypeSpatialResolution_SpatialExtent_EPSGCode_VersionNumber_RevisionNumber*

**➔ CLMS_CLCPLUS_RASDL_S2023_R10m_EXXNXX_03035_V01_R00**

Where:

|  |  |
|----|----|
| Prefix: CLMS | SpatialResolution (SpatialResolutionUnit): 10m |
| DataTheme: CLCPLUS | SpatialExtent: EXXNXX or GF, GP, MQ, RE, YT for French DOMs |
| DataSub-Theme: RASDL | EPSGCode: 03035 (or EPSG codes for national projections of DOMs) |
| TemporalReference: S2023 | VersionNumber: V01 |
| DataType: R; V | RevisionNumber: R00 |

The product specifications for the CLCplus Backbone RASDL layer are
summarized in Table 4.

Table 4: Technical specifications of the Raster Data Score Layer

| CLCplus Backbone Raster Data Score Layer / Acronym: RAS / Product family: CLMS_CLCplus |
|----|
| **Summary**: The Data Score Layer is a 10m pixel-based auxiliary layer for the CLCplus Backbone RAS. It is based on a filtered Sentinel-2 time series from October 2022 to March 2024 and auxiliary features. |
| **Reference year**: 2023 |
| **Geometric resolution**: Pixel resolution 10m x 10m, fully conform with the EEA reference grid |
| **Coordinate Reference System**: European ETRS89 LAEA projection / WGS84 and the respective UTM zone for French DOMs |
| **Coverage**: 6.002.105 km² (covering the full EEA38 + UK) |
| **Geometric accuracy (positioning scale)**: equals the Sentinel-2 positional accuracy in 2023 (\<9m at 95.5% confidence) |
| **Data type**: 16bit unsigned raster with LZW compression |
| **Minimum Mapping Unit (MMU)**: Pixel-based (no MMU) |
| **Necessary attributes**: Value, Count, Obs_count |
| **Raster coding**: <br> 0-200: Valid observations count <br> 65535: Outside area |
| **Metadata**: XML metadata files according to INSPIRE metadata standards |
| **Delivery format**: Cloud optimized GeoTIFFs as 100x100km tiles incl. pyramids and embedded colour map (\*.tif), attribute table (\*.aux.xml), and INSPIRE-compliant metadata in XML format (\*.xml) |

### Raster Confidence Layer

The Raster Confidence Layer (RASCL) holds information on the confidence
of the classifier in the class assignment of each 10m pixel. The higher
the confidence value, the more reliable the class assignment for a
pixel, the lower the confidence value the more uncertain it is. The
value range of RASCL is 0-100.

<a href="#fig-figure18" class="quarto-xref">Figure 18</a> shows the
RASCL for the reference year 2023 for EEA38 + UK. The partially visible
edges (see closeup in
<a href="#fig-figure19" class="quarto-xref">Figure 19</a>) are the
result of different regional classification model trainings for adjacent
Production Units (see
<a href="#sec-production-units" class="quarto-xref">Section 7.2</a>),
where the distribution of the probabilities is different according to
actual regional differences in the present land cover. In general, areas
with lower confidence are typically concentrated in transition areas
between different land cover types or biogeographical transition areas,
with a higher degree of mixed spectral-temporal signatures from mixed
land cover types.

<div id="fig-figure18">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-dce450dddbdcde7b15953ed341a6d06ccee0784e.png"
style="width:6.27in"
data-fig-alt="Choropleth map displaying the Raster Confidence Layer (Data Score Layer) for the CLCplus Backbone product, covering EEA38 Member States plus the United Kingdom, in 2023. The map includes insets for the Azores Islands and the Canary and Madeira Islands. The confidence values range from 0 (Low, represented by yellow) to 100 (High, represented by blue-green). The geographic area spans from approximately 10°W to 70°E longitude and 30°N to 60°N latitude. Areas of high confidence (blue-green) are predominantly found in Central, Western, and Northern Europe, including the UK, Ireland, France, Germany, Poland, the Baltic states, and much of Fennoscandia. Areas of lower confidence (yellow/orange) are visible in Southern Europe, specifically across the Iberian Peninsula (Spain, Portugal), parts of Italy, Greece, and Turkey. Iceland and some coastal areas of Norway also show lower confidence values. The main map includes a scale bar indicating 0 to 1,000 km. The insets for the Azores Islands and Canary and Madeira Islands each include a scale bar indicating 0 to 300 km. The map&#39;s geometric resolution is 10m x 10m pixel-based."
alt="Choropleth map displaying the Raster Confidence Layer (Data Score Layer) for the CLCplus Backbone product, covering EEA38 Member States plus the United Kingdom, in 2023. The map includes insets for the Azores Islands and the Canary and Madeira Islands. The confidence values range from 0 (Low, represented by yellow) to 100 (High, represented by blue-green). The geographic area spans from approximately 10°W to 70°E longitude and 30°N to 60°N latitude. Areas of high confidence (blue-green) are predominantly found in Central, Western, and Northern Europe, including the UK, Ireland, France, Germany, Poland, the Baltic states, and much of Fennoscandia. Areas of lower confidence (yellow/orange) are visible in Southern Europe, specifically across the Iberian Peninsula (Spain, Portugal), parts of Italy, Greece, and Turkey. Iceland and some coastal areas of Norway also show lower confidence values. The main map includes a scale bar indicating 0 to 1,000 km. The insets for the Azores Islands and Canary and Madeira Islands each include a scale bar indicating 0 to 300 km. The map&#39;s geometric resolution is 10m x 10m pixel-based." />

Figure 18: CLCplus Backbone Raster Confidence Layer 2023

</div>

Choropleth map displaying the Raster Confidence Layer (Data Score Layer)
for the CLCplus Backbone product, covering EEA38 Member States plus the
United Kingdom, in 2023. The map includes insets for the Azores Islands
and the Canary and Madeira Islands. The confidence values range from 0
(Low, represented by yellow) to 100 (High, represented by blue-green).
The geographic area spans from approximately 10°W to 70°E longitude and
30°N to 60°N latitude. Areas of high confidence (blue-green) are
predominantly found in Central, Western, and Northern Europe, including
the UK, Ireland, France, Germany, Poland, the Baltic states, and much of
Fennoscandia. Areas of lower confidence (yellow/orange) are visible in
Southern Europe, specifically across the Iberian Peninsula (Spain,
Portugal), parts of Italy, Greece, and Turkey. Iceland and some coastal
areas of Norway also show lower confidence values. The main map includes
a scale bar indicating 0 to 1,000 km. The insets for the Azores Islands
and Canary and Madeira Islands each include a scale bar indicating 0 to
300 km. The map’s geometric resolution is 10m x 10m pixel-based.

<div id="fig-figure19">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-30f84d5430161602116c020f37687fa15d9cb6f1.png"
style="width:6.15in"
data-fig-alt="This map displays the spatial distribution of Confidence Values for the Copernicus Land Monitoring Service (CLMS) CLC+ (next-generation CORINE Land Cover) Backbone Raster Data Score Layer (RASDL), likely for the reference year 2023. The map shows a landscape featuring numerous lakes, predominantly rendered in dark blue. A legend in the top right corner indicates &#39;Confidence Value,&#39; with a colour gradient ranging from green for &#39;High : 100&#39; to blue for &#39;Low : 0,&#39; passing through yellow and orange. Areas of high confidence (bright green) are widely distributed, interspersed with areas of lower confidence (yellow and orange). Dark blue regions correspond to very low confidence values, most notably for the large bodies of water. The map appears to be composed of two adjacent map tiles, with a vertical seam slightly right of the center. The visual pattern suggests a varied confidence level across the landscape, with water bodies consistently showing the lowest confidence values."
alt="This map displays the spatial distribution of Confidence Values for the Copernicus Land Monitoring Service (CLMS) CLC+ (next-generation CORINE Land Cover) Backbone Raster Data Score Layer (RASDL), likely for the reference year 2023. The map shows a landscape featuring numerous lakes, predominantly rendered in dark blue. A legend in the top right corner indicates &#39;Confidence Value,&#39; with a colour gradient ranging from green for &#39;High : 100&#39; to blue for &#39;Low : 0,&#39; passing through yellow and orange. Areas of high confidence (bright green) are widely distributed, interspersed with areas of lower confidence (yellow and orange). Dark blue regions correspond to very low confidence values, most notably for the large bodies of water. The map appears to be composed of two adjacent map tiles, with a vertical seam slightly right of the center. The visual pattern suggests a varied confidence level across the landscape, with water bodies consistently showing the lowest confidence values." />

Figure 19: Closeup of the RASCL showing edges as a result of separate
training models per production unit

</div>

This map displays the spatial distribution of Confidence Values for the
Copernicus Land Monitoring Service (CLMS) CLC+ (next-generation CORINE
Land Cover) Backbone Raster Data Score Layer (RASDL), likely for the
reference year 2023. The map shows a landscape featuring numerous lakes,
predominantly rendered in dark blue. A legend in the top right corner
indicates “Confidence Value,” with a colour gradient ranging from green
for “High : 100” to blue for “Low : 0,” passing through yellow and
orange. Areas of high confidence (bright green) are widely distributed,
interspersed with areas of lower confidence (yellow and orange). Dark
blue regions correspond to very low confidence values, most notably for
the large bodies of water. The map appears to be composed of two
adjacent map tiles, with a vertical seam slightly right of the center.
The visual pattern suggests a varied confidence level across the
landscape, with water bodies consistently showing the lowest confidence
values.

<div id="fig-figure20">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-59c1dd0915814ee2101e85c9ab825da1feea60d1.png"
style="width:6.27in"
data-fig-alt="A bar chart showing the distribution of Confidence values for the Raster Data Score Layer (RASCL) of the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone 2023 product. The X-axis represents &#39;Confidence&#39; ranging from 0 to 100, and the Y-axis represents &#39;Fraction&#39; as a percentage, ranging from 0% to 18%. The distribution is heavily skewed towards higher confidence values. Confidence values between 0 and approximately 60 have very low fractions, generally less than 1%. The fraction gradually increases from around 60 Confidence, rising sharply for values above 90. The highest fraction, approximately 15.8%, is observed at a Confidence value of 100."
alt="A bar chart showing the distribution of Confidence values for the Raster Data Score Layer (RASCL) of the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone 2023 product. The X-axis represents &#39;Confidence&#39; ranging from 0 to 100, and the Y-axis represents &#39;Fraction&#39; as a percentage, ranging from 0% to 18%. The distribution is heavily skewed towards higher confidence values. Confidence values between 0 and approximately 60 have very low fractions, generally less than 1%. The fraction gradually increases from around 60 Confidence, rising sharply for values above 90. The highest fraction, approximately 15.8%, is observed at a Confidence value of 100." />

Figure 20: Distribution and fractions of values in the Raster Confidence
Layer (RASCL) of CLCplus Backbone 2023 across the EEA38+UK

</div>

A bar chart showing the distribution of Confidence values for the Raster
Data Score Layer (RASCL) of the Copernicus Land Monitoring Service
(CLMS) CLCplus Backbone 2023 product. The X-axis represents “Confidence”
ranging from 0 to 100, and the Y-axis represents “Fraction” as a
percentage, ranging from 0% to 18%. The distribution is heavily skewed
towards higher confidence values. Confidence values between 0 and
approximately 60 have very low fractions, generally less than 1%. The
fraction gradually increases from around 60 Confidence, rising sharply
for values above 90. The highest fraction, approximately 15.8%, is
observed at a Confidence value of 100.

The distribution of the raster confidence values is displayed in
<a href="#fig-figure20" class="quarto-xref">Figure 20</a>. It shows a
significant increase of confidence values from approximately 90%
upwards. Overall, approximately 69% of all classified pixels were
assigned to the respective dominant class (out of max. 11 classes) with
a confidence of ≥50%. Considering the classifier’s general difficulty to
distinguish between up to 11 classes (depending on the present land
cover in the respective regions), this shows that the classifier was
able to draw on a sufficiently large data and sample basis, to resolve
most uncertainties in the class assignment. While this measure of
uncertainty is not always a good proxy for the distribution of errors
(i.e. in case of spectral-temporal similarity, the classification can
still commit an error with high confidence), it is worth noting that
areas with lower confidence generally coincide with areas where land
cover classification is generally more difficult, e.g. due to very dry
conditions, short vegetation periods, or generally high cloud cover
(i.e. Southern Europe, Norway and Iceland).

#### File naming convention

The filenames for the CLCplus Backbone Raster Confidence Layer (RASCL)
are composed of the following elements:

*Prefix_DataTheme_DataSub-Theme_TemporalReference_DataTypeSpatialResolution_SpatialExtent_EPSGCode_VersionNumber_RevisionNumber*

**➔ CLMS_CLCPLUS_RASCL_S2023_R10m_EXXNXX_03035_V01_R00**

Where:

|  |  |
|----|----|
| Prefix: CLMS | SpatialResolution (SpatialResolutionUnit): 10m |
| DataTheme: CLCPLUS | SpatialExtent: EXXNXX or GF, GP, MQ, RE, YT for French DOMs |
| DataSub-Theme: RASCL | EPSGCode: 03035 (or EPSG codes for national projections of DOMs) |
| TemporalReference: S2023 | VersionNumber: V01 |
| DataType: R; V | RevisionNumber: R00 |

The product specifications for the RASCL are summarized in Table 5.

Table 5: Technical specifications of the CLCplus Backbone Raster
Confidence Layer

| CLCplus Backbone Raster Confidence Layer / Acronym: RASCL / Product family: CLMS_CLCplus |
|----|
| **Summary**: The Confidence Layer is a 10m pixel-based auxiliary layer for the CLCplus Backbone RAS. It provides information about the reliability of the land cover class assignment per pixel. |
| **Reference year**: 2023 |
| **Geometric resolution**: Pixel resolution 10m x 10m, fully conform with the EEA reference grid |
| **Coordinate Reference System**: European ETRS89 LAEA projection / WGS84 and the respective UTM zone for French DOMs |
| **Coverage**: 6.002.105 km² (covering the full EEA38 + UK) |
| **Geometric accuracy (positioning scale)**: equals the Sentinel-2 positional accuracy in 2023 (\<9m at 95.5% confidence) |
| **Data type**: 8bit unsigned raster with LZW compression |
| **Minimum Mapping Unit (MMU)**: Pixel-based (no MMU) |
| **Attributes**: Value, Count, Confidence |
| **Raster coding**: <br> 0-100: Confidence values <br> 254: Outside area |
| **Metadata**: XML metadata files according to INSPIRE metadata standards |
| **Delivery format**: Cloud optimized GeoTIFFs as 100x100km tiles incl. pyramids and embedded colour map (\*.tif), attribute table (\*.aux.xml), and INSPIRE-compliant metadata in XML format (\*.xml) |

### Raster Post-processing Layer

The Raster Post-Processing Layer (RASPL) provides the information, if a
pixel’s class has been changed during the post-processing (more detailed
info provided in AD-1).

The RASPL for the CLCplus Backbone 2023 is shown in
<a href="#fig-figure21" class="quarto-xref">Figure 21</a>. The green
areas represent these re-coded and thus improved areas. The
post-processing rulesets were intentionally tailored to be rather
conservative and introduce adaptations only where auxiliary layers
provide very reliable information. This is reflected in the very small
fraction of pixels that underwent automated corrections (0.03%) during
the post-processing.

<div id="fig-figure21">

<img
src="CLCplus_Backbone_2023_PUM_v1-media/img-873fc1d0b90c1e8fea175db5a26fb19ff0db0f39.png"
style="width:6.27in"
data-fig-alt="Choropleth map displaying the extent of post-processing changes for the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone Raster Confidence Layer (RASCL) for the reference year 2023. The map covers Europe, including the Azores Islands and the Canary and Madeira Islands (shown in inset maps), within a geographic grid from 40°W to 70°E longitude and 30°N to 60°N latitude. The legend indicates two categories: * **White**: &#39;No change during post-processing&#39; * **Green**: &#39;Recoded during post-processing&#39; The majority of the mapped area, covering continental Europe, the United Kingdom, Iceland, Ireland, and the included Atlantic islands (Azores, Canary, Madeira), is coloured white, signifying no changes during the post-processing phase. A small, distinct area in northern Fennoscandia (likely northern Norway and Finland) is coloured green, indicating that this region was &#39;Recoded during post-processing&#39;. The main map includes a scale bar showing distances of 0, 250, 500, and 1,000 km. The inset maps for Azores Is. and Canary and Madeira Is. each feature a scale bar showing distances of 0, 150, and 300 km."
alt="Choropleth map displaying the extent of post-processing changes for the Copernicus Land Monitoring Service (CLMS) CLCplus Backbone Raster Confidence Layer (RASCL) for the reference year 2023. The map covers Europe, including the Azores Islands and the Canary and Madeira Islands (shown in inset maps), within a geographic grid from 40°W to 70°E longitude and 30°N to 60°N latitude. The legend indicates two categories: * **White**: &#39;No change during post-processing&#39; * **Green**: &#39;Recoded during post-processing&#39; The majority of the mapped area, covering continental Europe, the United Kingdom, Iceland, Ireland, and the included Atlantic islands (Azores, Canary, Madeira), is coloured white, signifying no changes during the post-processing phase. A small, distinct area in northern Fennoscandia (likely northern Norway and Finland) is coloured green, indicating that this region was &#39;Recoded during post-processing&#39;. The main map includes a scale bar showing distances of 0, 250, 500, and 1,000 km. The inset maps for Azores Is. and Canary and Madeira Is. each feature a scale bar showing distances of 0, 150, and 300 km." />

Figure 21: CLCplus Backbone Raster Post-Processing Layer (RASPL) 2023

</div>

Choropleth map displaying the extent of post-processing changes for the
Copernicus Land Monitoring Service (CLMS) CLCplus Backbone Raster
Confidence Layer (RASCL) for the reference year 2023. The map covers
Europe, including the Azores Islands and the Canary and Madeira Islands
(shown in inset maps), within a geographic grid from 40°W to 70°E
longitude and 30°N to 60°N latitude.

The legend indicates two categories: \* **White**: “No change during
post-processing” \* **Green**: “Recoded during post-processing”

The majority of the mapped area, covering continental Europe, the United
Kingdom, Iceland, Ireland, and the included Atlantic islands (Azores,
Canary, Madeira), is coloured white, signifying no changes during the
post-processing phase. A small, distinct area in northern Fennoscandia
(likely northern Norway and Finland) is coloured green, indicating that
this region was “Recoded during post-processing”.

The main map includes a scale bar showing distances of 0, 250, 500, and
1,000 km. The inset maps for Azores Is. and Canary and Madeira Is. each
feature a scale bar showing distances of 0, 150, and 300 km.

File naming convention

The filenames for RASPL are composed of the following elements:

*Prefix_DataTheme_DataSub-Theme_TemporalReference_DataTypeSpatialResolution_SpatialExtent_EPSGCode_VersionNumber_RevisionNumber*

**➔ CLMS_CLCPLUS_RASPL_S2023_R10m_EXXNXX_03035_V01_R00**

Where:

|  |  |
|----|----|
| Prefix: CLMS | SpatialResolution (SpatialResolutionUnit): 10m |
| DataTheme: CLCPLUS | SpatialExtent: EXXNXX or GF, GP, MQ, RE, YT for French DOMs |
| DataSub-Theme: RASPL | EPSGCode: 03035 (or EPSG codes for national projections of DOMs) |
| TemporalReference: S2023 | VersionNumber: V01 |
| DataType: R; V | RevisionNumber: R00 |

The product specifications for the CLCplus Backbone Raster
Post-Processing Layer (RASPL) are summarized in Table 6.

Table 6: Technical specifications of the Raster Post-Processing Layer

| CLCplus Backbone Raster Post-Processing Layer / Acronym: RASPL / Product family: CLMS_CLCplus |
|----|
| Summary: The Post-Processing Layer is a 10m pixel-based auxiliary layer for the CLCplus Backbone RAS. It provides information of pixels that were re-coded during post-processing of the raster classification. |
| Reference year: 2023 |
| Geometric resolution: Pixel resolution 10m x 10m, fully conform with the EEA reference grid |
| Coordinate Reference System: European ETRS89 LAEA projection / WGS84 and the respective UTM zone for French DOMs |
| Coverage: 6,002,168 km² (covering the full EEA38 + UK) |
| Geometric accuracy (positioning scale): equals the Sentinel-2 positional accuracy in 2023 (\<9m at 95.5% confidence) |
| Data type: 8bit unsigned raster with LZW compression |
| Minimum Mapping Unit (MMU): Pixel-based (no MMU) |
| Raster coding <br> 0: No change during post-processing <br> 1: Recoded during post-processing <br> 254: Outside area |
| Attributes: Value, Count, Class_name |
| Metadata: XML metadata files according to INSPIRE metadata standards |
| Delivery format: Cloud optimized GeoTIFFs as 100x100km tiles incl. pyramids and embedded colour map (\*.tif), attribute table (\*.aux.xml), and INSPIRE-compliant metadata in XML format (\*.xml) |

# Product methodology and workflow

This section provides a brief overview on the implemented methodology.
For full detail on the input data used and the single processing steps,
please refer to the Algorithm Theoretical Basis Document \[AD-1\].

## Input data

The main input data source for the raster classification is Sentinel-2
time-series data covering the reference year ±3 months. Initially, all
Sentinel-2 scenes at L2A (i.e. at-surface reflectance) and with a cloud
coverage lower than 80% are fed into the production chain. More
specifically the Sentinel-2 bands B1, B3, B4, B5, B8, B9, B11, B12 and
four derived spectral indices, i.e. the NDVI, the Normalized Difference
Water Index (NDWI), the Normalized Difference Moisture Index (NDMI) and
the Normalized Burnt Ratio (NBR) are used.

The training and test data, required for the model calibration, is based
on the sample data base (Sample DB) from the initial CLCplus Backbone
2018 production and updated with every subsequent production to account
for changes over time. In total, more than 1 million sample point are
used for CLCplus Backbone production.

## Production units

Considering the diversity of the European landscapes and to ensure
high-accuracy mapping within CLCplus Backbone, all main processing
steps, such as algorithm training, testing or final land cover
classification, are performed along substrata. These substrata are based
on biogeographical regions (Metzger et al. 2013) and further consider
roughly the national boundaries (with regards to prioritized production
of the EU27) as well as a maximum size for processing efficiency. The
entire production area (EEA38+UK and French DOMs) is stratified into 138
substrata, the Production Units (PU).

## Time series classification

The time series classification comprises three main steps, i.e. the time
series extraction, the classification model training and the roll out of
the trained model, computing the actual land cover classification.

The classifier used is a Temporal Convolutional Neural Network (TempCNN)
classifier, which is a state-of-the-art classifier for satellite image
time series analysis and outperforms other algorithms, such as Recurrent
Neural Networks (RNNs), as described in Pelletier et al. (2019).

## Post-processing

The post-processing steps comprise 1) bilateral filtering of the class
probabilities, 2) blending of the probabilities along production unit
borders and 3) a cross-calibration with the class probabilities from the
previous 2018 and 2021 productions to ensure best possible product
consistency. The cross-calibration still allows for changes in the land
cover, where there has indeed been a change, as well as for enhancements
and correction of areas with lower accuracy in previous productions.
Further optional post-processing is applied to areas with remaining
issues. As a last post-processing step, the coastal water area is
recoded to separate it from the inland water (i.e. auxiliary class 253).

# Terms of use and product technical support

## Terms of use

The Terms of Use for the product(s) described in this document
acknowledge the following:

Free, full and open access to the products and services of the
Copernicus Land Monitoring Service is made on the conditions that:

1.  When distributing or communicating Copernicus Land Monitoring
    Service products and services (data, software scripts, web services,
    user and methodological documentation and similar) to the public,
    users shall inform the public of the source of these products and
    services and shall acknowledge that the Copernicus Land Monitoring
    Service products and services were produced “with funding by the
    European Union”.

2.  Where the Copernicus Land Monitoring Service products and services
    have been adapted or modified by the user, the user shall clearly
    state this.

3.  Users shall make sure not to convey the impression to the public
    that the user’s activities are officially endorsed by the European
    Union.

The user has all intellectual property rights to the products he/she has
created based on the Copernicus Land Monitoring Service products and
services.

Consult [Data policy — Copernicus Land Monitoring
Service](https://land.copernicus.eu/en/data-policy) for further details.

## Citation

When planning a publication (scientific, commercial, etc.), it shall
explicitly mention:

“This publication has been prepared using European Union’s Copernicus
Land Monitoring Service information; \<insert all relevant DOI links
here, if applicable\>”

When developing a product or service using the products or services of
the Copernicus Land Monitoring Service, it shall explicitly mention:

“Generated using European Union’s Copernicus Land Monitoring Service
information;\<insert all relevant DOI links here, if applicable\>”

When redistributing a part of the Copernicus Land Monitoring Service
(product, dataset, documentation, picture, web service, etc.), it shall
explicitly mention:

“European Union’s Copernicus Land Monitoring Service information;
\<insert all relevant DOI links here, if applicable\>”

Consult Data policy — Copernicus Land Monitoring Service for further
details.

## Product technical support

Product technical support is provided by the product custodian through
[Copernicus Land Monitoring Service – Service
desk](https://land.copernicus.eu/en/contact-service-helpdesk). Product
technical support does not include software specific user support or
general GIS or remote sensing support.

More information on the products can be found on the Copernicus Land
Monitoring Service website <https://land.copernicus.eu/>.

# List of abbreviations & acronyms

| Abbreviation | Name | Reference |
|----|----|----|
| AD | Applicable Document |  |
| AOI | Area of Interest |  |
| BB | (Corine Land Cover plus) Backbone |  |
| CLC | CORINE Land Cover |  |
| CLCplus | CORINE Land Cover plus |  |
| CLMS | Copernicus Land Monitoring Service | <https://land.copernicus.eu/en> |
| DOMs | French Overseas Departments |  |
| EAGLE | Eionet Action Group on Land monitoring in Europe |  |
| EEA | European Environment Agency | [www.eea.europa.eu](www.eea.europa.eu) |
| EEA38 | The 32 member and 6 cooperating countries of the EEA | <https://land.copernicus.eu/en/faq/general-questions/what-is-eea38> |
| EO | Earth Observation |  |
| ETRS89 | European Terrestrial Reference System 1989 |  |
| GIS | Geographic Information System |  |
| HR | High resolution |  |
| IACS | Integrated Administration and Control System | [Managing payments - European Commission](https://agriculture.ec.europa.eu/common-agricultural-policy/financing-cap/assurance-and-audit/managing-payments_en) |
| INSPIRE | Infrastructure for Spatial Information in Europe | <https://knowledge-base.inspire.ec.europa.eu/index_en> |
| LAEA | Lambert Azimuthal Equal Area |  |
| LC | Land cover |  |
| LCC | Eagle Land Cover Component |  |
| LC/LU | Land cover / land use |  |
| LPIS | Land Parcel Identification System | [LPIS - land parcel identification system a.k.a. identification system for agricultural parcels -Guidance and Tools for CAP (GTCAP) - EC Public Wiki](https://wikis.ec.europa.eu/spaces/GUIDANCEANDTOOLSFORCAP/pages/86968605/LPIS+-+land+parcel+identification+system+a.k.a.+identification+system+for+agricultural+parcels) |
| LULUCF | Land Use and Land Use-Change and Forestry |  |
| L2A | Level 2A (processing level of Sentinel-2 satellite data) |  |
| MMU | Minimum Mapping Unit |  |
| NBR | Normalized Burnt Ratio |  |
| NDMI | Normalized Difference Moisture Index |  |
| NDVI | Normalized Difference Vegetation Index |  |
| NDSI | Normalized Difference Snow Index |  |
| NDWI | Normalized Difference Water Index |  |
| RAS | CLCplus BB Raster Product |  |
| RASCL | CLCplus BB Raster Confidence Layer |  |
| RASDL | CLCplus BB Raster Data Score Layer |  |
| RASPL | CLCplus BB Raster Post-Processing Layer |  |
| SCL | Scene Classification Layer |  |
| S-2 | Sentinel-2 |  |
| UK | United Kingdom |  |
| VHR | Very High Resolution |  |

# References {sec-references}

- European Commission (2018). Regulation (EU) 2018/841 of the European
  Parliament and of the Council of 30 May 2018 on the inclusion of
  greenhouse gas emissions and removals from land use, land use change
  and forestry in the 2030 climate and energy framework, and amending
  Regulation (EU) No 525/2013 and Decision No 529/2013/EU (Text with EEA
  relevance). <https://eur-lex.europa.eu/eli/reg/2018/841/oj/eng>
  \[2025-01-31\]

- European Commission (2023). Regulation (EU) 2023/839 of the European
  Parliament and of the Council of 19 April 2023 amending Regulation
  (EU) 2018/841 as regards the scope, simplifying the reporting and
  compliance rules, and setting out the targets of the Member States for
  2030, and Regulation (EU) 2018/1999 as regards improvement in
  monitoring, reporting, tracking of progress and review (Text with EEA
  relevance). <https://eur-lex.europa.eu/eli/reg/2023/839/oj>
  \[2025-01-31\]

- Metzger, M. J., Bunce, R. G., Jongman, R. H., Sayre, R., Trabucco, A.,
  & Zomer, R. (2013). A high-resolution bioclimate map of the world: a
  unifying framework for global biodiversity research and monitoring.
  *Global Ecology and Biogeography*, 22(5), 630-638.

- Pelletier, C., Webb G.I. & Petitjean, F. (2019). Temporal
  Convolutional Neural Network for the Classification of Satellite Image
  Time Series. Remote Sensing 11, no. 5: 523.
  [https://doi.org/10.3390/rs11050523](https://www.mdpi.com/2072-4292/11/5/523)

# Annexes

## Annex 1: Colour palettes

The CLCplus Backbone products are delivered with embedded colormaps.
Additionally, symbology files in .lyr, .qml and .sld format are
available.

### Raster Product (RAS)

<img src="CLCplus_Backbone_2023_PUM_v1-media/RasterProduct.png"
style="width:6.19in"
data-fig-alt="This table presents a land cover classification scheme, listing 14 distinct classes, their numerical codes, and associated RGB colour values with a visual palette representation. The classes are: | Class name | Class code | Colour (R,G,B) | Colour (Palette) | |---|---|---|---| | Sealed | 1 | 255, 0, 0 | Red | | Woody needle leaved trees | 2 | 34, 139, 34 | Dark Green | | Woody broadleaved deciduous trees | 3 | 128, 255, 0 | Light Green | | Woody broadleaved evergreen trees | 4 | 0, 255, 8 | Bright Green | | Low-growing woody plants | 5 | 128, 64, 0 | Brown | | Permanent herbaceous | 6 | 204, 242, 77 | Yellow-Green | | Periodically herbaceous | 7 | 255, 255, 128 | Yellow | | Lichens and mosses | 8 | 255, 128, 255 | Magenta | | Non and sparsely vegetated | 9 | 191, 191, 191 | Grey | | Water | 10 | 0, 128, 255 | Blue | | Snow and ice | 11 | 0, 255, 255 | Cyan | | Coastal seawater buffer | 253 | 191, 223, 255 | Light Blue | | Outside area | 254 | 230, 230, 230 | Light Grey | | No data | 255 | 0, 0, 0 | Black | The table provides a standard legend for interpreting land cover mapping products, with specific class codes and precise RGB colour definitions for each category, including various vegetation types, water bodies, and non-vegetated or artificial surfaces."
alt="Colour palette for the Raster (RAS) Product" />

This table presents a land cover classification scheme, listing 14
distinct classes, their numerical codes, and associated RGB colour
values with a visual palette representation. The classes are: \| Class
name \| Class code \| Colour (R,G,B) \| Colour (Palette) \|
\|—\|—\|—\|—\| \| Sealed \| 1 \| 255, 0, 0 \| Red \| \| Woody needle
leaved trees \| 2 \| 34, 139, 34 \| Dark Green \| \| Woody broadleaved
deciduous trees \| 3 \| 128, 255, 0 \| Light Green \| \| Woody
broadleaved evergreen trees \| 4 \| 0, 255, 8 \| Bright Green \| \|
Low-growing woody plants \| 5 \| 128, 64, 0 \| Brown \| \| Permanent
herbaceous \| 6 \| 204, 242, 77 \| Yellow-Green \| \| Periodically
herbaceous \| 7 \| 255, 255, 128 \| Yellow \| \| Lichens and mosses \| 8
\| 255, 128, 255 \| Magenta \| \| Non and sparsely vegetated \| 9 \|
191, 191, 191 \| Grey \| \| Water \| 10 \| 0, 128, 255 \| Blue \| \|
Snow and ice \| 11 \| 0, 255, 255 \| Cyan \| \| Coastal seawater buffer
\| 253 \| 191, 223, 255 \| Light Blue \| \| Outside area \| 254 \| 230,
230, 230 \| Light Grey \| \| No data \| 255 \| 0, 0, 0 \| Black \| The
table provides a standard legend for interpreting land cover mapping
products, with specific class codes and precise RGB colour definitions
for each category, including various vegetation types, water bodies, and
non-vegetated or artificial surfaces.

### Data Score Layer (RASDL)

<img src="CLCplus_Backbone_2023_PUM_v1-media/DataScoreLayer.png"
style="width:3.69in"
data-fig-alt="| Number of cloud free observations | Colour (R,G,B) | Colour (Palette) | |---|---|---| | &gt; 200 | 0, 97, 0 | (dark green) | | 150 | 122, 171, 0 | (mid-green) | | 100 | 255, 255, 0 | (yellow) | | 50 | 255, 153, 0 | (orange) | | 0 | 255, 34, 0 | (red) | This table defines a colour palette for visualising the number of cloud-free observations, mapping higher counts (greater than 200) to a dark green (0, 97, 0) and lower counts (0) to a red (255, 34, 0), transitioning through mid-green (122, 171, 0), yellow (255, 255, 0), and orange (255, 153, 0)."
alt="Colour palette for the Data Score Layer" />

| Number of cloud free observations | Colour (R,G,B) | Colour (Palette) |
|-----------------------------------|----------------|------------------|
| \> 200                            | 0, 97, 0       | (dark green)     |
| 150                               | 122, 171, 0    | (mid-green)      |
| 100                               | 255, 255, 0    | (yellow)         |
| 50                                | 255, 153, 0    | (orange)         |
| 0                                 | 255, 34, 0     | (red)            |

This table defines a colour palette for visualising the number of
cloud-free observations, mapping higher counts (greater than 200) to a
dark green (0, 97, 0) and lower counts (0) to a red (255, 34, 0),
transitioning through mid-green (122, 171, 0), yellow (255, 255, 0), and
orange (255, 153, 0).

### Raster Confidence Layer (RASCL)

<img src="CLCplus_Backbone_2023_PUM_v1-media/RasterConfidenceLayer.png"
style="width:3.69in"
data-fig-alt="| Confidence value [%] | Colour (R,G,B) | Colour (Palette) | |---|---|---| | 100 | 12, 47, 122 | (dark blue) | | 80 | 32, 153, 143 | (teal green) | | 60 | 0, 219, 0 | (bright green) | | 40 | 255, 255, 0 | (yellow) | | 20 | 237, 161, 19 | (orange) | | 0 | 194, 82, 60 | (red-brown) | This table defines a colour scale for visualising confidence values ranging from 0% to 100%, assigning specific RGB colour codes to each 20% interval, transitioning from dark blue for 100% confidence to red-brown for 0% confidence."
alt="Colour palette for the Raster Confidence Layer" />

| Confidence value \[%\] | Colour (R,G,B) | Colour (Palette) |
|------------------------|----------------|------------------|
| 100                    | 12, 47, 122    | (dark blue)      |
| 80                     | 32, 153, 143   | (teal green)     |
| 60                     | 0, 219, 0      | (bright green)   |
| 40                     | 255, 255, 0    | (yellow)         |
| 20                     | 237, 161, 19   | (orange)         |
| 0                      | 194, 82, 60    | (red-brown)      |

This table defines a colour scale for visualising confidence values
ranging from 0% to 100%, assigning specific RGB colour codes to each 20%
interval, transitioning from dark blue for 100% confidence to red-brown
for 0% confidence.

### Post-Processing Layer (RASPL)

<img
src="CLCplus_Backbone_2023_PUM_v1-media/RasterPost-ProcessingLayer.png"
style="width:5.78in"
data-fig-alt="| Class name | Class code | Colour (R,G,B) | Colour (Palette) | | :----------------------------- | :--------- | :------------- | :--------------- | | No change during post-processing | 0 | 240, 240, 240 | Light grey | | Recoded during post-processing | 1 | 112, 168, 0 | Green | | Outside area | 254 | 0, 0, 0 | Black | This table defines a classification scheme for land cover data, specifying three categories based on their status during post-processing: &#39;No change during post-processing&#39; (Class code 0, light grey), &#39;Recoded during post-processing&#39; (Class code 1, green), and &#39;Outside area&#39; (Class code 254, black), each with a unique RGB colour value for mapping."
alt="Colour palette for the Raster Post-processing Layer" />

| Class name                       | Class code | Colour (R,G,B) | Colour (Palette) |
|:---------------------------------|:-----------|:---------------|:-----------------|
| No change during post-processing | 0          | 240, 240, 240  | Light grey       |
| Recoded during post-processing   | 1          | 112, 168, 0    | Green            |
| Outside area                     | 254        | 0, 0, 0        | Black            |

This table defines a classification scheme for land cover data,
specifying three categories based on their status during
post-processing: “No change during post-processing” (Class code 0, light
grey), “Recoded during post-processing” (Class code 1, green), and
“Outside area” (Class code 254, black), each with a unique RGB colour
value for mapping.

## Annex 2: Projection parameters

Except for French DOMs, all CLCplus Backbone 2023 layers are produced
and delivered in the European LAEA projection (EPSG: 3035), which is
defined according to the following WKT (WellKnown Text representation):

``` markdown
PROJCS["ETRS89-extended / LAEA Europe",
    GEOGCS["ETRS89",
      DATUM["European_Terrestrial_Reference_System_1989",
        SPHEROID["GRS 1980",6378137,298.257222101,
          AUTHORITY["EPSG","7019"]],
        AUTHORITY["EPSG","6258"]],
      PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
      UNIT["degree",0.0174532925199433,
        AUTHORITY["EPSG","9122"]],
      AUTHORITY["EPSG","4258"]],
    PROJECTION["Lambert_Azimuthal_Equal_Area"],
    PARAMETER["latitude_of_center",52],
    PARAMETER["longitude_of_center",10],
    PARAMETER["false_easting",4321000],
    PARAMETER["false_northing",3210000],
    UNIT["metre",1,
      AUTHORITY["EPSG","9001"]],
    AXIS["Northing",NORTH],
    AXIS["Easting",EAST],
    AUTHORITY["EPSG","3035"]]
```

# Document history

| Version | Date       | Short description of changes |
|---------|------------|------------------------------|
| 1.2     | 01.04.2025 | Initial published issue      |

# Applicable documents

| ID | Applicable Document |
|----|----|
| AD-1 | [CLCplus Backbone 2023 - Algorithm Theoretical Basis Document (ATBD)](https://land.copernicus.eu/en/products/clc-backbone?tab=documentation) |
