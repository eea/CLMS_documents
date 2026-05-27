# High Resolution Layer Croplands 2017-present - Product User Manual

Copernicus Land Monitoring Service

This Product User Manual (PUM) serves as a comprehensive guide for users of the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands products, covering the period from 2017 to the present. It details the characteristics, production methodologies, and quality assessment of the annual HRL Croplands provision. The manual provides essential information on product usage, including nomenclature, spatial resolution, file formats, and terms of use, enabling effective application of these geospatial datasets. The technical focus includes the crop type classification, cropping patterns and accuracy assessment.

Author

Copernicus Land Monitoring Service

Published

December 3, 2025

Keywords

High Resolution Layer Croplands, Copernicus Land Monitoring Service, Crop Types layer, Cropping Patterns layers, Sentinel-2 imagery, agricultural practices mapping, Base Vegetation Layer, fAPAR timeseries, Accuracy assessment, Cloud-Optimized GeoTIFF

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

# 1 Executive summary

Copernicus is the European Union’s Earth Observation Programme. It offers information services based on satellite Earth observation and in situ (non-space) data. These information services are freely and openly accessible to its users through six thematic Copernicus services (Atmosphere Monitoring, Marine Environment Monitoring, Land Monitoring, Climate Change, Emergency Management and Security).

The Copernicus Land Monitoring Service (CLMS) provides geographical information on land cover and its changes, land use, vegetation state, water cycle and earth surface energy variables to a broad range of users in Europe and across the world in the field of environmental terrestrial applications.

CLMS is jointly implemented by the European Environment Agency (EEA) and the European Commission’s DG Joint Research Centre (JRC).

The High Resolution Layer (HRL) Vegetated land cover characteristics are a set of harmonised yearly maps dedicated to the thematic themes Tree Cover & Forests, Grasslands and Croplands. These include a rich suite of raster products mapping the yearly status of those land cover types at a spatial resolution of 10 metres and change layers at 3-yearly interval and 20-metre resolution. HRL vegetated land cover characteristics extends the time-series of the existing HRL’s Tree Cover & Forests and Grasslands and complements the CLMS portfolio with new layer dedicated to the mapping of crop types and agricultural practices such as mowing, harvest and cover crops.

# 2 Background of the document

## 2.1 Scope

This Product User Manual is the primary document that users are recommended to read before using the product. It provides a description of the product characteristics, production methodologies and workflows, and information about the product quality of the annual provision of HRL Croplands. Furthermore, it gives information on the terms of use and product technical support. More detailed information on the methodologies and processing workflows that were used to produce the products can be found in the Algorithm Theoretical Baseline Document (ATBD) \[7\].

## 2.2 Content and structure

In more detail, the document is structured as follows:

- Chapter 3 provides an overview of the lineage of the products in relation to previous productions;

- Chapter 4 contains a review of user requirements;

- Chapter 5 provides on overview of what is included in the High Resolution Layers vegetated land cover characteristics and how the comprised products relate to each other;

- Chapter 6 presents potential application areas and example use cases;

- Chapter 7 provides a description of the products including the nomenclature and class definitions, file naming, spatial resolution format(s), etc.;

- Chapter 8 summarizes the quality assessment, validation procedure and the results;

- Chapter 9 provides information about product access and use conditions as well as the technical product support.

# 3 Lineage of HRL Tree Cover and Forests, Grasslands, and Croplands

High Resolution Layers (HRL) on Tree Cover & Forests had already been established in the Copernicus Land Monitoring Service (CLMS) portfolio since the reference years 2012 producing initially a Dominant Leaf Type (DLT), a Tree Cover Density (TCD), and a Forest Type (FTY) map at a spatial resolution of 20 metres (Figure 3-1). Change layers and reference datasets were included with the reference year 2015. At the same time the accuracy targets were raised towards at least 90% user’s and producer’s accuracy for the DLT and TCD status layers. A further important step followed with the first production for the reference years 2018 (further referred to as Historic HRL Forest 2018) where the spatial resolution of the status layers was raised to 10 metres, the implementation of the change layers was partially reconsidered and target accuracies of 90% user’s and producer’s accuracy for the change layers were defined. In addition, new aggregated layers depicting the density of coniferous and broadleaved tree cover were introduced. With the HRL Tree Cover & Forests starting from the reference year 2018 the product specifications have been kept largely in line with the definitions used for the Historic HRL Forest 2018 \[8\] whereas major changes concerned in particular the move to a yearly update cycle for the status layers and changes to some confidence layers (not shown in Figure 3-1). The new HRL Tree Cover & Forests therefore replace and extend the Historic HRL Forest 2018. This does not include an update of the change layer 2015 – 2018; the new status layers for 2018 are therefore not consistent with the original change layers 2015 – 2018.

HRL’s on Grasslands had already been established in the Copernicus Land Monitoring Service (CLMS) portfolio since the reference years 2015 initially producing a status layer on the absence / presence of grassland (Figure 3-1) with a target Overall Accuracy of 85%. With the reference year 2018, the spatial resolution of the status layers was increased to 10 metres and a change layer with a target Overall Accuracy of 80% was introduced. With the HRL Grasslands starting from the reference year 2017, the product specifications have been largely maintained to ensure consistency with the definitions used for the Historic HRL Grassland 2018 \[9\]. In particular, the HRL Grassland (GRA) layer has been transitioned to an annual update cycle for the status layers, complemented by an additional yearly Herbaceous Cover layer that also includes temporary grassland in the reference year. A further methodological enhancement concerns the removal of the Minimum Mapping Unit (MMU) from both the PLOUGH and GRA layer starting from 2022. This adjustment was introduced to improve the current consistency between the GRA, HER, and PLOUGH layers and to eliminate artificial gains and losses resulting from MMU-induced filtering. While this change enhances the internal coherence and spatial detail of the current HRL Grassland layers, it may lead to minor differences when compared to historic layers (years before 2022) where MMU thresholds were still applied. Consequently, users should be aware that actual small-area grassland changes may be partly mixed with technical changes resulting from the removal of the MMU. New layers on the count and timing of Grassland Mowing (Minimum Mapping Unit of 0.25 ha) and changes to some confidence layers (not shown in detail in Figure 3-1) are introduced. The new HRL Grasslands therefore replaces and extends the Historic HRL Grassland 2018. This does not include an update of the change layer 2015 – 2018; the new status layers for 2018 are therefore not consistent with the original change layers 2015 – 2018.

The HRL Croplands is a new set of layers dedicated to agriculture and comprises several yearly layers mapping crop types (10-metre spatial resolution) and agricultural practices such as harvest, fallow land and secondary crops (10-metre spatial resolution, Minimum Mapping Unit of 0.25 ha).

![This diagram illustrates the historical production and transition to yearly updates for Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) products, specifically HRL Forest, HRL Grassland, and HRL Croplands. The HRL Forest section details product evolution across three production years: \* \*\*Production 2012 (Reference year: 2012 +/- 1 year, 90% overall accuracy for status layers):\*\* Includes Status layers (Tree Cover Density (TCD) 20m, Dominant Leaf Type (DLT) 20m, Forest Type (FTY) 20m) and Aggregated layers (TCD 100m, FTY 100m). \* \*\*Production 2015 (Reference year: 2015 +/- 1 year, Minimum 90% user's/producer's accuracy for TCD and DLT):\*\* Includes Status layers (TCD 20m, DLT 20m, FTY 20m, TCD RDB), Aggregated layers (TCD 100m, FTY 100m), and Change layers (Tree Cover Density Change (TCDC) 20m\* and Dominant Leaf Type Change (DLTC) 20m). Note: TCDC 20m\* is discontinued. \* \*\*Production 2018 (Reference year: 2018 +/- 1 year, Minimum 90% user's/producer's accuracy for TCD, DLT and TCPC):\*\* Includes Status layers (TCD 10m, DLT 10m, FTY 10m, TCD RDB, Coniferous Cover Density (CCD) 100m), Aggregated layers (TCD 100m, FTY 100m, Broadleaved Cover Density (BCD) 100m), and Change layers (Tree Cover Change Mask (TCCM) 20m\*\*, DLTC 20m, TCCM RDB). Note: TCCM 20m\*\* is continued as Tree Cover Presence Change (TCPC). \* \*\*Future Updates:\*\* From 2018 onward, HRL Forest products were replaced by yearly updates of HRL Tree Cover & Forests. The HRL Grassland section details product evolution across two production years: \* \*\*Production 2015 (Reference year: 2015 +/- 1 year, Minimum 85% Overall Accuracy (OA) of GRA status layer per biogeographical regions):\*\* Includes Status layers (Grassland (GRA) 20m) and Aggregated layers (GRA 100m). \* \*\*Production 2018 (Reference year: 2018 +/- 1 year, Minimum 85% OA for GRA status layer & minimum 80% OA for change layer per biogeographical regions):\*\* Includes Status layers (GRA 10m), Aggregated layers (GRA 100m), and Change layers (Grassland Change (GRAC) 20m). \* \*\*Future Updates:\*\* From 2017 onward, HRL Grassland products were replaced by yearly updates of HRL Grasslands. Separately, the diagram indicates that from 2017 onward, HRL Croplands products are also replaced by yearly updates.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image1.png)

Figure 3-1 Evolution of HRL Forest and Grassland towards the three product groups HRL Tree Cover & Forests, HRL Grasslands, HRL Croplands.

# 4 Review of User Requirements

In the frame of the Horizon 2020 (H2020) project ECoLaSS a survey \[5\] of key stakeholders has been performed in order to evaluate the user requirements towards the evolution of existing and future Copernicus products. This survey made also use of the results from the Nextspace User Study \[6\] and revealed that HRL users like European institutions, service industry, research and academia, national agencies, regional administrations, NGOs or private users would in general appreciate:

- High thematic quality/meaningful and application-oriented product definitions;

- Sufficient spatial and timely resolution concerning both, status layer and change layer;

- Short update cycles;

- Change monitoring;

- Free and open access;

- High technical quality;

- Standardized and comparable nomenclature;

- Transparent and scientific workflows and state-of-the-art methodology;

- Detailed documentation of these workflow and the respective methodology;

- Consistency of the Pan-European products enabling synergistic use of all products;

- Streamlining the pan-European product with global ones;

- Availability of historic data and compatibility of time series;

- Open access to the original Copernicus Sentinel data;

- Sophisticated product presentation and visualisation possibilities in an online viewer on the Copernicus platform;

- IPCC -compliant land-use categories.

While many of these requirements had already been satisfied with previous HRL reference years some could only be implemented within the current update:

- A long-standing thematic gap in the European CLMS portfolio concerning the monitoring of agriculture has been addressed though new products on crop types and agricultural activities. This also improves the separation between grassland and cropland and the IPCC conformity;

- Yearly update cycle for status layer;

- Grassland use intensity (or the dynamics of intensification/ extensification) is partially addressed through a new product on Grassland mowing.

Further requirements that remain to be considered for future updates are for example:

- More fine-grained differentiation among species-rich (extensively used) and separation from species-poor (intensively used) and managed grassland;

- Tree-species compositions and shifts between extensive and intensive management;

- Increased timeliness of availability of the products: The mid-term goal is a product provision at latest 12 months after the end of the reference year.

# 5 Product structure - What are the High Resolution Layers?

The High Resolution Layers (HRL) vegetated land cover characteristics portfolio consists of Tree Cover & Forests, Grasslands and Croplands products (Figure 5-1), which together cover most of what is defined as the Biotic component of the EAGLE Land Cover Components[^1]. More specifically, the mapping is focused on surfaces with a vegetation cover above 30%; an exception to this is tree cover where the objective is to map tree cover with a continuous range of 1-100% Tree Cover Density (TDC), i.e. also below 30%, as far as detectable from 10-metre resolution satellite imagery. This definition is also in line with the Sparsely Vegetated class in the Corine Land Cover (CLC)+ Backbone Raster[^2] and considers that detection / classification of vegetation below this threshold is typically more error-prone. The definition also aims at largely avoiding overlaps with the non-vegetated land cover characteristics such as HRL Imperviousness, which is focused on areas with less than 10% vegetation cover during any time of the year, for a reference period of 3 year.

Some overlaps between the three product groups are allowed by definition, for example areas with tree crops (i.e. olive, fruit and nut trees) which are included in both the Tree Cover & Forests and the Croplands products. Furthermore, specific vegetations types are not included in the HRLVLCC portfolio; this concerns areas dominated by natural shrubs (i.e. shrubs that are not under agricultural use) and associations of lichens and mosses.

![This hierarchical overview diagram presents the Copernicus Land Monitoring Service (CLMS) High Resolution Layers (HRL) vegetated land cover characteristics product portfolio. The top-level category, labelled 'High Resoluton Layers vegetated land cover characteristics' (note: 'Resolution' is misspelled as 'Resoluton' in the image), branches into three distinct product groups: 1. \*\*Tree Cover & Forest Products:\*\* These products have been available yearly since 2018. 2. \*\*Grasslands Products:\*\* These products have been available yearly since 2017. 3. \*\*Cropland Products:\*\* These products have been available yearly since 2017. The diagram indicates the start year for the yearly availability of each product category within the HRL vegetated land cover characteristics.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/img-e8467516151840ea4a22d7d91f3cf2c6ceebe367.png)

Figure 5-1: Products within the HRL vegetated land cover characteristics.

Given several interdependencies and potential overlaps among the Grasslands, Croplands and Tree Cover & Forests products, the overall workflow starts with the classification of Base Vegetation Layer (BVL). A high-level description is provided for the overall workflow in Figure 5-2. The yearly BVL classification initially targets the separation of five basic land cover classes being:

1.  herbaceous vegetation;

2.  cropland;

3.  tree cover;

- tree crops (i.e. nomenclature overlap between broadleaved tree cover and permanent crops in the Croplands product);

4.  background class (including bare and sparsely vegetated areas and non-agricultural shrubs);

In a subsequent post-processing step two further classes are derived to delineate the:

5.  potential overlap herbaceous – cropland (i.e. pixels which are classified as cropland and herbaceous at least once in the time-series);

6.  The second derived class is derived from the intersection of all areas classified as tree cover and a preliminary version of the Tree Cover Density to delineate areas with low Tree Cover Density and hence allowed overlaps of herbaceous and tree cover.

The derived yearly BVL is considered for the downstream productions of Grasslands, Croplands and Tree Cover & Forests products as follows:

- For the production of the Grasslands layers: all areas classified as herbaceous, overlap herbaceous – tree cover, or overlap herbaceous – Cropland are considered as the potential maximum extent for the Herbaceous Cover (HER) layer. In addition, the BVL classification probabilities for the herbaceous class are used as the main input for the derivation of the HER layer.

- For the Croplands layers: the areas delineated as cropland, overlap herbaceous –cropland, or Tree Crops are considered as the maximum extent for the CTY classification and further refinement.

- For the Tree Cover & Forests layers: the areas classified as tree cover, overlap herbaceous – tree cover, tree crops and the respective probabilities are used directly to derive the respective change layers and yearly DLT and TCD status layers.

Within the areas identified as overlap herbaceous – cropland, a further harmonization step is carried out downstream. To this end the CTY classification initially includes a class for fodder crops which are transferred to the HER layer if occurring in the designated overlap class.

