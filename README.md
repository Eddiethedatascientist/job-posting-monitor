# job-posting-monitor
# Job Posting Monitor

A Python data pipeline that collects job postings from job websites, cleans them and brings them into one consistent format, with the goal of monitoring them over time and reporting changes by email.

> **Status: prototype.** Phase 1 (data collection and preparation) is done as a set of code experiments. Phase 2 (database, AI monitoring and email reports) is in progress and planned. This repository is not a finished application yet.

---

## Project overview

This is a personal project to practise the building blocks of a data pipeline: collecting data, cleaning it, normalising it, storing it and monitoring it for changes.

The idea is simple: many job websites load their postings from data endpoints behind the page. If those endpoints can be found and read, the postings can be collected automatically, stored, and compared over time to see what changed.

---

## Pipeline

```text
Find data endpoints
        ↓
Pull data with HTTP requests
        ↓
Data cleaning        (keep only the needed data)
        ↓
Data normalisation   (one consistent format)
        ↓
Database             (Phase 2, in progress)
        ↓
AI monitoring        (Phase 2, planned)
        ↓
Email report of changes
```

---

## Phase 1: data collection and preparation (done)

These steps have been tested as separate experiments.

1. **Finding data endpoints.** Looking for endpoints that return data, and confirming they respond with **status code 200**, which means the data can be pulled down.
2. **HTTP requests.** Sending requests to those endpoints and reading the data that comes back.
3. **Data cleaning.** The raw responses contain much more than is needed, so the data is filtered down to the job-related information only.
4. **Data normalisation.** Different sources describe the same thing in different ways, so the cleaned data is converted into **one common format**, ready to be stored in a SQL table.

### Normalised format

| Field | Description |
|---|---|
| `job_id` | Identifier of the posting |
| `title` | Job title |
| `location` | Where the job is located |
| `url` | Link to the original posting |

---

## Phase 2: database, monitoring and reporting (in progress / planned)

- [ ] Design the database (currently learning SQL and database fundamentals: entities, attributes and structure)
- [ ] Store the normalised postings in the database
- [ ] Compare newly collected data with the stored data to detect changes
- [ ] Use AI to monitor continuously and to tell **real changes** from **different wording** of the same posting
- [ ] Send an **email report** summarising the changes over a recent period (for example, the last 2 hours)

---

## Technologies

- Python
- HTTP requests and web data endpoints
- Data cleaning and normalisation
- SQL and databases (learning, planned for Phase 2)
- AI-based monitoring and email reporting (planned)

---

## Repository contents

- `experiments/`: the scripts for each Phase 1 step (endpoints, requests, cleaning, normalisation)
- `sample_data/`: a small sample of the normalised output

---

## Responsible use

Only use data endpoints that are publicly accessible. Check the terms of use and `robots.txt` of each website before collecting data, keep the request rate reasonable, and never commit credentials or API keys to this repository.

---

## Author

**Eddie Nguyen**

Bachelor's Programme in Computer Science and Engineering

University of Oulu
