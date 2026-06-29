# HRL TREE COVER & FORESTS - PRODUCT USER MANUAL

Copernicus Land Monitoring Service – High Resolution Layer – Tree Cover & Forests

This Product User Manual offers a comprehensive guide to the Copernicus Land Monitoring Service (CLMS) High-Resolution Layer (HRL) Tree Cover & Forests product suite, covering 2018 onwards. It details the product’s characteristics, including Tree Cover Density, Dominant Leaf Type, and Forest Type layers, alongside change products and confidence layers. The document outlines production methodologies, data formats, and the rigorous quality assessment procedures employed to ensure accuracy and consistency across Europe. Designed for scientists, regulators, and data engineers, this manual is essential for effective utilisation and understanding of these critical land monitoring datasets.

Published

November 3, 2025

Keywords

Product User Manual (PUM), HRL Tree Cover & Forests, Tree Cover Density (TCD), Dominant Leaf Type (DLT), Forest Type (FTY), Tree Cover Presence Change (TCPC), Thematic accuracy assessment, Copernicus Land Monitoring Service (CLMS), European Environment Agency (EEA), Sentinel-2 imagery, Quality assessment procedures, Land Use, Land Use Change and Forestry (LULUCF)

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

## 0.1 List of Figures

Figure 3-1 Evolution of HRL Forest and Grassland towards the three product groups HRL Tree Cover & Forests, HRL Grasslands, HRL Croplands. Figure 5-1: Products within the HRL vegetated land cover characteristics. Figure 5-2: High-level overview of the relationship between the Base Vegetation Layer and the subsequent production of Grasslands, Croplands and Tree Cover & Forests products………….. 12 Figure 6-1: Right: Tree Cover Presence Change documenting tree cover loss areas between 2018- 2021 in Harz mountains, Germany. Left side shows S2 scenes (top left: 2018, bottom left: 2021) with clearly visible clear cut sides (yellow circle) and dead trees (red circle), caused by drought and bark beetle infestation Figure 6-2: DLT time series showing the gradual decrease of coniferous tree cover from 2018 to 2021. Figure 7-1: LAEA tile layout including distinction between tiles to cover EU27 and EEA38. …… 17 Figure 7-2 HRL Tree Cover & Forests product portfolio Figure 8-1: Spatial distribution of 14.000 Primary Sampling Units. Figure 8-2: Secondary Sample Units used for 2018 and 2021 Tree Cover & Forests reference layers. Red dot: initial sample; white dot: secondary sample unit; green outline: area around the initial sample that is used to derived product statistics. Figure 8-3: HRL TCD 2018, 2021 and 2022 scatterplots and correlations at EU27 level Figure 8-4: HRL TCD 2018, 2021 and 2022 scatterplots and correlations at EEA38 level Figure 8-5: Illustration of typical broadleaved tree cover commissions errors in the DLT for an area Terceira island, Portugal. Shown are a) the DLT 2022 b) an overlay of the DLT 2022 on top of the VHR IMAGE 2021 and c) a zoom of the latter and the pixels with commission errors marked in yellow.

## 0.2 List of Tables

Table 7-1: Elements to be included/excluded in tree cover. Table 7-2: Download content, file naming convention and file format(s) for HRL Tree Cover & Forests layers Table 7-3: Projection and spatial coverage for HRL Tree Cover & Forests layers Table 7-4: Spatial resolution for HRL Tree Cover & Forests layers Table 7-5: Temporal information for HRL Tree Cover & Forests layers. Table 7-6: Characteristics of HRL Tree Cover & Forests layers.. Table 8-1: Layers to be verified and target accuracies Table 8-2: HRL TCD validation results at EU27 level Table 8-3: HRL TCD validation results at EEA38 Level Table 8-4: DLT validation results at EU27 level Table 8-5: DLT validation results at EEA38 Level Table 8-6: HRL Tree Cover & Forests Change layers validation results at EU27 Level Table 8-7: HRL Tree Cover & Forests Change layers validation results at EEA38 level Table 0-1: Colour palette and attributes of TCD 2018-2021 Table 0-2: Colour palette and attributes of DLT layer Table 0-3: Colour palette and attributes of FTY layer. Table 0-4: Colour palette and attributes of FADSL Table 0-5: Colour palette and attributes of DLTC layer Table 0-6: Colour palette and attributes of TCPC layer Table 0-7: Colour palette and attributes of BCD layer.. Table 0-8: Colour palette and attributes of CCD layer. Table 0-9: Colour palette and attributes of TCDCL Table 0-10: Colour palette and attributes of DLTCL Table 0-11: Colour palette and attributes of TCPCCL

