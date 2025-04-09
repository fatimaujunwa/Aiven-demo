terraform {
  required_providers {
    aiven = {
      source  = "aiven/aiven"
      version = "~> 4.0"
    }
  }
}

provider "aiven" {
  api_token = var.aiven_api_token
}

resource "aiven_kafka" "kafka" {
  project      = var.project_name
  cloud_name   = "google-europe-west1"
  plan         = "business-4"
  service_name = "demo-kafka"
}

resource "aiven_pg" "postgresql" {
  project      = var.project_name
  cloud_name   = "google-europe-west1"
  plan         = "business-4"
  service_name = "demo-postgres"
}

resource "aiven_opensearch" "opensearch" {
  project      = var.project_name
  cloud_name   = "google-europe-west1"
  plan         = "startup-4" # 👈 lighter plan for dashboards
  service_name = "demo-opensearch"
}
resource "aiven_kafka_topic" "clickstream" {
  project      = aiven_kafka.kafka.project
  service_name = aiven_kafka.kafka.service_name
  topic_name   = "clickstream-events"
  partitions   = 3
  replication  = 2
}


resource "aiven_kafka_acl" "clickstream_producer" {
  project      = aiven_kafka.kafka.project
  service_name = aiven_kafka.kafka.service_name
  permission   = "write"
  topic        = "clickstream-events"
  username     = "avnadmin"
}

