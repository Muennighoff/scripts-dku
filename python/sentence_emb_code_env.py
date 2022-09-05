######################## Base imports #################################
import logging
import os
import shutil

from dataiku.code_env_resources import clear_all_env_vars
from dataiku.code_env_resources import grant_permissions
from dataiku.code_env_resources import set_env_path
from dataiku.code_env_resources import set_env_var
from dataiku.code_env_resources import update_models_meta

# Set-up logging
logging.basicConfig()
logger = logging.getLogger("code_env_resources")
logger.setLevel(logging.INFO)

# Clear all environment variables defined by a previously run script
clear_all_env_vars()

######################## Sentence Transformers #################################
# Set sentence_transformers cache directory
set_env_path("SENTENCE_TRANSFORMERS_HOME", "sentence_transformers")

import sentence_transformers

# Download pretrained models
MODELS_REPO_AND_REVISION = [
    ("DataikuNLP/average_word_embeddings_glove.6B.300d", "52d892b217016f53b6c717839bf62c746a658933"),
    ("DataikuNLP/TinyBERT_General_4L_312D", "33ec5b27fcd40369ff402c779baffe219f5360fe"),
    ("DataikuNLP/paraphrase-multilingual-MiniLM-L12-v2", "4f806dbc260d6ce3d6aed0cbf875f668cc1b5480"),
]

sentence_transformers_cache_dir = os.getenv("SENTENCE_TRANSFORMERS_HOME")
for (model_repo, revision) in MODELS_REPO_AND_REVISION:
    logger.info("Loading pretrained SentenceTransformer model: {}".format(model_repo))
    model_path = os.path.join(sentence_transformers_cache_dir, model_repo.replace("/", "_"))
    
    # Uncomment below to overwrite (force re-download of) all existing models
    # if os.path.exists(model_path):
    #     logger.warning("Removing model: {}".format(model_path))
    #     shutil.rmtree(model_path)

    # This also skips same models with a different revision
    if not os.path.exists(model_path):
        model_path_tmp = sentence_transformers.util.snapshot_download(
            repo_id=model_repo,
            revision=revision,
            cache_dir=sentence_transformers_cache_dir,
            library_name="sentence-transformers",
            library_version=sentence_transformers.__version__,
            ignore_files=["flax_model.msgpack", "rust_model.ot", "tf_model.h5",],
        )
        os.rename(model_path_tmp, model_path)
    else:
        logger.info("Model already downloaded, skipping")
# Add sentence embedding models to the code-envs models meta-data
# (ensure that they are properly displayed in the feature handling)
update_models_meta()
# Grant everyone read access to pretrained models in sentence_transformers/ folder
# (by default, sentence transformers makes them only readable by the owner)
grant_permissions(sentence_transformers_cache_dir)