„Picture Coverpage © K I Photography – stock.adobe.com“

------------------------------------------------------------------------

**Document Control Information:**

Document Control Information

|  |  |
|----|----|
| **Document Title** | D1.12 HRL Tree Cover and Forests Product User Manual |
| **Project Title** | Copernicus Land Monitoring Service - High Resolution Layer - Vegetated Land Cover Characteristics |
| **Document Author** | André Stumpf, Stephanie Wegscheider, Christian Siegert, Elcin Acar (GAF AG), Bert De Roo, Kasper Bonte (VITO), Tanja Gasber (GeoVille), Loïc Faucqueur (CLS) |
| **Project Owner** | Luca Battistella (EEA) |
| **Project Manager** | Christian Siegert (GAF AG) |
| **Document Code** | D1.12 HRL TC&F |
| **Document Version** | 2.3 |
| **Distribution** | Public |
| **Date** | 2025-11-03 |

# 1 Executive summary

Copernicus is the European Union’s Earth Observation Programme. It offers information services based on satellite Earth observation and in situ (non-space) data. These information services are freely and openly accessible to its users through six thematic Copernicus services (Atmosphere Monitoring, Marine Environment Monitoring, Land Monitoring, Climate Change, Emergency Management and Security).

The **Copernicus Land Monitoring Service (CLMS)** provides geographical information on land cover and its changes, land use, vegetation state, water cycle and earth surface energy variables to a broad range of users in Europe and across the world in the field of environmental terrestrial applications.

CLMS is jointly implemented by the **European Environment Agency (EEA)** and the European Commission’s **DG Joint Research Centre (JRC)**.

The **High Resolution Layer (HRL)** vegetated land cover characteristics are a set of harmonised yearly maps dedicated to the thematic themes **Tree Cover & Forests, Grasslands and Croplands**. These include a rich suite of raster products mapping the yearly status of those land cover types at a spatial resolution of 10 metres and change layers at 3-yearly interval and 20-metre resolution. HRL vegetated land cover characteristics extends the time-series of the existing HRL’s Tree Cover & Forests and Grasslands and complements the CLMS portfolio with new layer dedicated to the mapping of crop types and agricultural practices such as mowing, harvest and cover crops.

# 2 Background of the document

## 2.1 Scope

This Product User Manual is the primary document that users are recommended to read before using the product. It provides a description of the product characteristics, production methodologies and workflows, and information about the product quality of the annual provision of **HRL Tree Cover & Forests**. Furthermore, it gives information on the terms of use and product technical support. More detailed information on the methodologies and processing workflows that were used to produce the products can be found in the Algorithm Theoretical Baseline Document (ATBD) \[7\].

## 2.2 Content and structure

In more detail, the document is structured as follows:

- Chapter 3 provides an overview of the lineage of the products in relation to previous HRL productions;
- Chapter 4 contains a review of user requirements;
- Chapter 5 provides on overview of what is included in the High Resolution Layers Vegetated Land Cover Characteristics and how the comprised products relate to each other;
- Chapter 6 presents potential application areas and example use cases;
- Chapter 7 provides a description of the products including the nomenclature and class definitions, file naming, spatial resolution format(s), etc.;
- Chapter 8 summarizes the quality assessment, validation procedure and the results;
- Chapter 9 provides information about product access and use conditions as well as the technical support.

# 3 Lineage of HRL Tree Cover and Forests, Grasslands, and Croplands

