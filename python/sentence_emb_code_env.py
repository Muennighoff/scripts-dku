## Base imports
from dataiku.code_env_resources import clear_all_env_vars
from dataiku.code_env_resources import set_env_path
from dataiku.code_env_resources import set_env_var

# Clears all environment variables defined by previously run script
# clear_all_env_vars()

## Hugging Face
# Set HuggingFace cache directory
set_env_path("SENTENCE_TRANSFORMERS_HOME", "sentence_transformers")

# Import sentence transformers
from sentence_transformers import SentenceTransformer

# Download pretrained models
MODEL_IDENTIFIERS = [
    "DataikuNLP/paraphrase-albert-small-v2",
    "DataikuNLP/average_word_embeddings_glove.6B.300d",
    "DataikuNLP/paraphrase-MiniLM-L6-v2",
    "DataikuNLP/TinyBERT_General_4L_312D",
    "DataikuNLP/camembert-base",
    "DataikuNLP/distiluse-base-multilingual-cased-v1",
    "DataikuNLP/paraphrase-multilingual-MiniLM-L12-v2",
]

for model_identifier in MODEL_IDENTIFIERS:
    SentenceTransformer(model_identifier)
