# Final Delivery Report

D3.2

This document serves as an internal Quality Control and Quality Assurance Delivery Report for the Copernicus Land Monitoring Service’s Coastal Zones Land Cover/Land Use (CZ LCLU) dataset, covering reference years 2012 and 2018. It details product specifications, including a 71-class nomenclature, mapped area statistics, and the Very High Resolution (VHR) satellite imagery used. The report comprehensively outlines the production methodology, which combines automatic classification and visual interpretation, alongside presenting a rigorous quantitative accuracy assessment of the status and change maps for the EEA39 coastal areas.

Published

February 10, 2021

Keywords

Coastal Zones Land Cover/Land Use (CZ LCLU), Very High Resolution (VHR) satellite imagery, Land cover change map 2012-2018, Thematic accuracy assessment, Quantitative quality assessment, Stratified random point sampling, Coastal zones nomenclature, ETRS89 Lambert Azimuthal Equal Area (LAEA) projection, Minimum mapping unit 0.5 ha, Geometric skeleton integration, Copernicus Land Monitoring Service (CLMS)

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

Document History

|                 |                    |            |               |
|-----------------|--------------------|------------|---------------|
| List of reviews |                    |            |               |
| Version         | Author             | Date       | Note          |
| v0              | CZ Production Team | 10/02/2021 | First release |

# 1 Introduction

## 1.1 Purpose and scope

This document represents the Internal final QC/QA Delivery Report referring to the Coastal Zones products covering the 100% of the AOI to be mapped within the framework of the SPECIFIC CONTRACTS No 3436/RO-COPERNICUS/EEA.57850 and No 3436/RO-COPERNICUS/EEA.58088, both implementing Framework service contract No EEA/DIS/R0/18/008 – Production of Very High Resolution Land Cover/Land Use dataset for coastal zones of the reference years 2012 and 2018.

This Delivery Report includes the following key information about the final delivery:

- Product specifications (including keynotes about the production process and used source files)
- Quantitative assessment of LCLU delivered data
- Delivered files

## 1.2 Applicable documents

| Ref. | Tile |
|----|----|
| \[AD.1\] | Tender Specifications “EEA/DIS/R0/18/008 Framework service contract for Copernicus Local Land Monitoring Services – Production of Very High Resolution Land Cover/Land Use dataset for coastal zones of the reference years 2012 and 2018” |
| \[AD.2\] | Proposal responding to EEA’S Invitation for Tender (pkz008-429-1.0_EEA_LC_Coastal_Zone_Technical_Proposal) |
| \[AD.3\] | Framework Service Contract EEA/DIS/RO/18/008 |
| \[AD.4\] | SPECIFIC CONTRACT No 3436/RO-COPERNICUS/EEA.57850 |
| \[AD.5\] | SPECIFIC CONTRACT No 3436/RO-COPERNICUS/EEA.58088 |

## 1.3 Reference documents

| Ref. | Tile |
|----|----|
| \[RD.1\] | Footprints for VHR2012 data (pkz048-47-1.0 – D4.1) |
| \[RD.2\] | Assessment report on the availability of VHR2012 data (pkz048-37-1.1 – D4.2) |
| \[RD.3\] | Preliminary Coastal Zones AOI 2018 (pkz048-43-1.0 – D5.1) |
| \[RD.4\] | Final Coastal Zones AOI 2018 (pkz048-65-1.2 - D5.2) |
| \[RD.5\] | Final mapping guidelines (pkz048-66-v2 – D6.2) |
| \[RD.6\] | <https://github.com/eea/copernicus_quality_tools/wiki/Coastal-Zones-2012#vectornaming> |
| \[RD.7\] | <https://github.com/eea/copernicus_quality_tools/wiki/Coastal-Zones-2018#vectornaming> |
| \[RD.8\] | <https://github.com/eea/copernicus_quality_tools/wiki/Coastal-Zones-Change-2012-2018#vectornaming> |
| \[RD.9\] | Data Warehouse phase 2 DAP v2.5 <https://spacedata.copernicus.eu/documents/12833/14545/DAP+Document+-+current/c2449218-3ed9-434a-b32c-edfbb95b9362> |
| \[RD.10\] | GMES Space Component Data Access Portfolio: Data Warehouse 2011-2014 <https://spacedata.copernicus.eu/documents/12833/14553/DAP_Document_DWH_V2.8_27122013.pdf> |

# 2 Product specifications

The Coastal Zones products provide a detailed Land Cover/Land Use dataset for the coastal zones of the EEA39. The mapped coastal zones are delimited by the CLC boundaries on the seaward side and include an adapted 10 km wide strip on landward side, including specific areas under clear coastal influence or being clearly relevant for coastal zones even if reaching further than 10 km landwards.

The CZ LC/LU product includes three complementary layers:

1.  LC/LU status map for the reference year 2012.
2.  LC/LU status map for the reference year 2018.
3.  LC/LU change map 2012-2018 derived from and fully consistent with 1) and 2) to characterize the evolution of the coastal zones over time.

Product specifications of each layer are described in the following three tables.

Table 1: Coastal Zones Land Cover and Land Use status map 2012

[TABLE]

Table 2: Coastal Zones Land Cover and Land Use status map 2018

[TABLE]

Table 3: Coastal Zones Land Cover and Land Use change map 2012-2018

[TABLE]

## 2.1 Nomenclature

The Coastal Zones LC/LU layer differentiates 71 thematic LC/LU classes. In line with the other thematic hotspot products, the CZ nomenclature is designed to address the MAES classes at level 2.0.

Table 4 describes the CZ nomenclature and how CZ classes shall be aggregated to map MAES at level 2. More details about the CZ nomenclature can be found in \[RD.5\].

