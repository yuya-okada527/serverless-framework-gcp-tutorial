# Serverless Framework Sample

## 構築手順

GCS から Pub/Sub への通知設定

```sh
$ gsutil notification create -f json -t projects/ml-playground-306716/topics/sample-notification-topic gs://sample-pub-sub-notification-bucket
```
