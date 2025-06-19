from prefect import flow

from .example_flow_parameters import request_parameters
from .example_task import register_file


@flow(
    name="register-file",
    retries=2,
    retry_delay_seconds=15,
    log_prints=True,
)
def register_file_flow(
    path: str,
    name: str,
) -> None:
    register_file(file_data={"path": path, "name": name})


if __name__ == "__main__":
    register_file_flow(path="path1", name="name1")