Table 4: Detailed CZ LC/LU classes and cross reference to MAES Level 2

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Ecosystem types level 2 (MAES) |
| 1 Urban | 1.1 Urban fabric, industrial, commercial, public, military and private units | 1.1.1 Urban fabric (predominantly public and private units) | 1.1.1.1 Continuous urban fabric (IMD ≥80%) |  | Urban |
|  |  |  | 1.1.1.2 Dense urban fabric (IMD ≥30-80%) |  |  |
|  |  |  | 1.1.1.3 Low density fabric (IMD \<30%) |  |  |
|  |  | 1.1.2 Industrial, commercial, public and military units | 1.1.2.1 Industrial, commercial, public and military units (other) |  |  |
|  |  |  | 1.1.2.2 Nuclear energy plants and associated land |  |  |
|  | 1.2 Transport infrastructure | 1.2.1 Road networks and associated land |  |  |  |
|  |  | 1.2.2 Railways and associated land |  |  |  |
|  |  | 1.2.3 Port areas and associated land | 1.2.3.1 Cargo port |  |  |
|  |  |  | 1.2.3.2 Passenger port |  |  |
|  |  |  | 1.2.3.3 Fishing port |  |  |
|  |  |  | 1.2.3.4 Naval port |  |  |
|  |  |  | 1.2.3.5 Marinas |  |  |
|  |  |  | 1.2.3.6 Local multi-functional harbours |  |  |
|  |  |  | 1.2.3.7 Shipyards |  |  |
|  |  | 1.2.4 Airports and associated land |  |  |  |
|  | 1.3 Mineral extraction, dump and construction sites, land without current use | 1.3.1 Mineral extraction, dump and construction sites | 1.3.1.1 Mineral extraction sites |  |  |
|  |  |  | 1.3.1.2 Dump sites |  |  |
|  |  |  | 1.3.1.3 Construction sites |  |  |
|  |  | 1.3.2 Land without current use |  |  |  |
|  | 1.4 Green urban, sports and leisure facilities |  |  |  |  |
| 2 Cropland | 2.1 Arable land | 2.1.1 Arable irrigated and non-irrigated land |  |  | Cropland |
|  |  | 2.1.2 Greenhouses |  |  |  |
|  | 2.2 Permanent crops | 2.2.1 Vineyards, fruit trees and berry plantations |  |  |  |
|  |  | 2.2.2 Olive groves |  |  |  |
|  | 2.3 Heterogeneous agricultural area | 2.3.1 Annual crops associated with permanent crops |  |  |  |
|  |  | 2.3.2 Complex cultivation patterns |  |  |  |
|  |  | 2.3.3 Land principally occupied by agriculture with significant areas of natural vegetation |  |  |  |
|  |  | 2.3.4 Agro-forestry |  |  |  |
| 3 Woodland and forest | 3.1 Broadleaved forest | 3.1.1 Natural & semi-natural broadleaved forest |  |  | Woodland and forest |
|  |  | 3.1.2 Highly artificial broadleaved plantations |  |  |  |
|  | 3.2 Coniferous forest | 3.2.1 Natural & semi-natural coniferous forest |  |  |  |
|  |  | 3.2.2 Highly artificial coniferous plantations |  |  |  |
|  | 3.3 Mixed forest | 3.3.1 Natural & semi-natural mixed forest |  |  |  |
|  |  | 3.3.2 Highly artificial mixed plantations |  |  |  |
|  | 3.4 Transitional woodland and scrub |  |  |  |  |
|  | 3.5 Lines of trees and scrub |  |  |  |  |
|  | 3.6 Damaged forest |  |  |  |  |
| 4 Grassland | 4.1 Managed grassland |  |  |  | Grassland |
|  | 4.2 Natural & semi-natural grassland | 4.2.1 Semi-natural grassland |  |  |  |
|  |  |  | alpine natural grassland |  |  |
| 5 Heathland and scrub | 5.1 Heathland and moorland |  |  |  | Heathland and shrub |
|  | 5.2 Alpine scrub land |  |  |  |  |
|  | 5.3 Sclerophyllous scrubs |  |  |  |  |
| 6 Open spaces with little or no vegetation | 6.1 Sparsely vegetated areas | 6.1.1 Sparse vegetation on sands |  |  | Sparsely vegetated land |
|  |  | 6.1.2 Sparse vegetation on rocks |  |  |  |
|  | 6.2 Beaches, dunes, river banks | 6.2.1 Beaches and dunes | 6.2.1.1 Beaches | 6.2.1.1.1 Sandy beaches |  |
|  |  |  |  | 6.2.1.1.2 Shingle beaches |  |
|  |  |  | 6.2.1.2 Dunes |  |  |
|  |  | 6.2.2 River banks |  |  |  |
|  | 6.3 Bare rocks, burnt areas, glaciers and perpetual snow | 6.3.1 Bare rocks, outcrops, cliffs | 6.3.1.1 Bare rocks and outcrops |  |  |
|  |  |  | 6.3.1.2 Coastal cliffs |  |  |
|  |  | 6.3.2 Burnt areas (except burnt forest) |  |  |  |
|  |  | 6.3.3 Glaciers and perpetual snow |  |  |  |
| 7 Wetland | 7.1 Inland wetlands | 7.1.1 Inland marshes |  |  | Wetlands |
|  |  | 7.1.2 Peat bogs | 7.1.2.1 Exploited peat bogs |  |  |
|  | 7.2 Coastal wetlands |  | 7.1.2.2 Unexploited peat bogs |  |  |
| 8 Water |  | 7.2.1 Salt marshes |  |  | Marine inlets and transitional waters |
|  |  | 7.2.2 Salines |  |  |  |
|  | 8.1 Water courses | 7.2.3 Intertidal flats |  |  |  |
|  |  | 8.1.1 Natural & semi-natural water courses |  |  |  |
|  |  | 8.1.2 Highly modified water courses and canals |  |  |  |
|  | 8.2 Lakes and reservoirs | 8.1.3 Seasonally connected water courses (oxbows) |  |  | Rivers and lakes |
|  |  | 8.2.1 Natural lakes |  |  |  |
|  |  | 8.2.2 Reservoirs |  |  |  |
|  |  | 8.2.3 Aquaculture ponds |  |  |  |
|  | 8.3 Transitional waters | 8.2.4 Standing water bodies of extractive industrial sites |  |  | Marine inlets and transitional waters |
|  |  | 8.3.1 Lagoons |  |  |  |
|  |  | 8.3.2 Estuaries |  |  |  |
| 8.4 Sea and ocean | 8.3.3 Marine inlets and fjords |  |  | Open ocean Coastal |  |
|  | 8.4.1 Open sea |  |  |  |  |

A recoding rule table from 4th to 5th class level has been agreed with EEA and applied to all the CZ mapping products in order to maximize coherence between CZ and N2k nomenclatures (See Appendix A). For the same reason, compared to the previous deliveries, in this final delivery the LC/LU classes 8.3.2.0 – “Marine inlets and fjords” and 8.3.3.0 – “Estuaries” have been switched (in the previous deliveries the LC/U class 8.3.2.0 was “Estuaries” and the LC/LU class 8.3.3.0 was “Marine inlets and fjords”).

## 2.2 Overview of mapped area

The entire mapped area (100% of the AOI) totals 2.229.478 km², including the marine and ocean LCLU classes: 84100 - Open sea and 84200 - Coastal waters.

In terms of only land mapped area¹ the size of the AOI is: 723.518 km² (for status layer 2018).

Compared to the 719.844,2 km² defined in SC2 + SC3 (and spatially defined in \[RD.4\]), the final AOI includes additional 3.673 km². The additional km² originates from a more detailed mapping of the LCLU class 72300 - Intertidal flats and, to a minimal extent, from a further refining of the coastline which, in some cases, has been corrected to improve the overlap with the VHR images.

More in detail, Class 72300 - Intertidal flats, initially extracted from the CLC map, was furtherly refined through photointerpretation of the VHR images by including additional intertidal flats that were not included in the CLC map due to the different (lower) MMU of the latter.

Figure 1 illustrates the spatial distribution of the total area mapped.

