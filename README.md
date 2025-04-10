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

## 🛠️ Prerequisites

1. **Aiven Account**  
   If you don’t have one, [sign up for free](https://console.aiven.io/signup) to get access to managed services like Kafka, PostgreSQL, and OpenSearch.

2. **Aiven API Token**  
   Generate one from the [Aiven Console](https://console.aiven.io/) under your profile settings — it’s required for Terraform provisioning.

3. **Terraform Installed**  
   Follow [Terraform's guide](https://developer.hashicorp.com/terraform/downloads) to install it on your system.

4. **Python 3.10+**

## 🧱 Architecture Overview

<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/b3c6bd3b-a792-4311-b658-05b06b527c4c" />

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

🎬 [Click here to watch the 10-minute demo](https://drive.google.com/file/d/1l81ItFywvSPyklzInQlJezGO8APngbv5/view?usp=drive_link)



















 
