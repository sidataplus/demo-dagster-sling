from dagster import (
    Definitions,
    ScheduleDefinition,
	AssetSelection,
    define_asset_job,
    load_assets_from_modules,
)

from . import assets, resources

all_assets = load_assets_from_modules([assets])

all_assets_job = define_asset_job(name="all_assets_job", selection=AssetSelection.all())

daily_refresh_schedule = ScheduleDefinition(
    job=all_assets_job,
    # cron_schedule="0 0 * * *", # every day at midnight
    # cron_schedule="0 1 * * *", # every day at 1am
	cron_schedule="* * * * *", # every minute
)

defs = Definitions(
	resources={
        "sling_parquet": resources.sling_parquet,
        "sling_csv": resources.sling_csv,
    },
    assets=all_assets,
	jobs=[all_assets_job],
    schedules=[daily_refresh_schedule],
)
