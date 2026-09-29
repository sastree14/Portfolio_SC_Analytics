from evidently import Report
from evidently.presets import DataDriftPreset

def build_drift_report(reference, current):
    report=Report([DataDriftPreset()])
    result=report.run(reference_data=reference,current_data=current)
    return result
