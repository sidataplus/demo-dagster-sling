from dagster import AssetSpec, ExperimentalWarning
from dagster_embedded_elt.sling import SlingMode, build_sling_asset

import warnings
warnings.filterwarnings("ignore", category=ExperimentalWarning) 


asset_def = build_sling_asset(
	sling_resource_key="sling_parquet",
    asset_spec=AssetSpec(key="person_parquet", group_name="cdm"),
    source_stream="main.PERSON",
    target_object="person",
	target_options={"format": "parquet", "file_max_bytes": 4000000},
    mode=SlingMode.INCREMENTAL,
    primary_key="PERSON_ID"
)


asset_def_csv = build_sling_asset(
	sling_resource_key="sling_csv",
    asset_spec=AssetSpec(key="person_csv", group_name="cdm", deps=["person_parquet"]),
    source_stream='SELECT * FROM main.PERSON WHERE gender_source_value = "F"',
    target_object="person_csv",
	target_options={"format": "csv", "file_max_bytes": 4000000},
    mode=SlingMode.INCREMENTAL,
    primary_key="PERSON_ID",
)
