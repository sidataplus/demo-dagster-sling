from dagster import get_dagster_logger, file_relative_path, ExperimentalWarning
from dagster_embedded_elt.sling import SlingResource, SlingSourceConnection, SlingTargetConnection

import warnings
warnings.filterwarnings("ignore", category=ExperimentalWarning) 

logger = get_dagster_logger()

source = SlingSourceConnection(
    type="sqlite",
	instance=file_relative_path(__file__, "../data/src/eunomia.sqlite")
)

target_parquet = SlingTargetConnection(
    type="local",
    url="file:///"+file_relative_path(__file__, "../data/tgt/parquet/")
)

target_csv = SlingTargetConnection(
    type="local",
    url="file:///"+file_relative_path(__file__, "../data/tgt/csv/")
)

sling_parquet = SlingResource(source_connection=source, target_connection=target_parquet)
sling_csv = SlingResource(source_connection=source, target_connection=target_csv)