![This is a high-level overview diagram illustrating the relationship between the Base Vegetation Layer Service and the subsequent production of Grasslands, Croplands, and Tree Cover & Forests products within the Copernicus Land Monitoring Service (CLMS). The process begins with the 'Base Vegetation Layer Service' which classifies areas into three primary categories: 'Herbaceous', 'Cropland', and 'Tree Cover'. This service also identifies specific overlap areas: \* 'Overlap Herbaceous – Tree Cover (TCD 1-10%)' \* 'Overlap Herbaceous-Cropland (e.g. Fodder crops)' \* 'Overlap Tree Cover-Cropland (Tree crops)' The 'Herbaceous' classification, including its maximum extent and probabilities, is fed into 'Grassland Product Services'. The 'Cropland' classification, including its maximum extent, is fed into 'Cropland Product Services'. The 'Tree Cover' classification, including its maximum extent and probabilities, is fed into 'Forest Product Services'. The 'Grassland Product Services' generate several products: \* 'Herbaceous Cover (10m)' \* 'Grassland (10m, 100m)' \* 'Grassland Change (20m, Minimum Mapping Unit 1ha)' \* 'Grassland Mowing Events (10m, Minimum Mapping Unit 0.25ha)' The 'Cropland Product Services' generate products such as: \* 'Crop Types (10m, Minimum Mapping Unit 0.25 ha)' \* 'Cropping patterns (10m, Minimum Mapping Unit 0.25 ha)' \* 'Main Crops, Bare Soil, Secondary Crops' \* 'Fallow Land, Annual Crop Characteristics' Notably, 'Fodder crops' identified by the 'Cropland Product Services' are fed back as an input to the 'Grassland Product Services' for harmonization. The 'Forest Product Services' generate products including: \* 'Dominant Leaf Type (10m)' \* 'Tree Cover Density (10m, 100m)' \* 'Forest Type (10m, 100m)' \* 'Forest Change (20m, Minimum Mapping Unit 1ha)'](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/img-6bc33732696023251e282e419d868126e4611b92.png)

Figure 5-2: High-level overview of the relationship between the Base Vegetation Layer and the subsequent production of Grasslands, Croplands and Tree Cover & Forests products

# 6 Product application areas and examples of use cases

The HRL Tree Cover & Forests, Grasslands and Croplands set of products is designed for use by a broad user community as basis for environmental and regional analysis and for supporting political decision-making, such as the Common Agricultural Policy (CAP), LULUCF (Land Use, Land Use Change and Forestry) regulation, the Nature Restoration Regulation (NRR), or the proposed European Forest Monitoring Law (FML). With the new products the EEA will ensure continuity and further densification of the well-established HRL Tree Cover & Forests and Grasslands product time series. Those include a rich suite of raster products at a 3-yearly interval mapping the status of those land cover types with a spatial resolution of 10-metre and change layers at 20-metre spatial resolution.

As an example, the following sections provide short information on (potential) use cases at national level, for which the Copernicus HRL Croplands product represent a fundamental input.

## 6.1 Use case: C3/C4 crops specific parametrization for biomass monitoring.

The HRL Crop Types (CTY) layer offers comprehensive information on various crop types, allowing for further differentiation between C3 and C4 crops (if class not mixed-up). Maize, being the most common C4 crop cultivated in Europe could be easily derived from this dataset. By providing detailed information on crop types and their specific locations, the CTY layer enables the use of tailored parameters for biomass estimation at C3/C4 crop locations on an annual basis. This information is particularly relevant for on-going work within the Evoland[^3] project, where the enhancement of biomass mapping for both crop and grassland areas is envisaged. In this respect, the reliability of the biomass mapping could benefit from the availability of this detailed crop type information. Moreover, the distinction between C3 and C4 crops is useful for better estimating autotrophic respiration, which in turn allows for more accurate conversions of gross primary productivity to net primary productivity. Given that C3 and C4 crops have distinct photosynthetic pathways and respiration rates, this differentiation supports the use of more precise parameters in productivity models, contributing to enhanced biomass mapping across crop landscapes.

## 6.2 Use case: Land cover specific monitoring

Detailed and dynamic information on the state of the land as provided by the HRL Croplands layers allows to analyse regional trends in the area occupied by these land covers, which could be relevant information for authorities and policy makers. Furthermore, applications which require information on the land cover status can benefit from the HRL Croplands. For example, in case of biomass mapping often land cover specific parametrization is applied. Using HRL Croplands, allows to do this in a much more detailed and dynamic way. In case of the Evoland project, it is intended to use these layers to apply specific parametrization over crop and grassland locations.

# 7 Product description

The HRL Croplands layers are generally provided in 100km Lambert Azimuthal Equal Area (LAEA) projection tiles as shown in Figure 7-1. The five French Oversea Territories are provided in UTM with the layout of the respective territory. The layers are available as Cloud-Optimized GeoTIFFs (COG) per reference year and 100km LAEA tile aligned with the EEA reference grid. Each raster file is accompanied by a Persistent Auxiliary Metadata (PAM) XML and an INSPIRE XML.

![This map illustrates the 100km Lambert Azimuthal Equal Area (LAEA) projection tile layout for Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands products, distinguishing between EU27 and European Environment Agency (EEA) 38 coverage. The geographic area covers Europe and associated overseas territories. The legend defines two categories of grid cells: - Green square outline: 'Included in EU27 coverage.' These tiles cover the continental EU27 Member States, the United Kingdom, and several Atlantic islands (e.g., Azores, Madeira, Canary Islands, French overseas territories). - Light blue square outline: 'Included only in EEA38 coverage.' These tiles extend the coverage to include countries like Iceland, Norway, Switzerland, Turkey, and the Western Balkan states (Albania, Bosnia and Herzegovina, Kosovo under UN Security Council Resolution 1244/99, Montenegro, North Macedonia, Serbia), forming the wider EEA38 area. The map displays a regular grid of 100km x 100km tiles over the landmasses and surrounding waters. The scale bar at the bottom indicates distances from 0 km to 1600 km, with increments of 400 km.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/img-ca1eb55e3cba78bf3f78fb81c831ae27ef69af7e.png)

Figure 7-1: LAEA tile layout incl. distinction between tiles to cover EU27 and EEA38.

The HRL Croplands information aims at filling the data gap needed for detailed agricultural monitoring and enables repeatable and harmonised continental scale assessments within the CLMS portfolio. The HRL Croplands layers entail the mapping the extent of croplands and crop types, delineation of parcel-complexes, mapping agricultural practices on large scale and with wall-to-wall coverage and high spatial details.

![This diagram illustrates the hierarchical structure of the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands data, available yearly since 2017. The main Croplands data is categorised into two primary branches: 'Status' and 'Ancillary' layers. The 'Status' branch includes: 1. \*\*Crop Type (CTY)\*\*. 2. \*\*Cropping Patterns (CP) 10m\*\*, which further detail: \* \*\*Main Crop (CPMC) 10m\*\* with sub-components: Emergence (CPMCE), Harvest (CPMCH), and Duration (CPMCD). \* \*\*Bare Soil (CPBS) 10m\*\* with sub-components: Before (CPBSB) and After (CPBSA). \* \*\*Secondary Crops (CPSC) 10m\*\* with sub-components: Type (CPSCT), Emergence (CPSCE), and Duration (CPSCD). \* \*\*Fallow Land (CPFL) 10m\*\* with sub-components: Presence (CPFLP) and Duration (CPFLD). \* \*\*Cropping Seasons (CPCS) 10m\*\* with sub-components: Yearly (CPCSY) and Types (CPCST). The 'Ancillary' branch includes: 1. \*\*Crop Type Confidence Layer (CTYCL) 10m\*\*. 2. \*\*Cropping Patterns Confidence Layers (CP ... CL) 10m\*\*, which provide confidence metrics for specific cropping pattern attributes: \* Emergence (CPMCECL) \* Harvest (CPMCHCL) \* Duration (CPCDCL) \* Before (CPBSBCL) \* After (CPBSACL) \* Duration (CPSCDCL) \* Presence (CPFLPCL) \* Duration (CPFLDCL)](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/img-f66692b52cdab6bf7c00868d035160c85d2d44d8.png)

Figure 7-2 HRL Croplands product overview

The primary layer is the yearly Crop Types (CTY) layer at 10 metre, which maps the specific crop grown in the main growing season for all pixels identified as arable or permanent crops by the BVL. Maximum uniformity, comparability, and interpretability of the final product is guaranteed across different regions in Europe by focusing on the main growing season. Besides the CTY layer a supportive Crop Types Confidence Layer (CTYCL) layer is provided to match the CTY layer. CTYCL indicates the degree of confidence of the provided crop type label. The probability value from the winning class as determined by the model is taken as the confidence level.

Several further status HRL Cropping Patterns (CP) layers, covering 5 thematic domains, give information on the agricultural practices within the classified cropland area for the following domains:

- Main Crops;

- Bare Soil;

- Secondary Crops;

- Fallow Land;

- Cropping Seasons;

All the CP layers are only applied over annual arable land, excluding permanent crops. Permanent crops do not have specific seasonal cycles, which is the primary focus of the cropping pattern layers. The workflow used to define the different agricultural practices is applied at field level scale, to ensure homogeneity in the seasonal signal and reduce signal noise. Afterwards, all the different layers are rasterized and aligned on the same spatial grid as the CTY layer. Therefore, only for those locations where initially a field could be delineated and where it coincides with a classified annual cropland, the Cropping Pattern layers are generated (excluding crop rotation layer, see last paragraph of section). Since the MMU is applied to the originally delineated parcel geometry used for defining CP information, further alignment with annual cropland may result in smaller spatial patterns due to the clipping of the original field boundaries. However, the CP information itself remains based on an MMU of at least 0.25 ha, as it is still derived from the original parcel geometry.

The Main Crops (MC) layers focus on the characteristics of the main growing season which usually takes place during (part of) the summer season. These layers provide information on the emergence (CPMCE) and harvest (CPMCH) of the main growing season, as well as the duration of the season (CPMCD). Each of these layers include a Confidence Layer (CL) that indicates the level of uncertainty in days. Information on the characteristics of the growing season and its variations over time give valuable information on how growing seasons are impacted by (extreme) weather conditions and climate change at regional and national levels.

The Bare Soil (BS) group of layers include information on the duration of the bare soil period. Presence of a period of Bare Soil Before (CPBSB) the emergence of the main crop season and Bare Soil After (CPBSA) the harvest of the main crop season are evaluated. Both layers also feature a CL that indicates the level of uncertainty in the duration of the bare soil period in days. This uncertainty is based on the uncertainty of the emergence and/or harvest events that define the bare soil period. The bare soil period is only defined for the duration within the reference year. Therefore, emergence events occurring after the calendar year that marks the end of the bare soil period following the main season will not be considered in the uncertainty calculation. Similarly, for the bare soil period before the main season, if the preceding harvest event took place in the previous calendar year, it will not be included in the uncertainty calculation. Information of bare soil periods are relevant for policy makers to assess the susceptibility of soils to leaching and erosion.

The Secondary Crops (SC) group of layers provides information on agricultural parcels where an off-season secondary growing season occurs. Typically, this secondary season involves planting a cover crop in the field. Secondary season presence in only evaluated if a main season is detected. The secondary season is categorized into four Secondary Crop Types (CPSCT) based on the emergence date and length of the season: short/long summer and short/long winter secondary seasons. In addition, to this classification, information on the Secondary Crop Emergence (CPSCE) and Secondary Crop Duration (CPSCD) of the season is included. Similarly, as for the Main Crops (MC) layer, uncertainty information is provided for both the duration and emergence of the secondary crops. The SC layers offer valuable information for assessing policy implementation to prevent soil degradation and monitoring cropping changes during off-season over time at regional and national level.

The Fallow Land (FL) layers give information on Fallow Land Presence (CPFLP) and Fallow Land Duration (CPFLD). Fallow land presence is defined as agricultural land where, temporarily, no agricultural activity takes place. Fallow land duration indicates the number of days a parcel is left fallow for the five-year period i.e., 2017-2021. Both the FLP layer and the FLD layer have an accompanying Confidence Layer (CL).

Finally, the Cropping Seasons layers provide information on the number of detected growing seasons in the Cropping Seasons Yearly (CPCSY) layer and information on main crop rotation in the Cropping Seasons Types over 3 years (CPCST) layer. The CPCSY layer is based on the CTY and the CPSCT layers to count the number of growing seasons in a specific year. CPCST is based on the crop diversity count and contains the number of unique crop types grown in the main agricultural season over a 3-year period. Since, CPCST is based on information of previous year’s crop types, it is only available for the 2017-2019, 2018-2020, and 2019 till 2021 time periods. Furthermore, it does not rely on the delineation of parcel complexes compared to the other CP layers as it is a purely CTY based layer. Information on crop rotation provides valuable insights to monitor the application of monoculture or rotation cycle in specific regions.

## 7.1 Thematic characteristics of the HRL Croplands layers

The HRL Croplands layers are only provided for those locations where the BVL designates arable or permanent cropland (i.e., BVL classes cropland, tree crops and overlap herbaceous and crops). For those locations the pixel-based crop type algorithm classifies according to the crop type grown in the main growing season. A main crop season is defined as the most crucial period for cultivating crops of economic value. Initially, the algorithm also classifies the grassland and fodders crops that are present in the applied BVL mask (overlap herbaceous and crops), but those locations are transferred to the Herbaceous Cover (HER) layer (see 5.2). In Table 7-1, the final mapped crop types and the aggregation levels of the hierarchical nomenclature are given. The crop type aggregation level is used within the Crop Types (CTY) layer. For those cases where the classification algorithm remains undecided due to low confidence values, a separate category is added, subdivided in unclassified arable and permanent crop. This output is further spatially cleaned and harmonised over the years to enhance temporal and spatial consistency of the product. As a result of these post-processing steps, it might happen that there is some minimal overlap between the HRL Croplands and Grassland layers that are both located within the arable or permanent crops classes defined by BVL \[7\]. This potential overlap can be present in the published layers and solely occurs at borders between cropland and temporary grassland.