![Choropleth map displaying the Area of Interest (AOI) for the Copernicus Land Monitoring Service (CLMS) Coastal Zones (CZ) mapping products across Europe, North Africa, and the Middle East. The landmasses are rendered in light grey and water bodies in darker grey. The AOI is highlighted in red, extensively covering the coastlines of the British Isles, Fennoscandia, the Baltic Sea countries, the Mediterranean Basin (including Member States like Italy, Greece, Spain, Portugal, France), the Black Sea region (including Turkey, Bulgaria, Romania, Ukraine), and Iceland. Additional scattered red areas are visible in the Atlantic Ocean, specifically around the Azores, Madeira, and Canary Islands, representing insular coastal zones. Some inland red areas are present, particularly in Fennoscandia, likely indicating coverage of large inland water bodies or riparian zones. The map provides a visual representation of the approximately 2.229.478 km² total mapped area, which includes marine and ocean Land Use / Land Cover (LULC) classes 84100 (Open sea) and 84200 (Coastal waters), with a land-only AOI of 723.518 km² for the 2018 status layer. No explicit legend, scale, or compass is shown.](products_2012-2018_Quality_Assessment_Report_v0-media/img-d589a2af3eddf7a752bd0f1e75376bde.png)

Figure 1: Spatial distribution of the area mapped.

¹ i.e. excluding marine and ocean LCLU classes: 83200 - Estuaries, 83300 - Marine inlets and fjords, 84100 - Open sea and 84200 - Coastal waters

### 2.2.1 Summary statistics

The summary statistics on the CZ LC/LU class spatial distribution for the mapped area is reported in Table 5. The change area covers just ~1,5% of the total land surface of the mapped area.

Table 5: CZ LC/LU class spatial distribution for the mapped area.

