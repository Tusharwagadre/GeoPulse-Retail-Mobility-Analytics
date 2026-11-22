# GeoPulse: Hyper-Local Retail Mobility Analytics

## 1. Project Overview
GeoPulse is a geospatial analytics project focused on understanding urban mobility and retail foot traffic patterns. It aims to help retailers make informed decisions about potential store locations by analyzing anonymized mobile GPS data.

## 2. Problem Statement
Retailers often depend on static census data when selecting new store locations. This approach may fail to capture actual movement patterns and foot traffic throughout the day. As a result, a new store may overlap with the customer movement patterns of an existing store, potentially causing sales cannibalization.

GeoPulse aims to address this challenge through geospatial data analysis and visualization.

## 3. Project Objectives
- Analyze anonymized mobile GPS pings to understand movement patterns.
- Explore foot traffic across different locations and time periods.
- Use spatial joins to connect GPS points with store catchment areas.
- Calculate unique visitors per store per hour.
- Analyze potential customer overlap between multiple store locations.
- Develop interactive geospatial visualizations to support retail location decisions.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Snowflake | Geospatial data storage |
| Apache Sedona / PySpark | Spatial transformations and joins |
| dbt | Data cleaning and modeling |
| Kepler.gl | Geospatial visualization |
| React | Dashboard interface |
| Apache Airflow | Workflow automation |

## 5. Development Roadmap
- **Week 1:** Generate mock anonymized GPS data and load it into Snowflake.
- **Week 2:** Perform spatial joins and aggregate unique visitors per store per hour.
- **Week 3:** Develop store cannibalization analysis and integrate the map interface.
- **Week 4:** Automate data pipelines using Apache Airflow and refine the interactive map.

## 6. Project Status
Repository initialization and project documentation are in progress. Implementation will follow the official project development plan.

---
*Project: GeoPulse — Infotact Solutions Internship*