**High Resolution Layers (HRL)** on **Tree Cover & Forests** had already been established in the **Copernicus Land Monitoring Service (CLMS)** portfolio since the reference years 2012 producing initially a **Dominant Leaf Type (DLT)**, a **Tree Cover Density (TCD)**, and a **Forest Type (FTY)** map at a spatial resolution of 20 metres (Figure 3-1). Change layers and reference datasets were included with the reference year 2015. At the same time the accuracy targets were raised towards at least 90% user’s and producer’s accuracy for the DLT and TCD status layers. A further important step followed with the first production for the reference years 2018 (further referred to as **Historic HRL Forest 2018**) where the spatial resolution of the status layers was raised to 10 metres, the implementation of the change layers was partially reconsidered and target accuracies of 90% user’s and producer’s accuracy for the change layers were defined. In addition, new aggregated layers depicting the density of coniferous and broadleaved tree cover were introduced. With the **HRL Tree Cover & Forests** starting from the reference year 2018 the product specifications have been kept largely in line with the definitions used for the Historic HRL Forest 2018 \[8\] whereas major changes concerned in particular the move to a yearly update cycle for the status layers and changes to some confidence layers (not shown in Figure 3-1). The new HRL Tree Cover & Forests therefore replace and extend the **Historic HRL Forest 2018**. This does not include an update of the change layer 2015 – 2018; the new status layers for 2018 are therefore not consistent with the original change layers 2015 – 2018.

HRL’s on **Grasslands** had already been established in the Copernicus Land Monitoring Service (CLMS) portfolio since the reference years 2015 initially producing a status layer on the absence / presence of grassland (Figure 3-1) with a target Overall Accuracy of 85%. With the reference year 2018, the spatial resolution of the status layers was increased to 10 metres and a change layer with a target Overall Accuracy of 80% was introduced. With the **HRL Grasslands** starting from the reference year 2017, the product specifications have been largely maintained to ensure consistency with the definitions used for the **Historic HRL Grassland 2018** \[9\]. In particular, the **HRL Grassland (GRA)** layer has been transitioned to an annual update cycle for the status layers, complemented by an additional yearly **Herbaceous Cover** layer that also includes temporary grassland in the reference year. A further methodological enhancement concerns the removal of the **Minimum Mapping Unit (MMU)** from both the **PLOUGH** and **GRA** layer starting from 2022. This adjustment was introduced to improve the current consistency between the **GRA, HER**, and **PLOUGH** layers and to eliminate artificial gains and losses resulting from MMU-induced filtering. While this change enhances the internal coherence and spatial detail of the current HRL **Grassland** layers, it may lead to minor differences when compared to **historic layers** (years before 2022) where MMU thresholds were still applied. Consequently, users should be aware that actual small-area grassland changes may be partly mixed with technical changes resulting from the removal of the MMU. New layers on the count and timing of Grassland Mowing (Minimum Mapping Unit of 0.25 ha) and changes to some confidence layers (not shown in detail in Figure 3-1) are introduced. The new **HRL Grasslands** therefore replaces and extends the **Historic HRL Grassland 2018**. This does not include an update of the change layer 2015 – 2018; the new status layers for 2018 are therefore not consistent with the original change layers 2015 – 2018.

The **HRL Croplands** is a new set of layers dedicated to agriculture and comprises several yearly layers mapping crop types (10-metre spatial resolution) and agricultural practices such as harvest, fallow land and secondary crops (10-metre spatial resolution, Minimum Mapping Unit of 0.25 ha).

HRL Forest

[TABLE]

[TABLE]

↓

From 2018 onward replaced by  
yearly updates of HRL Tree Cover & Forests

HRL Grassland

[TABLE]

[TABLE]

↓

From 2017 onward replaced by  
yearly updates of HRL Grasslands

↓

From 2017 onward yearly updates of HRL Croplands

Figure 3-1 Evolution of HRL Forest and Grassland towards the three product groups HRL Tree Cover & Forests, HRL Grasslands, HRL Croplands.

# 4 Review of User Requirements

In the frame of the Horizon 2020 (H2020) project ECoLaSS a survey \[5\] of key stakeholders has been performed in order to evaluate the user requirements towards the evolution of existing and future **Copernicus** products. This survey made also use of the results from the Nextspace User Study \[6\] and revealed that HRL users like European institutions, service industry, research and academia, national agencies, regional administrations, NGOs or private users would in general appreciate:

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
- IPCC -compliant land-use categories..

While many of these requirements had already been satisfied with previous HRL reference years some could only be implemented within the current update:

- A long-standing thematic gap in the European CLMS portfolio concerning the monitoring of agriculture has been addressed though new products on crop types and agricultural activities. This also improves the separation between grassland and cropland and the IPCC conformity;
- Yearly update cycle for status layer;
- Grassland use intensity (or the dynamics of intensification/ extensification) is partially addressed through a new product on Grassland mowing.