|  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|
| Class code | Class names | Status map 2012 |  |  | Status layer 2018 |  |  | Change layer 2012-2018 |  |  |
|  |  | Counts | Area (km²) | Area (%) | Counts | Area (km²) | Area (%) | Area gain (km²) | Area loss (km²) | Diff (km²) |
| 11110 | Continuous urban fabric (IM,D ≥ 80%) | 27762 | 3246,65 | 0,15% | 27873 | 3258,51 | 0,15% | 13,42 | 1,55 | 11,86 |
| 11120 | Dense urban fabric (IM,D ≥ 30-80%) | 161366 | 18827,99 | 0,84% | 161707 | 19084,97 | 0,86% | 264,94 | 7,96 | 256,98 |
| 11130 | Low density urban fabric (IM,D \< 30%) | 553987 | 13767,87 | 0,62% | 556971 | 13943,46 | 0,63% | 182,48 | 6,90 | 175,58 |
| 11210 | Industrial, commercial, public and military units (other) | 376863 | 11314,42 | 0,51% | 385050 | 11862,07 | 0,53% | 586,14 | 38,49 | 547,64 |
| 11220 | Nuclear energy plants and associated land | 41 | 16,72 | \>0,01% | 50 | 18,74 | \>0,01% | 2,02 |  | 2,02 |
| 12100 | Road networks and associated land | 7736 | 4695,29 | 0,21% | 7817 | 4789,97 | 0,21% | 97,68 | 3,00 | 94,68 |
| 12200 | Railways and associated land | 3092 | 705,27 | 0,03% | 3141 | 713,83 | 0,03% | 9,11 | 0,55 | 8,55 |
| 12310 | Cargo port | 1794 | 546,25 | 0,02% | 1811 | 571,25 | 0,03% | 27,31 | 2,32 | 24,99 |
| 12320 | Passenger port | 504 | 23,34 | \>0,01% | 513 | 24,94 | \>0,01% | 1,62 | 0,02 | 1,59 |
| 12330 | Fishing port | 1480 | 29,51 | \>0,01% | 1518 | 30,56 | \>0,01% | 1,08 | 0,02 | 1,05 |
| 12340 | Naval port | 116 | 31,88 | \>0,01% | 116 | 32,23 | \>0,01% | 0,34 |  | 0,34 |
| 12350 | Marinas | 3506 | 145,88 | 0,01% | 3559 | 149,34 | 0,01% | 3,62 | 0,16 | 3,46 |
| 12360 | Local multi-functional harbours | 1285 | 35,54 | \>0,01% | 1293 | 35,98 | \>0,01% | 0,60 | 0,16 | 0,44 |
| 12370 | Shipyards | 402 | 40,54 | \>0,01% | 409 | 41,80 | \>0,01% | 1,32 | 0,06 | 1,27 |
| 12400 | Airports and associated land | 751 | 908,50 | 0,04% | 759 | 912,90 | 0,04% | 8,56 | 4,17 | 4,39 |
| 13110 | Mineral extraction sites | 14767 | 1449,72 | 0,07% | 14881 | 1510,91 | 0,07% | 164,41 | 103,23 | 61,19 |
| 13120 | Dump sites | 2013 | 117,60 | 0,01% | 2055 | 117,57 | 0,01% | 7,81 | 7,84 | -0,03 |
| 13130 | Construction sites | 14015 | 602,97 | 0,03% | 10930 | 540,62 | 0,02% | 393,42 | 455,76 | -62,34 |
| 13200 | Land without current use | 30742 | 840,84 | 0,04% | 29031 | 788,19 | 0,04% | 82,13 | 134,78 | -52,65 |
| 14000 | Green urban, sports and leisure facilities | 101860 | 5827,75 | 0,26% | 103091 | 5896,32 | 0,26% | 100,40 | 31,83 | 68,57 |
| 21100 | Arable irrigated and non-irrigated land | 335945 | 122755,66 | 5,51% | 338372 | 122217,06 | 5,48% | 353,05 | 891,65 | -538,61 |
| 21200 | Greenhouses | 28913 | 1549,81 | 0,07% | 30257 | 1703,81 | 0,08% | 202,90 | 48,90 | 154,00 |
| 22100 | Vineyards, fruit trees and berry plantations | 111145 | 15598,94 | 0,70% | 112828 | 15728,69 | 0,71% | 298,29 | 168,55 | 129,75 |
| 22200 | Olive groves | 108815 | 15297,06 | 0,69% | 109494 | 15283,00 | 0,69% | 41,30 | 55,35 | -14,05 |
| 23100 | Annual crops associated with permanent crops | 4444 | 480,82 | 0,02% | 4466 | 479,17 | 0,02% | 1,30 | 2,94 | -1,65 |
| 23200 | Complex cultivation patterns | 38258 | 3494,51 | 0,16% | 38368 | 3487,52 | 0,16% | 4,94 | 11,93 | -6,99 |
| 23300 | Land principally occupied by agriculture with significant areas of natural vegetation | 23949 | 2854,33 | 0,13% | 24042 | 2851,10 | 0,13% | 4,55 | 7,78 | -3,23 |
| 23400 | Agro-forestry (Mediterranean Areas) | 2743 | 1048,79 | 0,05% | 2747 | 1044,44 | 0,05% | 2,30 | 6,66 | -4,35 |
| 31100 | Natural & semi-natural broadleaved forest | 426043 | 74640,42 | 3,35% | 428992 | 74527,39 | 3,34% | 470,67 | 583,71 | -113,04 |
| 31200 | Highly artificial broadleaved plantations | 15290 | 6172,99 | 0,28% | 15525 | 6118,50 | 0,27% | 55,74 | 110,24 | -54,50 |
| 32100 | Natural & semi-natural coniferous forest | 244012 | 76659,29 | 3,44% | 253200 | 74109,04 | 3,32% | 1299,62 | 3849,86 | -2550,25 |
| 32200 | Highly artificial coniferous plantations | 4441 | 586,41 | 0,03% | 4806 | 661,02 | 0,03% | 109,87 | 35,26 | 74,61 |
| 33100 | Natural & semi-natural mixed forest | 101368 | 19043,31 | 0,85% | 102973 | 18897,99 | 0,85% | 273,64 | 418,96 | -145,32 |
| 33200 | Highly artificial mixed plantations | 393 | 44,07 | \>0,01% | 453 | 46,92 | \>0,01% | 5,32 | 2,47 | 2,85 |
| 34000 | Transitional woodland and scrub | 171587 | 12240,05 | 0,55% | 194055 | 14594,22 | 0,65% | 4659,75 | 2305,58 | 2354,17 |
| 35000 | Lines of trees and scrub | 11844 | 241,67 | 0,01% | 11866 | 245,75 | 0,01% | 4,91 | 0,83 | 4,08 |
| 36000 | Damaged forest | 266 | 53,84 | \>0,01% | 668 | 325,50 | 0,01% | 322,92 | 51,25 | 271,67 |
| 41000 | Managed grassland | 276578 | 56337,34 | 2,53% | 277341 | 56130,94 | 2,52% | 84,91 | 291,31 | -206,40 |
| 42100 | Semi-natural grassland | 362745 | 35404,02 | 1,59% | 364138 | 35253,64 | 1,58% | 366,50 | 516,88 | -150,38 |
| 42200 | Alpine and sub-alpine natural grassland | 56 | 2,41 | \>0,01% | 72 | 2,86 | \>0,01% | 0,61 | 0,16 | 0,45 |
| 51000 | Heathland and moorland | 132860 | 44469,98 | 1,99% | 133002 | 44395,65 | 1,99% | 20,90 | 95,24 | -74,33 |
| 52000 | Alpine scrub land | 1024 | 55,05 | \>0,01% | 1026 | 55,37 | \>0,01% | 0,38 | 0,07 | 0,32 |
| 53000 | Sclerophyllous scrubs | 110991 | 38964,49 | 1,75% | 111758 | 38558,07 | 1,73% | 124,68 | 531,10 | -406,42 |
| 61100 | Sparse vegetation on sands | 7061 | 926,12 | 0,04% | 7142 | 926,09 | 0,04% | 6,07 | 6,10 | -0,03 |
| 61200 | Sparse vegetation on rocks | 211328 | 44344,88 | 1,99% | 211545 | 44378,01 | 1,99% | 62,73 | 29,60 | 33,14 |
| 62111 | Sandy beach | 11675 | 1118,98 | 0,05% | 11708 | 1131,68 | 0,05% | 21,40 | 8,71 | 12,69 |
| 62112 | Shingle beach | 2477 | 106,09 | \>0,01% | 2470 | 106,33 | \>0,01% | 0,89 | 0,64 | 0,24 |
| 62120 | Dunes | 1458 | 527,47 | 0,02% | 1464 | 527,25 | 0,02% | 0,55 | 0,76 | -0,21 |
| 62200 | River banks | 11843 | 973,52 | 0,04% | 11968 | 953,47 | 0,04% | 33,24 | 53,29 | -20,05 |
| 63110 | Bare rocks and outcrops | 31194 | 15086,22 | 0,68% | 31260 | 15092,21 | 0,68% | 9,93 | 3,95 | 5,99 |
| 63120 | Coastal cliffs | 30377 | 1409,62 | 0,06% | 30355 | 1406,98 | 0,06% | 0,26 | 2,90 | -2,64 |
| 63200 | Burnt areas (except burnt forest) | 448 | 129,50 | 0,01% | 540 | 183,74 | 0,01% | 177,52 | 123,28 | 54,24 |
| 63300 | Glaciers and perpetual snow | 3133 | 1148,63 | 0,05% | 3133 | 1142,30 | 0,05% | 0,22 | 6,54 | -6,33 |
| 71100 | Inland marshes | 40724 | 5698,52 | 0,26% | 40835 | 5702,56 | 0,26% | 22,04 | 18,00 | 4,04 |
| 71210 | Exploited peat bog | 3119 | 1183,07 | 0,05% | 3142 | 1186,63 | 0,05% | 6,09 | 2,53 | 3,56 |
| 71220 | Unexploited peat bog | 63443 | 18937,96 | 0,85% | 63489 | 18921,81 | 0,85% | 0,78 | 16,93 | -16,15 |
| 72100 | Salt marshes | 32063 | 5228,60 | 0,23% | 32109 | 5221,32 | 0,23% | 9,27 | 16,55 | -7,28 |
| 72200 | Salines | 1087 | 707,59 | 0,03% | 1093 | 710,03 | 0,03% | 6,64 | 4,20 | 2,44 |
| 72300 | Intertidal flats | 7112 | 12142,34 | 0,54% | 7123 | 12148,68 | 0,54% | 9,81 | 3,48 | 6,33 |
| 81100 | Natural & semi-natural water courses | 19219 | 3428,76 | 0,15% | 19274 | 3463,89 | 0,16% | 59,76 | 24,63 | 35,13 |
| 81200 | Highly modified water courses and canals | 7553 | 722,79 | 0,03% | 7668 | 739,05 | 0,03% | 18,03 | 1,77 | 16,26 |
| 81300 | Seasonally connected water courses (oxbows) | 475 | 27,91 | \>0,01% | 490 | 28,42 | \>0,01% | 0,62 | 0,11 | 0,50 |
| 82100 | Natural lakes | 107399 | 12479,63 | 0,56% | 107576 | 12501,30 | 0,56% | 31,10 | 9,43 | 21,67 |
| 82200 | Reservoirs | 7200 | 168,08 | 0,01% | 7586 | 187,84 | 0,01% | 22,02 | 2,26 | 19,76 |
| 82300 | Aquaculture ponds | 681 | 126,33 | 0,01% | 696 | 127,31 | 0,01% | 1,33 | 0,35 | 0,98 |
| 82400 | Standing water bodies of extractive industrial sites | 1589 | 63,50 | \>0,01% | 1752 | 72,41 | \>0,01% | 13,26 | 4,35 | 8,94 |
| 83100 | Lagoons | 2959 | 5619,55 | 0,25% | 2966 | 5617,08 | 0,25% | 3,01 | 5,48 | -2,48 |
| 83200 | Estuaries | 597 | 3367,10 | 0,15% | 601 | 3360,57 | 0,15% | 0,41 | 6,94 | -6,53 |
| 83300 | Marine inlets and fjords | 701 | 28829,98 | 1,29% | 711 | 28806,84 | 1,29% | 0,15 | 23,28 | -23,14 |
| 84100 | Open sea | 250 | 1267898,72 | 56,87% | 249 | 1267898,70 | 56,87% |  | 0,02 | -0,02 |
| 84200 | Coastal waters | 803 | 205906,74 | 9,24% | 812 | 205893,70 | 9,24% | 28,46 | 41,50 | -13,04 |
| SUM |  | **4.425.760** | **2.229.478,03** | **100%** | **4.482.781** | **2.229.478,03** | **100%** | **11203,05** | **11203,05** |  |

