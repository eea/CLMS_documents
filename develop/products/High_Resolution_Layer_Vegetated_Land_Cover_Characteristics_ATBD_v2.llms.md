# High Resolution Layer Vegetated Land Cover Characteristics - Algorithm Theoretical Basis Document

Copernicus Land Monitoring Service

Published

June 27, 2025

Keywords

{keywords_str}

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

# 1 Executive summary

Copernicus is the European Union’s Earth Observation Programme. It offers information services based on satellite Earth observation and in situ (non-space) data. These information services are freely and openly accessible to its users through six thematic Copernicus services (Atmosphere Monitoring, Marine Environment Monitoring, Land Monitoring, Climate Change, Emergency Management and Security).

The Copernicus Land Monitoring Service (CLMS) is jointly implemented by the European Environment Agency and the European Commission’s DG Joint Research Centre (JRC) and provides geographical information on land cover and its changes, land use, vegetation state, water cycle and earth surface energy variables to a broad range of users in Europe and across the world in the field of environmental terrestrial applications. Within this service, the HighResolution Vegetated Land Cover Characteristics (HRL VLCC) product suite provides detailed annual maps and change layers for Tree Cover & Forests, Grasslands, and Croplands at resolutions of 10 meters (status layers) and 20 meters (change layers). The High-Resolution Vegetated Land Cover Characteristics products extend the time-series of the existing HRLs Forest and Grassland and complements the CLMS portfolio with new layer dedicated to the mapping of Crop Types and Agricultural practices such as mowing, harvest and cover crops.

The HRL VLCC products leverage advanced algorithms and multi-source satellite data, including Sentinel-2 imagery, to ensure high thematic accuracy. Key innovations include the Base Vegetation Layer (BVL), which harmonizes classifications across land cover types, and new agricultural monitoring capabilities such as crop type identification, ploughing indicators, and grassland mowing event detection. Complementary confidence layers quantify classification reliability for enhanced decision-making.

This document serves as a critical resource for understanding the scientific rigor behind HRL VLCC products, enabling their effective application in biodiversity conservation, agricultural monitoring, climate change adaptation, and compliance with EU policies such as the Common Agricultural Policy (CAP) and LULUCF regulation.

# 2 Background of the document

## 2.1 Scope

The Algorithm Theoretical Basis Document (ATBD) for the High-Resolution Vegetated Land Cover Characteristics (HRL VLCC) offers a comprehensive overview of the methodologies, algorithms, and workflows underpinning the generation of the HRL VLCC products.

## 2.2 Content and structure

In more detail, the document is structured as follows:

- Chapter 1 contains the executive summary of the project together with a general information about European Union’s Earth Observation Programme and Copernicus Land Monitoring Service (CLMS),

- Chapter 2 details the scope, content and structure of this document with a list of applicable documents,

- Chapter 3 describes the general thematic content and product descriptions with the methodology and workflows,

- and the References and Annex Chapters list references to the cited literature and documents.

# 3 Product Description

## 3.1 Base Vegetation Layer

The Base Vegetation Layer (BVL) is an internal processing layer to ensure better base consistency between the VLCC product groups Croplands, Grasslands and Tree Cover & Forests. The BVL provides a gap-free yearly mapping of the areas with tree cover and cropland and/or grassland. It also classifies a background class which comprises non-vegetated areas (e.g. bare ground, urban areas, water), lichens and mosses as well as shrubs (as long as not for agriculture such as vineyards). This section details the applied methods for the production of the BVL. An overview of the workflow is provided in Figure 1.

![This diagram illustrates the processing workflow for the Copernicus Land Monitoring Service (CLMS) High-Resolution Vegetated Land Cover Characteristics (HRL VLCC) product suite. The process begins with: 1. \*\*Scene selection\*\*: Utilizing the Sentinel-2 (S-2) archive, covering 5 reference years and a ±3 months temporal window, combined with Biogeographical strata for spatial context. 2. \*\*Regional model calibration\*\*: The selected scenes feed into a process that performs regional model calibration using a Temporal Convolutional Neural Network (TCNN). This calibration also integrates Multi-year training data (5 reference years, \>1 million points). The TCNN is trained to classify land cover into six categories: 1. Herbaceous, 2. Broadleaved trees, 3. Coniferous trees, 4. Cropland, 5. Tree crops (broadleaved), and 6. Other land cover. 3. \*\*Outlier detection and sample revision\*\*: Training data undergoes an outlier detection and sample revision step, which includes human intervention, providing feedback to refine the Multi-year training data. 4. \*\*Spatial-filtering\*\*: The calibrated regional models proceed to spatial filtering. 5. \*\*Spatial-blending\*\*: Filtered data is then spatially blended. 6. \*\*Multi-year probability time series\*\*: The blended data generates a Multi-year probability time series covering 2017 to 2021. 7. \*\*Tree cover change detection\*\*: This step calculates tree cover change (Δ) based on the multi-year probability time series. 8. \*\*Rule-based harmonization\*\*: Both the multi-year probability time series and the tree cover change detection results feed into rule-based harmonization to produce harmonized multi-year land cover maps (2017-2021). Outputs from the Multi-year probability time series and rule-based harmonization are then processed by specific land cover processors: \* \*\*Tree Cover & Forests Processor\*\*: Takes inputs for classes 2 (Broadleaved trees), 3 (Coniferous trees), and 5 (Tree crops broadleaved) from the Multi-year probability time series, as well as data from the Tree Cover Density (TCD) time-series. It also considers 'Overlap - Herbaceous - Tree Cover' (8). This processor feeds back into the TCD time-series. \* \*\*Grassland Processor\*\*: Processes class 1 (Herbaceous) from the Multi-year probability time series, 'Overlap - Herbaceous - Cropland' (7), and 'Overlap - Herbaceous - Tree Cover' (8). It also receives 'Fodder crops (within 8)' from the Cropland Processor. \* \*\*Cropland Processor\*\*: Processes class 4 (Cropland) and class 5 (Tree crops broadleaved) from the Multi-year probability time series, and 'Overlap - Herbaceous - Cropland' (7). It outputs 'Fodder crops (within 8)' to the Grassland Processor. The defined overlap categories are: 7. Overlap - Herbaceous - Cropland, and 8. Overlap - Herbaceous - Tree Cover.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-676c43b68eec6fd5be8bccbd542e4bc1c38175e2.png)

Figure 1: High-level flow chart of the BVL workflow and its usage by the downstream processors for Tree Cover & Forests, Grasslands and Croplands.

### 3.1.1 Input data

The main input data sources for the BVL are Sentinel-2 time-series covering the period for a respective reference years ± 3 months (e.g. for 2018 observations from 2016-10-01 till 2019-03-31 are considered). Initially the Scene Classification Layers (SCL) for all available S-2 L2A products and with a cloud coverage lower than 80% are retrieved and a time-series is constructed using the best (i.e. lowest cloud cover) scenes within a given spatio-temporal window. Typically,windows of 15 days and 20x20km are used, for parts of Scandinavia this has been augmented to 5 days and 10x10km to reduce the impact of frequent cloud cover.

The training / validation and test data required for the model calibration are compiled from various sources, such as from adjusted and filtered LUCAS (Eurostat, 2018) data of 2018, from stratified automated land cover (LC) class annotations based on existing land use/land cover maps, such as the CORINE Land Cover (CLC) 2018 and HRL Imperviousness 2018. Those are complemented with additional visual sample point photo-interpretation from Very High Resolution (VHR) imagery, Normalised Difference Vegetation Index (NDVI) time series and auxiliary datasets.

The initial training dataset comprises approximately 1.1 Million training points which are subjected to routines for detecting tree cover losses (based on NDVI time-series) as well as erroneous annotations and outliers related to general land cover changes (Cleanlab, Northcutt et al., 2021). Additional sampling is performed during the production on an ad hoc basis for particularly difficult areas.

### 3.1.2 Annual classification

Given the heterogeneity of the addressed European landscapes, all classifier training, testing and, finally, LC classification, is performed along substrata based on biogeographical regions (Metzger et al. 2013) and existing LC layers. The AOI is subdivided in 232 of these substrata which form the Production Units (PUs) (Figure 2). The goal of this stratification is to facilitate the fitting of the models to the regional specificities and thereby achieve a higher accuracy. The model architecture is a Temporal Convolutional Neural Network (TempCNN, Pelletier et al. 2019) which is trained with labels and filtered time-series (see section Input Data) of five reference years in the respective PU and a buffer area of 10km. Inference is performed on yearly time-series for the target reference year ± 3 months and outputs yearly probabilities for the 6 basic land cover classes:

1.  herbaceous vegetation;

2.  tree cover-broadleaved;

3.  tree cover-coniferous

4.  cropland;

5.  tree crops (i.e. nomenclature overlap between broadleaved tree cover and permanent crops in the HRL Croplands product);

6.  background class (including bare and sparsely vegetated areas and non-agricultural shrubs);

In a subsequent post-processing step two further classes are derived to delineate the:

7.  potential overlap herbaceous – cropland (i.e. pixels which are classified as cropland and herbaceous at least once in the time-series);

8.  The second derived class is derived from the intersection of all areas classified as tree cover and a preliminary version of the Tree Cover Density to delineate areas with low Tree Cover Density and hence allowed overlaps of herbaceous and tree cover.

The resulting Base Vegetation Layer is derived annually considering a time-window of five years (e.g. 2017 – 2021) to delineate the boundaries between grassland, cropland, tree cover and other land cover types (e.g. built-up areas, sealed areas, water, bare ground, permanent snow/ice, non-agricultural shrubs) not relevant for further processing steps within the HRL VLCC.

![This map displays the geographical coverage of Europe, including the main continental landmass and several Outermost Regions (ORs), delineated by national and sub-national administrative boundaries. The main map shows Europe with its internal administrative divisions, encompassing countries such as Iceland, Ireland, the United Kingdom, and the continental European Member States, extending eastward to include Turkey and some Balkan countries. Two inset maps provide magnified views of specific Outermost Regions: 1. Top-left inset: Four French overseas departments—Guadeloupe (GP), Martinique (MQ), Mayotte (YT), and Réunion (RE)—are shown with their coastlines. No scale bar is provided for this inset. 2. Middle-left inset: French Guiana (GF) is depicted with its internal administrative boundaries. This inset includes a scale bar indicating 0 km, 200 km, 400 km, and 600 km. A chain of small islands, likely including the Canary Islands (Spain), is visible in the bottom-left of the main map area. All land areas are uniformly shaded light grey with dark grey borders for clarity. The main map includes a scale bar at the bottom-right, marked with 0 km, 400 km, 800 km, and 1200 km. The map serves as a geographical reference, likely for Copernicus Land Monitoring Service (CLMS) data collection and reporting activities, such as for CORINE Land Cover (CLC) and High Resolution Layer (HRL) products.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-96d4f7ffe37f4b6d5ba2b5ac9886614e2b0e3258.jpg)

Figure 2: Production units subdividing the EEA-38 area into homogenous biogeographical substrata for the production of the BVL (GF: French Guiana, GP: Guadeloupe, MQ: Martinique, RE: Le Réunion, YT: Mayotte).

### 3.1.3 Post-classification processing

A sequence of post-processing steps is applied to improve the spatial and temporal consistency of the products. Spatial filtering aims to reduce salt and pepper noise and temporal filtering reduces frequent and implausible land cover changes (often along the class boundaries). The designation of overlap classes accounts for known overlaps in the nomenclatures and aims to minimize the inheritance of omission errors in the extent of herbaceous and cropland areas for further Grasslands and Croplands products.

An initial post-processing step involves applying bilateral filtering of the probabilities to reduce noise while preserving sharp spatial edges between land cover classes (Schindler 2012). This filtering is performed prior to rule-based harmonisation, ensuring that downstream products maintain spatially consistent classifications while avoiding excessive blurring at class boundaries and preserving ecologically meaningful edges. Subsequently the probabilities from any newly produced PU are blended with the readily available neighbouring PUs in an 10km overlap buffer. Within this buffer area the probabilities of all relevant PUs are averaged; the distance to the PU borders are used as a weight for the averaging to ensure seamless classification results.

In a further step change detection is performed to identify potential tree cover changes. To this end, the sum of the probabilities for tree cover (tree cover-broadleaved; tree cover-coniferous, tree crops) are considered; the difference of the sums is computed between the reference year at the intervals of the 3-yearly change layers (2018-2021-2024). Changes from a tree cover class to a non-tree cover class are allowed in the time-series if the difference of the tree cover probabilities exceed a certain threshold (see Section 3.2 for further details). Tree cover changes that do not exceed the thresholds are harmonized in the time-series to the class with the highest mean probability across a time-window of five years.

Finally, a rule-based postprocessing is applied to harmonize the 5-year classification, identify areas with potential overlaps among the different HRL VLCC products, and generate the final BVLs. Detected changes tree-cover changes are not modified by the rule-based processing.

The rules summarized in Table 1 are processed hierarchically so that latter rules overwrite the result of a previous rule for the same pixel:

Table 1: Overview of post-processing rules for the derivation of the harmonized annual BVLs.

| Rule \# | Rule | Purpose |
|----|----|----|
| 1\. | Five-year temporal sequences of herbaceous vegetation and the background class are recoded to sequences of herbaceous vegetation only. | Reduction of potential omission of herbaceous vegetation, especially in areas with dry grasslands. |
| 2\. | Five-year temporal sequences of cropland and the background class are recoded to sequences of cropland only. | Avoid omission of temporarily fallow land from cropland processing extent. |
| 3\. | Five-year temporal sequences of cropland and herbaceous vegetation are recoded to class 7overlap herbaceous – cropland. | Reduce propagation of uncertainties in BVL classification for downstream processing of croplands and grasslands. |
| 4\. | Any pixel with co-occurrence of tree cover and Tree Cover Density \<=10% in any of the last five reference years is assigned to class 6 overlaps of herbaceous and tree cover. | Account for the overlap of the definitions of the HRL Tree Cover & Forests and HRL Grassland layer. |

Those processing rules result into two further potential overlap classes being identified:

- overlap herbaceous – cropland

- overlaps of herbaceous and tree cover

Pixels with overlap herbaceous – cropland are then subject to further processing by both the Cropland and the Grassland processor. Specifically, pixels initially labelled as Fodder Crops in a preliminary version of the Crop Type (CTY) product are removed from the CTY product and now assigned to the Herbaceous (HER) layer.

Areas identified as overlaps of herbaceous and tree cover can be designated as both herbaceous and tree cover by the Grassland and Tree Cover & Forest processors, respectively. Similarly, areas identified as overlaps between crop and tree cover (i.e. tree crops) can appear in both the Cropland products and the Tree Cover & Forest products.

## 3.2 HRL Tree Cover & Forests

The HRL Tree Cover & Forests products comprise several annual status and 3-yearly change layers which are partially derived from the outputs of the BVL classification and combined with separate processing chain to estimate Tree Cover Density. This section details the applied methods for the production of the Tree Cover & Forests products. An overview of the workflow is provided in Figure 3.

![This data processing workflow diagram illustrates the steps for deriving harmonized annual Basal Vegetation Layers (BVLs), Tree Cover Density (TCD) products, and Dynamic Land Take (DLT) products. The process begins with three primary data inputs: 1. \*\*S-2 archive 5 ref. years vegetation seasons\*\*: This data undergoes 'Scene selection time feature computation'. 2. \*\*Existing HRL 2018 TCD\*\*: This input is used for 'Stratified sampling', which feeds into a 'Grid search' and then into 'TCD model calibration' using the 'CatBoost' algorithm. An iterative feedback loop connects Grid search and TCD model calibration. 3. \*\*Multi-year probability time series\*\* (for years 2017, 2018, 2019, 2020, 2021): This time series is combined with 'Biogeographical strata' (a map of Europe) as input for 'Tree cover change detection' (represented by a delta calculation of image probabilities). \*\*Upper Stream (BVL and TCD Derivation):\*\* Outputs from 'Scene selection time feature computation' and 'TCD model calibration' are fed into a 'Harmonization' step, which generates the 'BVL' product. The 'BVL' product, along with inputs from the first 'Harmonization' (not explicitly labelled but implied by the arrow connecting the box to the next step) then feeds into 'Temporal consistency analysis' (covering 2018, 2019, 2020, 2021). The results of 'Temporal consistency analysis' and the BVL are processed in a second 'Harmonization' step, leading to the 'TCD' (Tree Cover Density) product and the 'TCDCL' (TCD Change Layer). \*\*Lower Stream (Tree Cover Probability Change Derivation):\*\* The 'Tree cover change detection' output undergoes 'aggregation and MMU filter' (Minimum Mapping Unit), resulting in the 'TCPC' (Tree Cover Probability Change) product and the 'TCPCCL' (TCPC Change Layer). \*\*Final Dynamic Land Take (DLT) Derivation:\*\* Both the 'TCDCL' and 'TCPCCL' products are combined in a final 'aggregation and harmonisation' step. This step produces the 'DLT' (Dynamic Land Take) product and the 'DLTCL' (DLT Change Layer). A feedback loop is shown from the output of this 'aggregation and harmonisation' step back to the 'Tree cover change detection' input, implying that harmonized change information informs subsequent change detection processes.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-8c75bc7b81f884492f16d2dc812579fecc761de9.png)

Figure 3: High-level flow chart of the production workflow for the Tree Cover & Forests products TCD, DLT, TCPC and DLTC.

Dominant Leaf Type (DLT), Tree Cover Presence Change (TCPC) and Dominant Leaf Type Change (DLTC)

The BVL classification provides annual probabilities for coniferous trees, broadleaved trees and tree crops (e.g. fruit and olive trees). These probabilities serve as inputs for generating several forest-related products:

- Yearly **Dominant Leaf Type (DLT)**

- Yearly **Tree Cover Presence Change (TCPC)**

- Yearly **Dominant Leaf Type Change (DLTC)**

The derivation process begins with the detection of tree cover losses and gains based on the sum of the probabilities for tree cover (tree cover-broadleaved; tree cover-coniferous, tree crops). The difference of the sums of these probabilities is computed between the reference years at the intervals t1 and t2 of the 3-yearly change layers (e.g. between 2018 and 2021). Regionally calibrated thresholds are then applied to these probability differences whereas:

- Negative probability differences below the threshold are assigned as tree cover loss

- Positive probability differences above the threshold are assigned as tree cover gain

Vice-versa all probability changes that do not exceed the thresholds are discarded. For these rejected changes the most probable class across the 5-year period is assigned instead. Both accepted and rejected changes are then propagated back into the annual **DLT** and **BVL** layers to ensure consistency. Accepted changes are propagated to the time-step which has the highest difference in the time-series.

For example: The probability difference over three years (e.g. 2018-2021) for tree loss is -60% and below a defined threshold of -45%. The change is accepted. In the three annual time steps (e.g. 2018-2019, 2019-2020, 2020-2021) the probability differences are -20%, +10%, -50%. In this case the change is allocated in the last time-step of the annual status layers.

From this process an initial change pixel-based 3-annual change mask is obtained. This mask is aggregated to 20m resolution using the aggregation rules detailed in Annex I. To derive **Tree Cover Presence Change (TCPC)** a Minimum Mapping Unit (MMU) filter is applied (see Annex II for details) to:

- Eliminate change patches smaller than 1 hectare

- Fill small gaps within valid change patches

For the derivation of the **Dominant Leaf Type Change (DLTC)** the first step is the computation of a pixel-wise differences of the DLTs at t1 and t2 and its subsequent aggregation to 20m using the aggregation rules defined in Annex I. This raw version of the **DLTC** is subsequently masked and harmonized with the **TCPC**. For patches filled during the MMU filtering of the **TCPC** the leaf type information is complemented based on the majority of the surroundings in the raw **DLTC** to assure full consistency between **TCPC** and **DLTC**.

### 3.2.1 Tree Cover Density (TCD)

