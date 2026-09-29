select
  cast(record_id as varchar) as record_id,
  cast(signal_a as integer) as signal_a,
  cast(signal_b as double) as signal_b,
  priority
from read_csv_auto('../data/sample.csv')