## 2.3 Keynotes of used source files

The primary data source used for the mapping activities are the VHR datasets available in the ESA Data WareHouse. More in detail, in the areas covered by this delivery, the VHR2012 dataset is composed mainly by SPOT 5 data with a very small percentage of SPOT 6 data, while the VHR2018 dataset is composed by Pleiades and SPOT 7 data with minor percentages of PlanetScope and Deimos data.

In general, the data quality allows to meet the map specifications with minor issues in some areas where lower resolution images were available. In such cases the correct interpretation of the images has been supported by using available ancillary data.

In case of more than one image was available on a particular area, the interpretation was based on a defined hierarchy of the images: for the Status layer 2012 the images acquired in 2012 were first used, then the images acquired in 2013 and then in 2011 as last option. For Status layer 2018 the images acquired in 2018 were first used, than those acquired in 2017 since no images acquired in 2019 were available.

If more than one image was available in the same year on a particular area, than the hierarchy of the images dates was the following: Sep, Aug, Jul, Jun, May, Oct, Dec, Nov, Apr, Mar, Feb, Jan. For the day of the month the hierarchy was eventually in the reverse order from the last day to the first of the month.

Reference information of the satellite images used for the production of each LCLU map is included in the Parent Scene Identification Layer (PSIL, section 4.4).

In some cases, due to the complexity of the landscape and/or the resolution of the input VHR data, some ancillary data have been used to support the thematic interpretation while the objects delineation was always performed on the VHR satellite data.

The used ancillary data are:

- Microsoft Bing Maps.
- Google Earth satellite images.
- Map of the Nature System of Italy (partial)².
- Pan-European High Resolution Layers³.

## 2.4 Keynotes about the production process

The methodology implemented for the production of the Coastal Zone LC/LU map, due to the very detailed thematic specifications, is mainly founded on visual interpretation and delineation from remotely sensed Very High Resolution (VHR) images.

The visual interpretation is supported by a geometric skeleton derived by the integration of the already existing Copernicus Hot Spot mapping products such as Riparian Zones, Natura 2000 and Urban Atlas plus Open Street Map (in particular road and railway features) that have been used to the highest possible extent in order to avoid duplication of work.

The geometric skeleton and the VHR2012 are the basis data for the Coastal Zones LC/LU interpretation of the reference year 2012.

The change detection layer is created starting from the LC/LU 2012 status layer and applying a visual change interpretation and delineation based on the VHR satellite imagery of the reference years 2012 and 2018.

The status map 2018 layer is finally derived through the automatic integration of the status map 2012 and the change layer in a GIS environment.

² <http://www.isprambiente.gov.it/en/environmental-services/map-of-the-nature-system?set_language=en> ³ <https://land.copernicus.eu/pan-european/high-resolution-layers>

The geometric skeleton for Coastal Zones is derived by the following main input data:

- Natura 2000 & Riparian Zones
- Corine Land Cover (just selected classes)
- Urban Atlas (just selected classes & no direct integration)
- Open Street Maps (roads & railways)

Most of the input data have a similar nomenclature and mostly the same specifications as CZ (Minimum Mapping Unit = 0,5ha; Minimum Mapping Width = 10m, no spikes/acute angles, etc.). But still some of the input data can contain errors which are integrated also in the skeleton. These errors result due to:

- different degrees of application of the specifications
- different quality checks tools and methods (improvements of methods from first products to latest products, etc.)
- different thematic interpretations
- The specifications of Urban Atlas differ from CZ: some processing steps are needed to transform UA to input data for the skeleton. These processing steps can result in some artefacts, which produce MMW errors, spikes, etc.

The existing Copernicus Hot Spot mapping products (N2K, RZ, CLC) integrated in the skeleton are final and approved products (although containing some minor errors, e.g. MMW errors).

The integration of all input data into the skeleton also transfers the errors into the skeleton. Due to the combination of all data also some new errors on the border of the input data can be generated.

Ideally all errors in the CZ mapping should be resolved, but:

1.  some errors are introduced by the input data (that contain errors) that are already officially accepted
2.  some errors are introduced due to the skeleton generation (input data integration process) and the new mapping

Because some of the input data are already accepted by EEA and in the best-case errorless products could be expected for the integration into the skeleton, these errors are not corrected in the CZ products. Just the errors introduced in the CZ mapping due to the skeleton generation and the new mapping are resolved.

Handling of the different error types are described in the following Table 6.

Table 6: Handling of the errors inside the geometric skeleton

[TABLE]

### 2.4.1 Integration of CLC water classes

In order to take into account CZ Users feedback for amending seawards the final AOI, the “4.2.3 - Intertidal flats” thematic class from Corine Land Cover has been extracted and included in the final CZ product.

In addition, in order to close small gaps in the seawards and to homogenize the AOI in the whole EEA39, all sea and ocean gaps have been closed. For this reason the “5.2.3 Sea and ocean” thematic class from Corine Land Cover has been used and included in the final CZ product. The adopted solution improves the initial definition of a 1 km landwards buffer and makes the cartographic representation of the final product more aesthetically pleasing.

### 2.4.2 Different water levels in VHR2012 and VHR2018

For the scope of the Coastal Zones LC/LU production, the EU-Hydro coastline (updated on February 20, 2019 and amended through a comparison with the image data available from VHR-2018) is used as starting point. Only different water levels due to erosion/accretion of this coastline are mapped as changes in the change layer.

Different water body levels in VHR2012 and VHR2018 due to tide or temporal flooded areas are not considered as LC/LU changes. The reference year 2012 is used as basis for the LC/LU mapping and the water level of 2012 is delineated. If temporal fluctuations of water level between 2012 and 2018 without any real permanent change are detected, the water level change is not mapped and a comment is added to the class polygon.

# 3 Quantitative assessment of LCLU delivered data

The following section describes the internal accuracy assessment procedures and results of the LC/LU mapping referred to the final delivery (100% of the final AOI).

## 3.1 Accuracy Assessment

A well-proven thematic accuracy assessment was performed to evaluate the accuracy (overall accuracy, user’s and producer’s accuracy) of the Coastal Zones LC/LU status product of 2012, the status product of 2018 and the change layer (2012-2018). In order to understand the procedure of the internal accuracy assessment performed by the service providers, the applied sampling and response design is briefly described in this report. At the end of the report the results of the internal accuracy assessment for this intermediate delivery are presented. The validation shows that the consortium has delivered high quality products.