Further requirements that remain to be considered for future updates are for example:

- More fine-grained differentiation among species-rich (extensively used) and separation from species-poor (intensively used) and managed grassland;
- Tree-species compositions and shifts between extensive and intensive management;
- Increased timeliness of availability of the products: The mid-term goal is a product provision at latest 12 months after the end of the reference year.

# 5 Product structure - What are the High Resolution Layers?

The **High Resolution Layers (HRL)** vegetated land cover characteristics portfolio consists of **Tree Cover & Forests, Grasslands and Croplands** products (Figure 5-1), which together cover most of what is defined as the Biotic component of the EAGLE Land Cover Components[^1]. More specifically, the mapping is focused on surfaces with a vegetation cover above 30%; an exception to this is tree cover where the objective is to map tree cover with a continuous range of 1-100% **Tree Cover Density (TCD)**, i.e. also below 30%, as far as detectable from 10-metre resolution satellite imagery. This definition is also in line with the Sparsely Vegetated class in the **CLC+ Backbone Raster**[^2] and considers that detection / classification of vegetation below this threshold is typically more error-prone. The definition also aims at largely avoiding overlaps with the non-vegetated land cover characteristics such as **HRL Imperviousness**, which is focused on areas with less than 10% vegetation cover during any time of the year, for a reference period of 3 year.

Some overlaps between the three product groups are allowed by definition, for example areas with tree crops (i.e. olive, fruit and nut trees) which are included in both the Tree Cover & Forests and the Croplands products. Furthermore, specific vegetations types are not included in the HRL-

VLCC portfolio; this concerns areas dominated by natural shrubs (i.e. shrubs that are not under agricultural use) and associations of lichens and mosses.

![This diagram illustrates the structure of Copernicus Land Monitoring Service (CLMS) High Resolution Layers (HRL) products focusing on vegetated land cover characteristics. The top-level category is 'High Resoluton Layers' (a typo for High Resolution Layers) covering 'vegetated land cover characteristics'. This category is divided into three distinct product types: 1. 'Tree Cover & Forest Products', which are updated 'yearly since 2018'. 2. 'Grasslands Products', which are updated 'yearly since 2017'. 3. 'Cropland Products', which are updated 'yearly since 2017'. This diagram shows the availability and update frequency of these key CLMS HRL products.](products_Product_User_Manual_-_Tree_Cover_and_Forests_2018-present-media/img-5eed06584a29d03210da45a3a94cef02.png)

Figure 5-1: Products within the HRL vegetated land cover characteristics.

Given several interdependencies and potential overlaps among the **Grasslands, Croplands and Tree Cover & Forests** products, the overall workflow starts with the classification of **Base Vegetation Layer (BVL)**. A high-level description is provided for the overall workflow in Figure 5-2. The yearly BVL classification initially targets the separation of five basic land cover classes being:

1.  herbaceous vegetation;
2.  cropland;
3.  tree cover;
4.  tree crops (i.e. nomenclature overlap between broadleaved tree cover and permanent crops in the Croplands product);
5.  background class (including bare and sparsely vegetated areas and non-agricultural shrubs);

In a subsequent post-processing step two further classes are derived to delineate the:

6.  potential overlap herbaceous – cropland (i.e. pixels which are classified as cropland and herbaceous at least once in the time-series);
7.  The second derived class is derived from the intersection of all areas classified as tree cover and a preliminary version of the Tree Cover Density to delineate areas with low Tree Cover Density and hence allowed overlaps of herbaceous and tree cover.

The derived yearly BVL is considered for the downstream productions of Grasslands, Croplands and Tree Cover & Forests products as follows:

- For the production of the Grasslands layers: all areas classified as *herbaceous, overlap herbaceous – tree cover,* or *overlap herbaceous – Cropland* are considered as the potential maximum extent for the **Herbaceous Cover (HER)** layer. In addition, the BVL classification probabilities for the herbaceous class are used as the main input for the derivation of the **HER** layer.
- For the Croplands layers: the areas delineated as *cropland, overlap herbaceous – cropland,* or *Tree Crops* are considered as the maximum extent for the CTY classification and further refinement.
- For the **Tree Cover & Forests** layers: the areas classified as *tree cover, overlap herbaceous - tree cover, tree crops* and the respective probabilities are used directly to derive the respective change layers and yearly **DLT** and **TCD** status layers.

