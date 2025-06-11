# Litefold

Methods:

- <code title="get /">client.<a href="./src/litefold/_client.py">retrieve</a>() -> object</code>

# Upload

Methods:

- <code title="post /upload/fasta">client.upload.<a href="./src/litefold/resources/upload.py">create_fasta</a>(\*\*<a href="src/litefold/types/upload_create_fasta_params.py">params</a>) -> object</code>
- <code title="get /upload/stats">client.upload.<a href="./src/litefold/resources/upload.py">get_stats</a>() -> object</code>

# APIKeys

Types:

```python
from litefold.types import APIKeyCreateResponse, APIKeyListResponse, APIKeyRevokeResponse
```

Methods:

- <code title="post /api-keys">client.api_keys.<a href="./src/litefold/resources/api_keys.py">create</a>(\*\*<a href="src/litefold/types/api_key_create_params.py">params</a>) -> <a href="./src/litefold/types/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /api-keys">client.api_keys.<a href="./src/litefold/resources/api_keys.py">list</a>() -> <a href="./src/litefold/types/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="post /api-keys/revoke">client.api_keys.<a href="./src/litefold/resources/api_keys.py">revoke</a>(\*\*<a href="src/litefold/types/api_key_revoke_params.py">params</a>) -> <a href="./src/litefold/types/api_key_revoke_response.py">APIKeyRevokeResponse</a></code>

# StructurePrediction

Methods:

- <code title="get /structure-prediction/results/{job_name}">client.structure_prediction.<a href="./src/litefold/resources/structure_prediction.py">get_results</a>(job_name) -> object</code>
- <code title="get /structure-prediction/status/{job_name}">client.structure_prediction.<a href="./src/litefold/resources/structure_prediction.py">get_status</a>(job_name) -> object</code>
- <code title="post /structure-prediction/submit">client.structure_prediction.<a href="./src/litefold/resources/structure_prediction.py">submit</a>(\*\*<a href="src/litefold/types/structure_prediction_submit_params.py">params</a>) -> object</code>

# Health

Methods:

- <code title="get /health">client.health.<a href="./src/litefold/resources/health.py">check</a>() -> object</code>