![\| Code \| Land Cover \| Crop Group \| Crop type \| Colour \| \|---\|---\|---\|---\|---\| \| 1110 \| Arable Crops \| Cereals \| Wheat \| Orange \| \| 1120 \| Arable Crops \| Cereals \| Barley \| Light Orange \| \| 1130 \| Arable Crops \| Cereals \| Maize \| Yellow \| \| 1140 \| Arable Crops \| Cereals \| Rice \| Red-Orange \| \| 1150 \| Arable Crops \| Cereals \| Other cereals \| Light Brown/Pink \| \| 1210 \| Arable Crops \| Dry pulses & Vegetables \| Fresh Vegetables \| Light Blue \| \| 1220 \| Arable Crops \| Dry pulses & Vegetables \| Dry pulses \| Dark Blue \| \| 1310 \| Arable Crops \| Root/tuber crops \| Potatoes \| Brown \| \| 1320 \| Arable Crops \| Root/tuber crops \| Sugar Beet \| Dark Brown \| \| 1410 \| Arable Crops \| Non-permanent industrial crops \| Sunflower \| Pink \| \| 1420 \| Arable Crops \| Non-permanent industrial crops \| Soybeans \| Purple \| \| 1430 \| Arable Crops \| Non-permanent industrial crops \| Rapeseed \| Magenta \| \| 1440 \| Arable Crops \| Non-permanent industrial crops \| Flax, cotton and hemp \| Light Pink \| \| 2100 \| Permanent Crops \| Permanent Crops \| Grapes \| Light Green \| \| 2200 \| Permanent Crops \| Permanent Crops \| Olives \| Yellow-Green \| \| 2310 \| Permanent Crops \| Permanent Crops \| Fruits \| Dark Green \| \| 2320 \| Permanent Crops \| Permanent Crops \| Nuts \| Darkest Green \| \| 3100 \| Arable Crops \| Unclassified arable crop \| Unclassified arable crop \| Light Grey \| \| 3200 \| Permanent Crops \| Unclassified permanent crop \| Unclassified permanent crop \| Dark Grey \| This table presents the hierarchical nomenclature and classification codes for crop types within the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands product, including associated colours for mapping. It categorises crops first by 'Land Cover' (Arable Crops or Permanent Crops), then by 'Crop Group', and finally by specific 'Crop type'. Arable Crops include Cereals (Wheat, Barley, Maize, Rice, Other cereals), Dry pulses & Vegetables (Fresh Vegetables, Dry pulses), Root/tuber crops (Potatoes, Sugar Beet), and Non-permanent industrial crops (Sunflower, Soybeans, Rapeseed, Flax, cotton and hemp). Permanent Crops are grouped as Grapes, Olives, Fruits, and Nuts. Additionally, the table defines 'Unclassified arable crop' and 'Unclassified permanent crop' categories for instances where the classification algorithm cannot make a confident determination.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/Table7-1.png)

Table 7-1: HRL Crop Types nomenclature and aggregation levels

The emergence and harvest detection are the main input for the different HRL Cropping Patterns (CP) layers that provide information on the agricultural practices. The following definitions of emergence and harvest are used to detect these events from satellite imagery:

- Emergence is defined as the moment when the first leaves of the crop unfold

- Harvest is defined as the moment when all standing biomass is removed.

A main crop season is defined as the most crucial period for cultivating crops of economic value. Expert rules, developed by analysing seasonal boundaries in Europe and using USDA crop calendar data, are used to classify seasons as main or secondary \[7\]. Region specific seasonal boundaries are selected to reflect the seasonal shifts across Europe. Additionally, rules for prioritization are established to resolve conflicts in cases where multiple main seasons are possible. The complete procedure for selecting the growing season is outlined in the ATBD; while the detection is only performed for annual crops it is fully independent from the crop type label of the annual crop defined in the CTY layer \[7\]. However, due to the complexity of agricultural patterns, there may be challenges in accurately distinguishing the main season from the secondary season. This is particularly true in cases where a very late onset of the main growing season follows on a season with similar behaviour as winter cereals. Since the cultivation of winter cereals is also considered, the main season onset may occur before the reference year. Additionally, in rare instances, the harvest of the main season crop may occur shortly after the end of the year. In some situations, it is impossible to generate a Cropping Pattern product for the main crop layer based on the defined seasonal boundaries (i.e., season length should fall between 40 and 366 days, period of main growing season) and the detection of emergence and harvest events. In such cases, the corresponding pixels are flagged with dedicated codes (see Table 7-7).

The Secondary Crop (SC) layers follow a similar methodology to the main season classification, but with distinct seasonal boundaries based on the emergence and harvest detected for the secondary crop. The secondary season can occur both preceding and following the main growing season, although preference is given to labelling a secondary season that follows the main season when multiple instances arise. If there are more than one seasonal signal after the main season within the same calendar year, the SC product may not align with the actual cover crop sown, but rather with a short-term crop planted in a double cropping system. Each secondary crop season is subdivided into four categories, short/long summer, and short/long winter secondary seasons. A seasonal length shorter than 100 days is considered as a short growing variant, otherwise it is a long variant. If the secondary crop emergence is before September and takes place after the end of the main season, it is a summer variant. In all other cases, it is a winter variant.

The Bare Soil layers indicate the period before and after the main growing season when no crop cultivation activities occur. This period is determined by the detection of emergence and harvest events within that year in a particular field. Since a specific bare soil detection algorithm is not employed, there may be instances where the field is not completely bare during this period, possibly due to weed growth or the presence of residual crop remnants. Additionally, activities such as fertilization or ploughing of the field can fall within the bare soil period.

The Fallow Land layers consider only delineated parcels that are classified as annual cropland by the CTY layer, other parcels are omitted for the fallow land evaluation. For the determination of fallow land presence thematic rules, based on the expected behaviour of fallow land, are used. The rules consider the average Crop Types Confidence Layer (CTYCL), the number and sequence of detected harvests and emergences in combination with the maximum fAPAR value. Harvest dates are used to determine the fallow land duration. Therefore, the accuracy of the fallow land layers depends on the accuracy of the CTYCL, the detected harvests and emergence, and the fAPAR timeseries.

The Cropping Seasons layers provide insights into the annual crop rotation strategy and the number of growing seasons at specific locations. Note however that a maximum limit of two growing seasons is considered. If more than two seasons are identified, they will not be considered. Permanent crops are ignored in counting the crop diversity.

An overview of how cropping pattern layers (excluding Fallow Land and Cropping Seasonslayers) can be generated at the field level based on the identified emergence and harvest events within a six-month period before and after the calendar year is given in Figure 7-3. The emergence and harvest events are used to classify the season as either main or secondary based on predefined seasonal boundaries. In the example shown in Figure 7-3, the main season corresponds to a winter cereal, resulting in no bare soil period before the main season for the reference year. Instead, a bare soil period is indicated between the main and secondary seasons, defined by the harvest of the main season and the emergence of the secondary season. The secondary season is classified as a long winter variant. The uncertainty surrounding fAPAR values around the emergence and harvest events is utilized to generate the respective Confidence Layers.

