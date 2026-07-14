# CLMS → CDSE Migration Status

Copernicus Land Monitoring Service

This report provides a comprehensive overview of the ongoing migration of Copernicus Land Monitoring Service (CLMS) products to the Copernicus Data Space Ecosystem (CDSE). It tracks the ingestion status of the extensive CLMS portfolio, detailing progress across global, pan-European, and priority area product groups. The document highlights fully, partially, and not-yet-migrated datasets, offering a clear technical snapshot of data availability on the new platform. It serves as a vital resource for data engineers, scientists, and regulators monitoring the accessibility and integration of crucial land monitoring data through CDSE’s various services.

Author

Copernicus Land Monitoring Service

Published

July 14, 2026

Keywords

CLMS product migration, Copernicus Data Space Ecosystem (CDSE), data ingestion status, global land monitoring products, Pan-European land monitoring products, Priority Area products, S3 data access, OData API, STAC catalogue, OpenEO integration, Sentinel Hub, land portfolio tracking

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

**Last updated:** 2026-07-14 12:00 UTC

This report tracks the migration of CLMS products from the [land.copernicus.eu](https://land.copernicus.eu/en/dataset-catalog) portfolio to the [Copernicus Data Space Ecosystem (CDSE)](https://dataspace.copernicus.eu/). It is updated weekly.

## 1 Summary

| Metric                    | Value                    |
|---------------------------|--------------------------|
| CLMS Portfolio            | 236 datasets / 39 groups |
| CDSE S3 Ingestion         | 144 dataset IDs          |
| CDSE OData Products       | 8,060,310                |
| Datasets ingested on CDSE | 138                      |
| Groups fully ingested     | 19                       |
| Groups partially ingested | 5                        |
| Groups not yet on CDSE    | 15                       |

### 1.1 By Product Scope

| Scope            | Groups | Datasets | On CDSE | %                        |
|------------------|--------|----------|---------|--------------------------|
| 🌍 Global        | 17     | 101      | 88      | 87% █████████████████░░░ |
| 🇪🇺 Pan-European  | 17     | 107      | 46      | 43% ████████░░░░░░░░░░░░ |
| 📍 Priority Area | 5      | 28       | 4       | 14% ██░░░░░░░░░░░░░░░░░░ |

## 2 Per-Group Ingestion Status

| Product Group | Scope | Land | CDSE | % | Progress |
|----|----|----|----|----|----|
| Burnt Area | 🌍 Global | 4 | 4 | 100% | ████████████████████ |
| CLCplus Backbone | 🇪🇺 Pan-European | 4 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| CLCplus LULUCF Instance | 🇪🇺 Pan-European | 1 | 1 | 100% | ████████████████████ |
| CORINE Land Cover | 🇪🇺 Pan-European | 9 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Coastal Zones | 📍 Priority Area | 3 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Crop Types | 🇪🇺 Pan-European | 1 | 2 | 200% | ████████████████████ |
| Cropping Patterns | 🇪🇺 Pan-European | 12 | 20 | 167% | ████████████████████ |
| Dominant Leaf Type | 🇪🇺 Pan-European | 7 | 5 | 71% | ██████████████░░░░░░ |
| Dynamic Land Cover | 🌍 Global | 3 | 3 | 100% | ████████████████████ |
| EU-Hydro | 🇪🇺 Pan-European | 1 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| European Ground Motion Service | 🇪🇺 Pan-European | 4 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| European Image Mosaic | 🇪🇺 Pan-European | 13 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Evapotranspiration | 🌍 Global | 2 | 2 | 100% | ████████████████████ |
| Forest Type | 🇪🇺 Pan-European | 5 | 3 | 60% | ████████████░░░░░░░░ |
| Grassland Mowing Events | 🇪🇺 Pan-European | 2 | 3 | 150% | ████████████████████ |
| Grassland and Herbaceous | 🇪🇺 Pan-European | 7 | 7 | 100% | ████████████████████ |
| HR Imperviousness | 🇪🇺 Pan-European | 26 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| HR Water and Wetness | 🇪🇺 Pan-European | 2 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Hot Spots Monitoring | 📍 Priority Area | 5 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Lake Water Quality | 🌍 Global | 5 | 5 | 100% | ████████████████████ |
| Land Surface Temperature (LST) | 🌍 Global | 11 | 9 | 82% | ████████████████░░░░ |
| N2K / Protected Areas | 📍 Priority Area | 5 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Primary Production | 🌍 Global | 10 | 10 | 100% | ████████████████████ |
| Riparian Zones | 📍 Priority Area | 3 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| River and Lake Ice Extent | 🌍 Global | 7 | 8 | 114% | ████████████████████ |
| River and Lake Water Level | 🌍 Global | 2 | 2 | 100% | ████████████████████ |
| Small Landscape Features | 🇪🇺 Pan-European | 4 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Snow Cover Extent | 🌍 Global | 7 | 7 | 100% | ████████████████████ |
| Snow State | 🌍 Global | 2 | 2 | 100% | ████████████████████ |
| Snow Water Equivalent | 🌍 Global | 2 | 2 | 100% | ████████████████████ |
| Soil Moisture / SWI | 🌍 Global | 10 | 10 | 100% | ████████████████████ |
| Surface Reflectance | 🌍 Global | 1 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Tree Cover Density | 🇪🇺 Pan-European | 7 | 5 | 71% | ██████████████░░░░░░ |
| Urban Atlas | 📍 Priority Area | 12 | 4 | 33% | ██████░░░░░░░░░░░░░░ |
| Vegetation Indices | 🌍 Global | 6 | 8 | 133% | ████████████████████ |
| Vegetation Phenology and Productivity Parameters | 🌍 Global | 16 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Vegetation Properties | 🌍 Global | 9 | 9 | 100% | ████████████████████ |
| Vegetation Seasonal Trajectories | 🇪🇺 Pan-European | 2 | 0 | 0% | ░░░░░░░░░░░░░░░░░░░░ |
| Water Extent | 🌍 Global | 4 | 7 | 175% | ████████████████████ |

## 3 Groups Not Yet on CDSE (0%)

The following product groups have no datasets ingested on CDSE yet. These are the main gap in the migration.

- 🇪🇺 Pan-European — **HR Imperviousness** — 26 datasets pending
- 🌍 Global — **Vegetation Phenology and Productivity Parameters** — 16 datasets pending
- 🇪🇺 Pan-European — **European Image Mosaic** — 13 datasets pending
- 🇪🇺 Pan-European — **CORINE Land Cover** — 9 datasets pending
- 📍 Priority Area — **Hot Spots Monitoring** — 5 datasets pending
- 📍 Priority Area — **N2K / Protected Areas** — 5 datasets pending
- 🇪🇺 Pan-European — **CLCplus Backbone** — 4 datasets pending
- 🇪🇺 Pan-European — **European Ground Motion Service** — 4 datasets pending
- 🇪🇺 Pan-European — **Small Landscape Features** — 4 datasets pending
- 📍 Priority Area — **Coastal Zones** — 3 datasets pending
- 📍 Priority Area — **Riparian Zones** — 3 datasets pending
- 🇪🇺 Pan-European — **HR Water and Wetness** — 2 datasets pending
- 🇪🇺 Pan-European — **Vegetation Seasonal Trajectories** — 2 datasets pending
- 🇪🇺 Pan-European — **EU-Hydro** — 1 dataset pending
- 🌍 Global — **Surface Reflectance** — 1 dataset pending

## 4 Partially Ingested Groups

These groups have some datasets on CDSE but are not yet fully migrated.

- 🌍 Global — **Land Surface Temperature (LST)** — 9/11 (82%)
- 🇪🇺 Pan-European — **Dominant Leaf Type** — 5/7 (71%)
- 🇪🇺 Pan-European — **Tree Cover Density** — 5/7 (71%)
- 🇪🇺 Pan-European — **Forest Type** — 3/5 (60%)
- 📍 Priority Area — **Urban Atlas** — 4/12 (33%)

## 5 Fully Ingested Groups (100%+)

These groups are fully available on CDSE. Percentages above 100% indicate CDSE contains additional derived datasets (e.g., confidence layers) beyond the land portal’s base product listing.

- 🇪🇺 Pan-European — **Crop Types** — 2/1 (200%)
- 🌍 Global — **Water Extent** — 7/4 (175%)
- 🇪🇺 Pan-European — **Cropping Patterns** — 20/12 (167%)
- 🇪🇺 Pan-European — **Grassland Mowing Events** — 3/2 (150%)
- 🌍 Global — **Vegetation Indices** — 8/6 (133%)
- 🌍 Global — **River and Lake Ice Extent** — 8/7 (114%)
- 🌍 Global — **Burnt Area** — 4/4 (100%)
- 🇪🇺 Pan-European — **CLCplus LULUCF Instance** — 1/1 (100%)
- 🌍 Global — **Dynamic Land Cover** — 3/3 (100%)
- 🌍 Global — **Evapotranspiration** — 2/2 (100%)
- 🇪🇺 Pan-European — **Grassland and Herbaceous** — 7/7 (100%)
- 🌍 Global — **Lake Water Quality** — 5/5 (100%)
- 🌍 Global — **Primary Production** — 10/10 (100%)
- 🌍 Global — **River and Lake Water Level** — 2/2 (100%)
- 🌍 Global — **Snow Cover Extent** — 7/7 (100%)
- 🌍 Global — **Snow State** — 2/2 (100%)
- 🌍 Global — **Snow Water Equivalent** — 2/2 (100%)
- 🌍 Global — **Soil Moisture / SWI** — 10/10 (100%)
- 🌍 Global — **Vegetation Properties** — 9/9 (100%)

## 6 Scope Breakdown

### 6.1 🌍 Global Products

Products with worldwide coverage — bio-geophysical variables (temperature, water, snow, vegetation, energy fluxes), land cover (Dynamic Land Cover, Water Extent), and vegetation parameters.

**15/17** groups have datasets on CDSE.

### 6.2 🇪🇺 Pan-European Products

Products covering the EEA39 region (Europe) — high-resolution land cover, land use, forest, grassland, and imperviousness layers, thematic products (CLC, CLC+, EU-Hydro, EGMS, Image Mosaic), and vegetation seasonal trajectories.

**8/17** groups have datasets on CDSE.

### 6.3 📍 Priority Area Products

Local-scale monitoring products covering specific areas of interest (urban, coastal, riparian, protected areas, hot spots).

**1/5** groups have datasets on CDSE.

## 7 Services

CLMS data on CDSE is available through the following services:

- [S3](https://csv.dataspace.copernicus.eu/CLMS/)
- [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/)
- [STAC](https://browser.stac.dataspace.copernicus.eu/)
- [OpenEO](https://openeo.dataspace.copernicus.eu/)
- [Sentinel Hub](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data/CLMS.html)
- [Docs](https://documentation.dataspace.copernicus.eu/Data/CopernicusServices/CLMS.html)

## 8 Methodology

This report is generated by a weekly scraper that:

1.  **Fetches the land.copernicus.eu portfolio** — all 249 datasets across 39 product groups via the Plone REST API.
2.  **Crawls the CDSE CSV catalogue** — discovers dataset IDs available on S3 under `bio-geophysical`, `landcover_landuse`, and `land_cover_use_in_priority_areas`.
3.  **Queries the CDSE OData API** — total CLMS product count.
4.  **Cross-references** — maps CDSE dataset IDs to land portal product groups and reports ingestion status per group.

Back to top

## Reuse

EUPL (\>= 1.2)
