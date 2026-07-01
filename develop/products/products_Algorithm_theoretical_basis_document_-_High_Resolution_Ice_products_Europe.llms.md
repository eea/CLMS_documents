# Production of High Resolution Water, Snow and Ice products (Lot 1)

HR-WSI ALGORITHM THEORETICAL BASIS DOCUMENT - ICE PRODUCTS

This Algorithm Theoretical Basis Document (ATBD) comprehensively describes the methodologies for generating High-Resolution Water, Snow & Ice (HR-WSI) ice products within the Copernicus Land Monitoring Service (CLMS). Focusing on continental Europe, it details the algorithms for Water/Ice Cover (WIC) from Sentinel-1 radar and Sentinel-2 optical data, their combined WIC S1+S2 product, and the derived Aggregated Water/Ice Cover (AWIC) and Ice Cover Duration (ICD) products. The document outlines the preprocessing of satellite imagery, machine learning approaches, thresholding techniques, and temporal aggregation methods, along with crucial auxiliary data and product limitations, ensuring clarity for technical users.

Published

January 20, 2026

Keywords

High-Resolution Water, Snow & Ice (HR-WSI), Water/Ice Cover (WIC), Aggregated Water/Ice Cover (AWIC), Ice Cover Duration (ICD), Sentinel-1 Synthetic Aperture Radar (SAR), Sentinel-2 optical imagery, Machine learning classification, Random Forest classifier, Ice detection algorithms, Water mask, Temporal aggregation, Algorithm Theoretical Basis Document (ATBD)

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

[TABLE]

### 0.1 Document Approver(s) and Reviewer(s)

| Name               | Role                   | Action   | Date       |
|--------------------|------------------------|----------|------------|
| Joanna Przystawska | Project Owner          | Revision | 11/12/2024 |
| Lorenzo Solari     | Project Owner (deputy) | Revision | 11/12/2024 |
| Joanna Przystawska | Project Owner          | Revision | 07/03/2025 |
| Lorenzo Solari     | Project Owner (deputy) | Revision | 07/03/2025 |

### 0.2 Document history

[TABLE]

Back to top

## Reuse

EUPL (\>= 1.2)