For the annual Tree Cover Density (TCD) layer (starting with the reference year 2018), the median spectral values of Sentinel-2 bands (B02, B03, B04, B08, B11 and B12) are computed for the vegetation season of each reference year. In areas, affected by persistent snow or heavy cloud cover alternative percentiles of the respective bands are used to minimize potential artefacts in the product. These spectral inputs are complemented by the mean classification probabilities for coniferous trees, broadleaved trees and tree crops resulting from the **BVL** classification.

To train the model, reference samples are drawn from the previous version of HRL TCD 2018 using a stratified sampling approach over areas with stable tree cover across all 5 reference years. A CatBoost regression model (Dorogush et al. 2018) is then trained with these yearly input data for the respective production unit and used to estimate the TCD for each reference year over the full extent of the PU. The model calibration involves a grid-search during which different degrees of oversampling of lower and highest TCD value ranges are tested. The aim of this gridsearch is to reduce the underestimation of these values ranges in the final layer.

In a subsequent post-processing step, the yearly TCD are harmonised by applying a histogram matching technique (Coltuc et al. 2006) and an additional smoothing step to limit sudden implausible spikes in the TCD over time. Lastly, the DLT classification is applied on top of the TCD to mask out non-tree covered areas, ensuring the final product reflects only valid tree cover.

A series of further layers is derived from the TCD, DLT as well of other ancillary datasets. An overview of the dependencies of these derived products is provided in Figure 4 and detailed in the following paragraphs.

### 3.2.2 Forest Additional Support Layer (FADSL)

The **Forest Additional Support Layer (FADSL)** at 10m spatial resolution is used to separate real “forest” areas from non-forest areas (i.e. trees predominantly used for agricultural practices, trees in urban context) in order to derive a **Forest Type** product which is largely following the FAO definition. The respective areas are derived through a rule-based spatial intersection of the 10m **DLT** and **TCD** layers with **CLC** 2018 and **IMD** 2018.

1.  Generation of a binary mask with  

- 0: non-impervious: **HRL IMD** == 0

- 1: impervious: **HRL IMD** \> 0

2.  Filtering of all contiguous all non-impervious patches \< 25 ha which are fully surrounded by impervious areas in a 4-pixel connectivity mode and subsequently reclassification to 1 = all impervious areas.

3.  Hierarchical intersection of the **DLT** (with **TCD** ranging from 10-100%), **CLC 2018** (vector geometries rasterized at 10m spatial resolution) and the gap-filled imperviousness dataset as detailed in Table 2 .

Table 2 FADSL - hierarchical intersection of input layers and resulting thematic classes

| Order | DLT Class | CLCClass | IMDClass | FADSLClass | Class Description |
|----|----|----|----|----|----|
| 1.) | 1 or 2 | any | 1 | 4 | trees in urban context – broadleaved and coniferous (from HRL Imperviousness context) |
| 2.) | 1 or 2 | 141 | 0 | 5 | trees in urban context – broadleaved and coniferous (from CLC class 1.4.1) |
| 3.) | 1 | 222or223 | any | 3 | trees predominantly used for agricultural practices – broadleaved (from CLC classes 2.2.2 and 2.2.3) |
|  | 255 | any | any | 255 | outside area (predefined through boundary layer) |
|  | any other remaining combination | any other remaining combination | any other remaining combination | 0 | all non-tree areas, and tree cover without urban context or agricultural use |

It is worth mentioning that the derived delineation of non-forest tree cover areas has certain limitations due to the specifications and thematic accuracies of the different input data (**DLT** with density values ranging from 10-100%; **CLC** 2018 with 25 ha MMU; **IMD** 2018 also representing infrastructure). This includes the frequency and timelines of updates which imposes the need use input layers that predate the actual reference year of the **FTY** (e.g. **FTY** 2021 was produced using still CLC 2018 and the first version of the **HRL IMD** 2018.

![This workflow diagram illustrates the processing steps for deriving various forest-related land cover products from core Copernicus Land Monitoring Service (CLMS) datasets. The process begins with three main input data sources: 1. Tree Cover Density (TCD) 2. Dominant Leaf Type (DLT) 3. Ancillary datasets: High Resolution Layer Imperviousness Density (HRL IMD) 2018 and CORINE Land Cover (CLC) 2018. These inputs are fed into an initial processing step that involves: \* Exclusion of urban and agricultural tree cover \* Exclusion of sparse tree cover \* Minimum Mapping Unit (MMU) filtering. This step generates two intermediate products: Forest Additional Support Layer (FADSL) and Forest Type (FTY). The FADSL, FTY, and the original TCD, DLT, HRL IMD 2018, and CLC 2018 datasets are then collectively processed in a subsequent 'Aggregation to 100m' step. This aggregation step produces four final derived products: \* TCD 100m (Tree Cover Density at 100m resolution) \* BCD (Broadleaved Cover Density) \* CCD (Coniferous Cover Density) \* FTY 100m (Forest Type at 100m resolution)](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-ca3af50470b86f297c48a5a7e3b6625919df0077.png)

Figure 4: High-level flow chart of the production workflow for the Tree Cover & Forests products FADSL, FTY and aggregated products at 100m.

### 3.2.3 Forest Type (FTY)

The **Forest Type (FTY)** layer implements forest maps largely following the definition provided by the Food and Agriculture Organization (FAO), as specified in the terms and definitions of the *Global Forest Resources Assessment (FRA) Working Paper 1 (FAO, 2012)*. The 10m FTY product is computed by applying the FAO´s definition, however, for EEA-specific purposes, it explicitly includes tree cover in traditional agroforestry systems, such as Dehesa and Montado, which are typically excluded under standard FAO criteria.

In a first step an intermediate tree cover mask product is derived through spatial intersection of the two primary status layers **TCD** (≥ 10-100%) and \***DLT**, where areas under agricultural use and in urban context as provided by the **FADSL** are excluded. To ensure consistency with the specified Minimum Mapping Unit (MMU) of 0.5 hectares (equivalent to 50 pixels), the resulting tree cover mask is refined using the GDALSieve[^1] operation. This operation removes small patches below the MMU and fills in small gaps. The output is used to create an initial version of the Forest Type product, that is still missing information in areas, which were filled and marked as tree cover during the sieving process. Furthermore, an ancillary mask is created by mapping these specific pixels with no data values. The GDALFillNodata[^2] function is used to assign values to the pixel shown in the ancillary mask by using an inverse distance weighting algorithm to fill NoData areas based on the values of surrounding pixels. In the last formatting step those interpolated areas and the initial Forest Type version are combined to form the final Forest Type product, which is finally aligned to the processing extent as given in the official Boundary Layer (EEA, 2023).

### 3.2.4 Aggregated products - Tree Cover Density (TCD) 100m, Broadleaved Cover Density (BCD) & Coniferous Cover Density (CCD)

The TCD at 100m spatial resolution is derived through spatial aggregation from the 10m TCD status layer for the respective reference year. The 100m LAEA grid is used to calculate the arithmetic mean density of all underlying 10m pixels (with density values from 0-100) for each 100m cell. The thereof resulting mean values from the aggregation (floating point data type) are rounded and finally converted to integer values (e.g. raw values in the range from 33.5 to 34.4 are converted to a density value of 34).

Several further layers are derived through operations of intersection and aggregations including **Broadleaved Cover Density (BCD)** and **Coniferous Cover Density (CCD)** layers. **BCD** is the aggregated density of broadleaved trees and shows the percentage of broadleaved pixels in the **DLT** for the respective reference year while **CCD** is the aggregated density of coniferous trees and shows the percentage of coniferous pixels. Both **BCD** and **CCD** layers are derived through aggregation of the 10m **DLT**. The 100m LAEA grid is overlaid to the 10m **DLT** product. Within each 100m cell the number of broadleaved and coniferous pixels are counted and the respective percentages stored into 100m pixel of the **CCD** and **BCD**, respectively.

### 3.2.5 Aggregated products - Forest Type (FTY) 100m

The **FTY** at 100m spatial resolution is derived through spatial aggregation from the FTY 10m status layer based on the spatially consistent EEA 100m grid. The first step is to identify forest covered 100m cells by counting and summing up all forest pixels (broadleaved and coniferous) of the 10m FTY product within the respective grid cell. If the number of forest pixels is ≥ 50, the 100m grid cell is assigned to “forest cover”. In case a 100m cell contains less than 50 forest covered 10m pixels, it will be labelled as all non-forest areas in the final product.

After identifying the forest areas, the CORINE Land Cover definition for broadleaved, coniferous and mixed forest is applied. The class broadleaved forest is assigned in 100m grid cells, which contain ≥75% forest pixels belonging to broadleaved. If a 100m grid cells consists of ≥ 75% coniferous pixels within the forested area it is assigned to coniferous forest. Areas in which neither “broadleaved” nor “coniferous” constituents account for ≥75% of the 10m forest pixels are labelled as mixed zones.

### 3.2.6 Dominant Leaf Type Confidence Layer (DLTCL)

The **DLTCL** uses the probabilities gained during **BVL**/**DLT** computation from the Temporal convolutional neural network to compute classification confidence. The classification confidence is considered here as the probability margin between the highest and second highest ranked leaf type class. The margin is derived by calculating the absolute difference values of probabilities for coniferous and broadleaved tree cover classes. High confidence (up to 100%) indicates domination of one class, whereas lower values (close to 0%) are typical for areas with similar probabilities, suggesting uncertainty or mixed tree cover types.

### 3.2.7 Tree Cover Density Confidence Layer (TCDCL)

The **TCDCL** uses the Total Uncertainty (Variance) metric calculated from CatBoost algorithm to derive the standard deviation for each estimated TCD value. Total uncertainty is the sum of data and knowledge uncertainty. The former can be seen as a measure for data complexity due to noisy data or overlapping classes. Knowledge uncertainty is obtained from a single CatBoost model by using virtual ensembles (Malinin et al. 2020). If this option is enabled during the CatBoost run the one existing model is basically divided into (n) separate models. The annual **TCD** production was done with ()=10. Based on these 10 models Knowledge uncertainty is computed by the variance of the mean values predicted by all models. Low **TCDCL** values indicate high confidence in the estimated **TCD** value.

### 3.2.8 Tree Cover Presence Change Confidence Layer (TCPCCL)

The **TCPCCL** relies as well on the probabilities for coniferous and broadleaved tree cover classes gained during **BVL**/**DLT** computation to calculate change confidence. The change confidence here refers to the change in combined tree cover probability from 2018 to 2021. This is done by summing up the probabilities for coniferous and broadleaved tree cover classes for each reference year and afterwards the absolute difference is calculated between 2018 and 2021 respectively. High values signal a big difference between both years and thus a high confidence in change detection, whereas lower values indicate some uncertainty.

### 3.2.9 Encountered issues and known limitations

**Omission of sparse tree cover** is commonly known challenge for tree cover mapping since lower canopy cover leads to a mixed reflectance signal that becomes increasingly dominated by the understory. The issue is further aggravated by imperfections of the multi-temporal coregistration of the Sentinel-2 data. Sparse tree cover is common at the timber line but in particular in the Mediterranean comprising agroforestry systems (Dehesas, Montados) and Olive Groves. Initial classifications for the Iberian Peninsula and Southern Italy revealed large areas of Olive Groves and Dehesas which triggered a reprocessing. This included the revision of approximately 7000 additional samples and the collection of around 5500 additional tree cover samples. Retraining the model with the revised sample database indeed provided major improvements. Further enhancements were implemented also in the post-processing to boost tree cover probabilities in areas designated as Agroforestry, Olive Groves and other type of tree cover according to the Corine Land Cover layer for 2018. An example for the status of the DLT before and after the reprocessing is provided in Figure 5. Though the reprocessing has significantly reduced the amount of omission errors, tree cover omission is generally still more pronounced in the Mediterranean region.

![This image displays two aerial views of a landscape, demonstrating the difference between 10-meter and 100-meter spatial resolution land cover products from the Copernicus Land Monitoring Service (CLMS). Panel (a) displays a high-resolution aerial photograph overlaid with bright green 10-meter pixels. These green pixels represent detected tree cover, likely indicating broadleaved tree presence from a 10m Dominant Leaf Type (DLT) product. The underlying imagery shows individual broadleaved trees, grassland, and unpaved roads. A scale bar at the bottom indicates distances of 0, 100 m, 200 m, and 300 m. Panel (b) shows the aggregated land cover for the same area at 100-meter spatial resolution. Large green areas represent Broadleaved Cover Density (BCD), indicating a high percentage of broadleaved tree cover within those 100m cells. Dark grey areas depict non-tree cover. Scattered small purple pixels indicate Coniferous Cover Density (CCD). This panel illustrates the result of spatial aggregation from the 10m DLT product to the 100m grid for derived products like BCD and CCD. A scale bar at the bottom indicates distances of 0, 100 m, 200 m, and 300 m.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-76519c7ec6c010f538a443731db40973837bf1f3.jpg)

Figure 5: Dominant Leaf Type for the reference year 2021 a) after initial classification and b) after reprocessing for agroforestry system in Andalusia, Spain (LAEA 3044254.4m, 1822153.02m) Background Google Maps VHR imagery 03/2021.

The employed regression-based method for the estimation of the **Tree Cover Density** is generally sensitive to the propagation of **artefacts resulting from cloud cover and topographic effects** from the input satellite imagery. The usage of median time features is in most cases robust to such artefacts but some issues have been encountered frequently, not all of which could be fully resolved in the final layers.

This concerns topographic effects where cast shadows result in dark features in the imagery and an overestimation of the **TCD**. Similarly, the topographic correction of the Sentinel-2 L2A processor tends to overestimate reflectance on north and north-west facing slopes which in turn can lead to an underestimation of the **TCD**. Such topographic effects are typically more pronounced at higher latitudes with lower sun angles. An example is provided in Figure 6.

Underestimations and spatial patterns that are not related to actual variations of the canopies can also be caused by cloud cover. On the one hand, this can be caused by clouds that are not detected in the SCL accompanying the Sentinel-2 L2A data. On the other hand, frequent cloudcover during the peak period of the vegetation season can lead to a higher impact of scenes from early spring that may depict broadleaved deciduous tree (especially those with later leaf emergence such as Fagus and Quercus) still with leaf off conditions. A rigorous quality control was conducted to detect such artefacts and adjust parameters for median time-feature computation as much as possible. This included for example the usage of shorter time-windows (starting only in May) or alternative statistical metrics such as 25th- and 75th percentiles. While this enabled to significantly reduced the amount of artefacts as illustrated in Figure 7, it was not possible to fully resolve all cases encountered.

![This composite image displays three views of a coastal and forested landscape, illustrating Copernicus Land Monitoring Service (CLMS) forest products. All three panels show the same geographic extent, featuring a large body of water (top), a coastline, a prominent forested mountain ridge running horizontally through the center, and several smaller inland lakes. A yellow rectangular bounding box highlights the central forested ridge across all three sub-images. \*\*Panel (a)\*\* presents a true-colour satellite image of the area, showing dark blue/black water bodies and green forested land cover. \*\*Panel (b)\*\* shows a derived land cover map, which represents the Forest Type (FTY) 100m product. Forested areas are depicted in green, non-forest areas in white, and water bodies in black. This panel visually represents the identification of forest covered 100m cells, where a 100m grid cell is assigned to 'forest cover' if it contains at least 50 forest pixels from the 10m FTY product. \*\*Panel (c)\*\* displays a grayscale image, which represents the Dominant Leaf Type Confidence Layer (DLTCL) product. Dark areas indicate water, while varying shades of gray across the land cover suggest classification confidence for dominant leaf types (broadleaved, coniferous, or mixed forest) derived from probabilities during Broadleaved/Deciduous vs. Coniferous (BVL/DLT) computation. Each panel includes a scale bar, indicating distances such as 50 m, 100 m, 200 m, and 500 m, along with a visible grid overlay.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-bc1b609dee87f1e9ffa5ba0bf47c2f4e63f371a2.jpg)

Figure 6: Example for an area with imprints of topographic effects into the Tree Cover Density layer in Northern Norway (LAEA. 4833337.67m, 5288588.26m) a) VHR image 07/2021 (Google Maps) b) final TCD layer for 2021 and c) median of S-2 L2A band 3 over the vegetation season.

![The image displays three panels (a, b, c) comparing forest cover maps with underlying satellite imagery over an unlabelled geographic area. Panel (b) presents a false-colour satellite image, depicting vegetation in red hues, urban/bare areas in cyan/grey, and water bodies in dark blue. It shows a large central forested area, interspersed with agricultural fields and scattered urban or settlement patterns. Panels (a) and (c) are thematic maps illustrating forest cover density. Both share a common legend indicating percentage classes: 1 (lightest yellow/green), 25 (light green), 50 (medium green), 75 (darker green), and 100 (darkest green). White areas indicate non-forest. Panel (a) shows a granular representation of forest cover density, with a wider range of green shades indicating varying percentages across the forested areas, including many smaller, lighter green patches and less dense areas within the main forest block. Panel (c) displays a more aggregated and consolidated representation of forest cover, predominantly in darker green shades, suggesting a higher overall density. This likely represents a derived Forest Type (FTY) product where only cells meeting a certain forest pixel threshold (e.g., ≥50% forest pixels from a 10 m layer, as per the Copernicus Land Monitoring Service (CLMS) FTY definition) are considered 'forest cover' and displayed by their actual density, resulting in a visually denser output compared to panel (a). A common scale bar is provided at the bottom of the image, ranging from 0 km to 5 km.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-2dd3407d3fdf8a7517f3847a38faefdfec124e4d.jpg)

Figure 7: Example for initial TCD underestimation due to proportional high number of early spring scenes with trees in leaf-off conditions in Northern Germany (LAEA, 4186992.95m 3368117.83m). a) initial (unmasked) TCD estimates using median features for March – October 2021 and showing severe underestimation for broadleaved deciduous canopies, b) VHR image 2021 and c) final TCD based on reduced time window from May to September 2021 and percentile features.

## 3.3 HRL Grasslands status and change layers

This section gives an overview of the methodology employed to produce the layers **Herbaceous Cover (HER)**, **Ploughing Indicator (PLOUGH)**, **Grassland (GRA)** and **Grassland Change (GRAC)**.

### 3.3.1 Input data

All grassland products described in the following subsections are based on a common set of input and auxiliary data. The main source of information is the Base Vegetation Layer (**BVL**), specifically the probability associated with the herbaceous class serves as a starting point for subsequent derivations.

In addition to the **BVL**, different sets of auxiliary data are needed:

- **Corine Land Cover (CLC 2018)**[^3] (to dampen the probability of certain areas)

- **CLCplus Backbone 2018 (CLCplus BB)**[^4] (as reference to derive probability thresholds)

- **HRL Grassland** 2018[^5] (as reference to derive probability thresholds)

- Previous version of **HRL Ploughing Indicator** 2018 (to mark ploughing events before availability of S2 data in 2017)

### 3.3.2 Herbaceous Cover (HER)

The production of the **Herbaceous Cover (HER)** is primarily based on the probability estimates obtained from the **Base Vegetation Layer (BVL)** which also serves to harmonise the different vegetated **HRL** products, including **HRL Grasslands**, **Tree Cover & Forests and Croplands**. The **BVL** is created annually (2017-2021) and using probability estimates of various land cover types.

To derive the herbaceous layer, various operations are performed on the probability estimates to either locally increase or decrease the herbaceous probabilities. The **Corine Land Cover (CLC)** 2018 layer is applied to weight the probabilities for some classes such as peat bogs, sclerophyllous vegetation and others to eliminate false positives from the 2018 reference year classification. To determine the final herbaceous layer, a suitable threshold must be established for each processing unit (i.e. EEA tile). Probabilities above this threshold are considered to be herbaceous. The thresholds are calibrated using additional CLMS products, the previous version of **HRL Grassland** 2018 and **CLC** 2018. The **BVL** herbaceous probabilities are compared with all matching pixels from these layers. This ensures that only pixels are considered where both layers indicate the same land cover type. The threshold is chosen dynamically by finding the probability which maximizes the accuracy between the herbaceous **BVL** probability and the CLMS products. To avoid a too general (or even constant) threshold for the whole EEA tile, the accuracy is matched in 16 sub-tiles and then interpolated over the whole tile using a Gaussian filter. This process ensures that strong differences in landscape and vegetation within an EEA tile are still addressed.

