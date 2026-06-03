# Copernicus Land Data Store - Public Consultation Report

Copernicus Land Monitoring Service

This report summarises the findings of a public consultation survey regarding the Copernicus Land Data Store (CLDS), launched in October 2023. The survey aimed to understand the geospatial application landscape, focusing on factors that either hinder or motivate users to adopt cloud-based solutions. By assessing the balance between user needs (such as handling large data volumes) and concerns (such as migration difficulties and costs), the study provides valuable insights into the challenges and opportunities associated with transitioning to cloud environments for geospatial data processing and analysis.

Published

March 18, 2024

Keywords

Cloud migration barriers, Geospatial data accessibility, Cloud processing environment familiarity, Data storage solutions, Scalable processing resources, Copernicus data heterogeneity, Data product understanding, Cloud-based storage services, User onboarding mechanisms, FAIR data principles

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

# 1 Introduction

This report summarises the outcomes of the CLDS consultation survey launched on October 01, 2023. In addition to standard single/multiple choice questions and tables, the survey also offered several options for open replies and the possibility to interact further with CLMS by email. This was done to increase the possibility for interaction and to inquire about aspects respondents might consider relevant but were not covered by the questions.

The goal of the survey was to better understand working practices in the field of geospatial applications. In particular, we were interested to understand limiting factors that inhibit (or block) users from working on the cloud. The underlaying assumption is that an eventual migration to a cloud environment depends on several factors, which can be grouped into two key forces, and which the survey tries to assess specifically:

1.  **intensity of the need** (e.g., the lack of non-cloud-based infrastructure to cope with given data volumes and processing needs) against

2.  **intensity of concerns and difficulties** standing in the way of such migration.

Only when the needs outweigh the concerns and difficulties will a user consider migrating to the cloud. Finally, there is a third force worth mentioning - **curiosity** - which can introduce a certain unpredictability into the otherwise predictable equation of the first two. The flexibility to scale computing and storage resources as needed is considered as one important advantage of a cloud environment. Equally important is the data pool a cloud environment makes accessible.

It shall be noted that the relatively low number of respondents (25) suggests a certain level of caution when interpreting results. Given the limited sample size, the statistical significance of the figures may be constrained. Still, the replies reflect specific and common trends which overlap with key messages in the CLDS[^1] published in September 2023. Note that not all survey questions are presented in this report. In some cases, the low number of responses makes interpretation too difficult, and thus they were omitted. In other cases, the information is not sufficiently relevant for this report, and these too were omitted.

The survey was structured in three main sections:

1.  General user background assessment - \[7 questions\]

2.  Specific questions I: Data producers (commercial, public, research) – \[19 questions\]

3.  Specific questions II: Data consumers – \[16 questions\]

# 2 General user background assessment

The first part of the survey aimed to collect users’ background information, allowing for a better categorisation of their replies. Based on the user category (Figure 1), users were forwarded either to section 2 or to section 3.

## 2.1 Which category describes best your current professional activity?

![Bar chart showing the count of respondents from the CLMS consultation survey categorized by their role in geospatial services and applications. The Y-axis represents 'Count' and ranges from 0 to 9. The X-axis displays three categorical roles: 'Commercial or public provider of geospatial services' (red bar), 'Consumer of geospatial services' (light green bar), and 'Researcher in the field of geospatial applications' (blue bar). The counts for each role are: Commercial or public provider of geospatial services, 9; Consumer of geospatial services, 7; and Researcher in the field of geospatial applications, 9. Commercial or public providers and researchers represent the highest and equal number of respondents, while consumers have the lowest count.](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-7fc03cfba11c7af99271d646985f693eea22b9bd.png)

Figure 1 - ‘Which category describes best your current professional activity?’ (single choice)

In total 25 respondents were registered, and classified according to:

1.  Commercial or public provider of geospatial services. \[9 responses\]

2.  Consumer of geospatial services. \[7 responses\]

3.  Researcher in the field of geospatial applications. \[9 responses\]

## 2.2 How would you rate your technical skills in the field of geospatial applications?

![This grouped bar chart displays the self-assessed 'Skill level' (X-axis, ranging from 0 to 10) against the 'Count' of survey respondents (Y-axis, ranging from 0 to 3) across three professional activity categories. The categories, identified in the legend, are: 'Commercial or public provider of geospatial services' (red bars), 'Consumer of geospatial services' (green bars), and 'Researcher in the field of geospatial applications' (blue bars). The data points are: \* \*\*Skill level 3:\*\* 1 Consumer of geospatial services. \* \*\*Skill level 4:\*\* 1 Consumer of geospatial services. \* \*\*Skill level 5:\*\* 1 Consumer of geospatial services, 2 Researchers in the field of geospatial applications. \* \*\*Skill level 6:\*\* No respondents. \* \*\*Skill level 7:\*\* 2 Commercial or public providers of geospatial services, 1 Consumer of geospatial services, 2 Researchers in the field of geospatial applications. \* \*\*Skill level 8:\*\* 3 Commercial or public providers of geospatial services, 2 Consumers of geospatial services, 1 Researcher in the field of geospatial applications. \* \*\*Skill level 9:\*\* 2 Commercial or public providers of geospatial services, 1 Consumer of geospatial services, 3 Researchers in the field of geospatial applications. \* \*\*Skill level 10:\*\* 2 Commercial or public providers of geospatial services, 2 Researchers in the field of geospatial applications. No respondents reported skill levels of 0, 1, 2, or 6. Commercial or public providers and Researchers predominantly report higher skill levels, concentrated between 7 and 10. Consumers show a broader distribution of skill levels, from 3 to 9, though with lower counts per level. The highest number of respondents for a single skill level within a category is 3, occurring for Commercial or public providers at skill level 8 and for Researchers at skill level 9. This chart illustrates user background assessment from a survey related to Copernicus Land Monitoring Service (CLMS) documentation.](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-d82b983272123af1c3826fb1c922c0428186da86.png)

