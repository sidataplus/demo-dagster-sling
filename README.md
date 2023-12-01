# Demo Dagster Sling

In this demo, we will create a simple ELT pipeline using [Sling](https://slingdata.io) and [Dagster](https://dagster.io).

We will extract data from SQLite database of [OMOP CDM Data called Eunomia](https://github.com/OHDSI/Eunomia/tree/main/inst/sqlite) store in `data/src`, and load data into Parquet files at `data/tgt` with Sling. Then we will use Dagster to schedule the pipeline and monitor the pipeline runs.

We will follow this [Dagster Documentation: Embedded ELT](https://docs.dagster.io/integrations/embedded-elt) to create the pipeline.
See detailed step-by-step instructions in [how-to.md](how-to.md).

## Why Dagster & Sling

- Sling is a simple EL tool that can be used as CLI or Python wrapper.
- Dagster is an asset-based orchrestation tool, while Airflow is a task-based tool. [Read more](https://dagster.io/vs/dagster-vs-airflow)

## Why not

- Slink is still new, albeit version 1 is available. Watch for updates on [GitHub](https://github.com/slingdata-io/sling-cli).
- Dagster has role-based access control (RBAC) but limited to Dagster Cloud version. Airflow has [RBAC](https://airflow.apache.org/docs/apache-airflow/stable/security/access-control.html).

## What's next

This demo uses SQLite for simplicity. Sling is able to connect to many other databases such as MS SQL Server, PostgreSQL, Oracle and major cloud DB. See [Sling documentation](https://docs.slingdata.io/connections/database-connections) for more details.

From the Parquet file, we can load it into a data lake or, even better, a data lakehouse. Parquet files can be handled and managed by [Apache Iceberg](https://iceberg.apache.org/) via [Dremio](https://www.dremio.com/) or [Apache Spark](https://spark.apache.org/).
