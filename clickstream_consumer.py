import json
import psycopg2
from confluent_kafka import Consumer

# === Kafka config (same as your producer, plus group.id) ===
kafka_config = {
    'bootstrap.servers': 'demo-kafka-real-time-demo.e.aivencloud.com:11859',
    'security.protocol': 'SSL',
    'ssl.ca.location': 'ca.pem',
    'ssl.certificate.location': 'service.cert',
    'ssl.key.location': 'service.key',
    'group.id': 'clickstream-consumer-group',
    'auto.offset.reset': 'earliest'
}

# === PostgreSQL config (replace with your actual Aiven info) ===
pg_conn = psycopg2.connect(
    dbname="defaultdb",
    user="avnadmin",
    password="AVNS_hGUNb1DXzjMRfty7wBK",
    # ← Reveal and paste password
    host="demo-postgres-real-time-demo.e.aivencloud.com",
    port=11857,
    sslmode="require"
)
pg_cursor = pg_conn.cursor()

# === Kafka Consumer setup ===
consumer = Consumer(kafka_config)
consumer.subscribe(["clickstream-events"])

print("📥 Listening for clickstream events...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Kafka error:", msg.error())
            continue

        data = json.loads(msg.value().decode("utf-8"))
        print("📥 Event received:", data)

        pg_cursor.execute("""
            INSERT INTO sessions (event_id, user_id, page, timestamp)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (event_id) DO NOTHING;
        """, (
            data["event_id"],
            data["user_id"],
            data["page"],
            data["timestamp"]
        ))

        pg_conn.commit()

except KeyboardInterrupt:
    print("🛑 Stopping consumer...")

finally:
    consumer.close()
    pg_cursor.close()
    pg_conn.close()
