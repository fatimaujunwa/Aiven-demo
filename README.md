# 📊 Real-Time Website Analytics with Aiven

This proof of concept demonstrates how your team can track real-time website user activity — such as page visits, session flows, and user engagement — using Aiven’s fully managed services.

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
```

## ⚙️ How to Run the Demo

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/aiven-realtime-demo.git
cd aiven-realtime-demo
```

---

### 2. Provision Infrastructure with Terraform


```bash
cd terraform
terraform init
terraform apply
```
### 3. Simulate User Click Events
```bash
python producer/clickstream_producer.py
```
### 4. Process Data into PostgreSQL
```bash
python consumer/clickstream_consumer.py
```
### 5. Stream Events to OpenSearch

```bash
python opensearch/clickstream_to_opensearch.py

```
## 🗄️ PostgreSQL Data Example
Here's a snapshot of structured clickstream data stored in PostgreSQL:
<img width="666" alt="Image" src="https://github.com/user-attachments/assets/eb37c3c0-1ed0-436a-9808-981e9dbfbd64" />

## 📸 OpenSearch Dashboards
###  User Distribution
<img width="886" alt="Image" src="https://github.com/user-attachments/assets/70916936-16bb-481f-bc8d-8cbb293bbfd3" />

### Top Visited pages
<img width="892" alt="Image" src="https://github.com/user-attachments/assets/81002b6d-da14-4ffb-8fcd-30561590a590" />

### Event Timeline
<img width="899" alt="Image" src="https://github.com/user-attachments/assets/a15ddff8-a4a6-47ea-b06f-660bbb291a97" />





## 🧹 Clean-Up (Preserve Trial Credits)
To safely remove all services and resources:
```bash
terraform destroy
```
## 📦 Requirements
Install Python dependencies:

```bash
pip install -r requirements.txt

```
## 📽️ Demo Walkthrough Video

🎬 [Click here to watch the 10-minute demo](https://your-demo-video-link.com)



















 