## 3.2 Sampling Design

For the Coastal Zones thematic accuracy assessment of the status layer 2012, the status layer 2018 and change layer 2012-2018, a stratified random point sampling scheme, in which all areas have a known non-zero probability of sampling, was selected. The first level strata of the sampling scheme are the Delivery Units (3 deliveries with an area distribution of 15,1%, 34,9% and 50,0%) and the second level strata are all LC/LU classes on Level 5 that have been mapped within a Delivery Unit, while taking into account the area sizes of the respective LC/LU class occurrence. To sufficiently cover changes and potential changes in the validation, additional sample points were added in areas mapped as changes (commission stratum) and areas prone to changes (omission stratum).

## 3.3 Response Design

For the internal validation of the Coastal Zones status 2012 layer, status 2018 layer and change layer 2012-2018, reference labels down to class level 5 were inferred by visual interpretation of the selected sample points. This step was performed by independent, well-trained operators, who were not involved in the production itself, using the Very High-Resolution (VHR) satellite data or higher quality data if available and applicable (e.g. Google Earth, Bing Maps, national orthophoto WMS). When re-interpreting the LC/LU sample point, the response design had to respect the latest product specifications with Coastal Zones LC/LU nomenclature guidelines (\[RD.5\]). A blind validation (without seeing the mapped classes) was performed on Level 1, a validation using a plausibility approach was used for level 5 (validator have information on the mapped class and need to decide if it is plausible and correct).

## 3.4 Internal validation results

The internal validation comprises the estimation of the overall weighted thematic accuracy of the status layer of 2012, status layer of 2018 and change layer 2012-2018. In order to maintain full statistical rigor and representativeness and account for unequal inclusion probabilities and the relative occurrence of classes, area related weights were replied, according to the area ratio for each class compared to the overall area.

The area weighting was adapted for the marine classes (8.4 Sea and ocean: 8.4.1 Open sea & 8.4.2 Coastal waters). The large area of these classes (\>66% of the total Area of Interest) would distort the validation, since the weighting factor of them would overestimate the influence of these two classes. The area reaching 1 km from the coastline seawards was chosen as reference area for these classes, as this was the original Area of Interest. Using this approach, the validation kept its statistical soundness, but increased its validity and significance.

In total 60.001 sample points were evaluated for the full delivery of the Coastal Zones product. Every LC/LU class and every region should be represented sufficiently.

The validation assessment includes the Overall Accuracy, Producer’s Accuracies and User’s Accuracies for Status 2012, Status 2018 and for the Change 2012-2018. The assessments are made for Level 1 (blind Accuracy for Status 2012 and Status 2018 is presented, on Table 10Error! Reference source not found. and Table 11Error! Reference source not found. the Producer’s and User’s Accuracies of the 8 Level 1 classes and the 71 Level 5 classes respectively. Accuracy metrics of the change layer 2012-2018 are demonstrated on Table 8Error! Reference source not found. (Overall Accuracy of the change layer 2012-2018) and on Table 9Error! Reference source not found. (Producer’s and User’s Accuracies of the changes).

The Overall Accuracy for the plausibility validation on Level 5 is 97,90 % for Status 2012 and 97,70% for Status 2018. For the blind validation on Level 1 these values are slightly higher, 98,27 % for Status 2012 and 98,24 % for Status 2018. All these values exceed the required Overall Accuracies of 85%.

Table 7: Overall Accuracies for Status 2012 and Status 2018.

|             |                         |                         |
|-------------|-------------------------|-------------------------|
|             | **Overall Accuracy**    | **Confidence Interval** |
| **Level 5** | plausibility validation | 97.90%                  |
| **Level 1** | blind validation        | 98.27%                  |

For the change layer 2012-2018 an Overall Accuracy of 99,61 % on Level 5 (with aggregation of the changes on level 1), 99,44 % on Level 5 (with aggregation of the changes on level 5), and 99,61 % on Level 1 is reached. These values are high, because they state that 99,61 % of the area is correctly mapped as change or non-change. The change area covers just ~1,64% of the total land surface of the Area of Interest.

Table 8: Overall Accuracies for Change 2012-2018.

|  |  |  |
|----|----|----|
|  |  | **Overall Accuracy** |
| **Level 5** | plausibility validation / aggregation level 1 | 99.606% |
| **Level 5** | plausibility validation / aggregation level 5 | 99.437% |
| **Level 1** | blind validation | 99.608% |

5 with aggregation of the changes on level 5) This means, \>92 % of the real LC/LU changes were detected correctly and \>93 % of the mapped changes are real LC/LU changes (see Table 9Error! Reference source not found.).

Table 9: Producer’s and User’s Accuracies for Change 2012-2018.

|                 |                         |
|-----------------|-------------------------|
|                 | **Producer’s Accuracy** |
| **Changes**     | 92.935%                 |
| **Non-Changes** | 97.851%                 |

The Producer’s and User’s Accuracy for Status 2012 and Status 2018 for the blind validation of Level 1 classes all achieve the required 80 %.

Table 10: Producer’s and User’s Accuracies for Status 2012 and Status 2018 Level 1 classes.

| Class |                         |                     |
|-------|-------------------------|---------------------|
|       | **Producer’s Accuracy** | **User’s Accuracy** |
| 1     | 97.39%                  | 98.66%              |
| 2     | 97.67%                  | 98.20%              |
| 3     | 98.68%                  | 98.18%              |
| 4     | 94.91%                  | 96.96%              |
| 5     | 91.20%                  | 96.76%              |
| 6     | 94.70%                  | 98.15%              |
| 7     | 97.08%                  | 98.41%              |
| 8     | 98.31%                  | 99.50%              |

exceed the 80% in the Producer’s and User’s Accuracy. Some rare classes have slightly lower accuracy values (see Table 11Error! Reference source not found.).

Table 11: Producer’s and User’s Accuracies for Status 2012 and Status 2018 Level 5 classes.