To further tune these **HER** thresholds a manual inspection using visually interpreted sample points is conducted. In case of strong over- or underestimation the process can be rerun manually forcing the algorithm to use increased or decreased thresholds.

Moreover, the probabilities between yearly layers are harmonized to reduce rapid changes that are often due to classification noise. This achieved by calculating the (fast) Dynamic Time Warp (DTW) of the time-series of two subsequent years using the **Vegetation Phenology and Productivity– Plant Phenology Index (HR-VPP PPI)**[^6] time-series (Salvador et. al. 2007). All yearly binary HER layers are finally determined by applying the threshold found in the procedure described above. Further details follow in the **Grassland Change (GRAC)** layer section 3.3.6.

Additionally, the binary HER layer is enriched with information from the **Crop Types (CTY)** layer. All pixels classified as fodder crop (class 1500) are included (for each year respectively) in the binary **HER** layer. Finally, the herbaceous extent is clipped to the yearly **BVL**.

**The following steps are needed to derive the herbaceous products:**

- Retrieve herbaceous probability estimates from **BVL** herbaceous class.

- Find threshold in reference year by maximizing accuracy when compared to CLMS products

- Tune probability estimates

  - Dampen probabilities of selected classes using **CLC** 2018 to eliminate false positives.

  - Harmonize probabilities between yearly layers to reduce rapid changes.

- Apply threshold to all years to determine binary layers

- Mask herbaceous layer

- Data outputs (creation of the Cloud-Optimized-GeoTiffs, colortables, metadata)

### 3.3.3 Ploughing Indicator (PLOUGH)

The **PLOUGH** indicator is generated by analysing a combination of data sources: a series of binary **HER** (herbaceous) classification layers, **BVL** (Base Vegetation Layer) classes, and **HR VPP PPI** (Plant Phenology Index) quantiles.

- **BVL** classes 4 (crop) and 7 (transition between herbaceous and crop) are used as indicators of a ploughing event.

- Low **PPI** quantiles signal periods of low vegetation, which may correspond to ploughing activity.

For reference years before 2017, where data is missing, the system uses ploughing records from the historic **PLOUGH (HIS-PLOUGH)** product, which can introduce certain inconsistencies (see section 3.3.9).

The algorithm works by detecting the first break in a continuous series of **HER** classifications—a potential sign of ploughing. If such a break is found, it’s labelled as a “possible ploughing event” and is then cross-checked with both the PPI data and **BVL** classification to confirm if ploughing actually occurred.

- If the break is confirmed, it’s recorded as a ploughing event.

- If it’s not confirmed, the pixel is either:

  - Reclassified as **HER** (if the **BVL** suggests it’s still herbaceous because it’s inside a crop class), or

  - Assigned to Class 100, indicating a change in HER cover but not due to ploughing.

If no break is found, the pixel is excluded from the PLOUGH layer but will still be included as grassland in the GRA layer. See Figure 8 for a visualization of the workflow as a flowchart.

To reduce salt-and-pepper noise, the final **PLOUGH** layer is filtered using a minimum mapping unit (MMU) of 0.03 ha (i.e. 3x10m pixels). Since the processing based on 100km tiles, this step includes gathering intermediate version of all neighbouring tiles to avoid edge-effects at the tile borders.

Data outputs include the creation of Cloud-Optimized GeoTIFFs, accompanying colour tables, and detailed metadata.

![This decision tree illustrates the algorithm for detecting ploughing events based on herbaceous (HER) cover changes. 1. The process begins by evaluating if a pixel is an HER pixel. \* IF the pixel is NOT an HER pixel, THEN the outcome is 'No ploughing' (class 253). \* IF the pixel IS an HER pixel, THEN the algorithm checks for a 'Break in HER series'. 2. IF there is NO 'Break in HER series', THEN the outcome is 'No ploughing' (class 253), labelled as GRA (Grassland/non-ploughed herbaceous). \* IF there IS a 'Break in HER series', THEN the algorithm proceeds to check if the 'Break is confirmed by BVL (Base Vegetation Layer) or VPP (Vegetation Phenology Index)'. 3. IF the 'Break IS confirmed by BVL or VPP', THEN the outcome is a 'Ploughing event' (class 0 to 6). \* IF the 'Break is NOT confirmed by BVL or VPP', THEN the algorithm checks IF the pixel is 'Herbaceous in BVL crop class'. 4. IF the pixel IS 'Herbaceous in BVL crop class', THEN the outcome is 'No ploughing' (class 253), and the pixel is reclassified to HER. \* IF the pixel is NOT 'Herbaceous in BVL crop class', THEN the outcome is 'HER cover change' (class 100).](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-da90c1314ea785b85e939102f3c1d3f6e81a9387.png)

Figure 8: Flowchart of the PLOUGH decision logic

### 3.3.4 Grassland (GRA)

The **Grassland (GRA)** layers are directly derived from the **Herbaceous Cover (HER)** and **Ploughing (PLOUGH)** layers. A pixel is considered to be grassland if it has been herbaceous for five consecutive years7. To retrieve this information the corresponding binary HER **layer** is masked with the corresponding **PLOUGH** layer, leaving only **HER** pixels which have not been ploughed in the previous year.

Like the **HER** layer, each Grassland layer is clipped to the yearly **BVL** extent and filtered to a MMU of 0.03 ha. However, only class 1 of the **BVL** is used to mask the GRA layer (unlike classes 1, 6 and 7 for HER), since overlaying classes 6 and 7 do not allow grassland classifications.

**The following steps are needed to derive the HRL Grasslands layers:**

- Mask binary **Herbaceous Cover (HER)** with ploughing indicator to determine grassland layer

- Mask **Grassland (GRA)** layer to yearly **BVL** (class 1 only)

- Application of the MMU 0.03 ha (i.e. of 3 x 10m pixels). Since the processing based on 100km tiles, this step includes gathering intermediate version of all neighbouring tiles to avoid edge-effects at the tile borders.

- Finalizing steps (creation of the Cloud-Optimized-GeoTiffs, colortables, metadata)

The application of the MMU and the finalization steps are performed only after all tiles have been processed to also take border regions of adjacent tiles into account.

### 3.3.5 Grassland Confidence (GRACL)

The **Grassland Confidence Layer (GRACL)** gives an estimate of how confident the classification was in predicting a certain grassland pixel. It is derived as the mean taken over the respective herbaceous confidence values. These are not an actual layer but are still derived in the workflow process. The herbaceous confidence for any year is the difference between an herbaceous probability taken from the **BVL** and the second highest probability. Therefore, the higher the herbaceous probability is, the greater the difference to the second highest probability and therefore also a higher herbaceous confidence value. In case another probability is higher than the herbaceous probability, the confidence value is set to zero.

The grassland confidence is then simply derived as the mean of the relevant herbaceous confidence layers.

Furthermore, the layer is clipped to actual grassland pixels. Note, that it is possible, even though unlikely, that a grassland pixel can result in having a confidence value of zero, if the mean of all herbaceous confidence values resulted in zero.

### 3.3.6 Grassland Change (GRAC)

