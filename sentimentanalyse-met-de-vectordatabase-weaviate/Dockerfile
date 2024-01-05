# 1. Neem de weaviate image, versie 1.22.0
FROM semitechnologies/weaviate:1.22.0

# 2. Stel de benodigde omgevingsvariabelen in
ENV OPENAI_APIKEY=$OPENAI_API_KEY
ENV QUERY_DEFAULTS_LIMIT=25
ENV AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=true
ENV AUTHENTICATION_SCHEME_NONE_ENABLED=true
ENV PERSISTENCE_DATA_PATH='/var/lib/weaviate'
ENV DEFAULT_VECTORIZER_MODULE='text2vec-openai'
ENV ENABLE_MODULES='text2vec-openai,generative-openai'
ENV CLUSTER_HOSTNAME='node1'

# 3. Zet poort 8080 open naar buiten
EXPOSE 8080

# 4. Zet de juiste http-configuratie als de container start
CMD ["--host", "0.0.0.0", "--port", "8080", "--scheme", "http"]