|  |  |  |  |  |
|----|----|----|----|----|
| Class | 2012 |  | 2018 |  |
|  | Producer's Accuracy | User's Accuracy | Producer's Accuracy | User's Accuracy |
| 11110 | 99.88% | 90.52% | 96.21% | 90.57% |
| 11120 | 91.65% | 98.06% | 89.70% | 98.23% |
| 11130 | 86.69% | 98.11% | 94.00% | 98.11% |
| 11210 | 96.52% | 97.97% | 94.67% | 97.99% |
| 11220 | 76.39% | 90.50% | 100.00% | 90.50% |
| 12100 | 98.51% | 98.38% | 95.65% | 98.90% |
| 12200 | 83.05% | 99.70% | 100.00% | 99.71% |
| 12310 | 95.37% | 92.24% | 90.29% | 92.33% |
| 12320 | 87.31% | 91.04% | 96.48% | 90.56% |
| 12330 | 94.45% | 90.59% | 81.71% | 91.12% |
| 12340 | 96.77% | 91.76% | 67.70% | 91.76% |
| 12350 | 94.81% | 87.86% | 95.54% | 94.04% |
| 12360 | 67.10% | 77.36% | 94.77% | 77.42% |
| 12370 | 97.45% | 85.24% | 98.35% | 85.56% |
| 12400 | 100.00% | 99.40% | 89.63% | 99.40% |
| 13110 | 91.48% | 96.65% | 92.82% | 93.68% |
| 13120 | 93.97% | 76.19% | 68.78% | 73.83% |
| 13130 | 92.59% | 95.20% | 87.20% | 88.64% |
| 13200 | 95.60% | 89.43% | 90.41% | 88.04% |
| 14000 | 70.95% | 96.48% | 91.71% | 96.63% |
| 21100 | 63.11% | 99.18% | 95.93% | 98.90% |
| 21200 | 93.99% | 94.89% | 94.38% | 97.48% |
| 22100 | 96.16% | 96.73% | 92.23% | 96.59% |
| 22200 | 95.06% | 96.42% | 88.29% | 96.06% |
| 23100 | 93.15% | 83.38% | 93.58% | 83.72% |
| 23200 | 92.86% | 84.03% | 74.17% | 83.94% |
| 23300 | 90.38% | 86.37% | 90.74% | 86.28% |
| 23400 | 83.30% | 89.88% | 97.37% | 89.80% |
| 31100 | 99.38% | 97.94% | 97.18% | 97.62% |
| 31200 | 95.80% | 99.04% | 88.12% | 98.99% |
| 32100 | 98.38% | 99.44% | 97.63% | 98.84% |
| 32200 | 94.81% | 71.68% | 80.16% | 86.46% |
| 33100 | 98.15% | 98.68% | 97.41% | 98.47% |
| 33200 | 92.90% | 38.10% | 90.84% | 38.64% |
| 34000 | 90.92% | 94.71% | 90.80% | 94.74% |
| 35000 | 99.13% | 94.24% | 90.34% | 94.24% |
| 36000 | 88.55% | 83.84% | 96.90% | 79.96% |
| 41000 | 97.28% | 98.14% | 95.74% | 97.72% |
| 42100 | 91.62% | 94.35% | 91.49% | 93.69% |
| 42200 | 94.50% | 26.34% | 67.32% | 27.65% |
| 51000 | 99.11% | 97.36% | 89.76% | 97.20% |
| 52000 | 97.61% | 86.68% | 100.00% | 81.55% |
| 53000 | 99.95% | 96.14% | 91.07% | 95.71% |
| 61100 | 98.83% | 86.55% | 98.22% | 87.38% |
| 61200 | 96.02% | 97.97% | 76.68% | 97.83% |
| 62111 | 97.44% | 98.48% | 88.92% | 97.87% |
| 62112 | 83.82% | 88.57% | 78.55% | 88.48% |
| 62120 | 51.18% | 98.70% | 89.13% | 98.75% |
| 62200 | 95.88% | 92.25% | 90.40% | 90.06% |
| 63110 | 99.75% | 98.08% | 93.45% | 97.87% |
| 63120 | 98.02% | 97.29% | 69.65% | 97.26% |
| 63200 | 91.21% | 93.87% | 100.00% | 77.57% |
| 63300 | 96.51% | 97.88% | 89.32% | 97.73% |
| 71100 | 92.93% | 95.03% | 79.74% | 94.98% |
| 71210 | 92.43% | 96.36% | 78.65% | 96.20% |
| 71220 | 98.77% | 97.92% | 86.73% | 97.91% |
| 72100 | 90.64% | 98.05% | 91.36% | 98.20% |
| 72200 | 98.09% | 99.54% | 99.12% | 99.54% |
| 72300 | 88.56% | 97.19% | 79.61% | 97.20% |
| 81100 | 96.86% | 98.45% | 96.74% | 98.24% |
| 81200 | 97.56% | 98.90% | 86.81% | 98.85% |
| 81300 | 100.00% | 98.40% | 91.27% | 98.35% |
| 82100 | 99.65% | 99.42% | 82.27% | 99.15% |
| 82200 | 68.75% | 89.53% | 91.49% | 89.93% |
| 82300 | 86.41% | 98.02% | 97.61% | 98.10% |
| 82400 | 92.29% | 90.28% | 87.55% | 90.47% |
| 83100 | 93.36% | 97.51% | 96.91% | 97.52% |
| 83200 | 97.61% | 98.13% | 85.44% | 98.19% |
| 83300 | 95.77% | 95.99% | 98.89% | 95.98% |
| 84100 | 100.00% | 100.00% | 99.95% | 100.00% |
| 84200 | 96.88% | 99.65% | 96.48% | 99.64% |

The validation estimates presented above express minimum quality values of the products delivered as the products have been further revised before delivery in order to correct the most important errors resulting from the internal validation process.

# 4 Delivered files

## 4.1 LCLU maps

According to the rules defined in \[RD.6\],\[RD.7\] and \[RD.8\], the data are delivered in three different zip files:

- `CZ_2012_DU004_3035_V1_0.zip` (includes the status map 2012)
- `CZ_2018_DU004_3035_V1_0.zip` (includes the status map 2018)
- `CZ_Change_2012_2018_DU004_3035_V1_0.zip` (includes the change map 2012-2018)

Each zip file includes the LCLU maps in Geopackage format as well as the metadata file in a separate folder as required in \[RD.6\], \[RD.7\] and \[RD.8\]. The name of the geopackage is the same of the zip file.

The attributes fields of each of the three layers are reported in Table 12.

Table 12: attribute fields in the three datasets

| Status map 2012 | Status maps 2018 | Change map 2012-2018 |
|-----------------|------------------|----------------------|
| ID              | ID               | ID                   |
| DU              | DU               | DU                   |
| CODE_1_12       | CODE_1_18        | CODE_1_12            |
| CODE_2_12       | CODE_2_18        | CODE_2_12            |
| CODE_3_12       | CODE_3_18        | CODE_3_12            |
| CODE_4_12       | CODE_4_18        | CODE_4_12            |
| CODE_5_12       | CODE_5_18        | CODE_5_18            |
| COMMENT_12      | COMMENT_18       | CODE_1_18            |
| NODATA_12       | NODATA_18        | CODE_2_18            |
| AREA_HA         | AREA_HA          | CODE_3_18            |
| Shape_Length    | Shape_Length     | CODE_4_18            |
| Shape_Area      | Shape_Area       | CODE_5_18            |
|                 |                  | COMMENT              |
|                 |                  | NODATA_12            |
|                 |                  | NODATA_18            |
|                 |                  | CHANGECODE           |
|                 |                  | AREA_HA              |
|                 |                  | Shape_Length         |
|                 |                  | Shape_Area           |

Where:

