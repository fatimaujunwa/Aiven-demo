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

## 📸 OpenSearch Dashboards

## 🧹 Clean-Up (Preserve Trial Credits)
To safely remove all services and resources:
```bash
terraform destroy
```
## 📦 Requirements

```bash
pip install -r requirements.txt

```
## 📽️ Demo Walkthrough Video

🎬 [Click here to watch the 10-minute demo](https://your-demo-video-link.com)



















 
