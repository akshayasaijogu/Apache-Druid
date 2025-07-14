# Apache-Druid

# 📘 Student Academic Data Management using Apache Druid

This project demonstrates a high-performance academic data management system built with **Apache Druid**, a real-time analytics database. It efficiently ingests structured academic records and provides dynamic analytics for student performance tracking.

---

## 📌 Table of Contents

- [📖 Overview](#-overview)
- [💻 Tech Stack](#-tech-stack)
- [🚀 Features](#-features)
- [🛠️ How to Run](#️-how-to-run)
- [📂 Files Included](#-files-included)
- [📊 Sample Queries](#-sample-queries)
- [📸 Screenshots](#-screenshots)
- [📄 License](#-license)

---

## 📖 Overview

This system processes academic records such as midterm, internal, and external exam scores. Using Apache Druid's real-time SQL engine, it calculates:

- SGPA (Semester Grade Point Average)
- Overall percentage
- Subject-wise performance insights
- All academic record details

With Druid’s distributed, column-oriented architecture, it delivers sub-second query performance even on large datasets.

---

## 💻 Tech Stack

- **Apache Druid 32.0.0**
- **Druid SQL**
- **VirtualBox with Ubuntu**
- **CSV for academic data ingestion**
---

## 🚀 Features

- 🔄 Real-time ingestion of academic datasets
- ⚡ Sub-second analytical query responses
- 📊 Key academic metrics like SGPA and subject-wise insights
- 🧩 Scalable and distributed backend
- 🔒 High availability and reliability

---

## 🛠️ How to Run

Follow the steps below to run this project locally in a virtual environment:

1. Open VirtualBox and start your Ubuntu VM
2. Open the terminal and navigate to the Druid directory:
    - cd apache-druid-32.0.0
3. Start Druid using the quickstart command:
    - bin/start-micro-quickstart
4. Open your browser and go to:
   - https://localhost:8888

5. Ingest your academic data files one-by-one through the Druid web console.

6. Run SQL queries to analyze performance metrics such as SGPA and subject-wise scores.