![Line chart illustrating the Fraction of Absorbed Photosynthetically Active Radiation (fAPAR) time series for a barley field from July 2018 to July 2020, indicating crop seasons and bare soil periods. The Y-axis represents fAPAR values ranging from 0.0 to 1.0. The X-axis represents time, with tick marks every three months from 2018-07 to 2020-07. The chart includes three green data series representing fAPAR quantiles: 'CropSAR_q50' (solid line), 'CropSAR_q10' (dashed line), and 'CropSAR_q90' (dash-dot line), which collectively show the fAPAR value and its uncertainty range. Two types of vertical lines indicate key events: 'modelled_emergen' (solid black lines) and 'modelled_harvest' (solid red lines). The fAPAR curve shows three distinct cycles, each representing a growing season characterized by high fAPAR values (typically 0.6–0.9) followed by sharp drops to low values (around 0.1–0.2) during harvest and bare soil periods. Specific events and periods annotated below the chart are: - A 'modelled_harvest' (red line) occurs around mid-October 2018, followed by a 'modelled_emergen' (black line) in late October 2018. - A green double-headed arrow labeled 'Main season' spans from approximately late October 2018 to early July 2019, indicating a period of active growth. The 'modelled_harvest' for this main season occurs in early July 2019. - A red double-headed arrow labeled 'BS after' (Bare Soil after) spans from early July 2019 to late October 2019, representing the bare soil period following the main season's harvest. A 'modelled_emergen' occurs in late October 2019, marking the start of the next season. - A blue double-headed arrow labeled 'Secondary crop season' spans from late October 2019 to late April 2020, representing a second period of active growth. The 'modelled_harvest' for this secondary season occurs in late April 2020. - Another 'modelled_emergen' is indicated in early May 2020, followed by another fAPAR growth cycle.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/img-80e6a4a68bfe83b945921f20705162656feeb945.png)

Figure 7-3: Example how the different cropping patterns layers for a barley field located in Belgium are generated for the reference year 2019. The season delineation is based on the predicted emergence (black line) and harvest dates (red line). The green timeseries curve is the daily fAPAR value (with uncertainty). BS after stands for the length of the bare soil period after the main season.

## 7.2 Download content, file naming convention and file format(s)

Table 7-2: Download content, file naming convention and file format(s) for the HRL Croplands layers

[TABLE]

**Delivery format (for Crop types & Crop types confidence):**  
Tiles of Cloud-Optimized GeoTIFF aligned with the 100km LAEA grid with embedded colormaps, as well as separate colour legends in the formats \*.qml,\* .sld and \*.lyr

**Delivery format (for all rows except Crop types & Crop types confidence):** Tiles of Cloud-Optimized GeoTIFF aligned with the 100km LAEA grid. Separate colour legends in the formats \*.qml,\* .sld and \*.lyr

**Metadata (applies to all rows):**  
XML metadata files according to INSPIRE metadata standards and GDAL-style Permanent Auxiliary Metadata (PAM)\*.aux.xml including statistics and Raster Attribute Table.

## 7.3 Projection and spatial coverage

Table 7-3: Projection and spatial coverage for the HRL Croplands layers

| Name of layer                             | Acronym |
|-------------------------------------------|---------|
| Crop types                                | CTY     |
| Crop types confidence                     | CTYCL   |
| Main Crop Harvest                         | CPMCH   |
| Main Crop Harvest Confidence Layer        | CPMCHCL |
| Main Crop Emergence                       | CPMCE   |
| Main Crop Emergence Confidence Layer      | CPMCECL |
| Main Crop Duration                        | CPMCD   |
| Main Crop Duration Confidence Layer       | CPMCDCL |
| Bare Soil Before                          | CPBSB   |
| Bare Soil Before Confidence Layer         | CPBSBCL |
| Bare Soil After                           | CPBSA   |
| Bare Soil After Confidence Layer          | CPBSACL |
| Secondary Crops Type                      | CPSCT   |
| Secondary Crops Emergence                 | CPSCE   |
| Secondary Crops Duration                  | CPSCD   |
| Secondary Crops Duration Confidence Layer | CPSCDCL |
| Fallow Land Presence                      | CPFLP   |
| Fallow Land Presence Confidence Layer     | CPFLPCL |
| Fallow Land Duration                      | CPFLD   |
| Fallow Land Duration Confidence Layer     | CPFLDCL |
| Cropping Seasons Yearly                   | CPCSY   |
| Cropping Seasons Types over 3 years       | CPCST   |

**Spatial coverage (applies to all rows):** 5.751.002 km² (covering the full EEA-38)

**Coordinate reference system (WKT) (applies to all rows):** PROJCS\[“ETRS89-extended / LAEA Europe”, GEOGCS\[“ETRS89”, DATUM\[“European_Terrestrial_Reference_System_1989”, SPHEROID\[“GRS 1980”,6378137,298.257222101, AUTHORITY\[“EPSG”,“7019”\]\], AUTHORITY\[“EPSG”,“6258”\]\], PRIMEM\[“Greenwich”,0, AUTHORITY\[“EPSG”,“8901”\]\], UNIT\[“degree”,0.0174532925199433, AUTHORITY\[“EPSG”,“9122”\]\], AUTHORITY\[“EPSG”,“4258”\]\], PROJECTION\[“Lambert_Azimuthal_Equal_Area”\], PARAMETRE\[“latitude_of_center”,52\], PARAMETRE\[“longitude_of_center”,10\], PARAMETRE\[“false_easting”,4321000\], PARAMETRE\[“false_northing”,3210000\], UNIT\[“metre”,1, AUTHORITY\[“EPSG”,“9001”\]\], AXIS\[“Northing”,NORTH\], AXIS\[“Easting”,EAST\], AUTHORITY\[“EPSG”,“3035”\]\] Except for French DOMs where the following CRS are used: YT: EPSG 32738 RE: EPSG 32740 MQ: EPSG 32620 GP: EPSG 32620 GF: EPSG 32620

## 7.4 Spatial resolution

The native spatial resolution of the HRL Cropland products CTY and the Cropping Patterns is 10 metres and linked to the highest resolution of Sentinel-2 (red, blue, green and near-infrared bands) as the primary input data source. The spatial resolution should, however, not be confused with the size and location-precision of the elements that can be represented in the maps. The latter is limited by certain factors that are intrinsic to the available input data:

- Ground Resolved Distance (GRD) is a metric that better reflects the spatial resolution of a satellite sensor than the spatial resolution of the image. For Sentinel-2 recent estimates suggest a GRD around 12.5 metres \[10\]

- To fully leverage Sentinel-2, the analyses of the time-series are essential. Since the completion of the reprocessing of Sentinel-2 Colllection-1 the multi-temporal coregistration is better than 4m in most cases[^4] whereas observations until August 2021 only had a co-registration accuracy of 12 metres before the reprocessing[^5].

&nbsp;

- Most other input data have a coarser spatial resolution (e.g. Sentinel-1 ~20 metre, Sentinel-2 short wave infrared at 20 metre).

- The detectability of land cover elements can be further limited by the intensity of their reflectance. This concerns for example vegetation on very bright soils or in urban areas where the reflectance of the brighter non-vegetated surfaces easily dominates the recorded reflectance within one pixel.

While it is difficult to quantify the cumulative effect and variability of these factors, limited detectability and spatial uncertainty of elements at a scale from 10-20 metres should probably be considered for the usage and validation of the maps.

Table 7-4: Spatial resolution for the HRL Croplands layers

| Name of layer                             | Acronym |
|-------------------------------------------|---------|
| Crop types                                | CTY     |
| Crop types confidence                     | CTYCL   |
| Main Crop Harvest                         | CPMCH   |
| Main Crop Harvest Confidence Layer        | CPMCHCL |
| Main Crop Emergence                       | CPMCE   |
| Main Crop Emergence Confidence Layer      | CPMCECL |
| Main Crop Duration                        | CPMCD   |
| Main Crop Duration Confidence Layer       | CPMCDCL |
| Bare Soil Before                          | CPBSB   |
| Bare Soil Before Confidence Layer         | CPBSBCL |
| Bare Soil After                           | CPBSA   |
| Bare Soil After Confidence Layer          | CPBSACL |
| Secondary Crops Type                      | CPSCT   |
| Secondary Crops Emergence                 | CPSCE   |
| Secondary Crops Duration                  | CPSCD   |
| Secondary Crops Duration Confidence Layer | CPSCDCL |
| Fallow Land Presence                      | CPFLP   |
| Fallow Land Presence Confidence Layer     | CPFLPCL |
| Fallow Land Duration                      | CPFLD   |
| Fallow Land Duration Confidence Layer     | CPFLDCL |
| Cropping Seasons Yearly                   | CPCSY   |
| Cropping Seasons Types over 3 years       | CPCST   |

**Pixel size (applies to all rows):** → 10m

**MMU (applies to all rows):** → 0.25ha\*

- For CP layers, smaller patterns may appear due to alignment with annual cropland. However, the CP information is derived from the original parcel geometries (before alignment), which adhere to the MMU requirements.

## 7.5 Temporal information

Table 7-5: Temporal information for the HRL Croplands layers

[TABLE]

## 7.6 Product characteristics and class codes

Table 7-6: Overview of the used quality flags within the HRL Croplands layers

[TABLE]

Table 7-7: Summary of the applicable quality flags of the HRL Croplands layers

[TABLE]

# 8 Production quality assessment

The aim of this chapter is to inform about the procedures for internal validation and accuracy assessment for the status and change layer across the full EEA38 area. While the different layers have their own quality requirements, all have in common an assessment of the thematic quality which relies on comparing mapped information within the layers with reference data at selected locations.

This procedure contains 3 steps that will be described in the following sections:

- Sampling design

- Response design

- Statistical Analysis

The internal validation of the HRL Croplands layers follows scientifically accepted and operationally proven validation design, applied in previous productions of various HRL’s of reference years 2012, 2015 and 2018. According to the product specifications, results will be presented in the form of Overall Accuracies (OA), Producer’s and User’s Accuracies or F-Score measure.

## 8.1 Layers to be verified

While the full portfolio of the HRL Croplands product includes numerous layers and reference years, only a subset of them is concerned by the internal verification exercise. The focus of the assessment has been set on the primary layer being the Crop Types layer and the reference years 2018 and 2021, 2022. The rationale for this selection has been mainly the availability of essential reference datasets such as LUCAS 2018 \[1\] and LUCAS 2022 \[2\], the VHR IMAGE coverages of 2018 and 2021 imagery, and publicly available GSAA datasets. An overview of the verified layers and their target accuracies is given in Table 8-1.

Table 8-1: Layers to be verified and target accuracies

[TABLE]

## 8.2 Sampling Design

Two sampling approaches are considered to ensure an adequate accuracy assessment of the layers at different hierarchical nomenclature levels.

The first sampling approach is dedicated to assess the accuracies of the Crop Typeslayer at crop group level. At pan-European level, this corresponds to a non-stratified, systematic and random sampling approach based on the 2 km by 2 km LUCAS grid. For the assessment of status layers, 10 000 samples (Primary Sampling Units) were randomly selected over the extended LUCAS grid (Figure 8-1). An additional 4000 samples have been allocated for the assessment of the HRL change layers Tree Cover Presence Change 2018-2021 \[11\] and Grassland Change 2018-2021\[12\] and are used here as well to exploit synergies.

![This map displays the pan-European distribution of sampling points (red dots) used for the accuracy assessment of Copernicus Land Monitoring Service (CLMS) Crop Types layers. The grey-shaded landmasses represent European countries. Red dots indicate the Primary Sampling Units selected from an extended 2 km by 2 km Land Use/Land Cover Area Frame Survey (LUCAS) grid. Approximately 14,000 such samples are distributed across continental Europe, the Nordic countries (including Iceland, excluding the United Kingdom), the Iberian Peninsula, Italy, the Balkan states, Ireland, Turkey, and the Portuguese Atlantic islands (Azores, Madeira). The United Kingdom is shown in grey but does not contain any red sampling points. The sampling approach is described as non-stratified, systematic, and random.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/img-c861206239383485c44d6e1af9b25dabed4cf2e7.png)

Figure 8-1: Approach I sample distribution for verification at Crop Group Level

The second sampling approach is dedicated to the accuracy assessment of the Crop Types layer at aggregation level 1 which contains 11 classes (Table 8-2). To ensure a correct and precise identification of crop parcels during the verification exercise, the use of LUCAS and GSAA data as reference data is mandatory. However, some limitations of those datasets exist:

- LUCAS survey information exists for the years 2018 and 2022 but not for the year 2021.

- GSAA data is not openly available for all countries and for all reference years.

To circumvent those limitations, the approach II proposes to:

- For the year 2018, take advantage of the LUCAS survey information by using all “LUCAS crops” (e.g. LUCAS point with crop type information) which were not used as calibration/training data for the year 2018 (3226 LUCAS points when excluding UK). The location of the samples is illustrated in Figure 8-2.

- Use of GSAA data when and where available: per country, a random sampling of crop parcels (among those not used for calibration/training purposes) is performed to populate the reference database. This sampling is done on the year 2021 when GSAA was available but can be done on years 2020 or 2019 depending on GSAA availability for said country. This is illustrated on Figure 8-4. The total amount of samples selected from GSAA data is similar to the sampling effort for the year 2018 when considering LUCAS crop sample (~3300 samples). For efficiency reasons it was not possible to collect and harmonize further GSAA datasets for following years.

- For the year 2022 the LUCAS survey information was used by selecting all LUCAS points for which the Copernicus protocol was applied and crop type information was available. Since LUCAS 2022 was not used at all for training and calibration during the production all samples could be used for the accuracy assessment. This amounts to a total of 32 732 LUCAS points that could be used to assess the accuracy at level 1 of the CTY nomenclature Figure 8-3.

![Choropleth map illustrating the geographic distribution of LUCAS (Land Use/Cover Area frame Survey) crop sampling points across Europe for the year 2018. The map displays the European continent, including EU Member States and surrounding countries, with land areas shown in grey and national borders outlined in white. Individual sampling locations are represented by small yellow-orange circular markers. The distribution shows a high density of LUCAS crop points across Central and Western European Member States, including France, Germany, Poland, Italy, and Spain. Significant concentrations are also visible in the Nordic countries (Sweden, Finland), Eastern Europe (Romania, Hungary), and the British Isles. The points represent LUCAS survey information with crop type data.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/img-9e704a7c3da9f900c7030e35f7e20b360d0ffd69.png)

Figure 8-2: Approach II sample distribution depending on LUCAS points containing crop type information for the year 2018

![Choropleth map illustrating the spatial distribution of Land Use/Cover Area frame Survey (LUCAS) points with crop type information for accuracy assessment in Europe, specifically for Approach II, in 2018. The map shows the landmass of Europe, including EU Member States (e.g., France, Germany, Italy, Spain, Poland, Sweden, Finland) and neighbouring countries, shaded in grey with white national borders. White areas represent oceans and seas. Small orange circular points are densely distributed across the continental landmass, representing LUCAS sample locations. These points are concentrated throughout Western, Central, and Southern Europe, including the British Isles (United Kingdom, Ireland). A sparser distribution is visible in Northern Europe (e.g., parts of Sweden, Finland) and southeastern Europe. Iceland, the far north of Norway, and parts of the Balkan peninsula and Turkey appear mostly devoid of points. These LUCAS points were not used as calibration/training data for the year 2018 and represent approximately 3,226 LUCAS points (excluding the UK) used for validation purposes, according to the accompanying text. No legend, scale bar, or coordinate reference system is explicitly displayed.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/img-e2575e0f399b4b95661426ae2f21c6c5c7a0b9bd.png)

Figure 8-3: Approach II sample distribution depending on LUCAS points containing crop type information for the year 2022

![Choropleth map of Europe illustrating the distribution of GSAA (Geospatial Aid Application) data availability for cropland sample selection for the years 2019, 2020, and 2021, used in the Copernicus Land Monitoring Service (CLMS) Croplands product's Approach II. The map uses a colour-coded legend to indicate the year of GSAA data used for sampling: \* Green: 2019 \* Orange: 2020 \* Black: 2021 Countries are coloured based on the year of GSAA data used for sampling within their territory, or left grey if no GSAA data from these years was used for this purpose. \* Denmark is entirely coloured green, indicating GSAA data from 2019 was used for sampling across the country. \* France and Croatia are entirely coloured orange, indicating GSAA data from 2020 was used for sampling across these countries. \* Extensive areas in black are distributed across numerous EU Member States and other European countries, including Sweden, Finland, Estonia, Latvia, Lithuania, Poland, Czechia, Slovakia, Hungary, Romania, Bulgaria, Austria, Slovenia, Italy, Spain, Portugal, Germany, Belgium, and the Netherlands. These black areas indicate where GSAA data from 2021 was used for cropland sampling. \* Countries such as Ireland, the United Kingdom, Norway, Switzerland, Greece, Albania, North Macedonia, Serbia, Bosnia and Herzegovina, and Montenegro, along with uncoloured parts of countries that are partially black, are shown in grey, signifying no GSAA data from 2019, 2020, or 2021 was used for sampling in those regions for this specific application.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/img-d2276222fad84e13af99fab131c83599787f58a8.png)

Figure 8-4: GSAA data availability, per country per year

It is important to note that those samplings do not cover the whole EEA38 due to the availability and specifications of GSAA and LUCAS data, so the reporting levels will differ from approach I.

## 8.3 Response Design

The response design is the protocol used for retrieval of the validation/reference information for all sample units. Two types of datasets are used to perform the interpretation of samples units: guiding data and reference data.

Guiding data are those used for production of HRL Croplands layers and consist mainly of timeseries of Sentinel data.

Reference data are complementary and independent data that can provide more spatial details and landscape context:

- VHR_IMAGE_20186 and VHR_IMAGE_20217: very high resolution optical earth observation imagery, covering EEA38 for the reference years 2018 and 2021 (+-1 year).

- Other external datasets:

  - Bing maps image/ cartography layer

  - Open Street Map data

  - Google Earth Image / cartography data

  - LUCAS data for the years 2018 and 2022 (where available)

  - GSAA data for the year 2018 and 2021 (where available)

  - Sentinel-2 imagery from January / March / May and July 2022

The interpretation workflow for the verification of the crop group consists of thematic plausibility analysis of the sample units. Plausibility analysis means that the class assigned by the layer is known by the interpreter during the interpretation. The Primary Sampling Units were interpreted at the crop group level (Table 8-2) using guiding and reference datasets, considering the surrounding of the sample (typically crop parcel) to properly account for the MMU of 0.25 ha.

Table 8-2: Crop Types layer nomenclature and aggregation levels

| Class code | Land Cover | Crop Group | Level 1(accuracy aggregation) | Crop types (Level 2) |
|----|----|----|----|----|
| 1110 | Arable Crops | Cereals | Cereals | Wheat |
| 1120 | Arable Crops | Cereals | Cereals | Barley |
| 1130 | Arable Crops | Cereals | Maize | Maize |
| 1140 | Arable Crops | Cereals | Rice | Rice |
| 1150 | Arable Crops | Cereals | Cereals | Other cereals |
| 1210 | Arable Crops | Dry pulses & Vegetables | Dry Pulses, Fresh vegetables and Potatoes | Fresh Vegetables |
| 1220 | Arable Crops | Dry pulses & Vegetables | Dry Pulses, Fresh vegetables and Potatoes | Dry pulses |
| 1310 | Arable Crops | Root/tuber crops | Dry Pulses, Fresh vegetables and Potatoes | Potatoes |
| 1320 | Arable Crops | Root/tuber crops | Sugar beet | Sugar Beet |
| 1410 | Arable Crops | Non-permanent industrial crops | Sunflower | Sunflower |
| 1420 | Arable Crops | Non-permanent industrial crops | Soybeans | Soybeans |
| 1430 | Arable Crops | Non-permanent industrial crops | Rapeseed | Rapeseed |
| 1440 | Arable Crops | Non-permanent industrial crops | Flax, cotton and hemp | Flax, cotton and hemp |
| 2100 | Permanent Crops | Permanent Crops | Permanent crops | Grapes |
| 2200 | Permanent Crops | Permanent Crops | Permanent crops | Olives |
| 2310 | Permanent Crops | Permanent Crops | Permanent crops | Fruits |
| 2320 | Permanent Crops | Permanent Crops | Permanent crops | Nuts |
| 3100 | Arable Crops | Unclassified arable crop | Unclassified arable crop | Unclassified arable crop |
| 3200 | Permanent Crops | Unclassified permanent crop | Unclassified permanent crop | Unclassified permanent crop |

For layers where the second sampling design has been applied (see 8.2) and the use of LUCAS and GSAA data were used, the response design is simplified. No visual interpretation is required as the reference class is extracted from LUCAS/GSAA data to be compared to the Crop Types layer without any additional process.

## 8.4 Statistical Analysis

The thematic accuracy level or the Crop Types layer is defined in terms of F-score, which can be derived from confusion matrices. To this end, the row and column totals and the diagonal of the matrix are used to assess two further types of accuracy, the User’s and Producer’s Accuracy:

- Producer’s Accuracy (PA) for a given class = \\\alpha\alpha/C\alpha\\, representing an (inversely proportional) measure of Omission Error. For instance, an observation has been identified as tree-covered in the validation dataset but was actually classified as another class: it has been omitted from the target class.

- User’s Accuracy (UA) for a given class = 𝛼\\\alpha\alpha/R\alpha\\, representing an (inversely proportional) measure of the Commission Error (or contamination risk), i.e. errors due to the wrong allocation of an observation (i.e. mapped landcover) to a landcover class. For instance, an observation is classified as broadleaved tree cover, but identified as belonging to another class during the validation process: this observation has contaminated another class.

F-score is a measure of accuracy calculated as the harmonic mean of the Producer’s and the User’s Accuracies calculated as:

\\ F_1=2.\frac{(P A\\.U A)}{(P A+U A)} \\

For both Crop Types layers 2018 and 2021 the F1 scores are computed derived for each class of crop group level (6 classes) and aggregation level 1 (11 classes) (Table 8-2).

## 8.5 Verification Results

The assessed accuracies for the Crop Types layers are presented at the crop group level (gridbased random sampling) and the aggregation level 1 (11 classes, opportunistic sampling from LUCAS and GSAA data). For the rationale on the different sampling designs please refer to section 8.2)

### 8.5.1 Crop Group level

At the crop group level, a total of 12960 (out of 14000 initially allocated) are available for the statistical analysis. The reminder has been disregarded due factors such as uncertain reference data or locations partially outside the area of interest. Accuracy figures for crop group level are presented in the confusion matrices shown for the EU27 in Table 8-4 and the EEA38 in Table 8-5.

At the crop group level, the layers should reach an F1-score of 85% for each class. This is the case for all classes for all reference years 2018, 2021 and 2022 at EU27 level, even crop types which present a lower number of samples such as root/tuber or dry pulses and vegetables. At EEA38 level, the results are similar with the exception of permanent crops class that reach accuracies slightly below the 85% threshold (83-84%). Generally, the accuracies at the crop group level are also fairly consistent across the different reference years.

Since the unclassified crop class’ purpose is to express uncertainty of the classification rather than presenting an actual class no accuracies are given, sample counts are still provided for the sake of completeness.

Table 8-3 Crop group level class codes

| Class code | Crop Group                     |
|------------|--------------------------------|
| 11         | Cereals                        |
| 12         | Dry pulses & Vegetables        |
| 13         | Root/tuber crops               |
| 14         | Non-permanent industrial crops |
| 20         | Permanent Crops                |
| 30         | Unclassified crop              |

Table 8-4 HRL Crop Types accuracies for crop groups, EU27 (for the class codes see Table 8-3)

**CTY2018 - EU27 (Weighted)**

| Product   | Ref. 0  | Ref. 11 | Ref. 12 | Ref. 13 | Ref. 14 | Ref. 20 | Ref. 30 | Total   |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|
| 0         | 5156.57 | 164.00  | 2.01    | 0.01    | 2.00    | 21.02   | 1.00    | 5346.60 |
| 11        | 2.00    | 816.07  |         |         |         |         |         | 818.07  |
| 12        |         |         | 63.01   |         |         |         |         | 63.01   |
| 13        |         |         |         | 51.00   |         |         |         | 51.00   |
| 14        | 1.00    | 1.00    |         |         | 203.01  | 1.00    |         | 206.01  |
| 20        | 10.01   | 4.00    |         |         |         | 160.46  | 1.00    | 175.48  |
| 30        | 3.00    | 25.00   |         |         |         | 1.00    | 8.04    | 37.04   |
| **Total** | 5172.58 | 1010.07 | 65.02   | 51.01   | 205.01  | 183.49  | 10.04   | 6697.22 |

| Metric         | 0      | 11     | 12      | 13      | 14     | 20     | 30  |
|----------------|--------|--------|---------|---------|--------|--------|-----|
| **Prod. Acc.** | 99.69% | 80.79% | 96.91%  | 99.99%  | 99.02% | 87.45% |     |
| **User Acc.**  | 96.45% | 99.76% | 100.00% | 100.00% | 98.54% | 91.45% |     |
| **F-score**    | 98.04% | 89.28% | 98.43%  | 99.99%  | 98.78% | 89.40% |     |

**CTY2021 - EU27 (Weighted)**

| Product   | Ref. 0  | Ref. 11 | Ref. 12 | Ref. 13 | Ref. 14 | Ref. 20 | Ref. 30 | Total   |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|
| 0         | 5127.29 | 133.02  | 0.01    | 0.00    | 2.00    | 19.04   | 1.00    | 5282.36 |
| 11        | 6.01    | 898.75  |         |         |         | 0.01    |         | 904.77  |
| 12        | 1.00    |         | 72.16   |         |         |         |         | 73.16   |
| 13        |         |         |         | 49.06   |         |         |         | 49.06   |
| 14        | 3.00    | 1.00    |         |         | 197.19  |         |         | 201.19  |
| 20        | 10.02   | 2.01    |         |         |         | 164.56  | 0.00    | 176.59  |
| 30        | 1.00    | 5.00    |         |         |         |         | 6.07    | 12.07   |
| **Total** | 5148.32 | 1039.78 | 72.17   | 49.06   | 199.19  | 183.61  | 7.07    | 6699.20 |

| Metric         | 0      | 11     | 12     | 13      | 14     | 20     | 30  |
|----------------|--------|--------|--------|---------|--------|--------|-----|
| **Prod. Acc.** | 99.59% | 86.44% | 99.99% | 100.00% | 99.00% | 89.63% |     |
| **User Acc.**  | 97.06% | 99.33% | 98.63% | 100.00% | 98.01% | 93.19% |     |
| **F-score**    | 98.31% | 92.44% | 99.31% | 100.00% | 98.50% | 91.37% |     |

**CTY2022 - EU27 (Weighted)**

| Product   | Ref. 0  | Ref. 11 | Ref. 12 | Ref. 13 | Ref. 14 | Ref. 20 | Ref. 30 | Total   |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|
| 0         | 5155.97 | 75.21   | 0.01    | 0.00    | 2.01    | 21.06   | 0.00    | 5254.27 |
| 11        | 9.08    | 874.54  | 0.01    |         | 6.01    | 1.00    |         | 890.63  |
| 12        | 2.03    |         | 79.12   |         | 1.00    | 3.00    |         | 85.16   |
| 13        | 0.00    | 4.00    |         | 27.03   | 1.00    |         |         | 32.03   |
| 14        | 0.00    |         |         |         | 205.25  |         |         | 205.26  |
| 20        | 14.11   | 7.00    | 2.01    |         | 1.01    | 167.65  | 1.00    | 192.77  |
| 30        | 3.04    | 7.03    | 1.00    |         | 1.00    | 0.01    | 7.01    | 19.08   |
| **Total** | 5184.23 | 967.78  | 82.15   | 27.03   | 217.27  | 192.71  | 8.01    | 6679.20 |

| Metric         | 0      | 11     | 12     | 13     | 14      | 20     | 30  |
|----------------|--------|--------|--------|--------|---------|--------|-----|
| **Prod. Acc.** | 99.45% | 90.36% | 96.32% | 99.99% | 94.47%  | 86.99% |     |
| **User Acc.**  | 98.13% | 98.19% | 92.91% | 84.38% | 100.00% | 86.97% |     |
| **F-score**    | 98.79% | 94.12% | 94.59% | 91.52% | 97.15%  | 86.98% |     |

Table 8-5: HRL Crop Types accuracies for crop groups, EEA38 (for the class codes see Table 8-3)

**CTY2018 - EEA38 (Weighted)**

| Product   | Ref. 0  | Ref. 11 | Ref. 12 | Ref. 13 | Ref. 14 | Ref. 20 | Ref. 30 | Total   |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|
| 0         | 6810.95 | 188.08  | 3.01    | 0.01    | 31.00   | 42.06   | 1.00    | 7076.11 |
| 11        | 20.02   | 960.10  |         | 0.00    | 18.00   |         |         | 998.12  |
| 12        | 2.00    | 3.00    | 93.04   |         | 1.00    |         |         | 99.04   |
| 13        |         | 1.00    |         | 52.00   |         |         |         | 53.00   |
| 14        | 1.00    | 13.00   |         |         | 226.01  | 1.00    |         | 241.01  |
| 20        | 18.02   | 5.00    |         |         | 2.00    | 179.51  | 1.00    | 205.54  |
| 30        | 5.00    | 26.01   | 1.00    |         | 4.00    | 1.00    | 8.04    | 45.05   |
| **Total** | 6857.00 | 1196.19 | 97.05   | 52.01   | 282.02  | 223.56  | 10.04   | 8717.87 |

| Metric         | 0      | 11     | 12     | 13     | 14     | 20     | 30  |
|----------------|--------|--------|--------|--------|--------|--------|-----|
| **Prod. Acc.** | 99.33% | 80.26% | 95.87% | 99.98% | 80.14% | 80.29% |     |
| **User Acc.**  | 96.25% | 96.19% | 93.94% | 98.11% | 93.78% | 87.34% |     |
| **F-score**    | 97.77% | 87.51% | 94.89% | 99.04% | 86.42% | 83.67% |     |

**CTY2021 - EEA38 (Weighted)**

| Product   | Ref. 0  | Ref. 11 | Ref. 12 | Ref. 13 | Ref. 14 | Ref. 20 | Ref. 30 | Total   |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|
| 0         | 6784.24 | 157.07  | 1.01    | 0.01    | 23.00   | 48.07   | 1.01    | 7014.40 |
| 11        | 22.07   | 1041.09 | 6.00    |         | 26.00   | 0.01    |         | 1095.17 |
| 12        | 1.01    | 4.02    | 82.18   |         | 2.00    |         | 1.00    | 90.21   |
| 13        | 1.00    |         |         | 52.07   | 1.00    |         | 0.00    | 54.07   |
| 14        | 4.00    | 20.01   | 2.00    |         | 216.22  | 1.01    |         | 243.24  |
| 20        | 17.02   | 3.02    |         |         | 2.00    | 179.61  | 0.00    | 201.65  |
| 30        | 2.02    | 8.00    | 2.00    |         | 3.00    |         | 8.07    | 23.09   |
| **Total** | 6831.37 | 1233.21 | 93.19   | 52.08   | 273.22  | 228.70  | 10.09   | 8721.85 |

| Metric         | 0      | 11     | 12     | 13     | 14     | 20     | 30  |
|----------------|--------|--------|--------|--------|--------|--------|-----|
| **Prod. Acc.** | 99.31% | 84.42% | 88.18% | 99.99% | 79.14% | 78.54% |     |
| **User Acc.**  | 96.72% | 95.06% | 91.10% | 96.30% | 88.89% | 89.07% |     |
| **F-score**    | 98.00% | 89.43% | 89.62% | 98.11% | 83.73% | 83.47% |     |

**CTY2022 - EEA38 (Weighted)**

| Product   | Ref. 0  | Ref. 11 | Ref. 12 | Ref. 13 | Ref. 14 | Ref. 20 | Ref. 30 | Total   |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|
| 0         | 7058.92 | 88.25   | 0.01    | 0.00    | 10.01   | 42.10   | 1.01    | 7200.31 |
| 11        | 16.08   | 1050.90 |         |         | 11.01   | 1.01    | 0.00    | 1079.00 |
| 12        | 0.03    |         | 98.19   |         |         | 1.01    |         | 99.23   |
| 13        |         |         |         | 42.05   |         |         |         | 42.05   |
| 14        | 0.01    | 14.00   |         |         | 240.30  | 0.00    | 1.00    | 255.32  |
| 20        | 17.12   | 9.01    | 2.01    |         | 2.01    | 187.68  | 1.00    | 218.83  |
| 30        | 4.05    | 19.05   | 2.00    | 0.00    | 3.00    | 0.01    | 8.01    | 36.13   |
| **Total** | 7096.20 | 1181.22 | 102.21  | 42.05   | 266.33  | 231.82  | 11.03   | 8930.86 |

| Metric         | 0      | 11     | 12     | 13      | 14     | 20     | 30  |
|----------------|--------|--------|--------|---------|--------|--------|-----|
| **Prod. Acc.** | 99.47% | 88.97% | 96.07% | 99.99%  | 90.23% | 80.96% |     |
| **User Acc.**  | 98.04% | 97.40% | 98.95% | 100.00% | 94.12% | 85.77% |     |
| **F-score**    | 98.75% | 92.99% | 97.49% | 99.99%  | 92.13% | 83.29% |     |

### 8.5.2 Aggregation level 1

Accuracy figures and sample counts for Crop Types layers at Aggregation Level 1 are presented in Table 8-6 below, according to the comparisons with LUCAS and GSSA data.

The target accuracy at this analysis level is an F-Score of 80% for each of the classes. The crop types cereals and maize generally exceed the 80% threshold in all years, sugar beet, sunflower, and rapeseed meet or miss the threshold depending on the year and reference dataset. The accuracies for the other classes generally remain below the 80% threshold. The F-scores for classes / years with very few samples (flax, cotton, hemp, rice, and soybean) must be interpreted with caution.

While the assessed accuracies vary depending on the reference datasets and reference years there is a general tendency for the figures to improve with an increasing number of available reference samples (see last row in Table 8-6).

Table 8-6: Accuracies for CTY 2018-2021 at aggregation level-1

|  |  | All GSAA data (2019 2020, 2021) | All GSAA data (2019 2020, 2021) | LUCAS 2018 | LUCAS 2018 | LUCAS 2022 | LUCAS 2022 |
|----|----|----|----|----|----|----|----|
| Class | Code | n samples | F-score | n samples | F-score | n samples | F-score |
| Other Cereals | 11 | 921 | 85.00% | 1571 | 84.50% | 16072 | 89.90% |
| Maize | 1130 | 400 | 87.90% | 458 | 82.20% | 5038 | 91.04% |
| Rice | 1140 | 0 |  | 2 |  | 21 | 66.67% |
| Dry pulses, Fresh vegetables & potatoes | 12 | 193 | 65.40% | 185 | 66.70% | 1884 | 73.41% |
| Sugar beet | 1320 | 17 | 68.60% | 70 | 91.50% | 673 | 81.15% |
| Sunflower | 1410 | 36 | 77.10% | 130 | 79.20% | 1319 | 89.03% |
| Soybeans | 1420 | 20 | 65.40% | 22 | 50.00% | 401 | 77.24% |
| Rapeseed | 1430 | 84 | 80.40% | 148 | 83.00% | 2505 | 76.75% |
| Flax, cotton and hemp | 1440 | 4 | 50.00% | 10 | 77.80% | 189 | 79.67% |
| Permanent crops | 20 | 300 | 73.50% | 385 | 67.30% | 4208 | 63.46% |
| Macro average |  | 198 | 72.59% | 298 | 75.80% | 3231 | 78.83% |

# 9 Terms of use and product technical support

## 9.1 Terms of use

The product(s) described in this document is/are created in the frame of the Copernicus programme of the European Union by the European Environment Agency (product custodian) and is/are owned by the European Union. The product(s) can be used following Copernicus full free and open data policy, which allows the use of the product(s) also for any commercial purpose. Derived products created by end users from the product(s) described in this document are owned by the end users, who have all intellectual rights to the derived products.

## 9.2 Citation

In cases of re-dissemination of the product(s) described in this document or when the product(s) is/are used to create a derived product it is required to provide a reference to the source. A template is provided below:

“© European Union, Copernicus Land Monitoring Service , European Environment Agency (EEA)”

## 9.3 Product technical support

Product technical support is provided by the product custodian through Copernicus Land Monitoring Service helpdesk at copernicus@eea.europa.eu. Product technical support does not include software specific user support or general GIS or remote sensing support.

# 10 List of Abbreviations & Acronyms

| Abbreviation | Name                                                         |
|--------------|--------------------------------------------------------------|
| ATBD         | Algorithm Theoretical Basis Document                         |
| BS           | Bare Soil                                                    |
| BVL          | Base Vegetation Layer                                        |
| CAP          | Common Agricultural Policy                                   |
| CL           | Confidence Layer                                             |
| CLC          | CORINE Land Cover                                            |
| CLMS         | Copernicus Land Monitoring Service                           |
| COG          | Cloud-Optimized GeoTIFFs                                     |
| CORINE       | Coordination of information on the environment               |
| CP           | Cropping Patterns                                            |
| CPBSB        | Bare Soil Before                                             |
| CPBSBCL      | Bare Soil Before Confidence Layer                            |
| CPBSA        | Bare Soil After                                              |
| CPBSACL      | Bare Soil After Confidence Layer                             |
| CPCST        | Cropping Seasons Types over 3 years                          |
| CPCSY        | Cropping Seasons Yearly                                      |
| CPFLD        | Fallow Land Duration                                         |
| CPFLDCL      | Fallow Land Duration Confidence Layer                        |
| CPFLP        | Fallow Land Presence                                         |
| CPFLPCL      | Fallow Land Presence Confidence Layer                        |
| CPMCD        | Main Crop Duration                                           |
| CPMCDCL      | Main Crop Duration Confidence Layer                          |
| CPMCE        | Main Crop Emergence                                          |
| CPMCECL      | Main Crop Emergence Confidence Layer                         |
| CPMCH        | Main Crop Harvest                                            |
| CPMCHCL      | Main Crop Harvest Confidence Layer                           |
| CPSCT        | Secondary Crops Type                                         |
| CPSD         | Secondary Crops Duration                                     |
| CPSCDCL      | Secondary Crops Duration Confidence Layer                    |
| CPSE         | Secondary Crops Emergence                                    |
| CTY          | Crop Types                                                   |
| CTYCL        | Crop Types Confidence Layer                                  |
| DLT          | Dominant Leaf Type                                           |
| DLTC         | Dominant Leaf Type Change                                    |
| DOY          | Day Of Year                                                  |
| EAGLE        | EIONET Action Group on Land monitoring in Europe             |
| ECoLaSS      | Evolution of Copernicus Land Services based on Sentinel Data |
| EEA          | European Environment Agency                                  |
| EEA38        | The 32 member and 6 cooperating countries of the EEA         |
| EIONET       | European Environment Information and Observation Network     |
| EO           | Earth Observation                                            |
| EU           | European Union                                               |
| EU27         | The 27 member states of the EU                               |
| fAPAR        | Fraction of absorbed photosynthetically active radiation     |
| FLP          | Fallow Land Presence                                         |
| FML          | Forest Monitoring Law                                        |
| GIS          | Geographic Information System                                |
| GRD          | Ground Resolved Distance                                     |
| GSAA         | GeoSpatial Aid Application                                   |
| H2020        | Horizon2020                                                  |
| HER          | Herbaceous Cover Layer                                       |
| HR           | High Resolution                                              |
| HRL / HRLs   | High Resolution Layer / High Resolution Layers               |
| HRL VLCC     | High Resolution Layer – Vegetated Land Cover Characteristics |
| ID           | Identification Number                                        |
| IPCC         | Intergovernmental Panel on Climate Change                    |
| JRC          | Joint Research Centre                                        |
| LAEA         | Lambert Azimuthal Equal Area projection                      |
| LU           | Land Use                                                     |
| LUCAS        | Land Use / Cover Area frame Survey                           |
| LULUCF       | Land Use, Land Use Change and Forestry                       |
| MC           | Main Crops                                                   |
| MMU          | Minimum Mapping Unit                                         |
| OA           | Overall Accuracy                                             |
| PA           | Producer Accuracy                                            |
| PAM          | Permanent Auxiliary metadata                                 |
| SC           | Secondary Crops                                              |
| TCD          | Tree Cover Density                                           |
| UA           | User’s Accuracy                                              |
| UK           | United Kingdom                                               |
| USDA         | U.S. Department of Agriculture                               |
| UTM          | Universal Transverse Mercator                                |
| VHR          | Very High Resolution                                         |
| VITO         | Vlaamse Instelling voor Technologisch Onderzoek              |
| XML          | Extensible Markup Language                                   |

# 11 References

\[1\] Eurostat. (2018). LUCAS Survey 2018. \[Data set\]. https://ec.europa.eu/eurostat/web/lucas/database/primary-data.

\[2\] Eurostat. (2022). LUCAS Survey 2022. \[Data set\]. https://ec.europa.eu/eurostat/web/lucas/database/primary-data.

\[3\] Selkowitz, D. J., & Stehman, S. V. (2011). Thematic accuracy of the National Land Cover Database (NLCD) 2001 land cover for Alaska. Remote Sensing of Environment, 115(6), 1401-1407.

\[4\] Olofsson, P., Foody, G. M., Stehman, S. V., & Woodcock, C. E. (2013). Making better use of accuracy data in land change studies: Estimating accuracy and area and quantifying uncertainty using stratified estimation. Remote Sensing of Environment, 129, 122-131.

\[5\] ECoLaSS (2019). Deliverable D3.2 - Service Evolution Requirements Report Vol. 2 https://www.ecolass.eu/\_files/ugd/c90769_5a431f06039141a6b4db4d6b4596d272.pdf (accessed 28 October 2024)

\[6\] Nextspace (2018 ). Work performed by the Nextspace consortium – Observation Requirements (February 2018); https://www.copernicus.eu/en/documentation/technicaldocuments/technical-documents (accessed 28 October 2024)

\[7\] CLMS HRL VLCC (2025). HRL VLCC Algorithm Theoretical Basis Document; https://land.copernicus.eu/en/technical-library/algorithm-theoretical-basis-documentpan-european-land-cover-characteristics

\[8\] CLMS HRL Forests 2018 (2021). HRL Tree-cover/forest and change 2015-2018 User Manual, https://land.copernicus.eu/en/technical-library/hrl-forest-2018

\[9\] CLMS HRL Grassland 2018 (2021). Grassland 2018 and Grassland change 2015-2018 User Manual, https://land.copernicus.eu/en/technical-library/hrl-grassland-2018-product-usermanual

\[10\] Dadrass Javan, F., Samadzadegan, F., Toosi, A., Schneider, M., & Persello, C. (2025). Ground Resolved Distance Estimation of Sentinel-2 Imagery Using Edge-based SceneDriven Approach. PFG – Journal of Photogrammetry, Remote Sensing and Geoinformation Science, 93(2), 131–152. https://doi.org/10.1007/s41064-024-00330-x

\[11\] CLMS HRL Tree Cover & Forests (2025). CLMS HRL Tree Cover & Forests - Product User Manual; https://land.copernicus.eu/en/technical-library/product-user-manual-tree-coverand-forests-2018-present

\[12\] CLMS HRL Grasslands (2025). CLMS HRL Grasslands - Product User Manual; https://land.copernicus.eu/en/technical-library/product-user-manual-grasslands-2017-present

# 12 Annex I – Colour tables for HRL Croplands

![This table provides the class codes, names, and corresponding Red, Green, Blue (RGB) colour values for the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Crop Types (CTY) layer. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|:-----------\|:-------------------\|:----\|:------\|:-----\| \| 0 \| No Cropland \| 240 \| 240 \| 240 \| \| 1110 \| Wheat \| 238 \| 110 \| 50 \| \| 1120 \| Barley \| 251 \| 162 \| 74 \| \| 1130 \| Maize \| 250 \| 220 \| 20 \| \| 1140 \| Rice \| 233 \| 67 \| 1 \| \| 1150 \| Other Cereals \| 232 \| 169 \| 149 \| \| 1210 \| Fresh Vegetables \| 174 \| 199 \| 232 \| \| 1220 \| Dry Pulses \| 72 \| 151 \| 191 \| \| 1310 \| Potatoes \| 201 \| 140 \| 67 \| \| 1320 \| Sugar Beet \| 156 \| 91 \| 12 \| \| 1410 \| Sunflower \| 255 \| 121 \| 121 \| The table defines a colour scheme for visualising different crop types, with 'No Cropland' assigned a light grey (RGB 240, 240, 240), cereals in shades of orange to yellow, vegetables and pulses in blues, and root crops and oilseeds in browns and reds.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image2.png)

![This table presents the colour palette and attributes for various High Resolution Layer (HRL) Crop Types (CTY) as used in the Copernicus Land Monitoring Service (CLMS). It lists a unique Class Value, the corresponding Crop Type, and its RGB colour components, along with a visual colour sample. \| Class Value \| Crop Type \| R \| G \| B \| \|:------------\|:--------------------------\|:----\|:----\|:----\| \| 1420 \| Soybeans \| 168 \| 106 \| 150 \| \| 1430 \| Rapeseed \| 227 \| 119 \| 194 \| \| 1440 \| Flax, cotton and hemp \| 247 \| 182 \| 210 \| \| 2100 \| Grapes \| 219 \| 219 \| 141 \| \| 2200 \| Olives \| 193 \| 206 \| 18 \| \| 2310 \| Fruits \| 121 \| 160 \| 58 \| \| 2320 \| Nuts \| 90 \| 124 \| 48 \| \| 3100 \| Unclassified arable crop \| 215 \| 215 \| 215 \| \| 3200 \| Unclassified permanent crop \| 171 \| 171 \| 171 \| \| 65535 \| Outside area \| 255 \| 255 \| 255 \| The table provides a standard set of colours for visualising different HRL Crop Types. Specific crop categories like Soybeans and Rapeseed are assigned distinct colours, while generic classes such as 'Unclassified arable crop', 'Unclassified permanent crop', and 'Outside area' are represented by shades of grey and black, respectively.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image3.png)

Table 0-1: Colour palette and attributes of HRL Crop Types (CTY) layer

![\| Class Code \| Class Name \| Red \| Green \| Blue \| \|---\|---\|---\|---\|---\| \| 0 \| 0% classification confidence \| 255 \| 0 \| 0 \| \| 1-49 \| 1-49% classification confidence \| colour shades in between \| colour shades in between \| colour shades in between \| \| 50 \| 50% classification confidence \| 255 \| 255 \| 0 \| \| 51-99 \| 51-99% classification confidence \| colour shades in between \| colour shades in between \| colour shades in between \| \| 100 \| 100% classification confidence \| 8 \| 99 \| 0 \| \| 254 \| No cropland \| 240 \| 240 \| 240 \| \| 255 \| Outside area \| 0 \| 0 \| 0 \| This table defines the colour palette and RGB attributes for different classification confidence levels within the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Crop Types (CTY) product. Pixels with 0% classification confidence are assigned red (RGB 255, 0, 0), 50% confidence yellow (RGB 255, 255, 0), and 100% confidence dark green (RGB 8, 99, 0). Intermediate confidence ranges (1-49% and 51-99%) are represented by colour shades transitioning between these primary values. Additionally, 'No cropland' areas are light grey (RGB 240, 240, 240), and 'Outside area' is black (RGB 0, 0, 0).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image4.png)

Table 0-2: Colour palette and attributes of CTYCL layer

![This table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Crop Types (CTY) layer. It maps 'Class Code' to 'Class Name' and specifies the corresponding Red, Green, and Blue (RGB) colour values. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|---\|---\|---\|---\|---\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 17090 \| Apr (product year) \| 255 \| 128 \| 159 \| \| 17120 \| May (product year) \| 255 \| 176 \| 127 \| \| 17151 \| Jun (product year) \| 255 \| 223 \| 128 \| \| 17181 \| Jul (product year) \| 223 \| 255 \| 128 \| \| 17212 \| Aug (product year) \| 159 \| 255 \| 128 \| \| 17243 \| Sep (product year) \| 109 \| 220 \| 141 \| \| 17273 \| Oct (product year) \| 128 \| 255 \| 223 \| \| 17304 \| Nov (product year) \| 128 \| 223 \| 255 \| \| 17334 \| Dec (product year) \| 127 \| 189 \| 255 \| \| 18365 \| Jan (product year+1) \| 64 \| 0 \| 255 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| The table provides RGB colour definitions for annual cropland by month, spanning April of the product year to January of the subsequent year (product year+1). Class 0 represents 'No annual cropland' with a light grey (240,240,240). The monthly crop types transition from pinks/oranges (Apr, May) through yellows/greens (Jun, Jul, Aug, Sep) to blues (Oct, Nov, Dec, Jan). Two additional codes, 65526 and 65527, are assigned light grey (225,225,225) and medium grey (200,200,200) respectively, with their Class Name being identical to their Class Code.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image5.png)

![A partial table displaying colour palette attributes. The column headers are not visible in the provided image snippet. The table lists three rows of data. \* \*\*Row 1\*\*: Code 65531, followed by two empty cells, then repeated Code 65531, with RGB values R=100, G=100, B=100, represented by a dark grey colour swatch. \* \*\*Row 2\*\*: Code 65532, followed by two empty cells, then repeated Code 65532, with RGB values R=75, G=75, B=75, represented by a dark grey colour swatch. \* \*\*Row 3\*\*: Code 65533, followed by two empty cells, then repeated Code 65533, with RGB values R=126, G=52, B=107, represented by a purple colour swatch. \| Code 1 \| \[unreadable/missing header\] \| \[unreadable/missing header\] \| Code 2 \| R \| G \| B \| Colour Sample \| \|---\|---\|---\|---\|---\|---\|---\|---\| \| 65531 \| \| \| 65531 \| 100 \| 100 \| 100 \| Dark Grey \| \| 65532 \| \| \| 65532 \| 75 \| 75 \| 75 \| Dark Grey \| \| 65533 \| \| \| 65533 \| 126 \| 52 \| 107 \| Purple \| This table provides integer codes and corresponding RGB colour values for specific entries in a Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands product, identified as 'C' \[partial\] layer in the context. The first two entries (65531 and 65532) share similar dark grey colours with slightly different RGB values, while the third entry (65533) is distinctly purple.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image6.png)

![This image displays a single row from a colour palette and attributes table, likely associated with a Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands product, based on the surrounding context. The row represents data classified as 'Outside area'. \| Pixel Value (Class ID) \| Class Name \| R \| G \| B \| Colour Swatch \| \|---\|---\|---\|---\|---\|---\| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| black \| The 'Pixel Value' of 65535 typically indicates a 'no data' or 'fill value' for areas outside the product's defined geographic extent or processing domain. The 'Class Name' for this value is 'Outside area'. The R, G, and B values of 0, 0, 0 collectively represent the colour black, as depicted by the solid black rectangle in the 'Colour Swatch' column.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image7.png)

Table 0-3: Colour palette and attributes of CPMCH layer

![This table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands CPMCE layer, providing Class Codes, Class Names, and corresponding Red, Green, and Blue (RGB) component values. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|------------\|------------------------\|------------------------\|------------------------\|------------------------\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 1 \| 1 day uncertainty \| 202 \| 0 \| 32 \| \| 1-19 \| 1-19 days uncertainty \| Colour shades in between \| \| \| \| 20 \| 20 days uncertainty \| 247 \| 243 \| 241 \| \| 21-39 \| 21-39 days uncertainty \| Colour shades in between \| \| \| \| 40 \| 40 days uncertainty \| 5 \| 113 \| 176 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| \| 65534 \| 65534 \| 179 \| 48 \| 179 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The table maps class codes to land cover categories and their associated colour representations. It includes specific RGB values for distinct classes such as 'No annual cropland' (light grey, RGB 240, 240, 240), '1 day uncertainty' (red, RGB 202, 0, 32), '20 days uncertainty' (very light grey, RGB 247, 243, 241), and '40 days uncertainty' (blue, RGB 5, 113, 176). For class code ranges '1-19 days uncertainty' and '21-39 days uncertainty', the table indicates 'Colour shades in between' for the RGB values. Additional class codes (65526 to 65534) are provided, with their Class Names being the codes themselves, representing a progression of greyscale tones and two purple shades. Class 655](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image8.png)

Table 0-4: Colour palette and attributes of CPMCHCL layer

![This table provides the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands CPMCD layer. It lists 'Class Code', 'Class Name', and Red, Green, and Blue (RGB) colour component values, alongside a visual representation of the colour. \| Class Code \| Class Name \| Red \| Green \| Blue \| \| :--------- \| :----------------- \| --: \| ----: \| ---: \| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 16214 \| Aug (product year-1) \| 72 \| 135 \| 67 \| \| 16245 \| Sep (product year-1) \| 101 \| 204 \| 129 \| \| 16276 \| Oct (product year-1) \| 125 \| 252 \| 200 \| \| 16306 \| Nov (product year-1) \| 128 \| 255 \| 223 \| \| 16336 \| Dec (product year-1) \| 128 \| 223 \| 255 \| \| 16366 \| Jan (product year) \| 159 \| 127 \| 255 \| \| 17031 \| Feb (product year) \| 221 \| 127 \| 255 \| \| 17059 \| Mar (product year) \| 255 \| 127 \| 223 \| The table details distinct colours for 'No annual cropland' (light grey, RGB 240, 240, 240) and various monthly periods related to crop development. These monthly periods span from 'Aug (product year-1)' (dark green, RGB 72, 135, 67) to 'Mar (product year)' (pink, RGB 255, 127, 223), showing a progression of hues from greens, through teals and light blues, to purples and pinks.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image9.png)

![\| Value \| Attribute \| R \| G \| B \| Colour representation \| \|---\|---\|---\|---\|---\|---\| \| 17120 \| Apr (product year) \| 255 \| 127 \| 161 \| Pink \| \| 17151 \| May (product year) \| 255 \| 176 \| 127 \| Orange \| \| 17181 \| Jun (product year) \| 255 \| 223 \| 128 \| Yellow \| \| 17212 \| Jul (product year) \| 223 \| 255 \| 128 \| Light Green \| \| 17243 \| Aug (product year) \| 159 \| 255 \| 128 \| Medium Green \| \| 17273 \| Sep (product year) \| 109 \| 220 \| 141 \| Darker Green \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| Light Grey \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| Medium Grey \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| Dark Grey \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| Darker Grey \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| Purple \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| Black \| This table, titled 'Table 0-7: Colour palette and attributes of CPMCD layer', defines the colour scheme and associated attributes for the Cropland Parcel Monitoring Crop Type Density (CPMCD) layer within the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands product. It lists numerical pixel values, their descriptive attributes (including specific months indicating a product year or phenological stage, or specific codes like 65526-65533, and 'Outside area'), and the corresponding Red, Green, and Blue (RGB) colour components for visual representation. The monthly attributes (Apr-Sep) show a progression from pink to various shades of green, while the numerical codes 65526 through 65532 are assigned shades of grey, and 65533 is purple. The 'Outside area' attribute is assigned the value 65535 and represented by black (RGB 0,0,0).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image10.png)

Table 0-5: Colour palette and attributes of CPMCE layer

![This table provides the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands Permanent Minor Cultivated Dynamics (CPMCD) layer. It maps \`Class Code\` to \`Class Name\` and defines the corresponding Red, Green, and Blue (RGB) colour components. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|---\|---\|---\|---\|---\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 1 \| 1 day uncertainty \| 202 \| 0 \| 32 \| \| 1-19 \| 1-19 days uncertainty \| Colour shades in between \| \| \| \| 20 \| 20 days uncertainty \| 247 \| 243 \| 241 \| \| 21-39 \| 21-39 days uncertainty \| Colour shades in between \| \| \| \| 40 \| 40 days uncertainty \| 5 \| 113 \| 176 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| \| 65534 \| 65534 \| 179 \| 48 \| 179 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The table details specific uncertainty ranges for cropland detection, such as '1 day uncertainty' (Class Code 1, RGB 202, 0, 32) and '40 days uncertainty' (Class Code 40, RGB 5, 113, 176). Intermediate ranges like '1-19 days uncertainty' and '21-39 days uncertainty' are represented by colour shades in between the defined RGB values. Miscellaneous codes (65526, 65527, 65531, 65532, 65533, 65534) are also assigned specific RGB values, and 'Outside area' (Class Code 65535) is mapped to black (RGB 0, 0, 0).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image11.png)

Table 0-6: Colour palette and attributes of CPMCECL layer

![This table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Cropland Phenology Monitoring - Cropping Duration (CPMCD) layer. It maps specific class codes and names to Red, Green, and Blue (RGB) colour values. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|---\|---\|---\|---\|---\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 40 \| 40 days \| 215 \| 25 \| 28 \| \| 41-189 \| 41-189 days \| Colour shades in between \| Colour shades in between \| Colour shades in between \| \| 190 \| 190 days \| 255 \| 243 \| 178 \| \| 191-365 \| 191-365 days \| Colour shades in between \| Colour shades in between \| Colour shades in between \| \| 366 \| 366 days \| 26 \| 150 \| 65 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The table details distinct RGB values for specific cropping durations: 'No annual cropland' (white, RGB 240,240,240), '40 days' (red, RGB 215,25,28), '190 days' (light yellow, RGB 255,243,178), and '366 days' (green, RGB 26,150,65). For duration ranges '41-189 days' and '191-365 days', the colour is specified as 'Colour shades in between', implying interpolation. Additionally, it lists specific class codes (65526, 65527, 65531, 65532, 65533, 65535) with corresponding grayscale shades (light to very dark grey), a purple (RGB 126,52,107), and black for 'Outside area' (RGB 0,0,0).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image12.png)

Table 0-7: Colour palette and attributes of CPMCD layer

![This table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) CPMCDCL layer. It maps Class Codes and Class Names to their corresponding Red, Green, and Blue (RGB) colour components. \| Class Code \| Class Name \| Red \| Green \| Blue \| \| :--------- \| :--------------------- \| :-- \| :---- \| :--- \| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 1 \| 1 \| 202 \| 0 \| 32 \| \| 2-29 \| 2-29 days uncertainty \| Colour shades in between \| \| 30 \| 30 days uncertainty \| 247 \| 245 \| 243 \| \| 31-59 \| 31-59 days uncertainty \| Colour shades in between \| \| 60 \| \>60 days uncertainty \| 5 \| 113 \| 176 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| \| 65534 \| 65534 \| 179 \| 48 \| 179 \| The table details specific colour assignments for categories such as 'No annual cropland' (RGB 240, 240, 240) and various levels of 'days uncertainty' (e.g., '30 days uncertainty' is RGB 247, 245, 243; '\>60 days uncertainty' is RGB 5, 113, 176). Intermediate uncertainty ranges like '2-29 days uncertainty' and '31-59 days uncertainty' are represented by colour shades derived between defined values. Several class codes (1, 65526 through 65534) also have corresponding RGB values, with some of the higher codes using various shades of grey.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image13.png)

![This table row specifies the colour palette attributes for a land cover class designated as 'Outside area' within a Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) product, likely related to Croplands (CTY) based on the surrounding document context. \| Value \| Description \| R \| G \| B \| Colour \| \|---\|---\|---\|---\|---\|---\| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| (black) \| The 'Outside area' class is assigned a pixel value of 65535, and its colour is defined by RGB values of (0, 0, 0), which corresponds to black.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image14.png)

Table 0-8: Colour palette and attributes of CPMCDCL layer

![This table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) CPMCH (Cropland Monthly Change) layer. It lists Class Codes, their corresponding Class Names, and the Red, Green, and Blue (RGB) colour components (0-255) used for visualisation. A visual colour swatch is provided in the rightmost column. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|:-----------\|:-------------------------\|:-------------------------\|:------\|:-----\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 10 \| 10 days \| 214 \| 44 \| 58 \| \| 11-74 \| 11-74 days \| Colour shades in between \| \| \| \| 75 \| 75 days \| 247 \| 247 \| 247 \| \| 76-149 \| 76-149 days \| Colour shades in between \| \| \| \| 150 \| \> 150 days \| 5 \| 113 \| 176 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65529 \| 65529 \| 150 \| 150 \| 150 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| \| 65534 \| 65534 \| 179 \| 48 \| 179 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The table maps temporal categories, such as '10 days' and '\> 150 days' (likely referring to a duration related to cropland), and specific internal classification codes (e.g., 65526-65534) to unique RGB colour values. Class 0, 'No annual cropland,' is rendered in light grey (RGB 240, 240, 240), while Class 65535, 'Outside area,' is black (RGB 0, 0, 0). Ranges '11-74 days' and '76-149 days' are indicated to use 'Colour shades in between' without specifying fixed RGB values.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image15.png)

Table 0-9: Colour palette and attributes of CPBSB layer

![This table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) Croplands Best Single Bounding Box with Confidence Level (CPBSBCL) layer. It lists Class Codes, their corresponding Class Names, and the Red, Green, and Blue (RGB) colour components for visual representation. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|:---\|:---\|:---:\|:---:\|:---:\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 1 \| 1 \| 202 \| 0 \| 32 \| \| 2-29 \| 2-29 days uncertainty \| Colour shades in between \| Colour shades in between \| Colour shades in between \| \| 30 \| 30 days uncertainty \| 247 \| 245 \| 243 \| \| 31-59 \| 31-59 days uncertainty \| Colour shades in between \| Colour shades in between \| Colour shades in between \| \| 60 \| \> 60 days uncertainty \| 5 \| 113 \| 176 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| The table maps specific class codes and ranges of uncertainty, measured in days, to distinct RGB colour values or a range of colour shades. For example, 'No annual cropland' is assigned an RGB value of (240, 240, 240), representing a light grey, while '\> 60 days uncertainty' is assigned (5, 113, 176), representing a medium blue. Class codes 1 and 65526 have identical class names and corresponding RGB values, with class 1 being red (202, 0, 32) and class 65526 being light grey (225, 225, 225).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image16.png)

![This table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) CPMCHCL (Cropland Monitoring High Coverage Change Layer) product. It lists seven distinct data values, their corresponding Red (R), Green (G), and Blue (B) colour components, and a descriptive label for one value. \| Value \| Description \| Value (repeated) \| R \| G \| B \| \|-------\|-------------\|------------------\|---\|---\|---\| \| 65527 \| \| 65527 \| 200 \| 200 \| 200 \| \| 65529 \| \| 65529 \| 150 \| 150 \| 150 \| \| 65531 \| \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| \| 65533 \| 126 \| 52 \| 107 \| \| 65534 \| \| 65534 \| 179 \| 48 \| 179 \| \| 65535 \| Outside area\| \| 0 \| 0 \| 0 \| The colours represented by the RGB values are: light grey for value 65527, medium grey for 65529, dark grey for 65531, very dark grey for 65532, purple for 65533, magenta for 65534, and black for value 65535. Value 65535 is explicitly labelled 'Outside area', and its 'Value (repeated)' column is empty, while for all other entries, the 'Value (repeated)' column matches the 'Value' column.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image17.png)

Table 0-10: Colour palette and attributes of CPBSBCL layer

![This table defines the colour palette and attributes for a Copernicus Land Monitoring Service (CLMS) cropland layer, mapping Class Codes to Class Names and their corresponding Red, Green, and Blue (RGB) colour component values. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|:-----------\|:---------------------\|:----\|:------\|:-----\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 10 \| 10 days \| 214 \| 44 \| 58 \| \| 11-74 \| 11-74 days \| Colour shades in between \| \| 75 \| 75 days \| 247 \| 247 \| 247 \| \| 76-149 \| 76-149 days \| Colour shades in between \| \| 150 \| \>150 days \| 5 \| 113 \| 176 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65529 \| 65529 \| 150 \| 150 \| 150 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| \| 65534 \| 65534 \| 179 \| 48 \| 179 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The table defines colours for cropland classes based on duration in days, ranging from 'No annual cropland' (code 0, light grey) to '\>150 days' (code 150, dark blue), with intermediate ranges (11-74 days and 76-149 days) indicating colour gradients. Class codes 65526 through 65534 are defined with their own code as the class name, coloured in shades of grey (65526-65532) and specific purple/magenta tones (65533, 65534). Class 65535, labelled 'Outside area', is assigned black (RGB 0,0,0). This table is likely part of a Product User Manual (PUM) for a CLMS Cropland product.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image18.png)

Table 0-11: Colour palette and attributes of CPBSA layer

![\| Class Code \| Class Name \| Red \| Green \| Blue \| \|------------\|--------------------\|-----\|-------\|------\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| This table defines the colour palette and attributes for Class Code 0, named 'No annual cropland'. The class is assigned an RGB colour value of Red: 240, Green: 240, and Blue: 240, which corresponds to a light grey colour. This specific table relates to the colour palette and attributes of the Copernicus Land Monitoring Service (CLMS) CPBSBCL layer, which represents the Annual Cropland Base Seed Layer with Cropland Classification.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image19.png)

![This table defines the colour palette and attributes for the CPBSBCL (Cropland Bare Soil Bioclimatic Classification Layer). It maps pixel values or ranges to specific colour representations using RGB component values. \| Pixel Value / Range \| Description \| R \| G \| B \| Colour Representation \| \| :------------------ \| :--------------------- \| :-- \| :-- \| :-- \| :-------------------- \| \| 1 \| \| 202 \| 0 \| 32 \| Red \| \| 2-29 \| 2-29 days uncertainty \| \| \| \| Colour shades in between \| \| 30 \| 30 days uncertainty \| 247 \| 245 \| 243 \| Very Light Grey \| \| 31-59 \| 31-59 days uncertainty \| \| \| \| Colour shades in between \| \| 60 \| \>60 days uncertainty \| 5 \| 113 \| 176 \| Dark Blue \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| Light Grey \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| Medium Grey \| \| 65529 \| 65529 \| 150 \| 150 \| 150 \| Dark Grey \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| Very Dark Grey \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| Darkest Grey \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| Purple \| \| 65534 \| 65534 \| 179 \| 48 \| 179 \| Magenta \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| Black \| The table displays distinct RGB values for specific pixel codes (1, 30, 60, 65526-65535) and indicates 'Colour shades in between' for ranges of uncertainty days (2-29 and 31-59). Pixel code 1 is represented in Red, 30 in Very Light Grey, and 60 in Dark Blue, corresponding to various levels of uncertainty. Specific codes from 65526 to 65532 are assigned to a gradient of grey colours, while 65533 and 65534 are assigned Purple and Magenta, respectively. Pixel code 65535, indicating 'Outside area,' is represented in Black.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image20.png)

Table 0-12: Colour palette and attributes of CPBSBCL layer

![The table defines the colour palette and RGB (Red, Green, Blue) attributes for different cropland classes within a Copernicus Land Monitoring Service (CLMS) CPSCE layer. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|:-----------\|:--------------------\|:----\|:------\|:-----\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 1 \| Short summer CC \| 254 \| 203 \| 91 \| \| 2 \| Long summer CC \| 255 \| 198 \| 1 \| \| 3 \| Short winter CC \| 99 \| 229 \| 59 \| \| 4 \| Long winter CC \| 16 \| 100 \| 0 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65530 \| 65530 \| 125 \| 125 \| 125 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| \| 65534 \| 65534 \| 179 \| 48 \| 179 \| Note: 'CC' stands for 'Cover Crop'. The table assigns specific RGB values for visualisation, ranging from light grey (No annual cropland) to dark green (Long winter Cover Crop) and various shades of yellow, green, grey, purple. Classes 65526 through 65534 repeat the class code in the Class Name column.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image21.png)

![The table displays a single row from a colour palette and attributes table, likely associated with a Copernicus Land Monitoring Service (CLMS) Croplands layer. \| Pixel Value \| Attribute \| R \| G \| B \| Colour Sample \| \|---\|---\|---\|---\|---\|---\| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| black \| This row indicates that pixels with a Digital Number (DN) value of 65535 are classified as 'Outside area' and are represented by an RGB colour of (0, 0, 0), which corresponds to black.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image22.png)

Table 0-13: Colour palette and attributes of CPSCT layer

![The table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) 'CPSCE' layer, providing a mapping between numerical Class Codes, descriptive Class Names (months of a product year), and their corresponding Red, Green, and Blue (RGB) colour components. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|:-----------\|:--------------------\|----:\|------:\|-----:\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 16366 \| Jan (product year) \| 159 \| 127 \| 255 \| \| 17031 \| Feb (product year) \| 221 \| 127 \| 255 \| \| 17059 \| Mar (product year) \| 255 \| 127 \| 223 \| \| 17090 \| Apr (product year) \| 255 \| 127 \| 161 \| \| 17120 \| May (product year) \| 255 \| 176 \| 127 \| \| 17151 \| Jun (product year) \| 255 \| 223 \| 128 \| \| 17181 \| Jul (product year) \| 223 \| 255 \| 128 \| \| 17212 \| Aug (product year) \| 159 \| 255 \| 128 \| \| 17243 \| Sep (product year) \| 109 \| 220 \| 141 \| \| 17273 \| Oct (product year) \| 128 \| 255 \| 223 \| \| 17304 \| Nov (product year) \| 128 \| 223 \| 255 \| The table lists 12 distinct classes, including a 'No annual cropland' class (Class Code 0) assigned a light grey colour (RGB 240, 240, 240). The remaining 11 classes represent months from January to November within a 'product year', each assigned a unique colour to facilitate visual interpretation, ranging from purple for January to light blue for November.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image23.png)

![This table presents the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) CPBSBCL layer, showing the mapping between numeric values, their descriptions, and corresponding RGB colour codes. \| Value \| Description \| R \| G \| B \| \|---\|---\|---\|---\|---\| \| 17334 \| Dec (product year) \| 127 \| 189 \| 255 \| \| 65526 \| 65526 \| 222 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65530 \| 65530 \| 125 \| 125 \| 125 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The table details eight distinct entries. Value 17334 is described as 'Dec (product year)' and is assigned a light blue colour (RGB 127, 189, 255). Values 65526, 65527, 65530, 65531, and 65532 are assigned progressively darker shades of grey, ranging from very light grey (RGB 222, 225, 225) for 65526 to very dark grey (RGB 75, 75, 75) for 65532. Value 65533 is given a purple/burgundy colour (RGB 126, 52, 107). The final entry, 65535, represents 'Outside area' and is coloured black (RGB 0, 0, 0).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image24.png)

Table 0-14: Colour palette and attributes of CPSCE layer

![This table defines the colour palette and attributes for a Copernicus Land Monitoring Service (CLMS) Cropland layer, classifying land based on crop duration or status. It lists Class Codes, their corresponding Class Names indicating duration in days or status, and the Red, Green, and Blue (RGB) colour components, along with a visual colour swatch. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|:-----------\|:----------------------\|:---------------------\|:-----------------------\|:-----------------------\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 40 \| 40 days \| 215 \| 25 \| 28 \| \| 41-149 \| 41-149 days \| Colour shades in between \| Colour shades in between \| Colour shades in between \| \| 150 \| 150 days \| 247 \| 252 \| 189 \| \| 151-199 \| 151-200 days \| Colour shades in between \| Colour shades in between \| Colour shades in between \| \| 200 \| 200 days \| 165 \| 217 \| 165 \| \| 201-249 \| 201-249 days \| Colour shades in between \| Colour shades in between \| Colour shades in between \| \| 250 \| \>250 days \| 43 \| 131 \| 186 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65530 \| 65530 \| 125 \| 125 \| 125 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| The table defines specific RGB values for 'No annual cropland' (light grey, RGB 240,240,240), '40 days' (red, RGB 215,25,28), '150 days' (light yellow, RGB 247,252,189), '200 days' (light green, RGB 165,217,165), and '\>250 days' (blue, RGB 43,131,186). For intermediate duration ranges (41-149 days, 151-199 days, 201-249 days), the table specifies 'Colour shades in between' for the RGB values, indicating a gradient. Class Codes 65526 to 65531 are assigned various shades of grey, ranging from very light grey (65526, RGB 225,225,225) to dark grey (65531, RGB 100,100,100), likely representing auxiliary data categories such as masked areas or no data.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image25.png)

![This table provides the colour palette and attributes for the Copernicus Cropland Single Crop Dominance (CPSCD) layer. It lists pixel values, their corresponding descriptions, RGB colour components, and a visual colour swatch. \| Pixel Value \| Description \| R \| G \| B \| \| :---------- \| :----------- \| :-- \| :-- \| :-- \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| 65533 \| 126 \| 52 \| 107 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The table defines three entries: pixel value 65532 is represented by RGB (75, 75, 75) which is a dark grey; pixel value 65533 is represented by RGB (126, 52, 107) which is a purple colour; and pixel value 65535, described as 'Outside area', is represented by RGB (0, 0, 0) which is black.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image26.png)

Table 0-15: Colour palette and attributes of CPSCD layer

![\| Class Code \| Class Name \| Red \| Green \| Blue \| \|---\|---\|---\|---\|---\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 1 \| \| 202 \| 0 \| 32 \| \| 2-29 \| 2-29 days uncertainty \| Colour shades in between \| Colour shades in between \| Colour shades in between \| \| 30 \| 30 days uncertainty \| 247 \| 245 \| 243 \| \| 31-59 \| 31-59 days uncertainty \| Colour shades in between \| Colour shades in between \| Colour shades in between \| \| 60 \| \>60 days uncertainty \| 5 \| 113 \| 176 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| The table defines the colour palette and attributes for the Copernicus Cropland Season Classification and Dynamics Classification Layer (CPSCDCL), mapping class codes to land cover categories, uncertainty levels, and their corresponding RGB colour values. Class Code 0 represents 'No annual cropland' (RGB: 240, 240, 240), Class Code 1 has a blank name and is assigned a red colour (RGB: 202, 0, 32), and Class Code 60 indicates '\>60 days uncertainty' in blue (RGB: 5, 113, 176). Intermediate uncertainty ranges (2-29 days and 31-59 days) are described as having 'Colour shades in between' the defined values.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image27.png)

![\| Pixel Value \| Attribute Description \| Red \| Green \| Blue \| \|---\|---\|---\|---\|---\| \| 65530 \| (no description visible) \| 125 \| 125 \| 125 \| \| 65531 \| (no description visible) \| 100 \| 100 \| 100 \| \| 65532 \| (no description visible) \| 75 \| 75 \| 75 \| \| 65533 \| (no description visible) \| 126 \| 52 \| 107 \| \| 65534 \| (no description visible) \| 179 \| 48 \| 179 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| This table defines a colour palette and attributes for a Copernicus Land Monitoring Service (CLMS) Croplands product layer, likely related to CPBSBCL, CPBSA, CPSCT, CPSCE, CPSCD, CPFLP, or CPFLPCL, based on the surrounding context. It assigns specific RGB colour values to distinct pixel values. Pixel values 65530, 65531, and 65532 are represented by progressively darker shades of grey. Pixel value 65533 is defined as purple (RGB 126, 52, 107), and 65534 as magenta (RGB 179, 48, 179). The pixel value 65535 is explicitly labelled 'Outside area' and is assigned black (RGB 0,0,0).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image28.png)

Table 0-16: Colour palette and attributes of CPSCDCL layer

![This table defines the colour palette and attributes for the Copernicus Fallow Land Dynamics (CPFLD) layer, mapping class codes to land cover types and their corresponding RGB colour values. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|:-----------\|:----------------\|:----\|:------\|:-----\| \| 0 \| No fallow land \| 240 \| 240 \| 240 \| \| 1 \| Fallow \| 206 \| 139 \| 39 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The table shows that 'No fallow land' is represented by RGB (240, 240, 240), 'Fallow' land by RGB (206, 139, 39), and 'Outside area' by RGB (0, 0, 0).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image29.png)

Table 0-17: Colour palette and attributes of CPFLP layer

![The table specifies the colour palette and attributes for the Fallow Land Detection Confidence Level (CPFLDCL) layer, detailing the mapping from Class Code to Class Name, associated RGB values, and a visual colour representation. \| Class Code \| Class Name \| Red \| Green \| Blue \| \| :--------- \| :------------------ \| :-- \| :---- \| :--- \| \| 0 \| 0% confidence \| 202 \| 0 \| 32 \| \| 1-49 \| 1-49% confidence \| Colour shades in between \| \| 50 \| 50% confidence \| 247 \| 247 \| 247 \| \| 51-99 \| 51-99% confidence \| Colour shades in between \| \| 100 \| 100% confidence \| 5 \| 113 \| 176 \| \| 253 \| No fallow land \| 240 \| 240 \| 240 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The colour palette uses a gradient for confidence levels: 0% confidence is represented by RGB (202, 0, 32), which is red; 50% confidence by RGB (247, 247, 247), which is a light grey; and 100% confidence by RGB (5, 113, 176), which is blue. Intermediate confidence ranges (1-49% and 51-99%) correspond to colour shades interpolated between these key values. Specific codes are assigned for 'No fallow land' (Class Code 253, RGB 240, 240, 240, a very light grey) and 'Outside area' (Class Code 65535, RGB 0, 0, 0, black).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image30.png)

Table 0-18: Colour palette and attributes of CPFLPCL layer

![\| Class Code \| Class Name \| Red \| Green \| Blue \| \|---\|---\|---\|---\|---\| \| 0 \| No fallow land \| 240 \| 240 \| 240 \| \| 40 \| 40 days \| 215 \| 25 \| 28 \| \| 41-948 \| 41-948 days \| Colour shades in between \| \| \| This table defines the colour palette for the Copernicus Cropland Fallow Land Duration (CPFLD) layer, mapping specific fallow land duration classes to RGB colour values. Class 0, representing 'No fallow land', is assigned light grey (RGB 240, 240, 240). Class 40, representing '40 days' of fallow land, is assigned a bright red colour (RGB 215, 25, 28). For the range of '41-948 days' of fallow land, the table indicates a gradient of colour shades would be used in between the specified colours.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image31.png)

![The table displays the colour palette and corresponding attributes for a CPFLD (Copernicus Cropland Field Delineation) layer, mapping specific numerical values to colour representations. \| Value \| Description \| Red (R) \| Green (G) \| Blue (B) \| Colour \| \|---\|---\|---\|---\|---\|---\| \| 949 \| 949 days \| 248 \| 252 \| 185 \| (light yellow) \| \| 950-1825 \| 950-1825 days \| - \| - \| - \| Colour shades in between \| \| 1826 \| 1826 days \| 26 \| 150 \| 65 \| (dark green) \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| (black) \| This table defines specific integer values, descriptive text, and their associated Red, Green, Blue (RGB) colour components for visual representation. Values up to 949 days are mapped to a light yellow colour (RGB: 248, 252, 185), while 1826 days are mapped to a dark green (RGB: 26, 150, 65). The range 950-1825 days is represented by transitional colour shades between these two specific values. The value 65535 represents 'Outside area' and is mapped to black (RGB: 0, 0, 0).](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image32.png)

Table 0-19: Colour palette and attributes of CPFLD layer

![This table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) Cropland Fallow Land Dynamics and Crop Type Layer (CPFLDCL), as specified in a Product User Manual for 2017-present data. \| Class Code \| Class Name \| Red \| Green \| Blue \| \| :--------- \| :--------------------- \| --: \| ----: \| ---: \| \| 0 \| No fallow land \| 240 \| 240 \| 240 \| \| 1 \| 1 day uncertainty \| 202 \| 0 \| 32 \| \| 1-19 \| 1-19 days uncertainty \| \_ \| \_ \| \_ \| \| 20 \| 20 days uncertainty \| 247 \| 243 \| 241 \| \| 21-39 \| 21-39 days uncertainty \| \_ \| \_ \| \_ \| \| 40 \| \>40 days uncertainty \| 5 \| 113 \| 176 \| \| 65534 \| 65534 \| 179 \| 48 \| 179 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| For class codes '1-19' and '21-39', the RGB values are described as 'Colour shades in between' other defined values. The table maps levels of uncertainty in days for fallow land, ranging from 'No fallow land' (light grey, RGB 240,240,240) to '\>40 days uncertainty' (dark blue, RGB 5,113,176). '1 day uncertainty' is specifically assigned a bright red colour (RGB 202,0,32). Additionally, special codes 65534 (purple, RGB 179,48,179) and 65535 ('Outside area', black, RGB 0,0,0) are defined.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image33.png)

Table 0-20: Colour palette and attributes of CPFLDCL layer

![This table defines the colour palette and attributes for a Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Croplands product, specifically for a layer identified in the context as 'CPFLD'. It lists \`Class Code\`, \`Class Name\`, and the \`Red\`, \`Green\`, and \`Blue\` (RGB) colour components for each class, along with a visual colour swatch. \| Class Code \| Class Name \| Red \| Green \| Blue \| \|:-----------\|:-------------------\|:----\|:------\|:-----\| \| 0 \| No annual cropland \| 240 \| 240 \| 240 \| \| 1 \| 1 growing season \| 231 \| 157 \| 29 \| \| 2 \| 2 growing seasons \| 138 \| 233 \| 55 \| \| 65526 \| 65526 \| 225 \| 225 \| 225 \| \| 65527 \| 65527 \| 200 \| 200 \| 200 \| \| 65531 \| 65531 \| 100 \| 100 \| 100 \| \| 65532 \| 65532 \| 75 \| 75 \| 75 \| \| 65533 \| \| 126 \| 52 \| 107 \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| The table details specific colour assignments for different cropland classifications, including codes for 'No annual cropland' (light grey), '1 growing season' (orange), and '2 growing seasons' (lime green). Other class codes (65526, 65527, 65531, 65532, 65533) are assigned various shades of grey and purple, with code 65535 representing 'Outside area' (black). For class codes 65526, 65527, 65531, and 65532, the class name column repeats the numeric class code itself, and for 65533, the class name column is empty.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image34.png)

Table 0-21: Colour palette and attributes of CPCSY layer

![This table defines the colour palette and attributes for the Copernicus Land Monitoring Service (CLMS) Cropland Field Delineation (CPFLD) layer. It maps specific class codes and names to Red, Green, and Blue (RGB) colour values. \| Class Code \| Class Name \| Red \| Green \| Blue \| Colour Swatch \| \|:-----------\|:----------------------------------\|:----\|:------\|:-----\|:--------------\| \| 0 \| No annual cropland (over 3-years period) \| 240 \| 240 \| 240 \| Light Grey \| \| 1 \| 1 annual crop type over three years period \| 231 \| 157 \| 29 \| Orange \| \| 2 \| 2 annual crop types over three years period \| 138 \| 233 \| 55 \| Light Green \| \| 3 \| 3 annual crop types over three years period \| 243 \| 58 \| 252 \| Magenta \| \| 65528 \| 65528 \| 175 \| 175 \| 175 \| Grey \| \| 65535 \| Outside area \| 0 \| 0 \| 0 \| Black \| The table details 6 distinct classes, including specific annual crop type counts over a three-year period, non-cropland, and special codes for unclassified areas (65528) and outside the area of interest (65535). Each class is assigned a unique RGB triplet and a visual colour representation.](High_Resolution_Layer_Croplands_2017-present_PUM_v2-media/image35.png)

Table 0-22: Colour palette and attributes of CPCST layer

# 13 Document Control Information:

| Document Title | D1.12 HRL Croplands - Product User Manual |
|----|----|
| Project Title | Copernicus Land Monitoring Service – High Resolution Layer - Vegetated Land Cover Characteristics |
| Document Author | André Stumpf, Stephanie Wegscheider, Christian Siegert, Elcin Acar (GAF AG), Bert De Roo, Kasper Bonte (VITO), Tanja Gasber (GeoVille), Loïc Faucqueur (CLS) |
| Project Owner | Luca Battistella (EEA) |
| Project Manager | Christian Siegert (GAF) |
| Document Code | D1.12 HRL CTY |
| Document Version | 2.3 |
| Distribution | Public |
| Date | 2025-11-03 |

# 14 Change Log

| Date       | Version | Summary         |
|------------|---------|-----------------|
| 2025-12-02 | 2.3.0   | Initial release |

Back to top

## Footnotes

## Reuse

EUPL (\>= 1.2)

[^1]: https://land.copernicus.eu/en/eagle?tab=technical_implementation

[^2]: https://land.copernicus.eu/en/technical-library/product-user-manual-clc-backbone-2021

[^3]: https://www.evo-land.eu/method/biomass-mapping/

[^4]: https://sentiwiki.copernicus.eu/\_\_attachments/1673423/OMPC.CS.DQR.001.08-2025-Sentinel-2-MSI-L1C-DQR-September-2025-115.pdf?inst-v=21d709d1-2d56-4cc7-aec1-05e4dd76e738

[^5]: S2-PDGS-MPC-DQR Issue: 66 Date: 02/08/2021