Figure 2 - ‘How would you rate your technical skills in the field of geospatial applications?’

The aim of this question was to apply a stratification depending on the level of expertise of respondents. As expected, commercial and public data providers (red) as well as researchers (blue) show a similarly high level of technical expertise. Data consumers (green) show a broader range and relatively to the other categories a slightly lower scoring. It might be worth noting that 4 out of 7 consumers still score relatively high (7 and more).

## 2.3 How do you normally work with geodata?

![This grouped stacked bar chart illustrates the frequency of use of Programming, Desktop, and Web geospatial applications across three professional activity categories: 'Researcher in the field of geospatial applications', 'Commercial or public provider of geospatial services', and 'Consumer of geospatial services'. The Y-axis represents Frequency, scaled from 0.00 to 1.00. The legend defines the colour-coded frequency levels: dark green for '(almost) exclusively', light green for 'often', orange for 'sometimes', and red for '(almost) never'. For \*\*Programming\*\*: \* 'Researcher in the field of geospatial applications' respondents report usage frequencies of 12% '(almost) never', 15% 'sometimes', 42% 'often', and 31% '(almost) exclusively'. \* 'Commercial or public provider of geospatial services' respondents report 10% '(almost) never', 15% 'sometimes', 37% 'often', and 38% '(almost) exclusively'. \* 'Consumer of geospatial services' respondents report 45% '(almost) never', 31% 'sometimes', 19% 'often', and 5% '(almost) exclusively'. For \*\*Desktop\*\*: \* 'Researcher in the field of geospatial applications' respondents report 15% '(almost) never', 10% 'sometimes', 70% 'often', and 5% '(almost) exclusively'. \* 'Commercial or public provider of geospatial services' respondents report 5% '(almost) never', 30% 'sometimes', 60% 'often', and 5% '(almost) exclusively'. \* 'Consumer of geospatial services' respondents report 15% '(almost) never', 20% 'sometimes', 60% 'often', and 5% '(almost) exclusively'. For \*\*Web\*\*: \* 'Researcher in the field of geospatial applications' respondents report 15% '(almost) never', 20% 'sometimes', 60% 'often', and 5% '(almost) exclusively'. \* 'Commercial or public provider of geospatial services' respondents report 5% '(almost) never', 25% 'sometimes', 65% 'often', and 5% '(almost) exclusively'. \* 'Consumer of geospatial services' respondents report 15% '(almost) never', 30% 'sometimes', 50% 'often', and 5% '(almost) exclusively'. Overall, Researchers and Commercial/Public Providers show higher frequencies of 'often' and '(almost) exclusively' usage for Programming and Desktop applications compared to Consumers. Consumers report the highest frequency of '(almost) never' for Programming. Desktop and Web applications are used 'often' or 'sometimes' by a high proportion of all respondent categories.](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-b517b561ae2527eb4f9db918fdb10897bb804325.png)

Figure 3 - ‘How do you normally work with geodata?’

***Researchers:***

- Prefer a ‘Coding/Programming’ or also a ‘Graphical Desktop’ solution for working.

***Commercial or public Data Providers:***

- Do use all three working types ‘Coding/Programming’, ‘Graphical Desktop’ as well as ‘(interactive) web-based’ solutions.

***Consumers:***

- Are only exceptionally programmers, and mainly working with Desktop solution (GIS). For consumers of geospatial information, the skill level remains surprisingly high.

Web-based interactive maps seem to be the least used mean of interacting with geospatial data.

# 3 Specific questions

## 3.1 What is the data amount you are usually dealing with?