Within the areas identified as *overlap herbaceous - cropland*, a further harmonization step is carried out downstream. To this end the **CTY** classification initially includes a class for fodder crops which are transferred to the **HER** layer if occurring in the designated overlap class.

![This is a workflow diagram outlining the processing for the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) vegetated land cover characteristics. The process begins with the 'Base Vegetation Layer Service,' which classifies initial land cover into 'Herbaceous,' 'Cropland,' and 'Tree Cover.' Within this service, specific overlap areas are identified: 'Overlap Herbaceous – Tree Cover (Tree Cover Density (TCD) 1-10%),' 'Overlap Herbaceous-Cropland (e.g. Fodder crops),' and 'Overlap Tree Cover-Cropland (Tree crops).' From the 'Base Vegetation Layer Service,' data is distributed: 1. 'Herbaceous' areas, considering 'Max. extent & probabilities,' are processed by 'Grassland Product Services.' 2. 'Cropland' areas, considering 'Max. extent,' are processed by 'Cropland Product Services.' 3. 'Tree Cover' areas, considering 'Max. extent & probabilities,' are processed by 'Forest Product Services.' A feedback loop exists where 'Fodder crops' data from 'Cropland Product Services' is fed into 'Grassland Product Services.' The final outputs from each product service are: - \*\*Grassland Product Services\*\* generate products such as 'Herbaceous Cover (10m),' 'Grassland (10m, 100m),' 'Grassland Change (20m, Minimum Mapping Unit (MMU) 1ha),' and 'Grassland Mowing Events (10m, MMU 0.25ha).' - \*\*Cropland Product Services\*\* generate products such as 'Crop Types (10m, MMU 0.25 ha),' 'Cropping patterns (10m, MMU 0.25 ha),' 'Main Crops, Bare Soil, Secondary Crops,' 'Fallow Land,' and 'Annual Crop Characteristics.' - \*\*Forest Product Services\*\* generate products such as 'Dominant Leaf Type (10m),' 'Tree Cover Density (10m, 100m),' 'Forest Type (10m, 100m),' and 'Forest Change (20m, MMU 1ha).'](products_Product_User_Manual_-_Tree_Cover_and_Forests_2018-present-media/img-0f4778c79e1edff8abc04229a8f348b7.png)

Figure 5-2: High-level overview of the relationship between the Base Vegetation Layer and the subsequent production of Grasslands, Croplands and Tree Cover & Forests products

# 6 Product application areas and examples of use cases

The **HRL Tree Cover & Forests, Grasslands and Croplands** set of products is designed for use by a broad user community as basis for environmental and regional analysis and for supporting political decision-making, such as the **Common Agricultural Policy (CAP)**, **LULUCF (Land Use, Land Use Change and Forestry)** regulation, the **Nature Restoration Regulation (NRR)**, or the proposed **European Forest Monitoring Law (FML)**. Notably, the NRR (Regulation (EU) 2024/1991) explicitly refers to the Tree Cover Density dataset as the basis for determining urban tree canopy cover, thereby establishing a direct legal reference to the HRL framework within EU legislation. With the new products the EEA will ensure continuity and further densification of the well-established HRL Tree Cover & Forests and Grasslands product time series. Those include a rich suite of raster products at a 3-yearly interval mapping the status of those land cover types with a spatial resolution of 10-metre and change layers at 20-metre spatial resolution.

As an example, the following sections provide short information on (potential) use cases at national level, for which the **Copernicus HRL Tree Cover & Forests** product represent a fundamental input.

## 6.1 Use Case: Monitoring of Tree Cover Change and Dominant Leaf Type

The **Tree Cover Presence Change (TCPC)** layer documents losses of tree cover between 2018 and 2021 which can serve as a reliable information source for forest authorities. The example shown in Figure 6-1 is also confirmed by the **Dominant Leaf Type (DLT)** layer pictured in Figure 6-2.

