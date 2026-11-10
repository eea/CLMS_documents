# Protected Areas 2021 - Product User Manual (PUM)

Copernicus Land Monitoring Service

This Product User Manual details the Copernicus Land Monitoring Service (CLMS) Protected Areas (PA) product, offering harmonised land cover and land use information for over 25,000 Natura 2000 sites across Europe. It outlines the product’s evolution, including the 2021 status layer, which establishes a new baseline with comprehensive coverage and a refined methodology. The document meticulously explains the technical specifications, such as the 59-class hierarchical nomenclature, 0.5 ha minimum mapping unit, and the production workflow, which leverages super-resolved Sentinel-2 and Very High Resolution satellite imagery. Furthermore, it presents a thorough quality assessment, including thematic accuracy and validation results, enabling scientists and data engineers to effectively utilise this crucial biodiversity monitoring resource.

Published

February 26, 2026

Keywords

CLMS Protected Areas, Natura 2000 sites, land cover and land use classification, Very High Resolution satellite imagery, Super-resolved Sentinel-2 time series, thematic accuracy assessment, hierarchical classification nomenclature, Minimum Mapping Unit, Deep Learning models, biodiversity monitoring

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

# 1 Non-technical summary

The Copernicus Land Monitoring Service Protected Areas product provides detailed and harmonised land cover and land use information for Natura 2000 sites across Europe. The 2021 product covers approximately 821,000 km² and 25,011 Natura 2000 sites, creating a common European dataset that can support biodiversity monitoring, conservation assessments and the analysis of changes within protected areas.

The product maps land cover and land use using a hierarchical nomenclature with 59 classes at the most detailed level. The minimum mapping unit is 0.5 ha and the minimum mapping width is 10 m, allowing relatively small and narrow landscape features to be represented. The dataset is distributed as polygon vector data for use in geographic information systems.

Production combines Earth observation imagery and existing reference information. Multi-temporal Sentinel-2 imagery provides information on seasonal and spectral behaviour, while Very High-Resolution satellite imagery supports visual interpretation and manual refinement. Existing Copernicus Land Monitoring Service datasets and other ancillary information are also used to improve thematic consistency and support difficult classification decisions.

The Protected Areas product continues the earlier Natura 2000 land cover and land use mapping series for 2006, 2012 and 2018. The 2021 layer establishes a new baseline with complete terrestrial Natura 2000 coverage and a revised methodology. The 2024 production cycle will provide an updated status layer together with a 2021–2024 change layer.

Potential uses include analysing the distribution and evolution of broad land cover and land use types, identifying areas where changes have occurred, supporting assessments of protected-area management, and combining the information with other Copernicus or biodiversity datasets. For applications requiring detailed habitat condition, species-level information or local ecological interpretation, complementary thematic or field information may still be required.

# 2 Executive summary

Copernicus is the European Union’s Earth Observation Programme. It offers information services based on satellite Earth observation and in situ (non-space) data. These information services are freely and openly accessible to its users through six thematic Copernicus services (atmosphere monitoring, marine environment monitoring, land monitoring, climate change, emergency management and security).

The Copernicus Land Monitoring Service (CLMS) provides geographical information on land cover and its changes, land use, vegetation state, water cycle and earth surface energy variables to a broad range of users in Europe and across the world in the field of environmental terrestrial applications. CLMS is jointly implemented by the European Environment Agency and the European Commission DG Joint Research Centre (JRC).

The local component as part of the CLMS is coordinated by the European Environment Agency and aims to provide specific and more detailed information that is complementary to the information obtained through the Pan-European component. The local component focuses on different hotspots, i.e. areas that are prone to specific environmental challenges and problems. It is based on very high-resolution imagery in combination with other available datasets (high and medium resolution images) over the pan-European area.

Natura 2000 sites are important hotspots for nature conservation therefore, the objective of the Protected Areas (PA) product of CLMS is to provide detailed Land Cover / Land Use (LC/LU) mapping results, covering a total of 25,011 Natura 2000 sites and the service covers 821,000 km² of land surface across Europe.

The central aim of the Natura 2000 (N2K) protected areas network is to ensure the long-term survival of Europe’s most valuable and threatened species and habitats. Information is still lacking on the effectiveness of conservation measures in Europe’s protected areas. The CLMS N2K product aims at filling these gaps through objective and European-wide harmonized information on LC/LU within Natura 2000 sites, directly supporting the analysis of trends and progress in stopping the ongoing loss of biodiversity in Europe. It currently offers two types of products, status maps for the three reference years and two change layer products for the two reference periods and covers 821,000 km² of land surface across Europe. For each selected Natura 2000 site, the former N2K product also covers a 2 km buffer zone.

This is a unique product with a high level of detail (Minimum Mapping Unit (MMU) is 0.5 ha), based on Very High Resolution (VHR) satellite data. The classification provides 59 distinct thematic classes, and the class definitions follow a pre-defined nomenclature based on the Mapping and Assessment of Ecosystems and their Services typology of ecosystems (at level 1) and are further harmonised with Corine Land Cover and adapted to the specific characteristics of grasslands habitats (levels 2 to 4). It offers two types of products: status maps for 2021 reference year and 2024 as well as one change products between those periods.

The N2K former product offers a good basis to analyse the LC/LU situation in grassland- rich Natura 2000 sites and furthermore allows to devise the general trends and change factors within the sites through the observation periods, as well as within the buffer zone surrounding those. CLMS decided to restart the N2K product (from 2021 onwards) with a 3-year interval between inventories (2021 and 2024) and covering all Natura 2000 sites, thereby addressing the spatial and temporal resolution requirements. It was also decided to no longer map the 2 km buffer surrounding the sites. Hereinafter referred to as “CLMS PA”, a LC/LU product in a selection of Natura 2000 sites.

# 3 Background of the document

## 3.1 Scope and objectives

This Product User Manual is the primary document that users are recommended to read before using the CLMS Protected Areas (former N2K) product. It provides an overview of the product characteristics, product methodology and workflows, user requirements and example/potential use cases, information about the quality assessment checks and their results as well as product technical support.

## 3.2 Content and structure

The document is structured as follows:

- **Chapter 1** provides a non-technical overview of the product and its intended use.
- **Chapter 2** provides the executive summary.
- **Chapter 3** explains the scope, content and structure of this Product User Manual and lists the applicable project documents.
- **Chapter 4** describes the lineage of the product.
- **Chapter 5** reviews the main user requirements.
- **Chapter 6** presents product application areas; example use cases and thematic overlaps.
- **Chapter 7** describes the product portfolio, characteristics and technical specifications.
- **Chapter 8** summarises the production methodology, workflow and quality assessment information relevant to users.
- **Chapter 9** provides the terms of use, citation guidance and product technical support.

The final sections provide the list of abbreviations and acronyms, references and, where applicable, annexes.

## 3.3 Applicable documents (AD)

The project documents listed in Table 1 provide the detailed technical, validation and nomenclature information supporting this Product User Manual.

Table 1: Applicable project documents

| ID | Document name / content |
|----|----|
| AD01 | CLMS PA Nomenclature and Mapping Guideline (30/04/2026): not published yet |
| AD02 | PA validation report (2021 database): not published yet |
| AD03 | PA Algorithm Theoretical Basis Document (2021 database): not published yet |

# 4 Lineage of product

The Protected Areas product continues the Copernicus Land Monitoring Service Natura 2000 land cover and land use mapping series produced for the reference years 2006, 2012 and 2018. The earlier product focused on a subset of Natura 2000 sites, particularly grassland-rich areas, and used a six-year update cycle.

Building on that experience and on the user needs described in this manual, the Protected Areas product extends the spatial coverage to all terrestrial Natura 2000 sites included in the service and increases the update frequency to three years. The 2021 status layer provides the new baseline. The 2024 production cycle will provide a new status layer together with a 2021-2024 change layer.

The updated product also introduces a revised production approach based on multi-temporal Sentinel-2 information, Very High-Resolution imagery, existing Copernicus Land Monitoring Service datasets and ancillary information. The nomenclature has been expanded to 59 classes to accommodate the broader diversity of land cover and land use conditions found across the complete Protected Areas domain.

# 5 Review of user requirements

The European Commission has been systematically collecting user needs for Copernicus products and services, expressed in different policy areas. Information on specific aspects of land cover, land use and changes such as provided by this CLMS N2K product are an essential prerequisite to support many policies, reporting and monitoring obligations (European Comission -EC-2019).

The reference baseline for pan-European land cover and land use mapping has traditionally been provided by the Corine Land Cover (CLC) inventory and its complementary High-Resolution Layers. The former CLMS N2K product supplemented these datasets by delivering information at a finer thematic and spatial resolution for a subset of grassland-rich Natura 2000 sites. The new Protected Areas product ensures continuity with the previous N2K dataset while extending the coverage to all terrestrial Natura 2000 sites across the EU27 (European Union 27 Member States), amounting to approximately 821,000 km² and 25,011 sites. Also, PA shows a strong core as a 2,5 m x 2,5 m raster classification derived from the use of super-resolved Sentinel-2 time series and a reliable training dataset coming from Copernicus information feeding Deep Learning models, as well as confidence layers. In addition, the nomenclature has been expanded from 55 to 59 classes to account for the wider diversity of Natura 2000 habitats.

The central objective of the Natura 2000 network is to ensure the long-term conservation of Europe’s most valuable and threatened species and habitats. Despite significant progress, information gaps remain regarding the effectiveness of conservation measures and the evolution of ecosystems within protected areas. The Protected Areas product addresses these gaps by providing harmonized Very High Resolution (VHR) land cover and land use information, supporting assessments of ecosystem status and changes across Natura 2000 sites. The previous N2K product demonstrated the value of detailed LC/LU information for analyzing trends in grassland-rich sites. Building on this experience and on recommendations from the Knowledge Centre on Earth Observation (KCEO, Camia et al., 2024), the new product extends the spatial scope to all Natura 2000 habitats and increases the update frequency from six to three years. The 2021 status layer provides the baseline, while the 2024 update includes both a new status layer and a 2021–2024 change layer, enabling improved monitoring of ecosystem dynamics and supporting more timely assessments.

The product supports the implementation of the European Union -EU- Biodiversity Strategy for 2030 and contributes to the monitoring of protected areas, ecological connectivity and conservation effectiveness. It also responds to recommendations identified in the KCEO Biodiversity Deep Dive assessment, which highlighted the need for complete Natura 2000 coverage and increased temporal resolution. Furthermore, the product provides a basis for supporting agri-environmental indicators and future policy requirements by integrating Very High-Resolution imagery with other Copernicus products, Sentinel time series and ancillary data sources.

The new EU Biodiversity Strategy for 2030 makes it clear that for the good of our environment and our economy additional efforts are needed, to deal with the five main direct drivers of biodiversity loss – changes in land and sea use, overexploitation, climate change, pollution, and invasive alien species. The CLMS PA products support the EU Biodiversity Strategy 2030 with specific focus on areas of very high biodiversity value or potential.

# 6 Product application areas and use case examples