![Grouped bar chart displaying the count of respondents by data volume category and user role. The Y-axis represents \`Count\` and ranges from 0 to 6. The X-axis represents data volume categories: \`\< 10 GBs\`, \`10 GBs \< 100 GBs\`, and \`\>= 100 GBs\`. Two data series are shown: \`Commercial or public provider of geospatial services\` (red bars) and \`Researcher in the field of geospatial applications\` (blue bars). For the \`\< 10 GBs\` category, there are 4 respondents identified as commercial or public providers and 6 respondents identified as researchers. For the \`10 GBs \< 100 GBs\` category, there are 2 respondents identified as commercial or public providers and 2 respondents identified as researchers. For the \`\>= 100 GBs\` category, there are 3 respondents identified as commercial or public providers and 1 respondent identified as a researcher. Overall, researchers more frequently work with geospatial data volumes less than 10 GBs, while commercial or public providers show a higher propensity to work with data volumes of 100 GBs or more. Both user groups have an equal count of respondents for data volumes between 10 GBs and less than 100 GBs.](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-fd0320b7c3ea7d2d43dc68e239016ec2f0d948f4.png)

Figure 4 - What is the data amount you are usually dealing with? (single choice)

Since data consumers usually are not in the situation of handling data, this question was asked to data producers only. As it can be seen in Figure 4, there are three different size classes:

- ‘Less than 10GBs’,

- ‘More than 10 and up to 100 GBs’,

- ‘More than 100GBs’.

This question was meant to assess a key factor relevant for the freedom of choosing a processing solution. The smaller data volumes a user is confronted with, the less pressure there is on users to opt for a scalable and managed storage and production environment.

The first category is defined for small-scale applications, and regarding hardware constraints easily executable on any desktop computer. The second category represents an average-sized setup, requiring a dedicated system that may not necessarily be scalable. The third category is tailored for large-scale projects, where transitioning to the cloud becomes a sensible choice. Initially, there was a ‘below 1 GB’ category, but it was subsequently merged with the ‘below 10 GB’ class for greater clarity and simplicity.

There is a relatively high share of small-scale projects (10 out of 18 projects are \< 10GBs). Such small-scale projects typically do not have demands on scalable processing and storage resources. Besides the hardware aspect, the access to a vast data pool present on the cloud might still be of great interest for such projects.

While researchers clearly tend to work with smaller data volumes, commercial and public data providers show a much broader range. A reason for that could be, that 1) researchers are working on a lower spatial resolution, and 2) operational high resolution wall-to-wall mapping of large areas is not so common.

## 3.2 ‘Where is your data mostly stored?’

![A 100% stacked bar chart illustrating the relative frequency (Freq.) of different data processing solutions, categorized by user role. The Y-axis represents frequency from 0.00 to 1.00. The X-axis displays two user roles: 'Commercial or public provider of geospatial services' and 'Researcher in the field of geospatial applications'. The stacked bars show the proportion of 'local' (dark blue), 'server' (pink), and 'cloud' (yellow) solutions. For 'Commercial or public provider of geospatial services': \* 'local' solutions account for approximately 17% (from 0.00 to 0.17). \* 'server' solutions account for approximately 33% (from 0.17 to 0.50). \* 'cloud' solutions account for approximately 50% (from 0.50 to 1.00). For 'Researcher in the field of geospatial applications': \* 'local' solutions account for approximately 12% (from 0.00 to 0.12). \* 'server' solutions account for approximately 63% (from 0.12 to 0.75). \* 'cloud' solutions account for approximately 25% (from 0.75 to 1.00). The chart indicates that commercial/public providers of geospatial services primarily utilize cloud solutions, while researchers in geospatial applications rely most heavily on server-based solutions.](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-9fcdf4dd99e33e58363bedaf14ede7ffd8020dff.png)

Figure 5 - ‘Where is your data mostly stored?’ (multiple question)

Respondents could choose between:

- ‘local’, i.e., a workstation,

- ‘server’ i.e., a dedicated self-managed data server, and

- ‘cloud’, i.e., a cloud-based storage service.

Only 12-15% of data producers are working on a local standalone machine. Conversely, almost 90% of the respondents have some sort of data pool they are accessing remotely. 50% of the public and commercial data providers do make use of a cloud service for storing data. Which seems to be plausible due to the larger data amounts, and the need to expose the services to their customers. More than 60% of researchers mostly use a self-managed infrastructure.

## 3.3 In recent times, let’s say in the past year, have you been working in a cloud processing environment?

This question aims to understand the frequency with which data producers work in cloud environments. It is expected that the frequency coincides also with the level of acquaintance of users to work in a cloud environment.

![This stacked bar chart displays the distribution of responses from 'Commercial or public provider of geospatial services' (pink) and 'Researcher in the field of geospatial applications' (blue) across an 11-point scale from 0 ('Never') to 10 ('Exclusively'). The Y-axis represents the 'Count' of respondents, ranging from 0 to 5. Specific data points for 'Researcher in the field of geospatial applications' are: 1 at scale point 0, 2 at scale point 1, 2 at scale point 3, 1 at scale point 5, 2 at scale point 6, and 1 at scale point 9. Specific data points for 'Commercial or public provider of geospatial services' are: 3 at scale point 1, 1 at scale point 5, 3 at scale point 7, 1 at scale point 9, and 1 at scale point 10. The chart represents a total of 18 projects. Researchers show a higher frequency at the lower end of the scale (0, 1, 3, 6), indicating less exclusive engagement or reliance. Commercial or public providers exhibit a broader distribution across the scale, with notable peaks at scale points 1 and 7, and also appear at the higher exclusivity points of 9 and 10.](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-847a58a2c98af9f2bb83d5970d0a80c5b862ded8.png)

Figure 6 - In recent times, let’s say in the past year, have you been working in a cloud processing environment?

At least occasionally, most users seem to have recently worked in the cloud.

- 7 out of 17 almost never - rarely (0-3)

- 7 out of 17 regularly (4-7)

- 3 out of 17 almost exclusively (8-10)

## 3.4 What is the scale you are usually working on?

![Grouped bar chart displaying the count of different geospatial actors across five working scales: local, regional, national, continental, and global. The Y-axis represents 'Count' from 0 to 6. The X-axis represents 'Working Scale'. The chart presents three data series, distinguished by colour: \* Red: Commercial or public provider of geospatial services \* Green: Consumer of geospatial services \* Blue: Researcher in the field of geospatial applications Data points for each working scale are as follows: \* \*\*local\*\*: Commercial or public provider (4), Consumer (5), Researcher (1). \* \*\*regional\*\*: Commercial or public provider (6), Consumer (5), Researcher (1). \* \*\*national\*\*: Commercial or public provider (4), Consumer (4), Researcher (2). \* \*\*continental\*\*: Commercial or public provider (6), Consumer (3), Researcher (3). \* \*\*global\*\*: Commercial or public provider (3), Consumer (0), Researcher (3). Commercial or public providers of geospatial services show the highest counts at regional and continental scales (6 each). Consumers of geospatial services are most prevalent at local and regional scales (5 each), but none operate at a global scale. Researchers in geospatial applications consistently have lower counts across all scales compared to the other groups, with their highest activity at continental and global scales (3 each).](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-512418cabf87a8782d0d8a929294999ef8874591.png)

Figure 7 – What is the scale you are usually working on? (multiple choice)

As it can be seen **researchers** do tendentially work more at continental and global scale. Taking into account also the data volumes (Figure 4), it is likely that they are working with lower resolution data.

**Commercial and public data providers** are more present on local to continental scales. Interestingly, there is a strong overall in the distribution of commercial and public data producers with data users. Eventually, this could be interpreted as an indicator of good match between user demands and data offer.

## 3.5 Generally, do you find yourself in the situation where you would like to have more data/products at your disposal?

![Stacked bar chart illustrating challenges related to data availability and sufficiency for two groups of geospatial data users. The Y-axis represents 'Count' of respondents, ranging from 0 to 10. The X-axis displays two categories of respondents: 'Commercial or public provider of geospatial services' and 'Researcher in the field of geospatial applications'. The chart segments each bar by the following responses: \* Green: 'No, I usually have all the products I need.' \* Orange: 'Yes, I am sometimes in the situation where I would not mind to have other/better data/products.' \* Red: 'Yes, I am regularly in the situation where missing/sub-optimal data is hampering my project goals.' For 'Commercial or public provider of geospatial services' (total 9 respondents): \* 2 respondents (red segment) are regularly hampered by missing/sub-optimal data. \* 6 respondents (orange segment) sometimes desire other/better data/products. \* 1 respondent (green segment) usually has all needed products. For 'Researcher in the field of geospatial applications' (total 7 respondents): \* 0 respondents (red segment) are regularly hampered by missing/sub-optimal data. \* 4 respondents (orange segment) sometimes desire other/better data/products. \* 3 respondents (green segment) usually have all needed products. The chart shows that commercial or public providers of geospatial services report more significant issues with data availability and quality, with two respondents regularly hampered by data gaps, compared to researchers, none of whom report regular hampering by data issues. Researchers more frequently report usually having all the products they need (3 out of 7, or approximately 43%) than commercial/public providers (1 out of 9, or approximately 11%).](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-b9a0538f6ac96aa1dc153d1e6526ec2149bc2f7a.png)

Figure 8 - Generally, do you find yourself in the situation where you would like to have more data/products at your disposal?

This question aims at assessing the availability of EO data and derived products, and how often and how strong a gap in the data offer impactsthe implementation of a project/product/service. The question was only asked to data producers and researchers, but retrospectively it probably should have been also asked to data consumers.

What can be said is that the lack of data/products seems to be a **major issue**.

Researchers seem to have somewhat fewer and minor issues, but with only 3 out of 7 cases, having no problems with the data situation, does not seem to be an optimal situation either.

## 3.6 How easy/difficult it is to…

The next two sets of questions are aiming at understanding the difficulties data producers/ data consumers are encountering in the process of implementing a geospatial project / using a geospatial product. To better address important points, each group was asked a slightly different set of questions.

### 3.6.1 Commercial/public data producers and researchers - Think about new products that you wish to include in your processes. How difficult/problematic is…

This question was asked to commercial/public data producers as well as to researchers and assesses the respondents experience in the process of setting up and implementing a data production project. The following key activities of a potential product generation workflow were included:

1.  Finding a potentially useful dataset

2.  Understanding a potentially useful dataset

3.  Bringing the new dataset to your processing environment

4.  Pre-processing the new dataset to make it usable for your processes.

5.  Handling large scale processes

6.  Processing costs

7.  Publish

Respondents had to rate each of these questions with one of the following options:

- no problem

- somewhat difficult

- difficult

- very difficult (I regularly don’t use a product for that reason)

![This multi-panel horizontal bar chart displays the perceived difficulty of seven key activities in a geospatial product generation workflow, as rated by commercial/public data producers and researchers. The shared Y-axis represents 'Count' with a scale from 0 to 7.5. The shared X-axis shows the problem rating categories: 'no problem', 'somewhat difficult', 'difficult', and 'very difficult (I regularly don't use a product for that reason)'. Each panel corresponds to a specific activity: 1. \*\*Finding a potentially useful dataset\*\* (red bars): Rated as 'somewhat difficult' by approximately 7.5 respondents, 'difficult' by about 3.5 respondents, 'no problem' by 2.0 respondents, and 'very difficult' by 2.0 respondents. 2. \*\*Understanding a potentially useful dataset\*\* (gold bars): Rated 'somewhat difficult' by 6.0 respondents, 'no problem' by 4.5 respondents, 'difficult' by 4.5 respondents, and 'very difficult' by 1.5 respondents. 3. \*\*Bringing the new product to your processing environment\*\* (green bars): Rated 'difficult' by 7.0 respondents, 'no problem' by 3.5 respondents, 'somewhat difficult' by 1.5 respondents, and 'very difficult' by 1.5 respondents. 4. \*\*Pre-processing the new product to make it usable for your processes.\*\* (teal bars): Rated 'difficult' by 7.0 respondents, 'no problem' by 3.0 respondents, 'somewhat difficult' by 3.0 respondents, and 'very difficult' by 1.0 respondent. 5. \*\*Handling large scale processes\*\* (light blue bars): Rated 'difficult' by 6.0 respondents, 'no problem' by 4.0 respondents, 'somewhat difficult' by 3.0 respondents, and 'very difficult' by 2.5 respondents. 6. \*\*Processing costs\*\* (purple bars): Rated 'difficult' by 7.0 respondents, 'somewhat difficult' by 4.5 respondents, 'no problem' by 1.0 respondent, and 'very difficult' by 1.0 respondent. 7. \*\*Publish (this also entails moving your product)\*\* (pink bars): Rated 'somewhat difficult' by 5.5 respondents, 'difficult' by 3.5 respondents, 'no problem' by 3.0 respondents, and 'very difficult' by 1.0 respondent. Overall, the chart indicates a considerable level of difficulty across all listed activities, with 'somewhat difficult' and 'difficult' categories receiving the most votes. Specifically, 'Finding a potentially useful dataset' and 'Understanding a potentially useful dataset' predominantly score as 'somewhat difficult,' while 'Bringing the new product to your processing environment,' 'Pre-processing the new product,' and 'Processing costs' are most frequently rated as 'difficult.'](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-a9bf8b3bb3ef3583aacd84449d7142cc137d5de1.png)

Figure 9 – ‘Think about new products that you wish to include in your processes. How difficult/problematic is…’

It is clearly visible that most votes are ‘somewhat difficult’ and ‘difficult’, showing overall a considerable level of difficulty. Question one and two, finding and understanding a potentially product score mostly ‘somewhat difficult’. While this is better than others, it remains a considerable friction in the user’s workflow.

Questions three to six focus on the preparatory steps and cloud processing activities, i.e., elements that a cloud service should aim to make as simple and efficient as possible. Overall, they seem to be the most problematic part of the overall workflow. This is also confirmed by the free text questions ([Section 4](#sec-Free-text-replies)).

Product publication seems to be somewhat less. It could be assumed that publication is often not a mandatory step, or that it can be done by simple means, such as a pdf report, or a download link, and whenever more complex data publication activities are involved, the needed expertise is available.

### 3.6.2 Data Consumers - How easy is it …

In analogy with 3.6.1, these questions were asked to data consumers with the scope of understanding the respondents experience in the process of using a geospatial product. These are the following key activities of a potential data search and use:

How easy do you think is…:

1.  Discovering new geospatial data?

2.  Finding the geospatial data you are looking for?

3.  Understanding the potential usage of a data product?

4.  Using on-line applications to interact with spatial data?Respondents had to rate each of these questions with one of the following:

- Straight-forward

- Rather easy

- Rather hard

- Very hard

![This is a series of four horizontal bar charts, each representing survey responses for a different question regarding the ease of geospatial data activities for data consumers. The Y-axis for all charts represents 'Count' with a range from 0 to 5. The X-axis for all charts shows response categories: 'straight-forward', 'rather easy', 'rather hard', and 'very hard'. The data points are as follows: \* \*\*Question: 'Discovering new geospatial data?'\*\* \* straight-forward: 0 counts \* rather easy: 5 counts \* rather hard: 2 counts \* very hard: 0 counts \* \*\*Question: 'Finding the geospatial data you are looking for?'\*\* \* straight-forward: 1 count \* rather easy: 3 counts \* rather hard: 3 counts \* very hard: 0 counts \* \*\*Question: 'Understanding the potential usages of a data product?'\*\* \* straight-forward: 0 counts \* rather easy: 3 counts \* rather hard: 3 counts \* very hard: 1 count \* \*\*Question: 'Using on-line applications to interact with spatial data?'\*\* \* straight-forward: 0 counts \* rather easy: 4 counts \* rather hard: 2 counts \* very hard: 1 count Overall, the responses indicate that 'Discovering new geospatial data?' is most frequently rated as 'rather easy', while 'Finding the geospatial data you are looking for?' and 'Understanding the potential usages of a data product?' show an equal number of respondents finding them 'rather easy' and 'rather hard'. All questions received at least one 'rather hard' response, and two questions received a 'very hard' response.](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-7059a8039acb8745a6057d792689b8d46f062375.png)

Figure 10 – ‘How easy it is…’

Overall, most replies score ‘rather easy’ but there is also a high occurrence of ‘rather hard’. These results indicate a certain level of difficulties on the customer’s side. To generate considerable uptake dynamics the (public and commercial) geospatial service providers must ensure these points score almost exclusively ‘straight-forward’.

## 3.7 Please rank the following ways of consuming geospatial data according to your preference and regular use

The following questions aims at assessing how consumers preferably use geospatial information. Respondents had to rank the following options:

- Online, by means of a catalogue to discover and find data.

- Online, by means of map viewers where I can combine layers.

- Offline, after downloading ad-hoc spatial data.

- Offline, after downloading statistics as Excel, CSV, PDF files…

- Online, by means of dashboards including pre-processed data.

The plot shows an aggregated evaluation of the results, where, for each rank position different score is given, i.e., first position got 5 points, second position got 4,…, until the fifth one, which got 1 point. Summing up the points for each question resulted in the following bar plot, giving an idea of consumers preferences.

![Vertical bar chart showing aggregated scores for different methods of consuming geospatial data, based on user preferences. The Y-axis represents 'Score' and ranges from 0 to 20. The X-axis lists five distinct methods for data consumption. The scores are derived from a ranking system where the first position received 5 points, the second 4, down to the fifth receiving 1 point. The data series, represented by green bars, shows the following scores for each consumption method: \* 'Online, by means of a catalogue to discover and find data': 21 points. \* 'Online, by means of map viewers where I can combine layers': 17 points. \* 'Offline, after downloading ad-hoc spatial data': 15 points. \* 'Offline, after downloading statistics as Excel, CSV, PDF files...': 11 points. \* 'Online, by means of dashboards including pre-processed data': 11 points. The chart indicates that online methods for discovering data via a catalogue and using map viewers are the most preferred ways of consuming geospatial data, followed by offline downloading of ad-hoc spatial data. Downloading statistics offline and using online dashboards are the least preferred methods, receiving identical, lower scores.](dr3yejtzxollhygq0lwfgjxf755jvzyly2lemmvpgiqrzf5own2074qpdivug54c-media/img-1dfb0d2b588aed2d55dd53387a4c4271397c434b.png)

Figure 11 - ‘Please rank the following ways of consuming geospatial data according to your preference and regular use’

# 4 Free text replies

Besides the choice-based replies, the survey also contained several questions with the reply in a free text form. This was a particularly precious element of the survey, as respondents could express concerns and proposals which could not have been captured otherwise.

Before the free text reply respondents were asked: ‘*In recent times, let’s say in the past year, have you been working in a cloud processing environment?*’ (see 3.3)

Followed by the free text question: ‘*If the above question scores lower than you would like: why didn’t you work more intensively in a cloud processing environment?*’

And then a second one: ‘*What are possible improvements you are currently missing in most cloud-based storage and/or processing solutions?*’

## 4.1 Respondent 1

Respondents background:

- Commercial or public provider of geospatial services

- Very high technical skills in the field of geodata

- Mostly working with scripting/programming

- Projects typically between 10 and 100 GB

- Working on a wide range of scales (local; regional; continental; global)

- Hosting data on a company/institution managed server

- \[Not used to work in a cloud environment!\]{.underline}

**Question**: “Why didn’t you work more intensively in a cloud processing environment?”

**Answer**: “*Accessibility and preparation of the various required input data is not straight forward on a cloud system. Moving from one’s own system to a cloud processing environment requires too much effort to be considered for any developments or tests. Considering the long-term usage of a processing environment - which is usually desired when a full processing chain has been developed and is set up - the costs for using a cloud processing system are much higher than building a processing system on one’s own server. Further, the resources on a cloud cannot be reused, but a user must pay each time when the resources are needed. Maintenance efforts on a cloud system are out of a user’s control and can have a major impact on the processing environment or the timing of one’s own work.*”

This respondent does not seem to deal with very large data scales. On hardware side such scale is still very well manageable on a local workstation. This means that there is no strong pushfactor for moving the production to a cloud environment. Apparently, there are no sufficient pull-factors on the respondents, i.e., convincing arguments, for moving to the cloud. Main issues highlighted by the respondent are:

- significant effort required for migration,

- higher long-term costs compared to a self-built server,

- lack of resource reusability, and

- concerns about lack of control over maintenance efforts that could impact their work.

**Question**: “What are possible improvements you are currently missing in most cloud-based storage and/or processing solutions?”

**Answer**: “*Direct access to data provided by the main international EO data providers, including Copernicus, ESA, EUMETSAT, NASA, NOAA, JAXA, etc.*“

The proposed improvements are clearly highlighting the importance of the data pool, a key advantage of a cloud environment. The respondent also highlights how important a seamless/direct access to data is despite where it is stored.

Indeed, the fragmentation of European data is remarkable. On the other hand, one unique cloud solution does not seem to be realistic either. The focus must rely on seamless access mechanisms and interoperability which includes processing capabilities across the cloud infrastructures.

Federation, system integration, open standards, seem to be the keywords for addressing the problem.

## 4.2 Respondent 2

Respondents background:

- Researcher in the field of geospatial applications

- High technical skills in the field of geodata

- Mostly working with Desktop GIS/image processing software.

- Projects typically below 10 GB

- Working usually on at continental scale

- Hosting data on a company managed server

- \[Not used to work in a cloud environment!\]{.underline}

**Question**: “Why didn’t you work more intensively in a cloud processing environment?”

**Answer**: “*Not used to it, often lack of knowledge about how to process.*”

This respondent primarily deals with minimal data volumes, resulting in limited hardware and productivity tool requirements for handling extensive files, both in terms of quantity and size. As a result, there is a minimal impetus for this user to transition to the cloud, particularly when viewed through the lens of hardware demands and tool compatibility.

**Question**: “What are possible improvements you are currently missing in most cloud-based storage and/or processing solutions?”

**Answer**: “*Make the use easy with processes to download data pre-configurated and well explained ad-hoc options with examples.*”

This respondent shows some level of interest to work in the cloud. The lack of knowledge on how to work on the cloud seems to be the key problem. This respondent clearly points out the need for **guidance** and **training**, as well as the provision of **simple** and **user-friendly** solutions that can help to overcome the initial difficulties.

It is probably safe to say that a key obstacle for a user starting to work in a cloud environment is the difficulty of learning how to work in the cloud. It cannot be emphasised enough how important it is to support users in learning how to work in the cloud.

Asked about “*…why didn’t you work more intensively in a cloud processing environment?*”, the majority of the free-text replies point to the same note:

- “I haven’t had the training to learn how to use it”

- “cost, competence and personal resources”

- “not specifically needed, not very friendly environments”

- “no time”

And: “What are possible improvements you are currently missing in most cloud-based storage and/or processing solutions?”

- “Improvement of general System security”

- “Clearer guidelines, user-friendly environments”

## 4.3 Respondent 3

Respondents background:

- Commercial or public provider of geospatial services

- Very high technical skills in the field of geodata

- Using all possible solution for working with geodata.

- Projects typically above 100 GBs

- Working usually on at continental and global scales

- Hosting data in cloud

- Very much used to work in cloud environments!

**Question**: “Why didn’t you work more intensively in a cloud processing environment?”

**Answer**: “*At the moment we lack the possibilities for subscription of consume based services, hour or capacity-usage based pricing models on European Copernicus Cloud Providers, such as WEkEO. A more dynamic price model and advanced Container Orchestration services (e.g. Kubernetes as a Service) would provide us the possibility to increase our efficiency and would enable us to provide more cost-effective products. In addition, a more stable and robust European cloud environment would be highly appreciated and would lead to shorter production times, leading to lower productions costs.*”

This respondent is a data provider, used to handle large data amounts and very much used to work in the cloud.

The data volumes and services this respondent is used to work with, likely offersfew alternatives and necessitating the use of a cloud-based solution. At some point this respondent took the decision of learning how to work in the cloud and migrating the workflowsthere. While the level of satisfaction of migrating to the cloud is not disclosed, with this step the respondent had to accept a higher degree of dependency to the quality and the competitivity of a cloud-based services.

**Question**: “What are possible improvements you are currently missing in most cloud-based storage and/or processing solutions?”

**Answer**: “*To provide cost efficient product for our customers we heavily rely on European cloudenvironments in the domain of public domains, such as the Copernicus Programme.*”

This experienced cloud users ask for more competitivity in the current cloud offers, the proposed improvements are pointing at:

More dynamic pricing models (e.g., capacity-usage based) and at the technological layer important for the production process (process scalability, e.g., Kubernetes).

Such improvements would allow to offer more effective services (reduction of cost and production time), and thus ultimately to the benefit of the users, and strengthening the competitivity of the European market.

## 4.4 Respondent 4

Respondents background:

- Researcher in the field of geospatial applications

- Very high technical skills in the field of geodata

- Mostly working with scripting/programming and desktop solutions

- Projects typically between 10 and 100 GB

- Working on a wide range of scales (local; regional; national; continental)

- Hosting data on a company/institution managed server

- Used to work in cloud environments!

**Question**: “Why didn’t you work more intensively in a cloud processing environment?”

**Answer**: “*I wish that the EU and EC increased cooperation with NASA and really used NASA’s experience in data sharing and processing. Instead of tens of different data portals and gateways just use one properly that keeps all the data in the same structure like LP DAAC. And also provides a user with useful tools e.g.: https://appeears.earthdatacloud.nasa.gov/*

*Using Copernicus data is difficult because there is chaos, they are not consistent across, and formats are not very user-friendly. Why ASF (https://asf.alaska.edu/) can better provide (and process) S1 data than Copernicus and EC?*”

Very experienced in geoscience, used to manage medium size data volumes and used to work in the cloud.

The respondent seems to be interested and capable of working in a cloud environment. The main issue seems to be in the heterogeneity and inconsistency of European data provision landscape. The respondent indirectly also highlights the importance of the data pool, which besides and independently from the availability of scalable processing resources can be considered a further good reason (pull factor) for migrating to the cloud.

The proposed improvements are clearly pointing at ‘fewer but better’ services related to data provision and processing capabilities.

# 5 Conclusions

The survey was set up to better understand the working practices of the geodata community. Emphasis was given to cloud based working practices – how much experts rely on cloud-based solutions in their day-to-day applications, and especially to understand what shall be improved to make cloud environments more attractive.

The low number of respondents must be considered when assessing the results. The survey queried data producers (science, commercial, and public) and data users/consumers separately (Figure 1) and despite the expected uncertainties, the most important patterns seem to be well captured.

Although most experts do not appear to be fundamentally opposed to “working in the cloud”, only a surprisingly small proportion implement it consistently ([Section 3.3](#sec-3-3)). This is perhaps the most important discrepancy identified in this survey, and understanding and addressing its causes must be at the centre of our attention.

A high proportion of projects are working with relatively small amounts of data (Figure 4) and may therefore have a lower need for scalable cloud solutions. However, as it can be seen from the free text responses ([Section 4](#sec-Free-text-replies)), the willingness and interest in working in the cloud is clearly noticeable. In view of the large variety of freely available data, the question of why users do not work with large amounts of data may also be justified. Is there simply no need for large data volumes, or are the possibilities for accessing and processing the data inadequate?

It is clear from Figure 9, and even more so from the free text responses in [Section 4](#sec-Free-text-replies), that data producers face a variety of difficulties that prevent them from engaging with potential cloud solutions. In summary the main concerns and difficulties are:

- Data is distributed across several unintegrated data pools.

- Data products and access mechanisms are not consistent.

- Stability, reliability, and robustness of cloud production environments.

- Migrating to the cloud requires a considerable investment in expertise, and there is a lack of well-conceived user onboarding mechanisms.

- Uncompetitive pricing schemes (lack of ‘consumer-based services’)

- High costs as compared to self-hosted solution (at least for small to medium scale requirements)

In fact, these ’*concerns and difficulties*’ are the most significant obstacles preventing the decision to transition to the cloud. Addressing concerns and difficulties should therefore be put high up in the agenda of good cloud services. This involves offering compelling services and showcasing example workflows that not only persuade users with scalability demands but also resonate with those working with smaller data amounts, encouraging them to embrace the benefits of a cloud environment.

If we look at the existing cloud solutions, we can see that the competition is mainly on the available data pool, the costs (including how costs are allocated) and the functionalities offered by cloud providers. The aim of the CLDS is to remove the data pool from this equation. Users should be free to choose the best fitting cloud services without having to accept a limitation of the available datasets. As outlined in the concept note[^2], the Copernicus Land Data Store aims to make the CLMS portfolio accessible to as many cloud services as possible. Cloud providers should be able to easily integrate CLMS data into the services.

To improve findability and accessibility of CLMS data, the CLDS will also build on the FAIR[^3] principles. Together with the FAIR principles the CLDS will ensure product documentation and CLMS related articles can be harvested by chatbots helping users to enquire CLMS product usability and technical details. These measures shall help to reduce the difficulties users encounter on their journey to work with CLMS data (see [Section 3.5](#sec-3-5), [Section 3.6.1](#sec-3-6-1), [Section 3.6.2](#sec-3-6-2)).

In conclusion, we can produce a few main recommendations that should be taken up by cloud services and data stakeholders:

- Expose data using open and state of the art solutions. This includes proper data format and access mechanisms.

- Ensure good connectivity to and from the data pool.

- Harmonise data access methods, allowing users to rely on one single access solutions connecting to all data pools.

- Invest in user uptake:

  - Pre-configured well documented practical examples

  - Trainings and webinars

  - Helpdesk

- Enable competitive pricing schemes and infrastructure services.

- Cloud services shall see their value in, and prioritize accordingly:

  - Scalable processing and storage resources

  - Availability and efficient accessibility to large data pools

  - Effective, competitive, and reliable production environment

# 6 Change Log

| Date       | Version | Summary         |
|------------|---------|-----------------|
| 2025-12-03 | 1.0.0   | Initial release |

Back to top

## Footnotes

## Reuse

EUPL (\>= 1.2)

[^1]: https://land.copernicus.eu/en/news/clds-survey/clds-concept-note_final.pdf/%40%40download/file

[^2]: https://land.copernicus.eu/en/news/clds-survey/clds-concept-note_final.pdf/%40%40download/file

[^3]: https://www.go-fair.org/