- “ID”: unique feature identifier.
- “DU”: coastal zones delivery unit ID.
- “CODE_1_12”: LCLU class code level 1, 2012.
- “CODE_2_12”: LCLU class code level 2, 2012.
- “CODE_3_12”: LCLU class code level 3, 2012.
- “CODE_4_12”: LCLU class code level 4, 2012.
- “CODE_5_12”: LCLU class code level 5, 2012.
- “CODE_1_18”: LCLU class code level 1, 2018.
- “CODE_2_18”: LCLU class code level 2, 2018.
- “CODE_4_18”: LCLU class code level 4, 2018.
- “CODE_5_18”: LCLU class code level 5, 2018.
- “NODATA_12”: indicator that polygon was not mapped in 2012 (0 or 1).
- “NODATA_18”: indicator that polygon was not mapped in 2018 (0 or 1).
- “COMMENT_12”: MMU or MMW exception and different water level comment.
- “COMMENT_18”: MMU or MMW exception and different water level comment.
- “COMMENT”: area size exception comment.
- “CHANGECODE”: “CODE_4_12”\_“CODE_4_18” e.g. “2110_1111”.
- “AREA_HA”: “real”, area of polygon in hectares.
- “Shape_Length”: the perimeter of the feature.
- “Shape_Area”: the area of the polygon expressed in m².

## 4.2 Reference points interpreted

Reference points interpreted for the product level delivery report are also included in the delivery. The points are delivered in shapefile format included in a zip file. This file collects the validation points used in delivery 1 (15,4% of AOI), delivery 2 (34,6% of AOI) and delivery 3 (50% of AOI), for a total of 60.001 points.

The map validation process has been the same for each single delivery. Since a re-coding to 5\\^{th}\\ level class of the nomenclature has been agreed with EEA during the project (only re-coding not introducing further classification improvement), the validation has been always performed at class level 4 and then the results have been presented at level 5 according to the recoding table agreed with EEA (Appendix A).

Reference points, provided as shapefile named “CZ_DEL04_validation_points.zip”, do not consider the 5\\^{th}\\ level class of the nomenclature. The shapefile has the following attribute table listed in Table 13.

Table 13: Attribute table of the reference points shapefile.

| Name | Description |
|----|----|
| Id | Id of the point |
| CODE_4_12 | Class of the polygon underneath the point at the 4\\^{th}\\ level of the status map 2012 |
| CODE_4_18 | Class of the polygon underneath the point at the 4\\^{th}\\ level of the status map 2018 |
| Val_4_12 | Validator class attribution at 4\\^{th}\\ level for status map 2012 (plausibility approach) |
| Val_4_18 | Validator class attribution at 4\\^{th}\\ level for status map 2018 (plausibility approach) |
| Val_1_12 | Validator class attribution at 1\\^{st}\\ level for status map 2012 (blind approach) |
| Val_1_18 | Validator class attribution at 1\\^{st}\\ level for status map 2018 (blind approach) |

The spatial reference system for all data is: ETRS89 ETRS-LAEA equal-area projection (EPSG: 3035).

## 4.3 Metadata

Metadata are provided together with the products as INSPIRE-compliant XML files according to the EEA Metadata Standard for Geographic Information (EEA-MSGI). EEA-MSGI has been developed by EEA to meet needs and demands for inter-operability of metadata. EEA’s standard for metadata is a profile of the ISO 19115 standard for geographic metadata and contains more elements than the minimum required to comply the INSPIRE metadata regulation.

at: <http://www.eionet.europa.eu/gis>.

## 4.4 PSIL

The Parent Scene Identification Layer (PSIL) is an auxiliary vector file included in the delivery containing spatially explicit reference information of the satellite images used for the production of each LCLU map.

The PSIL includes two files:

- “CZ_DEL04_PSIL_2012.zip” related to the images used for the status map 2012
- “CZ_DEL04_PSIL_2018.zip” related to the images used for the status map 2018

Each zip file includes a vector polygon file in ESRI Shapefile format projected in ETRS89 Lambert Azimuthal Equal Area (EPSG: 3035). The shapefiles define the VHR images used in production for each point of the maps. The attribute table of each shapefile is described in Table 14.

Table 14: Attribute table of the PSIL shapefiles

| Name | Description |
|----|----|
| Id | Id of the polygon |
| Filename | File name of the image as defined in the ESA Data WareHouse |
| ProdType | Product Type as defined in \[RD.9\] and \[RD.10\] |
| Start_Sens | Start date and time of the acquisition of the image |
| Stop_Sens | Stop date and time of the acquisition of the image |
| Platform | Satellite platform code |
| Datasets | Name of the dataset including the image file in the ESA Data WareHouse |
| Delivery | Delivery number for which the image has been used |

# 5 Appendix A: Re-coding table from 4\\^{th}\\ to 5\\^{th}\\ class level

The following re-coding rule table from 4\\^{th}\\ to 5\\^{th}\\ class level has been agreed with EEA and applied to all the CZ mapping products in order to maximize coherence between CZ and N2k nomenclatures.

| forth level of old nomenclature class code | Fifth level of new nomenclature class code |
|----|----|
| 1111 | 11110 |
| 1112 | 11120 |
| 1113 | 11130 |
| 1121 | 11210 |
| 1122 | 11220 |
| 1210 | 12100 |
| 1220 | 12200 |
| 1231 | 12310 |
| 1232 | 12320 |
| 1233 | 12330 |
| 1234 | 12340 |
| 1235 | 12350 |
| 1236 | 12360 |
| 1237 | 12370 |
| 1240 | 12400 |
| 1310 | 13110 |
| 1320 | 13120 |
| 1330 | 13130 |
| 1340 | 13200 |
| 1400 | 14000 |
| 2110 | 21100 |
| 2120 | 21200 |
| 2210 | 22100 |
| 2220 | 22200 |
| 2310 | 23100 |
| 2320 | 23200 |
| 2330 | 23300 |
| 2340 | 23400 |
| 3110 | 31100 |
| 3120 | 31200 |
| 3210 | 32100 |
| 3220 | 32200 |
| 3310 | 33100 |
| 3320 | 33200 |
| 3400 | 34000 |
| 3500 | 35000 |
| 3600 | 36000 |
| 4100 | 41000 |
| 4210 | 42100 |
| 4220 | 42200 |
| 5100 | 51000 |
| 5300 | 53000 |
| 6110 | 61100 |
| 6120 | 61200 |
| 6211 | 62111 |
| 6212 | 62112 |
| 6220 | 62120 |
| 6230 | 62200 |
| 6311 | 63110 |
| 6312 | 63120 |
| 6320 | 63200 |
| 6330 | 63300 |
| 7110 | 71100 |
| 7121 | 71210 |
| 7122 | 71220 |
| 7210 | 72100 |
| 7220 | 72200 |
| 7230 | 72300 |
| 8110 | 81100 |
| 8120 | 81200 |
| 8130 | 81300 |
| 8210 | 82100 |
| 8220 | 82200 |
| 8230 | 82300 |
| 8240 | 82400 |
| 8310 | 83100 |
| 8320 | 83200 |
| 8330 | 83300 |
| 8410 | 84100 |
| 8420 | 84200 |

Back to top

## Reuse

EUPL (\>= 1.2)