![The image displays a comparison of optical satellite imagery with a derived classified map illustrating tree cover changes over time. It consists of three panels: The top-left panel shows an earlier temporal snapshot of the landscape, characterised by dense tree cover, a central, elongated water body (likely a reservoir or river), and a network of tracks or unpaved roads. The bottom-left panel shows a later temporal snapshot of the same landscape. A red circle highlights an area where previous dense tree cover has visibly been removed or significantly thinned. A yellow circle highlights another area which appears to show some regrowth or new vegetation cover compared to the top image. The right-hand panel presents a classified map of tree cover change, derived from the comparison of the two satellite images. The legend defines four classes: \* White (class 0): unchanged no tree cover \* Green (class 1): new tree cover (a small green square is visible in the legend, but no discernible green pixels appear on the map within this displayed area) \* Red (class 2): loss of tree cover \* Grey (class 10): unchanged tree cover The classified map clearly delineates significant areas of tree cover loss (red), aligning with the area highlighted by the red circle in the bottom-left satellite image. Extensive areas of unchanged tree cover are depicted in grey, and unchanged non-tree covered areas (including the water body and some open land) are shown in white. All three panels share a common scale bar, ranging from 0 m to 2000 m, with increments at 400 m, 800 m, 1200 m, 1600 m, and 2000 m. This visual demonstrates the process of deriving Tree Cover & Forests layers as part of Copernicus Land Monitoring Service (CLMS) products, by analyzing changes in basic vegetation layers (BVL).](products_Product_User_Manual_-_Tree_Cover_and_Forests_2018-present-media/img-b6cee66e1f97a8f74fee6b06fd496b1a.png)

Figure 6-1: Right: Tree Cover Presence Change documenting tree cover loss areas between 2018-2021 in Harz mountains, Germany. Left side shows S2 scenes (top left: 2018, bottom left: 2021) with clearly visible clear cut sides (yellow circle) and dead trees (red circle), caused by drought and bark beetle infestation

![These four choropleth maps display annual tree cover classifications for an undisclosed geographic region, likely a forested area with a central water body, over the period 2018 to 2021. Each map panel is labelled with its respective year: 2018 (top-left), 2019 (top-right), 2020 (bottom-left), and 2021 (bottom-right). The legend, consistent across all maps, uses three colour classes: \* White: 0: no tree cover \* Light green: 1: Broadleaved trees \* Dark green: 2: Coniferous trees A prominent white area, representing 'no tree cover' or a water body, runs through the lower-central portion of all maps. From 2018 to 2020, the spatial distribution of broadleaved and coniferous trees remains relatively stable. However, the 2021 map shows a substantial increase in 'no tree cover' areas (white) across the landscape, particularly in the upper and right sections, indicating a significant reduction in overall tree cover compared to the preceding years. This change suggests extensive land cover modification, such as deforestation or other disturbances, occurred by 2021.](products_Product_User_Manual_-_Tree_Cover_and_Forests_2018-present-media/img-c4134578fe123095b3b93fc0761ceac5.png)

Figure 6-2: DLT time series showing the gradual decrease of coniferous tree cover from 2018 to 2021

## 6.2 Use case: Land cover specific monitoring

Detailed and dynamic information on the state of the land as provided by the **HRL Tree Cover & Forests** layers allows to analyse regional trends in the area occupied by these land covers, which could be relevant information for authorities and policy makers. Furthermore, applications which require information on the land cover status can benefit from the HRL Tree Cover & Forests. For example, in case of biomass mapping often land cover specific parametrization is applied. Using the Tree Cover & Forests, allows to do this in a much more detailed and dynamic way. In case of the Evoland[^3] project, it is intended to use these layers to apply specific parametrization over tree-covered locations.

## 6.3 Use Case: Feasibility study for tree species mapping

**Umweltbundesamt (UBA)**, Germany: Explorative use of the **HRL Tree Cover & Forests** as base information and further analysis towards derivation of tree species from Sentinel-2 data in the frame of a feasibility study with German and Austrian partners. Results from 5 case study sites show that a number of 8-16 tree species could be detected using multi-temporal Sentinel-2 data. The study showed that a high number of available cloud-free satellite scenes and the availability

There is such demand for a tree species map in Germany at:

