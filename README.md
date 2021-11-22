# Minitube

Steps to run
1. clone the repo
2. docker-compose up
3. wait for all services to come up, takes around 2-3 mins
4. initial setup:
    ```
   a. add api key(s):
      curl --location --request POST 'localhost:8000/api/v1/api-key/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "name": "youtube_crawler_api_key",
            "identifier": "15199dcf-30f4-4fb0-88a5-d65a27bf3e25",
            "key": "api key",
            "key_config": null,
            "is_active": true
        }'

   b. create crawler(s):
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
   c. start crawler:
        curl --location --request POST 'localhost:8000/api/v1/crawler/init/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "name": "youtube_moon_landing"
        }'
   
   d. search items:
        curl --location --request GET 'localhost:8000/api/v1/search/yt/?query=landing' \
        --header 'Content-Type: application/json'
    ```