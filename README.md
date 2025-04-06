# 📊 Real-Time Website Analytics with Aiven

This proof of concept demonstrates how a team can capture and analyze real-time website activity — including page views, session duration, and user engagement — using fully managed Aiven services.

It’s designed for product, engineering, and analytics teams that need live insight into user behavior without managing infrastructure manually.

---

## 💡 What This Solves

> "We want to understand what users are doing on our website — right now — and turn that into live, actionable insight."

This PoC provides:
- **Kafka** for real-time event ingestion  
- **PostgreSQL** for structured session storage  
- **OpenSearch** for dashboards and visualizations  
- **Terraform** for fully automated provisioning

---

## 🧱 Architecture Overview

```text
                [Simulated User Activity]
                           |
                    (Clickstream Events)
                           ↓
              ┌────────────────────────┐
              │   Aiven for Kafka      │
              │   (Event Ingestion)    │
              └────────────────────────┘
                           ↓
        ┌──────────────────────────┐         ┌────────────────────────────┐
        │ Aiven for PostgreSQL     │         │ Aiven for OpenSearch       │
        │ (Session Storage via SQL)│         │ (Live Dashboards & Charts) │
        └──────────────────────────┘         └────────────────────────────┘

 