- **Umweltbundesamt (UBA -Environmental Protection Agency)**: Assessment and risk analysis of forest ecosystems, assessment of material discharges (critical loads), monitoring of indicators in the framework of the German Strategy for Adaptation to Climate Change.
- **Bundesamt für Naturschutz (BfN – Federal Agency for Nature Conservation):** renewable energy planning, requiring tree species composition to identify valuable habitats; considering adaptation to climate change.
- **Thünen-Institut (TI – Federal Research Institute for Rural Areas, Forestry and Fisheries):** Tree species accounting for the German State-of-Forest report („Wald-Zustandsbericht“).

# 7 Product description

The **HRL Tree Cover & Forests** layers are generally provided in 100km LAEA tiles as shown in Figure 7-1. The five French Oversea Territories are provided in UTM with the layout of the respective territory. The layers are available as Cloud-Optimized GeoTIFFs (COG) per reference year and 100km LAEA tile aligned with the **EEA reference grid**. Each raster file is accompanied by a Persistent Auxiliary metadata (PAM) XML and an INSPIRE XML.

The HRL **Tree Cover & Forests** layers comprise two yearly primary status layers: **Dominant Leaf Type (DLT)** and **Tree Cover Density (TCD)**. The status layers at 10-metre spatial resolution share the same spatial extent and provide information on the leaf type (**DLT**) and the proportional tree cover at pixel level (**TCD**). These layers map trees wherever they occur, also outside of what is (technically) a forest.

In the HRL **Tree Cover & Forests** product there is an additional status layer that applies the FAO forest definition[^4], and can therefore be called a (sensu stricto) forest product: the **Forest Type (FTY)** layer (in 10 metres and 100 metres resolution). The fact that TCD and DLT do not have a forest definition and filtering applied, makes it possible for users to adapt the existing tree cover density / dominant leaf type layers to their own forest definition (if different from the FAO definition). Following the FAO definition, the FTY excludes tree cover with a density of less than 10%, trees located in urban areas or under agricultural use, and group of trees smaller than 0.5 ha. This information is sourced from **Corine Land Cover** and the **HRL Imperviousness** datasets and is made available in the auxiliary **Forest Additional Support Layer (FADSL)**. The Minimum Mapping Width (MMW) of 20 metres suggested by the FAO definition is not enforced and thinner tree cover elements mapped in the DLT are retained as long as they satisfy the MMU of 0.5ha.

The yearly status layers classifications at a spatial resolution of 10 metres represent the input for two change layers which follow a 3-yearly update cycle. Those are a **Tree Cover Presence Change (TCPC)**[^5] and a **Dominant Leaf Type Change (DLTC)** layers in 20-metre spatial resolution and with a Minimum Mapping Unit of 1 ha. The **TCPC** layer includes four thematic classes out of which two indicate changes (new tree cover/loss of tree cover) between two time steps. The **DLTC** is derived by dedicated GIS operations from TCPC and the primary status layer (**DLT**) of 2018 and 2021. It includes 6 thematic classes, thereof 4 change classes.

![Choropleth map of Europe illustrating the spatial coverage of land monitoring data, categorized by two geographical scopes: EU27 and EEA38. The map features a base layer of European country outlines in grey, overlaid with a grid of squares. The legend indicates: \* Green outlined squares: 'Included in EU27 coverage'. This covers the 27 EU Member States (e.g., France, Germany, Italy, Spain, Poland, Ireland, Portugal, Greece, etc.) and their associated islands like the Canary Islands, Madeira, and Azores. \* Blue outlined squares: 'Included only in EEA38 coverage'. These squares extend the coverage to non-EU Member States that are part of the European Environment Agency (EEA38) network, including Norway, Iceland, the United Kingdom, Switzerland, and Turkey, as well as the Western Balkan countries (e.g., Albania, Bosnia and Herzegovina, Montenegro, North Macedonia, Serbia). The map shows that the EU27 coverage forms a contiguous block over the majority of continental Europe. The EEA38 coverage expands this to include northern Scandinavia, the British Isles, Iceland, Switzerland, and a significant portion of Southeast Europe and Anatolia. A horizontal scale bar at the bottom right indicates distances from 0 km to 1600 km, marked at 400 km intervals.](products_Product_User_Manual_-_Tree_Cover_and_Forests_2018-present-media/img-e00db7d8be8efd95fe018590f9af1505.png)

Figure 7-1: LAEA tile layout including distinction between tiles to cover EU27 and EEA38.

