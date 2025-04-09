import json
from datetime import datetime, timezone
from confluent_kafka import Consumer
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests.auth import HTTPBasicAuth

# === Kafka config ===
kafka_config = {
    'bootstrap.servers': 'demo-kafka-real-time-demo.e.aivencloud.com:11859',
    'security.protocol': 'SSL',
    'ssl.ca.location': 'ca.pem',
    'ssl.certificate.location': 'service.cert',
    'ssl.key.location': 'service.key',
    'group.id': 'opensearch-consumer-group',
    'auto.offset.reset': 'earliest'
}

# === OpenSearch config ===
opensearch = OpenSearch(
    hosts=[{
        'host': 'demo-opensearch-real-time-demo.e.aivencloud.com',
        'port': 11857
    }],
    http_auth=HTTPBasicAuth('avnadmin', 'AVNS__2pghAaCYe5SJ9t0vdc'),
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

INDEX_NAME = "clickstream-events"

# Create index if it doesn't exist
if not opensearch.indices.exists(INDEX_NAME):
    opensearch.indices.create(INDEX_NAME)
    print(f"✅ Created OpenSearch index: {INDEX_NAME}")

# === Kafka consumer ===
consumer = Consumer(kafka_config)
consumer.subscribe(["clickstream-events"])

print("📥 Consuming from Kafka and streaming to OpenSearch...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Kafka error:", msg.error())
            continue

        event = json.loads(msg.value().decode("utf-8"))

        # Add timestamp field (timezone-aware and OpenSearch-friendly)
        event["@timestamp"] = datetime.now(timezone.utc).isoformat()

        # Send to OpenSearch using 'body=' instead of 'document='
        response = opensearch.index(index=INDEX_NAME, body=event)
        print(f"✅ Indexed event {event['event_id']}")

except KeyboardInterrupt:
    print("🛑 Stopped by user.")
finally:
    consumer.close()
