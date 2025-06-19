from typing import Any, Dict

import requests

from prefect import task

BACKEND_URL = "http://backend:5000/api"


@task
def register_file(
    file_data: Dict[str, str],
    endpoint: str = f"{BACKEND_URL}/files",
    verify: bool = True,
) -> Any:
    print(f"Creating file: {file_data}")
    response = requests.post(url=endpoint, json=file_data, verify=verify)
    response.raise_for_status()
    return response.json()