The CLMS PA product provides highly detailed and consistent information on Land Cover / Land Use (LC/LU) for approximately 821.000 km² across Europe. It has a thematic depth of 59 different LC/LU classes with a Minimum Mapping Unit (MMU) and Minimum Mapping Width (MMW), i.e. the smallest area to be distinguished, of 0.5 ha and 10 m, respectively.

The product is available for reference years 2006, 2012 and 2018 as N2K and 2021 as PA (reference year) and allows due to its technical setup a direct analysis of LC/LU changes across time using a homogenous data source across Europe. Examples of potential applications include:

- Monitoring land cover and land use evolution within Natura 2000 sites by comparing status layers from different reference years and, for 2021-2024, using the dedicated change layer.
- Identifying changes in agricultural, grassland, forest, wetland, urban or water-related land cover within protected areas and prioritising locations for further expert review.
- Supporting assessments of protected-area context by combining the Protected Areas land cover and land use information with biodiversity, habitat, species or conservation-management datasets.
- Analysing landscape structure and ecological connectivity by combining the Protected Areas product with complementary Copernicus Land Monitoring Service datasets.
- Supporting European, national or regional reporting and monitoring activities that require harmonised and spatially detailed land cover and land use information for Natura 2000 sites.

The product should be interpreted according to its thematic definitions, minimum mapping unit, minimum mapping width, reference period and validation results. Applications requiring detailed habitat condition, species-level information or local ecological interpretation may require complementary thematic or in-situ information.

## 6.1 Thematic overlaps between CLMS and external datasets

The hierarchical CLMS N2K LC/LU nomenclature is highly compatible with the CLMS Local Component Coastal Zone (CZ) and Riparian Zone (RZ) products. Depending on the LC/LU under investigation, these products could be jointly used to analyse LC/LC trends and changes.

The Protected Areas product overlaps thematically with other Copernicus Land Monitoring Service datasets, including Coastal Zones, Riparian Zones, High Resolution Layers and CLCPlus Backbone. These products have different objectives, thematic definitions, spatial characteristics and reference periods and should therefore be considered complementary rather than interchangeable.

Users should select or combine datasets according to the intended application. Protected Areas provides detailed land cover and land use information specifically for the protected-area domain, while other products may provide broader geographic coverage or more specialised thematic information. When several datasets are used together, differences in nomenclature, temporal reference, spatial resolution and mapping rules should be considered.

# 7 Product description and methodology

## 7.1 Overview of the product portfolio

The CLMS PA product contains two specific information layers for each reference year. The status layer describes the LC/LU situation in the relevant reference year. The change layer describes LC/LU change areas between two reference years. Currently status layers for the reference years 2006, 2012 and 2018 are available as N2K18 (Natura 2000 2018), with corresponding layers for 2006-2012 and 2012-2018. The CLMS PA for 2021 status layer product covers an area of 821.000 km² (Figure 1).

The CLMS PA layers are provided as polygon vector data. They cover 25.011 Natura 2000 sites across Europe (Figure 1), including a 20-meter buffer zone around each site (Figure 2).

The LC/LU classification is based on temporal series of superresolved Sentinel-2 imagery and visual image interpretation from Very High Resolution (VHR) satellite imagery. The characteristics of the product are the following:

- LC/LU is encoded following a detailed mapping nomenclature and guideline (AD01) into 59 different classes using a hierarchical LC/LU encoding structure ranging from 8 LC/LU classes at Code level 1 to the full 59 classes at Code level 4.
- LC/LU classes are:
  - based on the MAES (Mapping and Assessment of Ecosystems and their Services) ecosystem types of specification at Code level 1.
  - largely compatible with CORINE Land Cover (CLC) and Urban Atlas and adapted to the specific characteristics of grasslands habitats (Code levels 2 to 4).
  - harmonized with CLMS Riparian Zones and Coastal Zones products.
- Minimum Mapping Unit is 0.5 ha.
- Minimum Mapping Width is 10 m.

![A choropleth map illustrating the spatial distribution of land cover and land use within Natura 2000 (N2K) sites across the European continent. The map depicts numerous small, irregularly shaped patches of colour, predominantly shades of green (ranging from yellowish-green to dark green) and some sparse light blue, overlaid onto a white background representing areas outside the depicted features. These patches outline the boundaries and internal characteristics of what are identified in the surrounding context as Natura 2000 sites. The green hues likely represent various natural and semi-natural land cover types such as forests, grasslands, and other vegetated areas, while the blue patches suggest the presence of water bodies or wetlands within these protected areas. The density of these sites appears higher in central Europe, along mountain ranges, and in parts of the Iberian Peninsula and Scandinavian countries. No legend, scale bar, compass orientation, or explicit reference year is provided in the image itself, however, the surrounding context indicates this data is from the Copernicus Land Monitoring Service (CLMS) Protected Areas product, providing detailed land cover/land use (LCLU) information for Natura 2000 sites.](Protected_Areas_2021_PUM_v1-media/img-e9d05179488b557063b2e3c78d45b926.jpeg)

Figure 1: Coverage of the CLMS PA product

![This map displays a detailed mosaic of land cover and land use (LCLU) types within a geographic area, likely in Europe, consistent with Copernicus Land Monitoring Service (CLMS) datasets. The map uses a multi-coloured thematic classification to delineate different LCLU categories. Prominent features include: \* Extensive areas of light green and darker green, likely representing various types of natural or semi-natural vegetation such as forests, grasslands, or agricultural fields. \* Patches of orange and red, indicating urban fabric, industrial areas, or other artificial surfaces, with a concentration along a major linear feature. \* Smaller, interspersed patches of yellow, brown, and purple, which could signify agricultural areas, bare land, wetlands, or other specific land uses. \* A distinct linear feature, depicted in light grey and light blue, potentially representing a river, canal, or major transport infrastructure (road/railway), with adjacent land use patterns. The map lacks a visible legend, scale bar, compass rose, or reference year. The depicted complexity of land cover types is characteristic of detailed High Resolution Layers (HRL) or CORINE Land Cover (CLC) products.](Protected_Areas_2021_PUM_v1-media/img-5bcb69792943d4b60b180bb2752c14e6.jpeg)

Figure 2: Example coverage of CLMS PA product for a selected Natura 2000 site

## 7.2 Product characteristics

### 7.2.1 Natura 2000 boundary changes and the impact in the CLMS N2K product Area of Interest (Aol)

The Aol for mapping the LC/LU was set up, changed and extended throughout the evolution of the CLMS N2K product, in four different phases throughout the N2K-PA history:

Within the **first production phase**, during the initial setup of the N2K Aol under the Global Monitoring for Environment and Security (GMES) Initial Operations (GIO) project phase (GMES Initial Operation Phase in 2014) a selection of Natura 2000 grassland-rich sites (representing five grassland habitat types) as identified in Annex I of the Habitats Directive was used.

A list of Natura 2000 sites was proposed by the Directorate-General for Environment (DG ENV) based on their representativeness and relative importance for the given habitat types. The information about selecting sites based on the above criteria has been taken from the Natura 2000 site’s Standard Data Forms in the most recent version of the EU-wide Natura 2000 database at the time.

Based on this list of Natura 2000 site codes the corresponding site boundaries were extracted from the Natura 2000 Database (version: Natura 2000 v2013). This led to an Aol area of around 150.800 km². This led to an AoI area of around 150.800 km².

A GIS (Geographic Information System) and Earth Observation data analysis were then performed to:

- Buffer the Natura 2000 sites by 2 km, which increased the N2K Aol area to around 252.600 km²).
- Identify existing VHR satellite coverage for reference years 2006.
  - ± 1 year (with extension to ± 2 years for gap-filling) and 2012
  - ± 2 years within defined seasonal windows, so that in combination they reach \> 80% coverage of the full (buffered) N2000 (Natura 2000) site size (i.e. in the same areas, for both time steps). This reduced the Aol to around 162.600 km² - 173.800 km².

The finally mapped N2K product during the GIO Phase covered 160.443 km².

In the **second production phase** (started in 2016) the N2K Aol was enlarged. Additional Natura 2000 sites were selected, now based on a list of 32 different Annex 1 grassland habitat types as defined under the Habitats Directive. The additional Natura 2000 site boundaries were again taken from the Natura 2000 Database (this time from version: end2015). The buffer was applied to the newly selected sites and minor adaptations to the N2K Aol were made to correct imprecisions and omission errors. This changed the Aol size and geometry in a way that:

- Missing 2 km buffers were included, for mainly buffers around islands were missing
- Wrongly clipped buffers of selected N2K sites were included
- Existing gaps between N2K sites shapefile and EEA39 member states boundary shapefile were filled. Regarding water areas, those gaps over water appeared if EEA39 boundaries do not coincide with N2K site boundaries along coastlines and had also to be corrected and included
- Minor gaps and spikes between the Aols of the first and second phases were corrected and included
- Small angles (\<20°) were checked and corrected where feasible.

In the end of the second production phase, the existing 160.443km² were complemented by 471.377 km² leading to the N2K product covering 631.820 km² for the reference years 2006 and 2012.

In the **third production phase** (started in 2020 and finished in May 2021) the N2K product is updated to the reference year 2018, including the change layer 2012-2018. No changes were applied to the geographic coverage of the product.

The option taken for the N2K product was to have a stable Aol so that the change mapping exercise could be done within the same area and that the derived statistics were not affected by changing Aol’s.

As can be seen from the above “history” of the N2K Aol creation process, there were several input data sets used as well as several geospatial corrections applied to generate the currently used N2K coverage of 631.820km². As stated above there are several factors which prevent a 1:1 relation between the N2K Aol and Natura 2000 site boundaries:

- Different Natura 2000 database versions were applied to generate the unbuffered N2K site selection (version Natura 2000 v2013 and later version end2015). Changes in the yearly updated Natura 2000 site definitions were not adapted for already mapped N2K sites (Figure 3).
- N2K Aol adaptations to achieve a technically “clean” dataset may have led to deviations from a strict 2 km buffer zone around each selected Natura 2000 site.
- The availability of archived VHR satellite data for the reference years 2006 and 2012 required a threshold to produce N2K LC/LU information also for Natura 2000 sites covered by up to a minimum of 80% satellite data.

![The map displays several clusters of Natura 2000 (N2K) sites and their surrounding 2 km buffer zones, likely located within France based on the 'FR' prefix in the site identifiers. Individual Natura 2000 site boundaries are outlined in blue, while areas where these boundaries have undergone minor adaptations, imprecision corrections, or omission error fixes are highlighted with a red outline. A light grey shaded area encompasses each N2K site, representing a 2 km buffer around the site boundary. Specific Natura 2000 sites identified by their codes include: \* FR8212005, FR8202002, FR8201773 in the top left cluster. \* FR8201781 in the central-left and lower-left clusters. \* FR8212028 and FR8202003 associated with the large central landmass. \* FR8201777 in the top-right and lower-right clusters. The map illustrates the spatial extent of the Natura 2000 Area of Interest (N2K Aol), including buffered zones and adapted site geometries during a production phase, as described in the accompanying text. No scale bar, compass, or explicit legend is visible within the image.](Protected_Areas_2021_PUM_v1-media/img-40d29864fcd1f064824aff8885d3d596.jpeg)

