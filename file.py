from google.cloud import bigquery
import time

# def load_data_from_file(dataset_name, table_name, source_file_name):
#     bigquery_client = bigquery.Client()
#     dataset = bigquery_client.dataset(dataset_name)
#     table = dataset.table(table_name)
#
#     # Reload the table to get the schema.
#     table.reload()
#
#     with open(source_file_name, 'rb') as source_file:
#         # This example uses CSV, but you can use other formats.
#         # See https://cloud.google.com/bigquery/loading-data
#         job = table.upload_from_file(
#             source_file, source_format='text/csv')
#
#     wait_for_job(job)
#
#     print('Loaded {} rows into {}:{}.'.format(
#         job.output_rows, dataset_name, table_name))
#
# def wait_for_job(job):
#     while True:
#         job.reload()
#         if job.state == 'DONE':
#             if job.error_result:
#                 raise RuntimeError(job.errors)
#             return
#         time.sleep(1)
#
#
# load_data_from_file("PlantOS", "sample_data", "/Users/aryan/Desktop/personal_projects/PlantOS/gcp/WorkBook1.csv")

client = bigquery.Client()
QUERY = ('SELECT name, state, number,  FROM [bigquery-public-data:usa_names.usa_1910_2013]')
query = client.run_sync_query('%s LIMIT 100' % QUERY)
query.timeout_ms = 10000
query.run()

for row in query.rows:
    print(row)

print len(query.rows)