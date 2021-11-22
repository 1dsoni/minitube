# Minitube

Steps to run
1. clone the repo
2. docker-compose up [first run might take around 10-15 minutes to build]
3. wait for all services to come up, it takes around 2-3 minutes to come up post build step
4. initial setup:
    ```
   a. create an index in the elastic search via:
         curl --location --request PUT 'http://localhost:9200/youtube_videos' \
         --header 'Content-Type: application/json' \
         --data-raw '{
             "mappings": {
                 "properties": {
                     "video_id": {
                         "type": "keyword"
                     },
                     "thumbnail": {
                         "type": "keyword",
                         "index": false
                     },
                     "title": {
                         "type": "search_as_you_type"
                     },
                     "description": {
                         "type": "text"
                     },
                     "published_at": {
                         "type": "search_as_you_type"
                     }
                 }
             }
         }'
  
   b. add api key(s):
      curl --location --request POST 'localhost:8000/api/v1/api-key/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "name": "youtube_crawler_api_key",
            "identifier": "15199dcf-30f4-4fb0-88a5-d65a27bf3e25",
            "key": "api key",
            "key_config": null,
            "is_active": true
        }'

   c. create crawler(s):
        curl --location --request POST 'localhost:8000/api/v1/crawler/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "name": "youtube_moon_landing",
            "crawler": "youtube",
            "crawler_config":{
                "query": "moon landing"
            },
            "run_after_seconds": 10,
            "status": "stopped",
            "is_enabled": true
        }'
   d. start crawler:
        curl --location --request POST 'localhost:8000/api/v1/crawler/init/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "name": "youtube_moon_landing"
        }'
   
   e. search items:
        curl --location --request GET 'localhost:8000/api/v1/search/yt/?query=landing' \
        --header 'Content-Type: application/json'
    ```

### Overview
- the crawler uses the api keys to fetch "queries"
- the fetched items are sent for indexing via kafka queue
- the indexer picks items from kafka queue and indexes it into elastic search
- the webserver queries the elastic search for the items