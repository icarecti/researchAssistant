# ResearchAssistant

![researchAssistant](https://github.com/icarecti/researchAssistant/assets/79723245/e6bdfc78-f490-42fb-a91c-ad7d9955c369)

Struggling to stay abreast with the dynamic advancements in the field of AI, often overwhelmed by the sheer volume of incoming information? Let your worries be a thing of the past with researchAssistant - your personal AI-powered ally. Simply feed it a list of URLs, and it will dutifully scan, summarize, and rank the information, presenting you with a detailed analysis for each source. The beauty lies in the seamless integration of these analyses into Obsidian, making the once overwhelming information instantly navigable. ResearchAssistant transforms your digital research experience, ensuring you never miss a beat in the fast-paced world of AI (or any other field of your interest).

# How it works and what is planned

![Untitled-2023-03-28-0034_dark](https://github.com/icarecti/researchAssistant/assets/79723245/78bfcf09-9ef1-466f-b9e5-b1e53624359e)

# Getting Started

## Prerequisites

Before starting the app you should have Obsidian installed on your computer and set some variables in the .env file. Use the .env-example as a template. Add you
keys and folder path and rename it to .env.

## start the app via docker

```

docker-compose up -d

```

## start the app directly

```

# 1. activate python3 venv

source venv/bin/activate

# 2. install requirements

pip3 install -r requirements.txt

# 3. then start the app.py

python3 app.py

```
## how to use the app
Once the app is started there are two rest enpoints that can be triggered. These will be triggered in the future by a browser plugin. For now they have to be triggered manually:

1. **Analyse URLs**: send a POST request with a list of URLS to http://localhost:5000/urls
```
curl --location 'http://localhost:5000/urls' \
--header 'Content-Type: application/json' \
--data '{
    "urls": ["https://some-example-url.com", "https://www.a-second-example-url.com/lates/post"]
}'
```

2. **Create Canvas**: send a GET request to http://localhost:5000/knowledgeMap
```
curl --location 'http://localhost:5000/knowledgeMap'
```