Further, aggregated layers of the status layers at 100-metre resolution are provided, as well as additional auxiliary layers and some reference datasets (Figure 7-2). The **TCD** at **100-metre** spatial resolution is derived through spatial aggregation from the 10-metre TCD status layer for the respective reference year. **Broadleaved Cover Density (BCD)** and **Coniferous Cover Density (CCD)** layers depict respectively the percentage of broadleaved and coniferous pixel at 100-metre spatial resolution. They are derived through aggregation of the 10-metre **DLT** for the respective reference year.

![This diagram illustrates the data product structure for the Copernicus Land Monitoring Service (CLMS) High Resolution Layer (HRL) Tree Cover & Forests, provided yearly since 2018. The product suite is organised into four main categories: Status, Change, Ancillary, and Reference. The \*\*Status\*\* category includes products describing current forest characteristics: \* Dominant Leaf Type (DLT) at 10m resolution. \* Tree Cover Density (TCD) at 10m and 100m resolutions. \* Forest Type (FTY) at 10m and 100m resolutions. \* Broadleaved Cover Density (BCD) at 100m resolution. \* Coniferous Cover Density (CCD) at 100m resolution. The \*\*Change\*\* category includes products for detecting forest changes: \* Tree Cover Presence Change (TCPC) at 20m resolution. \* Dominant Leaf Type Change (DLTC) at 20m resolution. The \*\*Ancillary\*\* category provides support and confidence layers: \* Dominant Leaf Type Confidence Layer (DLTCL) at 20m resolution. \* Tree Cover Density Confidence Layer (TCDCL) at 20m resolution. \* Tree Cover Presence Change Confidence Layer (TCPCCL) at 20m resolution. \* Forest Additional Support Layer (FADSL) at 10m resolution. The \*\*Reference\*\* category contains: \* Samples for internal accuracy assessment (FORREF).](products_Product_User_Manual_-_Tree_Cover_and_Forests_2018-present-media/img-5ad86979641a90d95be4b7b74e8133a8.png)

Figure 7-2 HRL Tree Cover & Forests product portfolio

## 7.1 Thematic characteristics of the Tree Cover & Forests Product

Table 7-1 provides an overview of the **Land Cover (LC)** and **Land Use (LU)** features that shall be included or excluded in the “tree cover” mapping, if detectable from the satellite imagery. In general, this definition has been kept consistent with previous productions since the initial reference year 2012.

The **Tree Cover Density (TCD)** is defined as the „vertical projection of tree crowns to a horizontal earth’s surface“ and provides information on the proportional crown coverage per pixel. Reference TCD values have originally been derived using **Very High Resolution (VHR)** satellite data and/or aerial ortho-imagery as reference data. Thereby **TCD** is assessed on different VHR sources by visual interpretation following a 10x10 point grid approach, resulting in proportional density information on a 100 x 100 metres grid level. This density information can be linked with the average spectral values from the input satellite data to train regression models which are subsequently used to estimate the **TCD** for areas where no reference data is available.

TCD shows a natural sensitivity towards phenology and radiometric influences (e.g. haze). Consequently, the magnitude of TCD values strongly relies on the availability and quality of adequate satellite input data and reference data and may vary regionally. Furthermore, extreme weather events and climate conditions (e.g. European drought 2018) show a negative influence on the magnitude of density values due to leaf colouring and leaf shedding.

Table 7-1: Elements to be included/excluded in tree cover

[TABLE]

## 7.2 Download content, file naming convention and file format(s)

Table 7-2: Download content, file naming convention and file format(s) for HRL Tree Cover & Forests layers

[TABLE]

## 7.3 Projection and spatial coverage

Table 7-3: Projection and spatial coverage for HRL Tree Cover & Forests layers

[TABLE]

Back to top

## Footnotes

## Reuse

EUPL (\>= 1.2)

[^1]: <https://land.copernicus.eu/en/eagle?tab=technical_implementation>

[^2]: <https://land.copernicus.eu/en/technical-library/product-user-manual-clc-backbone-2021>

[^3]: <https://www.evo-land.eu/method/biomass-mapping/> of additional adequate local reference data for algorithm training are required for retrieval of the results\[^4\].

[^4]: <https://www.fao.org/4/ad665e/ad665e03.htm>

[^5]: In previous productions the TCPC was still called Tree Cover Change Mask (TCCM)
