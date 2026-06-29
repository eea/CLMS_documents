# Product development support - HRL vegetated

2025-04-15

- [<span class="toc-section-number">1</span> Background](#background)
- [<span class="toc-section-number">2</span> Assignment of this task and
  specific actions](#assignment-of-this-task-and-specific-actions)
- [<span class="toc-section-number">3</span> Key
  Deliverables](#key-deliverables)
- [<span class="toc-section-number">4</span> Assessment of similarities
  and differences](#assessment-of-similarities-and-differences)
  - [<span class="toc-section-number">4.1</span> Overview of the
    selected initiatives mapping
    grassland](#overview-of-the-selected-initiatives-mapping-grassland)
  - [<span class="toc-section-number">4.2</span> A closer look into
    selected initiatives - background, data, products,
    methods.](#a-closer-look-into-selected-initiatives---background-data-products-methods)
    - [<span class="toc-section-number">4.2.1</span> Global Pasture
      Watch ](#global-pasture-watch-123)
    - [<span class="toc-section-number">4.2.2</span> SUPER-G
      Project](#super-g-project45)
    - [<span class="toc-section-number">4.2.3</span> GRASS
      SIGNAL](#grass-signal6)
    - [<span class="toc-section-number">4.2.4</span> ESDAC Soil Biomass
      Productivity (Grassland
      Layer)](#esdac-soil-biomass-productivity-grassland-layer7)
  - [<span class="toc-section-number">4.3</span> Comparison of CLMS HRL
    VLCC Grassland with
    EUGW](#comparison-of-clms-hrl-vlcc-grassland-with-eugw)
    - [<span class="toc-section-number">4.3.1</span> Initial look into
      both datasets](#initial-look-into-both-datasets)
    - [<span class="toc-section-number">4.3.2</span> Detailed overview
      of EUGW portfolio](#detailed-overview-of-eugw-portfolio)
    - [<span class="toc-section-number">4.3.3</span> Similarities and
      differences](#similarities-and-differences)
    - [<span class="toc-section-number">4.3.4</span> Potential and
      recommendations](#potential-and-recommendations)
- [<span class="toc-section-number">5</span> Collection of user
  requirements and literature review of additional forest
  Types](#collection-of-user-requirements-and-literature-review-of-additional-forest-types)
  - [<span class="toc-section-number">5.1</span> Literature
    review](#literature-review)
    - [<span class="toc-section-number">5.1.1</span> EEA Classification
      on European Forest
      type](#eea-classification-on-european-forest-type)
    - [<span class="toc-section-number">5.1.2</span> Eu ecosystem
      typology](#eu-ecosystem-typology)
    - [<span class="toc-section-number">5.1.3</span> Forest category for
      LULUCF reporting](#forest-category-for-lulucf-reporting)
    - [<span class="toc-section-number">5.1.4</span> Refining ona
      proposal on Forest Type extent
      nomenclature](#refining-ona-proposal-on-forest-type-extent-nomenclature)
    - [<span class="toc-section-number">5.1.5</span> First set of
      recommendations](#first-set-of-recommendations)
- [<span class="toc-section-number">6</span> Assessment of Timeseries
  Consistency of Forest
  Layers](#assessment-of-timeseries-consistency-of-forest-layers)
  - [<span class="toc-section-number">6.1</span> Basic concepts and
    terminology used for tree cover / forest related CLMS
    products](#basic-concepts-and-terminology-used-for-tree-cover--forest-related-clms-products)
  - [<span class="toc-section-number">6.2</span> Overview and evolution
    of main HRL Forest
    products](#overview-and-evolution-of-main-hrl-forest-products)
  - [<span class="toc-section-number">6.3</span> Assessment of the
    stability of HRL Forest
    products](#assessment-of-the-stability-of-hrl-forest-products)
    - [<span class="toc-section-number">6.3.1</span> Evolution of the
      specification of individual
      products](#evolution-of-the-specification-of-individual-products)
    - [<span class="toc-section-number">6.3.2</span> Changes in the
      total mapped area](#changes-in-the-total-mapped-area)
    - [<span class="toc-section-number">6.3.3</span> Evolution of total
      tree cover estimated for EEA38
      area](#evolution-of-total-tree-cover-estimated-for-eea38-area)
    - [<span class="toc-section-number">6.3.4</span> Evolution of the
      calibration of TCD
      values](#evolution-of-the-calibration-of-tcd-values)
    - [<span class="toc-section-number">6.3.5</span> Overview of the
      stability of leaf type classification in DLT status
      layers](#overview-of-the-stability-of-leaf-type-classification-in-dlt-status-layers)
    - [<span class="toc-section-number">6.3.6</span> Classification
      differences HRL DLT2018 vs VLCC DLT2018
      layers](#classification-differences-hrl-dlt2018-vs-vlcc-dlt2018-layers)
    - [<span class="toc-section-number">6.3.7</span> Classification
      differences VLCC DLT2018 vs CLCplus Backbone
      2018](#classification-differences-vlcc-dlt2018-vs-clcplus-backbone-2018)
    - [<span class="toc-section-number">6.3.8</span> Classification
      differences HRL DLT2012 vs HRL DLT2015
      layers](#classification-differences-hrl-dlt2012-vs-hrl-dlt2015-layers)
    - [<span class="toc-section-number">6.3.9</span> Classification
      differences HRL DLT2015 vs HRL DLT2018
      layers](#classification-differences-hrl-dlt2015-vs-hrl-dlt2018-layers)
    - [<span class="toc-section-number">6.3.10</span> Classification
      differences VLCC DLT2018 vs VLCC DLT2021
      layers](#classification-differences-vlcc-dlt2018-vs-vlcc-dlt2021-layers)
  - [<span class="toc-section-number">6.4</span> Discussion of the
    mapping concepts applied for creating HRL Forest
    layers](#discussion-of-the-mapping-concepts-applied-for-creating-hrl-forest-layers)
    - [<span class="toc-section-number">6.4.1</span> Effect of 1ha MMU
      applied to VLCC Forest change
      data](#effect-of-1ha-mmu-applied-to-vlcc-forest-change-data)
    - [<span class="toc-section-number">6.4.2</span> Effects of the
      aggregation of change data to 20m raster
      resolution](#effects-of-the-aggregation-of-change-data-to-20m-raster-resolution)
    - [<span class="toc-section-number">6.4.3</span> Chance of achieving
      full consistency in HRL Forest
      time-series](#chance-of-achieving-full-consistency-in-hrl-forest-time-series)
  - [<span class="toc-section-number">6.5</span> Conclusions &
    recommendations](#conclusions--recommendations)
- [<span class="toc-section-number">7</span> Summary &
  Conclusions](#summary--conclusions)
- [<span class="toc-section-number">8</span> References](#references)

# Background

The new High-Resolution Layer (HRL) production on vegetated land cover
has been ongoing since 2022. HRL Vegetated is a complex product
comprising HRL Crop Types, HRL Grasslands, and HRL Forest, each with
several sub-layers. In preparation for the continuation of HRL Vegetated
Land Cover Characteristics (VLCC) for the reference year 2025 onwards,
the European Environment Agency (EEA) foresees the potential need for
product definitions and methodologies updates. This task is aimed at
supporting the EEA in the evolution of the HRL VLCC products.

# Assignment of this task and specific actions

- **ST1: Assessment of Similarities and Differences**

  This subtask aims to explore various grassland mapping initiatives in
  Europe and compare them with HRL VLCC products. The goal is to
  identify similarities, differences, and potential improvements for
  future product development.

- **ST2: Collection of User Requirements and Literature Review of
  Additional Forest Types**

  This subtask will support the EEA in gathering user requirements for
  extending forest-type classifications within the VLCC Forest dataset
  and conducting a literature review on current classification
  methodologies.

- **ST3: Assessment of Timeseries Consistency of Forest Layers**

  This subtask focuses on assessing the stability and consistency of
  time series for HRL Forest layers to support indicator development.

# Key Deliverables

Overview of grassland datasets and their comparison, proposed forest
type classifications based on user requirements and literature review,
time series assessment summary and recommendations for improving
consistency.

# Assessment of similarities and differences

## Overview of the selected initiatives mapping grassland

The monitoring and mapping of grasslands play a crucial role in
sustainable land management, biodiversity conservation, and agricultural
policy implementation across Europe and beyond. Grasslands represent a
significant land cover type that supports ecosystem services, carbon
sequestration, and habitat provision for numerous species (Bengtsson et
al., 2019; Peeters, 2009). In recent years, advancements in remote
sensing technology and the availability of high-resolution satellite
imagery have enabled more detailed and consistent efforts in grassland
monitoring.

European institutions and global organisations have invested in various
projects and initiatives to monitor grasslands at different spatial and
temporal scales. These initiatives aim to address challenges such as
land-use change, grassland degradation, and the need for effective
management practices. Grassland data sources, like the High-Resolution
Layer Vegetated Land Cover Characteristics (HRL VLCC) Grassland and the
EU Grassland Watch (EUGW) project, exemplify how remote sensing and
data-driven approaches are being employed to provide accurate and
up-to-date information on grassland distribution, productivity, and
management.

This chapter explores the various grassland mapping initiatives and data
sources currently being utilised for grassland monitoring and assessment
across Europe and globally. The goal is to offer an in-depth
understanding of the available datasets, their applications, and the
grassland classification, and management methodologies. Special focus is
placed on the EU Grassland Watch (EUGW) project and its comparison with
the HRL VLCC Grassland dataset, as these two initiatives are important
to understanding the current state of grassland mapping at the European
level. Focusing on qualitative comparison highlights differences in
coverage, accuracy, thematic layers, and practical applications.

In addition to these primary datasets, several other grassland
monitoring initiatives contribute to a broader understanding of
grassland distribution and related characteristics such as productivity
or management practices. These initiatives utilise different
methodologies, ranging from in-situ data collection and field surveys to
remote sensing-based or even including predictive modelling, providing
valuable datasets for land management, biodiversity conservation, and
agricultural practices. Beyond data production, these projects also
offer valuable policy insights and research recommendations. Overall,
six different initiatives, products, and projects were identified, each
offering a unique perspective on grassland mapping and monitoring (Table
1).

- **EU Grassland Watch (EUGW)** provides high-resolution monitoring of
  grassland management, productivity, and biodiversity across Natura
  2000 sites in Europe. The dataset offers yearly updates dating back to
  1994, leveraging both Sentinel and pre-Sentinel satellite data to
  track grassland dynamics. It focuses on management events,
  productivity trends, habitat mapping and related biodiversity as well
  as land cover-based indicators.
- **LUCAS Grassland Module** offers an extensive in-situ dataset based
  on systematic field surveys conducted across thousands of locations in
  Europe. The module provides detailed information on grassland
  management, soil types, and species composition, making it an
  essential validation source for remote sensing-based classifications.
  First introduced in 2018 as a pilot, with a more extensive rollout in
  2022, LUCAS provides point-based vector data that serves as a
  ground-truth dataset for European grassland studies. LUCAS data points
  are already used for validation and training samples in the production
  of HRL VLCC Grassland data.
- **Global Pasture Watch** delivers 30m-resolution raster data on a
  global scale, mapping annual pasture extent, livestock density, short
  vegetation cover, and gross primary productivity. Covering the period
  2000-2022, this initiative integrates multiple Earth observation
  datasets to monitor the dynamics of both natural and managed
  pasturelands. It may serve as a valuable resource for tracking global
  grassland changes, particularly in response to climate change, grazing
  pressures, and land-use conversion.
- **The SUPER-G Project** takes a multidisciplinary approach to
  sustainable grassland management, integrating remote sensing, field
  studies, and policy research. Running from 2018 to 2023 under the
  Horizon 2020 framework, SUPER-G focused on developing sustainable
  permanent grassland systems by combining 10m-resolution Sentinel-1 and
  Sentinel-2 data with field-based ecological assessments. Its outputs
  include policy recommendations, biodiversity assessments, and tools
  for optimising land management practices.
- **GRASS SIGNAL** is a real-time monitoring and forecasting tool
  designed for agricultural applications, predicting grass yield,
  quality, and moisture supply over a five-day forecast period. Using
  Sentinel-1 and Sentinel-2 data provides insights into biomass
  productivity, crude protein content, nitrogen uptake, and the energy
  value of grasslands. GRASS SIGNAL is valuable as an aid tool to
  farmers and land managers in optimising grazing and forage management
  while contributing to precision agriculture applications.
- Lastly, the **ESDAC Soil Biomass Productivity Maps** offer a static,
  model-based assessment of grassland productivity across the EU. These
  maps, developed by the European Soil Data Centre (ESDAC), evaluate
  grassland fertility and productivity potential under varying soil,
  climatic, and topographical conditions. Based on long-term modelling,
  the dataset (published in 2016) provides 1km-resolution raster data,
  offering insights into the inherent soil productivity of European
  grasslands without being influenced by short-term climatic
  variability.

These explorations on several mapping initiatives and grassland-related
projects may help to identify gaps, opportunities, and best practices
for future grassland monitoring activities, supporting the evolution of
the HRL VLCC Grassland product. The table below provides an overview of
key grassland mapping initiatives and data sources (excluding HRL VLCC
Grassland and complex LU/LC datasets like the Global Land Cover-SHARE
(GLC-SHARE)). Each source has its unique focus, coverage, and
applications, making them useful for different grassland monitoring
tasks. The following subchapters briefly introduce the individual
initiatives (except for EUGW), including visualizing the data if
available, and a more detailed comparison between the EUGW and HRL VLCC
Grassland will be then provided.

Table 1 An overview of different initiatives (except for CLMS HRL VLCC
Grassland) that map grassland in Europe and globally. These initiatives
cover a broad range of thematic categories, including remote
sensing-based grassland mapping, field-based mapping, policy-oriented
and research projects, and Al-based monitoring services.

| Source/Initiative/Project | Brief description | Spatial coverage | Temporal coverage | Resolution, Data type |
|----|----|----|----|----|
| **EU Grassland Watch (EUGW)** <br> Source: <br> <https://cop4n2k.eu/> <br> <https://ec.europa.eu/eu-grassland-watch/> | Monitors grassland management, productivity, and biodiversity within Natura 2000 sites. | Europe (only Natura 2000 sites) | yearly, 1994-present (Sentinel and pre-Sentinel era) | 10m (Sentinel era), 30m (pre-Sentinel era), raster |
| **LUCAS Grassland Module** <br> Source: <br> <https://wikis.ec.europa.eu/display/EUPKH/LUCAS+grassland+survey> | Provides indicative information on grassland management sward height and floristic composition collected via an in-situ survey. LUCAS data points are already used for validation and training samples in the production of HRL VLCC. | Europe | 2018 (pilot grassland module, 3000 sites), 2022 (full module, 20000 sites) | Point-based, vector |
| **Global Pasture Watch** <br> Source: <br> <https://landcarbonlab.org/about-global-pasture-watch/> | Provides a 30-meter global dataset mapping annually. This includes four deliverables: Pasture, livestock density map, short vegetation map, and gross primary productivity map. | Global | 2000-2022 | 30m, raster |
| **SUPER-G Project** <br> Source: <br> <https://cordis.europa.eu/project/id/774124>, <br> <https://www.super-g.eu/> | A European research initiative focused on developing sustainable permanent grassland systems and policies, combining field data, remote sensing, and modelling outputs to promote biodiversity, productivity, and ecosystem services. | Europe (case studies) | policy-oriented, has been implemented during 2018-2023 (Horizon 2020 project) | policy-oriented, field surveys, recommendations |
| **GRASS SIGNAL** <br> Source: <br> <https://business.esa.int/projects/grasssignal> | Service that helps to monitor grass growth. It predicts the yield and quality of grass for a five-day forecast period. | Africa, Australia, USA, UK | 2016 and onwards (considering Sentinel-2 data), weekly predictions | up to 10m (Sentinel-1 and Sentinel-2), raster |
| **ESDAC Soil Biomass Productivity (Grassland Layer)** <br> Source: <br> <https://esdac.jrc.ec.europa.eu/content/soil-biomass-productivity-maps-grasslands-and-pasture-coplands-and-forest-areas-european> | A map that provides soil biomass productivity maps, assessing grassland fertility and productivity under varying soil, climatic, and topographical conditions. | Europe (EU27) | 2016 (based on long-term soil productivity modelling) | 1km, raster (GeoTIFF) |

## A closer look into selected initiatives - background, data, products, methods.

### Global Pasture Watch [^1][^2][^3]

The Global Pasture Watch research consortium provides high-resolution
(30m) annual grassland mapping products covering the period 2000-2022,
with planned updates beyond 2022. This collaborative initiative is led
by the Land & Carbon Lab in partnership with multiple research
institutions, including the World Resources Institute, OpenGeoHub,
IIASA, the German Centre for Integrative Biodiversity Research, and
Cornell University. The consortium applies state-of-the-art machine
learning techniques, earth observation data fusion, and crowdsourced
validation to create highly accurate grassland and pasture mapping
products. This chapter provides an overview of the available dataset,
its methodology, key deliverables, and potential applications with CLMS
HRL VLCC Grassland.

The dataset consists of four core mapping products that integrate
multi-source earth observation data and expert validation. This includes
the following four key products:

- **Pasture Class Maps**

  Represented by annual land cover classification maps at 30m resolution
  identifying natural/semi-natural and cultivated pastures globally.
  Using a probabilistic classification approach, these maps
  differentiate grasslands from other land cover types.

- **Livestock Density Maps**

  Provide per-hectare estimates of livestock density, identifying
  hotspots of managed and unmanaged grazing areas. These maps support
  the monitoring of rangeland management, overgrazing, and
  livestock-related carbon emissions.

- **Short Vegetation Height Maps**

  Represent annual 30m-resolution vegetation height estimates, helping
  to identify grassland structure and biomass availability. These maps
  are derived from IceSat-2 LiDAR data, offering insights into pasture
  productivity and suitability for grazing. Root mean square error
  (RMSE) ranges around 2.3m depending on the monitored vegetation type.
  Vegetation height is expressed as majority value rather than mean or
  median values.

- **Gross Primary Productivity (GPP) Maps**

  Represented by bi-monthly carbon flux maps, estimating the amount of
  carbon fixed by grasslands through photosynthesis. These maps help
  assess grassland health, productivity, and carbon sequestration
  potential over time.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-a2c96346397e60da1174013adc9a2c45.png"
data-fig-alt="This diagram illustrates the Global Pasture Watch methodology for generating high-resolution annual grassland mapping products, spanning the period 2000–2022. The legend indicates white boxes represent Data and grey boxes represent Methods. The workflow begins with **Earth Observation data preprocessing**, including: 1. Bi-monthly Landsat ARD2 (Spectral bands &amp; indices). 2. Long-term MODIS (Temperature &amp; water vapor). 3. Geometric temperature (Monthly maximum &amp; minimum). 4. Static digital terrain model (Elevation, slope &amp; hillshade). 5. Static distance maps (Accessibility, roads, water). These inputs are combined in a &#39;Spacetime overlay&#39; for all features. In parallel, **reference data is generated**: 1. A &#39;Sampling design (Feature space coverage sampling)&#39; step utilizes &#39;Very high-res. imagery (Google Maps &amp; Bing Maps)&#39; to generate &#39;10,000 tiles (1x1 km)&#39;. 2. These tiles undergo a &#39;Reference labeling protocol (Visual interpretation in QGIS)&#39;. 3. The labeled tiles are processed through &#39;Samples preprocessing and filtering (Conversion to point samples &amp; temporal interpolation)&#39; to create &#39;2.3 million quality-controlled point samples&#39; for cultivated grassland, natural/semi-natural grassland, and other land-cover types. 4. These 2.3 million point samples are then integrated with the &#39;Spacetime overlay&#39; features. The integrated data feeds into **Spatiotemporal model training (5-fold spatial Cross-Validation)**, which forms an &#39;Iterative mapping improvement&#39; loop: 1. &#39;Feature selection (Recursive feature elimination - RFE)&#39;. 2. &#39;Hyperparameter tuning (Successive halving - SH)&#39;. 3. &#39;ML algorithm comparison (Log_loss &amp; precision-recall curve)&#39;. 4. &#39;Training final models (Random Forest)&#39;. This process results in &#39;Production-ready models&#39; (one model per class). These models are used for **Spatiotemporal prediction**: 1. &#39;Global predictions (Probabilities per pixel)&#39; are generated &#39;Per GLAD tile&#39;. 2. Predictions undergo &#39;Smoothing filtering (Spatiotemporal Savitzky-Golay)&#39;. 3. Followed by &#39;Global mosaicking (Cloud Optimized GeoTIFF)&#39;. This yields &#39;Dominant grassland production (Balanced threshold &amp; probability integration)&#39;. **Validation and Feedback Mechanisms**: * &#39;Pre-existing LULC Maps&#39; (UMD GLAD, GLC_FCS30D) and &#39;Pre-existing reference samples&#39; (GLanCE, Copernicus) are harmonized through &#39;Spacetime overlay &amp; overlap (Legend harmonization)&#39;. * This output informs &#39;Spatial comparison (Based on existing LULC maps)&#39; and &#39;Technical validation (Spatial CV &amp; independent validation)&#39;. * It also contributes to &#39;Probability threshold definition (Precision-recall curve)&#39;, which feeds into &#39;Dominant grassland production&#39;. * &#39;Dominant grassland production&#39; provides &#39;Mapping Feedback (Based on local knowledge) GEO-Wiki&#39;, which loops back to the &#39;Spatiotemporal model training&#39; for continuous improvement. * &#39;Grassland reference samples (Multi-year labels 2000–2022)&#39; are used in conjunction with &#39;Spatial comparison&#39;, &#39;Technical validation&#39;, and &#39;Dominant grassland production&#39; outputs to &#39;Publish research outputs (Reference samples, models and maps)&#39;. The final mapping products, available for 2000–2022, include: * Cultivated grassland (Annual probability maps). * Dominant grassland (Annual maps). * Natural / Semi-natural grassland (Annual probability maps). An additional derived product is the &#39;Mean absolute probability difference (Savitzky-Golay 2000–2022)&#39;. All data is publicly available through Google Earth Engine, Zenodo, and the SpatioTemporal Asset Catalog (STAC)."
alt="Figure 1 Methodology of Global Pasture Watch dataset production. The diagram outlines the workflow used to generate the grassland class and extent datasets, including data preprocessing, sampling, machine learning classification, validation, and map production." />

This diagram illustrates the Global Pasture Watch methodology for
generating high-resolution annual grassland mapping products, spanning
the period 2000–2022. The legend indicates white boxes represent Data
and grey boxes represent Methods.

The workflow begins with **Earth Observation data preprocessing**,
including: 1. Bi-monthly Landsat ARD2 (Spectral bands & indices). 2.
Long-term MODIS (Temperature & water vapor). 3. Geometric temperature
(Monthly maximum & minimum). 4. Static digital terrain model (Elevation,
slope & hillshade). 5. Static distance maps (Accessibility, roads,
water). These inputs are combined in a “Spacetime overlay” for all
features.

In parallel, **reference data is generated**: 1. A “Sampling design
(Feature space coverage sampling)” step utilizes “Very high-res. imagery
(Google Maps & Bing Maps)” to generate “10,000 tiles (1x1 km)”. 2. These
tiles undergo a “Reference labeling protocol (Visual interpretation in
QGIS)”. 3. The labeled tiles are processed through “Samples
preprocessing and filtering (Conversion to point samples & temporal
interpolation)” to create “2.3 million quality-controlled point samples”
for cultivated grassland, natural/semi-natural grassland, and other
land-cover types. 4. These 2.3 million point samples are then integrated
with the “Spacetime overlay” features.

The integrated data feeds into **Spatiotemporal model training (5-fold
spatial Cross-Validation)**, which forms an “Iterative mapping
improvement” loop: 1. “Feature selection (Recursive feature
elimination - RFE)”. 2. “Hyperparameter tuning (Successive halving -
SH)”. 3. “ML algorithm comparison (Log_loss & precision-recall curve)”.
4. “Training final models (Random Forest)”. This process results in
“Production-ready models” (one model per class).

These models are used for **Spatiotemporal prediction**: 1. “Global
predictions (Probabilities per pixel)” are generated “Per GLAD tile”. 2.
Predictions undergo “Smoothing filtering (Spatiotemporal
Savitzky-Golay)”. 3. Followed by “Global mosaicking (Cloud Optimized
GeoTIFF)”. This yields “Dominant grassland production (Balanced
threshold & probability integration)”.

**Validation and Feedback Mechanisms**: \* “Pre-existing LULC Maps” (UMD
GLAD, GLC_FCS30D) and “Pre-existing reference samples” (GLanCE,
Copernicus) are harmonized through “Spacetime overlay & overlap (Legend
harmonization)”. \* This output informs “Spatial comparison (Based on
existing LULC maps)” and “Technical validation (Spatial CV & independent
validation)”. \* It also contributes to “Probability threshold
definition (Precision-recall curve)”, which feeds into “Dominant
grassland production”. \* “Dominant grassland production” provides
“Mapping Feedback (Based on local knowledge) GEO-Wiki”, which loops back
to the “Spatiotemporal model training” for continuous improvement. \*
“Grassland reference samples (Multi-year labels 2000–2022)” are used in
conjunction with “Spatial comparison”, “Technical validation”, and
“Dominant grassland production” outputs to “Publish research outputs
(Reference samples, models and maps)”.

The final mapping products, available for 2000–2022, include: \*
Cultivated grassland (Annual probability maps). \* Dominant grassland
(Annual maps). \* Natural / Semi-natural grassland (Annual probability
maps). An additional derived product is the “Mean absolute probability
difference (Savitzky-Golay 2000–2022)”. All data is publicly available
through Google Earth Engine, Zenodo, and the SpatioTemporal Asset
Catalog (STAC).

The Global Pasture Watch dataset is derived using an integrated remote
sensing and machine learning approach (see Figure 1). It combines GLAD
Landsat ARD-2, MOD11A2, MCD19A2, and auxiliary datasets (e.g.,
accessibility, roads, water) to enhance classification accuracy. Over
2.3 million reference samples, visually interpreted from VHR imagery
within the dedicated QGIS Fast Grid Inspection plugin, support model
training. Two spatiotemporal Random Forest models separately classify
cultivated and natural/semi-natural grasslands, ensuring robust
differentiation. The models generate annual probability-based maps
(2000–2022) at 30m resolution, enabling long-term monitoring of
grassland dynamics.

Furthermore, various maps can be generated using custom algorithms
accessible from GitHub (see:
<https://github.com/wri/global-pasture-watch/blob/main/ggc-30m/README.md>),
and data produced by the Global Pasture Watch project can also be viewed
by the Google Earth Engine app (see:
<https://global-pasture-watch.projects.earthengine.app/view/ggc-30m>;
Figure 2).

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-d2c7542543900ab5b4943b0b539ce4b9.png"
data-fig-alt="This map displays the annual grassland class and extent maps at 30-metre spatial resolution for the region around Innsbruck, Austria, in the year 2020, as viewed within an &#39;Earth Engine Apps&#39; interface. The base map is a satellite image showing urban areas (Innsbruck, Hall in Tirol, Absam, Wattens), major roads (A12, E45, A13, B182, B171), forests, and mountainous terrain. An overlay highlights areas classified as grassland. A &#39;Map customization&#39; panel is visible on the right, allowing the user to configure the display. The selected &#39;Year&#39; is 2020. Sliders are present for two grassland types, indicating probabilistic classification thresholds: * Natural / semi-natural Grassland: set at 0.43 * Cultivated Grassland: set at 0.32 A button to &#39;Apply default thresholds&#39; is also visible. The legend for &#39;Dominant grassland&#39; classes is: * Orange: Cultivated grassland * Red/Brown: Natural/Semi-natural grassland The map shows a distribution where natural/semi-natural grasslands (red/brown) are prevalent in mountainous areas and on slopes, particularly south of Innsbruck and around prominent peaks. Cultivated grasslands (orange) appear more fragmented and are often found in valleys and lower-lying areas, interspersed with urban settlements and agricultural plots. The scale bar at the bottom right indicates &#39;2 km&#39;. Map data is sourced from ©2025 GeoBasis-DE/BKG (©2009) and Google Imagery ©2025 TerraMetrics."
alt="Figure 2 Viewing Global Pasture Watch products in the web application." />

This map displays the annual grassland class and extent maps at 30-metre
spatial resolution for the region around Innsbruck, Austria, in the year
2020, as viewed within an “Earth Engine Apps” interface. The base map is
a satellite image showing urban areas (Innsbruck, Hall in Tirol, Absam,
Wattens), major roads (A12, E45, A13, B182, B171), forests, and
mountainous terrain. An overlay highlights areas classified as
grassland.

A “Map customization” panel is visible on the right, allowing the user
to configure the display. The selected “Year” is 2020. Sliders are
present for two grassland types, indicating probabilistic classification
thresholds: \* Natural / semi-natural Grassland: set at 0.43 \*
Cultivated Grassland: set at 0.32 A button to “Apply default thresholds”
is also visible.

The legend for “Dominant grassland” classes is: \* Orange: Cultivated
grassland \* Red/Brown: Natural/Semi-natural grassland

The map shows a distribution where natural/semi-natural grasslands
(red/brown) are prevalent in mountainous areas and on slopes,
particularly south of Innsbruck and around prominent peaks. Cultivated
grasslands (orange) appear more fragmented and are often found in
valleys and lower-lying areas, interspersed with urban settlements and
agricultural plots. The scale bar at the bottom right indicates “2 km”.
Map data is sourced from ©2025 GeoBasis-DE/BKG (©2009) and Google
Imagery ©2025 TerraMetrics.

In summary, some aspects of Global Pasture Watch can be relevant to the
potential further development of CLMS HRL VLCC Grassland data. In
particular, methodologies applied to produce the Global Pasture Watch
dataset may contribute to enhancing the CLMS HRL VLCC Grassland product
by machine learning-based classification. HRL VLCC could benefit from
similar probabilistic classification methods, for example, for detecting
grassland management practices, which is one of the challenges in
grassland mapping within the CLMS portfolio. This information about
farming practises of management intensity is sometimes available only in
national LPIS data, although it can be very useful for various research
related to, for example, productivity monitoring on the pan-European
level. Specifically, grazing still remains an important aspect of
agricultural grassland management not addressed within the VLCC. Within
Global Pasture Watch grazing is inferred from national databases. For
Europe this is mainly provided by Eurostat. While this approach is
suitable for products with a global scope, it does not provide means to
map at higher spatial accuracy underlining the need for in-situ data on
livestock density to be used as input for higher resolution mapping
within Europe.

Another interesting product provided by the Global Pasture Watch are the
short vegetation height maps. This is a LIDAR derived mapping product
indicating dominant sward height. While again this is very interesting
global product, the spatial resolution may not be suitable for European
applications especially for e.g. such as measuring scrub encroachment.
Vegetation height as such remains an important aspect of grassland
physiology and structure and remains excluded from the VLCC.

### SUPER-G Project[^4][^5]

The SUPER-G project (SUstainable PERmanent Grassland systems and
policies) is a five-year European initiative (2018–2023) primarily aimed
as a policy-oriented and research-driven initiative rather than a
data-providing project like EU Grassland Watch or Global Pasture Watch.
It focuses on developing sustainable permanent grassland systems and
policies, engaging multiple stakeholders (farmers, policymakers,
researchers) to promote biodiversity, ecosystem services, and climate
resilience in grassland management. The overall objective of the SUPER-G
project is to co-develop sustainable permanent grassland systems and
policies with farmers and policymakers that will be effective in
optimising productivity whilst supporting biodiversity and delivering
several ecological services. The key objectives include:

- **Co-Development**

  Engage farmers, policymakers, and other stakeholders to
  collaboratively develop sustainable permanent grassland systems,
  typology and policies to improve communication and policymaking across
  Europe.

- **Ecosystem Services Optimization**

  Conduct a systematic review of grassland multifunctionality,
  emphasizing their role in providing ecological services like carbon
  sequestration, biodiversity, and climate resilience benefits.

- **Benchmarking and Testing**

  Assess the productivity of permanent grasslands across Europe through
  field data collection and analysis from farm networks and experimental
  platforms.

- **Policy Support**

  Develop tools and mechanisms that inform and support policy decisions
  related to the management of permanent grasslands. Evaluating existing
  policies and developing recommendations to support sustainable
  permanent grassland management.

SUPER-G employs a multi-actor approach involving farmers, land managers,
advisors, researchers, and policymakers. The project spans 14 countries
across various European biogeographic regions, including the
Mediterranean, Atlantic, Continental, Alpine, Pannonian, and Boreal
zones (Figure 3).

<div class="tbl-caption">

Figure 3 An example of one of the experimental sites where innovative
grassland management options and new technologies, such as spectral and
electromagnetic sensors, were tested and evaluated.

</div>

<table data-quarto-postprocess="true">
<colgroup>
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr>
<th style="background-color: #d9ead3"><strong>SITE</strong></th>
<th style="background-color: #d9ead3"><strong>BIOGEOGRAPHIC
REGION</strong></th>
<th style="background-color: #d9ead3"><strong>LEAD ORGAN.</strong></th>
<th style="background-color: #d9ead3"><strong>MANAGEMENT OPTION(S)
/<br />
TECHNOLOGIES TESTED</strong></th>
<th style="background-color: #d9ead3"><strong>MEASUREMENTS</strong></th>
<th style="background-color: #d9ead3"><strong>ES</strong></th>
<th style="background-color: #d9ead3"><strong>TYPE OF<br />
INVESTIGATED AGRICULTURE</strong></th>
<th style="background-color: #d9ead3"><strong>LIVEST. TYPE</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Forage Research Station, Moravian Uplands</td>
<td>Continental / Pannonian</td>
<td>MENDU</td>
<td>Grazing management<br />
Fertilisation<br />
Species mixes<br />
Over-seeding methods</td>
<td>Grass yield and quality<br />
Water balance and flows</td>
<td>Food Production<br />
Water quality<br />
Flood control<br />
Erosion Control</td>
<td>Conventional<br />
Organic</td>
<td>Dairy<br />
Beef</td>
</tr>
</tbody>
</table>

While SUPER-G does not provide a large-scale remote sensing dataset, the
most important additional value of the SUPER-G project probably lies in
the extensive research findings, various factsheets (see:
<https://www.super-g.eu/communication/factsheets/>), case study results,
and policy recommendations, which can contribute to the future
development of CLMS HRL VLCC Grassland. This can be achieved by
improving classification rules based on refining definitions of
grasslands, identifying new grassland management indicators that could
enhance CLMS HRL VLCC Grassland portfolio by detecting mowing events or
grazing intensity or supporting the integration of grassland typologies
that better reflect management intensity, sustainability practices, and
biodiversity metrics.

### GRASS SIGNAL[^6]

In contrast to two previously described initiatives, the GRASS SIGNAL
project is an Al-powered satellite-based grassland monitoring and
decision-support service designed to provide real-time insights on grass
growth, biomass, quality, and degradation risks. The GRASS SIGNAL is a
dynamic forecasting tool, delivering weekly predictions to support
sustainable grassland and rangeland management. Developed by Deep Planet
in partnership with the European Space Agency, the project harnesses
Earth Observation data (Sentinel-1 and Sentinel-2), Al-driven analytics,
and machine learning models (Figure 4) to optimise grazing,
fertilisation, and irrigation strategies across diverse ecosystems.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-a79014b42b25044941de77e38a333dee.png"
data-fig-alt="This system architecture diagram illustrates a Proprietary Machine Learning Platform that integrates various agricultural data sources to produce analytical outputs. The central processing component is labelled &#39;Machine Learning, Catalogs, Models, Data Science&#39;. The platform&#39;s data inputs are: 1. **Satellite Data Optical + Radar**: This data source interacts bidirectionally with the &#39;Machine Learning, Catalogs, Models, Data Science&#39; core. 2. **Crop Agronomy**: This input interacts bidirectionally with both &#39;Machine Learning, Catalogs, Models, Data Science&#39; and &#39;In Field Data&#39;. 3. **In Field Data**: This input interacts bidirectionally with &#39;Machine Learning, Catalogs, Models, Data Science&#39;, &#39;Crop Agronomy&#39;, and &#39;Historical Data&#39;. 4. **Historical Data**: This input interacts bidirectionally with &#39;Machine Learning, Catalogs, Models, Data Science&#39; and &#39;In Field Data&#39;. The &#39;Machine Learning, Catalogs, Models, Data Science&#39; core processes these inputs and generates five distinct outputs, each represented by a monitor display: 1. **Crop Detection + Yield Forecast**: Displays a map-like visualization of land areas, potentially indicating crop types or conditions. 2. **Health Prediction**: Shows multiple time-series graphs with varying coloured lines, suggesting monitoring of health metrics over time. 3. **Soil Moisture Prediction**: Presents two heatmap-like visualizations, likely indicating spatial distribution of soil moisture levels. 4. **Crop Monitoring + Actions**: Displays a map with distinct field boundaries, colour-coded areas (green, red, yellow), and highlighted sections with red outlines, implying monitoring and recommended actions. 5. **Yield Prediction**: Features a bar chart with three series (orange, blue, grey) across multiple categories, indicating predicted yield values."
alt="Figure 4 Prediction scheme based on a proprietary machine learning platform." />

This system architecture diagram illustrates a Proprietary Machine
Learning Platform that integrates various agricultural data sources to
produce analytical outputs. The central processing component is labelled
“Machine Learning, Catalogs, Models, Data Science”.

The platform’s data inputs are: 1. **Satellite Data Optical + Radar**:
This data source interacts bidirectionally with the “Machine Learning,
Catalogs, Models, Data Science” core. 2. **Crop Agronomy**: This input
interacts bidirectionally with both “Machine Learning, Catalogs, Models,
Data Science” and “In Field Data”. 3. **In Field Data**: This input
interacts bidirectionally with “Machine Learning, Catalogs, Models, Data
Science”, “Crop Agronomy”, and “Historical Data”. 4. **Historical
Data**: This input interacts bidirectionally with “Machine Learning,
Catalogs, Models, Data Science” and “In Field Data”.

The “Machine Learning, Catalogs, Models, Data Science” core processes
these inputs and generates five distinct outputs, each represented by a
monitor display: 1. **Crop Detection + Yield Forecast**: Displays a
map-like visualization of land areas, potentially indicating crop types
or conditions. 2. **Health Prediction**: Shows multiple time-series
graphs with varying coloured lines, suggesting monitoring of health
metrics over time. 3. **Soil Moisture Prediction**: Presents two
heatmap-like visualizations, likely indicating spatial distribution of
soil moisture levels. 4. **Crop Monitoring + Actions**: Displays a map
with distinct field boundaries, colour-coded areas (green, red, yellow),
and highlighted sections with red outlines, implying monitoring and
recommended actions. 5. **Yield Prediction**: Features a bar chart with
three series (orange, blue, grey) across multiple categories, indicating
predicted yield values.

The GRASS SIGNAL is specifically designed to support farmers, rangeland
managers, livestock producers, and policymakers by providing highly
accurate, data-driven decision support. The service offers:

- **Biomass & Growth Monitoring**

  Provides weekly biomass estimates at up to 97% accuracy, identifying
  growth patterns and productivity.

- **Overgrazing & Degradation Alerts**

  Detects high-impact grazing areas and signals land degradation risks
  for adaptive management.

- **Irrigation & Fertilization Insights**

  Uses NDVI and NDWI indicators to predict water stress and nutrient
  requirements for improved pasture management.

- **Decision-Support System**

  Integrated into Deep Planet’s Al platform, offering automated
  recommendations and work order tracking to optimise grazing
  strategies.

- **Scalability & Global Reach**

  Initially designed for African rangelands, then extended to Australia,
  the USA, and the UK, with applications for intensively grazed
  pastures.

The GRASS SIGNAL methodology integrates Sentinel-1 SAR and Sentinel-2
optical imagery, accessed via the Sentinel Hub API, to enable
high-resolution monitoring of grasslands. It employs Al-driven
predictive models trained on EO data, historical field observations, and
in-situ validation, ensuring accurate classification. The system
provides high-frequency updates, generating biomass, grazing intensity,
and moisture maps every 2 to 3 days, significantly enhancing traditional
monitoring approaches. Additionally, the cloud-based Al platform offers
a web interface for visualizing data, receiving alerts, and tracking
pasture conditions in real time, facilitating informed decision-making
for land managers and stakeholders (Figure 5).

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-cf0e8ae09be78ccc205a2752e64a7c0f.png"
data-fig-alt="The image displays a geographic information system (GIS) map from the &#39;deepplanet&#39; web platform, showcasing &#39;Grassland Biomass (kg/he)&#39; for the &#39;EnonkishuBlocks&#39; farm/conservancy, located within Bomet County and Nakuru County, Kenya. The underlying map is satellite imagery from 2020, with map data attributed to Google and imagery to CNES/Airbus, Landsat/Copernicus, and Maxar Technologies. An overlaid colour-coded layer on the map indicates Grassland Biomass for the period 1 October 2020 to 24 November 2020. The legend shows a gradient from red (2100 kg/he) to blue (2200+ kg/he), representing biomass density. Areas within the white outlined conservancy boundary display varying biomass levels, with patches of dark blue indicating high biomass and red/orange indicating lower biomass. Major roads, such as &#39;C14&#39; and &#39;C13&#39;, are visible, along with county labels for &#39;BOMET COUNTY&#39; and &#39;NAKURU COUNTY&#39;. The user interface on the left provides navigation options under &#39;Soil Signal&#39;, with &#39;Grassland Biomass&#39; currently highlighted. Other available options include &#39;Dashboard&#39;, &#39;Summary&#39;, &#39;Overgrazed Area&#39;, &#39;Forst Biomass&#39; (likely Forest Biomass), &#39;Bare Soil&#39;, &#39;Leaf Area&#39;, &#39;Plant Density&#39;, &#39;Plant Mature&#39;, &#39;Plant Young&#39;, &#39;Plant Height&#39;, &#39;NDVI ESA&#39; (Normalised Difference Vegetation Index European Space Agency), and &#39;NDWI ESA&#39; (Normalised Difference Water Index European Space Agency). Specific dates are associated with some metrics, such as Plant Density (7 Nov 2020), Plant Mature (23 Oct 2020), Plant Young (8 Oct 2020), and Plant Height (3 Oct 2020). The top bar of the application features &#39;SETTINGS&#39;, &#39;HELP&#39;, &#39;Languages&#39;, and a user welcome message &#39;Welcome, enonkishu&#39;. The map illustrates the spatial distribution of grassland biomass within the conservancy, highlighting heterogeneous productivity levels across the area for the specified time frame."
alt="Figure 5 Web-based platform offering a user-friendly interface for visualizing data." />

The image displays a geographic information system (GIS) map from the
“deepplanet” web platform, showcasing “Grassland Biomass (kg/he)” for
the “EnonkishuBlocks” farm/conservancy, located within Bomet County and
Nakuru County, Kenya. The underlying map is satellite imagery from 2020,
with map data attributed to Google and imagery to CNES/Airbus,
Landsat/Copernicus, and Maxar Technologies.

An overlaid colour-coded layer on the map indicates Grassland Biomass
for the period 1 October 2020 to 24 November 2020. The legend shows a
gradient from red (2100 kg/he) to blue (2200+ kg/he), representing
biomass density. Areas within the white outlined conservancy boundary
display varying biomass levels, with patches of dark blue indicating
high biomass and red/orange indicating lower biomass. Major roads, such
as “C14” and “C13”, are visible, along with county labels for “BOMET
COUNTY” and “NAKURU COUNTY”.

The user interface on the left provides navigation options under “Soil
Signal”, with “Grassland Biomass” currently highlighted. Other available
options include “Dashboard”, “Summary”, “Overgrazed Area”, “Forst
Biomass” (likely Forest Biomass), “Bare Soil”, “Leaf Area”, “Plant
Density”, “Plant Mature”, “Plant Young”, “Plant Height”, “NDVI ESA”
(Normalised Difference Vegetation Index European Space Agency), and
“NDWI ESA” (Normalised Difference Water Index European Space Agency).
Specific dates are associated with some metrics, such as Plant Density
(7 Nov 2020), Plant Mature (23 Oct 2020), Plant Young (8 Oct 2020), and
Plant Height (3 Oct 2020). The top bar of the application features
“SETTINGS”, “HELP”, “Languages”, and a user welcome message “Welcome,
enonkishu”.

The map illustrates the spatial distribution of grassland biomass within
the conservancy, highlighting heterogeneous productivity levels across
the area for the specified time frame.

While GRASS SIGNAL is not a conventional grassland mapping initiative,
its dynamic monitoring capabilities offer potential enhancements to CLMS
HRL VLCC Grassland. These improvements could benefit from high-frequency
biomass updates, which may, for instance, enhance the detection of
seasonal mowing events. However, it may also be useful to integrate
these advancements into product platforms such as the High Resolution –
Vegetation Phenology and Productivity (HR-VPP) where their application
may be more targeted. Furthermore, GRASS SIGNAL’s data on overgrazing
and soil moisture could refine CLMS HRL VLCC Grassland classifications
by distinguishing between different management practices.

### ESDAC Soil Biomass Productivity (Grassland Layer)[^7]

The ESDAC Soil Biomass Productivity dataset is a static mapping product
developed by the European Soil Data Centre (ESDAC) under the Joint
Research Centre (JRC) of the European Commission. This dataset provides
a model-based assessment of soil biomass productivity for grasslands,
croplands, and forests across the EU27 (with reference year 2016 based
on long-term soil productivity modelling). The grassland-specific
component of this dataset classifies and ranks grassland soil
productivity based on inherent soil fertility, climate conditions, and
land use. It relies on soil modelling and spatial interpolation
techniques to estimate productivity patterns. The calculations integrate
pre-existing soil datasets, climate models, and topographic information,
resulting in 1 km resolution raster maps that depict relative soil
fertility on a standardised scale (0-10).

The ESDAC Soil Biomass Productivity dataset may potentially complement
HRL VLCC Grassland by improving the characterization of grassland soil
fertility. The dataset offers potential for insights into further
grassland classification, particularly in distinguishing productive
vs. marginal grasslands, particularly in regions where long-term soil
conditions strongly influence grassland productivity.

## Comparison of CLMS HRL VLCC Grassland with EUGW

### Initial look into both datasets

- **CLMS HRL VLCC Grassland portfolio**

The HRL VLCC Grassland dataset represents a fundamental restructuring of
the pre-existing High-Resolution Layer (HRL) Grassland products from
2015 and 2018, while also maintaining consistency with them. Unlike
traditional land cover datasets, HRL VLCC does not solely focus on land
cover classification but extends to include essential management
practices, such as mowing events and ploughing indicators. This approach
is intended to enhance the understanding of grassland dynamics,
particularly in agricultural and environmental monitoring contexts.

The HRL VLCC Grassland dataset is derived from multi-temporal
classifications using a combination of Sentinel-1 (SAR) and Sentinel-2
(optical) satellite imagery. The processing workflow integrates Base
Vegetation Layers (BVLs), which serve as an annual composite layer,
offering insights into grassland health and changes over time.
Calibration with existing Copernicus datasets, such as HRL Grassland
2018 and CLC 2018, ensures consistency in classification and reduces
discrepancies between different data years. Additionally, confidence
layers are included to assess the reliability of the classification
results, offering users a measure of uncertainty in the dataset. With
annual time-series the product is unprecedented in timeliness of
provided thematic information. However, it is important to understand
that annual production does not equal a change mapping and although a
specific class probability weighting scheme is applied between years to
minimize noise changes between years can occur simply by chance. There
is also a dedicated Grassland Change layer which acts as a continuation
of the HRL tri-annual cycle. This undergoes an internal validation and
is set at 80% mapping accuracy.

The HRL VLCC dataset provides wall-to-wall coverage across all 38 EEA
member and cooperating countries, making it highly suitable for policy
monitoring, Common Agricultural Policy (CAP) compliance assessments, and
large-scale environmental monitoring efforts.

<div class="tbl-caption">

Table 2 Overview of HRL VLCC Grassland portfolio

</div>

| No | Name of product | Acronym | Description |
|----|----|----|----|
| 1 | Grassland | GRA | Binary layer mapping grasslands (10m) |
| 2 | Grassland | GRA | Binary layer mapping grasslands (100m) |
| 3 | Grassland Change | GRAC | Change layer between 2018 and 2021, gain, loss or unchanged |
| 4 | Ploughing indicator | PLOUGH | Number of years before when ploughing occurred |
| 5 | Grassland Confidence Layer | GRACL | Percentage of grassland confidence |
| 6 | Herbaceous cover | HER | Binary layer defining temporary grasslands |
| 7 | Grassland change confidence layer | GRACL | Percentage of grassland change confidence |
| 8 | Grassland mowing events | GRAME | Number of mowing events detected |
| 9 | Grassland mowing event dates | GRAMD | Date of the year when mowing event started |
| 10 | GRAME confidence layers | GRAMECL | Mowing detection confidence |
| 11 | Points for internal quality control of Grassland products | GRAREF | Point marking 10m pixel annotated as grassland vs non-grassland |

**EU Grassland Watch (EUGW)**

The EUGW is a targeted grassland mapping initiative that focuses on
Natura 2000 sites rich in grassland biodiversity (Table 3). Unlike HRL
VLCC Grassland, which provides pan-European coverage, EUGW is restricted
to the boundaries of Natura 2000 and is designed primarily for
conservation, biodiversity monitoring, and Article 17 reporting under
the EU Habitats Directive.

<div class="tbl-caption">

Table 3 Summary of key characteristics of the EUGW project.

</div>

| Feature/component | Description |
|----|----|
| Coverage | Natura 2000 sites in Europe |
| Reference Years | 1994-2024 (continuous time series) |
| Primary Data Sources | Sentinel-1 (SAR), Sentinel-2 (optical), Landsat, DEM |
| Classification Approach | Machine learning-based classification with NDVI time series and SAR backscatter indices |
| Key Thematic Components | Grassland Type (EUNIS habitat mapping), Management (mowing, ploughing, grazing), Productivity (NDVI-based trends) |
| Change Detection | Annual information without dedicated change layers. |
| Temporal Harmonization | Yes, ensures long-term trend consistency |
| Validation Methods | Validation of Land Cover product is primarily conducted based on photo interpretation using a dedicated web-tool (Sentinel era) as well as in-situ data. Model accuracy of the Grassland Type component is validated using, national inventories, and in situ databases such as the European Vegetation Archive. |
| User Target Group | Biodiversity conservation, Natura 2000 monitoring, Article 17 reporting |

The product definition and choice of input data for EUGW have been
aligned with CLMS mapping products. At a primary level, EUGW provides a
basic 9-class land cover product, which mostly complies with CLC+
Backbone for potential analysis going beyond the extent of Natura 2000
alone. This land cover product is provided for an extensive time series
from 1994 to 2024, starting with the birth of the Natura 2000 network in
1994 until the present. The land cover product provides the basic
spatial delineation mask to identify permanent herbaceous vegetation.

At the secondary level, all areas within this mask are further
characterised by three independent components (Figure 6Figure 6 Three
independent thematic components developed within the EUGW project. These
components are further described in more detail in the next chapter.):

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-20f987ca121abf8e62c80bd479a76764.png"
data-fig-alt="This diagram outlines the three key thematic components of the EU Grassland Watch (EUGW) project. 1. **Grassland Type Classification:** This component uses European Nature Information System (EUNIS) Level 2 habitat mapping to differentiate semi-natural grasslands, managed meadows, and intensively used pastures. It aligns with biodiversity conservation goals and habitat quality assessments. 2. **Grassland Management:** This component identifies mowing and ploughing events using Sentinel-1 (Synthetic Aperture Radar) and Sentinel-2 (optical) time series data. It potentially includes grazing indicators, offering insights into land-use intensity, and enables assessments of grassland sustainability and agricultural practices. 3. **Grassland Productivity:** This component is derived from Normalised Difference Vegetation Index (NDVI)-based temporal analysis, tracking short-term and long-term biomass productivity. It includes indicators such as seasonal variations in vegetation health and trends in grassland vigor. Productivity data is computed for the full 1994–2024 time series, with Sentinel-2-based data available from 2016 onwards."
alt="Figure 6 Three independent thematic components developed within the EUGW project. These components are further described in more detail in the next chapter." />

This diagram outlines the three key thematic components of the EU
Grassland Watch (EUGW) project.

1.  **Grassland Type Classification:** This component uses European
    Nature Information System (EUNIS) Level 2 habitat mapping to
    differentiate semi-natural grasslands, managed meadows, and
    intensively used pastures. It aligns with biodiversity conservation
    goals and habitat quality assessments.
2.  **Grassland Management:** This component identifies mowing and
    ploughing events using Sentinel-1 (Synthetic Aperture Radar) and
    Sentinel-2 (optical) time series data. It potentially includes
    grazing indicators, offering insights into land-use intensity, and
    enables assessments of grassland sustainability and agricultural
    practices.
3.  **Grassland Productivity:** This component is derived from
    Normalised Difference Vegetation Index (NDVI)-based temporal
    analysis, tracking short-term and long-term biomass productivity. It
    includes indicators such as seasonal variations in vegetation health
    and trends in grassland vigor. Productivity data is computed for the
    full 1994–2024 time series, with Sentinel-2-based data available
    from 2016 onwards.

Grassland type and productivity are computed for the full-time series
(1994-2024), while the management data relies on a denser time series
and is only available for the Sentinel 2 era (2016 onwards). To enhance
accuracy, EUGW integrates multiple Earth Observation (EO) datasets,
including:

- Machine learning-based classification using Sentinel-1 and Sentinel-2
  imagery.
- Historical Landsat data to extend analysis into the pre-Sentinel era.
- Digital Elevation Models (DEM) to refine landform-based
  classifications.
- SAR backscatter analysis for improved detection of vegetation
  structural changes.

EUGW was developed based on lessons learned from the previous COP4N2K
project, which used a MAES-aligned mixed land cover/land use
nomenclature. Based on user feedback, the pre-classification of
grasslands into fixed categories (e.g., managed or semi-natural
grassland) was found to be too restrictive. As a response, EUGW avoids
hard-coded grassland classifications and instead provides modular
thematic layers that users can combine in different ways to suit their
specific needs. This flexible approach enables better differentiation
between land-use intensity levels, biodiversity values, and management
regimes. One of the key methodological strengths is also the temporal
harmonization framework, which reduces inconsistencies in classification
over time. This ensures that trend analysis remains robust, minimizing
artifacts caused by sensor differences or classification shifts across
different reference years.

Because the product portfolio is highly modular and can thus be
overwhelming to non-expert users, EUGW also offers a dedicated
web-platform containing selected products for direct view.

### Detailed overview of EUGW portfolio

- **Grassland Type Characterization Component**

The Grassland Type Thematic Layer (GTYP) is a key component of the EUGW
dataset, providing spatial information on the distribution of different
grassland types across Natura 2000 sites (Table 4). It is based on a
classification system that aligns with the EUNIS Level-2 habitat
framework, distinguishing categories such as dry grasslands, mesic
grasslands, wet and temporarily wet grasslands, alpine and sub-alpine
meadows, inland salt steppes, forest clearings, and sparsely wooded
grasslands. This classification is derived from a combination of
vegetation indices (NDVI, NMDI, TCARI), SAR backscatter data,
topographic variables (DEM, TWI, TPI), and high-resolution vegetation
phenology datasets (HR-VPP) trained on in-situ data from the LUCAS
grassland module and EVA database. The GTYP layer is updated annually,
ensuring consistency in monitoring habitat conditions, conservation
status, and long-term grassland trends. Its 10m resolution (since 2016)
and 30m resolution (1994-2015) make it suitable for biodiversity
assessments and habitat reporting under Article 17 of the Habitats
Directive. The GTYP layer plays a crucial role in providing reliable
baseline data for ecological assessments, conservation planning, and
land-use monitoring within protected areas.

<div class="tbl-caption">

Table 4 Overview of EUGW - Grassland Type products (the first and key
component)

</div>

| No | Name of product | Acronym | Description |
|----|----|----|----|
| 1 | Grassland Type Thematic Layer | GTYP | Spatial extent of the considered grassland type categories |

- **Grassland Management Characterization Component**

The Grassland Management Characterization Component (GM) of EUGW
provides essential insights into the intensity and frequency of
grassland management activities, including mowing, grazing, and
ploughing (Table 5). This component is designed to track the temporal
persistence of grasslands, distinguishing between permanent and
temporary grasslands based on their management history. It incorporates
data from NDVI-based time-series analysis, bare soil occurrence metrics,
and grassland texture analysis to classify different levels of
management intensity. The GM component includes key datasets such as
Grassland Management Events (MNEV), which record the number of detected
management activities per year, and First and Last Management Event
Dates (MFED, MLED), which mark the timing of interventions. Additional
indicators, like the Grassland Dynamics Index (MGDI) and Gross/Net
Productivity Indices (MGPI, MNPI), compare real productivity and biomass
removal with a theoretical no-management scenario. The component also
assesses bare soil persistence (BSAP, BSRP) and texture uniformity
(GTEX) as proxies for management intensity. These products support
agricultural monitoring, and environmental sustainability assessments,
offering high-resolution data for annual evaluations of grassland
condition and management trends.

<div class="tbl-caption">

Table 5 Overview of EUGW - Grassland Management products (the second
component)

</div>

| No | Name of product | Acronym | Note |
|----|----|----|----|
| 2 | Grassland Management Thematic Layer | GMNG | Spatial extent of the considered grassland management categories |
| 3 | Grassland Persistence - all LC (relative) | GPER | Indication of last land cover change “any-to-grassland” |
| 4 | Grassland Persistence - all LC (absolute) | GPEY | Indication of last land cover change “any-to-grassland” |
| 5 | Grassland Persistence - arable land (relative) | GALR | Indication of last land cover change “arable land-to-grassland” |
| 6 | Grassland Persistence - arable land (absolute) | GALY | Indication of last land cover change “arable land-to-grassland” |
| 7 | Grassland Management Events | MNEV | Number of management events detected during the given year |
| 8 | First Event Date | MFED | Date (DOY) of the first detected management event |
| 9 | Last Event Date | MLED | Date (DOY) of the last detected management event |
| 10 | Grassland Dynamics Index | MGDI | Relative comparison of the real annual grassland dynamics with theoretical “no management scenario” |
| 11 | Grassland Gross Productivity Index | MGPI | Relative comparison of the real annual grassland productivity with theoretical “no management scenario” |
| 12 | Grassland Net Productivity Index | MNPI | Relative comparison of the real annual grassland productivity with theoretical “no management scenario” |
| 13 | Bare Soil Occurrence | BSOC | Monthly indication of bare soil occurrence (on grassland areas) |
| 14 | Bare Soil Anomalies | BSAN | Monthly indication of bare soil anomaly Occurrence (on grassland areas): Bare soil occurrence taking into account the context of the given N2000 site and time |
| 15 | Bare Soil Anomaly Type | BSAT | (differentiate real anomalies from cases where the presence of bare or “almost bare” surfaces could reflect common conditions of the site) Categorization of the identified bare soil anomalies from a temporal perspective: permanently bare vs. damage vs. recovery vs. damage & recovery vs. temporary recovery |
| 16 | Bare Soil Absolute Persistence | BSAP | Number of months for which the given pixel exhibits bare status |
| 17 | Bare Soil Relative Persistence | BSRP | Relative part of the year for which the given pixel exhibits bare status |
| 18 | Grassland Texture | GTEX | Grassland texture: indicator of grassland spatial uniformity |

- **Grassland Productivity Characterization Component**

The Grassland Productivity Characterization Component (GP) of EUGW
provides a detailed assessment of grassland productivity across both
short-term and long-term temporal scales ( Table 6). It evaluates
productivity trends, state, and performance by leveraging
satellite-based phenology and productivity datasets (HR-VPP), NDVI
time-series, and statistical analyses. The short-term productivity
assessment compares annual grassland productivity with a six-year
reference period, while the long-term productivity assessment uses data
from 1996 onwards to evaluate productivity changes over decades. Key
indicators include the Grassland Productivity Trend (SPTR, LPTR), which
tracks increasing or decreasing productivity based on regression
analysis, and Grassland Productivity State (SPSP, LPSP), which
classifies productivity levels relative to historical baselines. The
Grassland Productivity Performance (SPPC, LPPC) assesses productivity
compared to other sites within the same habitat type, offering insights
into grassland condition relative to its ecosystem context. To enhance
accuracy, productivity anomalies are detected using percentile
classifications and Z-score analyses (SPSZ, LPSZ). The GP component is
instrumental in monitoring land-use changes, climate impacts, and
habitat degradation or recovery.

<div class="tbl-caption">

Table 6 Overview of EUGW - Grassland Productivity products (the last
third component)

</div>

| No | Name of product | Acronym | Note |
|----|----|----|----|
| 19 | Grassland Short Term Productivity Thematic Layer | GSTP | Spatial extent of the considered grassland productivity categories |
| 20 | Grassland Long Term Productivity Thematic Layer | GLTP | Spatial extent of the considered grassland productivity categories |
| 21 | Grassland Short Term Productivity Trend - Slope | SPTR | Slope of the short-term productivity trend |
| 22 | Grassland Short Term Productivity Trend - Score | SPRR | R2 of the linear trend fit |
| 23 | Grassland Short Term Productivity Trend - Direction | SPTD | Direction of the short-term productivity trend |
| 24 | Grassland Short Term Productivity Trend - Significance | SPTS | Significance (p-value) of the Mann-Kendall trend test |
| 25 | Grassland Long Term Annual Dynamics Trend - Slope | LPTR | Slope of the long-term productivity trend |
| 26 | Grassland Long Term Annual Dynamics Trend - Score | LPRR | R2 of the linear trend fit |
| 27 | Grassland Long Term Annual Dynamics Trend - Direction | LPTD | Direction of the long-term productivity trend |
| 28 | Grassland Long Term Annual Dynamics Trend - Significance | LPTS | Significance (p-value) of the Mann-Kendall trend test |
| 29 | Grassland Short Term Productivity State - Percentile Classes | SPSP | Comparison of the actual and reference productivity in temporal domain (percentile classes) |
| 30 | Grassland Short Term Productivity State Percentile Classes Change | SPSC | Temporal change of productivity class (percentile classes) |
| 31 | Grassland Short Term Productivity State - Z-Score Classes | SPSZ | Comparison of the actual and reference productivity in temporal domain (z-score classes) |
| 32 | Grassland Long Term Annual Dynamics State | LPSP | Comparison of the actual and reference productivity in temporal domain (percentile classes) |
| 33 | Grassland Long Term Annual Dynamics State | LPSC | Temporal change of productivity class (percentile classes) |
| 34 | Grassland Long Term Annual Dynamics State | LPSZ | Comparison of the actual and reference productivity in temporal domain (z-score classes) |
| 35 | Grassland Short Term Productivity Performance - Percentile Classes | SPPC | Comparison of the actual and reference productivity in spatial domain (percentile classes) |
| 36 | Grassland Short Term Productivity Performance - Z-Score Classes | SPPZ | Comparison of the actual and reference productivity in spatial domain (z-score classes) |
| 37 | Grassland Long Term Annual Dynamics Performance - Percentile Classes | LPPC | Comparison of the actual and reference productivity in spatial domain (percentile classes) |
| 38 | Grassland Long Term Annual Dynamics Performance - Z-score Classes | LPPZ | Comparison of the actual and reference productivity in spatial domain (z-score classes) |

### Similarities and differences

The CLMS HRL VLCC Grassland and EUGW datasets are both high-resolution
grassland monitoring initiatives but serve different user needs,
thematic scopes, and spatial extents. While EUGW’s structure allows for
higher thematic resolution in ecological assessments, HRL VLCC provides
broad-scale monitoring with simplified classifications. This section
highlights their methodological overlaps, structural differences, and
potential synergies.

#### Spatial Coverage

HRL VLCC provides pan-European coverage across all EEA38 countries,
ensuring wall-to-wall consistency. It is particularly suited for
agricultural and land-use assessments at a continental scale. EUGW is
site-specific, focusing on Natura 2000 protected areas, which represent
biodiversity-rich grasslands. Its mapping is optimized for Article 17
reporting under the EU Habitats Directive.

#### Thematic Focus

HRL VLCC primarily integrates:

- Binary grassland classification (permanent vs. temporary)
- Grassland change mapping (gain/loss)
- Mowing and ploughing indicators
- Confidence layers assessing classification reliability.

EUGW, on the other hand, goes much further in biophysical
differentiation, offering:

- Grassland type classification based on EUNIS habitat categories (dry,
  mesic, wet, alpine, salt steppes, sparsely wooded, and forest
  clearings)
- Grassland management layers, detailing mowing, grazing occurrence, and
  ploughing trends. Like mowing and ploughing, grazing is inferred from
  the development of biomass over the year reflected by spectral
  indices. Due to the difficulty of distinguishing grazing in areas with
  low productivity in late summer (e.g. mediterranean) grazing can only
  be partially captured and is not provided as dedicated layer but
  rather incorporated into the “management events” layer.
- Grassland productivity layers, including e.g. short-term and long-term
  productivity trends

#### Methodological Overlaps

Both HRL VLCC Grassland and EUGW share several methodological principles
in their approach to grassland classification and monitoring. A key
similarity lies in their use of multi-sensor EO data. Both datasets rely
on Sentinel-1 SAR for backscatter analysis and Sentinel-2 optical
imagery for NDVI-based classification. However, EUGW expands its
historical depth by incorporating Landsat imagery (1994-2015), enabling
long-term trend analysis, whereas HRL VLCC focuses primarily on more
recent Sentinel-era observations (2017-2021).

Temporal harmonization is another critical aspect where both datasets
ensure consistency over time. HRL VLCC emphasizes short-term
consistency, aligning with previous HRL Grassland products from 2015 and
2018 to maintain classification stability across recent years. In
contrast, EUGW offers a fully structured 30-year time series
(1994–2024), employing explicit temporal harmonization techniques to
minimize classification inconsistencies that could arise due to sensor
transitions and methodological updates.

Both initiatives utilize machine learning-based classification
techniques, integrating optical and SAR composites to refine land cover
and management event detection. HRL VLCC employs Base Vegetation Layers
(BVLs) as annual composites, ensuring stability and consistency through
the years in grassland classification. Meanwhile, EUGW applies advanced
time-series modelling, incorporating phenology metrics and vegetation
dynamics to enhance the accuracy of grassland type and management
intensity assessments. These approaches allow HRL VLCC to maintain
consistency in agricultural monitoring, while EUGW provides a richer
ecological perspective through dynamic trend analysis.

#### Product-Level Differences

<div class="tbl-caption">

Table 7 The key characteristics of both initiatives.

</div>

| Parameter | CLMS HRL VLCC Grassland | EU Grassland Watch |
|----|----|----|
| Coverage Area | Pan-European (38 EEA member and cooperating countries) | Pan-European, focusing on Natura 2000 sites (\> 16430 sites) and biodiversity hotspots |
| Reference Years | 2017-2021 | 1994 to present, split into pre-Sentinel (1994-2015) and Sentinel eras (\>2016) |
| Spatial Resolution | 10m for primary products; 20m for some other products | 10m for recent years (2016 onwards), 30m for earlier years (1994-2015) |
| Grassland Typology | Binary classification (grassland/non-grassland) | EUNIS level 2-based habitat mapping |
| Projection | ETRS89 LAEA for mainland Europe | ETRS89 LAEA for mainland Europe |
| Main Products | Including 11 different products/indicators, e.g. Grassland Mask (GRA), Herbaceous Cover (HER), Grassland Change Layer (GRAC), Grassland Mowing Events (GRAME), Grassland Confidence Layer (GRACL), Ploughing Indicator (PLOUGH) | Including 38 different products/indicators, e.g. Grassland Type Layer, Management Intensity Layer, Productivity Metrics, Bare Soil Occurrence, each component contains different products. Selected main products will be available on web-tool for direct view, while more advanced expert products will be available for download. |
| Primary Data Sources | Sentinel-1 (radar), Sentinel-2 (optical) | Sentinel-1, Sentinel-2, Landsat, EU-DEM data, SAR backscatter data |
| In Situ Data Usage | Limited reliance on in situ data, primarily satellite-based | Extensive use of national inventories and European databases for validation |
| Processing Methodology | Multi-temporal classification based on annual Base Vegetation Layers (BVLs). The process includes data calibration using Copernicus products (HRL Grassland 2018, CLC 2018) and visually interpreted sample points | Machine learning classification, NDVI profile analysis, SAR backscatter indices, temporal harmonization |
| Classification Criteria | Grasslands are classified based on vegetation cover exceeding thresholds of NDVI, distinguishing between permanent and temporary grasslands. Fodder crops, such as seeded grassland, are included if they dominate the land cover | Grasslands are characterised based on vegetation types, management practices, and productivity indicators. There is no a-priori thematic grassland classification. |
| Thematic Layers | Thematic layers provide insights into grassland coverage, grassland changes, mowing events, and ploughing activities. Confidence layers assess classification reliability | Includes grassland coverage, management events (mowing, grazing, ploughing), and productivity trends |
| Change Detection | Grassland Change Layer (GRAC) tracks the gain or loss of grassland areas between 2018 and 2021. Ploughing Indicator (PLOUGH) detects ploughing events over a six-year period | Tracks mowing and ploughing events, productivity changes over time, and bare soil occurrences, short- and long-term productivity trends |
| Accuracy and Validation | Target thematic accuracy is 85% at the biogeographical region level. Validation is primarily internal, with reference points and polygons annotated for grassland and non-grassland classification | Prototype site validations and consistency checks across different years and regions |
| Potential Use Cases | Environmental monitoring, policy reporting (e.g., CAP), biodiversity assessments, tracking agricultural management practices such as mowing and ploughing | Environmental monitoring, biodiversity assessments, CAP policy reporting, agricultural management tracking |
| Exclusions | Areas dominated by shrubs, lichen, mosses, or wetlands with herbaceous species are not included in the HRL VLCC Grassland portfolio | Excludes areas with less than 30% herbaceous cover or dominated by non-graminoid species |

#### Cross-Compatibility with CLMS Products

EUGW is designed for optimal cross-comparability with CLMS and,
therefore, will include an aggregated grassland mask, ensuring direct
overlap between EUGW permanent herbaceous areas, CLC-BB permanent
herbaceous, HRL-GRA, and VLCC GRA (Figure 7).

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-44a29bf6eb06793ebb71610d38d615fb.png"
data-fig-alt="This diagram illustrates a grassland mask aggregation workflow combining data from four distinct sources into a single aggregated product. The process involves four input grassland masks: EUGW (EU Grassland Watch), CLC-BB (CORINE Land Cover Grassland Baseline Backfill), HRL-GRA (High Resolution Layer Grassland), and VLCC-GRA (Very High Resolution Land Cover and Change Grassland). Each input mask is visually represented by a distinct map showing grassland areas (coloured) against a grey background (non-grassland). These four masks are combined to produce an &#39;AGGR&#39; (Aggregated Grassland Mask), which is visually represented as a composite map with varying shades of yellow and green, indicating different aggregation codes. The aggregation process is supported by two tables: **Table A: Grassland mask aggregation** This table specifies the particular product versions used for each input mask across different reference years (2016–2023): | YEAR | EUGW | CLC-BB | HRL | VLCC | |---|---|---|---|---| | 2016 | EUGW 2016 | | HRL-GRA 2015 | VLCC-GRA 2017 | | 2017 | EUGW 2017 | | HRL-GRA 2015 | VLCC-GRA 2017 | | 2018 | EUGW 2018 | CLC-BB 2018 | HRL-GRA 2018 | VLCC-GRA 2018 | | 2019 | EUGW 2019 | | HRL-GRA 2018 | VLCC-GRA 2019 | | 2020 | EUGW 2020 | | HRL-GRA 2018 | VLCC-GRA 2020 | | 2021 | EUGW 2021 | CLC-BB 2021 | HRL-GRA 2018 | VLCC-GRA 2021 | | 2022 | EUGW 2022 | | HRL-GRA 2018 | | | 2023 | EUGW 2023 | | HRL-GRA 2018 | | Empty cells indicate no specific product from that source is used for that year in the aggregation. **Table B: Aggregated grassland mask coding** This table defines how binary (0 or 1, representing absence or presence of grassland) values from the four input masks are combined to generate the final &#39;AGGR&#39; code (0–15): | EUGW | CLC-BB | HRL-GRA | VLCC-GRA | AGGR | |---|---|---|---|---| | 0 | 0 | 0 | 0 | 0 | | 1 | 0 | 0 | 0 | 1 | | 0 | 1 | 0 | 0 | 2 | | 0 | 0 | 1 | 0 | 3 | | 0 | 0 | 0 | 1 | 4 | | 1 | 1 | 0 | 0 | 5 | | 1 | 0 | 1 | 0 | 6 | | 1 | 0 | 0 | 1 | 7 | | 0 | 1 | 1 | 0 | 8 | | 0 | 1 | 0 | 1 | 9 | | 0 | 0 | 1 | 1 | 10 | | 1 | 1 | 1 | 0 | 11 | | 1 | 1 | 0 | 1 | 12 | | 1 | 0 | 1 | 1 | 13 | | 1 | 1 | 1 | 0 | 14 | | 1 | 1 | 1 | 1 | 15 | Each row represents a unique combination of input mask statuses, which is assigned a distinct AGGR code. Code 0 indicates no input mask identifies grassland, while code 15 indicates all four input masks identify grassland."
alt="Figure 7 Aggregated grassland mask produced by EUGW to ensure cross comparability with existing CLMS products, including VLCC Grassland (Source: Jan Mišurec GISAT / EUGW internal communication)" />

This diagram illustrates a grassland mask aggregation workflow combining
data from four distinct sources into a single aggregated product. The
process involves four input grassland masks: EUGW (EU Grassland Watch),
CLC-BB (CORINE Land Cover Grassland Baseline Backfill), HRL-GRA (High
Resolution Layer Grassland), and VLCC-GRA (Very High Resolution Land
Cover and Change Grassland). Each input mask is visually represented by
a distinct map showing grassland areas (coloured) against a grey
background (non-grassland). These four masks are combined to produce an
‘AGGR’ (Aggregated Grassland Mask), which is visually represented as a
composite map with varying shades of yellow and green, indicating
different aggregation codes.

The aggregation process is supported by two tables:

**Table A: Grassland mask aggregation** This table specifies the
particular product versions used for each input mask across different
reference years (2016–2023): \| YEAR \| EUGW \| CLC-BB \| HRL \| VLCC \|
\|—\|—\|—\|—\|—\| \| 2016 \| EUGW 2016 \| \| HRL-GRA 2015 \| VLCC-GRA
2017 \| \| 2017 \| EUGW 2017 \| \| HRL-GRA 2015 \| VLCC-GRA 2017 \| \|
2018 \| EUGW 2018 \| CLC-BB 2018 \| HRL-GRA 2018 \| VLCC-GRA 2018 \| \|
2019 \| EUGW 2019 \| \| HRL-GRA 2018 \| VLCC-GRA 2019 \| \| 2020 \| EUGW
2020 \| \| HRL-GRA 2018 \| VLCC-GRA 2020 \| \| 2021 \| EUGW 2021 \|
CLC-BB 2021 \| HRL-GRA 2018 \| VLCC-GRA 2021 \| \| 2022 \| EUGW 2022 \|
\| HRL-GRA 2018 \| \| \| 2023 \| EUGW 2023 \| \| HRL-GRA 2018 \| \|
Empty cells indicate no specific product from that source is used for
that year in the aggregation.

**Table B: Aggregated grassland mask coding** This table defines how
binary (0 or 1, representing absence or presence of grassland) values
from the four input masks are combined to generate the final ‘AGGR’ code
(0–15): \| EUGW \| CLC-BB \| HRL-GRA \| VLCC-GRA \| AGGR \|
\|—\|—\|—\|—\|—\| \| 0 \| 0 \| 0 \| 0 \| 0 \| \| 1 \| 0 \| 0 \| 0 \| 1
\| \| 0 \| 1 \| 0 \| 0 \| 2 \| \| 0 \| 0 \| 1 \| 0 \| 3 \| \| 0 \| 0 \|
0 \| 1 \| 4 \| \| 1 \| 1 \| 0 \| 0 \| 5 \| \| 1 \| 0 \| 1 \| 0 \| 6 \|
\| 1 \| 0 \| 0 \| 1 \| 7 \| \| 0 \| 1 \| 1 \| 0 \| 8 \| \| 0 \| 1 \| 0
\| 1 \| 9 \| \| 0 \| 0 \| 1 \| 1 \| 10 \| \| 1 \| 1 \| 1 \| 0 \| 11 \|
\| 1 \| 1 \| 0 \| 1 \| 12 \| \| 1 \| 0 \| 1 \| 1 \| 13 \| \| 1 \| 1 \| 1
\| 0 \| 14 \| \| 1 \| 1 \| 1 \| 1 \| 15 \| Each row represents a unique
combination of input mask statuses, which is assigned a distinct AGGR
code. Code 0 indicates no input mask identifies grassland, while code 15
indicates all four input masks identify grassland.

#### Grazing Detection – A Common Challenge

One of the main limitations of both HRL VLCC and EUGW is their lack of
capability to accurately and extensively map grazing activity. While
EUGW incorporates grazing intensity within its grassland management
component, the publication of a dedicated grazing pressure layer remains
under discussion (Status: 03/2025).

Distinguishing grazed from non-grazed areas using remote sensing alone
presents several challenges. One of the primary limitations is the
scarcity and coarse resolution of in-situ reference data, which makes it
difficult to train reliable classifiers for grazing detection.
Additionally, seasonal biomass variations complicate the differentiation
between grazing and mowing, as both activities can result in similar
spectral and structural changes in vegetation indices. This issue is
particularly problematic in non-intensively grazed semi-natural areas,
where biomass regrowth varies significantly across different ecosystems
and years.

To improve grazing detection capabilities, additional supplementary
datasets such as livestock density maps, climate factors, and local
grazing records. These external data sources could help discriminate
grazing impacts from other land management activities, providing a more
robust basis for mapping grazing pressure within both HRL VLCC and EUGW.
A recent example of efforts in this direction has been provided by Malek
et al. (2024), emphasizing the need for non-Earth Observation (non-EO)
reference data to enhance grazing classification.

### Potential and recommendations

The development of EUGW has been aligned with HRL VLCC and other CLMS
products, ensuring a high degree of transferability and
cross-comparability. Due to its modular structure, EUGW is designed to
be flexible and adaptable, allowing for integration with existing land
monitoring datasets and potential future expansions. This modular
approach ensures that EUGW remains compatible with HRL VLCC broad-scale
agricultural applications while providing finer ecological granularity
for biodiversity assessments within Natura 2000 sites.

One of the most critical gaps in grassland monitoring is the lack of a
dedicated grazing pressure product within both HRL VLCC and EUGW. While
EUGW incorporates grazing intensity indicators within its management
characterization component, the publication of a standalone grazing
detection layer remains pending. The absence of high-resolution in-situ
reference data makes the systematic identification of grazed areas
challenging from remote sensing data, limiting the effectiveness of
machine-learning-based classification approaches. Additionally, biomass
variability across ecosystems and seasons further complicates the
differentiation between grazing and mowing events, leading to
uncertainties in classification.

To address this issue, additional initiatives might be needed to foster
the development of harmonized grazing reference databases. A notable
example of such an initiative is the Global Biodiversity Information
Facility (GBIF), which provides a centralized API-based database for
species presence data. A similar approach could be applied to grazing
pressure, where a comprehensive reference database for livestock
stocking density at higher spatial resolutions would significantly
enhance the accuracy of grassland management assessments. Such an
activity has been launchen by the Land Management for Sustainability
(LAMASUS) project[^8] which has developed a Picture Pile app to classify
and collect information on grazing. This type of dataset would support
remote sensing-based grazing monitoring, enabling both HRL VLCC and EUGW
to improve their classification of grassland use intensity. Grazing
information cannot only be derived from in-situ data but may also be
derived punctually from the analysis of image data from webcams (Weber
et al. 2023).

Another area for potential enhancement is grassland productivity
assessment. EUGW includes detailed short-term (GSTP) and long-term
(GLTP) productivity indicators, providing insights into grassland health
trends over time. HRL VLCC currently lacks dedicated productivity
layers, relying instead on mowing frequency as a simplified proxy for
productivity monitoring. Future iterations of HRL VLCC could benefit
from adopting EUGW’s productivity trend methodology, allowing for a more
refined assessment of biomass dynamics and long-term ecosystem
sustainability.

Given the increasing role of agricultural-related datasets in
environmental and agricultural policy monitoring, HRL VLCC and EUGW
should continue to enhance their interoperability. EUGW already ensures
alignment with CLC Backbone, HRL Grassland, and VLCC Grassland, enabling
direct comparability between datasets. HRL VLCC could further benefit
from incorporating EUGW’s aggregated grassland mask, ensuring consistent
cross-product analysis and enhanced usability for CAP compliance and
biodiversity monitoring. By addressing these gaps and opportunities, HRL
VLCC can provide an even more robust foundation for grassland
monitoring, agricultural assessments, and biodiversity conservation
across Europe.

# Collection of user requirements and literature review of additional forest Types

## Literature review

This review investigates possible alternative classifications on forest
types and their connection to the EEA forest typology (European
Environment Agency 2007) as well as the forest type needs for Member
States under different regulation systems, such as the Ecosystem
accounting regulation and the LULUCF.

### EEA Classification on European Forest type

The EEA European Forest Type (EFT) system consists of 14 main
categories, which are further divided into 78 types (Table 8). A study
by Pividori et al. 2016 constructed a matrix where the presence of key
tree and shrub species per forest type are represented, based on the EEA
forest typology report. In this matrix, tree and shrub species are
separated into three main groups: Conifers, Broadleaved, and Alien
trees. Additionally, the species presence is categorized into three
categories:

the species is abundant and dominant in the EFT the species presence in
the EFT is either secondary or predominant but in peculiar and not
characteristic ecological conditions of the EFT the presence in the EFT
is both dominant and secondary in some cases

The EFT defines categories 4-8 (European Environment Agency 2007, table
6.1) as the section for broadleaved deciduous and mixed
coniferous-broadleaved forest. However, after analysing the presence of
key tree and shrub species per forest type within each category, it
became evident that only category 7 (Mountainous beech forest)
represents a real mixed class. This category is characterized by
mountainous vegetation belt coniferous species (Spruce, Fir) that become
competitive with deciduous species (Beech).

<div class="tbl-caption">

Table 8 European Forest Type (EFT) system categorization

</div>

<table data-quarto-postprocess="true">
<colgroup>
<col style="width: 60%" />
<col style="width: 39%" />
</colgroup>
<tbody>
<tr>
<td><strong>Category</strong></td>
<td><strong>Forest Type</strong></td>
</tr>
<tr>
<td rowspan="2" style="vertical-align: middle">1. Boreal forest</td>
<td>1.1 Spruce and sprucebirch boreal forest</td>
</tr>
<tr>
<td>1.2 Pine and pinebirch boreal forest</td>
</tr>
<tr>
<td rowspan="6" style="vertical-align: middle">2. Hemiboreal forest and
nemoral coniferous and mixed broadleavedconiferous forest</td>
<td>2.1 Hemiboreal forest</td>
</tr>
<tr>
<td>2.2 Nemoral Scots pine forest</td>
</tr>
<tr>
<td>2.3 Nemoral spruce forest</td>
</tr>
<tr>
<td>2.4 Nemoral Black pine forest</td>
</tr>
<tr>
<td>2.5 Mixed Scots pinebirch forest</td>
</tr>
<tr>
<td>2.6 Mixed Scots pinepedunculate oak forest</td>
</tr>
<tr>
<td rowspan="3" style="vertical-align: middle">3. Alpine coniferous
forest</td>
<td>3.1 Subalpine larch-arolla pine and dwarf pine forest</td>
</tr>
<tr>
<td>3.2 Subalpine and mountainous spruce and mountainous mixed
sprucesilver fir forest</td>
</tr>
<tr>
<td>3.3 Alpine Scots pine and Black pine forest</td>
</tr>
<tr>
<td rowspan="2" style="vertical-align: middle">4. Acidophilous oak and
oakbirch forest</td>
<td>4.1 Acidophilous oakwood</td>
</tr>
<tr>
<td>4.2 Oakbirch forest</td>
</tr>
<tr>
<td rowspan="9" style="vertical-align: middle">5. Mesophytic deciduous
forest</td>
<td>5.1 Pedunculate oak-hornbeam forest</td>
</tr>
<tr>
<td>5.2 Sessile oak-hornbeam forest</td>
</tr>
<tr>
<td>5.3 Ashwood and oakash forest</td>
</tr>
<tr>
<td>5.4 Mapleoak forest</td>
</tr>
<tr>
<td>5.5 Limeoak forest</td>
</tr>
<tr>
<td>5.6 Maplelime forest</td>
</tr>
<tr>
<td>5.7 Lime forest</td>
</tr>
<tr>
<td>5.8 Ravine and slope forest</td>
</tr>
<tr>
<td>5.9 Other mesophytic deciduous forests</td>
</tr>
<tr>
<td rowspan="7" style="vertical-align: middle">6. Beech forest</td>
<td>6.1 Lowland beech forest of southern Scandinavia and north central
Europe</td>
</tr>
<tr>
<td>6.2 Atlantic and subatlantic lowland beech forest</td>
</tr>
<tr>
<td>6.3 Subatlantic submountainous beech forest</td>
</tr>
<tr>
<td>6.4 Central European submountainous beech forest</td>
</tr>
<tr>
<td>6.5 Carpathian submountainous beech forest</td>
</tr>
<tr>
<td>6.6 Illyrian submountainous beech forest</td>
</tr>
<tr>
<td>6.7 Moesian submountainous beech forest</td>
</tr>
<tr>
<td rowspan="8" style="vertical-align: middle">7. Mountainous beech
forest</td>
<td>7.1 South western European mountainous beech forest (Cantabrians,
Pyrenees, central Massif, south western Alps)</td>
</tr>
<tr>
<td>7.2 Central European mountainous beech forest</td>
</tr>
<tr>
<td>7.3 ApennineCorsican mountainous beech forest</td>
</tr>
<tr>
<td>7.4 Illyrian mountainous beech forest</td>
</tr>
<tr>
<td>7.5 Carpathian mountainous beech forest</td>
</tr>
<tr>
<td>7.6 Moesian mountainous beech forest</td>
</tr>
<tr>
<td>7.7 Crimean mountainous beech forest</td>
</tr>
<tr>
<td>7.8 Oriental beech and hornbeamoriental beech forest</td>
</tr>
<tr>
<td rowspan="8" style="vertical-align: middle">8. Thermophilous
deciduous forest</td>
<td>8.1 Downy oak forest</td>
</tr>
<tr>
<td>8.2 Turkey oak, Hungarian oak and Sessile oak forest</td>
</tr>
<tr>
<td>8.3 Pyrenean oak forest</td>
</tr>
<tr>
<td>8.4 Portuguese oak and Mirbeck's oak Iberian forest</td>
</tr>
<tr>
<td>8.5 Macedonian oak forest</td>
</tr>
<tr>
<td>8.6 Valonia oak forest</td>
</tr>
<tr>
<td>8.7 Chestnut forest</td>
</tr>
<tr>
<td>8.8 Other thermophilous deciduous forests</td>
</tr>
<tr>
<td rowspan="5" style="vertical-align: middle">9. Broadleaved evergreen
forest</td>
<td>9.1 Mediterranean evergreen oak forest</td>
</tr>
<tr>
<td>9.2 Olivecarob forest</td>
</tr>
<tr>
<td>9.3 Palm groves</td>
</tr>
<tr>
<td>9.4 Macaronesian laurisilva</td>
</tr>
<tr>
<td>9.5 Other sclerophlyllous forests</td>
</tr>
<tr>
<td rowspan="11" style="vertical-align: middle">10. Coniferous forests
of the Mediterranean, Anatolian and Macaronesian regions</td>
<td>10.1 Mediterranean pine forest</td>
</tr>
<tr>
<td>10.2 Mediterranean and Anatolian Black pine forest</td>
</tr>
<tr>
<td>10.3 Canarian pine forest</td>
</tr>
<tr>
<td>10.4 Mediterranean and Anatolian Scots pine forest</td>
</tr>
<tr>
<td>10.5 AltiMediterranean pine forest</td>
</tr>
<tr>
<td>10.6 Mediterranean and Anatolian fir forest</td>
</tr>
<tr>
<td>10.7 Juniper forest</td>
</tr>
<tr>
<td>10.8 Cypress forest</td>
</tr>
<tr>
<td>10.9 Cedar forest</td>
</tr>
<tr>
<td>10.10 Tetraclinis articulata stands</td>
</tr>
<tr>
<td>10.11 Mediterranean yew stands</td>
</tr>
<tr>
<td rowspan="5" style="vertical-align: middle">11. Mire and swamp
forest</td>
<td>11.1 Conifer dominated or mixed mire forest</td>
</tr>
<tr>
<td>11.2 Alder swamp forest</td>
</tr>
<tr>
<td>11.3 Birch swamp forest</td>
</tr>
<tr>
<td>11.4 Pedunculate oak swamp forest</td>
</tr>
<tr>
<td>11.5 Aspen swamp forest</td>
</tr>
<tr>
<td rowspan="3" style="vertical-align: middle">12. Floodplain
forest</td>
<td>12.1 Riparian forest</td>
</tr>
<tr>
<td>12.2 Fluvial forest</td>
</tr>
<tr>
<td>12.3 Mediterranean and Macaronesian riparian forest</td>
</tr>
<tr>
<td rowspan="5" style="vertical-align: middle">13. Non riverine alder,
birch, or aspen forest</td>
<td>13.1 Alder forest</td>
</tr>
<tr>
<td>13.2 Italian alder forest</td>
</tr>
<tr>
<td>13.3 Boreal birch forest</td>
</tr>
<tr>
<td>13.4 Southern boreal birch forest</td>
</tr>
<tr>
<td>13,5 Aspen forest</td>
</tr>
<tr>
<td rowspan="2" style="vertical-align: middle">14. Plantations and
self-sown exotic forest</td>
<td>14.1 Plantations of sitenative species</td>
</tr>
<tr>
<td>14.2 Plantations of not site native species and selfsown exotic
forest</td>
</tr>
</tbody>
</table>

We compared how the 14 main EFT categories align with the current Corine
Land Cover (CLC) classes which represent Forest cover (Table 9). There
is a match between some of the CLC classes and the EFT categories,
including Broad-leaved, Coniferous and Mixed Forest. However, CLC does
not provide sufficient information to match the different EFT
categories. It also does not provide a distinction between evergreen and
deciduous forests and is missing a class for transitional
woodland/shrub. Finally, plantations are considered within other CLC
classes.

Among the EFT categories, the category 11. Mire and swamp forest is
worth mentioning as it can be divided into coniferous and broadleaved
types based on forest types which compose it: Coniferous: 11.1 Conifer
dominated or mixed mire forest (Spruce mire, Pine mire)) and
Broadleaved: 11.2 Alder swamp forest; 11.3 Birch swamp forest; 11.4
Pedunculate oak swamp forest; 11.5 Aspen swamp forest.

<div class="tbl-caption">

Table 9 Alignment of EFT categories with the current Corine Land Cover
(CLC) classes

</div>

<table style="width:100%;" data-quarto-postprocess="true">
<colgroup>
<col style="width: 34%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr>
<td colspan="3"><strong>Corine Land Cover</strong></td>
<td><strong>EEA European Forest Typology</strong></td>
</tr>
<tr>
<td><strong>Level 2</strong></td>
<td><strong>Level 3</strong></td>
<td><strong>Description</strong></td>
<td><strong>Category</strong></td>
</tr>
<tr>
<td rowspan="15" style="vertical-align: middle">3.1 Forest</td>
<td rowspan="8" style="vertical-align: middle">3.1.1 Broad-leaved
Forest</td>
<td rowspan="8" style="vertical-align: middle">Vegetation formation
composed principally of trees, including shrub and bush understorey,
where broad-leaved species predominate.</td>
<td style="background-color: #d9ead3">4. Acidophilous oak and oak birch
forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">5. Mesophytic deciduous
forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">6. Beech forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">8. Thermophilous deciduous
forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">9. Broadleaved evergreen
forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">11. Mire and swamp forest
(11.2-11.5)</td>
</tr>
<tr>
<td style="background-color: #d9ead3">12. Floodplain forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">13. Non riverine alder, birch, or
aspen forest</td>
</tr>
<tr>
<td rowspan="5" style="vertical-align: middle">3.1.2 Coniferous
Forest</td>
<td rowspan="5" style="vertical-align: middle">Vegetation formation
composed principally of trees, including shrub and bush understorey,
where coniferous species predominate.</td>
<td style="background-color: #b6d7a8">1. Boreal forest</td>
</tr>
<tr>
<td style="background-color: #b6d7a8">2. Hemiboreal forest and nemoral
coniferous and mixed broadleaved-coniferous forest</td>
</tr>
<tr>
<td style="background-color: #b6d7a8">3. Alpine coniferous forest</td>
</tr>
<tr>
<td style="background-color: #b6d7a8">10. Coniferous forests of the
Mediterranean, Anatolian and Macronesian regions</td>
</tr>
<tr>
<td style="background-color: #b6d7a8">11. Mire and swamp forest
(11.1)</td>
</tr>
<tr>
<td style="vertical-align: middle">3.1.3 Mixed Forest</td>
<td style="vertical-align: middle">Vegetation formation composed
principally of trees, including shrub and bush understorey, where
neither broad-leaved nor coniferous species predominate.</td>
<td>7. Mountainous beech forest</td>
</tr>
<tr>
<td style="vertical-align: middle">3.2 Shrub and/or herbaceous
vegetation associations</td>
<td style="vertical-align: middle">3.2.4 Transitional
woodland/shrub</td>
<td style="vertical-align: middle">Transitional bushy and herbaceous
vegetation with occasional scattered trees. Can represent woodland
degradation, forest regeneration / recolonization or natural
succession</td>
</tr>
<tr>
<td colspan="3">Within other CLC classes</td>
<td>14. Plantations and self-sown exotic forest</td>
</tr>
</tbody>
</table>

### Eu ecosystem typology

We also compared the EU Ecosystem Typology (ET) classification (at Level
2) with the 14 EFT categories (Table 10). In comparison to CLC, the ET
classification includes 2 additional classes that better align with the
EFT categories: Broadleaved evergreen and Plantation. However, ET is
also missing a class for transitional woodland/shrub and does not
provide sufficient information to match the different EFT categories.

<div class="tbl-caption">

Table 10 Comparison between EFT and EU Ecosystem typology classes

</div>

<table style="width:100%;" data-quarto-postprocess="true">
<colgroup>
<col style="width: 34%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr>
<td colspan="3"><strong>EU Ecosystem Typology</strong></td>
<td><strong>EEA European Forest Typology</strong></td>
</tr>
<tr>
<td><strong>Level 1</strong></td>
<td><strong>Level 2</strong></td>
<td><strong>Description</strong></td>
<td><strong>Category</strong></td>
</tr>
<tr>
<td rowspan="16" style="vertical-align: middle">4. Forest and
woodlands</td>
<td rowspan="6" style="vertical-align: middle">4.1 Broadleaved deciduous
forests</td>
<td rowspan="6" style="vertical-align: middle">Woodlands and forests
dominated by summer-green non-coniferous trees that lose their leaves in
winter. Includes woodland with mixed evergreen and deciduous broadleaved
trees, provided that the deciduous cover exceeds that of evergreens. The
proportion of conifers should not exceed 25%.</td>
<td style="background-color: #d9ead3">4. Acidophilous oak and oak birch
forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">5. Mesophytic deciduous
forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">6. Beech forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">8. Thermophilous deciduous
forest</td>
</tr>
<tr>
<td style="background-color: #d9ead3">11. Mire and swamp forest
(11.2-11.5)</td>
</tr>
<tr>
<td style="background-color: #d9ead3">12. Floodplain forest</td>
</tr>
<tr>
<td rowspan="6" style="vertical-align: middle">4.2 Coniferous
forests</td>
<td rowspan="6" style="vertical-align: middle">Vegetation formation
composed principally of trees, including shrub and bush understory,
where coniferous species predominate. The proportion of deciduous trees
should not exceed 25%.</td>
<td style="background-color: #d9ead3">13. Non riverine alder, birch, or
aspen forest</td>
</tr>
<tr>
<td style="background-color: #b6d7a8">1. Boreal forest</td>
</tr>
<tr>
<td style="background-color: #b6d7a8">2. Hemiboreal forest and nemoral
coniferous and mixed broadleaved-coniferous forest</td>
</tr>
<tr>
<td style="background-color: #b6d7a8">3. Alpine coniferous forest</td>
</tr>
<tr>
<td style="background-color: #b6d7a8">10. Coniferous forests of the
Mediterranean, Anatolian and Macronesian regions</td>
</tr>
<tr>
<td style="background-color: #b6d7a8">11. Mire and swamp forest
(11.1)</td>
</tr>
<tr>
<td style="vertical-align: middle">4.3 Broadleaved evergreen
forests</td>
<td style="vertical-align: middle">Forests dominated by broadleaved
sclerophyllous or lauriphyllous evergreen trees, or by palms. They are
characteristic of the Mediterranean and warm-temperate humid zones.</td>
<td style="background-color: #d9ead3">9. Broadleaved evergreen
forest</td>
</tr>
<tr>
<td style="vertical-align: middle">4.4 Mixed forests</td>
<td style="vertical-align: middle">Vegetation formation composed
principally of trees, including shrub and bush understorey, where
neither broadleaved nor coniferous species strongly predominate (i.e.
&lt;75% deciduous and &lt;75% coniferous trees).</td>
<td>7. Mountainous beech forest</td>
</tr>
<tr>
<td style="vertical-align: middle">4.5 Transitional Forest and Woodland
shrub</td>
<td style="vertical-align: middle">Transitional forests and woodland
shrub. Includes vegetation that is always shrubland and areas of
temporarily cleared forest (as part of forest management).</td>
<td>Within other EFT classes</td>
</tr>
<tr>
<td style="vertical-align: middle">4.6 Plantations</td>
<td style="vertical-align: middle">Monoculture plantations or
plantations strongly dominated by one or few species of non-European
coniferous and broadleaved trees with very sparse or lacking
undergrowth, e.g. eucalyptus plantations. Forest stands of single or
mixed species consisting of native and/or non-native trees species that
have long been established in European ecosystems and have diverse
undergrowth typical for forest ecosystems should be classified as part
of types 4.1 to 4.4. If not possible to distinguish plantations, these
areas should be attributed to the classes 4.1 - 4.4.</td>
<td>14. Plantations and self-sown exotic forest</td>
</tr>
</tbody>
</table>

Delving into Level 3 of the ET classification, we find a more elaborate
distinction of the Mixed Forest class (4.4). There is differentiation
made between Mixed forests dominated by coniferous species (4.4.1),
Mixed forests dominated by broadleaved species (4.4.2) and other mixed
forests including stands of non-native trees species that have long been
established in European forest mixes (4.4.3).

Taking these distinctions into account, we might consider adding more
categories besides category 7 (Mountainous Beech Forest) to the Mixed
Forest class. The following categories show a combination of deciduous
and coniferous species that are either dominant or both dominant and
secondary in some cases, according to the European Forest Types: tree
species matrix (Pividori et al. 2016):

1 Boreal forest 2 Hemiboreal forest and nemoral coniferous and mixed
broadleaved-coniferous forest 8 Thermophilous deciduous forest 10
Coniferous forests of the Mediterranean, Anatolian and Macronesian
regions

Additionally, when looking into Level 3 of the ET classification, we
noticed that there are two classes (one for Coniferous and one for
Broadleaved evergreen) are missing in the EEA classification of European
Forest Types:

- Taiga forests (4.2.7)
- Mainland laurophyllous forests (4.3.2)

### Forest category for LULUCF reporting

To understand which forest type categories are being reported by Member
States, we analysed the Member States’ LULUCF data from 2019 (as part of
Task 1.4.4.1 – Support to LULUCF). We summarized the forest type
categories reported by the 28 Member States and derived the following
insights:

<div class="tbl-caption">

Table 11 Stratification reported by Member States

</div>

| Stratification forest types | № | Countries |
|----|----|----|
| No further stratification | 11 | Belgium, Germany, Denmark, Italy, Greece, Luxembourg, Malta, Netherlands, Poland, Sweden, United Kingdom |
| Further stratification | 17 | Austria, Bulgaria, Cyprus, Czechia, Estonia, Spain, Finland, France, Croatia, Hungary, Ireland, Italy, Lithuania, Latvia, Portugal, Romania, Slovenia, Slovakia |

Among the Member States that provided further stratification beyond the
general “forest” category, some reported broader classes (e.g.,
Broadleaved, Coniferous), others reported at species level, and some a
combination of both. Below is an overview of the 12 countries that
reported broader classes:

<div class="tbl-caption">

Table 12 Forest classes reported by Member States

</div>

| Reported class | № | Member States |
|----|----|----|
| Broadleaved deciduous | 10 | Austria, Bulgaria, Cyprus, Spain, Finland, France, Croatia, Ireland, Lithuania, Slovenia |
| Coniferous | 11 | Austria, Bulgaria, Cyprus, Spain, France, Croatia, Hungary, Ireland, Lithuania, Romania, Slovenia |
| Broadleaved evergreen | 0 |  |
| Mixed | 3 | Spain, France, Ireland |
| Transitional Forest and Woodland shrub | 0 |  |
| Plantations | 1 | Italy |
| Shrubs | 2 | Spain, Croatia |

There were also 12 countries that provided species-level information,
some in combination with broader classes.

<div class="tbl-caption">

Table 13 Species reported by Member States, in accordance with the
groups of the European Forest Types: tree species matrix (Pividori et
al. 2016)

</div>

| Group | Species | № | Member States |
|----|----|----|----|
| Broadleaved | Oak (Quercus) | 6 | Czechia, Hungary, Latvia, Romania, Portugal, Slovakia |
|  | Beech (Fagus) | 4 | Czechia, Hungary, Romania, Slovakia |
|  | Poplar (Populus) | 3 | France, Hungary, Slovakia |
|  | Willow (Salix) | 3 | Hungary, Latvia, Slovakia |
|  | Ash (Fraxinus) | 2 | Latvia, Slovakia |
|  | Alder (Alnus) | 2 | Latvia, Slovakia |
|  | Birch (Betula) | 2 | Latvia, Slovakia |
|  | Hornbeam (Carpinus) | 1 | Slovakia |
|  | Maple (Acer) | 1 | Slovakia |
|  | Elm (Ulmus) | 1 | Slovakia |
|  | Linden (Tilia) | 1 | Slovakia |
| Coniferous | Pine (Pinus) | 7 | Czechia, Estonia, Finland, Ireland, Latvia, Portugal, Slovakia |
|  | Spruce (Picea) | 6 | Czechia, Estonia, Finland, Ireland, Latvia, Slovakia |
|  | Fir (Abies) | 1 | Estonia |
|  | Larch (Larix) | 2 | Estonia, Slovakia |
| Alien/Planted | Locust (Robinia) | 2 | Hungary, Slovakia |
|  | Eucalyptus | 1 | Portugal |

### Refining ona proposal on Forest Type extent nomenclature

The initial nomenclature proposal, presented by GAF (Oct 2024)
effectively outlines key species used to delineate the 14 classes of the
EEA European Forest Type classification scheme. Important species for
the major forest types like Broadleaved Deciduous (Fagus, Quercus,
Betula, Alnus, Populus), Broadleaved Evergreen (Quercus, Olea europaea,
Eucalyptus), and Coniferous (Picea, Pinus) are included. When combined
with biogeographical data, specific zones, tree height, and soil types,
these species can help define the 14 categories. For example, the DEM
layer, together with predominantly Evergreen Deciduous species like
Fagus (Beech), can be used to identify Category 6 - Beech Forest.

Additionally, it may be useful to include information on other species,
such as Abies (Fir), Fraxinus (Ash), Salix (Willow), and Populus
(Alder), as these species were frequently reported in LULUCF submissions
by Member States.

### First set of recommendations

- The initial proposal of GAF nomenclature aligns with the 14 EEA
  European Forest Type classes, with major forest types (Broadleaved
  Deciduous, Broadleaved Evergreen, and Coniferous) at Level 1 and key
  species at Level 2.
- There’s no separate Mixed Forest category in the GAF nomenclature,
  though it can be inferred from other classes. Defining Mixed Forest
  requires clarity on species proportions. The Mixed Forest class is
  required in EU module on ecosystem accounting. In the reports analysed
  of LULUCF, only 3 countries report on mixed forest.
- The GAF lacks a Plantations category. While Eucalyptus is included,
  some Member States also mention Populus, which could be considered an
  important species for plantations. Additionally, there are some alien
  species that were mentioned by the Member States (e.g., Robinia,
  Platanus). These species might be taken into consideration, although
  they might be more common in urban areas (parks, street lines, etc.).
  Finally, there is a Transitional Forests and Woodland Shrubs category
  lacking from the current GAF nomenclature.
- LULUCF data shows 16 of 28 Member States report forest stratification,
  with 12 providing species details. Common species are included in the
  GAF, but others like Abies, Fraxinus, Salix, and Populus could be
  added.

# Assessment of Timeseries Consistency of Forest Layers

Meaningful monitoring of natural processes requires consistent
monitoring of individual land cover (and land use) elements. We say that
a time-series is consistent if the difference between the status of any
two reference years corresponds to the changes:

$$Change = New status – Old status$$

Unfortunately, this simple requirement is violated in most currently
available land cover time series because of several practical reasons.
The main objective of this subtask is to analyse how far the consistency
criteria is fulfilled in the currently available CLMS Forest time
series, to explore the reasons of inconsistency, and to make suggestions
for possible improvements.

## Basic concepts and terminology used for tree cover / forest related CLMS products

Available CLMS products provide various time-series of tree cover or
forest related information. However, the terms “forest” and “tree cover”
have different meanings when describing specific Land Cover / Land Use
(LCLU) products.

A forest is an ecosystem characterized by a dense community of trees.
Hundreds of definitions of forest are used throughout the world,
incorporating factors such as tree density, tree height, land use, legal
standing, and ecological function. The United Nations’ Food and
Agriculture Organization (FAO) defines a forest as, “Land spanning more
than 0.5 hectares with trees higher than 5 meters and a canopy cover of
more than 10 percent, or trees able to reach these thresholds in-situ.
It does not include land that is predominantly under agricultural or
urban use” (FAO 2018).

→ In many countries the official term “forest” is used to characterize
area used by forestry, but this may include areas without actual tree
cover after a clear-cut, or e.g. nurseries. → Information about forest
cover is provided by various, typically vector based CLMS products, as
specific thematic classes of Corine Land Cover (CLC) or Priority Area
Monitoring products (PAM).

Tree (canopy) cover is often defined as the “vertical projection of tree
crowns to a horizontal earth’s surface”. This definition is used by many
Earth Observation (EO) based surveys, providing information on a pixel
basis about either:

→ the proportional crown coverage; → binary information about presence /
absence of tree cover; → additional information about leaf type.

<div class="tbl-caption">

Table 14 Forest / tree cover related CLMS products covering entire EEA38
/ EEA38+UK area

</div>

| CLMS survey | Reference dates | Description |
|----|----|----|
| HRL Forest / VLCC Forest | 2012, 2015, 2018, (2018revised, 2019, 2020, 2021) | Raster products (20m/10m resolution): Tree Cover Density (TCD), Dominant Leaf Type (DLT), Forest Type (FTY) |
| CLCplus Backbone | 2018, 2021, (2023) | Raster products (10m resolution) including woody classes: 2: Woody - needle leaved trees; 3: Woody - Broadleaved deciduous trees; 4: Woody - Broadleaved evergreen trees |
| Small Landscape Features | 2018, (2021) | Raster product (5m) providing estimation for total tree cover: <br> 2018: Woody Vegetation Mask + Forest Mask <br> 2021: Woody Vegetation Layer (WVL – production in progress) |
| Corine Land Cover (CLC) | 2000, 2006, 2012, 2018 | Vector (raster) product: Forest classes (311, 312, 313, 324) and other classes with significant tree cover, as 141-Green urban areas; 223-Olive groves; 222-Fruit trees and berry plantations; 243-Land principally occupied by agriculture, with significant areas of natural vegetation; 244-Agro-forestry areas |

## Overview and evolution of main HRL Forest products

HRL Forest layers are the main focus of this analysis. Note, despite of
the name “Forest”, these layers are in character more tree cover than
forest related, considering terminology described in chapter 3.1.

HRL Forest layers include three main product types:

- **Tree Cover Density (TCD)** status product estimates the ratio of the
  rectangular cell area (0-100%) of the vertical projection of tree
  crowns to a horizontal earth’s surface. The product is created from
  the reference year of 2018 in 10m (previously 20m) resolution,
  aggregated in a second step to 100m.
- **Dominant Leaf Type (DLT)** status is a classified product providing
  the separation of broadleaved and coniferous cover for tree covered
  (TCD \> 0 %) areas. The product is created from the reference year of
  2018 in 10m (previously 20m) resolution. Aggregated 100m DLT products
  were created presenting dominant leaf type classes during HRL2015
  update for 2012 and 2015 reference years. From 2018 aggregated 100m
  resolution Broadleaved Cover Density (BCD) and Coniferous Cover
  Density (CCD) layers are provided.
- **Forest Type (FTY)** product is derived from primary TCD and DLT
  data, largely following the FAO forest definition by applying 10% tree
  cover density threshold and 0.5 ha Minimum Mapping Unit (MMU). Urban
  trees and trees under predominantly agricultural use are marked (2012
  & 2015), from 2018 excluded based on the Forest Type Additional
  Support layer (FADSL). Aggregated 100m FTY products are created
  presenting dominant leaf type classes.

The first status product of the HRL Forest time series dates back to the
reference year 2012. The initial three years update period was repeated
with yearly update in case of TCD and DLT products from 2018 in frames
of the new HRL Vegetated Land Cover Component (VLCC) mapping (products
are delivered, but not published yet), FTY status was produced only for
the reference year of 2021 and change layers are still produced to
represent a 3 years period, currently between 2018-2021.

<div class="tbl-caption">

Table 15 Overview of HRL Forest status and change layers

</div>

<table style="width:100%;" data-quarto-postprocess="true">
<colgroup>
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 3%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2" style="vertical-align: middle"><strong>Ref.
year</strong></td>
<td colspan="3"><strong>Status</strong></td>
<td colspan="3"><strong>Change</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Tree Cover Density</strong></td>
<td style="text-align: center;"><strong>Dominant Leaf Type</strong></td>
<td style="text-align: center;"><strong>Forest Type</strong></td>
<td style="text-align: center;"><strong>Tree Cover Density
change</strong></td>
<td style="text-align: center;"><strong>Dominant Leaf Type
change</strong></td>
<td style="text-align: center;"><strong>Forest Type change</strong></td>
</tr>
<tr>
<td style="text-align: center;">2012</td>
<td>TCD2012 20m<br />
TCD2012 100m</td>
<td>DLT2012 20m<br />
DLT2012 100m</td>
<td>FTY2012 20m<br />
FADSL2012 20m<br />
FTY2012 100m</td>
<td rowspan="2" style="vertical-align: middle">TCDC1215 100m*<br />
TCCM1215 20m</td>
<td rowspan="2" style="vertical-align: middle">DLTC1215 20m</td>
<td rowspan="4"
style="text-align: center; vertical-align: middle;">-</td>
</tr>
<tr>
<td style="text-align: center;">2015</td>
<td>TCD2015 20m<br />
TCD2015 100m</td>
<td>DLT2015 20m<br />
DLT2015 100m*<br />
BCD2018 100m<br />
CCD2018 100m</td>
<td>FTY2015 20m<br />
FADSL2015 20m<br />
FTY2015 100m</td>
</tr>
<tr>
<td style="text-align: center;">2018</td>
<td>TCD2018 10m<br />
TCD2018 100m</td>
<td>DLT2018 10m<br />
BCD2018 100m<br />
CCD2018 100m</td>
<td>FTY2018 10m<br />
FADSL2018 10m<br />
FTY2018 100m</td>
<td>TCCM1518 20m</td>
<td>DLTC1518 20m</td>
</tr>
<tr>
<td style="text-align: center;">2018-2021 (VLCC)</td>
<td>TCD20xx 10m<br />
TCD20xx 100m</td>
<td>DLT20xx 10m<br />
BCD20xx 100m<br />
CCD20xx 100m</td>
<td>FTY20yy 10m<br />
FADSL20yy 10m<br />
FTY20yy 100m</td>
<td>TCPC1821 20m</td>
<td>DLTC1821 20m</td>
</tr>
<tr>
<td colspan="7">TCD&amp;DLT (xx): 2018(revised), 2019, 2020, 2021;
FTY(yy): only 2018 (revised) and 2021</td>
</tr>
</tbody>
</table>

## Assessment of the stability of HRL Forest products

The stability of the HRL Forest time-series is influenced by a number of
factors, including:

- The basic concept of mapping and updating the products;
- Changes between individual surveys in:
  - Specification of products (mapping rules, resolution, etc);
  - Mapped Area of Interest (AOI);
  - Input data and in the complex classification methodology;
  - External input (CLC, HRL Imperviousness) used to derive FTY layers;

### Evolution of the specification of individual products

The production of currently available HRL Forest products can be divided
into three eras linked to individual mapping contracts.

#### HRL Forest 2015 (reference years 2015 & 2012)[^9]

The HRL Forest with reference year 2015 (± 1 year) has been fully
produced with one harmonised set of products (no split in different
service elements and geographic lots) by a consortium of
well-established European service providers. For the first time, the
product portfolio included a set of new change products at pan-European
scale. Additionally, the 2015 production included the correction and
re-processing of the historical 2012 HRL Forest products to allow a full
harmonisation across Europe.

<div class="tbl-caption">

Table 16 Overview of key parameters of products created in the frames of
HRL Forest 2015 survey

</div>

| Parameter | Description |
|----|----|
| **Reference years** | 2015 (± 1 year)<br>2012 (± 1 year) - reprocessed historical HRL 2012 products |
| **Area mapped** | Countries mapped: EEA39 (current terminology EEA38+UK)<br>Total area mapped: 5 858 166 sqkm |
| **Unclassifiable (254) area** | 87 431 sqkm for reprocessed historical HRL 2012 products,<br>734 sqkm for 2015 products; |
| **Spatial resolution** | 20m for primary status products (TCD, DLT, FTY)<br>20m for Dominant Leaf Type Change (DLTC) product,<br>100m for Tree Cover Density Change (TCDC) product<br>100m for aggregated products |
| **Satellite input imagery used** | Primarily Sentinel-2A & Landsat-8 resampled to 20m & ESA DWH VHR 2015 (2015 products);<br>ESA Data Warehouse HR and VHR data (re-processing of historical 2012 products); |
| **Ancillary data used** | Previous GMES Forest 2012 data;<br>CLC2012 & HRL Impervious Degree 2012 & 2015 used to exclude trees in urban and agricultural context by creating FAD and FTY 2012 & 2015 layers;<br>Other ancillary data, as HRL Grassland 2012&2015m Water&Wetness 2012&2015 etc. |
| **Relevant novelties in methodology compared to historical (GMES) HRL data** | Primary layers DLT and TCD at 20m spatial resolution are sharing the same spatial extent for both 2015 and 2012 products;<br>New change products DLTC (20m) and TCDC (100m) introduced; |

#### HRL Forest 2018 (reference year 2018)[^10]

The HRL Forest with reference year 2018 (± 1 year) has been fully
produced by a consortium of European service providers. Significant
novelty was the resolution upgrade to 10m in case of primary status
layers and the introduction of a set of additional expert layers
(e.g. Confidence Layers). The specification of change layers was
slightly updated, new Tree Cover Change Mask layer in 20m resolution was
introduced to the portfolio and additionally created for previous
2012-2015 period as well.

<div class="tbl-caption">

Table 17 Overview of key parameters of products created in the frames of
HRL Forest 2018 survey

</div>

| Parameter | Description |
|----|----|
| **Reference years** | 2018 (± 1 year) |
| **Area mapped** | Countries mapped: EEA39 (current terminology EEA38+UK), slightly extended compared to HRL 2015 area<br>Total area mapped: 5 911 062 sqkm |
| **Unclassifiable (254) area** | none |
| **Spatial resolution** | 10m for primary status products (TCD, DLT, FTY)<br>20m for Dominant Leaf Type Change (DLTC) & Tree Cover Change Mask (TCCM),<br>100m for aggregated products |
| **Satellite input imagery used** | Primarily Sentinel-2A & Sentinel-2B L2A-data from the reference year 2018 in 10m |
| **Ancillary data used** | Previous HRL Forest 2015 & 2012 data;<br>CLC2018 & HRL Impervious Degree 2018 used to exclude trees in urban and agricultural context by creating FAD and FTY 2018 layers;<br>Other ancillary data close to reference year of 2018. |
| **Relevant novelties in methodology compared to historical (GMES) HRL data** | Resolution upgrade from 20m to 10m (status layers);<br>Introduction of 20m resolution TCPC change layer, calculation backward to 2012-2015 period as well;<br>Physical exclusion of urban trees and trees under predominantly agricultural use from FTY forest areas (previously these were only marked by FADSL);<br>Produced in large part in cloud environment (MUNDI web services), complex workflow described in Product User Manual; |

#### HRL VLCC Forest (reference years 2018-2021)[^11]

The HRL VLCC portfolio comprises raster layers dedicated to the themes
Tree cover and Forest, Grassland and Cropland for the EEA38 countries.
Significant novelties are the harmonized production of the yearly
updated status layers and the harmonization with other vegetation layers
included to VLCC portfolio.

<div class="tbl-caption">

Table 18 Overview of key parameters of products created in the frames of
VLCC Forest survey

</div>

| Parameter | Description |
|----|----|
| **Reference years** | new 2018 (revised), 2019, 2020, 2021 |
| **Area mapped** | Countries mapped: EEA38 (without UK)<br>Total area mapped: 5 610 863 sqkm |
| **Unclassifiable (254) area** | none |
| **Spatial resolution** | 10m for primary status products (TCD, DLT, FTY)<br>20m for Dominant Leaf Type Change (DLTC) & Tree Cover Presence Change (TCPC)\*,<br>100m for aggregated products |
| **Satellite input<br>imagery used\*\*** | Primarily Sentinel-2A & Sentinel-2B L2A-data in 10m resolution ? |
| **Ancillary data<br>used\*\*** | Previous HRL Forest 2018; ?<br>CLC2018 & HRL Impervious Degree 2018 used to exclude trees in urban and agricultural context by creating FAD and FTY 2018 layers; ?<br>Other ancillary data close to reference year of 2018. ?<br>CLCplus Backbone ?? |
| **Relevant novelties<br>in methodology<br>compared to<br>historical (GMES)<br>HRL data** | Substantial changes in mapping concept:<br>Yearly update of tree cover / forest status between 2018-2021;<br>New (revised) status for the reference year of 2018 (TCD, DLT, FTY);<br>High level technical consistency in time-series (AOI, calibration, leaf type, status vs changes)<br>Introduction of 1ha MMU for change patches in 20m change products (TCPC, DLTC). |

\*New name for Tree Cover Change Mask (TCCM) produced by previous HRL
Forest inventories \*\* No exact information, product user manual not
yet available.

### Changes in the total mapped area

The estimated total tree covered area is influenced by total area mapped
by a certain survey. Additional factor is the presence of unclassifiable
(254) areas in pre-2018 products due to cloud cover (limitations in the
availability of satellite input imagery). The influence of all these
factors is appearing in the overall statistics of the original HRL
products.

<div class="tbl-caption">

Table 19 Overall statistics of Dominant Leaf Type (DLT) raster products
(sqkm)

</div>

| DLT class | HRL DLT2012 | HRL DLT2015 | HRL DLT2018 | VLCC DLT2018 | VLCC DLT2019 | VLCC DLT2020 | VLCC DLT2021 |
|----|----|----|----|----|----|----|----|
| 0: non-tree covered areas | 3 670 507 | 3 631 870 | 3 711 454 | 3 581 943 | 3 588 549 | 3 598 260 | 3 609 649 |
| 1: broadleaved trees | 1 217 389 | 1 340 814 | 1 268 761 | 1 099 650 | 1 098 026 | 1 095 801 | 1 093 336 |
| 2: coniferous trees | 882 839 | 884 748 | 930 847 | 976 398 | 971 416 | 963 931 | 955 007 |
| 254: unclassifiable | 87 431 | 734 |  |  |  |  |  |
| TOTAL AREA | 5 858 166 | 5 858 166 | 5 911 062 | 5 657 991 | 5 657 991 | 5 657 991 | 5 657 991 |
| TREE COVER | 2 100 228 | 2 225 562 | 2 199 608 | 2 076 049 | 2 069 442 | 2 059 732 | 2 048 342 |

The total area providing valid CLMS tree cover information shows the
following evolution:

- Most of CLMS products were produced in the 2012-2018 period for the
  area of 39 EEA member countries (EEA39), but the mapped areas are
  still showing some differences:
- **HRL Forest 2015 (reference years 2015 & 2012)**: The total area of
  HRL Forest products for both 2012 and 2015 reference years is exactly
  the same, as HRL Forest 2012 was re-processed in the frames of HRL2015
  survey. On the other hand, large unclassifiable area (87 431 sqkm) is
  present in 2012 year products, while significantly lower amount (734
  sqkm) is present in 2015 year products;
- **HRL Forest 2018**: The total mapped area is slightly larger for 2018
  year survey due to refinement of land mask e.g. by considering
  previously unmapped islands along the coastline.
- **VLCC Forest layers (2018-2021)**: The CLMS production in the period
  between 2018-2021, including VLCC Forest layers and CLCplus Backbone
  2021 was restricted to the EEA38 countries, without UK area.

HRL Forest Type (FTY) layers are aimed to estimate “forest” area, by
largely following the FAO forest definition. HRL FTY is a derived
product, and combines tree cover information from primary HRL DLT & TCD
layers, as well as from HRL Imperviousness and Corine Land Cover:

- FTY Forest type (broadleaved vs coniferous) is originated directly
  from DLT tree cover 1&2;
- DLT tree covered classes (1&2) characterized by lower than 10% tree
  cover density (TCD \<10%) are excluded from FTY forest areas;
- Areas under agricultural use and in urban context are excluded from
  FTY forest areas based on information derived from CLC and HRL
  Imperviousness;
- Minimum Mapping unit of 0.5ha is applied both for tree-covered for
  non-tree-covered areas in a 4-pixel connectivity mode.

<div class="tbl-caption">

Table 20 Overall statistics of Forest Type (FTY) raster products (sqkm)

</div>

| FTY class | HRL FTY2012 | HRL FTY2015 | HRL FTY2018 | VLCC FTY2018 | VLCC FTY2019 | VLCC FTY2020 | VLCC FTY2021 |
|----|----|----|----|----|----|----|----|
| 0: all non-forest areas | 3 716 772 | 3 673 400 | 3 816 871 | 3 662 597 |  |  | 3 689 335 |
| 1: broadleaved forest | 1 168 519 | 1 300 187 | 1 159 570 | 1 015 159 |  |  | 1 009 473 |
| 2: coniferous forest | 885 445 | 883 845 | 934 621 | 980 235 |  |  | 959 184 |
| 254: unclassifiable | 87 431 | 734 |  |  |  |  |  |
| TOTAL AREA | 5 858 166 | 5 858 166 | 5 911 062 | 5 657 991 | \- | \- | 5 657 991 |
| FOREST AREA | 2 053 963 | 2 184 033 | 2 094 191 | 1 995 394 | \- | \- | 1 968 657 |

The overall statistics of Forest Type products are showing similar
picture, while the estimated forest cover is slightly lower than
corresponding tree cover values.

### Evolution of total tree cover estimated for EEA38 area

In order to exclude the effect of the variations in AOI, estimated total
tree cover values were compared to areas commonly mapped by all surveys,
by excluding all areas from the comparison, where the out of area (255)
raster code is appearing in any of the HRL Forest products. The commonly
mapped area corresponds to the area of EEA38 countries, but slightly
lower than the total area mapped by VLCC survey.

<div class="tbl-caption">

Table 21 Overall statistics of DLT products clipped to area commonly
mapped by all surveys (sqkm)

</div>

| DLT class | HRL DLT2012 | HRL DLT2015 | HRL DLT2018 | VLCC DLT2018 | VLCC DLT2019 | VLCC DLT2020 | VLCC DLT2021 |
|----|----|----|----|----|----|----|----|
| 0: all non-tree covered areas | 3 452 112 | 3 418 330 | 3 443 636 | 3 535 642 | 3 542 247 | 3 551 957 | 3 563 347 |
| 1: broadleaved trees | 1 200 102 | 1 317 597 | 1 247 205 | 1 099 295 | 1 097 671 | 1 095 446 | 1 092 980 |
| 2: coniferous trees | 872 074 | 874 558 | 920 022 | 975 926 | 970 944 | 963 460 | 954 535 |
| 254: unclassifiable | 86 575 | 378 |  |  |  |  |  |
| TOTAL AREA | 5 610 863 | 5 610 863 | 5 610 863 | 5 610 863 | 5 610 863 | 5 610 863 | 5 610 863 |
| Tree Cover | 2 072 176 | 2 192 155 | 2 167 227 | 2 075 221 | 2 068 616 | 2 058 906 | 2 047 515 |

#### Estimation of tree covered area by various sources

Tree cover is mapped by several CLMS surveys, providing various results
by estimation the total tree cover of European area. The primary
products of two of the surveys can be characterized with similar
thematic specification and the same, i.e. 10m raster resolution from the
reference year of 2018, namely HRL Forest and CLCplus Backbone. The list
of included and excluded elements of tree covered features is very
similar both for HRL Forest as well as for CLCplus Backbone woody areas,
although slight differences appear in the list. Despite of the
similarities in the specifications there are significant differences in
the estimated extent and structure of soil tree cover.

Thus, the area covered by trees may be estimated from:

- TCD layers, by considering tree cover density values in various ways;
- DLT layers, by considering all raster cells classified as broadleaved
  or coniferous trees;
- CLCplus Backbone by considering woody classes (2: needle leaved / 3:
  broadleaved deciduous / 4: broadleaved evergreen) or even class 5 (low
  growing woody vegetation);
- Additionally, FTY layers are aimed to estimate forest cover, by
  considering all raster cells classified as broadleaved or coniferous
  forest.

**Area estimations based on tree cover density**

TCD maps are created by a procedure characterized by two major steps:

- Creation of the mask (“skeleton”) of tree covered areas based a list
  of included / excluded elements. The area of this mask corresponds
  exactly to the total area of DLT map and is usually created by hybrid
  methods considering image classification and in-situ knowledge of tree
  covered features;
- Calculation of the tree cover density value (1-100%) within the mask
  based on EO derived vegetation indices.

Various possible calculation methods are used to calculate the extent of
tree cover based on TCD:

- **Tree cover estimation based on TCD values directly**: By definition
  this calculation method would deliver the exact estimation of tree
  cover, where the tree covered area of an individual raster cell is
  calculated as the total area of the raster cell multiplied by the
  percentage of tree cover shown by TCD value. Note, in practice the TCD
  value is significantly influenced by the current state of the
  vegetation;
- **Tree cover estimations based on binary maps, by applying various
  thresholds on TCD values**:
- TCD \> 1%: All elements included to Tree Cover Mask (equivalent to DLT
  tree covered area by definition);
- $TCD \ge 10\%$: Commonly applied value appearing in forest definition,
  used by production of FTY layers as well besides 0.5ha MMU and
  exclusions by CLC and IMD data on agricultural and urban areas;
- $TCD \ge 30\%$: Commonly applied value for practical applications,
  appearing e.g in CLC forest definition;
- $TCD \ge 50\%$: Corresponding to theoretical majority rule (initial
  assumption for the comparability with CLCplus Backbone woody classes).

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-311ae6e6e70b6691756876f53e589bad.png"
data-fig-alt="This is a line chart showing the time-series of estimated tree cover, measured in square kilometres (sqkm), for the area of EEA38 countries, derived from different Copernicus Land Monitoring Service (CLMS) products and methodologies. The Y-axis represents estimated tree cover area, ranging from 1,400,000 sqkm to 2,200,000 sqkm. The X-axis indicates the reference years or product versions: HRL2012, HRL2015, HRL2018, VLCC HRL2018, VLCC HRL2019, VLCC HRL2020, and VLCC HRL2021. The chart displays six data series, each representing a different tree cover estimation method: * **TCD direct** (grey line): Tree Cover Density direct estimation. * **TCD&gt;=10%** (yellow line): Tree Cover Density where values are greater than or equal to 10%. * **TCD&gt;=30%** (dark blue line): Tree Cover Density where values are greater than or equal to 30%. * **TCD&gt;=50%** (light blue line): Tree Cover Density where values are greater than or equal to 50%. * **DLT (TCD&gt;=1%)** (green line): Dominant Leaf Type where Tree Cover Density is greater than or equal to 1%. * **FTY** (orange line): Forest Type. All data series show an initial increase in estimated tree cover from HRL2012 to HRL2015, followed by a general decrease or stabilisation in subsequent years through VLCC HRL2021. The DLT (TCD&gt;=1%) series consistently shows the highest estimated tree cover, peaking at 2,192,155 sqkm in HRL2015 and decreasing to 2,047,515 sqkm by VLCC HRL2021. The TCD&gt;=50% series consistently shows the lowest estimates, peaking at 1,898,315 sqkm in HRL2015 and ending at 1,820,094 sqkm in VLCC HRL2021. The TCD direct series shows fluctuating values, starting at 1,419,336 sqkm in HRL2012, peaking at 1,551,438 sqkm in HRL2015, dropping to 1,459,714 sqkm in HRL2018, and then slightly recovering to 1,511,230 sqkm by VLCC HRL2021. The underlying data table provides the exact values for each series and year: | | HRL2012 | HRL2015 | HRL2018 | VLCC HRL2018 | VLCC HRL2019 | VLCC HRL2020 | VLCC HRL2021 | |:---|---:|---:|---:|---:|---:|---:|---:| | TCD direct | 1419336 | 1551438 | 1459714 | 1526075 | 1526888 | 1521607 | 1511230 | | TCD&gt;=10% | 2035616 | 2162570 | 2154569 | 2069836 | 2063402 | 2053720 | 2042220 | | TCD&gt;=30% | 1936441 | 2088975 | 2056060 | 2016263 | 2012098 | 2002510 | 1989572 | | TCD&gt;=50% | 1702344 | 1898315 | 1770995 | 1839166 | 1840904 | 1834070 | 1820094 | | DLT (TCD&gt;=1%) | 2072176 | 2192155 | 2167227 | 2075221 | 2068616 | 2058906 | 2047515 | | FTY | 2026067 | 2152565 | 2064989 | 1994605 | 1994605 | 1994605 | 1967869 |"
alt="Figure 8 Time-series of estimated tree cover for the area of EEA38 countries based on HRL Forest surveys. FTY layer was not created for 2019 and 2020 reference years, VLCC FTY2018 values were copied to fill these gaps." />

This is a line chart showing the time-series of estimated tree cover,
measured in square kilometres (sqkm), for the area of EEA38 countries,
derived from different Copernicus Land Monitoring Service (CLMS)
products and methodologies. The Y-axis represents estimated tree cover
area, ranging from 1,400,000 sqkm to 2,200,000 sqkm. The X-axis
indicates the reference years or product versions: HRL2012, HRL2015,
HRL2018, VLCC HRL2018, VLCC HRL2019, VLCC HRL2020, and VLCC HRL2021.

The chart displays six data series, each representing a different tree
cover estimation method: \* **TCD direct** (grey line): Tree Cover
Density direct estimation. \* **TCD\>=10%** (yellow line): Tree Cover
Density where values are greater than or equal to 10%. \* **TCD\>=30%**
(dark blue line): Tree Cover Density where values are greater than or
equal to 30%. \* **TCD\>=50%** (light blue line): Tree Cover Density
where values are greater than or equal to 50%. \* **DLT (TCD\>=1%)**
(green line): Dominant Leaf Type where Tree Cover Density is greater
than or equal to 1%. \* **FTY** (orange line): Forest Type.

All data series show an initial increase in estimated tree cover from
HRL2012 to HRL2015, followed by a general decrease or stabilisation in
subsequent years through VLCC HRL2021. The DLT (TCD\>=1%) series
consistently shows the highest estimated tree cover, peaking at
2,192,155 sqkm in HRL2015 and decreasing to 2,047,515 sqkm by VLCC
HRL2021. The TCD\>=50% series consistently shows the lowest estimates,
peaking at 1,898,315 sqkm in HRL2015 and ending at 1,820,094 sqkm in
VLCC HRL2021. The TCD direct series shows fluctuating values, starting
at 1,419,336 sqkm in HRL2012, peaking at 1,551,438 sqkm in HRL2015,
dropping to 1,459,714 sqkm in HRL2018, and then slightly recovering to
1,511,230 sqkm by VLCC HRL2021.

The underlying data table provides the exact values for each series and
year:

|  | HRL2012 | HRL2015 | HRL2018 | VLCC HRL2018 | VLCC HRL2019 | VLCC HRL2020 | VLCC HRL2021 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| TCD direct | 1419336 | 1551438 | 1459714 | 1526075 | 1526888 | 1521607 | 1511230 |
| TCD\>=10% | 2035616 | 2162570 | 2154569 | 2069836 | 2063402 | 2053720 | 2042220 |
| TCD\>=30% | 1936441 | 2088975 | 2056060 | 2016263 | 2012098 | 2002510 | 1989572 |
| TCD\>=50% | 1702344 | 1898315 | 1770995 | 1839166 | 1840904 | 1834070 | 1820094 |
| DLT (TCD\>=1%) | 2072176 | 2192155 | 2167227 | 2075221 | 2068616 | 2058906 | 2047515 |
| FTY | 2026067 | 2152565 | 2064989 | 1994605 | 1994605 | 1994605 | 1967869 |

Considering various possibilities for the estimations of tree cover
described above, the estimated total tree covered area is influenced by
the major factors of:

- The extent end structure of the binary mask of tree cover further
  classified in DLT / FTY products as broadleaved or coniferous -
  influencing all presented estimations;
- The calibration of TCD values – influencing TCD, TCD≥10%, TCD≥30% and
  TCD≥50% estimations.

Both the extent and structure of tree cover mask, as well as calibration
of TCD values are showing significant differences, and characterise the
individual surveys. All of these factors are influencing the total
estimated tree covered area presented in Figure 8:

- Large variation of total estimated tree cover is shown in the period
  2012-2018, while the time-series within VLCC survey (2018-2021) is
  showing stability by presenting the slow decrease of total tree cover;
- All estimations show obvious breakpoint in 2018 between HRL2018 and
  VLCC2018 surveys;
- Lowest tree covered area is estimated by TCD direct calculation
  method, while highest values are shown by DLT layers (equivalent with
  TCD ≥ 1%);
- Lowest total tree covered area in the time-series is shown by 2012
  survey. One of the possible reasons is, that relatively large area
  (altogether 86 575 sqkm) could not be classified because of cloud
  cover, represented by value 254 (unclassifiable area) in HRL2012 data;
- The highest total tree covered area in the time-series is shown by
  2015 survey. Possible reason is the significant overestimation of tree
  cover experienced by many visual checks;
- Local minimum is shown only by TCD direct and TCD ≥ 50% calculations
  in case of HRL2018;
- FTY and TCD ≥ 1% shows only few differences in 2012 and in 2015, while
  larger differences from 2018 onwards. The reason is, that areas under
  agricultural use and in urban context were only marked in 2012 and
  2015, while from 2018 excluded from FTY forest areas by FADSL layers.

### Evolution of the calibration of TCD values

TCD-value based estimations of tree covered area are significantly
influenced by the calibration of TCD values. Calibration differences
between individual surveys may be illustrated well by the histogram of
TCD values. The calibration differences between HRL TCD2018 and VLCC
TCD2018 are highlighted to demonstrate that the distribution of TCD
values is not specific to the reference year, but to the survey.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-e282e8058eba9d7214d914a5ec52b2bc.png"
data-fig-alt="A grid of eight bar charts, with the bottom right empty, illustrating the distribution of land area in hectares across different Tree Cover Density (TCD) percentages for EEA38 countries. Each chart&#39;s X-axis represents TCD values from 1% to 100%, and the Y-axis represents Area in hectares (ha), ranging from 0 to 6,000,000 ha. The first three charts display High Resolution Layer (HRL) TCD data: * **HRL TCD2012 [ha]**: Shows a peak area of approximately 4,500,000 ha at 82–85% TCD. * **HRL TCD2015 [ha]**: Shows a peak area of approximately 5,500,000 ha at 85–88% TCD. * **HRL TCD2018 [ha]**: Shows a peak area of approximately 5,000,000 ha at 85–88% TCD. The bottom four charts display Very Large Continuous Cover (VLCC) TCD data: * **VLCC TCD2018 [ha]**: Shows a peak area of approximately 5,500,000 ha at 94–97% TCD. * **VLCC TCD2019 [ha]**: Shows a peak area of approximately 5,200,000 ha at 94–97% TCD. * **VLCC TCD2020 [ha]**: Shows a peak area of approximately 5,500,000 ha at 94–97% TCD. * **VLCC TCD2021 [ha]**: Shows a peak area of approximately 5,500,000 ha at 94–97% TCD. The fourth chart, **HRL TCD2018 vs VLCC TCD2018 [ha]**, directly compares the two datasets for 2018. HRL TCD2018 (blue bars) shows a distribution with larger areas for TCD values between 50% and 70%, peaking around 85–88%. VLCC TCD2018 (red bars) shows larger areas for TCD values above 70%, with its peak at a higher TCD percentage of 94–97%. Both HRL and VLCC distributions show minimal area for TCD values below 30%. The VLCC TCD distributions consistently peak at higher TCD percentages (94-97%) compared to HRL TCD distributions (82-88%) across the years shown."
alt="Figure 9 Calibration differences of various surveys illustrated by the distribution of TCD values. Y axis represents total area (ha) in EEA38 countries covered by raster cells characterised by a certain TCD value." />

A grid of eight bar charts, with the bottom right empty, illustrating
the distribution of land area in hectares across different Tree Cover
Density (TCD) percentages for EEA38 countries. Each chart’s X-axis
represents TCD values from 1% to 100%, and the Y-axis represents Area in
hectares (ha), ranging from 0 to 6,000,000 ha.

The first three charts display High Resolution Layer (HRL) TCD data: \*
**HRL TCD2012 \[ha\]**: Shows a peak area of approximately 4,500,000 ha
at 82–85% TCD. \* **HRL TCD2015 \[ha\]**: Shows a peak area of
approximately 5,500,000 ha at 85–88% TCD. \* **HRL TCD2018 \[ha\]**:
Shows a peak area of approximately 5,000,000 ha at 85–88% TCD.

The bottom four charts display Very Large Continuous Cover (VLCC) TCD
data: \* **VLCC TCD2018 \[ha\]**: Shows a peak area of approximately
5,500,000 ha at 94–97% TCD. \* **VLCC TCD2019 \[ha\]**: Shows a peak
area of approximately 5,200,000 ha at 94–97% TCD. \* **VLCC TCD2020
\[ha\]**: Shows a peak area of approximately 5,500,000 ha at 94–97% TCD.
\* **VLCC TCD2021 \[ha\]**: Shows a peak area of approximately 5,500,000
ha at 94–97% TCD.

The fourth chart, **HRL TCD2018 vs VLCC TCD2018 \[ha\]**, directly
compares the two datasets for 2018. HRL TCD2018 (blue bars) shows a
distribution with larger areas for TCD values between 50% and 70%,
peaking around 85–88%. VLCC TCD2018 (red bars) shows larger areas for
TCD values above 70%, with its peak at a higher TCD percentage of
94–97%. Both HRL and VLCC distributions show minimal area for TCD values
below 30%. The VLCC TCD distributions consistently peak at higher TCD
percentages (94-97%) compared to HRL TCD distributions (82-88%) across
the years shown.

While the distribution of TCD values shows significant differences
between each reference year in 2012-2018 period, the shape of the
histograms is almost the same for all VLCC TCD layers - the yearly
time-series of VLCC TCD layers shows stability in terms of calibration
as well. The question is however, how far the calibration of next survey
(beyond 2021) may be harmonized with the current calibration of VLCC TCD
layers.

### Overview of the stability of leaf type classification in DLT status layers

Besides of providing a mask for tree / forest covered areas, DLT and FTY
layers provide separation of the leaf type between broadleaved vs
coniferous. The stability of the classification in the time-series was
analysed by checking the differences of the DLT layers.

Following difference codes were applied by considering all possible
combinations in the classification:

0: unchanged areas with no tree cover 1: new broadleaved cover (no tree
cover in first layer) 2: new coniferous cover (no tree cover in first
layer) 3: loss of broadleaved cover (no tree cover in second layer) 4:
loss of coniferous cover (no tree cover in second layer) 11: unchanged
broadleaved cover 22: unchanged coniferous cover 120: broadleaved
changed to coniferous 210: coniferous changed to broadleaved 254:
unclassifiable in any of parent status layers

In order to gain comparable results for the entire period the DLT
differences were calculated for the area mapped commonly by all DLT
layers. All differences were calculated in 10m raster resolution.

<div class="tbl-caption">

Table 22 Classification differences in DLT time-series for commonly
mapped EEA38 area (sqkm)

</div>

| DIFFERENCE CODE | HRL DLT2012 VS HRL DLT2015 | HRL DLT2015 VS HRL DLT2018 | VLCC DLT2018 VS VLCC DLT2019 | VLCC DLT2019 VS VLCC DLT2020 | VLCC DLT2020 VS VLCC DLT2021 |
|----|----|----|----|----|----|
| 0 | 3 209 737 | 3 297 386 | 3 535 164 | 3 540 472 | 3 547 401 |
| 1 | 200 052 | 103 320 | 354 | 1 297 | 3 234 |
| 2 | 42 024 | 42 930 | 124 | 479 | 1 321 |
| 3 | 118 517 | 198 077 | 1 978 | 3 522 | 5 700 |
| 4 | 40 839 | 40 180 | 5 105 | 7 963 | 10 246 |
| 11 | 1 008 487 | 947 604 | 1 097 317 | 1 094 149 | 1 089 746 |
| 22 | 736 584 | 831 471 | 970 821 | 962 981 | 953 214 |
| 120 | 73 070 | 101 524 |  |  |  |
| 210 | 94 600 | 48 371 |  |  |  |
| 254 | 86 953 |  |  |  |  |
| SUM | 5 610 863 | 5 610 863 | 5 610 863 | 5 610 863 | 5 610 863 |
|  | **HRL DLT2018 VS VLCC DLT2018** |  |  |  |  |
| 0 | 3 208 100 |  |  |  |  |
| 1 | 170 956 |  |  |  |  |
| 2 | 39 275 |  |  |  |  |
| 3 | 176 445 |  |  |  |  |
| 4 | 58 793 |  |  |  |  |
| 11 | 975 178 |  |  |  |  |
| 22 | 714 724 |  |  |  |  |
| 120 | 165 974 |  |  |  |  |
| 210 | 101 041 |  |  |  |  |
| 254 | 378 |  |  |  |  |
| SUM | 5 610 863 |  |  |  |  |

**Key observations:**

- In case of all change classes (new cover / loss of cover)
  significantly more differences are shown between HRL or HRL vs VLCC
  layers in 2012-2018 period, than between VLCC layers in period
  2018-2021;
- Large areas were re-classified from broadleaved to coniferous and vice
  versa between HRL or HRL vs VLCC layers in 2012-2018 period, while no
  re-classification is shown between VLCC layers in period 2018-2021;
- Two different classifications (HRL vs VLCC survey) were compared to
  the same reference year of 2018, similar magnitude of differences is
  shown than between any of previous classifications;
- Unclassifiable areas appear in comparisons between HRL DLT layers
  2012-2015 and 2015-2018.

### Classification differences HRL DLT2018 vs VLCC DLT2018 layers

The magnitude of classification differences between HRL DLT2018 vs VLCC
DLT2018 layers characterizes well the level of classification
uncertainty of individual surveys. Classification differences were coded
the same way as in case of tree cover presence change data.

<div class="tbl-caption">

Table 23 Differences in estimated tree cover for the reference year of
2018

</div>

| DIFFERENCE CLASS | HRL DLT2018 vs VLCC DLT2018 |  |  |
|----|----|----|----|
|  | **sqkm** | **%** | **% of unchanged<br>tree cover** |
| 0: unchanged areas with no tree cover | 3 343 511 | 59.1% |  |
| 1: new tree cover | 146 363 | 2.6% | 7.6% |
| 2: loss of tree cover | 238 325 | 4.2% | 12.4% |
| 10: unchanged areas with tree cover | 1 929 685 | 34.1% | 100.0% |
| 254: unclassifiable in any status | \- | \- |  |
| **SUM** | **5 657 885** | **100.0%** |  |

Significant differences in estimated tree cover are shown between the
two classifications performed to the same reference year of 2018.
Altogether 146 363 sqkm areas (7.6% of all stable tree cover) were
classified in VLCC DLT2018 as new tree cover against HRL DLT2018, while
238 325 sqkm (12.4% of all stable tree cover) were classified as loss of
tree cover compared to HRL DLT2018.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-32d63c515af7799baea1df52ffd59923.png"
data-fig-alt="Choropleth map of Europe displaying &#39;All tree cover differences&#39; between the High Resolution Layer (HRL) Dynamic Land Take (DLT) 2018 and Very Low Cover Class (VLCC) Dynamic Land Take (DLT) 2018 classifications, for the reference year 2018. The map covers EU Member States and surrounding countries, including the UK, Switzerland, Norway, the Balkan states, and Turkey. A seven-class diverging colour scale indicates percentage differences in tree cover: * Dark green: 20% – 100% (HRL DLT2018 estimates higher tree cover) * Light green: 10% – 20% (HRL DLT2018 estimates higher tree cover) * Pale green: 1% – 10% (HRL DLT2018 estimates higher tree cover) * Grey: -1% – 1% (minimal difference or agreement between classifications) * Light red: -10% – -1% (HRL DLT2018 estimates lower tree cover) * Red: -20% – -10% (HRL DLT2018 estimates lower tree cover) * Dark red: -100% – -20% (HRL DLT2018 estimates significantly lower tree cover) Areas where HRL DLT2018 estimates higher tree cover (green shades) are visible in parts of the Iberian Peninsula (Spain, Portugal), southern France, Italy, and scattered regions in Eastern Europe. Areas where HRL DLT2018 estimates lower tree cover (red shades) are prominent in northern Scandinavia (Sweden, Finland), parts of Eastern Europe (e.g., Poland), and Turkey. Much of Central Europe, including Germany and France, shows close agreement between the two classifications, indicated by extensive grey areas."
alt="Figure 10 Aggregated difference map of all tree cover differences. Green colours indicate surplus of tree cover mapped by VLCC DLT2018, while red colours indicate surplus of tree cover mapped by HRL DLT2018." />

Choropleth map of Europe displaying “All tree cover differences” between
the High Resolution Layer (HRL) Dynamic Land Take (DLT) 2018 and Very
Low Cover Class (VLCC) Dynamic Land Take (DLT) 2018 classifications, for
the reference year 2018. The map covers EU Member States and surrounding
countries, including the UK, Switzerland, Norway, the Balkan states, and
Turkey. A seven-class diverging colour scale indicates percentage
differences in tree cover: \* Dark green: 20% – 100% (HRL DLT2018
estimates higher tree cover) \* Light green: 10% – 20% (HRL DLT2018
estimates higher tree cover) \* Pale green: 1% – 10% (HRL DLT2018
estimates higher tree cover) \* Grey: -1% – 1% (minimal difference or
agreement between classifications) \* Light red: -10% – -1% (HRL DLT2018
estimates lower tree cover) \* Red: -20% – -10% (HRL DLT2018 estimates
lower tree cover) \* Dark red: -100% – -20% (HRL DLT2018 estimates
significantly lower tree cover)

Areas where HRL DLT2018 estimates higher tree cover (green shades) are
visible in parts of the Iberian Peninsula (Spain, Portugal), southern
France, Italy, and scattered regions in Eastern Europe. Areas where HRL
DLT2018 estimates lower tree cover (red shades) are prominent in
northern Scandinavia (Sweden, Finland), parts of Eastern Europe (e.g.,
Poland), and Turkey. Much of Central Europe, including Germany and
France, shows close agreement between the two classifications, indicated
by extensive grey areas.

Aggregated tree cover differences were calculated for a 10x10km
statistical grid. The distribution of tree cover differences between the
two classifications shows regional variations, especially large
differences are shown for Mediterranean and Scandinavian areas.

<div class="tbl-caption">

Table 24 DLT classification uncertainties for the reference year of 2018

</div>

| DIFFERENCE CLASS | HRL DLT2018 vs VLCC DLT2018 |  |  |  |
|----|----|----|----|----|
|  | **sqkm** | **%** | **% to unchanged<br>broadleaved** | **% to<br>unchanged<br>coniferous** |
| 0: unchanged areas with no tree cover | 3 343 511 | 59.1% |  |  |
| 1: new broadleaved cover | 103 376 | 1.8% | 10.9% |  |
| 2: new coniferous cover | 42 988 | 0.8% |  | 5.2% |
| 3: loss of broadleaved cover | 198 119 | 3.5% | 20.9% |  |
| 4: loss of coniferous cover | 40 207 | 0.7% |  | 4.8% |
| 11: unchanged broadleaved cover | 947 878 | 16.8% | 100.0% |  |
| 22: unchanged coniferous cover | 831 863 | 14.7% |  | 100.0% |
| 120: broadleaved changed to coniferous | 101 548 | 1.8% | 10.7% |  |
| 210: coniferous changed to broadleaved | 48 397 | 0.9% |  | 5.8% |
| 254: unclassifiable in any status |  | 0.0% |  |  |
| **SUM** | **5 657 885** | **100.0%** |  |  |

Not only the presence of tree cover, but also the leaf type
classification is showing differences between the two surveys.
Classification differences were coded in similar way as in case of
dominant leaf type change data, but all the meaningful combinations were
kept.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-1ec3d6e380fe7439ca0c3479dd789046.png"
data-fig-alt="Choropleth map displaying the percentage differences in broadleaved cover between the High Resolution Layer Dominant Leaf Type (HRL DLT2018) and Very Large-Scale Cartography Dominant Leaf Type (VLCC DLT2018) datasets for the reference year 2018 across Europe, including EU Member States, the UK, Norway, Switzerland, Iceland, the Western Balkans, and Turkey. The legend indicates broadleaved cover differences as follows: - Dark Green: 20% - 100% (HRL DLT2018 shows significantly more broadleaved cover than VLCC DLT2018). - Light Green: 10% - 20% (HRL DLT2018 shows more broadleaved cover than VLCC DLT2018). - Pale Green: 1% - 10% (HRL DLT2018 shows slightly more broadleaved cover than VLCC DLT2018). - Grey: -1% - 1% (minimal difference between datasets). - Pale Red: -10% - -1% (HRL DLT2018 shows slightly less broadleaved cover than VLCC DLT2018). - Red: -20% - -10% (HRL DLT2018 shows less broadleaved cover than VLCC DLT2018). - Dark Red: -100% - -20% (HRL DLT2018 shows significantly less broadleaved cover than VLCC DLT2018). Spatially, areas displaying significantly less broadleaved cover in HRL DLT2018 (red and dark red) are concentrated in Fennoscandia (Norway, Sweden, Finland), Eastern Europe (Poland, Czechia, Romania, Bulgaria, and the Baltic States), the Carpathian Mountains, and across large parts of Turkey. Areas showing more broadleaved cover in HRL DLT2018 (green shades) are scattered, with notable occurrences in parts of France, Portugal, Spain, Italy, and the Western Balkans. Most of Western and Central Europe, including Germany, the Netherlands, and large portions of France, the UK, and the Iberian Peninsula, exhibit minimal differences between the two datasets, depicted in grey."
alt="Figure 11 Aggregated difference map of broadleaved cover differences. Green colours indicate surplus of broadleaved cover mapped by VLCC DLT2018, while red colours indicate surplus of broadleaved cover mapped by HRL DLT2018." />

Choropleth map displaying the percentage differences in broadleaved
cover between the High Resolution Layer Dominant Leaf Type (HRL DLT2018)
and Very Large-Scale Cartography Dominant Leaf Type (VLCC DLT2018)
datasets for the reference year 2018 across Europe, including EU Member
States, the UK, Norway, Switzerland, Iceland, the Western Balkans, and
Turkey.

The legend indicates broadleaved cover differences as follows: - Dark
Green: 20% - 100% (HRL DLT2018 shows significantly more broadleaved
cover than VLCC DLT2018). - Light Green: 10% - 20% (HRL DLT2018 shows
more broadleaved cover than VLCC DLT2018). - Pale Green: 1% - 10% (HRL
DLT2018 shows slightly more broadleaved cover than VLCC DLT2018). -
Grey: -1% - 1% (minimal difference between datasets). - Pale Red: -10% -
-1% (HRL DLT2018 shows slightly less broadleaved cover than VLCC
DLT2018). - Red: -20% - -10% (HRL DLT2018 shows less broadleaved cover
than VLCC DLT2018). - Dark Red: -100% - -20% (HRL DLT2018 shows
significantly less broadleaved cover than VLCC DLT2018).

Spatially, areas displaying significantly less broadleaved cover in HRL
DLT2018 (red and dark red) are concentrated in Fennoscandia (Norway,
Sweden, Finland), Eastern Europe (Poland, Czechia, Romania, Bulgaria,
and the Baltic States), the Carpathian Mountains, and across large parts
of Turkey. Areas showing more broadleaved cover in HRL DLT2018 (green
shades) are scattered, with notable occurrences in parts of France,
Portugal, Spain, Italy, and the Western Balkans. Most of Western and
Central Europe, including Germany, the Netherlands, and large portions
of France, the UK, and the Iberian Peninsula, exhibit minimal
differences between the two datasets, depicted in grey.

Aggregated differences of broadleaved / coniferous cover were calculated
for a 10x10km statistical grid to illustrate regional variations in leaf
type classification. Large amount of broadleaved cover was eliminated or
re-classified to coniferous cover by VLCC DLT survey compared to HRL
DLT2018.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-cbb85153645e3c9aeee6428dd3d29a08.png"
data-fig-alt="Choropleth map displaying the differences in coniferous cover percentage between the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Dominant Leaf Type (DLT) product for 2018 and the Validation and Land Cover Classification (VLCC) DLT product for 2018, across Europe. The map shows the percentage difference, where positive values indicate higher coniferous cover in HRL DLT2018 compared to VLCC DLT2018, and negative values indicate lower coniferous cover in HRL DLT2018. The legend defines seven colour classes for these differences: * Dark Green: 20% - 100% * Medium Green: 10% - 20% * Light Green: 1% - 10% * Grey: -1% - 1% (representing areas with no significant difference) * Light Red: -10% - -1% * Medium Red: -20% - -10% * Dark Red: -100% - -20% Spatially, northern European regions, including Scandinavia and parts of the Baltic States, show predominantly green hues, indicating HRL DLT2018 reports higher coniferous cover. Conversely, large areas in Southern Europe, particularly in the Iberian Peninsula (Spain, Portugal), parts of Italy, the Balkans, and Turkey, exhibit red and dark red colours, signifying that HRL DLT2018 reports significantly lower coniferous cover compared to VLCC DLT2018. Central Europe shows a mix of light green and light red patches, while Ireland and the United Kingdom are largely grey, indicating minimal differences."
alt="Figure 12 Aggregated difference map of coniferous cover differences. Green colours indicate surplus of coniferous cover mapped by VLCC DLT2018, while red colours indicate surplus of coniferous cover mapped by HRL DLT2018." />

Choropleth map displaying the differences in coniferous cover percentage
between the Copernicus Land Monitoring Service (CLMS) High Resolution
Layer (HRL) Dominant Leaf Type (DLT) product for 2018 and the Validation
and Land Cover Classification (VLCC) DLT product for 2018, across
Europe. The map shows the percentage difference, where positive values
indicate higher coniferous cover in HRL DLT2018 compared to VLCC
DLT2018, and negative values indicate lower coniferous cover in HRL
DLT2018.

The legend defines seven colour classes for these differences: \* Dark
Green: 20% - 100% \* Medium Green: 10% - 20% \* Light Green: 1% - 10% \*
Grey: -1% - 1% (representing areas with no significant difference) \*
Light Red: -10% - -1% \* Medium Red: -20% - -10% \* Dark Red: -100% -
-20%

Spatially, northern European regions, including Scandinavia and parts of
the Baltic States, show predominantly green hues, indicating HRL DLT2018
reports higher coniferous cover. Conversely, large areas in Southern
Europe, particularly in the Iberian Peninsula (Spain, Portugal), parts
of Italy, the Balkans, and Turkey, exhibit red and dark red colours,
signifying that HRL DLT2018 reports significantly lower coniferous cover
compared to VLCC DLT2018. Central Europe shows a mix of light green and
light red patches, while Ireland and the United Kingdom are largely
grey, indicating minimal differences.

Large green areas in Scandinavia indicate new coniferous cover partly as
new cover partly as re-classified from broadleaved by VLCC DLT survey
compared to HRL DLT2018.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-7e837cb6c0a5adb20b4c1e055c3596dd.png"
data-fig-alt="Two comparison maps illustrating aggregated broadleaved cover differences, likely derived from the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Dominant Leaf Type (DLT) 2018 data versus VLCC DLT2018 data, as suggested by the surrounding context. The maps use green colours to indicate the presence of broadleaved cover, with a specific light green shade indicating a &#39;surplus of broadleaved cover&#39; (based on the partial caption). White areas represent no tree cover or unclassified areas. The left panel displays a significantly larger extent of light green areas, signifying more pronounced &#39;surplus broadleaved cover&#39; in this view. This panel also contains dark green areas for general broadleaved cover. The right panel shows predominantly dark green areas for general broadleaved cover and white areas, with only minimal, scattered light green areas, indicating fewer or smaller areas of &#39;surplus broadleaved cover&#39; compared to the left panel."
alt="Figure 13 DLT2018 maps illustrating differences between the two surveys. x,y= 4323013,4079743 close to lake Vrangla, Norway." />

Two comparison maps illustrating aggregated broadleaved cover
differences, likely derived from the Copernicus Land Monitoring Service
(CLMS) High Resolution Layer (HRL) Dominant Leaf Type (DLT) 2018 data
versus VLCC DLT2018 data, as suggested by the surrounding context. The
maps use green colours to indicate the presence of broadleaved cover,
with a specific light green shade indicating a “surplus of broadleaved
cover” (based on the partial caption). White areas represent no tree
cover or unclassified areas. The left panel displays a significantly
larger extent of light green areas, signifying more pronounced “surplus
broadleaved cover” in this view. This panel also contains dark green
areas for general broadleaved cover. The right panel shows predominantly
dark green areas for general broadleaved cover and white areas, with
only minimal, scattered light green areas, indicating fewer or smaller
areas of “surplus broadleaved cover” compared to the left panel.

HRL DLT2018 VLCC DLT2018

#### Visualization of classification differences by high resolution maps

In order to gain exact statistics and be able to visualize all
differences between DLT classifications DLT difference maps were
calculated in 10m raster resolution between neighbouring status data,
where all possible combinations were considered. The high-resolution
difference map between HRL DLT2018 and VLCC DLT2018 survey results
indicate especially large variations in tree cover classifications
Mediterranean, Scandinavian and Alpine regions.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-21d1ab18ffa3734969f2177447ba31b8.png"
data-fig-alt="This image contains two land cover maps. The top map, titled &#39;DLT DIFFERENCE MAP: HRL DLT2018 vs VLCC DLT2018&#39;, displays differences in Dominant Leaf Type (DLT) classification between the High Resolution Layer (HRL) DLT2018 and the Vegetation Land Cover Component (VLCC) DLT2018 products. The legend indicates: * White (0): unchanged areas with no tree cover * Bright green (1): new broadleaved cover * Dark green (2): new coniferous cover * Orange (3): loss of broadleaved cover * Red (4): loss of coniferous cover * Light grey (11): unchanged areas with broadleaved cover * Dark grey (22): unchanged areas with coniferous cover * Blue (120): Broadleaved changed to coniferous * Light blue (210): Coniferous changed to broadleaved * Magenta (254): unclassifiable in any of parent status layers The map predominantly shows large areas of unchanged broadleaved cover (light grey) and unchanged coniferous cover (dark grey). Significant areas of broadleaved cover changed to coniferous (blue) are visible, along with smaller, dispersed patches of new broadleaved/coniferous cover (greens) and loss of broadleaved/coniferous cover (orange/red). This indicates a re-classification where broadleaved cover was identified as coniferous in the VLCC DLT survey compared to HRL DLT2018. The bottom map, labelled &#39;CLCplus Backbone&#39;, illustrates the underlying land cover structure. The legend includes: * Red (1): Sealed * Dark green (2): Woody needle leaved trees * Light green (3): Woody broadleaved deciduous trees * Bright green (4): Woody broadleaved evergreen trees * Brown (5): Low-growing woody plants * Light yellow (6): Permanent herbaceous * Pale yellow (7): Periodically herbaceous * Pink (8): Lichens &amp; mosses * Light grey (9): Non and sparsely vegetated * Dark blue (10): Water * Light blue (11): Snow &amp; ice This map shows a landscape dominated by woody needle-leaved trees (dark green) and woody broadleaved deciduous trees (light green), with numerous dark blue water bodies. Patches of low-growing woody plants (brown) and permanent herbaceous areas (light yellow) are also visible."
alt="Figure 14 Typical view of differences between tree cover classifications for the reference year 2018. x,y= 4323013,4079743 close to lake Vrangla, Norway." />

This image contains two land cover maps. The top map, titled “DLT
DIFFERENCE MAP: HRL DLT2018 vs VLCC DLT2018”, displays differences in
Dominant Leaf Type (DLT) classification between the High Resolution
Layer (HRL) DLT2018 and the Vegetation Land Cover Component (VLCC)
DLT2018 products. The legend indicates: \* White (0): unchanged areas
with no tree cover \* Bright green (1): new broadleaved cover \* Dark
green (2): new coniferous cover \* Orange (3): loss of broadleaved cover
\* Red (4): loss of coniferous cover \* Light grey (11): unchanged areas
with broadleaved cover \* Dark grey (22): unchanged areas with
coniferous cover \* Blue (120): Broadleaved changed to coniferous \*
Light blue (210): Coniferous changed to broadleaved \* Magenta (254):
unclassifiable in any of parent status layers The map predominantly
shows large areas of unchanged broadleaved cover (light grey) and
unchanged coniferous cover (dark grey). Significant areas of broadleaved
cover changed to coniferous (blue) are visible, along with smaller,
dispersed patches of new broadleaved/coniferous cover (greens) and loss
of broadleaved/coniferous cover (orange/red). This indicates a
re-classification where broadleaved cover was identified as coniferous
in the VLCC DLT survey compared to HRL DLT2018.

The bottom map, labelled “CLCplus Backbone”, illustrates the underlying
land cover structure. The legend includes: \* Red (1): Sealed \* Dark
green (2): Woody needle leaved trees \* Light green (3): Woody
broadleaved deciduous trees \* Bright green (4): Woody broadleaved
evergreen trees \* Brown (5): Low-growing woody plants \* Light yellow
(6): Permanent herbaceous \* Pale yellow (7): Periodically herbaceous \*
Pink (8): Lichens & mosses \* Light grey (9): Non and sparsely vegetated
\* Dark blue (10): Water \* Light blue (11): Snow & ice This map shows a
landscape dominated by woody needle-leaved trees (dark green) and woody
broadleaved deciduous trees (light green), with numerous dark blue water
bodies. Patches of low-growing woody plants (brown) and permanent
herbaceous areas (light yellow) are also visible.

CLCplus Backbone 2018

The re-classification of broadleaved cover to coniferous by VLCC DLT2018
is typical for most of Scandinavian area.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-f21efee1e215800108c6bc47d662f737.png"
data-fig-alt="This image displays two juxtaposed choropleth maps of the same local geographic area. The top map, titled &#39;DLT DIFFERENCE MAP&#39;, compares Dominant Leaf Type (DLT) classifications from the High Resolution Layer (HRL) DLT2018 and VLCC DLT2018 datasets. The legend defines the colour coding as follows: * White: 0 (unchanged areas with no tree cover) * Light green: 1 (new broadleaved cover) * Dark green: 2 (new coniferous cover) * Orange: 3 (loss of broadleaved cover) * Red: 4 (loss of coniferous cover) * Light grey: 11 (unchanged areas with broadleaved cover) * Dark grey: 22 (unchanged areas with coniferous cover) * Dark blue: 120 (Broadleaved changed to coniferous) * Light blue: 210 (Coniferous changed to broadleaved) * Magenta: 254 (unclassifiable in any of parent status layers) The map illustrates a complex pattern of tree cover change and stability, with distinct areas showing loss of broadleaved cover (orange), new coniferous cover (dark green), and broadleaved to coniferous conversion (dark blue). Many areas remain unchanged with or without tree cover (white and grey shades). The bottom map displays the &#39;CLCplus Backbone&#39; land cover classification for the identical geographic area. Its legend defines the land cover classes as: * Red: 1 (Sealed) * Dark green: 2 (Woody needle leaved trees) * Medium green: 3 (Woody broadleaved deciduous trees) * Light green: 4 (Woody broadleaved evergreen trees) * Brown: 5 (Low-growing woody plants) * Light yellow-green: 6 (Permanent herbaceous) * Light yellow: 7 (Periodically herbaceous) * Pink: 8 (Lichens &amp; mosses) * Grey: 9 (Non and sparsely vegetated) * Dark blue: 10 (Water) * Light blue: 11 (Snow &amp; ice) This map provides a detailed view of the underlying land cover, predominantly showing various types of woody vegetation (needle-leaved, broadleaved, low-growing) and herbaceous areas, alongside smaller patches of sealed surfaces and water bodies."
alt="Figure 15 Typical view of differences between tree cover classifications for the reference year 2018. x,y = 2817368,2020876 - close to Atalaia, Portugal" />

This image displays two juxtaposed choropleth maps of the same local
geographic area.

The top map, titled “DLT DIFFERENCE MAP”, compares Dominant Leaf Type
(DLT) classifications from the High Resolution Layer (HRL) DLT2018 and
VLCC DLT2018 datasets. The legend defines the colour coding as follows:
\* White: 0 (unchanged areas with no tree cover) \* Light green: 1 (new
broadleaved cover) \* Dark green: 2 (new coniferous cover) \* Orange: 3
(loss of broadleaved cover) \* Red: 4 (loss of coniferous cover) \*
Light grey: 11 (unchanged areas with broadleaved cover) \* Dark grey: 22
(unchanged areas with coniferous cover) \* Dark blue: 120 (Broadleaved
changed to coniferous) \* Light blue: 210 (Coniferous changed to
broadleaved) \* Magenta: 254 (unclassifiable in any of parent status
layers) The map illustrates a complex pattern of tree cover change and
stability, with distinct areas showing loss of broadleaved cover
(orange), new coniferous cover (dark green), and broadleaved to
coniferous conversion (dark blue). Many areas remain unchanged with or
without tree cover (white and grey shades).

The bottom map displays the “CLCplus Backbone” land cover classification
for the identical geographic area. Its legend defines the land cover
classes as: \* Red: 1 (Sealed) \* Dark green: 2 (Woody needle leaved
trees) \* Medium green: 3 (Woody broadleaved deciduous trees) \* Light
green: 4 (Woody broadleaved evergreen trees) \* Brown: 5 (Low-growing
woody plants) \* Light yellow-green: 6 (Permanent herbaceous) \* Light
yellow: 7 (Periodically herbaceous) \* Pink: 8 (Lichens & mosses) \*
Grey: 9 (Non and sparsely vegetated) \* Dark blue: 10 (Water) \* Light
blue: 11 (Snow & ice) This map provides a detailed view of the
underlying land cover, predominantly showing various types of woody
vegetation (needle-leaved, broadleaved, low-growing) and herbaceous
areas, alongside smaller patches of sealed surfaces and water bodies.

CLCplus Backbone 2018

The example in Portugal illustrates well the uncertainty of the
classification on low density Mediterranean tree cover. Primarily the
presence of tree cover is classified differently in Mediterranean area
by the two surveys, but at several regions the re-classification of
broadleaved to coniferous is characteristic to southern areas as well.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-5e6187e234250570682d4a3e1e6aca8c.png"
data-fig-alt="The image displays two thematic maps of a mountainous region, both pertaining to land cover and dominant leaf type (DLT) classifications from 2018. The top map, titled &#39;DLT DIFFERENCE MAP: HRL DLT2018 vs VLCC DLT2018&#39;, illustrates differences in Dominant Leaf Type classifications between the High Resolution Layer (HRL) DLT2018 and Vegetation Layer Cover Continuity (VLCC) DLT2018 surveys. The legend shows: * White (0): unchanged areas with no tree cover * Light Green (1): new broadleaved cover * Dark Green (2): new coniferous cover * Orange (3): loss of broadleaved cover * Red (4): loss of coniferous cover * Light Grey (11): unchanged areas with broadleaved cover * Dark Grey (22): unchanged areas with coniferous cover * Blue (120): Broadleaved changed to coniferous * Cyan (210): Coniferous changed to broadleaved * Magenta (254): unclassifiable in any of parent status layers The map primarily shows large areas of unchanged cover, with significant patches of &#39;loss of coniferous cover&#39; (red) in the central mountainous regions, and &#39;Broadleaved changed to coniferous&#39; (blue) appearing in the northern and western parts of the mapped area. The bottom map, titled &#39;CLCplus Backbone&#39;, presents a detailed land cover/land use (LULC) classification. The legend includes: * Red (1): Sealed * Dark Green (2): Woody needle leaved trees * Light Green (3): Woody broadleaved deciduous trees * Lime Green (4): Woody broadleaved evergreen trees * Brown (5): Low-growing woody plants * Light Yellow (6): Permanent herbaceous * Yellow (7): Periodically herbaceous * Pink (8): Lichens &amp; mosses * Grey (9): Non and sparsely vegetated * Dark Blue (10): Water * Light Blue (11): Snow &amp; ice This map reveals extensive forested areas, predominantly &#39;Woody needle leaved trees&#39; (dark green) and &#39;Woody broadleaved deciduous trees&#39; (light green). A river valley features &#39;Sealed&#39; (red) areas along its course, leading to a large &#39;Water&#39; body (dark blue). Patches of &#39;Snow &amp; ice&#39; (light blue) are visible in the higher elevations."
alt="Figure 16 Typical view of differences between tree cover classifications for the reference year 2018. x,y = 4589578,2725264 - close to Stambach, Austria" />

The image displays two thematic maps of a mountainous region, both
pertaining to land cover and dominant leaf type (DLT) classifications
from 2018.

The top map, titled “DLT DIFFERENCE MAP: HRL DLT2018 vs VLCC DLT2018”,
illustrates differences in Dominant Leaf Type classifications between
the High Resolution Layer (HRL) DLT2018 and Vegetation Layer Cover
Continuity (VLCC) DLT2018 surveys. The legend shows: \* White (0):
unchanged areas with no tree cover \* Light Green (1): new broadleaved
cover \* Dark Green (2): new coniferous cover \* Orange (3): loss of
broadleaved cover \* Red (4): loss of coniferous cover \* Light Grey
(11): unchanged areas with broadleaved cover \* Dark Grey (22):
unchanged areas with coniferous cover \* Blue (120): Broadleaved changed
to coniferous \* Cyan (210): Coniferous changed to broadleaved \*
Magenta (254): unclassifiable in any of parent status layers The map
primarily shows large areas of unchanged cover, with significant patches
of “loss of coniferous cover” (red) in the central mountainous regions,
and “Broadleaved changed to coniferous” (blue) appearing in the northern
and western parts of the mapped area.

The bottom map, titled “CLCplus Backbone”, presents a detailed land
cover/land use (LULC) classification. The legend includes: \* Red (1):
Sealed \* Dark Green (2): Woody needle leaved trees \* Light Green (3):
Woody broadleaved deciduous trees \* Lime Green (4): Woody broadleaved
evergreen trees \* Brown (5): Low-growing woody plants \* Light Yellow
(6): Permanent herbaceous \* Yellow (7): Periodically herbaceous \* Pink
(8): Lichens & mosses \* Grey (9): Non and sparsely vegetated \* Dark
Blue (10): Water \* Light Blue (11): Snow & ice This map reveals
extensive forested areas, predominantly “Woody needle leaved trees”
(dark green) and “Woody broadleaved deciduous trees” (light green). A
river valley features “Sealed” (red) areas along its course, leading to
a large “Water” body (dark blue). Patches of “Snow & ice” (light blue)
are visible in the higher elevations.

CLCplus Backbone 2018

Forest areas in the mountainous Alpine relief are often misclassified.
Typical differences between the two surveys are illustrated for Alpine
region, the most characteristic difference is the re-classification of
broadleaved to coniferous by VLCC DLT2018, but similarly typical issue
is the loss of coniferous cover in the new classification. In the
example the latter area was classified as low-growing woody vegetation
by CLCplus Backbone.

### Classification differences VLCC DLT2018 vs CLCplus Backbone 2018

CLCplus Backbone is representing a third independent classification
concerning tree cover information for the European area. Overall
statistics of woody classes were compared to the commonly mapped (EEA38)
area.

<div class="tbl-caption">

Table 25 Overall statistics of VLCC DLT vs CLCplus Backbone for the
reference year of 2018 (sqkm)

</div>

<table data-quarto-postprocess="true">
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 22%" />
<col style="width: 13%" />
</colgroup>
<tbody>
<tr>
<td><strong>DLT class</strong></td>
<td><strong>VLCC<br />
DLT2018</strong></td>
<td><strong>CLCplus Backbone class</strong></td>
<td><strong>CLCplus<br />
Backbone<br />
2018</strong></td>
<td><strong>Difference:<br />
Backbone –<br />
DLT (sqkm)</strong></td>
<td><strong>Difference:<br />
%</strong></td>
</tr>
<tr>
<td>0: no tree cover</td>
<td>3 581 943</td>
<td>0: no tree cover (all other classes)</td>
<td>3 629 182</td>
<td>47 239</td>
<td>1.3%</td>
</tr>
<tr>
<td rowspan="2" style="vertical-align: middle">1: broadleaved trees</td>
<td rowspan="2" style="vertical-align: middle">1 099 650</td>
<td>3: broadleaved deciduous trees</td>
<td>916 188</td>
<td rowspan="2" style="vertical-align: middle">-65 968</td>
<td rowspan="2" style="vertical-align: middle">-6.0%</td>
</tr>
<tr>
<td>4: broadleaved evergreen trees</td>
<td>117 494</td>
</tr>
<tr>
<td>2: coniferous trees</td>
<td>976 398</td>
<td>2: needle leaved trees</td>
<td>995 129</td>
<td>18 731</td>
<td>1.9%</td>
</tr>
<tr>
<td>SUM</td>
<td>5 657 991</td>
<td>SUM</td>
<td>5 657 991</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>All tree cover (1+2)</td>
<td>2 076 049</td>
<td>All tree cover (2+3+4)</td>
<td>2 028 810</td>
<td>-47 237</td>
<td>2.3%</td>
</tr>
</tbody>
</table>

Only few differences (47 237 sqkm, corresponding to 2.3% surplus by
DLT2018) are indicated by overall statistics between the two surveys.
Largest difference (65 968 sqkm, corresponding to 6.0% surplus by
DLT2018) is shown for broadleaved trees.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-45f37abc1d2b9403b968e120e3d10243.png"
data-fig-alt="Choropleth map of Europe illustrating the percentage differences in &#39;All tree cover&#39; between CLCplus Backbone 2018 and VLCC DLT2018. The map covers EU Member States and neighbouring countries, including parts of North Africa and Turkey. The legend defines seven classes of percentage difference: * Dark Green: 20% - 100% (VLCC DLT2018 tree cover surplus) * Green: 10% - 20% (VLCC DLT2018 tree cover surplus) * Light Green: 1% - 10% (VLCC DLT2018 tree cover surplus) * Grey: -1% - 1% (minimal difference) * Light Red: -10% - -1% (VLCC DLT2018 tree cover deficit) * Red: -20% - -10% (VLCC DLT2018 tree cover deficit) * Dark Red: -100% - -20% (VLCC DLT2018 tree cover deficit) The map reveals a significant surplus of tree cover mapped by VLCC DLT2018 compared to CLCplus Backbone 2018 across large areas of Spain and Portugal (dark green and green). Smaller surpluses (light green) are scattered throughout central and eastern Europe. Deficits in tree cover (red and dark red) are noticeable in parts of Scandinavia (e.g., Norway, Sweden, Finland) and along the northern coast of Turkey. Most of the European continent is coloured grey, indicating minimal differences (-1% to 1%) between the two datasets in 2018."
alt="Figure 17 Aggregated difference map of all tree cover differences. Green colours indicate surplus of tree cover mapped by VLCC DLT2018, while red colours indicate surplus of tree cover mapped by CLCplus Backbone 2018." />

Choropleth map of Europe illustrating the percentage differences in “All
tree cover” between CLCplus Backbone 2018 and VLCC DLT2018. The map
covers EU Member States and neighbouring countries, including parts of
North Africa and Turkey. The legend defines seven classes of percentage
difference: \* Dark Green: 20% - 100% (VLCC DLT2018 tree cover surplus)
\* Green: 10% - 20% (VLCC DLT2018 tree cover surplus) \* Light Green:
1% - 10% (VLCC DLT2018 tree cover surplus) \* Grey: -1% - 1% (minimal
difference) \* Light Red: -10% - -1% (VLCC DLT2018 tree cover deficit)
\* Red: -20% - -10% (VLCC DLT2018 tree cover deficit) \* Dark Red:
-100% - -20% (VLCC DLT2018 tree cover deficit)

The map reveals a significant surplus of tree cover mapped by VLCC
DLT2018 compared to CLCplus Backbone 2018 across large areas of Spain
and Portugal (dark green and green). Smaller surpluses (light green) are
scattered throughout central and eastern Europe. Deficits in tree cover
(red and dark red) are noticeable in parts of Scandinavia (e.g., Norway,
Sweden, Finland) and along the northern coast of Turkey. Most of the
European continent is coloured grey, indicating minimal differences (-1%
to 1%) between the two datasets in 2018.

Aggregated tree cover differences were calculated for a 10x10km
statistical grid. Relatively few differences are shown for most of the
European area except the large green spot in Spain-Portugal, indicating
significant surplus of tree cover mapped by DLT2018 compared to CLCplus
Backbone.

### Classification differences HRL DLT2012 vs HRL DLT2015 layers

DLT difference map was calculated in 20m raster resolution between HRL
DLT2012 vs HRL DLT2015 layers. Calculated differences were compared to
available change layers between 2012 and 2015 HRL Forest data.

<div class="tbl-caption">

Table 26 Tree cover differences compared to tree cover changes indicated
by TCCM1215\* data

</div>

| DIFFERENCE CLASS                      | HRL DLT2012 vs HRL DLT2015          |
|---------------------------------------|-------------------------------------|
|                                       | **Tree cover<br>difference (sqkm)** |
| 0: unchanged areas with no tree cover | 3 416 742                           |
| 1: new tree cover                     | 252 031                             |
| 2: loss of tree cover                 | 165 154                             |
| 10: unchanged areas with tree cover   | 1 936 075                           |
| 254: unclassifiable in any status     | 88 164                              |
| **SUM**                               | **5 858 166**                       |

\*Tree Cover Change Mask (TCCM) 2012-2015 data (20m resolution) were not
provided by original HRL Forest 2015 survey (and not included to
corresponding guidelines), but was provided later by HRL Forest 2018
survey.

The Dominant Leaf type Change (DLTC) layer produced by original HRL
Forest 2015 survey was an early version of that kind, is now outdated
and currently no DLTC layer for the 2012-2015 period is published on
CLMS website. The original DLTC1215 layer was produce by combining tree
cover change information with dominant leaf type change and has included
many classes, which cannot link fully to the difference classes derived
by logical combinations of DLTC classes.

<div class="tbl-caption">

Table 27 DLT differences compared to DLT changes indicated by DLTC1215\*
data

</div>

<table data-quarto-postprocess="true">
<colgroup>
<col style="width: 28%" />
<col style="width: 20%" />
<col style="width: 28%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr>
<td><strong>DLT difference class</strong></td>
<td><strong>DLT diff<br />
2012-2015</strong></td>
<td><strong>DLT 2012-2015 change class</strong></td>
<td><strong>DLT change<br />
2012-2015</strong></td>
</tr>
<tr>
<td>0: unchanged areas with no tree cover</td>
<td>3 416 742</td>
<td>0: unchanged areas with no tree cover</td>
<td>3 522 280</td>
</tr>
<tr>
<td>1: new broadleaved cover</td>
<td>209 205</td>
<td>1: new broadleaved cover</td>
<td>83 010</td>
</tr>
<tr>
<td>2: new coniferous cover</td>
<td>42 826</td>
<td>2: new coniferous cover</td>
<td>13 610</td>
</tr>
<tr>
<td>3: loss of broadleaved cover</td>
<td>122 860</td>
<td>3: loss of broadleaved cover</td>
<td>38 957</td>
</tr>
<tr>
<td>4: loss of coniferous cover</td>
<td>42 294</td>
<td>4: loss of coniferous cover</td>
<td>20 658</td>
</tr>
<tr>
<td>11: unchanged broadleaved cover</td>
<td>1 021 618</td>
<td>10: unchanged areas with tree cover</td>
<td>2 040 828</td>
</tr>
<tr>
<td>22: unchanged coniferous cover</td>
<td>745 126</td>
<td>11: broadleaved, increased density</td>
<td>16 559</td>
</tr>
<tr>
<td>120: broadleaved changed to coniferous</td>
<td>73 863</td>
<td>33: broadleaved, decreased density</td>
<td>7 183</td>
</tr>
<tr>
<td>210: coniferous changed to broadleaved</td>
<td>95 469</td>
<td>22: coniferous, increased density</td>
<td>4 663</td>
</tr>
<tr>
<td>254: unclassifiable in any status</td>
<td>88 164</td>
<td>44: coniferous, decreased density</td>
<td>3 062</td>
</tr>
<tr>
<td><strong>SUM</strong></td>
<td><strong>5 858 166</strong></td>
<td>120: broadleaved changed to coniferous</td>
<td>3 062</td>
</tr>
<tr>
<td></td>
<td></td>
<td>210: coniferous changed to broadleaved</td>
<td>15 668</td>
</tr>
<tr>
<td></td>
<td></td>
<td>254: unclassifiable in any status</td>
<td>88 164</td>
</tr>
<tr>
<td></td>
<td></td>
<td><strong>SUM</strong></td>
<td><strong>5 858 166</strong></td>
</tr>
</tbody>
</table>

\*DLTC1215 layer is outdated, not available any more in CLMS website

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-061becf2e843480e6c8eff117b39aed4.png"
data-fig-alt="Choropleth map displaying &#39;All tree cover differences&#39; between the High Resolution Layer (HRL) Distributed Land-use Tree cover (DLT) data for 2012 and 2015 across Europe. The map covers the geographical extent of Europe, including EU Member States, the United Kingdom, Norway, Switzerland, Western Balkans, and Turkey. The legend categorises percentage differences in tree cover into 7 classes: - Dark green: 20% - 100% (increase) - Light green: 10% - 20% (increase) - Pale green: 1% - 10% (increase) - Grey: -1% - 1% (minimal difference) - Pale red: -10% - -1% (decrease) - Red: -20% - -10% (decrease) - Dark red: -100% - -20% (decrease) The map shows areas of notable tree cover increase (green shades) predominantly in Northern Europe (e.g., Scandinavia, Baltic states) and eastern parts of Turkey. Conversely, significant tree cover decreases (red shades) are visible in the Iberian Peninsula (Spain, Portugal), southern France, parts of Italy, and areas of Eastern Europe. Large portions of Central and Western Europe are coloured grey, indicating minimal tree cover difference (between -1% and 1%) between 2012 and 2015."
alt="Figure 18 Aggregated difference map of all tree cover differences. Green colours indicate surplus of tree cover mapped by HRL DLT2015, while red colours indicate surplus of tree cover mapped by HRL DLT2012" />

Choropleth map displaying “All tree cover differences” between the High
Resolution Layer (HRL) Distributed Land-use Tree cover (DLT) data for
2012 and 2015 across Europe. The map covers the geographical extent of
Europe, including EU Member States, the United Kingdom, Norway,
Switzerland, Western Balkans, and Turkey. The legend categorises
percentage differences in tree cover into 7 classes: - Dark green: 20% -
100% (increase) - Light green: 10% - 20% (increase) - Pale green: 1% -
10% (increase) - Grey: -1% - 1% (minimal difference) - Pale red: -10% -
-1% (decrease) - Red: -20% - -10% (decrease) - Dark red: -100% - -20%
(decrease) The map shows areas of notable tree cover increase (green
shades) predominantly in Northern Europe (e.g., Scandinavia, Baltic
states) and eastern parts of Turkey. Conversely, significant tree cover
decreases (red shades) are visible in the Iberian Peninsula (Spain,
Portugal), southern France, parts of Italy, and areas of Eastern Europe.
Large portions of Central and Western Europe are coloured grey,
indicating minimal tree cover difference (between -1% and 1%) between
2012 and 2015.

Aggregated tree cover differences were calculated for a 10x10km
statistical grid. The distribution of all tree cover differences between
the two classifications shows regional variations. The overall vision
based on the statistics and maps is, that tree cover differences are
more the consequence of classification uncertainties of individual
processing units, than of real tree cover changes.

Tree cover changes represent about 40% of all the differences, but no
further information is available about the reliability of change data,
as the only validation result published[^12] was analysing only the 100m
resolution Tree Cover Density Change (TCDC) 2012-2015 data (besides of
TCD and FTY status).

The main findings and recommendations for the HRL TCDC product are
summarised in the report as follows:

- The TCDC layer only meets the minimum accuracy requirement for
  increased and decreased changes with respect to omission errors;
- The TCDC shows very high amount of commission errors which lead to an
  overestimation of changes.
- The next exercise for the production of the Forest layer should
  include the reprocessing of the change layers.
- Results provided at bio-geographical regions and country/group of
  country level, should provide a sound basis for further improving the
  product.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-7dfcbadafc51b6367027b5d57c9b939a.png"
data-fig-alt="This image displays two maps showing aggregated tree cover differences and changes, likely within a 10x10km statistical grid, based on Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Dominant Leaf Type (DLT) data. The top map, titled &#39;Difference map: HRL DLT2012 vs VLCC DLT2015,&#39; illustrates discrepancies between two tree cover classifications from 2012 and 2015. Its legend defines the following colour codes: * White: 0: unchanged areas with no tree cover * Light green: 1: new broadleaved cover * Dark green: 2: new coniferous cover * Orange: 3: loss of broadleaved cover * Red: 4: loss of coniferous cover * Light grey: 11: unchanged areas with broadleaved cover * Dark grey: 22: unchanged areas with coniferous cover * Dark blue: 120: Broadleaved changed to coniferous * Light blue: 210: Coniferous changed to broadleaved * Magenta: 254: unclassifiable in any of parent status layers The bottom map, titled &#39;DLT CHANGE MAP 2012-2015 (outdated),&#39; shows tree cover changes between 2012 and 2015. Its legend includes: * White: 0: unchanged areas with no tree cover * Light green: 1: new broadleaved cover - increased tree cover * Dark green: 2: new coniferous cover - increased tree cover * Orange: 3: loss of broadleaved cover - decreased tree cover * Red: 4: loss of coniferous cover - decreased tree cover * Grey: 10: unchanged areas with tree cover * Pale green: 11: increased broadleaved cover density * Cyan: 22: increased coniferous cover density * Pale brown: 33: decreased broadleaved cover density * Dark brown: 44: decreased coniferous cover density * Dark blue: 120: broadleaved changed to coniferous * Light blue: 210: coniferous changed to broadleaved * Magenta: 254: unclassifiable in any of parent status layers Both maps display a mosaic of land cover types, with large areas indicating &#39;unchanged&#39; status (white, light grey, dark grey in the top map; white, grey in the bottom map). Areas of &#39;loss of broadleaved cover&#39; (orange) and &#39;loss of coniferous cover&#39; (red) are distributed alongside &#39;new broadleaved cover&#39; (light green) and &#39;new coniferous cover&#39; (dark green). Prominent magenta areas indicate unclassifiable regions. The spatial distribution of differences and changes suggests regional variations, with significant patches of tree cover gains and losses, as well as shifts between broadleaved and coniferous types."
alt="Figure 19 DLT changes and differences between 2012-2015 x,y = 4552489,4083593 - close to Nordmark, Sweden" />

This image displays two maps showing aggregated tree cover differences
and changes, likely within a 10x10km statistical grid, based on
Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL)
Dominant Leaf Type (DLT) data.

The top map, titled “Difference map: HRL DLT2012 vs VLCC DLT2015,”
illustrates discrepancies between two tree cover classifications from
2012 and 2015. Its legend defines the following colour codes: \* White:
0: unchanged areas with no tree cover \* Light green: 1: new broadleaved
cover \* Dark green: 2: new coniferous cover \* Orange: 3: loss of
broadleaved cover \* Red: 4: loss of coniferous cover \* Light grey: 11:
unchanged areas with broadleaved cover \* Dark grey: 22: unchanged areas
with coniferous cover \* Dark blue: 120: Broadleaved changed to
coniferous \* Light blue: 210: Coniferous changed to broadleaved \*
Magenta: 254: unclassifiable in any of parent status layers

The bottom map, titled “DLT CHANGE MAP 2012-2015 (outdated),” shows tree
cover changes between 2012 and 2015. Its legend includes: \* White: 0:
unchanged areas with no tree cover \* Light green: 1: new broadleaved
cover - increased tree cover \* Dark green: 2: new coniferous cover -
increased tree cover \* Orange: 3: loss of broadleaved cover - decreased
tree cover \* Red: 4: loss of coniferous cover - decreased tree cover \*
Grey: 10: unchanged areas with tree cover \* Pale green: 11: increased
broadleaved cover density \* Cyan: 22: increased coniferous cover
density \* Pale brown: 33: decreased broadleaved cover density \* Dark
brown: 44: decreased coniferous cover density \* Dark blue: 120:
broadleaved changed to coniferous \* Light blue: 210: coniferous changed
to broadleaved \* Magenta: 254: unclassifiable in any of parent status
layers

Both maps display a mosaic of land cover types, with large areas
indicating “unchanged” status (white, light grey, dark grey in the top
map; white, grey in the bottom map). Areas of “loss of broadleaved
cover” (orange) and “loss of coniferous cover” (red) are distributed
alongside “new broadleaved cover” (light green) and “new coniferous
cover” (dark green). Prominent magenta areas indicate unclassifiable
regions. The spatial distribution of differences and changes suggests
regional variations, with significant patches of tree cover gains and
losses, as well as shifts between broadleaved and coniferous types.

Dominant Leaf Type Change (DLTC) 2012-2015 (outdated map and
classification)

In order to gain exact statistics and be able to visualize all
differences between DLT2012 and DLT2015 classifications DLT difference
map was calculated in 20m raster resolution, where all possible
combinations were considered. The high-resolution difference map between
HRL DLT2012 and HRL DLT2015 survey results indicate especially large
variations in tree cover classifications Mediterranean, Scandinavian and
Alpine regions. Unclassified areas due to cloud cover occur in many
places sporadically across Europe, but extreme large unclassified areas
are appearing in Scandinavian region.

### Classification differences HRL DLT2015 vs HRL DLT2018 layers

DLT difference map was calculated in 10m raster resolution between HRL
DLT2015 vs HRL DLT2018 layers. Calculated differences were compared to
available change layers between 2015 and 2018 HRL Forest data.

<div class="tbl-caption">

Table 28 Tree cover differences compared to tree cover changes indicated
by TCCM1518 data

</div>

| DIFFERENCE CLASS                      | HRL DLT2015 vs HRL DLT2018          |
|---------------------------------------|-------------------------------------|
|                                       | **Tree cover<br>difference (sqkm)** |
| 0: unchanged areas with no tree cover | 3 413 593                           |
| 1: new tree cover                     | 217 626                             |
| 2: loss of tree cover                 | 244 492                             |
| 10: unchanged areas with tree cover   | 1 981 069                           |
| 254: unclassifiable in any status     | 734                                 |
| **SUM**                               | **5 857 514**                       |

Both Tree Cover Change mask (TCCM) and Dominant Leaf Type Change (DLTC)
layers were provided by the HRL Forest 2018 survey in 20m resolution.
With the aggregation of thematic classes, DLT difference classes may be
linked to TCCM classes directly.

HRL DLT2015 (20m resolution) and HRL DLT2018 (10m resolution) layers
cannot be considered as consistent, not only because of the different
spatial resolution, but statistically the difference of the layers is
obviously not corresponding to the changes derived, the changes
represent only 0.9% (broadleaved trees) and 7.2% (coniferous trees) of
the differences.

With the merge of thematic classes, DLT difference classes may be linked
to DLTC classes directly, but as the DLTC layer does not include (by
definition) all combinations of possible DLT differences, DLTC layers
cannot be directly used in an backdating (“accounting”) process.

<div class="tbl-caption">

Table 29 DLT differences compared to DLT changes indicated by DLT1518
data

</div>

<table style="width:100%;" data-quarto-postprocess="true">
<colgroup>
<col style="width: 22%" />
<col style="width: 16%" />
<col style="width: 23%" />
<col style="width: 21%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr>
<td><strong>DLT difference class</strong></td>
<td><strong>DLT diff<br />
2015-<br />
2018</strong></td>
<td><strong>DLT 2012-2015 change class</strong></td>
<td><strong>DLT<br />
change<br />
2015-2018</strong></td>
<td><strong>Change /<br />
difference</strong></td>
</tr>
<tr>
<td>0: unchanged areas with no tree cover</td>
<td>3 413 593</td>
<td>0: unchanged areas with no<br />
tree cover</td>
<td>3 619 816</td>
<td>106.0%</td>
</tr>
<tr>
<td>1: new broadleaved cover</td>
<td>177 655</td>
<td>1: new broadleaved cover</td>
<td>1 239</td>
<td>0.7%</td>
</tr>
<tr>
<td>2: new coniferous cover</td>
<td>39 971</td>
<td>2: new coniferous cover</td>
<td>718</td>
<td>1.8%</td>
</tr>
<tr>
<td>3: loss of broadleaved cover</td>
<td>184 629</td>
<td>3: loss of broadleaved cover</td>
<td>5 415</td>
<td>2.9%</td>
</tr>
<tr>
<td>4: loss of coniferous cover</td>
<td>59 863</td>
<td>4: loss of coniferous cover</td>
<td>12 095</td>
<td>20.2%</td>
</tr>
<tr>
<td>11: unchanged broadleaved cover</td>
<td>988 726</td>
<td rowspan="2" style="vertical-align: middle">10: unchanged areas with
tree<br />
cover</td>
<td rowspan="2" style="vertical-align: middle">2 271 876</td>
<td rowspan="2" style="vertical-align: middle">132.7%</td>
</tr>
<tr>
<td>22: unchanged coniferous cover</td>
<td>722 894</td>
</tr>
<tr>
<td>120: broadleaved changed to coniferous</td>
<td>167 458</td>
<td rowspan="2" style="vertical-align: middle">12: potential change
among<br />
dominant leaf type</td>
<td rowspan="2" style="vertical-align: middle">313</td>
<td rowspan="2" style="vertical-align: middle">0.1%</td>
</tr>
<tr>
<td>210: coniferous changed to broadleaved</td>
<td>101 991</td>
</tr>
<tr>
<td>254: unclassifiable in any status</td>
<td>734</td>
<td>254: unclassifiable in any<br />
status</td>
<td>734</td>
<td>100.0%</td>
</tr>
<tr>
<td><strong>SUM</strong></td>
<td><strong>5 857 514</strong></td>
<td><strong>SUM</strong></td>
<td><strong>5 912 166</strong></td>
<td><strong>100.9%</strong></td>
</tr>
</tbody>
</table>

Changes in DLTC layer represent only the minority of all differences,
all the rest of differences were considered as “technical change” and
filtered out. Relatively high share (20.2%) of differences were kept in
case of DLTC class 4 (loss of coniferous forest).

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-b2078f1bad220032b9ee35fdd2023818.png"
data-fig-alt="Choropleth map displaying &#39;All tree cover differences&#39; between the High Resolution Layer Dominant Leaf Type (HRL DLT) datasets from 2015 and 2018, covering Europe, including EU Member States and surrounding countries. The legend categorises percentage differences into seven classes: * Dark Green: 20% - 100% (increase) * Light Green: 10% - 20% (increase) * Pale Green: 1% - 10% (increase) * Grey: -1% - 1% (stable or minimal difference) * Pale Red: -10% - -1% (decrease) * Red: -20% - -10% (decrease) * Dark Red: -100% - -20% (decrease) Areas showing significant tree cover increases (green shades) are present across parts of Ireland, the UK, France, Poland, the Baltic States, Ukraine, Italy, Greece, and coastal Turkey. Significant tree cover decreases (red shades) are visible in northern Scandinavia (Sweden, Finland), central Europe (Germany, Czechia, Austria), Portugal, parts of Spain, the Carpathian Mountains, the Balkan peninsula, and parts of Turkey. The majority of the mapped area is coloured grey, indicating relatively stable tree cover or minimal differences between the two HRL DLT classification years. The map highlights classification differences rather than necessarily real tree cover changes."
alt="Figure 20 Aggregated difference map of all tree cover differences. Green colours indicate surplus of tree cover mapped by HRL DLT2018, while red colours indicate surplus of tree cover mapped by HRL DLT2015." />

Choropleth map displaying “All tree cover differences” between the High
Resolution Layer Dominant Leaf Type (HRL DLT) datasets from 2015 and
2018, covering Europe, including EU Member States and surrounding
countries. The legend categorises percentage differences into seven
classes: \* Dark Green: 20% - 100% (increase) \* Light Green: 10% - 20%
(increase) \* Pale Green: 1% - 10% (increase) \* Grey: -1% - 1% (stable
or minimal difference) \* Pale Red: -10% - -1% (decrease) \* Red: -20% -
-10% (decrease) \* Dark Red: -100% - -20% (decrease) Areas showing
significant tree cover increases (green shades) are present across parts
of Ireland, the UK, France, Poland, the Baltic States, Ukraine, Italy,
Greece, and coastal Turkey. Significant tree cover decreases (red
shades) are visible in northern Scandinavia (Sweden, Finland), central
Europe (Germany, Czechia, Austria), Portugal, parts of Spain, the
Carpathian Mountains, the Balkan peninsula, and parts of Turkey. The
majority of the mapped area is coloured grey, indicating relatively
stable tree cover or minimal differences between the two HRL DLT
classification years. The map highlights classification differences
rather than necessarily real tree cover changes.

Aggregated tree cover differences were calculated for a 10x10km
statistical grid. The distribution of all tree cover differences between
the two classifications shows regional variations. The overall vision
based on the statistics and maps is, that tree cover differences are
more the consequence of classification uncertainties of individual
processing units, than of real tree cover changes.

Only limited information is available about the reliability of change
data, as no European validation results were published for HRL Forest
2018 products. On the other hand, DLTC1518 layer was verified by EEA
Member States and the evaluation report is available[^13]. Main
conclusions of the MS verification are:

- The average look and feel evaluation result for HRL DLTC 2015-2018
  layer was 2.9 (acceptable);
- The best-performing class was the “loss of coniferous cover (4)” with
  (good) overall result;
- The lowest result appeared at “potential change among leaf types (12)”
  class as 1.7 (insufficient);
- The other three classes reached “acceptable” level, class “new
  broadleaved cover (1)” with the lowest score among them: 2.5;
- Class “new coniferous cover (2)” with 2.9 and class “loss of
  broadleaved cover (3)” with the highest score among them, exceeding
  overall average, as 3.3.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-98b8e29d7fc14df7ed2c4f7b356944b2.png"
data-fig-alt="Two maps displaying land cover changes and differences in Dominant Leaf Type (DLT) at 10 m resolution. Both maps cover a local or regional land area. The top map is titled &#39;DLT DIFFERENCE MAP&#39; and is specifically captioned &#39;Difference map: HRL DLT2015 vs VLCC DLT2018 (10m resolution)&#39;. It classifies changes and differences into ten categories: * White (0): unchanged areas with no tree cover * Light Green (1): new broadleaved cover * Dark Green (2): new coniferous cover * Orange (3): loss of broadleaved cover * Red (4): loss of coniferous cover * Light Grey (11): unchanged areas with broadleaved cover * Dark Grey (22): unchanged areas with coniferous cover * Blue (120): Broadleaved changed to coniferous * Cyan (210): Coniferous changed to broadleaved * Magenta (254): unclassifiable in any of parent status layers This map shows a heterogeneous distribution of various change types, with significant areas of unchanged broadleaved (light grey) and coniferous (dark grey) cover, alongside patches of new tree cover (green), losses (orange/red), and shifts between broadleaved and coniferous (blue/cyan). The bottom map is titled &#39;DLT CHANGE MAP 2015-2018&#39;. It classifies changes into eight categories: * White (0): unchanged areas with no tree cover * Light Green (1): new broadleaved cover * Dark Green (2): new coniferous cover * Orange (3): loss of broadleaved cover * Red (4): loss of coniferous cover * Grey (10): unchanged areas with tree cover * Yellow (12): potential change among dominant leaf types * Magenta (254): unclassifiable in any of parent status layers This map presents a more aggregated view of change, primarily highlighting unchanged areas (grey and white) and areas of tree cover loss (red and orange). Compared to the difference map, it simplifies the &#39;unchanged&#39; tree cover categories into a single class (grey) and includes a &#39;potential change among dominant leaf types&#39; (yellow) category."
alt="Figure 21 DLT changes and differences between 2015-2018 х,у = 4600625,2848324 - close to Klaffenstrass, Germany / Austria." />

Two maps displaying land cover changes and differences in Dominant Leaf
Type (DLT) at 10 m resolution. Both maps cover a local or regional land
area.

The top map is titled “DLT DIFFERENCE MAP” and is specifically captioned
“Difference map: HRL DLT2015 vs VLCC DLT2018 (10m resolution)”. It
classifies changes and differences into ten categories: \* White (0):
unchanged areas with no tree cover \* Light Green (1): new broadleaved
cover \* Dark Green (2): new coniferous cover \* Orange (3): loss of
broadleaved cover \* Red (4): loss of coniferous cover \* Light Grey
(11): unchanged areas with broadleaved cover \* Dark Grey (22):
unchanged areas with coniferous cover \* Blue (120): Broadleaved changed
to coniferous \* Cyan (210): Coniferous changed to broadleaved \*
Magenta (254): unclassifiable in any of parent status layers This map
shows a heterogeneous distribution of various change types, with
significant areas of unchanged broadleaved (light grey) and coniferous
(dark grey) cover, alongside patches of new tree cover (green), losses
(orange/red), and shifts between broadleaved and coniferous (blue/cyan).

The bottom map is titled “DLT CHANGE MAP 2015-2018”. It classifies
changes into eight categories: \* White (0): unchanged areas with no
tree cover \* Light Green (1): new broadleaved cover \* Dark Green (2):
new coniferous cover \* Orange (3): loss of broadleaved cover \* Red
(4): loss of coniferous cover \* Grey (10): unchanged areas with tree
cover \* Yellow (12): potential change among dominant leaf types \*
Magenta (254): unclassifiable in any of parent status layers This map
presents a more aggregated view of change, primarily highlighting
unchanged areas (grey and white) and areas of tree cover loss (red and
orange). Compared to the difference map, it simplifies the ‘unchanged’
tree cover categories into a single class (grey) and includes a
‘potential change among dominant leaf types’ (yellow) category.

Dominant Leaf Type Change (DLTC) 2015-2018 (20m resolution)

In order to gain exact statistics and be able to visualize all
differences between HRL DLT2015 and HRL DLT2018 classifications DLT
difference map was calculated in 10m raster resolution, where all
possible combinations were considered. The high-resolution difference
map between HRL DLT2018 and HRL DLT2018 survey results indicate
especially large variations in tree cover classifications Mediterranean,
Scandinavian and in mountainous regions.

------------------------------------------------------------------------

### Classification differences VLCC DLT2018 vs VLCC DLT2021 layers

DLT difference map was calculated in 10m raster resolution between VLCC
DLT2018 vs VLCC DLT2021 layers. Calculated differences were compared to
available change layers between 2018 and 2021 VLCC Forest data.

<div class="tbl-caption">

Table 30 Tree cover differences compared to tree cover changes indicated
by TCPC1821 data

</div>

| DIFFERENCE CLASS | HRL DLT2015 vs HRL DLT2018 |  |  |
|----|----|----|----|
|  | **Tree cover<br>difference (sqkm)** | **Tree cover change<br>(sqkm)** | **Change / difference<br>%** |
| 0: unchanged areas with no tree cover | 3 576 183 | 3 525 896 | 98,6% |
| 1: new tree cover | 6 815 | 2 187 | 32,1% |
| 2: loss of tree cover | 34 521 | 21 204 | 61,4% |
| 10: unchanged areas with tree cover | 2 041 527 | 2 109 759 | 103,3% |
| 254: unclassifiable in any status | \- | \- | \- |
| **SUM** | **5 659 046** | **5 659 046** | **100,0%** |

VLCC DLT layers were produced for each reference year in the 2018-2021
period, both change layers Tree Cover Presence Change (PCPC, new name
for TCCM in previous surveys) and Dominant Leaf Type Change (DLTC)
layers were provided by the VLCC Forest 2018-2021 survey in 20m
resolution to cover the full 3 yearly period.

With the merge of thematic classes, DLT difference classes may be linked
to DLTC classes directly, but as the DLTC layer does not include (by
definition) all combinations of possible DLT differences, DLTC layers
cannot be directly used in a backdating (“accounting”) process.

<div class="tbl-caption">

Table 31 DLT differences compared to DLT changes indicated by DLT1821
data

</div>

<table data-quarto-postprocess="true">
<colgroup>
<col style="width: 23%" />
<col style="width: 17%" />
<col style="width: 24%" />
<col style="width: 19%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr>
<td><strong>DLT difference class</strong></td>
<td><strong>DLT diff<br />
2015-2018</strong></td>
<td><strong>DLT 2012-2015 change class</strong></td>
<td><strong>DLT change<br />
2015-2018</strong></td>
<td><strong>Change /<br />
difference</strong></td>
</tr>
<tr>
<td>0: unchanged areas with no tree cover</td>
<td>3 576 183</td>
<td>0: unchanged areas with no tree cover</td>
<td>3 525 896</td>
<td>98.6%</td>
</tr>
<tr>
<td>1: new broadleaved cover</td>
<td>4 888</td>
<td>1: new broadleaved cover</td>
<td>1 660</td>
<td>34.0%</td>
</tr>
<tr>
<td>2: new coniferous cover</td>
<td>1 927</td>
<td>2: new coniferous cover</td>
<td>528</td>
<td>27.4%</td>
</tr>
<tr>
<td>3: loss of broadleaved cover</td>
<td>11 203</td>
<td>3: loss of broadleaved cover</td>
<td>4 301</td>
<td>38.4%</td>
</tr>
<tr>
<td>4: loss of coniferous cover</td>
<td>23 319</td>
<td>4: loss of coniferous cover</td>
<td>16 903</td>
<td>72.5%</td>
</tr>
<tr>
<td>11: unchanged broadleaved cover</td>
<td>1 088 448</td>
<td rowspan="2" style="vertical-align: middle">10: unchanged areas with
tree cover</td>
<td rowspan="2" style="vertical-align: middle">2 109 759</td>
<td rowspan="2" style="vertical-align: middle">103.3%</td>
</tr>
<tr>
<td>22: unchanged coniferous cover</td>
<td>953 080</td>
</tr>
<tr>
<td>120: broadleaved changed to coniferous</td>
<td>-</td>
<td rowspan="2" style="vertical-align: middle">12: potential change
among dominant leaf type</td>
<td rowspan="2" style="vertical-align: middle">-</td>
<td rowspan="2" style="vertical-align: middle">-</td>
</tr>
<tr>
<td>210: coniferous changed to broadleaved</td>
<td>-</td>
</tr>
<tr>
<td>254: unclassifiable in any status</td>
<td>-</td>
<td>254: unclassifiable in any status</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td><strong>SUM</strong></td>
<td><strong>5 659 064</strong></td>
<td><strong>SUM</strong></td>
<td><strong>5 659 064</strong></td>
<td><strong>100.0%</strong></td>
</tr>
</tbody>
</table>

No re-classification between broadleaved to coniferous neither
vice-versa is appearing in DLT differences, neither class 12 (potential
change among dominant leaf type) is appearing in DLTC1821 layer, this is
unique in the whole of DLT time-series - VLCC DLT layers were produced
obviously in a technically harmonized way.

TCPC and DLTC changes represent almost all differences except that a
Minimum Mapping Unit (MMU = 1ha) was applied. TCPC and DLTC changes
represent between 27-72% of all differences depending on change classes,
where the missing changes correspond to differences appearing as
contiguous patches with a size smaller than 1 ha.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-5ac0950a64c5e4c7d0c4ea5b8926aea4.png"
data-fig-alt="Choropleth map displaying &#39;All tree cover differences&#39; across Europe between the Very Large Coverage Component Dominant Leaf Type (VLCC DLT) classifications of 2018 and 2021. The map uses a seven-class diverging colour scale to represent percentage change in tree cover: - Dark Green: 20% - 100% (increase) - Light Green: 10% - 20% (increase) - Pale Green: 1% - 10% (increase) - Light Grey: -1% - 1% (minimal change) - Pale Red: -10% - -1% (decrease) - Red: -20% - -10% (decrease) - Dark Red: -100% - -20% (decrease) The map shows widespread areas of minimal tree cover change (light grey) across much of central and northern Europe. Significant decreases in tree cover (pale red, red, dark red) are evident across large parts of Scandinavia (Finland, Sweden), the Iberian Peninsula (Portugal, Spain), parts of central Europe (e.g., Czechia, Poland, Germany), and the Balkans (Greece, Bulgaria, Romania). Areas with increases in tree cover (green shades) are less prominent and are scattered, notably appearing in the Iberian Peninsula."
alt="Figure 22 Aggregated difference map of all tree cover differences. Green colours indicate surplus of tree cover mapped by VLCC DLT2021, while red colours indicate surplus of tree cover mapped by VLCC DLT2018." />

Choropleth map displaying “All tree cover differences” across Europe
between the Very Large Coverage Component Dominant Leaf Type (VLCC DLT)
classifications of 2018 and 2021. The map uses a seven-class diverging
colour scale to represent percentage change in tree cover: - Dark Green:
20% - 100% (increase) - Light Green: 10% - 20% (increase) - Pale Green:
1% - 10% (increase) - Light Grey: -1% - 1% (minimal change) - Pale Red:
-10% - -1% (decrease) - Red: -20% - -10% (decrease) - Dark Red: -100% -
-20% (decrease)

The map shows widespread areas of minimal tree cover change (light grey)
across much of central and northern Europe. Significant decreases in
tree cover (pale red, red, dark red) are evident across large parts of
Scandinavia (Finland, Sweden), the Iberian Peninsula (Portugal, Spain),
parts of central Europe (e.g., Czechia, Poland, Germany), and the
Balkans (Greece, Bulgaria, Romania). Areas with increases in tree cover
(green shades) are less prominent and are scattered, notably appearing
in the Iberian Peninsula.

Aggregated tree cover differences were calculated for a 10x10km
statistical grid. The distribution of all tree cover differences between
the two classifications shows slight decrease of tree cover over
Scandinavia and sporadically across Europe except some Mediterranean
locations mostly in Spain or Portugal.

The overall vision is, that tree cover differences may correspond mostly
to real tree cover changes, however no external QA/QC results are
available yet for VLCC Forest data.

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-f770bcedbbb18535f245fc8051a8a75b.png"
data-fig-alt="This image displays two detailed maps comparing Dominant Leaf Type (DLT) products from the Copernicus Land Monitoring Service (CLMS) Very High Resolution (VHR) Land Cover Classification (VLCC) for the years 2018 and 2021 in an unlabelled sample area. The top map, titled &#39;DLT DIFFERENCE MAP: VLCC DLT2018 vs VLCC DLT2021&#39;, illustrates differences between the two reference years with the following legend: * White: 0: unchanged areas with no tree cover * Light Green: 1: new broadleaved cover * Dark Green: 2: new coniferous cover * Orange: 3: loss of broadleaved cover * Red: 4: loss of coniferous cover * Light Grey: 11: unchanged areas with broadleaved cover * Dark Grey: 22: unchanged areas with coniferous cover * Blue: 120: Broadelaevd changed to coniferous * Cyan: 210: Coniferous changed to broadleaved * Magenta: 254: unclassifiable in any of parent status layers The bottom map, titled &#39;DLT CHANGE MAP 2018-2021&#39;, shows aggregated changes from 2018 to 2021 with the following legend: * White: 0: unchanged areas with no tree cover * Light Green: 1: new broadleaved cover * Dark Green: 2: new coniferous cover * Orange: 3: loss of broadleaved cover * Red: 4: loss of coniferous cover * Grey: 10: unchanged areas with tree cover * Magenta: 254: unclassifiable in any of parent status layers Both maps prominently display large areas of unchanged tree cover (grey) and unchanged areas with no tree cover (white). Losses of coniferous cover (red patches) are widespread across the mapped area. New broadleaved cover (light green), new coniferous cover (dark green), and loss of broadleaved cover (orange) are also visible but less extensive. Categories 120 (Broadelaevd changed to coniferous) and 210 (Coniferous changed to broadleaved) are present in the legend of the DLT DIFFERENCE MAP but are visually negligible on the map, consistent with information stating these re-classifications are not appearing in the DLT differences. The DLT CHANGE MAP simplifies unchanged tree cover into a single grey class (10) compared to the more detailed broadleaved/coniferous distinction (11/22) in the DLT DIFFERENCE MAP."
alt="Figure 23 DLT changes and differences between 2018-2021. DLT changes and differences in the patch size range larger than 1ha seem to be almost identical. x,y = 4600625, 2848324 - close to Lysa, Czech Republic" />

This image displays two detailed maps comparing Dominant Leaf Type (DLT)
products from the Copernicus Land Monitoring Service (CLMS) Very High
Resolution (VHR) Land Cover Classification (VLCC) for the years 2018 and
2021 in an unlabelled sample area.

The top map, titled “DLT DIFFERENCE MAP: VLCC DLT2018 vs VLCC DLT2021”,
illustrates differences between the two reference years with the
following legend: \* White: 0: unchanged areas with no tree cover \*
Light Green: 1: new broadleaved cover \* Dark Green: 2: new coniferous
cover \* Orange: 3: loss of broadleaved cover \* Red: 4: loss of
coniferous cover \* Light Grey: 11: unchanged areas with broadleaved
cover \* Dark Grey: 22: unchanged areas with coniferous cover \* Blue:
120: Broadelaevd changed to coniferous \* Cyan: 210: Coniferous changed
to broadleaved \* Magenta: 254: unclassifiable in any of parent status
layers

The bottom map, titled “DLT CHANGE MAP 2018-2021”, shows aggregated
changes from 2018 to 2021 with the following legend: \* White: 0:
unchanged areas with no tree cover \* Light Green: 1: new broadleaved
cover \* Dark Green: 2: new coniferous cover \* Orange: 3: loss of
broadleaved cover \* Red: 4: loss of coniferous cover \* Grey: 10:
unchanged areas with tree cover \* Magenta: 254: unclassifiable in any
of parent status layers

Both maps prominently display large areas of unchanged tree cover (grey)
and unchanged areas with no tree cover (white). Losses of coniferous
cover (red patches) are widespread across the mapped area. New
broadleaved cover (light green), new coniferous cover (dark green), and
loss of broadleaved cover (orange) are also visible but less extensive.
Categories 120 (Broadelaevd changed to coniferous) and 210 (Coniferous
changed to broadleaved) are present in the legend of the DLT DIFFERENCE
MAP but are visually negligible on the map, consistent with information
stating these re-classifications are not appearing in the DLT
differences. The DLT CHANGE MAP simplifies unchanged tree cover into a
single grey class (10) compared to the more detailed
broadleaved/coniferous distinction (11/22) in the DLT DIFFERENCE MAP.

Dominant Leaf Type Change (VLCC DLTC) 2018-2021

In order to gain exact statistics and be able to visualize all
differences between VLCC DLT2018 and VLCC DLT2021 classifications DLT
difference map was calculated in 10m raster resolution, where all
possible combinations were considered.

The 10m resolution difference map between HRL DLT2018 and HRL DLT2018
surveys corresponds exactly to DLTC1821 change map except that:

- Difference map was produced in 10m resolution while DLTC map is
  provided in 20m resolution;
- Contiguous tree cover difference patches smaller than 1ha were
  eliminated from DLTC;
- Difference classes 11 (unchanged broadleaved) and 22 (unchanged
  coniferous) were merged to DLTC class 10 (unchanged areas with tree
  cover.

## Discussion of the mapping concepts applied for creating HRL Forest layers

The post classification comparison change mapping method is applied for
most of raster-based CLMS products, supplemented by the semi-automatic
separation of technical changes from real land cover changes.

Main and simplified steps of the complex processing are:

1.  Creating status layer for first reference year by complex
    classification procedure;
2.  Creating status layer for second reference year by complex
    classification procedure;
3.  Creating difference layer by GIS procedure;
4.  Separation of technical changes from real changes by semi-automatic
    procedures, creating change layer for publication.

Previous tree cover change layers for 2012-2015 and 2015-2018 period
have followed the above steps. This has resulted more or less reliable
tree cover change layers, but the status layers in the time-series were
not harmonized, the difference of the status layers have shown
significantly larger differences than changes appearing in TCCM or DLTC
layers.

The new VLCC Forest survey is providing technically harmonized
time-series of all primary tree cover data (TCD, DLT, FTY status and
TCPC & DLTC changes) for the 2018-2021 period. The high level of
technical consistency is unique among HRL Forest layers, but among other
high resolution land cover layers (HRL Imperviousness or CLCplus
Backbone) as well.

To reach this level, the additional step was introduced to the
processing:

5.  Artificial harmonization of the status layers, by creating the new
    status as a combination of previous status and real changes gained
    in step 4;

This step was obviously included to a more complex procedure applied to
harmonize all of the status layers between 2018 and 2021, as not only
these two layers, but all of them (2018-2019-2020-2021) proved to be
technically harmonized both in terms of both: Calibration of TCD values
and consistent classification tree cover, including leaf type.

Additional steps were applied to gain final tree cover change data:

6.  Elimination of contiguous patches of tree cover smaller than 1ha
    MMU;
7.  Resampling 10m intermediate tree cover change data to 20m
    resolution.

Steps 6 & 7 have introduced slight technical inconsistency between tree
cover status and change data, the simple requirement

$$Change = New status – Old status$$

is obviously not fulfilled, although VLCC Forest layers are technically
close to be perfectly consistent.

Remaining questions are be answered:

- Is the MMU of 1ha a good choice to improve the reliability of tree
  cover change data?
- Are valuable changes lost with the introduction of 1ha MMU? If yes,
  what is the recommended value for the MMU?
- How the resampling the change data to 20m is affecting the quality? Is
  it really necessary?
- Would be worth to make tree cover status and change data fully
  consistent?

### Effect of 1ha MMU applied to VLCC Forest change data

While the high level of technical consistency and plausible change
figures in terms of statistical tables and difference maps show the data
to be close to perfect, no extensive QA/QC results are available yet to
provide overall figures about data quality.

A common experience with HR LCLU layers is that the change data also
contain many 1-2 pixel change patches, which statistically account for
the largest mass of all changes, while they do not represent real
change, but are mostly identified as noise due to the uncertainty of the
classifications. For this reason, filtering out small patches of change
seems to be a very good idea, as confirmed by the preliminary quality
control results performed on preliminary delivery of VLCC Forest data,
where the reliability of remaining (larger than 1 ha) changes proved to
be rather high. On the other hand, the question is what we lose by
applying 1ha MMU - verification exercises usually do not check missing
changes.

In order to have an idea about the effect of applying 1ha MMU to VLCC
Forest change data, the difference of VLCC FLT2018 and VLCC DLT2021 was
examined in more detail.

**Data preparation**

Step 1: Tree cover difference map was calculated in 10m raster
resolution with the combination of VLCC DLT2018 and VLCC DLT2021 data.
Leaf type classification was not considered, only the presence or
absence of tree cover.

Step 2: The tree cover difference map was vectorized. The distribution
of tree cover differences by size of contiguous difference patches was
calculated (Table 32)

<div class="tbl-caption">

Table 32 Distribution of the aggregated area of tree cover difference
polygons by patch size ranges

</div>

<table data-quarto-postprocess="true">
<colgroup>
<col style="width: 30%" />
<col style="width: 14%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2" style="vertical-align: middle"><strong>Patch
size</strong></td>
<td colspan="2"><strong>New tree cover</strong></td>
<td colspan="2"><strong>Loss of tree cover</strong></td>
</tr>
<tr>
<td><strong>sqkm</strong></td>
<td><strong>%</strong></td>
<td><strong>sqkm</strong></td>
<td><strong>%</strong></td>
</tr>
<tr>
<td>Smaller than 0.1ha</td>
<td>2 044</td>
<td>30.0%</td>
<td>3 343</td>
<td>9.7%</td>
</tr>
<tr>
<td>0.1ha – 1ha</td>
<td>2 243</td>
<td>32.9%</td>
<td>7 638</td>
<td>22.1%</td>
</tr>
<tr>
<td>Greater or equal than 1ha</td>
<td>2 528</td>
<td>37.1%</td>
<td>23 540</td>
<td>68.2%</td>
</tr>
<tr>
<td><strong>All changes</strong></td>
<td><strong>6 815</strong></td>
<td><strong>100.0%</strong></td>
<td><strong>34 521</strong></td>
<td><strong>100.0%</strong></td>
</tr>
</tbody>
</table>

The effect of 1ha MMU shows different picture considering gain or loss
of tree cover:

- In case of new tree cover most of the differences (62.9%) is lost due
  to the applied 1ha MMU;
- In case of loss of tree cover still significant amount (31.8%) of
  differences is lost due to the applied 1ha MMU.

Due to the high level of harmonization between VLCC Forest layers the
difference of tree cover status layers in the size range greater or
equal to 1ha is almost fully compliant with TCPC change data, except
slight differences, probably due to the effect of the aggregation of 10m
difference raster to 20m:

- 2 528 sqkm difference in case of new tree cover against 2 187 sqkm in
  TCPC class 1;
- 23 540 sqkm difference in case of loss of tree cover against 21 204 in
  TCPC class 2.

Resources in the frames of this task did not allow to perform an
extensive quality check of tree cover change data, but we have used the
part of the limited resources to verify the validity of tree cover
differences as real changes under the 1ha MMU patch size limit.

#### Verification methodology

Step 1: Tree cover difference polygons in the size range of 0.1-1ha
(corresponding to 10-99 contiguous tree covered raster cells) were
pre-selected as target of further stratified random sampling.

Step 2: Altogether 100 random samples were selected both for new tree
cover and loss of tree cover from the pre-selected set;

<img
src="products_HRL_Vegetation_Layers_Comparative_Analysis_v0-media/img-dd71d46dd0e69a23523965c21e87cef3.png"
data-fig-alt="This map displays the spatial distribution of sampling points across Europe for verifying tree cover changes. The geographic area covers EU Member States, Norway, Sweden, Finland, Iceland, UK, Ireland, Switzerland, parts of the Western Balkans, and Turkey. The legend, titled &#39;Sample class&#39;, indicates: * Green circular markers: &#39;New tree cover&#39; * Red circular markers: &#39;Loss of tree cover&#39; These sampling points represent tree cover difference polygons in the size range of 0.1–1 hectare, pre-selected for stratified random sampling to verify tree cover changes. Both &#39;New tree cover&#39; and &#39;Loss of tree cover&#39; points are widely distributed across the continent, with concentrations of both types appearing in Scandinavia, Central Europe (e.g., Germany, Poland), Eastern Europe (e.g., Romania, Bulgaria), and Southern Europe (e.g., Spain, Italy, Greece, Turkey). No scale bar, compass, or reference year is visible on the map."
alt="Figure 24 The location of random samples selected in a stratified to check the validity of tree cover differences in the size range 0.1-1ha, whether these represent a real change in tree cover between 2018-2021." />

This map displays the spatial distribution of sampling points across
Europe for verifying tree cover changes. The geographic area covers EU
Member States, Norway, Sweden, Finland, Iceland, UK, Ireland,
Switzerland, parts of the Western Balkans, and Turkey. The legend,
titled “Sample class”, indicates: \* Green circular markers: “New tree
cover” \* Red circular markers: “Loss of tree cover”

These sampling points represent tree cover difference polygons in the
size range of 0.1–1 hectare, pre-selected for stratified random sampling
to verify tree cover changes. Both “New tree cover” and “Loss of tree
cover” points are widely distributed across the continent, with
concentrations of both types appearing in Scandinavia, Central Europe
(e.g., Germany, Poland), Eastern Europe (e.g., Romania, Bulgaria), and
Southern Europe (e.g., Spain, Italy, Greece, Turkey). No scale bar,
compass, or reference year is visible on the map.

Step 3: The random samples were checked visually against historical
Google Earth imagery supported by EEA VHR satellite imagery, by
answering following questions:

- Is appropriate Google Earth imagery available for both reference
  dates?
- Is the classification correct in VLCC DLT2018 data (leaf type not
  considered)?
- Is the classification correct in VLCC DLT2021 data (leaf type not
  considered)?
- Does the difference polygon correspond to a real tree cover change, or
  a partial tree cover change, or no change at all?

#### Results

Altogether 200 selected samples were checked, but only 189 samples could
be evaluated, as in case of the rest of samples no appropriate EO
imagery was available for both of reference dates.

<div class="tbl-caption">

Table 33 Results of validity check

</div>

<table data-quarto-postprocess="true">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2"
style="vertical-align: middle"><strong>Stratum</strong></td>
<td rowspan="2" style="vertical-align: middle"><strong>No. of all
samples</strong></td>
<td rowspan="2" style="vertical-align: middle"><strong>No. of samples
evaluated</strong></td>
<td><strong>DLT2018</strong></td>
<td><strong>DLT2021</strong></td>
<td colspan="3"><strong>Validity of change (no. of
samples)</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Correct</strong></td>
<td style="text-align: center;"><strong>Correct</strong></td>
<td style="text-align: center;"><strong>Real<br />
change</strong></td>
<td style="text-align: center;"><strong>Partial<br />
change</strong></td>
<td style="text-align: center;"><strong>No<br />
change</strong></td>
</tr>
<tr>
<td>New tree cover</td>
<td style="text-align: center;">100</td>
<td style="text-align: center;">98</td>
<td style="text-align: center;">93%</td>
<td style="text-align: center;">91%</td>
<td style="text-align: center;">74%</td>
<td style="text-align: center;">7%</td>
<td style="text-align: center;">18%</td>
</tr>
<tr>
<td>Loss of tree cover</td>
<td style="text-align: center;">100</td>
<td style="text-align: center;">91</td>
<td style="text-align: center;">89%</td>
<td style="text-align: center;">87%</td>
<td style="text-align: center;">74%</td>
<td style="text-align: center;">8%</td>
<td style="text-align: center;">19%</td>
</tr>
<tr>
<td><strong>Total:</strong></td>
<td style="text-align: center;"><strong>200</strong></td>
<td style="text-align: center;"><strong>189</strong></td>
<td style="text-align: center;"><strong>91%</strong></td>
<td style="text-align: center;"><strong>89%</strong></td>
<td style="text-align: center;"><strong>74%</strong></td>
<td style="text-align: center;"><strong>7%</strong></td>
<td style="text-align: center;"><strong>19%</strong></td>
</tr>
</tbody>
</table>

Based on the results of the look & feel validity check shown in Table 33
we can conclude, that the validity of tree cover changes examined in DLT
difference patches in the range of 0.1-1ha is still very high. Although
we only had the opportunity to examine a limited number of samples in
this exercise, we can argue that by excluding changes below 1ha we lose
valuable change information. More detailed analysis is required to
establish appropriate value for an MMU.

### Effects of the aggregation of change data to 20m raster resolution

The aggregation of 10m HRL difference data to 20m raster resolution HRL
change data causes obviously a built-in inconsistency between HRL status
and change information. While keeping the 20m resolution for the
2018-2015 data merging seemed largely logical due to the different
resolution of the HRL status layers, keeping the 20m resolution for the
post-2018 change raster layers cannot be justified in this way.

The only logical argument would be to filter out noise due to the
uncertainty of the classifications, but this can be considered solved by
introducing an MMU to change data. All in all, it seems that for the
post-2018 change data, keeping the 20m resolution is not justified, it
causes more problems than we expect to solve.

### Chance of achieving full consistency in HRL Forest time-series

The time-series of high resolution VLCC Forest data between 2018-2021
represent a high level of technical consistency, still status and change
layers are not entirely consistent. However, the full consistency could
be easily reached by applying few changes in current mapping concept
with following recommendations:

- Avoid the aggregation of change data from 10m to 20m;
- Apply an MMU on changes to eliminate noise like tree cover differences
  to gain final change data. The currently applied MMU of 1ha proved to
  be too high, we recommend an MMU around 0.1ha;
- Repeat harmonization process (step 5 as discussed in the introduction
  of chapter 3.4) with final change data.

This way a full harmonization could be reached in VLCC Forest
time-series for 2018-2021 period. Remaining questions are however:

- VLCC Forest layers are currently technically harmonized with other
  VLCC layers (e.g HRL Grassland). Therefore, any harmonization is
  recommended to be applied not only for Forest but to other layers
  vegetation layers as well in VLCC portfolio.
- The continuation of the production of VLCC layers after 2021 is to be
  planned in a similar, harmonized way, in order to avoid new
  breakpoints in the time-series.

## Conclusions & recommendations

The consistency of the time-series of HRL Forest data was examined in
the whole 2012-2021 period. Additionally, tree cover information derived
from CLCplus Backbone was compared to HRL Forest 2018 data.

**Main conclusions are as follows:**

- The terminology of the products may be misleading. The two primary
  products HRL Forest surveys (TCD and DLT) are closely tree cover
  instead of forest related, while the FTY product is derived from
  primary TCD and DLT data, largely following the FAO forest definition;
- Many break points were identified in the history of HRL Forest
  products due to changes in specifications, available input data and in
  mapping concept;
- The new VLCC Forest time-series provides yearly status and
  additionally change data between the 3 yearly period between
  2018-2021. This time-series of VLCC Forest status layers may be
  characterized with a very high level of technical consistency both in
  terms of calibration of TCD values and the classification of leaf
  type;
- The VLCC DLT status and change layers are almost completely
  consistent, except for the effects of applying 1 ha MMU and the
  generalization by aggregation to 20 m;
- CLCplus Backbone provides comparable, but not completely equivalent
  estimation for the tree cover of European area.

**Key recommendations are:**

- Keep the high level of harmonization between status layers in the
  continuation of the time-series after 2021 reference year;
- Perform detailed verification of tree cover change data, including the
  verification of potential changes under 1ha MMU;
- Consider the possibility of reducing MMU by finding a balance between
  validity of change features and avoiding significant omission in
  change data;
- Improve the consistency between status and change layers by additional
  harmonization steps and by avoiding the aggregation of change data to
  20m.

# Summary & Conclusions

This report presents the outcomes of Task 2: Product Development Support
for the HRL Vegetated Land Cover Characteristics (VLCC) products. The
focus has been on exploration of potential of improvements of grassland
and forest data products through three key subtasks:

- **ST1: Assessment of Similarities and Differences** - A comprehensive
  comparison was conducted between the HRL VLCC Grassland product and
  other existing and prominent grassland mapping initiatives, including
  EU Grassland Watch (EUGW), Global Pasture Watch, SUPER-G, GRASS
  SIGNAL, and ESDAC Soil Biomass Productivity. While HRL VLCC offers
  pan-European, consistent annual mapping aligned with CAP monitoring,
  it lacks deeper ecological detail. Key findings include:
  - EUGW provides unique modular, habitat-focused monitoring within
    Natura 2000 sites, offering detailed indicators for type,
    management, and productivity using NDVI, SAR, and HR-VPP.
  - Global Pasture Watch contributes innovative methods like
    probabilistic grassland classification, grazing inference, and
    vegetation height mapping, though with limitations in spatial
    accuracy.
  - SUPER-G and GRASS SIGNAL inform the potential of integrating
    farm-level management data, real-time biomass forecasting, and
    Al-driven decision support.
  - 
- **ST2: Collection of User Requirements and Literature Review of
  Additional Forest Types** – Collection of User Requirements and
  Literature Review of Additional Forest Types This subtask investigated
  the suitability and gaps in current forest typologies for integration
  into HRL VLCC Forest products. The review focused on the European
  Forest Types (EFT) classification and compared it against both the
  Corine Land Cover (CLC) and EU Ecosystem Typology (ET) frameworks. Key
  findings include:
  - Many EFT categories do not align neatly with CLC or ET due to
    missing classes such as Mixed Forests, Plantations, and Transitional
    Woodland-Shrub.
  - Only a few categories in EFT (e.g. Mountainous Beech Forest) clearly
    represent mixed compositions, highlighting the need for more
    explicit mixed-species definitions.
  - Species-level reporting (from LULUCF submissions by 17 Member
    States) confirms the frequent use of tree species such as Quercus,
    Fagus, Populus, Salix, and Robinia, which should be incorporated
    into classification rules. A first nomenclature proposal, developed
    by GAF, outlines forest type definitions based on combinations of
    dominant species, biogeographic regions, and auxiliary data such as
    DEM and soil. While it aligns with the 14 EFT categories at Level 1,
    it currently:
  - Lacks explicit Mixed Forest and Plantation classes.
  - Needs refinement to reflect national reporting requirements and
    ecosystem accounting needs. The recommendations from this subtask
    include:
  - Expanding the classification to better reflect national
    stratification practices (e.g., Mixed Forest, Plantations, and
    alien/exotic species).
  - Developing aggregation rules to support both broad classes for
    reporting and detailed classes for ecological assessments.
  - Aligning forest type mapping with LULUCF reporting and ecosystem
    typology frameworks to support policy integration.
- **ST3: Assessment of Time Series Consistency of Forest Layers** – This
  subtask examined the consistency of HRL Forest products from 2012 to
  2021, focusing on whether differences between reference years reflect
  actual changes. Multiple breakpoints were identified across mapping
  cycles due to changes in specifications, AOI, input data, and
  classification logic. While HRL Forest 2012–2018 shows high
  variability and inconsistency between status and change layers, the
  VLCC Forest 2018-2021 series displays a much higher level of technical
  harmonization, particularly in terms of calibration, leaf type
  classification, and year-to-year stability. However, full consistency
  is not yet achieved, mainly due to the application of a 1 ha Minimum
  Mapping Unit (MMU) and the aggregation of change layers to 20m, which
  filter out small but valid changes. Recommendations include reducing
  the MMU (e.g., to 0.1 ha), avoiding unnecessary resampling, and
  repeating harmonization steps to align status and change layers. The
  VLCC series demonstrates that fully consistent time-series production
  is feasible and valuable for long-term forest monitoring.

#### Key Cross-Cutting Findings and Outlook

This task has demonstrated the critical importance of harmonizing
methodologies and enhancing thematic granularity in the CLMS HRL VLCC
products. The comparison with EUGW and other initiatives underscores
that while HRL VLCC offers strong pan-European consistency, it can
benefit from more refined indicators, especially in productivity
assessment and grazing intensity detection. Integration of advanced
techniques, such as machine learning, and improved in-situ data use, as
seen in initiatives like Global Pasture Watch and GRASS SIGNAL, can
potentially enhance product reliability and thematic resolution.

In forest classification, the review and stakeholder analysis reveal a
demand for a more nuanced nomenclature that reflects both ecological
diversity and national reporting requirements. This includes recognizing
transitional forest types, plantations, and mixed-species forests,
aligning better with LULUCF and EU ecosystem accounting needs.

The time-series analysis of forest layers highlights the need for a
stable framework that ensures logical consistency across years.
Achieving full temporal consistency remains a challenge, but it is
essential for tracking long-term trends and supporting robust indicator
development.

#### Recommendations and potential improvements

- **Enhancement of thematic detail in grassland mapping:**

  Integrate productivity layers and more dynamic indicators (e.g.,
  derived from NDVI trends or vegetation phenology and productivity).
  Consider incorporating short vegetation height data and biomass
  metrics to support structural characterization.

- **Improvement of detection of grazing practices:**

  Support the collection of harmonized in-situ data on grazing or
  external reference datasets (e.g., livestock density, grazing activity
  data). In-situ data on all grazing related variables is essential to
  improve training of classifiers and improve (hybrid) mapping
  possibilities and quality in coming years.

- **Adoption of a refined forest type nomenclature:**

  Expand current classifications to include Mixed Forests, Plantations,
  and Transitional Woodland-Shrub categories. Incorporate frequently
  reported species (e.g., Populus, Robinia, Salix) into classification
  frameworks for better alignment with national LULUCF reports.

- **Fostering interoperability between products:**

  Ensure alignment of HRL VLCC Grassland and Forest layers with EUGW,
  CLC+ Backbone, and other CLMS products through common/aligned
  reference masks and nomenclature structures.

- **Ensuring time-series consistency:**

  Improve calibration and harmonization of forest layers across years to
  support temporal coherence. Implement quality control and validation
  procedures specifically aimed at identifying and minimizing
  year-to-year classification noise.

- **Facilitating stakeholder engagement:**

  Establish mechanisms for continuous feedback from users, including
  national forest institutes and conservation bodies, to adapt product
  development to emerging needs.

- **Promote modular and scalable product design:**

  Continue developing thematic components (e.g., grassland type,
  management, productivity) in a modular format, as seen in EUGW, to
  support flexible use and integration into diverse applications.

By addressing these recommendations, HRL VLCC can evolve into a more
robust, policy-relevant, and ecologically meaningful dataset suite
supporting the EU’s environmental and agricultural monitoring needs.

# References

Bengtsson, J., J. M. Bullock, B. Egoh, C. Everson, T. Everson, T.
O’Connor, P. J. O’Farrell, H. G. Smith, and R. Lindborg (2019):
Grasslands—more important for ecosystem services than you might think.
Ecosphere 10(2):e02582. <https://doi.org/10.1002/ecs2.2582>

Malek, Ž., Schulze, K., Bartl, H. et al. (2024): Mapping livestock
grazing in semi-natural areas in the European Union and United Kingdom.
Landscape Ecology, 39(2). <https://doi.org/10.1007/s10980-024-01810-6>

Peeters, A. (2009): Importance, evolution, environmental impact and
future challenges of grasslands and grassland-based systems in Europe.
55(3): 113-125. <https://doi.org/10.1111/j.1744-697X.2009.00154.x>

Pividori, M., Giannetti, F., Barbati, A., Chirici, G. (2016): European
Forest Types: tree species matrix. In: San-Miguel-Ayanz, J., de Rigo,
D., Caudullo, G., Houston Durrant, T., Mauri, A. (Eds.), European Atlas
of Forest Tree Species. Publ. Off. EU, Luxembourg, pp. e01f162+

[^1]: https://github.com/wri/global-pasture-watch/blob/main/ggc-30m/README.md

[^2]: https://landcarbonlab.org/about-global-pasture-watch/

[^3]: https://global-pasture-watch.projects.earthengine.app/view/ggc-30m

[^4]: https://www.super-g.eu/about-super-g/

[^5]: https://cordis.europa.eu/project/id/774124

[^6]: https://business.esa.int/projects/grasssignal

[^7]: https://esdac.jrc.ec.europa.eu/content/soil-biomass-productivity-maps-grasslands-and-pasture-coplands-and-forest-areas-european

[^8]: https://www.lamasus.eu/ -last accessed 08.05.2025 09:45

[^9]: Product specifications – DLT, FT and TCD (2012 and 2015) and DLT,
    FT and TCD Changes

[^10]: Product user manual – DLT, FT and TCD 2018 and DLT, FT and TCD
    Changes

[^11]: High Resolution Layer Vegetated Land Cover Characteristics
    2017-2021 Production - Key technical specifications

[^12]: HRL FOREST 2015 FINAL VALIDATION REPORT

[^13]: Task 9 Assessment of MS verification results (HRLs 2018) - HRL
    DLTC 2015-2018. ETC/ULS Copernicus Report 2021 under SC 58651.
    \*\*\*