Figure 3: Example of diverging Natura 2000 site boundaries (red 2015 version, blue 2019 version, grey N2K product coverage incl. the 2 km buffer)

Also, due to the buffering of the Natura 2000 sites by 2 km, the N2K sites may actually cover more than one Natura 2000 site (Figure 4). This has been one the reasons for the removal of the Natura 2000 Site code from the N2K Aol, to avoid a misinterpretation of the data. Because within the same N2K polygon there could be reference to more than one Natura 2000 site.

![The map displays several Natura 2000 (N2K) sites in Poland, outlined in black, with their surrounding 2 km buffer zones, delineated by a continuous red line. The geographic features suggest a complex landscape of land and water bodies. Three specific Natura 2000 sites are labelled with their codes: \`PLH220052\`, \`PLH220005\`, and \`PLH220037\`. A red label \`4409\` is visible near one of the features, likely indicating an Annex I habitat type as defined under the Habitats Directive (Directive 92/43/EEC). The red buffer lines collectively define an Area of Interest (Aol). No scale bar, compass, or legend is visible.](Protected_Areas_2021_PUM_v1-media/img-f8505692622f20726e498b2a77985674.jpeg)

Figure 4: Example of N2K Aol (red) covering multiple N2K sites (black)

To quantify the effects of the changing Natura 2000 Database on the N2K products a spatial analysis of the Natura 2000 database changes between 2015 and 2018 was performed.

During the data preparation it became evident, that the Natura 2000 databases are more complex than expected. The Natura 2000 sites are very often defined as “multi-part” polygons (Figure 5). This means that multiple detached areas form together one Natura 2000 site. Due to the above described N2K Aol creation process, Natura 2000 sites are not always covered by the N2K product for all their single areas. This is an important fact, if N2K products are related to Standard Data Form (SDF) information, e.g. Habitat coverage within site, which relates to the complete Natura 2000 site.

For this all Natura 2000 sites affected by the full N2K Aol were selected from the 2015 Natura 2000 Database (version: end2015). This resulted in 3872 different site codes. Performing the same process to the 2018 Natura 2000 Database (version: end2018) led to 3868 site codes. Four site codes have changed between 2015 and 2018. Here the Natura 2000 sites had a newer release data. This was for example the case for the Danish site code DK00BX044 in 2015, which was split up into two new site codes DK00BB396 and DK00BB380 (Figure 6). The four changed site codes were also included in the spatial analysis of the 2018 data.

Other Natura 2000 Database (DB) changes led to a partial coverage of 2018 geometries of formerly fully covered in 2015 (Figure 7). Partially these changes might still be covered by the N2K Aol, but initially the original 2 km buffer around the site is no longer valid for the complete site (Figure 8).

![This map displays several Natura 2000 (N2K) Areas of Interest (AoIs) in Europe. The main features are light blue, irregularly shaped polygons representing the AoIs. 1. \*\*Left Side:\*\* Two distinct light blue polygons are shown. \* The upper polygon is labelled 'AT3210001', likely indicating a Natura 2000 site in Austria. \* The lower polygon is labelled 'IT3110017', likely indicating a Natura 2000 site in Italy. \* Both of these light blue AoIs are surrounded by a consistent, light orange/peach outline. This outline likely represents the original Natura 2000 site boundary or a buffer layer associated with the Area of Interest delineation and correction process, as described in the Copernicus Land Monitoring Service (CLMS) documentation. 2. \*\*Right Side:\*\* A single, elongated, irregular light blue polygon is labelled 'AT3210001'. This AoI, unlike the ones on the left, does not have the surrounding light orange/peach outline. 3. \*\*Bottom Right:\*\* A smaller, unlabelled, irregular light blue polygon is partially visible at the bottom right, also without a surrounding outline. The presence or absence of the light orange/peach outline indicates different boundary processing or data representations for the respective N2K AoIs. The labels refer to specific N2K site codes. No scale bar or legend is visible. The geographic coverage for such N2K products is 631.820 km², with reference years 2006, 2012, and 2018 mentioned in the surrounding document text.](Protected_Areas_2021_PUM_v1-media/img-661c666a3f0e4739c79fc88f1883dba8.jpeg)

Figure 5: Example of multi-part Natura 2000 site (AT3210001) only partially covered by N2K Aol

![Choropleth map illustrating the impact of differing Natura 2000 (N2K) database versions on site definitions within a stable Area of Interest (AoI) for specific Danish (DK) sites. The image displays two side-by-side panels, representing a comparison of N2K site boundaries from different database iterations. Both panels feature an identical, irregular, light peach-coloured outer boundary, representing the N2K Area of Interest (AoI), consistent with the documentation's description of a stable AoI (e.g., a 2 km buffer zone) used for mapping and statistics. \*\*Left Panel:\*\* Depicts N2K sites in a light blue colour, likely corresponding to an earlier N2K database version (e.g., Natura 2000 v2013, as mentioned in the accompanying text). Two distinct N2K sites are labelled: 'DK00BX166' (an elongated area in the upper left portion of the AoI) and 'DK00BX044' (a smaller, compact area in the lower right). \*\*Right Panel:\*\* Depicts N2K sites in a light purple colour, likely corresponding to a later N2K database version (e.g., Natura 2000 end2015, per the documentation). The site 'DK00BX166' is still present in the upper left, but its precise shape shows minor alterations. The site 'DK00BX044' is no longer present; instead, two new, smaller sites, 'DK00BB396' and 'DK00BB380', appear clustered in its approximate former location in the lower right. This visual comparison demonstrates how N2K site definitions, including their shapes and unique identifiers, can be updated or revised across different database versions, while the defined N2K Area of Interest (AoI) remains consistent for mapping purposes. The map lacks an explicit scale bar, compass, or specific year labels within the image itself.](Protected_Areas_2021_PUM_v1-media/img-53ffe90508e380b5feedbc936a9c1826.jpeg)

Figure 6: Example of changed site codes and geometries from 2015 (left) to 2018 (right) Natura 2000 DB version

![Two choropleth maps comparing different versions of Natura 2000 (N2K) site definitions for a specific French site, FR7200672, within a consistent Area of Interest (AoI). The overall light orange shaded area in both maps represents the stable N2K Area of Interest (AoI), likely derived from a buffered N2K site selection, covering the same geographic extent in both views. The map on the left shows the N2K site boundaries based on an earlier database version (e.g., Natura 2000 v2013), depicted as fewer, larger, and more contiguous light blue polygons, each labelled 'FR7200672'. The map on the right shows the N2K site boundaries based on a later database version (e.g., Natura 2000 end2015), depicted as more numerous, smaller, and more fragmented light purple polygons, each also labelled 'FR7200672'. This comparison illustrates that while the N2K Area of Interest (AoI) (the light orange buffer) remains stable for Copernicus Land Monitoring Service (CLMS) products to facilitate change mapping, the underlying Natura 2000 site definitions (as governed by the Habitats Directive 92/43/EEC and Birds Directive 2009/147/EC) can change over time, leading to variations in the mapped protected area boundaries and fragmentation. No scale bar, compass, or legend are visible.](Protected_Areas_2021_PUM_v1-media/img-8c7c1f461c2570b3a750cb464982794d.jpeg)

Figure 7: Example of Natura 2000 DB site changes from 2015 (left) to 2018 (right). Background N2K Aol

![The map illustrates the divergence of Natura 2000 (N2K) site boundaries over time, contrasting an original site definition (left panel) with an updated definition (right panel) for several sites in France, all encompassed by a stable Area of Interest (Aol). The map displays two side-by-side views for the same set of N2K sites, labelled with identifiers such as FR7200682, FR7200683, FR7200684, FR7200685, and FR7200686. The light orange shading represents the N2K Area of Interest (Aol), which is a buffered zone (e.g., 2 km buffer) derived from an earlier Natura 2000 site selection and remains stable across updates. The left panel shows original Natura 2000 site boundaries, highlighted in light blue (teal), likely corresponding to an earlier database version such as Natura 2000 v2013. Internal grey lines indicate river networks or water bodies within these sites. The right panel shows updated Natura 2000 site boundaries, highlighted in light purple (lavender), corresponding to a later database version (e.g., end2015, used for the 2018 reference year update). These updated boundaries also contain internal grey lines for water features. The map clearly demonstrates how the shape and extent of the core N2K site boundaries (blue vs. purple) can change between different database versions while the surrounding N2K Aol (orange) remains fixed. This results in instances where the updated site boundaries (purple) either slightly deviate from the earlier boundaries (blue) within the consistent Aol, or where the Aol no longer perfectly matches the updated site shapes, as indicated by the accompanying text explaining that changes in yearly updated N2K site definitions were not adapted for already mapped N2K sites.](Protected_Areas_2021_PUM_v1-media/img-4266d4cac7e80dadc9370fc8dd5ef5c8.jpeg)

Figure 8: More examples of Natura 2000 DB site changes from 2015 (left) to 2018 (right). Background N2K Aol

The Natura 2000 site boundaries were intersected with the N2K Aol for both years to analyse the total area covered by the Natura 2000 sites, and their spatial overlap with the N2K Aol. Due to the fact that there are overlapping geometries in the Natura 2000 sites DB (Figure 10), the analysis was performed also with the Natura 2000 sites merged to one analysis extent.

The results showed that more than 98% of the area covered by the selected grassland-rich Natura 2000 sites is covered by the N2K product in for both Natura 2000 site definitions, version end2015 and end2018 (Figure 4).

![This map displays a geographic area within Italy, showcasing a single Copernicus Land Monitoring Service (CLMS) Natura 2000 (N2K) Area of Interest (AoI) (shaded pale blue) that covers several distinct Natura 2000 sites. The boundaries of the individual Natura 2000 sites are outlined in cyan within the larger pale blue AoI. Each individual N2K site is labelled with a unique identifier code, typical for Italian Natura 2000 sites: IT5340010, IT7110128, IT6020025, IT7120201, IT7120213, and IT7110202. The presence of multiple site codes within a single AoI illustrates how the CLMS N2K product coverage can aggregate several Natura 2000 sites, highlighting the removal of individual site codes from the N2K AoI to prevent misinterpretation of aggregated data. The white areas represent regions outside the defined N2K AoI. No scale bar, compass, or explicit legend is visible.](Protected_Areas_2021_PUM_v1-media/img-f4b3bdf0b65f14b0d0e5a96bff81f8ec.jpeg)

Figure 9: Example of Natura 2000 DB site overlap. The site codes IT6020025, IT7120201 and IT5340010 overlay the area of site code IT7110128.

Table 2: Spatial coverage of Natura 2000 DB sites by N2K Aol in 2015 and 2018

| Area | 2015 | 2018 | Difference 2015-2018 |
|----|----|----|----|
| Total area of Natura 2000 sites (with overlaps) \[km²\] | 284.195,48 | 284.977,85 | \+ 782,37 |
| Total area of Natura 2000 sites (without overlaps) \[km²\] | 272.483,95 | 273.266,93 | \+ 782,98 |
| Area of Natura 2000 sites (without overlap) covered by N2K AoI \[km²\] | 267.820,37 | 268.167,05 | \+ 346,68 |
| Percentage of Natura 2000 area covered by N2K AoI (without overlaps) \[%\] | 98,3 | 98,1 | \- 0,2 |

Comparing the spatial dynamics of the 2015 and 2018 Natura 2000 site boundaries in comparison to the current N2K Aol showed that the selected sites in the 2018 Natura 2000 DB had around 537 km² area removed, which was still contained in the 2015 DB version, whereas around 1.320 km² were newly added in the 2018 DB version. Of this newly added area, 66% was still covered by the unchanged N2K Aol (Figure 5).

Table 3: Area changes for Natura 2000 DB sites from 2015 to 2018

| Natura 2000 area changes 2015-2018 |  | Value |
|----|----|----|
| Common area in 2015 and 2018 |  | 271.946,91 km² |
| Area only in 2015 data (removed) |  | 537,04 km² |
| Area only in 2018 data (new) |  | 1.320,02 km² |
|  | covered by N2K AoI (Inside) | 871,79 km² (66%) |
|  | not covered by N2K AoI (Outside) | 448,23 km² (44%) |

The boundaries of Natura 2000 may change from year to year but usually those are not dramatic changes and are usually covered by the 2 km buffer zone. There are, however, a few occasions when a change in extent may have gone over the N2K established Aol. Extreme situation illustrated below (Figure 10).

![This map illustrates the geographic distribution of Production Units (DU) across Europe and provides a magnified example of a Natura 2000 (N2K) site, specifically for the Copernicus Land Monitoring Service (CLMS) Protected Areas (PA) status product 2021. The main map shows Europe and surrounding seas (Atlantic Ocean, Norwegian Sea, Barents Sea, Baltic Sea, Black Sea, Mediterranean Sea) divided into numerous Production units (DU) represented by white polygons with black outlines. Visible Production Unit labels include DU0001, DU0003, DU0006, DU0007, DU0009, DU0011, DU0013, DU0014, DU0015, DU0016, DU0017, DU0018, DU0019, DU0022, DU0023, DU0024, DU0025, DU0026, DU0027, DU0028, DU0031, DU0032, DU0033, DU0034, DU0035, DU0037, DU0038, and DU0039. A magnified inset, originating from the region of DU0013, details a selected Natura 2000 site. In this inset, the 'Natura 2000 site extent' is shown in pink, while the 'Buffered N2K AoI' (Area of Interest) is depicted in green, encompassing the pink area. A North arrow is present in the top-left corner. A scale bar indicates distances from 0 to 1,500 km, with intermediate marks at 500 km and 1,000 km.](Protected_Areas_2021_PUM_v1-media/img-f7017e3386d281258f003b5a84caf879.jpeg)

Figure 10: Example of a Natura 2000 site change in extent (enlargement): the green buffer follows the shape of the site in 2012, but in the 2018 Natura 2000 database the site has been enlarged therefore not anymore totally covered by the N2K Aol

This was one of the reasons why it was decided to **remove the Natura 2000 site boundary from the N2K product**: to allow users to use the N2K LC/LU product in combination with the Natura 2000 latest boundary, if they wish so in their dedicated assessments therefore not being bound by an outdated outline that may change on a yearly basis.

**CLMS N2K18 status layer: example**

The PA status layer represents the LC/LU status identified on the available satellite images for the specific reference year (Figure 11).

![This map illustrates Land Cover / Land Use (LCLU) polygons overlaid on a false-colour infrared satellite image, demonstrating an example of a Natura 2000 (N2K) site change. The specific geographic location is not named. The map is bounded by a blue outline, which represents the green buffer area following the shape of the Natura 2000 site as defined in 2012. Within this 2012 N2K buffer, the LCLU polygons are colour-coded as follows: \* \*\*Red:\*\* Indicates areas of dense urban fabric or highly impervious surfaces. \* \*\*Purple:\*\* Represents other artificial surfaces, potentially industrial, commercial, or transport units. \* \*\*Yellow and Light Green:\*\* Depict different types of agricultural land or grasslands. \* \*\*Dark Green:\*\* Shows areas of forest or semi-natural vegetation. \* \*\*Brown:\*\* Suggests sparsely vegetated areas, bare land, or specific agricultural uses. The underlying satellite imagery displays dense vegetation in red tones, agricultural fields in varying red and green hues, and some urban or bare areas in greyish-cyan. A scale bar at the bottom indicates a map scale of 1:50,000, with labelled distances for 0, 1, and 2 km. A North arrow is present. The map specifically highlights how an enlargement of a Natura 2000 site (e.g., in the 2018 Natura 2000 database) might extend beyond an older (2012) buffer zone, informing the design of Copernicus Land Monitoring Service (CLMS) Natura 2000 products.](Protected_Areas_2021_PUM_v1-media/img-956b769b579d24a89a162a94f6d563d0.jpeg)

Figure 11: CLMS PA status product 2021. Example for a selected Natura 2000 site.

In the **fourth production phase** (started in 2024) the PA Aol was enlarged. The Area of Interest (Aol) used for the CLMS Protected Areas products is derived from the aggregation of Natura 2000 sites provided by the Member States and complemented by Emerald Network sites and the United Kingdom contribution. Prior to production, the Aol underwent a dedicated refinement process aimed at ensuring geometric consistency and suitability for large-scale land cover and land use mapping. Several issues inherent to the aggregation of protected area datasets, such as overlapping polygons, multipart geometries, isolated features below the Minimum Mapping Unit (MMU) and topological inconsistencies, were identified and addressed. The following examples illustrate some of the most representative cases encountered during the Aol preparation and the actions undertaken to obtain a seamless and coherent area of interest for the CLMS Protected Areas products. A 20 m buffer was applied to the Area of Interest to reduce snapping issues between adjacent polygons and to avoid the generation of isolated artefacts and spikes. This operation contributed to obtaining a more robust and homogeneous spatial framework for the subsequent land cover and land use mapping activities.

Table 4: Overview of N2000 terrestrial sites and area per level of processing and inclusion within PA2021

| Area                     | 2015   | 2018    |
|--------------------------|--------|---------|
| Sites PA2021 ITT (no UK) | 24.298 | 735.481 |
| Sites PA2021 (w/ UK)     | 25.011 | 757.591 |
| Sites PA2021 (AoI fixed) | 25.011 | 821.354 |

**Overlapping polygons (Figures 12).**

Overlapping polygons inherited from the aggregation of different protected area sources were identified during the Aol preparation. These overlaps were reviewed and resolved in order to obtain a seamless and geometrically consistent area of interest suitable for the production workflow.

![Two satellite maps illustrate changes in Natura 2000 (N2K) site boundaries between 2012 and 2018, demonstrating how site enlargements can exceed older Area of Interest (AoI) definitions. The underlying satellite imagery shows a landscape of forests (dark green), agricultural fields (light green/brown), and water bodies (blue). In both maps: \* Red outlines represent the Natura 2000 site boundaries as recorded in the 2018 Natura 2000 database. \* Yellow outlines represent the Area of Interest (AoI) buffer, which follows the shape of the Natura 2000 site in 2012. The left map displays a long, winding riverine Natura 2000 site, along with several smaller, isolated N2K sites. The 2018 N2K boundary (red) is generally wider than and extends beyond the 2012 AoI buffer (yellow) in numerous sections, particularly in the central and southern parts of the main linear site. The smaller N2K sites are bounded in red but lack corresponding yellow 2012 AoI buffers. The right map focuses on a Natura 2000 site centered around a large lake, with an urban area visible to the north. The 2018 N2K site boundary (red) shows a significant enlargement compared to the 2012 AoI buffer (yellow). The red outline encompasses a much larger area of the lake and surrounding land to the south and west, clearly exceeding the extent of the yellow 2012 AoI. The maps highlight that the 2018 Natura 2000 sites are no longer entirely covered by the 2012 N2K Area of Interest, indicating site enlargement over time.](Protected_Areas_2021_PUM_v1-media/img-575f094e856495f5793c8358529ca690.jpeg)

Figure 12: Examples in Germany of overlapped N2000 terrestrial sites

**Multipart geometries (Figures 13).**

Several protected areas are represented by multipart geometries containing isolated components of different sizes. Particular attention was paid to small isolated polygons and their consistency with the Minimum Mapping Unit (MMU) requirements, ensuring that the final Aol remained coherent while preserving the integrity of the protected sites.

![A satellite imagery map illustrating the Copernicus Land Monitoring Service (CLMS) Protected Areas (PA) status product for 2021, showing examples within selected Natura 2000 (N2K) sites. The map is divided into two panels, displaying different geographic areas, likely within a European landscape characterized by forests, agricultural fields, and a river network. The base layer is high-resolution satellite imagery depicting detailed land cover/land use (LCLU). Red lines outline the boundaries of Natura 2000 sites, serving as contextual information. Yellow lines represent the CLMS PA status layer, highlighting specific Land Cover / Land Use (LCLU) status features identified within or adjacent to the protected areas. The left panel presents a wider view, showing several distinct, relatively large Natura 2000 sites (red outlines) primarily encompassing forested areas. A major river flows through the bottom. Numerous smaller, irregularly shaped yellow polygons, representing the LCLU status, are visible both within and outside the red Natura 2000 boundaries, often highlighting specific patches of land or features. The right panel shows a more magnified view of a different area, characterized by dense forest cover and agricultural mosaics. Here, the red Natura 2000 boundaries are more intricate and branching. The yellow lines representing the CLMS PA status product are predominantly elongated and curvilinear, often tracing linear landscape features or specific land cover types. The image serves as an example of how the CLMS PA status layer (yellow features) delineates LCLU status, in relation to, but distinct from, the formal Natura 2000 site boundaries (red outlines) for the 2021 reference year.](Protected_Areas_2021_PUM_v1-media/img-fc141ecc1348ed5eab4ddc75399643ef.jpeg)

Figure 13: Examples of multipart polygons in some N2000 terrestrial sites

**Minimum Mapping Unit issues (Figures 14).**

Small, isolated polygons and narrow artefacts below the Minimum Mapping Unit (MMU) and Minimum Mapping Width (MMW) thresholds were identified during the refinement process. Geometric adjustments and buffering operations were applied to avoid spikes and improve topological consistency.

![This map displays a Copernicus Land Monitoring Service (CLMS) Protected Area (PA) status product for a selected Natura 2000 (N2K) site, shown alongside a detailed satellite image of a specific feature. The left panel provides a wider geographic overview of a natural landscape, with a dark green background representing extensive vegetation (likely forest) and numerous dark blue/black patches indicating water bodies. Overlaid on this background are many red outlines of varying shapes and sizes, which delineate the boundaries of protected areas, consistent with Natura 2000 or Emerald Network sites. A single small yellow dot is centrally located in the upper portion of the left panel, highlighting a point of interest. The right panel presents a high-resolution satellite image, with a faint '2023' watermark, showing a zoomed-in view of the location marked by the yellow dot. This detailed view depicts a dense, dark green forest canopy. A small, yellow hexagonal outline draws attention to a specific feature within this forest, exemplifying isolated features below the Minimum Mapping Unit (MMU) that are identified and addressed during the Area of Interest (AoI) refinement process for CLMS Protected Areas products.](Protected_Areas_2021_PUM_v1-media/img-359b98648d2abd8462ff643404af119b.jpeg)

Figure 14: Examples of singular trees included as N2000 terrestrial sites, falling below MMU located in Finland and Germany

**Sliver polygons (Figures 15).**

Sliver polygons and narrow artefacts generated by geometric inconsistencies during the aggregation of protected area boundaries were identified throughout the Aol refinement process. Most of these artefacts were automatically corrected through dedicated topological operations based on angle revision and geometry regularization. In a limited number of cases, manual editing was required to preserve the integrity of the original boundaries and ensure a consistent representation of the Area of Interest.

![This image displays two panels of false-colour satellite imagery with overlaid yellow polygons, illustrating the issue and resolution of multipart geometries in Natura 2000 (N2K) terrestrial sites. The background imagery shows dense vegetation as red, and bare ground or rock as light blue/white. Small cyan points are present within the polygons. The top panel shows a Natura 2000 site boundary (yellow polygon) where the geometry is fragmented into multiple disconnected parts, including smaller, isolated yellow outlines within the larger extent of the protected area. This visualises the problem of 'multipart geometries'. The bottom panel shows the same geographic area with the yellow polygon boundaries refined. The smaller, isolated polygons depicted in the top panel have been processed and integrated into a more contiguous and geometrically consistent boundary, representing the resolved state of the multipart geometry issue. The cyan points remain in similar locations across both panels. No scale bar, compass, legend, or explicit reference year is visible in the image, but the surrounding document context refers to '2021_PUM_v1' and mentions consistency with Minimum Mapping Unit (MMU) requirements.](Protected_Areas_2021_PUM_v1-media/img-b26ea6681e093fcbbf295b22012f4b40.jpeg)

Figure 15: Examples of slivers within Aol borders located in Alps

**Bad snapping and boundary consistency**

Misalignments and bad snapping effects between adjacent polygons were detected during the preparation of the Aol. To improve boundary consistency and reduce the occurrence of small gaps, overlaps and isolated artefacts, a 20 m buffer was applied to the Area of Interest. This operation contributed to obtaining a more robust and homogeneous spatial framework for the subsequent land cover and land use mapping activities.

![This map illustrates a geometric adjustment process for Natura 2000 (N2K) terrestrial site boundaries, demonstrating an issue related to the Minimum Mapping Unit (MMU) and Minimum Mapping Width (MMW) thresholds. The background is a light yellow area representing the general land. A thin black line indicates an original, problematic boundary that likely contains small, isolated polygons or narrow artefacts falling below the MMU. At a vertex where the black line bends, a small white triangular area represents a 'spike' or an unresolvable geometric feature. A thicker cyan line overlays the black line, depicting the geometrically adjusted and topologically consistent boundary after refinement and buffering operations, resolving the MMU issue. The specific examples for such issues were identified in N2K terrestrial sites located in Finland and Germany. No scale bar, compass, or legend is visible in this highly localised view.](Protected_Areas_2021_PUM_v1-media/img-94fada3ae3ddd8f12483fe5dc32c9871.png)

Figure 16: Examples of bad snapping between N2000 terrestrial sites in Italy

**CLMS N2K21 status layer: example**

![This image displays three comparative maps and a common legend, illustrating different stages of Protected Area (PA) land cover classification for the year 2021, alongside Very High Resolution (VHR) false-colour imagery. The geographic area shown is centered around Lat: 47.812789, Lon: 16.653742 (near Parndorf, Austria). All maps share a scale bar showing 0, 0.5, and 1 km, with a ratio of 1:10.000, and include a north arrow. The three map panels are: 1. \*\*PA2021 L1-L4 TIF\*\*: This map shows a detailed land cover classification in a TIFF format, labeled as Protected Areas (PA) for 2021, representing classification levels 1 through 4. It features numerous small, intricate polygons. 2. \*\*PA2021 L4 GPKG\*\*: This map displays a more generalized land cover classification for Protected Areas (PA) in 2021, specifically level 4, stored in a GeoPackage (GPKG) format. Compared to the L1-L4 TIF map, polygons are larger and appear geometrically simplified, with fewer small linear features. 3. \*\*VHR False Colour 2021\*\*: This panel presents Very High Resolution satellite imagery from 2021 in false colour, showing the actual ground truth with visible agricultural fields, forest patches, and other land features, serving as a reference for the land cover classifications. The 'PA2021 Legend' below the maps lists 48 different numerical land cover class codes (e.g., 1110, 1120, 1210, 2110, 2120, 3110, 4110, 5100, 6100, 7110, 8110, 8310), each associated with a distinct colour. The specific land cover type descriptions corresponding to these numerical codes are not provided within the image. The comparison highlights how different classification levels and processing methods (e.g., aggregation for GPKG format) can impact the geometric representation of land cover, particularly in relation to the level of detail captured (like Minimum Mapping Unit coherence) when delineating Protected Areas and other land use/land cover features.](Protected_Areas_2021_PUM_v1-media/img-84fecdeade0e9a95beebde71864791ee.jpeg)

Figure 17: Examples of 2,5 m x 2,5 m LC/LU raster and final vector file in Geopackage (GPKG) format, as well as VHR 2021 False Colour

## 7.3 Product specifications

Table 5 summarizes the technical specifications of the N2K-PA products.

Table 5: Product overview sheet

[TABLE]

¹ Some exceptions are allowed for polygons at the product boundary and polygons inside the boundary related to linear networks or urban areas and for change polygons in very specific cases.

² Exceptions of 10m over a distance of up to 100m are allowed to maintain continuity of features with mostly linear nature.

The CLMS N2K-PA products are delivered as polygon vector data for the reference years over the selected sites across Europe. Each product is delivered as a separate data set, following a uniform technical specification. The content of a download package is explained below:

Each download package is a \*.zip file which contains three folders:

- **DATA** (contains the data files in gdb and geoPackage formats):

  - LC/LU status map 2006: LC/LU based on the analysis of satellite images from the reference year period 2006.
    - File name: N2K_2006_3035_v010
  - LC/LU status map 2012: LC/LU based on the analysis of satellite images from the reference year period 2012.
    - File name: N2K_2012_3035_v010
  - LC/LU status map 2018: LC and LU classification based on the analysis of satellite images from the reference year period 2018.
    - File name: N2K_2018_3035_v010
  - LC/LU change map 2006-2012: based on the outputs of the 2012 and 2006 status layers.
    - File name: N2K_Change_2006_2012_3035_v010
  - LC/LU change map 2012-2018: LC/LU change information based on the comparison of satellite images from the reference year periods 2012 and 2018. The production of this product is the basis for the status map for 2018 as well as for the revision of the previous time steps for 2012 and 2006.
    - File name: N2K_Change_2012_2018_3035_v010
  - **LC/LU status map 2021: LC and LU classification based on the analysis of satellite images from the reference year period 2021 for each BIOREGION.**
    - **File naming convention**: The file naming convention follows a standardized structure that encodes the service name, product type, reference year, delivery unit, biogeographical region, minimum mapping unit, geographical coverage, coordinate reference system, product and release versions, production date and file format. For example, CLMS_PA_LCU_S2021_DU0001_V05ha_EU27_03035_V01_R01_20260216.gpkg corresponds to the Protected Areas LC/LU status layer for 2021 in the Alpine region, delivered in GeoPackage format.
      - CLMS_PA_LCU_S2021_DU0001_V05ha_EU27_03035_V01_R01_20260216.gpkg.
      - CLMS_PA_LCU_S2021_DU0001_V05ha_EU27_03035_V01_R01_20260216.gdb.

- **SYMBOLOGY**: Contains symbology files in three formats: sld, lyr and qml.

- **METADATA**: Contains metadata file in XML format.

All products contain information on the LC/LU class as well as auxiliary information (e.g. on temporal dynamics of the mapped polygon or change related area size exceptions). The attribute information is given per polygon following a standardized attribution scheme (Table 6 and Table 7).

Table 6: Product attribute definition for the table LC_LU (ESRI GDB representation)

| Field | Description | Type | Value(s) | Applicable products |
|----|----|----|----|----|
| \[OBJECTID\] | Dynamic Feature Identifier | Object ID | 0 to 2.147.483.647 | Status, Change |
| \[Shape\] | Polygon | Geometry | Polygon | Status, Change |
| \[AREA_HA\] | Area in hectare \[ha\] | Double | 0.001 to 1.8E308 | Status, Change |
| \[UID\] | Unique Identifier of the feature geometry, generated as combination of Delivery Unit Code + OBJECTID in the form of “DU_OBJECTID” | String, Length 20 | Starting from 1_1 | Status, Change |
| \[CODE_1_21\] | Class code of LC/LU Level 1 for LC/LU 2018 | Long, Precision 9 | 1 to 10 | Status, Change |
| \[CODE_2_21\] | Class code of LC/LU Level 2 for LC/LU 2018 | Long, Precision 9 | 11 to 101 | Status, Change |
| \[CODE_3_21\] | Class code of LC/LU Level 3 for LC/LU 2018 | Long, Precision 9 | 111 to 1011 | Status, Change |
| \[CODE_4_21\] | Class code of LC/LU Level 4 for LC/LU 2018 | Long, Precision 9 | 1111 to 10111 | Status, Change |
| \[COMMENT_21\] | Comment field for additional information for LC/LU 2018 separated by Semicolon | String, Length 254 | Standardized text comments | Status |
| \[NODATA_21\] | Unclassifiable area due to clouds, shadows, snow, haze or missing data (no satellite data available) | Long, Precision 9 | 0,1 | Status, Change |
| \[du_id\] | Unique Identifier of Delivery Unit | String, Length 254 | Standardized text comments | Status |
| SHAPE_Length | Polygon perimeter in metres | Double | 0.001 to 1.8E308 | Status, Change |
| SHAPE_Area | Polygon area in m² | Double | 0.001 to 1.8E308 | Status, Change |

Table 7: Product attribute definition for the table LC_LU (GeoPackage .gpkg representation)

| Field | Description | Type | Value(s) | Applicable products |
|----|----|----|----|----|
| \[OBJECTID\] | Dynamic Feature Identifier | Object ID | 0 to 2.147.483.647 | Status, Change |
| \[Shape\] | Polygon | Geometry | Polygon | Status, Change |
| \[AREA_HA\] | Area in hectare \[ha\] | Double | 0.001 to 1.8E308 | Status, Change |
| \[UID\] | Unique Identifier of the feature geometry, generated as combination of Delivery Unit Code + OBJECTID in the form of “DU_OBJECTID” | String, Length 20 | Starting from 1_1 | Status, Change |
| \[CODE_1_21\] | Class code of LC/LU Level 1 for LC/LU 2018 | Long, Precision 9 | 1 to 10 | Status, Change |
| \[CODE_2_21\] | Class code of LC/LU Level 2 for LC/LU 2018 | Long, Precision 9 | 11 to 101 | Status, Change |
| \[CODE_3_21\] | Class code of LC/LU Level 3 for LC/LU 2018 | Long, Precision 9 | 111 to 1011 | Status, Change |
| \[CODE_4_21\] | Class code of LC/LU Level 4 for LC/LU 2018 | Long, Precision 9 | 1111 to 10111 | Status, Change |
| \[COMMENT_21\] | Comment field for additional information for LC/LU 2018 separated by Semicolon | String, Length 254 | Standardized text comments | Status |
| \[NODATA_21\] | Unclassifiable area due to clouds, shadows, snow, haze or missing data (no satellite data available) | Long, Precision 9 | 0,1 | Status, Change |
| \[du_id\] | Unique Identifier of Delivery Unit | String, Length 254 | Standardized text comments | Status |
| SHAPE_Length | Polygon perimeter in metres | Double | 0.001 to 1.8E308 | Status, Change |
| SHAPE_Area | Polygon area in m² | Double | 0.001 to 1.8E308 | Status, Change |

The standardized entries for \[COMMENT\] are separated by a semicolon in increasing order following their “Order No” (Table 8).

Table 8: List of allowed \[COMMENT\] entries

| Order No | Entry value | Description; Note | Applicable products |
|----|----|----|----|
| 1 | “Area size exception (at Natura2000 AoI boundary)“ | Polygons \< 0.5 ha at outer AoI site boundary, that have an apparent continuation outside the AoI boundary, which is visible on the image data. | Status, Change |
| 2 | “Area size exception (inside Natura2000 AoI boundary)“ | Polygons \< 0.5 ha inside AoI site boundary, that are allowed due to nomenclature guideline rules e.g. to represent changes, to ensure continuity of road/rail/river network at intersections of these classes, to mark urban objects confined by roads or railways ≥ 0.25 ha up to \< 0.5 ha | Status, Change |
| 3 | “Splitted change” | Changes over several classes. Each change is \< 0.5 ha but overall change (=sum of individual change areas) is \> 0.5 ha. | Change |
| 4 | “Areas related to change” | Polygons \< 0.5 ha with no change but connected to change polygons (same code at a neighbouring polygon in one of the two years) | Status |
| 5 | “Temporal fluctuation of water level” | Different water levels in comparison of image data taken during dry/wet season and conditions. The water level situation of the reference year 2012 should be used for delineation. A flood event is not considered as a “Temporal fluctuation of water level” | Status, Change |
| 6 | “Flooded area” | Used for extraordinary flooding events where non-water land cover features are covered (partly or fully) by water. Comment is applied only in the year of the flooding event. | Status, Change |
| 7 | “Braided River” | For river banks that are crossed by side arms of a river. Only valid for MAES_4 Code 6213 (river banks) | Status, Change |

### 7.3.1 CLMS PA Nomenclature

The Nomenclature for the LC/LU dataset is structured into four levels (Code level 1- Code level 4). There are 59 different LC/LU classes (Table 9). The detailed description of each class is given in the PA nomenclature and mapping guideline (AD01). The LC/LU code levels were designed to correspond to the Mapping and Assessment of Ecosystems and their Services (MAES) typology Level 2 (Maes et al., 2013).

Table 9: CLMS PA nomenclature overview (v1.4, dated 30.04.2026)

|  |  |  |  |  |
|----|----|----|----|----|
| Level 1 | Level 2 | Level 3 | Level 4 | MAES Level 2 |
| 1\. Urban | 1.1 Urban fabric, industrial, commercial, public, military and private units | 1.1.1 Urban fabric (predominantly public and private units) |  | URBAN |
|  |  | 1.1.2 Industrial, commercial and military units |  |  |
|  | 1.2 Transport infrastructure | 1.2.1 Road networks and associated land |  |  |
|  |  | 1.2.2 Railways and associated land |  |  |
|  |  | 1.2.3 Port areas and associated land |  |  |
|  |  | 1.2.4 Airports and associated land |  |  |
|  | 1.3 Mineral extraction, dump and construction sites, land without current use | 1.3.1 Mineral extraction sites, dump and construction sites |  |  |
|  |  | 1.3.2 Land without current use |  |  |
|  | 1.4 Green urban, sports and leisure facilities |  |  |  |
| 2\. Cropland | 2.1 Arable land | 2.1.1 Arable irrigated and non-irrigated land |  | CROPLAND |
|  |  | 2.1.2 Greenhouses |  |  |
|  | 2.2 Permanent crops | 2.2.1 Vineyards, fruit trees and berry plantations |  |  |
|  |  | 2.2.2 Olive groves |  |  |
|  | 2.3 Heterogeneous agricultural area | 2.3.1 Annual crops associated with permanent crops |  |  |
|  |  | 2.3.2 Complex cultivation patterns |  |  |
|  |  | 2.3.3 Land principally occupied by agriculture with significant areas of natural vegetation |  |  |
|  |  | 2.3.4 Agro-forestry |  |  |
| 3\. Woodland and forest | 3.1 Broadleaved forest | 3.1.1 Natural & semi-natural broadleaved forest |  | WOODLAND AND FOREST |
|  |  | 3.1.2 Highly artificial broadleaved plantations |  |  |
|  | 3.2 Coniferous forest | 3.2.1 Natural & semi-natural coniferous forest |  |  |
|  |  | 3.2.2 Highly artificial coniferous plantations |  |  |
|  | 3.3 Mixed forest | 3.3.1 Natural & semi-natural mixed forest |  |  |
|  |  | 3.3.2 Highly artificial mixed plantations |  |  |
|  | 3.4 Transitional woodland and scrub |  |  |  |
|  | 3.5 Lines of trees and scrub |  |  |  |
|  | 3.6 Damaged forest |  |  |  |
| 4\. Grassland | 4.1 Managed grassland |  |  | GRASSLAND |
|  | 4.2 Natural & semi-natural grassland | 4.2.1 Semi-natural grassland | 4.2.1.1 Semi-natural grassland with woody plants (C.C.D. ≥ 30 %) |  |
|  |  |  | 4.2.1.2 Semi-natural grassland without woody plants (C.C.D. \< 30%) |  |
|  |  | 4.2.2 Alpine and sub-alpine natural grassland |  |  |
| 5\. Heathland and scrub | 5.1 Heathland and moorland |  |  | HEATHLAND AND SCRUB |
|  | 5.2 Alpine scrub land |  |  |  |
|  | 5.3 Sclerophyllous scrubs |  |  |  |
| 6\. Open spaces with little or no vegetation | 6.1 Sparsely vegetated areas |  |  | SPARSELY VEGETATED |
|  | 6.2 Beaches, dunes, river banks | 6.2.1 Beaches and dunes |  |  |
|  |  | 6.2.2 River banks |  |  |
|  | 6.3 Bare rocks, burnt areas, glaciers and perpetual snow | 6.3.1 Bare rocks, outcrops, cliffs and scree | 6.3.1.1 Bare rocks, outcrops, cliffs |  |
|  |  |  | 6.3.1.2 Scree |  |
|  |  | 6.3.2 Burnt areas (except burnt forest) |  |  |
|  |  | 6.3.3 Glaciers and perpetual snow | 6.3.3.1 Glaciers |  |
|  |  |  | 6.3.3.2 Perpetual snow |  |
| 7\. Wetland | 7.1 Inland wetlands | 7.1.1 Inland marshes |  | WETLAND |
|  |  | 7.1.2 Peat bogs | 7.1.2.1 Exploited peat bogs |  |
|  |  |  | 7.1.2.2 Unexploited peat bogs |  |
|  | 7.2 Coastal wetlands | 7.2.1 Salt marshes |  | MARINE INLETS AND TRANSITIONAL WATERS |
|  |  | 7.2.2 Salines |  |  |
|  |  | 7.2.3 Intertidal flats |  |  |
| 8\. Water | 8.1 Water courses | 8.1.1 Natural & semi-natural water courses |  | RIVERS AND LAKES |
|  |  | 8.1.2 Highly modified water courses and canals |  |  |
|  |  | 8.1.3 Seasonally connected water courses (oxbows) |  |  |
|  | 8.2 Lakes and reservoirs | 8.2.1 Natural lakes |  |  |
|  |  | 8.2.2 Reservoirs |  |  |
|  |  | 8.2.3 Aquaculture ponds |  |  |
|  |  | 8.2.4 Standing water bodies of extractive industrial sites |  |  |
|  | 8.3 Transitional waters | 8.3.1 Lagoons |  | MARINE INLETS AND TRANSITIONAL WATERS |
|  |  | 8.3.2 Estuaries |  |  |
|  |  | 8.3.3 Marine inlets and fjords |  |  |
|  | 8.4 Sea and ocean | 8.4.1 Open sea |  | OPEN OCEAN |
|  |  | 8.4.2 Coastal waters |  | COASTAL |

# 8 Production methodology and workflow overview

The technical methodology underlying the CLMS Protected Areas products is described in detail in the **Algorithm Theoretical Basis Document (ATBD)** developed for the PA2021 production cycle (CLMS, 2026b). The ATBD provides a comprehensive description of the input datasets, processing chain, classification methodology, nomenclature implementation and post-processing procedures used for the generation of the products. The present section provides only a concise overview of the main methodological principles and workflow steps relevant to the users of the CLMS Protected Areas products. Detailed technical specifications and algorithmic aspects are available in the associated ATBD documentation. The CLMS N2K production is based on a **semiautomatic approach** (Figure 18).

![This diagram illustrates the Land Use / Land Cover (LULC) mapping workflow, specifically for generating a Copernicus Land Monitoring Service (CLMS) information product at a 50x50 km resolution, likely for the Protected Areas 2021 (PA2021) dataset covering Natura 2000 sites. The process integrates information at both the bioregional level and from Sentinel-2 (S2) satellite tiles, employing active learning and deep learning methodologies. The workflow begins with initial data inputs: 1. \*\*Tiles S2:\*\* Sentinel-2 imagery tiles covering Europe are used. 2. \*\*Bioregional level information:\*\* Environmental zoning data is incorporated from European bioregions. The core of the process involves an \*\*Active Learning\*\* module, which refines the model by interacting with data from two sources: \* 'Samples vs S2SR Time series per class': A line chart shows the temporal profiles of different land cover classes derived from Sentinel-2 Super Resolution (S2SR) time series. \* 'Samples vs model uncertainty': A bar chart displays the distribution of model uncertainty across samples. The Active Learning module feeds into the 'Model training and data production' phase, influencing the training dataset and deep learning model. A feedback loop from the final 'Information product at 50x50kms' back to Active Learning suggests iterative refinement. The \*\*Model training and data production\*\* phase consists of three steps: 1. \*\*Sentinel-2 Super Resolution Time Series Predictors:\*\* Time series data derived from Sentinel-2 imagery are used as predictors. 2. \*\*Training dataset:\*\* A training dataset, comprising geolocated samples (shown as coloured points on a map of Europe), is prepared. This step is influenced by the Active Learning module. 3. \*\*Deep Learning Model Training:\*\* A deep learning model is trained iteratively. The visible code snippet shows a training loop with \`loss = model(inputs, labels)\`, \`loss.backward()\`, and \`optimizer.step()\`, indicating an optimization process over epochs. Following model training, the \*\*Mapping production and refinement\*\* phase proceeds: 1. \*\*Predictions:\*\* Initial LULC predictions are generated across Europe (depicted as a classified map). 2. \*\*Post-processing:\*\* The predictions undergo a post-processing step to refine the classification. 3. \*\*Manual refinement:\*\* Further manual refinement is performed on the post-processed data, including a detailed visual inspection at a finer grid level. The output is an \*\*Information product at 50x50kms\*\*, which is generated using 'Working units' (a satellite image overlaid with a grid of 50x50 km cells, with a zoomed-in section showing individual pixels/grid cells). This product adheres to a new LULC nomenclature, 'L3_fusion', comprising 16 classes: \* \*\*Urban fabric:\*\* 110 (Continuous urban fabric), 120 (Discontinuous urban fabric) \* \*\*Cropland:\*\* 210 (Arable land), 220 (Permanent crops), 230 (Pastures) \* \*\*Forest:\*\* 310 (Broadleaved forest), 320 (Coniferous forest), 330 (Mixed forest) \* \*\*Grassland:\*\* 410 (Natural grassland) \* \*\*Shrubland:\*\* 420 (Moors and heathland) \* \*\*Wetland:\*\* 510 (Inland wetlands), 520 (Peatbogs) \* \*\*Water:\*\* 610 (Inland waters), 620 (Marine waters) \* \*\*Bare / sparse:\*\* 710 (Bare rock), 720 (Sparsely vegetated areas) \* \*\*Snow and ice:\*\* 810 (Permanent snow and ice)](Protected_Areas_2021_PUM_v1-media/img-3058833c9b82e13361c3e862fa8faa27.jpeg)

Figure 18: Production workflow for CLMS PA2021 product

## 8.1 Data pre-processing

The production of the CLMS Protected Areas products relies primarily on multi-temporal Sentinel-2 Level-2A imagery. Cloud-free seasonal mosaics are generated for each biogeographical region in order to maximize the spectral and temporal information available for land cover and land use characterization. To enhance the spatial detail while preserving the spectral consistency of Sentinel-2 observations, the imagery is processed using COTESA’s super-resolution approach, resulting in **super-resolved Sentinel-2 (S2SR) time series**. Multi-temporal coregistration and quality control procedures are subsequently applied to ensure geometric consistency and to remove suboptimal observations affected by clouds, haze, snow or other artefacts.

In addition to Sentinel-2 imagery, several CLMS products and ancillary datasets are integrated into the workflow to support classification and improve thematic consistency. These include the previous Natura 2000 layers, Coastal Zones, Riparian Zones, High Resolution Layers, CLCPlus Backbone, EU-Hydro, the European Wetland Map and OpenStreetMap data, among others. These complementary sources provide thematic support for specific classes and contribute to the harmonization with other Copernicus Land Monitoring Service products.

The ESA VHR_IMAGE_2021 collection consists of cloud-free orthorectified mosaics derived from multiple commercial Very High Resolution satellite missions acquired around the 2021 reference period. The collection provides multispectral information in the visible and near-infrared bands at spatial resolutions ranging from 1 to 4 m. Within the CLMS Protected Areas workflow, VHR imagery is primarily used as a reference source for manual refinement and quality control activities. Additional CLMS products and ancillary datasets are integrated into the production workflow to improve thematic consistency and support the land cover and land use analysis.

The satellite data provided via these ESA data sources include different sensor types:

- Deimos-02
- Geosat-02
- Vision-01
- SPOT-6
- GeoEye 01
- SPOT-7
- Superview.1
- SuperView-1
- Kompsat 03/04
- TripleSat
- Pleiades 1A
- WorldView 2
- Pleiades 1B
- WorldView 3

Additional ancillary information and online image services are used whenever necessary to support the interpretation process and resolve ambiguous situations during manual refinement. The combination of super-resolved Sentinel-2 time series, CLMS reference datasets and VHR imagery enable the generation of harmonized, high-resolution land cover and land use products for all terrestrial Natura 2000 sites.

## 8.2 Interpretation and classification

The Interpretation and Classification procedures follow the mapping rules and principles as stated in the CLMS N2K Nomenclature and Mapping Guideline (AD01; Issue 1.4, 30 April 2026; CLMS, 2026a). This documentation refers specifically to object delineation; MMU and MMW; feature extraction priority rules; water level mapping rules; handling of geometric inconsistencies between the reference years; inclusion of additional data sources and the application of standardized data attributes. Feature delineation is applied at a 1:10.000 mapping scale.

**Mapping LC/LU Status** The LC/LU status is generated through manual refinement (by using ESA_VHR_2021) on an automatic pipeline that heavily relies on the super-resolved Sentinel-2 temporal series and Copernicus curated data feeding Deep Learning models, as well as advanced post-processing techniques. The type of LC/LU is classified according to the CLMS N2K Nomenclature and Mapping Guideline document (AD01). A minimum mapping unit (MMU) of ≥ 0.5 ha for all objects applies. A minimum width (MMW) of ≥ 10 m is defined. MMU exceptions are allowed for:

- Objects located at a CLMS N2K product border: If an object is cut at a border, the feature is mapped, if the whole object (inside and outside the border) would amount to ≥ 0.5 ha. However, the MMU of those divided features lying inside the site shall have a MMU of at least ≥ 0.1 ha. Smaller objects will be generalized.
- Linear features (roads, railways, rivers) that are split in two or more polygons by other linear elements (e.g. the road/railway network) will be mapped even if the resulting segments are smaller than the MMU to preserve the network. However, features \< 0.1 ha will be generalized.
- Urban objects which are confined by roads or railways. Features \< 0.25 ha will be generalized.

MMW exceptions are allowed:

- To maintain continuity of features with mostly linear nature — Road networks and associated land (1.2.1), Railways and associated land (1.2.2), Beaches and dunes (6.2.1), Riverbanks (6.2.2), Natural & semi-natural water courses (8.1.1), and highly modified water courses and canals (8.1.2) — the MMW may fall below the limit of 10 m over a distance of up to 100 m.

## 8.3 Quality assessment

The quality assessment methodology and the quality control procedures implemented for the CLMS Protected Areas products are described in detail in the Protected Areas LC/LU 2021 status product - Final Validation Report (Hugé & Pennec, 2026). The present section provides only an overview of the approach followed for quality assurance and thematic validation, together with the main accuracy requirements and key validation results. Detailed descriptions of the validation methodology, sampling design, statistical analysis and complete accuracy assessment results are available in the dedicated quality assessment documentation.

### 8.3.1 Internal thematic validation

For each Protected Areas (PA) LC/LU product, a thematic validation is performed to assess the thematic accuracy of the status and change layers. The assessment is based on a scientifically and statistically sound sampling scheme and independent interpretation procedures.

The following accuracy requirements apply to the products:

- PA LC/LU status layers 2021 and 2024: ≥ 85% overall accuracy and ≥ 80% for class-specific producer’s and user’s accuracy.
- PA LC/LU change layer 2021–2024: ≥ 85% overall accuracy and ≥ 80% for class-specific producer’s and user’s accuracies.

#### 8.3.1.1 Sampling Design

The thematic accuracy assessment is based on a random systematic and stratified sampling design, ensuring that all areas within the product extent have a known and non-zero probability of being selected. The validation is performed at Level 1 of the nomenclature, which comprises the eight major land cover and land use classes defined for the Protected Areas products.

The sampling approach combines randomization and stratification principles in order to provide statistically robust estimates of overall and class-specific accuracies at pan-European level. Stratification is used to ensure a balanced representation of the different Level 1 classes and to improve the efficiency of the accuracy estimates, particularly for classes occupying relatively small proportions of the total area.

The sampling framework is based on the LUCAS (Land Use/Cover Area Frame Statistical Survey) grid, which provides a harmonised and spatially distributed reference across Europe. A replicate and sub-replicate strategy is adopted to guarantee a homogeneous spatial distribution of samples over the entire area of interest and to avoid concentration of observations in specific regions. Sample allocation is designed to ensure adequate representation of all thematic classes while maintaining statistical rigour and geographical consistency.

The resulting sample set provides sufficient coverage of the Protected Areas domain and supports the derivation of unbiased estimates of overall accuracy as well as class-specific producer’s and user’s accuracies. The methodology follows internationally recognised recommendations for thematic accuracy assessment and allows the quality of the products to be evaluated consistently at the pan-European scale.

#### 8.3.1.2 Response Design

All sample units are independently interpreted by experienced operators who are not involved in the production process. The interpretation is based on Very High Resolution (VHR) imagery and ancillary reference data and follows the applicable nomenclature and mapping guidelines.

The response design consists of a two-stage process:

- An initial blind interpretation, during which the validation team has no knowledge of the thematic class assigned in the product. Product polygons are nevertheless provided to account for boundary effects and geometric discrepancies.
- A plausibility analysis applied to all sample units showing disagreement with the production data, allowing ambiguous situations to be reviewed and ensuring consistency of the assessment.

#### 8.3.1.3 Validation results

The thematic accuracy indicators are derived from weighted confusion matrices and include overall accuracy, producer’s accuracy, user’s accuracy and F-score.

For the Protected Areas LC/LU 2021 status layer, the overall thematic accuracy reaches 89.63% ± 0.30%, thus fulfilling the target overall accuracy requirement of 85%. Most Level 1 classes satisfy the target values of 80% for producer’s and user’s accuracies. Detailed class-specific results are documented in the corresponding validation reports.

Full details on the validation methodology, sampling design, confusion matrices, producer’s and user’s accuracies, confidence intervals and class-specific results are provided in the **Final Validation Report** (Hugé & Pennec, 2026).

Table 10: Number of weighted points per class, as well as CI, omission, producer and user accuracy. Also, overall accuracy is shown

![The table presents a thematic accuracy assessment for eight Land Cover / Land Use (LULC) classes, designated as Class 1 through Class 8, likely corresponding to Level 1 of the nomenclature for Protected Areas products. The primary section is a confusion matrix comparing MAP classifications (rows) against REFERENCE classifications (columns). Values represent quantities (e.g., area or sample points) in an unspecified unit, showing correctly classified instances on the diagonal (highlighted). The total quantity across all reference classes is 36994.0. / MAP Class Reference Class / Class 1 / Class 2 / Class 3 / Class 4 / Class 5 / Class 6 / Class 7 / Class 8 / Total (MAP) / /---/---/---/---/---/---/---/---/---/---/ / Class 1 / 536.8 / 3.0 / 24.2 / 19.7 / 7.9 / 3.0 / 1.0 / - / 595.6 / / Class 2 / 25.9 / 3394.4 / 218.2 / 462.5 / 110.6 / 5.0 / 7.0 / 1.0 / 4224.6 / / Class 3 / 30.9 / 32.9 / 16305.3 / 65.8 / 168.5 / 6.0 / 35.9 / 8.0 / 16653.2 / / Class 4 / 73.3 / 254.5 / 287.2 / 5625.4 / 337.7 / 56.4 / 131.7 / 7.9 / 6774.3 / / Class 5 / 12.0 / 50.9 / 284.3 / 255.4 / 2990.0 / 71.8 / 9.0 / 3.0 / 3676.3 / / Class 6 / 1.1 / 12.3 / 24.5 / 71.8 / 94.1 / 1160.7 / 4.5 / 1.1 / 1370.2 / / Class 7 / 3.0 / 2.0 / 55.7 / 135.7 / 266.4 / 14.2 / 1225.6 / 35.4 / 1738.2 / / Class 8 / 5.0 / - / 9.9 / 6.0 / 5.0 / 4.0 / 11.9 / 1920.0 / 1961.8 / / Total (Reference) / 688.0 / 3750.1 / 17209.4 / 6642.3 / 3980.1 / 1321.1 / 1426.6 / 1976.4 / 36994.0 / The table also provides class-specific and overall accuracy metrics with 95% Confidence Intervals (CI95%): / Class / Producer Accuracy (Prod θ) / Omission Error / CI95% (Producer) / User Accuracy (User λ) / Commission Error (Com.) / CI95% (User) / /---/---/---/---/---/---/---/ / Class 1 / 78.02% / 21.98% / 2.75% / 90.13% / 9.87% / 2.37% / / Class 2 / 90.52% / 9.48% / 0.89% / 80.35% / 19.65% / 1.20% / / Class 3 / 94.75% / 5.25% / 0.32% / 97.91% / 2.09% / 0.22% / / Class 4 / 84.69% / 15.31% / 0.78% / 83.04% / 16.96% / 0.89% / / Class 5 / 75.12% / 24.88% / 1.16% / 81.33% / 18.67% / 1.26% / / Class 6 / 87.86% / 12.14% / 1.66% / 84.72% / 15.28% / 2.01% / / Class 7 / 85.91% / 14.09% / 1.70% / 70.51% / 29.49% / 2.16% / / Class 8 / 97.14% / 2.86% / 0.72% / 97.87% / 2.13% / 0.64% / Overall Accuracy (OA): 89.63% (CI95%: 0.30%) Producer accuracy (Prod θ) indicates how much of each real-world land cover class was correctly detected; User accuracy (User λ) indicates how reliable each classified pixel is; Omission error is the proportion of real features missed; Commission error is the proportion of false detections; CI95% represents the 95% confidence interval for the accuracy estimate. The overall accuracy for the product is 89.63%. Class 3 exhibits the highest User Accuracy (97.91%) and Producer Accuracy (94.75%) with the lowest Omission and Commission errors, while Class 7 has the lowest User Accuracy (70.51%) and highest Commission Error (29.49%), and Class 5 has the lowest Producer Accuracy (75.12%) and highest Omission Error (24.88%).](Protected_Areas_2021_PUM_v1-media/img-1bnyf9792943d4b609sd0bb2gfu774e9.png)

C1–C8 are the Level 1 class codes (class names are given in Table 11). Overall accuracy is 89.63% (CI95% ± 0.30%).

Table 11: Validation statistics (producer and user accuracy, CI95% and F-score per class at L1)

| Class code | Class name | Prod. accuracy | CI95% | User accuracy | CI95% | F-score |
|----|----|----|----|----|----|----|
| 1 | Urban | 78.02% | 2.75% | 90.13% | 2.37% | 0.84 |
| 2 | Cropland | 90.52% | 0.89% | 80.35% | 1.20% | 0.85 |
| 3 | Woodland and forest | 94.75% | 0.32% | 97.91% | 0.22% | 0.96 |
| 4 | Grassland | 84.69% | 0.78% | 83.04% | 0.89% | 0.84 |
| 5 | Heathland and scrub | 75.12% | 1.16% | 81.33% | 1.26% | 0.78 |
| 6 | Open spaces with little or no vegetation | 87.86% | 1.66% | 84.72% | 2.01% | 0.86 |
| 7 | Wetland | 85.91% | 1.70% | 70.51% | 2.16% | 0.77 |
| 8 | Water | 97.14% | 0.72% | 97.87% | 0.64% | 0.98 |

### 8.3.2 Quality Assurance (QA) and Quality Control (QC) measures

All CLMS Protected Areas products are produced by service providers operating under ISO 9001:2015 certified quality management systems. Quality assurance and quality control procedures are implemented throughout the production workflow to ensure that the products comply with the technical specifications and quality requirements defined for the service.

Continuous quality checks are carried out during data preparation, image interpretation, mapping and post-processing stages. These controls address data integrity and readability, thematic and geometric consistency, logical and topological consistency, attribute coding, completeness of the geographical coverage, metadata completeness and compliance with the Infrastructure for Spatial Information in the European Community (INSPIRE) implementing rules and the EIONET Action Group on Land Monitoring in Europe (EAGLE) data model. Additional checks are performed to verify the quality and suitability of the Earth Observation input data, including radiometric quality and the presence of clouds, haze, shadows, snow or other data gaps.

Besides the internal QA/QC procedures performed by the production teams, the products are subject to an independent thematic validation process based on statistically sound sampling and expert image interpretation. Validation activities are carried out separately from production and provide quantitative estimates of overall producer’s and user’s accuracies.

Finally, all CLMS Protected Areas products undergo a final quality control and approval process using the [EEA Copernicus Quality Tools](https://github.com/eea/copernicus_quality_tools), a web-based platform developed to support the quality assessment and acceptance of geospatial products submitted to the European Environment Agency.

### 8.3.3 External independent validation

The objective of the external independent validation is to provide quantitative information on the thematic quality of the CLMS Protected Areas products and to assess their compliance with the target accuracy requirements.

The external validation process is based on independent reference information and is performed separately from the production activities to ensure an objective assessment of the datasets. Reference data should be as close as possible in time to the imagery used to produce the products and must be fully independent from the information used during the mapping process. Likewise, the experts involved in the validation activities are independent from the production teams.

Within the CLMS Protected Areas framework, external validation refers to thematic validation. At the time of writing this document, the external independent validation has not yet been performed. The corresponding methodology and results will be documented in dedicated validation reports once available.

# 9 Terms of use and product technical support

## 9.1 Terms of use

The product(s) described in this document is/are created in the frame of the Copernicus programme of the European Union by the European Environment Agency (product custodian) and is/are owned by the European Union. The product(s) can be used following Copernicus full free and open data policy, which allows the use of the product(s) also for any commercial purpose. Derived products created by end users from the product(s) described in this document are owned by the end users, who have all intellectual rights to the derived products.

## 9.2 Citation

In cases of re-dissemination of the product(s) described in this document or when the product(s) is/are used to create a derived product it is required to provide a reference to the source. A template is provided below:

“© European Union, Copernicus Land Monitoring Service 2026, European Environment Agency (ΕΕΑ)”

## 9.3 Product technical support

Product technical support is provided by the product custodian through Copernicus Land Monitoring Service helpdesk at copernicus@eea.europa.eu. Product technical support doesn’t include software specific user support or general GIS or remote sensing support.

# 10 List of abbreviations and acronyms

| Abbreviation | Meaning |
|----|----|
| AD | Applicable Document |
| AoI | Area of Interest |
| ATBD | Algorithm Theoretical Basis Document |
| CLC | CORINE Land Cover |
| CLMS | Copernicus Land Monitoring Service |
| CZ | Coastal Zones |
| DB | Database |
| DG ENV | Directorate-General for Environment |
| EAGLE | EIONET Action Group on Land Monitoring in Europe |
| EC | European Commission |
| EEA | European Environment Agency |
| EPSG | European Petroleum Survey Group coordinate reference system codes |
| ESRI | Environmental Systems Research Institute |
| EU | European Union |
| EU27 | European Union 27 Member States |
| GIO | GMES Initial Operations |
| GIS | Geographic Information System |
| GMES | Global Monitoring for Environment and Security |
| GPKG | GeoPackage |
| INSPIRE | Infrastructure for Spatial Information in the European Community |
| KCEO | Knowledge Centre on Earth Observation |
| LC/LU | Land Cover / Land Use |
| MAES | Mapping and Assessment of Ecosystems and their Services |
| MMU | Minimum Mapping Unit |
| MMW | Minimum Mapping Width |
| N2K | Natura 2000 |
| N2K18 | Natura 2000 2018 |
| N2000 | Natura 2000 |
| PA | Protected Areas |
| PSIL | Parent Scene Identification Layer |
| QA | Quality Assurance |
| QC | Quality Control |
| RMSE | Root Mean Square Error |
| RZ | Riparian Zones |
| S2SR | Super-resolved Sentinel-2 |
| VHR | Very High Resolution |

# 11 References

Camia, A., Dowell, M., & Vancutsem, C. (2024). Earth Observation for Biodiversity. Gliottone, I., & Bertoglio, C. (Eds.). European Commission, Joint Research Centre, Ispra. JRC135083.

Copernicus Land Monitoring Service (CLMS). (2026). CLMS Protected Areas Nomenclature and Mapping Guideline, Issue 1.4, 30 April 2026. European Environment Agency. Unpublished project document.

Copernicus Land Monitoring Service (CLMS). (2026). Copernicus Land Monitoring Service – Priority Area Monitoring: – Protected Areas Status 2021: Algorithm Theoretical Basis Document (ATBD), Version 2.1. European Environment Agency.

European Commission. (2019). Commission Staff Working Document: Expression of User Needs for the Copernicus Programme. SWD(2019) 394 final. European Commission.

European Commission. (2020). EU Biodiversity Strategy for 2030: Bringing nature back into our lives. COM(2020) 380 final. European Commission.

Maes, J., Teller, A., & Erhard, M. (Eds.). (2013). Mapping and Assessment of Ecosystems and their Services: An analytical framework for ecosystem assessments under Action 5 of the EU Biodiversity Strategy to 2020. Publications Office of the European Union. JRC81328.

Hugé, J., & Pennec, A. (2026). Protected Areas LC/LU 2021 status product – Final Validation Report, Version 2.0. Copernicus Land Monitoring Services: Priority Area Monitoring – Protected Areas 2021 and 2024. Service contract EEA/DIS/R0/23/009. European Environment Agency. Unpublished project document.

# 12 Change Log

| Date | Version | Summary |
|----|----|----|
| 2026-11-10 | 1.1.0 | Initial release of the 'Protected Areas 2021 - Product User Manual (PUM)' document, offering a non-technical and executive summary, product lineage, user requirements, application areas, and detailed product specifications for the 2021 Protected Areas product. |

Back to top

## Reuse

EUPL (\>= 1.2)