As described above, the main part of the processing and time-series analysis is carried out in the processing of the herbaceous layer as this builds the fundament of any subsequently derived layer. For the change detection, it is specifically important to include a sophisticated time-series analysis into the herbaceous classification to prevent false class-flips between consecutive years and therefore to avoid artificial changes introduced by classification noise by calculating the (fast) Dynamic Time Warp (DTW) of the time-series of two subsequent years as already described in section [Section 3.3.2](#sec-Herbaceous-Cover) In principle, various vegetation indices, such as Normalised Difference Vegetation Index (NDVI), Enhanced Vegetation Index (EVI) or Leave Area Index (LAI), can be utilized to accomplish this objective. However, for ease of use and availability, it was decided to use **HR-VPP PPI**[^7] time-series for this analysis.

Depending on the similarity of the time-series in terms of DTW, the raw herbaceous classification probabilities are adapted according to the following formula:

\\ p\_{1,\text{new}} = (1 - f) \cdot p_1 + f \cdot p_2 \\

with

\\ f = \begin{cases} 0 & \text{for } \mathrm{DTW}(y_1, y_2) \< th\_{\min} \\ 1 & \text{for } \mathrm{DTW}(y_1, y_2) \> th\_{\max} \\ \frac{\mathrm{DTW}(y_1, y_2) - th\_{\min}}{th\_{\max} - th\_{\min}} & \text{otherwise} \end{cases} \\

In this equation, \\p_1\\ and \\p_2\\ represent the herbaceous classification probabilities for the two years, while \\y_1\\ and \\y_2\\ stand for their corresponding vegetation sensitive index time-series, specifically the **HR-VPP PPI**[^8] time-series. This approach allows to define two thresholds, \\th\_{\min}\\ and \\th\_{\max}\\ which define the level of similarity that must be reached by the two signals to allow or suppress a possible class switch in the **Herbaceous Cover (HER)**. In simple terms, the DTW gives a low value for very similar time series and a high value if the time-series are different. If no change is seen, the classification probability of the previous year is kept. Values in between the two thresholds are linearly interpolated. For the production, the thresholds were set to 0,5 and 1,5, respectively.

**After the grassland layers have been processed with the above algorithm, the derivation of the grassland change follows the following steps:**

- Aggregation to 20m by a majority rule (see aggregation rules in Annex II)

- Assignment of the GRAC classes:

  - 0: Non-grassland in both years

  - 1: Grassland gain

  - 2: Grassland loss

  - 10: Grassland in both years

- Application of the MMU of 1.0 ha (i.e. 25 x 20m pixels) for grassland losses and gains by the following steps:

  - Mask creation for losses and gains

  - Sieving of all classes with the above size threshold. Since the processing based on 100km tiles, this step includes gathering intermediate version of all neighbouring tiles to avoid edge-effects at the tile borders.

- Application of the filtered layer in masked parts

- Data output (creation of the Cloud-Optimized-GeoTiffs, colour tables, metadata)

The application of the MMU and the finalisation steps are performed only after all tiles have been processed to also take border regions of adjacent tiles into account.

### 3.3.7 Grassland Change Confidence Layer (GRACCL)

The **Grassland Change Confidence Layer (GRACCL)** gives an estimate on the confidence for the grassland gains and losses derived in the Grassland Change layer. To derive this confidence value the grassland probability layers from 2018 and 2021 are needed. These are derived by applying the mean to all for the reference year relevant herbaceous layers (e.g. for the 2021 grassland probability the mean over all herbaceous layers from 2017-2021 are used, since all those reference years influence those probabilities.

The grassland change confidence value is then derived as

\\ GRACCL = \left( p_1 \cdot (1 - p2) + p2 \cdot (1 - p1) \right) \cdot 100 \\

where p1 is the grassland probability of the first reference year and p2 is the grassland probability of the second reference year.

This value is only derived for grassland change pixels which identify as grassland gains or losses.

### 3.3.8 Aggregated products – Grassland (GRA)100m

A further 100m Grassland layer is derived through aggregation from the Grassland layer at 10m spatial resolution. To this end, all grassland 10m GRA pixels within the extent of a GRA 100m pixel are counted and reported as the aggregated GRA 100m value in the range \[0, 100\]. No data values such as 255 are ignored and not counted during the aggregation.

### 3.3.9 Encountered issues and known limitations

Initial tests demonstrated that the **HER time-series** was susceptible to false positive changes which in turn generated false positive changes in the **GRA** time-series and the **GRAC**.

This issue was addressed by harmonizing the **HER** time-series by comparing it with a change layer derived from the **HR-VPP PPI** (see [Section 3.3.6](#sec-GRAC)). A **HER** pixel is only allowed to change from one year to the next if there is a strong enough signal change detected in the **HR-VPP PPI**. The rules were applied more rigorously to ensure a higher consistency. The following **Error! Reference source not found**. shows an example of the **GRAC** layer in EEA tile E39N31 comparing changes from the previous test production vs. the processor deployed in production. The number of positive and negative changes decreased significantly due to the harder constraints on change during the years. The restrictions on **HER** layers being more consistent throughout the years propagates further to the **GRA** and **GRAC** layers.

![The image displays a comparison of grassland change detection results across two distinct geographic areas, referred to as map tiles and identified by numerical codes. Each area is presented with two versions of the land cover classification: 'Test production' and 'Current production'. The map panels are arranged in two rows and two columns: \* The top row shows results for tile '3957750 3114334' under 'Test production' (left) and 'Current production' (right). \* The bottom row shows results for tile '3984094 3150073' under 'Test production' (left) and 'Current production' (right). Colour coding: \* Light green represents stable grassland or other stable vegetated areas. \* Blue pixels indicate detected grassland gains. \* Red pixels indicate detected grassland losses. \* White/light grey areas represent non-grassland or areas not subject to change detection. For tile '3957750 3114334' (top row): \* The 'Test production' map shows a notable cluster of blue pixels (grassland gains) in the central-left region, alongside scattered red pixels (grassland losses). \* The 'Current production' map for the same tile shows significantly fewer blue pixels, primarily in the same central-left cluster, and almost no red pixels, indicating a substantial reduction in detected changes. For tile '3984094 3150073' (bottom row): \* The 'Test production' map shows a widespread and high density of red pixels (grassland losses) across the area, with some sparse blue pixels (grassland gains). \* The 'Current production' map for this tile shows a reduced, but still evident, distribution of red pixels and very few blue pixels compared to the test production. Overall, the 'Current production' consistently depicts fewer detected grassland gains and losses than the 'Test production' across both map tiles. This suggests that the current production methodology, possibly incorporating a 'Grassland Change Confidence Layer (GRACCL)' or filtering, results in a more conservative identification of grassland changes compared to the test phase. The underlying data for the Grassland layer is typically at a 10m spatial resolution.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-8719e7bd2267f1c5464a04d53f8f28dfc13d0098.jpg)

Figure 9: Comparison of GRAC layers from test production and current production taken from EEA tile E39N31 (upper example in the centre around (3957750, 3114334), lower example in the centre around (3984094, 3150073). Blue areas indicate grassland gain, red areas indicate grassland loss (for year 2018 to 2021).

The **HIS-PLOUGH** from 2012 to 2015 is based on Landsat data and hence not fully consistent in terms of quality and resolution (20m) with the **PLOUGH** for later reference years (10m, based on Sentinel-2). This issue was already realized during the HRL 2018 production and at the time it was decided to rely on the **HIS-PLOUGH** for the years 2016-2018 only[^9]. The same strategy would lead to continuously decreasing grassland extent in the 2017-2021 time series and thus, the full **PLOUGH** time series was hence considered to mitigate the issue. However, the variable resolution and quality of the early **HIS-PLOUGH** years still propagates to some degree to the **Grassland (GRA)** time-series (**Error! Reference source not found.**).

This limitation is generally difficult to be solved completely due to the unavailability of suitable Sentinel-2 time-series before 2017.

![Two raster maps are displayed side-by-side, visually comparing spatial patterns of coloured pixels on a white background. These maps likely represent areas of grassland change or their associated confidence from a Copernicus Land Monitoring Service (CLMS) Grassland Change Confidence Layer (GRACCL). The left map shows sparse, disconnected clusters of orange-brown pixels and a single small dark reddish-brown pixel. The right map shows a more extensive distribution of coloured pixels, dominated by large, irregular, interconnected areas of dark reddish-brown pixels, along with smaller, isolated patches of light yellow pixels. The maps lack a legend, geographic coordinates, or scale, preventing specific interpretation of the colour values or exact locations. The distinct spatial patterns suggest a comparison between different scenarios, regions, or thresholds related to grassland change detection or confidence.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-1361d85aaefb1873757c904fc85aa2aa2698f10a.png)

Figure 10: EEA tile E35N25. On the left side PLOUGH 2015 in 20 m and on the right side, the PLOUGH 2017-2021. The orange (left) and the yellow (right) patch in the centre of the figures comes from the HIST-PLOUGH and therefore shows the outline of the 20 m pixel size at that time.

The introduction of the HER has caused inconsistency issues between the **HER**, **GRA** and the **HISPLOUGH**. Therefore, the **HIS-PLOUGH** product was adapted as the following: Class *0 - indication of ploughing in current year, former class 0 converted to class 253, class 100* will contain all pixel that change between two years due to changes in the **HER** but not ploughed to maintain consistency between **PLOUGH**, **GRA** and **HER** layers. Please refer to **Error! Reference source not found**. for a side-by-side view of the old and new class coding.

![This image presents two tables showing classification schemes and associated RGB colour codes for grassland ploughing information, likely representing different versions or test productions of a Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Grassland product such as the Grassland Change (GRAC) layer. The first table (left) defines the following classes: \| Class Code \| Class Name \| Red \| Green \| Blue \| \|------------\|---------------------------------------------------------------------------\|-----\|-------\|------\| \| 0 \| no ploughing information \| 240 \| 240 \| 240 \| \| 1 \| 1 year since last indication of ploughing \| 128 \| 0 \| 0 \| \| 2 \| 2 years since last indication of ploughing \| 199 \| 60 \| 18 \| \| 3 \| 3 years since last indication of ploughing \| 230 \| 107 \| 37 \| \| 4 \| 4 years since last indication of ploughing \| 247 \| 153 \| 59 \| \| 5 \| 5 years since last indication of ploughing \| 252 \| 201 \| 91 \| \| 6 \| 6 years since last indication of ploughing \| 255 \| 236 \| 140 \| \| 254 \| unclassifiable (no satellite image available, or clouds, shadows, or snow) \| 153 \| 153 \| 153 \| \| 255 \| outside area \| 0 \| 0 \| 0 \| The second table (right) defines an updated or alternative set of classes: \| Class Code \| Class Name \| Red \| Green \| Blue \| \|------------\|------------------------------------------------\|-----\|-------\|------\| \| 0 \| Indication of ploughing in current year \| 66 \| 0 \| 0 \| \| 1 \| 1 year since last indication of ploughing \| 128 \| 0 \| 0 \| \| 2 \| 2 years since last indication of ploughing \| 199 \| 60 \| 18 \| \| 3 \| 3 years since last indication of ploughing \| 230 \| 107 \| 37 \| \| 4 \| 4 years since last indication of ploughing \| 247 \| 153 \| 59 \| \| 5 \| 5 years since last indication of ploughing \| 252 \| 201 \| 91 \| \| 6 \| 6 years since last indication of ploughing \| 255 \| 236 \| 140 \| \| 100 \| Change of herbaceous cover \| 229 \| 251 \| 17 \| \| 253 \| no ploughing information \| 240 \| 240 \| 240 \| \| 255 \| outside area \| 0 \| 0 \| 0 \| Both tables define classes for the number of years since the last indication of ploughing, from 1 to 6, with consistent RGB values (dark red to light yellow). Key differences include Class 0: 'no ploughing information' in the first table (RGB 240, 240, 240, white) versus 'Indication of ploughing in current year' in the second table (RGB 66, 0, 0, dark brown). The second table reassigns 'no ploughing information' to Class 253 (RGB 240, 240, 240) and introduces Class 100 'Change of herbaceous cover' (RGB 229, 251, 17, bright yellow), while omitting the 'unclassifiable' class (Class 254) from the first table. The 'outside area' class (255) is consistent across both tables (RGB 0, 0, 0, black).](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-b47d1af3225b944dbe9e4f0eab771936c27a02f9.png)

Figure 11: Colour palette and attributes of PLOUGH layer. Left: HRL GRA 2015/2018 and right HRL VLCC.

## 3.4 HRL Grasslands mowing layers

I this section the methods and workflows for the production of the layers, **Grassland Mowing Events (GRAME)**, **Grassland Mowing Dates (GRAMD)** and the **Grassland Mowing Events Confidence Layer (GRAMECL)** are explained in more detail.

### 3.4.1 Input data

The main source of information for the **Grassland Mowing (GRAM)** layers are time series of high-resolution Sentinel-2 satellite data. Both processing Sentinel-2 processing levels Level-1C and Level 2A are used in the processing chain. Since undetected clouds and cloud shadows remain a significant drawback for the time-series analysis additional custom cloud masks are required. Sentinel-2 Level-1C product (providing Top-Of-Atmosphere reflectance images) serves as the primary input for the calculation of cloud masks. The Level-2A product (Bottom-OfAtmosphere reflectance as provided by WEkEO / ESA), serves as the primary input for the mowing detection via a time-series analysis. In addition to Sentinel-2 imagery, additional auxiliary data are needed:

- **CLMS High Resolution Vegetation Phenology and Productivity layer (HR-VPP):** Startof-Season Date (SOSD) and End-of-Season Date (EOSD) (to calculate growing season parameters,

- **CLMS HRL Herbaceous layer (HER)** mask to perform the analysis only on the detected herbaceous area.

### 3.4.2 Grassland Mowing Dates (GRAMD)

Based on a thorough analysis of available methodologies and experiences from CAP-based monitoring of mowing events, a methodology closely following the approach of Griffiths et al., 2020, was developed. Mowing events are determined by looking for disturbances (unusually sharp drops in biophysical signal) compared to a reference value. To determine the reference value, a reference time series model approximating the theoretical phenology of undisturbed grassland was developed. Griffiths et al. (2020) have shown that using an idealized phenological model as an upper envelope allows mowing events to be identified as deviations from the idealized model.

As opposed to Griffiths et al. (2020), who used a compositing technique to combine Sentinel-2 and Landsat 8 data into temporally equally spaced time series, we only use time series of the available cloud-free (pixelwise) Sentinel-2 images.

Another difference concerns the determination of the reference - the “idealized phenological model” - used for the calculation of the residuals, which are in turn used to detect the mowing events. Griffiths et al. (2020) developed an algorithm for selecting some points to be used to fit a third order polynomial. The result of the fit is then the reference used for the calculation of the residuals. Explorative studies conducted at the beginning of the test period yielded comparable results when selecting the points and using third order polynomials, and when simply using the entire time series and fitting second order polynomials to the data points. An adjustment to the threshold for the residuals that determine whether a mowing event has occurred was needed.

Examples of the algorithm results are shown in Figure 12 and Figure 13. The NDVI time series refer to single pixels within fields in the Sentinel-2 test tile 32TPT, for which we could obtain exact dates of the mowing events from reliable ground-truth data. Cloud and shadow masking is performed by combining Sen2Cor SCL and Cloudsen12 (Aybar et al. 2022). As demonstrated by the plots, the observations are sufficiently dense and cloud/cloud shadow masking performed well, allowing for clear detection of most mowing events. Two false negatives are seen in both Figure 12 and Figure 13.

A high-level overview of the first part of the workflow that is deployed to derive an intermediate version of the mowing dates, event counts and confidence layers is presented in Figure 14.

![Line chart showing Normalised Difference Vegetation Index (NDVI) values over the Day of Year, comparing 'True mowing events' with events detected by a 'Mowing events algorithm'. The Y-axis represents the NDVI value, ranging from 0.0 to 1.5. The X-axis represents the Day of year, ranging from 100 to 300. The data series, labelled 'NDVI Sen2Cor + Cloudsen12', is plotted with blue circles connected by a light blue line. The NDVI values generally rise from approximately 0.8 at Day 105 to a peak around 0.95 at Day 155. A sharp decline in NDVI occurs around Day 165, dropping from about 0.9 to 0.5. A 'True mowing event' (green solid vertical line) is marked at Day 168, and a 'Mowing events algorithm' detection (red dashed vertical line) is marked at Day 170. The NDVI then recovers, rising to approximately 0.9 by Day 195. A second sharp decline occurs around Day 215, dropping from about 0.9 to 0.6. A 'True mowing event' (green solid vertical line) is marked at Day 218, and a 'Mowing events algorithm' detection (red dashed vertical line) is marked at Day 220. NDVI recovers again to above 0.85 by Day 250 and remains relatively stable until Day 300. A third 'True mowing event' (green solid vertical line) is shown around Day 263, but no corresponding sharp NDVI drop or algorithmic detection follows immediately. The chart demonstrates how mowing events cause sudden decreases in NDVI and evaluates the algorithm's detection accuracy against true events, showing algorithmic detections slightly later than true events in the first two instances.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-9a30382a1e822f8c20aba634c1b8b5fe39893347.png)

Figure 12: Single-pixel NDVI time series and mowing events (ground truth and detected) for 2021 (32TPT; WGS84 coordinates: 11.3151°E, 47.5911°N).

![This is a line chart displaying Normalised Difference Vegetation Index (NDVI) values over the 'Day of year' (X-axis, ranging from 100 to 305). The Y-axis represents 'NDVI value' and ranges from 0.0 to 1.5. The primary data series, 'NDVI Sen2Cor + Cloudsen12,' is plotted with blue circles connected by a light blue line, indicating the NDVI values derived from Sentinel-2 data processed with Sen2Cor and Cloudsen12 corrections. The NDVI values generally fluctuate between 0.65 and 0.95. Three vertical lines represent mowing events: 1. Solid green lines indicate 'True mowing events.' 2. Dashed red lines indicate detections by a 'Mowing events algorithm.' The chart shows three instances of a sharp drop in NDVI value: \* The first NDVI drop occurs around Day 155, from approximately 0.93 to 0.65. The 'True mowing event' is at Day 155, and the 'Mowing events algorithm' detects an event at Day 156. \* The second NDVI drop occurs around Day 230, from approximately 0.88 to 0.65. The 'Mowing events algorithm' detects an event at Day 230, while the 'True mowing event' is at Day 231. \* A third 'True mowing event' is indicated around Day 285, corresponding to an NDVI drop from approximately 0.91, declining to around 0.70 by Day 305. No corresponding 'Mowing events algorithm' line is visible for this third event within the charted range.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-6beb035041b6456fa36fcdababaf84705f920bdf.png)

Figure 13: Single-pixel NDVI time series and mowing events (ground truth and detected) for 2021 (32TPT; WGS84 coordinates: 11.3103°E, 47.5884°N).

![This is a data processing workflow diagram for the production of Copernicus Land Monitoring Service (CLMS) Grassland Mowing (GRAM) layers, specifically Grassland Mowing Events (GRAME), Grassland Mowing Dates (GRAMD), and Grassland Mowing Events Confidence Layer (GRAMECL). The entire process is indicated as 'S2-tiles-based' (Sentinel-2 tiles based). The workflow begins with 'Retrieve input data,' which then branches into four primary input data sources: 1. 'VPP SODS and EODS' (Vegetation Phenology and Productivity Start-of-Season Date and End-of-Season Date) from the CLMS High Resolution Vegetation Phenology and Productivity (HR-VPP) layer. 2. 'VLCC HER layer' (Vegetated Land Cover Characteristics Herbaceous layer) from the CLMS High Resolution Layer (HRL) Herbaceous (HER) mask. 3. 'Sentinel 2 L2A' (Level-2A) satellite data. 4. 'Sentinel 2 L1C' (Level-1C) satellite data. The process follows these steps: 1. 'VPP SODS and EODS' and 'VLCC HER layer' are used to 'Derive start and end of season for herbaceous pixels.' 2. 'Sentinel 2 L1C' data is used to 'Compute cloud and shadow mask,' which generates a 'Cloud and shadow mask' data product. 3. 'Sentinel 2 L2A' data is combined with the 'Cloud and shadow mask' to 'Compute masked NDVI' (Normalised Difference Vegetation Index), resulting in 'Masked NDVI' data. 4. The 'Masked NDVI' data then splits into two parallel processing paths: a. One path applies a 'mowing detection algorithm pixelwise,' which generates the 'Mowing counts and dates raster' (corresponding to GRAME and GRAMD). b. The other path 'Analyse time series gaps pixelwise,' which generates the 'Confidence raster' (corresponding to GRAMECL).](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-e3e2e358e2935abec94b3406f1fbcc86ad73801c.png)

Figure 14: Processing workflow and pipeline for the GRAMD and GRAME layers part 1: Source data selection, pre-processing and cloud masking, and mowing event detection.

The mowing detection algorithm is season-based, meaning that a start and end of season are needed for the analysis of the time series. Extending the time window of the analysis beyond the true length of the growing season would result in a strong increase in false positive detections, while the consequence of using too short of a time window is the strong increase of false negatives (i.e., mowing events are not detected, being outside the analyzed time frame). The determination of the season length has been performed on Sentinel-2 tile basis, exploiting the HR-VPP layers (see section 3.3.1). By default, we use the 25th percentile of the start of season and the 75th percentile of the end of season of the herbaceous surfaces of the considered tile.

NDVI time-series are computed from the Sentinel-2 L2A, observations with clouds or shadows are removed, and the mowing event detection algorithm described above is applied within the determined vegetation season. The detection of mowing events is limited to a maximum of four events per season.

A high-level overview of the subsequent steps of the workflow is presented in Figure 15.

![This workflow diagram illustrates the processing chain for generating Copernicus Land Monitoring Service (CLMS) Grassland Mowing (GRAM) layers, specifically Grassland Mowing Events (GRAME), Grassland Mowing Dates (GRAMD), and Grassland Mowing Events Confidence Layer (GRAMECL). The process begins with two input rasters: 1. \*\*Mowing counts and dates raster\*\* 2. \*\*Confidence rasters\*\* These inputs proceed sequentially through the following steps: 1. \*\*Reproject:\*\* Both input rasters are reprojected. 2. \*\*Rearrange mowing events and confidences from season to year:\*\* The reprojected data is restructured to consolidate information from seasonal to annual scope. 3. \*\*Mosaic:\*\* The rearranged data is then mosaicked. From the 'Mosaic' step, the workflow branches into two main parallel paths that converge before finalization: \*\*Path A (GRAMD and GRAME layer generation):\*\* 4. Apply sieve filter to GRAMD layers: This step processes the data to generate 'GRAMD temporary layers'. 5. Count non-zero occurrences pixelwise across GRAMD layers: This step takes the 'GRAMD temporary layers' and computes pixel-wise non-zero occurrences, resulting in a 'GRAME temporary layer'. \*\*Path B (GRAMECL layer preparation):\*\* 6. Directly from the 'Mosaic' step, a 'GRAMECL temporary layer' is prepared and routed towards the finalization. \*\*Finalization:\*\* 7. Apply finalizing steps (format, color table, ...): The 'GRAMD temporary layers', 'GRAME temporary layer', and 'GRAMECL temporary layer' are all fed into this final processing step. The workflow concludes with the generation of the final products: \*\*GRAME, GRAMD, GRAMECL\*\*.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-303adab12940a2f66fe85851323e4e84adb79614.png)

Figure 15: Processing workflow and pipeline for the GRAMD and GRAME layers: reprojection, shift to yearly timeframes, mosaic, MMU filtering and data export.

While in most tiles the start and end of season are within a single year, some climatic areas can have a start of season in the previous year, combined with an early end of season. In those cases, the final product is derived by the combination of the season-based products, keeping only the dates within the year of interest.

Following the steps described above, the GRAMD layers in Sentinel-2 tiles are mosaicked to form EEA tiles. Furthermore, GDAL sieve is applied, aiming at reducing the unavoidable noise in the resulting raster due to fluctuations in time and space of the NDVI values. The minimum mapping unit of 0.25 ha from the product specifications corresponds to 25 pixels. The sieve filter is applied to the tile product with an extra buffer of 25 pixels, to avoid border effects at the tile boundaries, and the result is finally cropped back to the EEA tile extension. For known limitations of the spatial sieving on a multi-valued date laser please refer to section 3.4.5)

Summarizing, **the following steps are needed to derive the GRAMD layers:**

- Determination of start and end of season using **HR-VPP SOSD and EOSD** layers, masked with HER layers.

- Computation of cloud and shadow masks for dates within the growing season period.

- Computation of NDVI for dates within the growing season period, and application of cloud and shadow mask.

- Application of the mowing detection algorithm on herbaceous pixels (according to **HER** layer);

- If applicable, re-grouping of mowing events, from season to year.

- Application of the MMU of 25 pixels (0.25 ha);

- Finalizing steps (creation of the Cloud-Optimized-GeoTiffs, color tables, metadata).

### 3.4.3 Grassland Mowing Events (GRAME)

After the application of the sieve filter to the **GRAMD** layers, the **GRAME** layer is derived by counting non-zero events for each pixel.

**The following steps are needed to derive the GRAME layers:**

- Count of non-zero occurrences in the stack of **GRAMD** layers (pixelwise);

- Finalizing steps (creation of the Cloud-Optimized-GeoTiffs, color tables, metadata)

### 3.4.4 Grassland Mowing Event Confidence Layer (GRAMECL)

Long gaps in the time series reduce the capability of detecting mowing events (see also section [Section 3.4.5](#sec-Encountered-issues-and-known-limitations)). The confidence layer provides an indication of the likelihood of not having missed a mowing event and combines it with the individual confidence of each of the detected events.

The **Grassland Mowing Event Confidence Layer (GRAMECL)** gives an estimate of the confidence that the occurrence of the false negative and false positive events is minimized. All the **GRAMD** layers and the **GRAME** layer are required to derive **GRAMECL**. The confidence is computed as

\\\mathrm{GRAMECL} = 100 \times C\_{\mathrm{FN}} \times C\_{\mathrm{FP}}\\

where \\C\_{FN}\\ and \\C\_{FP}\\ are the confidences of minimizing the occurrence of the false negative and the false positive events, respectively. Both \\C\_{FN}\\ and \\C\_{FP}\\ are calculated in the range \[0,1\] (as detailed below), such that the final confidence is in the range \\G R A M E C L\\ \in\\ \[0,100\]\\, with the highest value interpreted as the 100% probability that no true mowing event was missed and no false mowing event was incorrectly detected.

The confidence \\C\_{FN}\\ is concerned with gaps in the pixelwise time series. These gaps arise either from the prolonged periods of cloudiness, or due to the intrinsic gap due to the Sentinel-2 revisit time (as high as 10-15 days in certain areas), and they can be responsible for missing mowing events (false negatives). This issue is addressed, and the definition for the confidence \\C\_{FN}\\ is developed as follows. Supposing that a given pixel has \\N\\ available points in the time series, a probability that an event was missed between any two consecutive points is defined as:

\\ p_i = \begin{cases} \frac{\Delta t_i}{\Delta t\_{\mathrm{max}}}, & \Delta t_i \leq \Delta t\_{\mathrm{max}} \\ 1, & \Delta t_i \> \Delta t\_{\mathrm{max}} \end{cases} \\

Here, \\\Delta t_i\\ represents a time gap between the 𝑖-th and the \\(i+1)\\-th observation in the time series, and \\\Delta t\_{max}\\ is a predefined tolerance window, in this case set to \\\Delta t\_{max}=28\\ days. If the time interval between the two observations is smaller than \\\Delta t\_{max}\\ according to this definition the probability that an event was missed increases linearly with the time gap \\\Delta t_i\\. In case the interval between the two observations is larger than the predefined window, the probability of a missed event is assumed to be 1. The total probability that an event was missed is then obtained as a weighted average over all the time intervals \\\Delta t_i\\ (for \\i=1,...,N-1\\), namely:

\\ P\_{\mathrm{total}} = \sum\_{i=1}^{N-1} p_i \left( \frac{\Delta t_i}{\Delta T} \right) \\

Where \\\Delta T\\ is the total length of the time series (i.e., length of the growing season in days). The final confidence is obtained as \\C\_{FN}=1-P\_{total}\\.

The confidence \\C\_{FP}\\ is concerned with the imperfections in the cloud masking. Namely, events such as shadows, haze or thin clouds can be missed by the masking algorithm, and they can lead to incorrectly detected mowing events (false positives). This issue is addressed, and the definition for the confidence \\C\_{FP}\\ is developed as follows. For a given pixel, all the mowing events detected within the **GRAMD** layers are iterated over. For an \\i\\-th mowing event, image filtering is applied to its corresponding cloud mask, using an identity kernel. More specifically, a custom kernel (filter) is introduced as a normalized 2D identity array of the shape \\61 × 61\\, thus defining a relevant area of ± 30 pixels (300 m) around the pixel of interest. The result of the filtering is the percentage of clear pixels in the area defined by the kernel, \\P\_{clear}^{(i)}\\. The values of \\P\_{clear}^{(i)} \< 1\\ indicate the proximity of the pixel to any nearby clouds, which in turn lowers the confidence that the pixel in question is a clear pixel, free from any cloud or shadow. In addition, we compute the tile-based percentage of thin clouds detected within the Sentinel-2 tile, \\P\_{thin\\clouds}^{(i)}\\ (this information is straightforwardly computed from the generated Cloudsen12 cloud masks). The confidence that the \\i\\-th mowing event is not a false positive is then obtained as

\\ {c^{(i)}}\_{FP} = P\_{\mathrm{clear}}^{(i)} \\ \Big( 1 - P\_{\mathrm{thin\\ clouds}}^{(i)} \Big) \\

The final confidence follows as the product over all single-day confidences, \\C\_{FP} = \prod\_{i=1}^{N\_{\mathrm{events}}} c^{(i)}{}\_{FP}\\

### 3.4.5 Encountered issues and known limitations

During the implementation and production of the **GRAM** layers some issues have been identified. These can be divided into several subgroups:

**MMU-related**

The requirement of a Minimum Mapping Unit for the **GRAMD** layers, albeit resulting in more uniform results, also yields some issues resulting from the need to apply a spatial filtering on complex layers presenting dates and counts.

1.  The **HER** layer used for determining the areas where to apply the mowing detection algorithm does not have an MMU. It is therefore not possible to satisfy both the mapping of mowing events for all herbaceous pixels and the MMU of 0.25 ha of the **GRAMD**. As a result, the **GRAMD** still contains patches below the MMU in particular in small HER patches.

2.  The GDAL sieve[^10] filter needs to be applied independently to each of the four **GRAMD** layers. This filter ensures that patches of DOY-values smaller than the threshold of 0.25 ha (25 pixels) are replaced by the value of the largest neighboring patch, but only if the size of the neighboring patch is larger than the threshold. Since this filtering is applied individually to each **GRAMD** layer (**GRAMD_1, GRAMD_2, …**), in some cases, the newly assigned value is already present in one of the other mowing event date layers at the same location (i.e. the same pixels). In such cases, it results in date duplication, where timing of the first mowing event (**GRAMD_1**) and the second mowing event (**GRAMD_2**) share the same DOY. This occurs in approximately 0.4 % of the herbaceous pixels.

3.  The independent filtering of the **GRAMD** layers explained in the previous point can also result in a fictitious increase in the mowing count of the **GRAME** layer. Furthermore, the MMU requirement cannot be guaranteed in the resulting **GRAME** layer, because the MMU-compliant patches in the single GRAMD layers could overlap in an “unfavorable” manner. On the other hand, not re-counting the events after sieving or applying a second filter on the GRAME would result in strong inconsistencies across the different layers.

**Verification and quality control**

A quality assessment of the **GRAM** layer is very challenging due to lack of reliable and representative ground-truth data across Europe.

**Related EO input data**

Cloud cover can strongly reduce availability of usable data. This issue is dependent on the region, with an example of average cloudiness shown in Figure 16 (a). Sentinel-2 observation pattern and the associated swath borders lead to differences in the data availability in different regions, with some regions experiencing an average gap as high as 10-15 days (in combination with cloud coverage). The Sentinel-2 observation gaps are shown in Figure 16 (b). These gaps can result in noticeable border issues/data stripes in the **GRAME** product (see Figure 17).

In some case the atmospheric correction of the L2A also seems to be a cause of false positive mowing detection. Further investigations in this regard will be needed.

**Cross-year season**

For some tiles with an early start of the vegetation period, the mowing season associated with a reference year may begin in the previous calendar year. Likewise, the subsequent season, which for the next year, may already start within a given reference year. Since the production of the VLCC products (incl. the GRAM) has been conducted in several phases (2017-2021, 2022-2023, 2024) this can result in incomplete detection of mowing events for the final year in the production interval, as data from the following season is not yet processed. To ensure consistency and completeness, it may be necessary to include an additional year of data for tiles with early season starts and for the final year of the production interval.

![Two choropleth maps titled 'Sentinel-2 A&B L1C' display data at 1km resolution for the EEA (European Environment Agency) 39 countries in 2018. Map (a) shows 'Cloudiness \[%\]': The colour scale ranges from dark blue (10% cloudiness) to red (100% cloudiness), with intermediate values in shades of blue, green, yellow, and orange. Regions with higher cloudiness (yellow to red) include Iceland, Ireland, the United Kingdom, parts of Scandinavia, and the Alpine regions of Central Europe. Southern Europe (e.g., Spain, Greece, southern Italy) and parts of Eastern Europe show lower cloudiness (blue to light green). An inset map focuses on the Alpine region, showing detailed variations in cloudiness. Map (b) shows 'Average gap \[days\]': The colour scale ranges from dark blue (3 days average gap) to dark red (15 days average gap), with intermediate values in shades of blue, green, yellow, and orange. The map displays a distinct diagonal striped pattern across Europe, which reflects the Sentinel-2 satellite acquisition swaths. Within these stripes, areas with higher average gaps (red/orange) are visible in parts of the United Kingdom, Scandinavia, and Central Europe, while other areas (blue/green/yellow) show lower average gaps. An inset map focuses on the Alpine region, also illustrating this striped pattern of average gaps. The data originates from Sentinel-2 A and B Level-1C products.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-cc948934135584de49fbd4cb942740dcde2e9c17.jpg)

Figure 16: Sentinel-2A and - 2B L1C data coverage in 2018. Shown are (a) average cloudiness, and (b) average gap between cloud-free observations.

![A map showing the spatial distribution of inferred mowing events in a European rural landscape, derived from satellite imagery. The map displays agricultural areas, forests (dark green/black), and water bodies (blue). A legend defines the colour coding for the number of mowing events: \* Light green: 1 mowing event \* Medium light green: 2 mowing events \* Medium dark green: 3 mowing events \* Darkest green: 4 or more (4+) mowing events A yellow arrow highlights an area in the lower left quadrant dominated by small, fragmented light green patches, indicating a single mowing event. This area visually exemplifies the challenge of applying a Minimum Mapping Unit (MMU) of 0.25 ha to the Copernicus Land Monitoring Service (CLMS) Grassland Mowing Detection (GRAMD) layers, where patches from herbaceous (HER) layers, which lack an MMU, result in GRAMD output containing features below the specified MMU. No geographic labels, scale bar, compass, or data source year are visible.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-321da7a884def72c625e69183efbbe9654e38607.jpg)

Figure 17: Visibility of the Sentinel-2 swath borders and the different swath coverage in the GRAME layer (32TPT; WGS84 coordinates: 10.63480°E, 47.65318°N).

## 3.5 HRL Crop Type

This section gives an overview of the methodology employed to produce the layers Crop Type (CTY) and the Crop Type Confidence Layer (CTYCL).

### 3.5.1 Input data

Before the pixel-based inputs are fed to the model, minimal pre-processing is applied to transform the raw inputs to a consistent format. Optical Sentinel-2 data is first cloud-masked based on the official L2A scene classification value to which an erosion-dilation process is applied to enhance the cloud/shadow mask. Next, a 10-day compositing window is applied where the median operator is used if multiple observations are available. Finally, any remaining missing values are linearly interpolated to prevent gaps in the input data, as the presence of ‘no data’ values can lead to model instability. The 20m optical bands are resampled to 10m resolution by applying a nearest neighbour interpolation.

Sentinel-1 backscatter is derived from Level-1 GRD (Ground Range Detected) products, which have been pre-processed to correct for geometric distortions. To obtain meaningful surface backscatter values, sigma nought backscatter is calculated from these GRD products using the ellipsoidal Earth model. For enhanced accuracy, the Copernicus 30 m Digital Elevation Model (DEM) is also applied to support radiometric correction, compensating for terrain effects and ensuring consistent backscatter values across varying landscapes. By default, only one orbit direction (Descending) is kept, as the model is designed to handle a single Sentinel-1 orbit pass. Combining ascending and descending orbits could mix signals acquired under different viewing geometries, potentially leading to a loss of relevant information. Additionally, using both orbits would significantly increase processing costs without a clear benefit for model performance. The available observations are composited with the 10-day windows where multiple acquisitions are averaged. Any rare missing values are linearly interpolated. Finally, the backscatter intensity values are converted to decibel values. If there is insufficient Descending data (data gaps \> 10 days, especially happened over northern Europe) also Ascending data is used.

The Copernicus 30m DEM is used to derive altitude and slope at the pixel level, for which resampling to the Sentinel-2 10m grid is performed. Finally, the daily mean temperature variable is extracted from the original AgERA5 meteorological data, aggregated into 10-day intervals, and resampled to the Sentinel-2 10 m grid.

### 3.5.2 Classification algorithm and inference

The classification algorithm consists of a transformer-based feature extractor followed by a downstream crop classification head (Vaswani et al., 2017; Zerveas et al., 2021) (Figure 18). These two parts are coupled into one model which is trained end-to-end based on the available training data. Input to the model are the aligned inputs from the source-specific preprocessing steps. Time series from optical Sentinel-2 bands (“B02”, “B03”, “B04”, “B05”, “B06”, “B07”, “B08”, “B11”, “B12”) and radar Sentinel-1 backscatter (VH and VV) are jointly fed into a transformer-based encoder, which is designed to automatically extract the most relevant features for crop type classification. To better align similar inputs from different regions in Europe, the encoder model simultaneously has access to the temperature time series data in order to better differentiate the observed satellite time series across varying meteorological conditions. The transformer architecture contains an attention mechanism that learns to extract relevant information within and across the different input data streams. The original optical Sentinel-2 bands, radar Sentinel1 backscatter intensities, and meteorological time series are directly fed into the transformer encoder for automated feature extraction. Inputs that lack a temporal dimension are fed as scalars to a dense encoder for simple feature extraction. The output of the feature extractor (encoder) part represents a highly condensed and informative representation of the inputs and because the model is trained in a fully-supervised manner, the extracted features are already finetuned towards a crop classification task. Traditional manual feature engineering is hence not needed in this setup.

Once the features (embeddings) have been extracted, explicit fusion of the different inputs happens by concatenating these features before feeding them to a multi-layer perceptron classification head consisting of several stacked dense layers. Final output of the classification head is a probability of an input belonging to a crop type label, with probabilities of all labels summing to one. Final classification is performed by assigning to each 10m pixel from the 19 crop type classes the label that has the highest probability.

The model was trained on an extensive in-situ dataset of almost one million samples compiled from LPIS-GSA, LUCAS datasets and active learning sampling (Table 3) (Eurostat, 2018). The original LPIS-GSA and LUCAS datasets have each been fully harmonised towards a common crop type nomenclature (available for download, [here](https://artifactory.vgt.vito.be/artifactory/auxdata-public/worldcereal/legend/WorldCereal_LC_CT_legend_latest.csv)). The harmonized version of each dataset, along with the harmonization procedure and the translation of original crop type labels to harmonized labels, have all been published on the [WorldCereal Reference Data Module](https://rdm.esa-worldcereal.org/) (RDM) and are available for anyone to use. More general information about this harmonization procedure and on how to navigate the WorldCereal RDM application, is available on the [WorldCereal documentation portal](https://worldcereal.github.io/worldcereal-documentation/rdm/overview.html). In a next step, each individual dataset has been subsampled to derive a representative training dataset at European scale, avoiding as much as possible spatial and temporal bias and ensuring a label-balanced training dataset. This subsampling was done in an iterative way for each dataset separately:

1.  A fully random sample was drawn across all crop types available in the dataset. The initial sample size was chosen dynamically per dataset depending on the dataset’s spatial extent and the number of years available for the region. This first random step ensured the most dominant crop types for the region were sufficiently represented. Only grassland was ignored during this initial stage, to avoid massive bias towards this dominant land cover class.

2.  On top of the initial random sampling stage, we identified a number of “focus crops” for which we ensured a minimum number of samples taken from the dataset. Focus crops were defined as the target crops to be included in the eventual pan-European crop type maps. In case of cereals, the most dominant cereal types (wheat, barley, rye, oats, triticale) were sampled separately. Again, the minimum number of crop-specific samples were defined dynamically per dataset, depending on its spatial and temporal extent.

3.  Depending on early model iterations and testing, additional samples for targeted crop types in targeted regions were dynamically added to the training dataset. This for instance included additional wheat and barley data in Southern Europe.

Finally, all training data was merged into a final representative training dataset, which was used to train a single model that generalizes well across all regions and can be reused for crop classification on a yearly basis.

![This diagram illustrates the pixel-based workflow for the Crop Type (CTY) and Crop Type Confidence Layer (CTYCL) algorithm. 1. \*\*Pixel-based inputs\*\* are divided into two streams: \* \*\*Timeseries inputs:\*\* Sentinel-1 timeseries, Meteo timeseries, and Sentinel-2 timeseries are fed into a 'Transformer encoder'. \* \*\*Scalar inputs:\*\* Scalars, specifically Altitude and Slope, are fed into a 'Dense encoder'. 2. Both the Transformer encoder and the Dense encoder produce separate 'Embeddings'. 3. These individual embeddings are then combined into 'Concatenated embeddings'. 4. The concatenated embeddings are passed to an 'MLP classification head' (Multi-Layer Perceptron classification head). 5. The final \*\*Pixel-based output\*\* consists of the 'Crop type label & confidence'.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-30f252232ca825a8c65e2f9d4607446160de7470.png)

Figure 18: Schematic overview of the crop type model architecture

Table 3: Overview of the used training points per dataset and year for the CTY model training

| Country/Region           | Years                  | Number training points |
|--------------------------|------------------------|------------------------|
| Austria (LPIS/GSA)       | 2018, 2019, 2020       | 160 174                |
| Germany (LPIS/GSA)       | 2021                   | 77031                  |
| Denmark (LPIS/GSA)       | 2019                   | 39596                  |
| Estonia (LPIS/GSA)       | 2021                   | 16874                  |
| Spain (LPIS/GSA)         | 2019, 2020, 2021       | 133 830                |
| Finland (LPIS/GSA)       | 2021                   | 28138                  |
| Belgium (LPIS/GSA)       | 2018, 2019, 2020, 2021 | 52938                  |
| France (LPIS/GSA)        | 2019, 2020             | 108 158                |
| Croatia (LPIS/GSA)       | 2020                   | 12111                  |
| Lithuania (LPIS/GSA)     | 2021                   | 26243                  |
| Latvia (LPIS/GSA)        | 2021                   | 42226                  |
| Sweden (LPIS/GSA)        | 2021                   | 36374                  |
| Slovakia (LPIS/GSA)      | 2021                   | 46609                  |
| Europe (LUCAS)           | 2018                   | 26294                  |
| Europe (Active learning) | 2019, 2020, 2021       | 17196                  |

The trained model is deployed as part of an OpenEO[^11] workflow that covers in an end-to-end way the cloud-based access to the required algorithm inputs, preprocessing steps as described above, model inference, and writing of the output product. Parallelisation is done automatically after tuning the necessary parameters such as the height and width of individual processing windows. The CTY processing is based on 20km LAEA sub-tiles of the original LAEA 100km grid.

### 3.5.3 Post-processing

In the postprocessing pipeline (Figure 19 & Figure 20), each 20km LAEA sub-tile is postprocessed independently, except for the temporal rule-based postprocessing and the tile padding for GDAL Sieve steps. First, the cropland layer derived from **BVL** (classes ‘Annual arable cropland and perennial (permanent) crops’, ‘Tree crops’ and ‘Overlap herbaceous–Tree cover’) is applied as a basic mask, setting non-cropland pixels as well as out of scope zones. In that step, a correction is also performed for pixels which are classified as grass and fodder by the crop type model but for which the **BVL** considers them as permanent crops. In that case, the pixels crop types are changed to the permanent crop class with the highest probability. Then, remaining cropland pixels are reclassified by performing spatial smoothing with a gaussian kernel (3x3) on every perclass probability and re-assign the pixel’s class from the new highest probability. This allows to improve class consistency within fields, as the crop type classifier is pixel-based. The result of this process gives the intermediate crop type with grass/fodder crops included that is transferred to the herbaceous layer. The grass/fodder crops locations are removed from the crop type product for the next steps.

Afterwards, an interannual consistency correction is applied on the full time series (2017-2021). Products on the same location but for different years are concatenated together before running the correction. The following three cases are covered:

- When a sequence of crop types consists of only permanent crops, except for one year (that is not in the edges) then corrects that sequence to the permanent crop class that has the maximum accumulated probability over the sequence. Cases from the edge years are excluded as they may indicate transitions between arable and permanent crop states. Thus, sufficient data is lacking to make reliable assumptions.

- When a full sequence (including edge years) of permanent crops does not have the same crop type, then sets that sequence with the permanent class that has the maximum accumulated probability over the sequence. This operation helps by having a more consistent prediction in permanent crop cases.

- When a pixel of permanent crop class is in-between two arable years, which could correspond to (temporarily) fallow conditions, this pixel is set to the background class (0). For the same reasons as described in the first point, the edge years are not modified by this operation.

Grass and fodder classes are ignored in interannual consistency corrections and are treated as the background class. In addition, pixels that do not correspond to cropland for all the years of the analysis are ignored, as again the information is insufficient to make assumptions.

Thereafter, pixels where the maximum probability of all predicted classes is below 25% are set either to unclassified arable cropland or undecided permanent crop, dependent to which category the class with the highest probability belongs.

Isolated pixels and small fields are finally cleaned using the GDAL Sieve operation with a MMU of 0.25 ha and connectivity 4. In addition to obtain more consistent land cover maps, this operation also ensures a minimum mapping unit of 0.25ha for each field. To avoid artefacts at the boundaries between tiles, a padding must be added to each sub-tile before running the spatial cleaning. Once the padding is performed, the GDAL Sieve operation replaces every field with an area below the threshold of 0.25ha by changing the class to the class of the neighbour field with the largest area, including the background class (0) in the calculation to remove small, isolated fields. Pixels that were excluded by previous operations remain excluded after GDAL Sieve.

Finally, 20km sub-tiles are combined in larger tiles to obtain the final 100km crop-type and probability products.

![This diagram illustrates the post-processing workflow for Crop Type (CTY) and intermediate grassland products, covering three consecutive years: Year N-1, Year N, and Year N+1. The workflow consists of two main parallel processes: an 'Independent pixel-based run' and a 'CTY Post-processing pipeline', with a central 'Temporal rule-based postprocessing' component influencing the CTY pipeline. \*\*Independent pixel-based run (left side):\*\* For each year (N-1, N, N+1), the process steps are: 1. Input data streams are fed into a Classification Model. 2. The Classification Model produces raw output including Crop-type, Max probability, and Per-class probability. 3. BVL Masking is applied, using the cropland layer. 4. Spatial smoothing & Reclassification is performed. 5. This yields 'Intermediate Grassland product' for each respective year (Year N-1, Year N, Year N+1). All 'Intermediate Grassland products' for Year N-1, Year N, and Year N+1 collectively feed into a 'HER layer'. \*\*CTY Post-processing pipeline (right side):\*\* This pipeline uses 'Intermediate post-processed CTY' products. \* For Year N-1, the 'Intermediate post-processed CTY Year N-1' leads directly to 'Final products CTY - CTYCL Year N-1'. \* For Year N+1, the 'Intermediate post-processed CTY Year N+1' leads directly to 'Final products CTY - CTYCL Year N+1'. \* For Year N, the 'Intermediate post-processed CTY Year N-1', 'Intermediate post-processed CTY Year N', and 'Intermediate post-processed CTY Year N+1' (implicitly, as inputs to the temporal rule-based postprocessing) contribute to a 'Temporal rule-based postprocessing' step. The output of this temporal postprocessing influences the initial 'Apply threshold for unclassified pixels' step within Year N's CTY post-processing column. The steps for Year N are: 1. Apply threshold for unclassified pixels. 2. Remove grass and fodder classes. 3. This results in 'Intermediate post-processed CTY Year N'. This step involves 'Padding with Neighbor tiles' (using data from adjacent tiles). 4. GDAL Sieve (Minimum Mapping Unit - MMU) is applied. 5. This produces 'Final products CTY - CTYCL Year N'.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-78c38c35d79557f1150fa0e6918cd84024ca4f22.png)

Figure 19: CTY postprocessing pipeline flowchart

![This diagram is a post-processing decision tree for crop type classification, outlining the logical flow from raw input to final cropland classification. The process begins with 'CTY raw input' (Crop Type Year raw input) and proceeds through a series of conditional evaluations, with final classifications being 'No cropland', 'Annual cropland', or 'Permanent cropland'. The workflow is as follows: 1. \*\*Initial Cropland Check:\*\* \* The 'CTY raw input' is first evaluated against the 'Cropland (BVL)' (Basic Vegetation Layer) condition. \* IF 'Cropland (BVL)' is No, THEN the output classification is 'No](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-b752ff52dd8f50223ebe874203e33a0c3406029f.png)

Figure 20: Decision tree of the CTY postprocessing pipeline, outlining the main steps from raw crop type probabilities to final output classes. For clarity, output categories are simplified to ‘permanent’ and ‘annual’ cropland, as the decision rules were specifically designed for these classes. Note that spatial operations (defined in Figure 19) such as spatial smoothing and GDAL Sieve, although they may further modify crop type labels, are not included in this diagram to maintain readability

### 3.5.4 Crop Type Confidence Layer

The Crop Type Confidence Layer (CTYCL) provides a per-pixel estimate of the classification confidence by reporting the final probability associated with the selected crop type label at 10-meter resolution. This probability originates from the crop type classification model output, where each crop class is assigned a confidence value. However, the final probability values may be modified during the crop type postprocessing chain, which ensures spatial and temporal consistency. Specifically, the following chronological steps can influence the confidence values:

- Spatial smoothing: A 3×3 Gaussian filter is applied to the per-class probability output, enhancing spatial coherence across neighbouring pixels. Pixel classes are re-assigned based on the updated highest probability, which may differ from the original model output.

- Interannual consistency correction (see also above): When a permanent crop is missing (excluding edge years) in a single year of an otherwise consistent time series, or when the sequence includes different permanent crop types, the final crop type class will be adjusted. In these cases, the pixel’s confidence value is recalculated as the average probability of the selected permanent crop class across the time series.

- GDAL Sieve operation: To remove small, isolated patches, pixel values are reassigned based on the dominant neighbouring class. If a pixel’s class is changed during this step, its probability is updated to reflect the confidence of the newly assigned class.

Pixels that are reassigned to the background class during postprocessing steps are assigned the “no cropland” confidence value of 253.

### 3.5.5 Encountered issues and know limitations

During the quality assurance process, minor **violations of the minimum mapping unit (MMU)** requirement were detected in non-cropland areas of the crop type layer (2017-2021).Specifically, the issue arose due to the GDAL Sieve operation being applied in a single pass. While a single pass may suffice for layers with a limited number of classes, it is not adequate when more than four distinct classes are present. In such cases, multiple sieving iterations are necessary to fully enforce the MMU constraint.

Although the original implementation included checks to address this limitation, non-cropland pixels were unintentional excluded from these checks. As a result, small patches of non-cropland remained below the MMU threshold. The overall impact of this issue is minimal, affecting approximately 0.0002% of the total crop type pixels.

Despite the application of postprocessing steps aimed at improving consistency, some **implausible crop type sequences** remain in the final crop type product (2017-2021). These arise from the inherent trade-off between enforcing temporal and spatial consistency. Interannual consistency checks promote temporal stability across years, while spatial consistency is enhanced using the GDAL Sieve operation. However, strictly enforcing both constraints would result in overly homogeneous patches, undermining the high-resolution detail offered by the 10-meter product.

This challenge is particularly pronounced in heterogeneous and complex landscapes such as those found in southern Europe, including agroforestry systems like Dehesa. In such regions, mixed sequences of permanent and annual crops may still appear, even if they are agronomically unlikely.

Additionally, the presence of the no-cropland class (label 0) within a sequence can be explained by various factors. These include the removal of grass/fodder pixels during postprocessing, reclassification through interannual consistency checks, or changes introduced by the GDAL Sieve operation. Such instances result in discontinuities within the crop type sequences.

Finally, the limited five-year time span of the dataset may not be sufficient to fully identify and correct all implausible sequences. Future observations beyond this period could help to better identify consistent crop type sequences and further reduce inconsistencies.

## 3.6 HRL Cropping Pattern

This section gives an overview of the methodology employed to produce the **Cropping Patterns (CP)** layers which includes a comprehensive of layers that provide details on the timing and extent of agricultural practices along five thematic groups being Main crops, Bare soil, Secondary crops, Fallow land and Cropping Seasons.

### 3.6.1 Input data

The **HRL Cropping Patterns (CP)** layers entail a wide set of layers relying on both Sentinel-2 optical and Sentinel-1 SAR-based satellite data. The **HRL CTY** layer is used to define the focus locations of the **CP** layers generation.

Sentinel-2 and Sentinel-1 backscatter data are pre-processed in a similar way as for the **CTY** layer, with some minor differences. In case of Sentinel-2 only a subset of relevant bands is retained, including band 2,3,4,8, 11 and the incident angles information. The latter is needed to derive fraction of Absorbed Photosynthetic Active Radiation (fAPAR) at 10m.

For the Sentinel-1 backscatter both the ascending and descending orbits information are combined to ensure maximum data availability required for detecting abrupt events like field harvest. Extraction of the data is done at field level, resulting in timeseries per field. Field boundaries are defined using a delineation algorithm.

### 3.6.2 Product structure

The **CP** portfolio compromises a diverse range of layers, derived from field level seasonal information. The methodology used to obtain field level seasonal information and derived cropping pattern layers is shown in Figure 21. In a first step, the locations for which CP layers are derived are filtered, i.e., only fields that are delineated and are dominantly covered by an annual crop are retained. The field delineations are obtained by using a 3D Res-UNet field delineation algorithm which uses Sentinel-2 images. Only fields above the MMU of 0.25 ha and which are classified as an annual crop by the **CTY** layer are retained. For this subset of delineated fields, Sentinel-1, and Sentinel-2 timeseries are retrieved, which are necessary inputs for the harvest and emergence detection. The detected harvest and emergence events are used to derive a maximum of two growing seasons per year based on expert rules. The workflow results in several CP layers, which are subdivided into 5 thematic themes:

- **Main crops**

- **Bare soil**

- **Secondary crops**

- **Fallow land**

- **Cropping Seasons**

All vector-based **CP** layers are rasterized to 10 m spatial resolution to align with **HRL CTY** layer. Although the original **CP** layers are derived exclusively from delineated parcels larger than the defined MMU of 0.25 ha, a final spatial alignment with the **HRL CTY** layer is required to ensure consistency across product layers. This alignment step involves clipping the field-based **CP** outputs to the **CTY**-classified (pixel-based) annual cropland extent. As a result, some **CP** outputs—originally MMU-compliant—may appear as smaller spatial fragments due to partial overlap at field boundaries. While this may produce local patterns below the MMU threshold, these are a by-product of spatial alignment rather than the initial **CP** derivation. Reapplying a sieving operation at this stage to enforce the MMU would risk removing valid and relevant **CP** information, particularly in transitional or fragmented agricultural landscapes. Moreover, the clipping step alone already leads to some loss of **CP** content, and further filtering would compound this loss.

In the following sections, the methods used to delineate growing season(s) and derive the corresponding **CP** layers are described.

![This diagram illustrates the methodology workflow for producing Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Cropping Patterns (CP) layers. The process is divided into five main stages: Raw Input, Filtering, Parcel based input, Growing season delineation method, and Cropping pattern layers (outputs). 1. \*\*Raw Input\*\*: Initial data sources include the HRL Crop Type (CTY) layer, Parcel delineation, Sentinel-2 optical satellite data, and Sentinel-1 Synthetic Aperture Radar (SAR) satellite data. 2. \*\*Filtering\*\*: \* The HRL CTY layer undergoes an 'Annual crop filter' to generate a 'Crop mask'. \* The 'Parcel delineation' data is processed by a 'Minimum Mapping Unit (MMU) filter' to create 'Cleaned parcels'. \* The 'Crop mask' is then applied to the 'Cleaned parcels' to refine the areas of interest, which then become the input for the next stage. 3. \*\*Parcel based input\*\*: \* The 'Cleaned parcels' are combined with pre-processed 'Sentinel-2' data via a 'Mean operator' to produce 'Sentinel-2 time series'. \* In parallel, the 'Cleaned parcels' are combined with pre-processed 'Sentinel-1' data via a 'Mean operator' to produce 'Sentinel-1 time series'. 4. \*\*Growing season delineation method\*\*: \* Both the 'Sentinel-2 time series' and 'Sentinel-1 time series' feed into 'Emergence detection' and 'Harvest detection' modules. \* Outputs from 'Emergence detection' and 'Harvest detection', along with 'Expert rules', are used as inputs for the central 'Growing season delineation' module. 5. \*\*Cropping pattern layers\*\*: The 'Growing season delineation' module generates five thematic groups of Cropping Patterns layers: \* \*\*Main crops\*\*: This group includes sub-layers for 'Main crop harvest + confidence', 'Main crop emergence + confidence', and 'Main crop duration + confidence'. \* \*\*Bare soil\*\*: This group includes sub-layers for 'Bare soil before + confidence' and 'Bare soil after + confidence'. \* \*\*Secondary crops\*\*: This group includes sub-layers for 'Secondary crops type', 'Secondary crops emergence', and 'Secondary crops duration + confidence'. \* \*\*Fallow land\*\*: This group includes sub-layers for 'Fallow land presence + confidence' and 'Fallow land duration + confidence'. \* \*\*Cropping Seasons\*\*: This group includes sub-layers for 'Cropping seasons yearly' and 'Cropping seasons types over 3 years'.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-5aebd0eb11363c76ebc7b03745474b57189972ca.png)

Figure 21: Schematic overview of cropping pattern products generation.

### 3.6.3 Growing season delineation

The growing season delineation at field level forms the basis for the **CP** layers generation. The methodology used to determine the growing season delineation is shown in Figure 22. The onset and end of the season is based on the detected emergence and harvest events (see sections below), respectively. The detected emergence and harvest events are used in expert rules to determine the growing seasons (see sections below).

![This diagram illustrates the methodology for deriving High Resolution Layer (HRL) Cropping Patterns (CP) layers, structured into three main phases: Pre-processing, Methods, and Post-processing. \*\*Pre-processing:\*\* 1. \*\*Sentinel-2 time series\*\* are processed to derive two key outputs: \* Normalised Burn Ratio 2 (NBR2) \* Fraction of Absorbed Photosynthetic Active Radiation (fAPAR) 2. \*\*Sentinel-1 time series\*\* are processed to derive three outputs: \* Two Vertical-Horizontal (VH) polarization components \* One combined Vertical-Horizontal / Vertical-Vertical (VH/VV) polarization component All NBR2 and fAPAR outputs from Sentinel-2, along with two VH polarization outputs from Sentinel-1, are fed into a module labelled \*\*CropSAR\*\*. The remaining VH and VH/VV outputs from Sentinel-1 are fed directly into the subsequent 'Methods' stage. \*\*Methods:\*\* 1. The CropSAR output feeds into \*\*Emergence detection + confidence\*\*. 2. The VH and VH/VV outputs from Sentinel-1 feed into \*\*Harvest detection + confidence\*\*. 3. Both Emergence detection and Harvest detection contribute to the Post-processing stage via 'Expert rules'. \*\*Post-processing:\*\* 1. The 'Expert rules' derived from Emergence detection and Harvest detection are used for \*\*Growing season delineation + confidence\*\*.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-7ada907705c4edf3e61d95d290fbdd4b8e17b4df.png)

Figure 22: Schematic overview of the growing season delineation.

#### 3.6.3.1 Emergence detection

The inflection behavior of the spectral signal around the moment of emergence is used to detect emergence events. As spectral signal, daily fAPAR values obtained from the CropSAR technology are used. CropSAR is a deep learning method that allows to fill-in the cloud gaps in fAPAR timeseries using the relationship between Sentinel-2 fAPAR and Sentinel-1 backscatter data (CropSAR, 2024; Piccard et al., 2023). Optical fAPAR data were preferred to Sentinel-1 derived features since fAPAR is not influenced by soil structure and moisture content around emergence (Khabbazan et al, 2019). Additionally, the change of fAPAR around the emergence period is quite gradual. A rule-based approach was used to determine emergence events as deep learning methods depend on a substantial amount of training which were not available.

Field data on emergence dates (+- 200) of agricultural fields, located mainly in Belgium, were used to investigate the behavior of the fAPAR signal around emergence. From this, generalizable rules and threshold could be defined to allow a robust and consistent emergence detection as shown on Figure 23. The values of the parameters are obtained by applying a Monte Carlo simulation. Emergence is detected shortly after the occurrence of a slope inflection of the CropSAR timeseries (Figure 23), this is also confirmed in literature (Gao et al., 2017; Gao et al., 2021). Some additional parameters are used to check if the slope inflection is related with a clear seasonal signal (i.e., amplitude, duration until season peak, …). Within the literature it is also clearly confirmed that emergence typically occur after an inflection of the time series from optical derived data (Gao et al., 2017; Gao et al., 2021). The detected emergence date corresponds with the unfolding of the first leaves of the crop on the field.

![Line chart displaying the evolution of a smoothed CropSAR signal over time, from March 2022 to August 2022. The Y-axis represents CropSAR values, ranging from 0.0 to 1.0. The X-axis represents time, showing dates from 2022-03 to 2022-08, with 'Offset days' indicated on the axis. The main data series, 'CropSAR (smoothed)' (green line), starts around 0.2 in March 2022, gradually decreasing to approximately 0.1 around early May. It then shows a sharp increase, peaking at around 0.85-0.9 in early July, before declining again. Key annotations and reference lines are present: \* A 'Baseline value' is indicated by green text pointing to the early, relatively flat segment of the CropSAR curve (around 0.1-0.15). \* A first 'Slope inflection' point is marked by a blue dot on the curve around 2022-05, where the CropSAR value is approximately 0.1, indicating the beginning of the steep growth phase. \* 'OBSERVED EMERGENCE' is represented by a solid red vertical line, positioned just after the first slope inflection point, around May 2022. \* 'PREDICTED EMERGENCE' is represented by a dashed black vertical line, positioned shortly after the observed emergence, around late May / early June 2022. \* 'Offset days' is a bracket on the X-axis measuring the temporal difference between the OBSERVED EMERGENCE and PREDICTED EMERGENCE lines. \* A second 'Slope inflection' point is marked by a blue dot on the curve around early July, coinciding with the peak CropSAR value of 0.85-0.9, where the growth rate slows or reverses. \* 'Δ duration' is a horizontal dashed orange line extending from the CropSAR value of the first inflection point to the vertical projection of the second inflection point, representing the duration of the main growth period. \* 'Seasonal amplitude' is a vertical dotted yellow line extending from the baseline CropSAR value to the peak CropSAR value at the second inflection point, illustrating the total signal change during the season. The chart visually demonstrates the methodology for detecting and characterizing crop emergence and growth phases from CropSAR time series data.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-0b015b66e7689d69b6db9b63a616bcca4a767ec0.png)

Figure 23: Different parameters selected for detecting an emergence event out of a seasonal profile.

#### 3.6.3.2 Harvest detection

Harvest is defined as the moment of total removal of standing biomass from the field. For the harvest detection, a sequential neural network is trained to identify a harvest event out of set of selected satellite derived features. 600 fields with information on harvest date (both on the main season and for some on the secondary season) are used for model training. Most of these fields are in Belgium, Italy, Greece, and Austria and cover a wide range of the most common cultivated crops. The model is trained such that a detection of a harvest event aligns with the agreed definition on harvest. The following spectral features are used in the harvest detection algorithm:

- fAPAR (CropSAR)

- Sentinel-2 Normalized Burnt Ratio 2 (NBR2) (Alcaras et al., 2022)

- VH/VV in decibels derived from Sentinel-1 backscatter.

The selected features complement each other. The VH/VV ratio does respond more to the structural changes of the field at harvest, while the other two features do react more on the biophysical change (Meroni et al., 2021; Van Tricht et al., 2018). The NBR2 is added as it is particularly sensitive for harvest at low fAPAR values. This typically occurs in cover crops or maize that are in a far stage of senescence at harvest. In such case, the fAPAR signal is not enough to properly detect a harvest event and the signal received from VH/VV is not that clear anymore due to the collapse (loss of structure) of the crop. All the different features are brought on a 6-daily temporal scale, in case of the NBR2 a Whittaker smoother has been applied to fill-in the cloud induced gaps. Gaps in Sentinel-1 VH/VV are linearly interpolated. The 6-daily time series of CropSAR, NBR2 and VH/VV are used in the harvest detection sequential neural network model.

#### 3.6.3.3 Season delineation

For the season delineation, all the emergence and harvest events in a period of 6 months before and after the reference year of interest are retained. This six-month period is added to also be able to detect seasonalities that do not fall within the year boundaries (e.g., secondary crops and winter cereals). In the first step, the emergence and harvest detections are cleaned and associated with a single seasonality to categorize it as either a main or secondary season. A series of expert rules, derived from an examination of seasonal boundaries at the European level in conjunction with United States Department of Agriculture (USDA) crop calendar data, are used for labeling the seasons (see Table 4). These rules are fully independent from the **CTY** crop labels to avoid error propagation. For both main and secondary crops, some further sub-seasonality labelling is done to differentiate between winter & spring crops and secondary crops growing before or after the main growing season of that reference year. Each of these sub-seasonality categories have different periods in which they can occur (Table 4). The sub-seasonality categorization can further assist in prioritizing the final selection of the labelled seasons as main or secondary season if multiple seasons conflict within one of these categories.

Additionally, also regional dependent seasonal bounds are defined due to different growing season periods within Europe. Therefore, Europe has been divided into two zones based on the Metzger environmental zones, which is based on variations in climatic conditions across the continent, for seasonal labeling (Metzger et al. 2018). The translation of the original environmental zones into the two zones is shown in Table 5. The subdivision is mainly dividing more temperate/cold climates from warm/Mediterranean climates within the European continent. In the latter, onset of the main growing season is substantially earlier compared to the colder climates where temperature delays the season onset.

The expert rules for season labelling are described below:

- Emergence and harvest are chronologically linked together into a season.

- A season that ends before the start of the reference year or starts after the end of that year, is removed.

- Seasons with a length below 40 days or above 365 days are removed.

- The remaining seasons are labelled into one of the following options (based on the defined limits in Table 4):

  - Spring crop

  - Winter crop

  - Secondary crop before the main season

  - Secondary crop after the main season

  - No labelling possible (if it does not fit to one of the above categories)

- If a season falls in the seasonal limits of two types of sub-seasons, the following labelling priority is given:

  - Overlap between winter and spring crop season:

    - Days overlap season in spring crop season period \> days overlap in winter season period → spring crop.

    - Days overlap season in spring crop season period = days overlap in winter season period → spring crop.

    - Days overlap season in spring crop season period \< days overlap in winter season period → winter crop.

  - Overlap between spring crop and secondary crop after main season → spring crop.

- Eventually, the final seasons used for generating the layers on main and secondary crops are defined as follows if there is a conflict (multiple occurrences) in one of these categories:

  - Main season:

    - Spring crop season \> winter crop season  

  - Secondary cover crop season:

    - After the main season \> before the main season  

If no main season is detected for a specific field in a certain reference year also no secondary crop season information is provided.

Table 4: Expert rules with seasonal limits for season delineation based on emergence and harvest input.

| Type season | Zone | Sub-seasonality | Emergence period | Harvest period |
|----|----|----|----|----|
| Main season | 1 | Winter crop | 15/08(year-1)→ 30/04(()) | 01/(06\_{()}) → 15 (;/09\_{(r)}) |
| Main season | 1 | Spring crop | (01/04\_{(}/07\_{(}) | (01/07\_{()}/1)(1/12\_{(}) |
| Main season | 2 | Winter crop | 15 (/08\_{()}/03\_{(}) | (01/04\_{(}/08\_{(}) |
| Main season | 2 | Spring crop | 01/(03\_{()}/07\_{()}) | (01/06\_{(}-)()/01((1)) |
| Secondary season | 1 | Before main season | 01/01 (.()))→ (30/04\_{()})) | 01/01 (.()))→ (30/04\_{()})) |
| Secondary season | 1 | After main season | 1 (.5.)/0 (7\_{()}))→ (30/04\_{(})) | 1 (.5.)/0 (7\_{()}))→ (30/04\_{(})) |
| Secondary season | 2 | Before main season | (01/01\_{()})(/03\_{(y e a r)}) | (01/01\_{()})(/03\_{(y e a r)}) |
| Secondary season | 2 | After main season | 1 (5/06\_{()}/03\_{(+1)}) | 1 (5/06\_{()}/03\_{(+1)}) |

Table 5: Translation of Metzger environmental zones into a zone used with the same season delineation limits.

| Environmental zone (Metzger) | Zone |
|------------------------------|------|
| Alpine north                 | 1    |
| Boreal                       | 1    |
| Nemoral                      | 1    |
| Atlantic north               | 1    |
| Atlantic south               | 1    |
| Continental                  | 1    |
| Atlantic central             | 1    |
| Pannonian                    | 2    |
| Lusitanian                   | 2    |
| Anatolian                    | 2    |
| Mediterranean mountains      | 2    |
| Mediterranean north          | 2    |
| Mediterranean south          | 2    |
| Macaronesia                  | 2    |
| Arctic                       | 1    |

### 3.6.4 Confidence layers

For most of the CP layers confidence information is provided and is based on the uncertainty of the emergence and harvest detection used to delineate the growing season(s). This confidence is calculated based on the uncertainty of satellite observations at the date of emergence or harvest. The CropSAR technology used to fill-in cloud induced gaps of fAPAR provides this uncertainty interval of fAPAR at these dates, as the (10^{}) (q10) and 90th (q90) percentile. The emergence and harvest detection algorithm use the q50 values for their predictions. The emergence or harvest uncertainty in days is based on the upper (q90) and lower (q10) confidence of fAPAR at the event (i.e., emergence or harvest) date and the slope of fAPAR at event date (denoted as slope \\fAPAR\_{event q50}\\) (see equation and Figure 24 below):

\\ fAPAR\_{\mathrm{uncertainty}\\q10} = fAPAR\_{\mathrm{event}\\q50} - fAPAR\_{\mathrm{event}\\q10} \\

\\ fAPAR\_{\mathrm{uncertainty}\\q90} = fAPAR\_{\mathrm{event}\\q50} - fAPAR\_{\mathrm{event}\\q90} \\

\\ days\\uncertainty\_{\mathrm{event}} = \mathrm{abs}\\\left(\frac{fAPAR\_{\mathrm{uncertainty}\\q10}} {slope\\fAPAR\_{\mathrm{event}\\q50}}\right) + \mathrm{abs}\\\left(\frac{fAPAR\_{\mathrm{uncertainty}\\q90}} {slope\\fAPAR\_{\mathrm{event}\\q50}}\right) \\

![Line chart illustrating the temporal evolution of fAPAR (Fraction of Absorbed Photosynthetically Active Radiation) and its associated uncertainty around a specific \`event\` date. The Y-axis represents fAPAR values on a scale from 0 to 1, while the X-axis represents \`Date\`. Three green lines depict fAPAR percentiles over time: a solid line for \`q50\` (50th percentile) and dashed lines for \`q90\` (90th percentile, representing the upper confidence bound) and \`q10\` (10th percentile, representing the lower confidence bound). A vertical dashed red line indicates a specific \`event\` date, such as emergence or harvest. At this event date, the chart highlights two uncertainty measures: \`fAPAR uncertainty q90\` (the vertical difference between the \`q90\` and \`q50\` fAPAR values) and \`fAPAR uncertainty q10\` (the vertical difference between the \`q50\` and \`q10\` fAPAR values). The \`slope fAPAR event q50\` is also indicated, showing the local slope of the \`q50\` curve at the intersection with the \`event\` date. This chart visually represents how the uncertainty interval for fAPAR is derived at key phenological events.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-23efa437cf45423915c018c5bdcd16023b7c710b.png)

Figure 24: Schematic overview on the parameters used to calculate the uncertainty at an event data (i.e., emergence or harvest). Event date is in this example, an emergence.

In rare cases, this approach does not yield reliable results, for example when the slope around emergence or harvest is nearly zero. In these cases, the uncertainty is calculated as follows.

1.  In case of emergence, the uncertainty is the number of days after the event to reach the q50 fAPAR value at emergence by the q10 time series. For harvest, the uncertainty in days can be estimated by the number of days before the harvest event that the q10 time series reach the q50 fAPAR value at harvest.

2.  In case of emergence, the uncertainty in days can be estimated by the number of days before the emergence event that the q90 time series reach the q50 fAPAR value at emergence. For harvest, the uncertainty is the number of days after the event to reach the q50 fAPAR value at harvest by the q90 time series.

3.  The total uncertainty is then determined by summing up the number of days determined in (1) and (2).

Note that, during cloudy periods, the confidence interval will increase as the uncertainty on the fAPAR will also increase.

For most **CP** layers the uncertainties correspond to the uncertainties that are derived from the emergence and harvest date of the specific season. And exception is the **Fallow Land Presence Confidence Layer (CPFLPCL)** which is based on the **Crop Type Confidence Layer (CTYCL)** (which is by default below 35 for fallow fields) and set to:

\\ \mathrm{CPFLPCL} = \frac{CTYCL - 10}{35 - 10} \cdot 100 \\

The lower the **CTYCL** of a fallow field the higher the **CPFLPCL**. In case the **CTYCL** is below 10, the confidence for fallow land presence is confined at 100.

The **Fallow Land Duration Confidence Layer (FLDCL)** can only be calculated when a harvest date is utilized to determine the start or end of a fallow land period. The uncertainty on the harvest date is used to provide information on the fallow land duration confidence. If there is no harvest event on the fallow field, a flag is assigned to the layer. Like for the **FLDCL** layer, the sum of the uncertainties (whenever present) is taken over the five-year period to determine the corresponding uncertainty.

### 3.6.5 Derivation of Main Crops, Bare Soil, Secondary Crops, Fallow Land and Cropping Seasons layers

Based on the delineation of the growing season and the uncertainty of the fAPAR the raster layers for the five layer groups Main Crops, Bare Soil, Secondary Crops, Fallow Land and Cropping Seasons can be derived. This section provides further details on how this has been implemented.

#### 3.6.5.1 Main Crops

For all fields that do have a delineated main season and are not designated as fallow land (see section 3.6.5.4), the following layers based on the main seasonality are derived:

- **Main Crop Harvest (MCH) + Confidence Layer (MCHCL)**

- **Main Crop Emergence (MCE) + Confidence Layer (MCECL)**

- **Main Crop Duration (MCD) + Confidence Layer (MCDCL)**

The first two layers are directly derived from the emergence and harvest information of the delineated season. The confidence is derived from the uncertainty on the emergence or harvest date. The **Main Crop Duration** is the difference in days between the emergence and harvest of the season. The confidence of the crop duration is the average of the confidence on the emergence and harvest date.

#### 3.6.5.2 Bare soil

The **Bare Soil (BS)** layers define the number of days that a field is left bare before and after the main season. If no main season is detected for a specific field or the if the field is designated as fallow land (see section 3.6.5.4) no bare soil information is provided). The following two bare soil layers are produced:

- **Bare Soil Before** main season **(BSB) + Confidence Layer (BSBCL)**

- **Bare Soil After** main season **(BSA) + Confidence Layer (BSACL)**

The duration of the bare soil period following the main season is determined by calculating the number of days between the harvest of the main season and the subsequent emergence date. If there is no emergence date within the same reference year as the product, the bare soil period ends on the last day of the year. If the main season ends after the end of the reference year, no bare soil period after the main season is provided. Conversely, for the bare soil period preceding the main season, the days between the last harvest date prior to the main season and the emergence date are determined. If there is no preceding harvest date in the reference year, the bare soil period begins on the first day of the year. If the main season commences before the reference year, no bare soil period is considered, as it is only calculated for the year in which the layer is produced.

The confidence of the bare soil layer before and after the main season layers is determined by considering the uncertainty in the emergence or harvest dates that define the bare soil period. The average uncertainty in the emergence and/or harvest dates is used to calculate the uncertainty in the bare soil layers. If the bare soil period begins at the start of the reference year and does not align with a harvest event, only the uncertainty in the emergence of the main season start is considered for the calculation of the bare soil period before the main season. Conversely, if the bare soil period ends at the end of the reference year and does not align with an emergence event, only the uncertainty in the harvest event from the main season is considered for the calculation of the uncertainty in the bare soil period after the main season.

#### 3.6.5.3 Secondary Crops

The **Secondary Crop (SC)** season typically occurs during the off-season period. Typical secondary crops are cover crops, which are directly planted after the main season. These crops are often used to enhance soil quality, prevent soil erosion, and provide various other beneficial effects (Fendrich et al., 2023). As a result, in the season delineation labeling (see section 3.6.3), priority was given to secondary seasons that occur after the main growing season. If only one secondary growing season is delineated that starts in winter or early spring within the reference year, that season will be classified as a secondary season. The following layers are available for secondary crops, only if the field has a main season and a secondary season and is not classified as fallow land (see section Fallow land):

- **Secondary Crops Type (SCT)**

- **Secondary Crops Emergence (SCE)**

- **Secondary Crops Duration (SCD) + Confidence Layer (SCDCL)**

The first layer classifies the detected secondary crops into four categories:

- *Short summer*

- *Long summer*

- *Short winter*

- *Long winter*

The categorization of crops is determined by two parameters: the duration of the secondary season and the timing of its emergence. Through cluster analysis of these parameters, secondary crops can be classified into the described four categories. The distinction between short and long growing variants is based on the length of the season: if it is less than 100 days, it is considered short; otherwise, it is classified as long. Additionally, a secondary crop that emerges after the main growing season and before September is labeled as a summer variant, all other cases are classified as winter variants. Typically, a secondary crop season preceding the main season is categorized as a short growing winter variant.

The **SCE** layer can be directly derived from the emergence date of the delineated secondary crop season. The secondary crop season duration is calculated based on the difference in days between the harvest and emergence date. The confidence of the **SCD** is the average of the confidence on the emergence and harvest date.

#### 3.6.5.4 Fallow land

Fallow land is defined as agricultural land where, temporarily, no agricultural activity takes place. The detection of fallow land is performed on a subset of the parcels used for the CP, i.e. only those fields where on average the CTY confidence within the field is below 35, are assessed.

Following layers are generated for fallow land:

➢ **Fallow Land Presence (FLP) + Confidence Layer (FLPCL)**

➢ **Fallow Land Duration (FLD) + Confidence Layer (FLDCL)**

***Fallow land presence classification method***

The workflow applied to determine fallow land presence is shown in Figure 25. After the selection of parcels with an average annual crop type confidence below 35, the number and sequence of detected harvests and emergences in combination with the maximum fAPAR value are evaluated. The evaluation of this parameters is solely done within the reference year. When a harvest event is detected on a field it is evaluated if it occurs before a zone-specific allowed harvest date. This zonation aligns with the two zones used for the season delineation (see section Growing season delineation). The allowed harvest date is set before April 1st for fields located in zone 2 (see Table 5) and before May 1st for fields located in zone 1. If the harvest falls earlier, then this allowed harvest date is likely the harvest of the previous year sown secondary crop. In total 8 cases were defined to which the selected parcels could be classified as fallow land, as described below:

**No emergence no harvest:** There is no harvest nor emergence detected on the field. These are fields where there is clearly no agricultural activity, and they can thus be considered as fallow.

**Harvest:** There is only one harvest event detected on the field and it occurs before the allowed harvest date. Since there is only one harvest that can be associated with a previous year secondary crop and no emergences or harvests are detected after the allowed harvest date the field is considered as fallow.

**Emergence:** There is only one emergence detected on the field, since there is no harvest detected on the field, the emergence can be associated to fallow vegetation emerging on the field.

**Harvest-Emergence:** One harvest date is detected before the allowed harvest date followed by an emergence. The harvest can be associated with a previous year secondary crop and the emergence can be associated to fallow vegetation emerging on the field.

**Emergence-Harvest:** An emergence is followed by a harvest event and the length between these two events is at least 252 days (i.e., 9 months). The emergence can be associated with fallow vegetation emerging on the field, a harvest after 9 months is allowed since fallow vegetation can die back in winter period which can be falsely detected as a harvest.

**Harvest-Harvest:** There are two harvests detected on the field before the allowed harvest date and the maximum fAPAR after the second harvest is below 0.35. In this case the harvest can be associated with a previous year secondary crop followed by a period of bare soil/very sparse fallow vegetation growth, the field is therefore considered as fallow.

**Harvest-Harvest-Emergence:** In the case two harvest events follow each other closely (i.e., they are less than or equal to sixty days apart) and an emergence follows these harvests. In this case the harvests can be associated with a previous year secondary crop followed by a period of fallow vegetation emergence, the field is therefore considered as fallow.

**Emergence-Emergence:** There are two emergences detected on the field but the maximum fAPAR value stays below 0.35. These fields have bare soil/very sparse fallow vegetation growth and are therefore considered as fallow.

![This diagram illustrates the Fallow Land Presence (FLP) classification workflow for agricultural parcels. The process starts with 'CP parcels with mean CTYCL \< 35' (Copernicus parcels with mean Crop Type Confidence Layer confidence below 35). These parcels are then subjected to a 'Filtering' step, which categorises them based on the detected sequence of emergence and harvest events within the reference year. There are eight possible filtered outcomes, each leading to a decision rule under 'Expert rules': 1. \*\*IF\*\* 'no emergence no harvest' \*\*THEN\*\* the field is classified as fallow. 2. \*\*IF\*\* 'Harvest' is detected \*\*AND\*\* the 'harvest occurs before \*allowed harvest date\*' \*\*THEN\*\* the field is classified as fallow. 3. \*\*IF\*\* 'Emergence' is detected \*\*THEN\*\* the field is classified as fallow (no additional expert rule is explicitly shown for this path). 4. \*\*IF\*\* 'Harvest - Emergence' is detected \*\*AND\*\* the 'harvest occurs before \*allowed harvest date\*' \*\*THEN\*\* the field is classified as fallow. 5. \*\*IF\*\* 'Emergence - Harvest' is detected \*\*AND\*\* the 'length between emergence and harvest is minimum 252 days' \*\*THEN\*\* the field is classified as fallow. 6. \*\*IF\*\* 'Harvest-Harvest - Emergence' is detected \*\*AND\*\* the 'number of days between two harvests \<= 60 days' \*\*AND\*\* the 'second harvest occurs before \*allowed harvest date\*' \*\*THEN\*\* the field is classified as fallow. 7. \*\*IF\*\* 'Harvest-Harvest' is detected \*\*AND\*\* the 'second harvest occurs before \*allowed harvest date\*' \*\*AND\*\* the 'max fAPAR after this date \<= 0.35' \*\*THEN\*\* the field is classified as fallow. 8. \*\*IF\*\* 'Emergence-Emergence' is detected \*\*AND\*\* the 'max fAPAR \<= 0.35' \*\*THEN\*\* the field is classified as fallow. The '\*allowed harvest date\*' is defined based on Metzger environmental zones: Zone 1 has an allowed harvest date of May 1st, and Zone 2 has an allowed harvest date of April 1st.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-2e78c63221247c54d2de67164438c015ea8c8e30.jpg)

Figure 25: Workflow for fallow land presence classification. With CP: cropping pattern, CTYCL: confidence value of CTY layer. For the Metzger based environmental zonation see Table 5.

For details on the calculation of the **Fallow Land Presence Confidence Layer (FLPCL)** please refer to section

***Fallow duration***

The **Fallow Land Duration (FLD)** layer is defined as the sum of the yearly **FLD** over the last fiveyears period. The yearly fallow land duration is calculated as follows:

➢ If a harvest date determines the start of the fallow land period, the length starts at that date until the end of the year.

➢ If the harvest defines the end of the fallow land period, the length starts at the first day of the year until the harvest date.

➢ If there is no harvest detected, the length is set to 365 days.

#### 3.6.5.5 Cropping Seasons

The **Cropping Seasons (CL)** layers provide some information on the crop type rotation over a three-year period or within a single reference year and consist of the following two layers:

- **Cropping Seasons Yearly (CSY)**

- **Cropping Season Types over three years (CST)**

The **CSY** layer establishes the number of growing seasons in one year (max. 2) for each selected field used in **CP** layers generation (only annual crops) and excluding fallow land. If both a secondary season and an annual crop type are identified, it will be counted as two growing seasons. If no secondary season falls within the seasonal limits, but it is classified as an annual crop type, it will be counted as one growing season for that year. In all other scenarios, it will be classified as having no cropping season within the reference year.

The **CST** layer is solely based on the **CTY** layer and only considers the annual crop type labels for counting crop rotation. For each reference period of three years, this layer is generated by considering the two years prior to the end of the reference period. As a consequence, the layer is only available from the reference period P2017-2019 onward. During any three-year reference period, the number of unique crop type labels is counted and can range from 1 to 3. Permanent crop labels are not included in the count, and if all three years consist of permanent crops, a value of zero will be assigned. There is one exception to the counting of crop type labels:

If the unclassified arable crop land label appears in any of the three years, it will be excluded from the count to avoid the risk of double counting the same crop type. If the entire period is classified as unclassified arable crop land, the count will be set to one.

#### 3.6.5.6 Encountered issues and known limitations

A limitation of the **Fallow Land (FL)** layers is that only a subset of fields is considered for fallow land evaluation. Therefore, fallow fields that are not covered by the annual crop type masked parcel delineation product will not be examined and therefore not detected. Furthermore, reference data on fallow land is scarce and often a harmonized definition of fallow land is absent, which makes it hard to evaluate the product. Therefore, it was decided to work with some thematic rules that fit with the expected behavior of fallow land.

The expert rules are defined to determine crop seasonality (section [Section 3.6.3.3](#sec-Season-delineation)) for most cases. However, there are still some specific cases that may not be addressed by the seasonal limits defined by the set of expert rules. In such cases, additional checks are needed to determine if the detected seasonality should be included in the **CP** layers. Some of these cases are discussed below.

In the case where a season does not correspond with any main season in the reference year, it is verified if there is still a season onset after the anticipated period of emergence for spring crops and a harvest event before the conclusion of the reference year. By applying this rule, the seasonality of vegetables that are planted late in the season are included. However, most of these cases involve fallow land with minimal seasonality and are categorized under fallow land layers (see section [Section 3.6.5.4](#sec-Fallow-land)).

In the case where multiple spring crops are cultivated on a field, the first detected season is considered as the main season and the second one as the secondary season. In the case two secondary crop seasons occur after the main season, the first one is selected as secondary season. Other exceptions can occur but are not described due to their rare occurrence.

Overall, the applied expert rules cover the most common seasonalities of annual crops, but some limitations exist. For example, in case of too short growing season lengths, some vegetables could be excluded from **CP** layers generation. However, shortening the allowed seasonal length would include much more expectations in the **CP** layers, leading to a less reliable product. Moreover, that the shorter the season the more errors could occur in the emergence and harvest detection, resulting in errors in the seasonal delineation.

In the case of double cropping seasons, there are instances where the seasonal labelling conflicts with the crop type label in the **CTY** layer. For instance, if a winter cereal is followed by maize, the **CTY** label might classify it as maize, while the season delineation designates the winter cereal season as the main season. This situation is more likely to occur in the southern regions of Europe where the climate allows for double cropping. In these areas, it is also possible for the harvest of winter cereals to coincide with the secondary crop harvest. In such cases, it becomes challenging to differentiate between winter cereals and secondary crops, leading to the possibility of the secondary crop being considered the main season. However, if a spring main crop signal is detected subsequently, it will be recognized as the main season.

In addition to the challenges associated with labeling seasons, issues may arise from the emergence and harvest detection processes themselves. For some specific crops like sunflowers, it is observed that often the seasonal signal is too subtle (Figure 26) to allow any harvest detection. This limitation has been particularly noted during the growing season of 2019 in southern Spain. No training data on this specific crop in this area is available to be able to improve the harvest detection algorithm.

![Line chart illustrating the temporal evolution of fAPAR (Fraction of Absorbed Photosynthetically Active Radiation) over a two-year period, from July 2018 to July 2020. The Y-axis represents fAPAR values ranging from 0.0 to 0.8. The X-axis represents time, with major ticks indicating quarterly intervals from 2018-07 to 2020-07. The chart displays two data series: 1. \*\*CropSAR_q50\*\* (green line): Represents the 50th percentile of fAPAR derived from CropSAR data. 2. \*\*modelled_emergence\*\* (thin black line): A modelled emergence signal, which closely aligns with and is mostly obscured by the CropSAR_q50 line, particularly during periods of low fAPAR. The \`CropSAR_q50\` line shows two distinct annual growth cycles. From July 2018 to early 2019, fAPAR values remain low, fluctuating between approximately 0.1 and 0.2. A moderate increase occurs in spring/summer 2019, peaking around 0.25 in July 2019, followed by a decline to low levels in late 2019 (0.1–0.15). A sharp increase in fAPAR begins in early 2020, reaching a peak of approximately 0.85 in May-June 2020, followed by a rapid decrease towards July 2020. Two vertical black lines are present: one around mid-June 2019 and another around mid-December 2019. These lines delineate specific time periods, possibly indicating seasonal limits or reference periods for cropping seasons. The values for \`modelled_emergence\` remain very low, often at or near the baseline of \`CropSAR_q50\` during non-peak growth periods.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img-a014c53b4082d3774a361ab4665f133ec588819a.png)

Figure 26: Example of CropSAR fAPAR signal for a sunflower field in southern Spain in 2019. The black lines show the detected emergence dates within the time series.

Additionally, in certain scenarios, consecutive emergence events without a corresponding harvest event in between, or vice versa occur. To address these situations, additional rules based on a bare soil indicator are developed to be able to select the correct emergence or harvest dates for linking seasons. However, some cases may still lead to the selection of incorrect emergence or harvest dates, resulting in outliers in seasonal length (either too short or excessively long) or even seasons that fall outside the allowed season boundaries. This issue is particularly prevalent when a secondary crop is planted immediately after the main crops harvest, or when the delineated parcel is a multi-cropped field, leading to emergence/harvest signals that reflect this multi-cropping behavior. Furthermore, in northern regions of Europe where a permanent snow cover occurs before main crops are harvested, the harvest may not be accurately detected, in these cases it impossible to identify any season even when crop cultivation does occur.

Finally, some limitations in the **CP** layers arise from the filtering of annual crops based on the **HRL CTY** classification. Specifically, if a field is delineated but not classified as annual cropland in the **CTY** layer, no **CP** information is generated for that field—even in cases where annual cropping activity may actually be present. Conversely, false positives in the **CTY** annual crop classification can introduce artefacts into the **CP** layers by triggering extraction where no actual annual crop exists.

On the other hand, some annual cropland pixels in the **CTY** layer lack corresponding field delineations, resulting in missing **CP** outputs. At the Pan-European scale, approximately 10% of pixels classified as annual crops do not intersect with any delineated field and therefore cannot be assigned **CP** information. This loss is primarily due to two factors:

- 5% is due to pixel-level misalignment at field boundaries, regions with more small and elongated fields will have more data loss.

- The remaining 5% stems from larger spatial mismatches between the extent of **CTY** classified annual crop areas and the delineated field geometries. These discrepancies are most pronounced for crop types with lower classification accuracy—such as fresh vegetables, other cereals, and unclassified arable crops.

In contrast, for other (and most common) annual crop classes, around 95% of pixels are successfully aligned with the delineated field boundaries, ensuring reliable **CP** generation for these key crop types. For these crop types, the pixel misalignment at the field border is the main reason for this 5% loss of **CP** output.

# 4 List of abbreviations

| Abbreviation | Name |
|----|----|
| ADs | Applicable Documents |
| AOI | Area of Interest |
| BCD | Broadleaved Cover Density |
| BVL | Base Vegetation Layer |
| CAP | Common Agricultural Policy of the European Union |
| CCD | Coniferous Cover Density |
| CDD | Crop Diversity and Diversification |
| CL | Confidence Layer |
| CLC | CORINE Land Cover |
| CLC+ | CORINE Land Cover + |
| CLMS | Copernicus Land Monitoring Service |
| CORINE | Coordination of information on the environment |
| CROP | Cropland Products |
| CT | Crop Type Layer |
| CTY | Crop Types |
| CTYCL | Crop Types Confidence Layer |
| DEM | Digital Elevation Model |
| DIAS | Copernicus Data and Information Access Services |
| DLT | Dominant Leaf Type |
| DLTC | Dominant Leaf Type Change |
| DLTCL | Dominant Leaf Type Change |
| DTW | Dynamic Time Warp |
| EEA | European Environment Agency |
| EEA38 | The 32 member and 6 cooperating countries of the EEA |
| EO | Earth Observation |
| EPSG | European Petroleum Survey Group |
| ESYRCE | Encuesta sobre Superficies y Rendimientos Cultivos |
| ETC | European Topic Centre |
| EU | European Union |
| EU27 | The 27 member states of the EU |
| EVI | Enhanced Vegetation Index |
| FADSL | Forest Additional Support Layer |
| fAPAR | fraction of Absorbed Photosynthetic Active Radiation |
| FL | Fallow Land |
| Fmask | Function of mask |
| FOR | Forest Products |
| FWC | Framework Contract |
| F-Score | Harmonic mean of the Producer’s and the User’s Accuracies |
| FTY | Forest Type |
| GDAL | Geospatial Data Abstraction Library |
| GRA | Grassland Status Layer |
| GRAC | Grassland Change Layer |
| GRACL | Grassland Confidence Layer |
| GRACCL | Grassland Change Confidence Layer |
| GRAM | Grassland Mowing Events |
| GRAMCL | Grassland Mowing Confidence Layer |
| GRAMD | Grassland Mowing Dates |
| GRAME | Grassland Mowing Events |
| HBS | Harvest and Bare Soil |
| HER | Herbaceous Cover Layer |
| HR | High Resolution |
| HRL / HRLs | High Resolution Layer / High Resolution Layers |
| HRL VLCC | High Resolution Layer – Vegetated Land Cover Characteristics |
| ID | Identification Number |
| JRC | Joint Research Centre |
| KOM | Kick-Off Meeting |
| L2A | Level 2A |
| LAEA | Lambert Azimuthal Equal Area projection |
| LAI | Leaf Area Index |
| LC | Land Cover |
| LiDAR | Light Detection and ranging |
| LPIS | Land-Parcel Identification System |
| LU | Land Use |
| LUCAS | Land Use/ Cover Area frame Survey |
| LULUCF | Land Use, Land Use Change and Forestry |
| MMU | Minimum Mapping Unit |
| NDVI | Normalised Difference Vegetation Index |
| NBR2 | Normalized Burnt Ratio 2 |
| OA | Overall Accuracy |
| OpenEO | API to connect different programming languages to EO cloud back-ends |
| PA | Producer Accuracy |
| PLOUGH | Ploughing Indicator |
| PPT | PowerPoint Presentation |
| PU | Production Unit |
| Rr | Recognition Rate |
| SAR | Synthetic Aperture Radar |
| SC | Specific Contract |
| SCL | Scene Classification Layer |
| Sen2Cor | Processor for Sentinel-2 Level 2A product generation |
| SIGPAC | Sistema de Información Geográfica de Parcelas Agrícolas |
| TBD | To Be Discussed / Defined |
| TCD | Tree Cover Density |
| TCCM | Tree Cover Change Mask |
| TCDCL | Tree Cover Density Confidence Layer |
| TCPC | Tree Cover Presence Change |
| TCPCCL | Tree Cover Presence Change Confidence Layer |
| TempCNN | Temporal Convolutional Neural Network |
| UA | User’s Accuracies |
| USDA | United States Department of Agriculture |
| UTM | Universal Transverse Mercator |
| VHR | Very High Resolution |
| VPP PPI | Vegetation Phenology and Productivity parameters – Plant Phenology Index |
| XML | Extensible Markup Language |
| WEkEO | Copernicus DIAS reference service for environmental data, virtual environments for data processing |

# 5 References

- Alcaras, E., Costantino, D., Guastaferro, F., Parente, C. & Pepe, M. Normalized Burn Ratio Plus (NBR+): A New Index for Sentinel-2 Imagery. remote sensing, vol. 14, no. 7, pp. 1-19, 2022.

- Aybar, C., Ysuhuaylas, L., Loja, J., Gonzales, K., Herrera, F., Bautista, L., … & GómezChova, L. (2022). CloudSEN12, a global dataset for semantic understanding of cloud and cloud shadow in Sentinel-2. Scientific Data, 9(1), 782.

- Coltuc, D., Bolon, P., & Chassery, J. M. (2006). Exact histogram specification. IEEE Transactions on Image Processing, 15(5), 1143-1152.

- “CropSAR service,” VITO, \[Online\]. Available: https://cropsar.vito.be/api/docs/.\[Accessed 24 07 2024\].

- De Vroey, M., Radoux, J., & Defourny, P. (2021). Grassland mowing detection using sentinel-1 time series: potential and limitations. Remote Sensing, 13(3), 348.

- Dorogush, A. V., Ershov, V., & Gulin, A. (2018). CatBoost: gradient boosting with categorical features support. arXiv preprint arXiv:1810.11363.

- EEA (2023). EEA38 10m Boundary Layer https://sdi.eea.europa.eu/webdav/datastore/public/eea_r_3035_10_m_copernicus-250m-buffer_p_2012-2018_v02_r00/GTIFF/Boundary_EEA38_03035_010m_v02.tif

- Eurostat. (2018). LUCAS Survey 2018. \[Data set\]. https://ec.europa.eu/eurostat/web/lucas/data/primary-data.

- FAO. (2012). Terms and Definitions: FRA 2015. Forest Resources Assessment Working Paper 180. Food and Agriculture Organization of the United Nations, Rome.

- Fendrich, A. N., Matthews, F., Van Eynde, E., Carozzi, M., Li, Z., d’Andrimont, R., Lugato, E., Martin, P., Ciais, P., & Panagos, P. (2023). From regional to parcel scale: A highresolution map of cover crops across Europe combining satellite data with statistical surveys. In Science of The Total Environment (Vol. 873, p. 162300). Elsevier BV. https://doi.org/10.1016/j.scitotenv.2023.162300

- Gao, F., Anderson, M., Johnson, D., Seffrin, R., Wardlow, B., Suyker, A., Dia, C. & Browning, D. Towards Routine Mapping of Crop Emergence within the Season Using the Harmonized Landsat and Sentinel-2 Dataset. Remote Sensing, vol. 13, no. 24:5074, 2021.

- Gao, F., Anderson, M., Zhang, X., Yang, Z., Alfieri, J., Kustas, W., Mueller, R., Johnson, D. & Prueger, J. Toward mapping crop progress at field scales through fusion of Landsat and MODIS imagery. Remote Sensing of Environment, vol. 188, pp. 9-25, 2017.

- Garioud, A., Giordano, S., Valero, S., & Mallet, C. (2019, August). Challenges in grassland mowing event detection with multimodal sentinel images. In 2019 10th International Workshop on the Analysis of Multitemporal Remote Sensing Images (MultiTemp) (pp. 1-4). IEEE.

- Griffiths, P., Nendel, C., Pickert, J., & Hostert, P. (2020). Towards national-scale characterization of grassland use intensity from integrated Sentinel-2 and Landsat time series. Remote Sensing of Environment, 238, 111124.

- Hardy, T., Kooistra, L., Domingues Franceschini, M., Richter, S., Vonk, E., van den Eertwegh, G., & Van Deijl, D. (2021). Sen2Grass: A cloud-based solution to generate field-specific grassland information derived from Sentinel-2 imagery. AgriEngineering, 3(1), 118-137.

- Khabbazan, S., Vermunt, P., Steele-Dunne, S., Arntz, L., Marinetti, C., Van der Valk, D., Iannini, L., Molijn, R., Westerdijk, K. & Van der Sande, C. Crop Monitoring Using Sentinel-1 Data: A Case Study from The Netherlands. Remote Sensing, vol. 11, no. 16:1887, 2019.

- Kolecka, N., Ginzler, C., Pazur, R., Price, B., & Verburg, P. H. (2018). Regional scale mapping of grassland mowing frequency with sentinel-2 time series. Remote Sensing, 10(8), 1221.

- Malinin, A., Prokhorenkova, L., & Ustimenko, A. (2020). Uncertainty in gradient boosting via ensembles. arXiv preprint arXiv:2006.10562.

- Meroni, M., D’andrimont, R., Vrieling, A., Fasbender, D., Lemoine, G., Rembold, F., Seguini, L. & Verhegghen, A. Comparing land surface phenology of major European crops as derived from SAR and multispectral data of Sentinel-1 and -2. Remote Sensing of Environment, vol. 253, no. 112232, 2021.

- Metzger M.J., Bunce R.G.H., Jongman R.H.G., Sayre R., Trabucco A., Zomer R., Sykes M. (2013). A high-resolution bioclimate map of the world: a unifying framework for global biodiversity research and monitoring. Glob. Ecol. Biogeogr., 22 (5), 630-638.

- Metzger, M. J. (2018). The Environmental Stratification of Europe \[Dataset\]. University of Edinburgh. https://doi.org/10.7488/DS/2356.

- Northcutt C., Athalye A., Mueller J. (2021). Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks. Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks, 1.

- Pelletier, C., Webb, G. I., & Petitjean, F. (2019). Temporal convolutional neural network for the classification of satellite image time series. Remote Sensing, 11(5), 523.

- Piccard, I., Gobin, A., Gilliams, S., Tits, L. & Decloedt, J. WatchITgrow. Precision Agriculture: Modelling, Springer, 2023, pp. 229-238.

- Reinermann, S., Asam, S., & Kuenzer, C. (2020). Remote sensing of grassland production and management—A review. Remote Sensing, 12(12), 1949.

- Reinermann, S., Gessner, U., Asam, S., Ullmann, T., Schucknecht, A., & Kuenzer, C. (2022). Detection of Grassland Mowing Events for Germany by Combining Sentinel-1 and Sentinel-2 Time Series. Remote Sensing, 14(7), 1647.

- Salvador, S., & Chan, P. (2007). Toward accurate dynamic time warping in linear time and space. Intelligent Data Analysis, 11(5), 561-580.

- Schindler, K. (2012). An overview and comparison of smooth labeling methods for landcover classification. IEEE transactions on geoscience and remote sensing, 50(11), 4534-4545.

- Siegmund, R., Redl, S., Wagner, M., & Hartmann, S. (2019, October). Grassland monitoring based on Sentinel-1. In Remote Sensing for Agriculture, Ecosystems, and Hydrology XXI (Vol. 11149, p. 1114902). SPIE.

- Stendardi, L., Karlsen, S. R., Niedrist, G., Gerdol, R., Zebisch, M., Rossi, M., & Notarnicola, C. (2019). Exploiting time series of Sentinel-1 and Sentinel-2 imagery to detect meadow phenology in mountain regions. Remote Sensing, 11(5), 542.

- Tamm, T., Zalite, K., Voormansik, K., & Talgre, L. (2016). Relating Sentinel-1 interferometric coherence to mowing events on grasslands. Remote Sensing, 8(10), 802.

- Van Tricht, K, Gobin, A., Gilliams, S. & Piccard, I. Synergistic Use of Radar Sentinel-1 and Optical Sentinel-2 Imagery for Crop Mapping: A Case Study for Belgium. Remote Sensing, vol. 10, no. 10:1642, 2018.

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., … & Polosukhin, I. (2017). Attention is all you need. Advances in neural information processing systems, 30.

- Zerveas, G., Jayaraman, S., Patel, D., Bhamidipaty, A., & Eickhoff, C. (2021, August). A transformer-based framework for multivariate time series representation learning. In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining (pp. 2114-2124).

# 6 Annex I - Aggregation rules for 20m layers TCPC, DLTC and GRAC

![This diagram illustrates the aggregation rules for two Copernicus Land Monitoring Service (CLMS) products: Tree Cover Presence Change (TCPC) and Dominant Leaf Type Change (DLTC), converting 10m resolution input pixels to 20m resolution output pixels. The aggregation process takes four 10m input pixels and assigns a single 20m output pixel value based on predefined rules, especially for 50/50 cases where there is an equal number of input pixel types. \*\*Part 1: Aggregation rules for TCPC from 10m to 20m\*\* The TCPC product legend defines:](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img1.png)

![This diagram illustrates the pixel aggregation rules for Grassland Related Change (GRAC) when downscaling from a 10-meter resolution (DLTC 10m) to a 20-meter resolution (DLTC 20m). Each 20m output pixel is derived from a 2x2 block of four 10m input pixels. The diagram provides specific examples of how different combinations of input codes at 10m result in an aggregated code at 20m, indicating a hierarchical or priority-based aggregation logic. Overriding Rules: \* Loss of coniferous](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img2.png)

![This diagram illustrates the Grassland Area Change (GRAC) detection workflow, outlining the classification logic for grassland gain and loss between two reference years, GRA 18 (2018) and GRA 21 (2021). The process consists of four main steps: 1. An aggregation to a 20m resolution is performed on the corresponding Grassland (GRA) status layers. In cases where grassland occurrence is 50/50 within a 20m cell, it will be classified as grassland. \* \*\*Visual Example 1 (GRAC: No GRA):\*\* If the 10m grid for GRA 18 shows one grassland cell (green) and GRA 21 shows zero grassland cells, the aggregated 20m cells for both GRA 18 and GRA 21 are classified as non-grassland (white). The resulting GRAC output is 'No GRA', assigned value '0'. \* \*\*Visual Example 2 (GRAC: All GRA):\*\* If the 10m grid for GRA 18 shows two grassland cells and GRA 21 also shows two grassland cells, the aggregated 20m cells for both GRA 18 and GRA 21 are classified as grassland (dark green). The resulting GRAC output is 'All GRA', assigned value '10'. 2. Change detection is performed based on these aggregated 20m status layers. 3. On the detected changes, a Minimum Mapping Unit (MMU) of 1 hectare (ha) is applied, but only to change classes. 4. For non-change classes, the Grassland (GRA) 2018 layer determines which non-change class is assigned. \* \*\*Visual Example 3 (GRAC: loss):\*\* If the 10m grid for GRA 18 shows two grassland cells and GRA 21 shows one grassland cell, the aggregated 20m cell for GRA 18 is classified as grassland (dark green), and for GRA 21 as non-grassland (white). The resulting GRAC output is 'loss', assigned value '2'. \* \*\*Visual Example 4 (GRAC: gain):\*\* If the 10m grid for GRA 18 shows one grassland cell and GRA 21 shows two grassland cells, the aggregated 20m cell for GRA 18 is classified as non-grassland (white), and for GRA 21 as grassland (dark green). The resulting GRAC output is 'gain', assigned value '1'. The legend defines the GRAC output values and their associated colours: '0' for 'All non-grassland' (white), '1' for 'GRA gain' (light blue), '2' for 'GRA loss' (red), '10' for 'All grassland' (dark green), and '255' for 'Outside area' (black).](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img3.png)

# 7 Annex II TCPC MMU filtering

The Tree Cover Presence Change is defined with a Minimum Mapping Unit (MMU) of 1 ha. The implementation of an MMU requires several choices and steps which are documented here. The detected gains and losses are initially aggregated to 20m according to the rules defined in Annex II. Holes smaller than the MMU and completely surrounded by either loss or gain are filled according to majority of their surroundings, in situation where no majority can be found the tree cover loss class dominates. Change patches smaller than the MMU are removed in such a way that tree cover gains are recoded as class 10 (unchanged areas with tree cover) and tree cover losses are recoded as class 0 (unchanged areas without tree cover).

![This process diagram illustrates the four-step sequence for TCPC (change detection product/method) Minimum Mapping Unit (MMU) filtering and aggregation of land cover change patches. 1. \*\*Initially detected change patch at 10m spatial resolution:\*\* The process begins with initially detected change patches on a 10m spatial resolution grid. Red cells represent 'loss', and green cells represent 'gain'. 2. \*\*Overlay of 20m grid:\*\* A coarser 20m grid is overlaid onto the existing 10m spatial resolution grid, effectively grouping 2x2 blocks of 10m cells into single 20m cells. 3. \*\*Assignment of class codes at 20m according to defined aggregation rules:\*\* Class codes (red for loss, green for gain) are assigned to the 20m grid cells based on defined aggregation rules. This step shows that some internal areas within the larger red and green patches are not classified, appearing as white 'holes'. 4. \*\*Holes in loss or gain patches are filled, respectively, if below the MMU:\*\* In the final step, any unclassified areas or 'holes' (white cells) within the loss (red) or gain (green) patches are filled with the surrounding majority class, provided their spatial extent is below the defined Minimum Mapping Unit (MMU).](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img4.png)

![This conceptual diagram illustrates the effect of applying a Minimum Mapping Unit (MMU) rule in spatial data processing, specifically for removing small 'change patches.' The top panel displays an initial grid composed of cells. It shows a large contiguous red patch, a large contiguous green patch, and a smaller green patch of 2x2 cells (4 grid cells) located between the larger red and green areas. White cells represent unclassified or background areas. The bottom panel depicts the grid after applying the rule described as '5) Change patches smaller than the MMU are removed'. In this resulting state, the small green patch (4 cells) has been removed, and its area is now filled by the adjacent large red patch, indicating it was considered a 'change patch' and was smaller than the defined Minimum Mapping Unit. The larger red and green patches remain unchanged. This process exemplifies a spatial generalization technique to simplify land cover / land use (LCLU) classifications by eliminating features below a specified size threshold.](High_Resolution_Layer_Vegetated_Land_Cover_Characteristics_ATBD_v2-media/img5.png)

# 8 Change Log

| Date       | Version | Summary         |
|------------|---------|-----------------|
| 2025-12-02 | 2.1.0   | Initial release |

Back to top

## Footnotes

## Reuse

EUPL (\>= 1.2)

[^1]: https://gdal.org/en/stable/api/gdal_alg.html#\_CPPv415GDALSieveFilter15GDALRasterBandH15GDALRasterBandH15GDALRasterBandHiiPPc16GDALProgressFuncPv

[^2]: https://gdal.org/en/stable/api/gdal_alg.html#\_CPPv414GDALFillNodata15GDALRasterBandH15GDALRasterBandHdiiPPc16GDALProgressFuncPv

[^3]: https://land.copernicus.eu/en/products/corine-land-cover/clc2018

[^4]: https://land.copernicus.eu/en/products/high-resolution-layer-grasslands/grassland-2018-raster-10-m-100-m-europe-yearly

[^5]: https://land.copernicus.eu/en/products/high-resolution-layer-grasslands/grassland-2018-raster-10-m-100-m-europe-yearly

[^6]: **https://land.copernicus.eu/en/products/vegetation**

[^7]: **https://land.copernicus.eu/en/products/vegetation**

[^8]: **https://land.copernicus.eu/en/products/vegetation**

[^9]: https://land.copernicus.eu/en/technical-library/hrl-grassland-2018-product-user-manual

[^10]: https://gdal.org/en/stable/api/gdal_alg.html#\_CPPv415GDALSieveFilter15GDALRasterBandH15GDALRasterBandH15GDALRasterBandHiiPPc16GDALProgressFuncPv

[^11]: https://openeo.org/
