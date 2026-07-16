import csv
import sys
from pathlib import Path

CSV_FILE_PATH = (
    Path(__file__).resolve().parents[1]
    / "sample_data"
    / "payment_exceptions_sample.csv"
)

VALID_PRIORITIES = (
    "Low",
    "Medium",
    "High",
    "Critical",
)

VALID_STATUSES = (
    "New",
    "In Review",
    "Pending External Response",
    "Escalated",
    "Resolved",
    "Closed",
)

VALID_BOOLEAN_VALUES = (
    "Yes",
    "No",
)

BOOLEAN_COLUMNS = (
    "customer_impact_flag",
    "high_value_flag",
    "duplicate_risk_flag",
    "sla_breach_flag",
    "aged_exception_flag",
    "escalation_flag",
    "open_case_flag",
    "unassigned_case_flag",
    "management_review_flag",
)

def add_error(
        errors: list[str],
        row_number: int,
        message: str,
) -> None:
    errors.append(f"Row {row_number}: {message}")

def validate_csv() -> int:
    if not CSV_FILE_PATH.exists():
        print(f"ERROR: CSV file not found: {CSV_FILE_PATH}")
        return 1
    
    errors: list[str] = []

    with CSV_FILE_PATH.open(
        mode="r",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        if csv_reader.fieldnames is None:
            print("ERROR: CSV header is missing.")
            return 1
        
        column_names=csv_reader.fieldnames
        rows = list(csv_reader)
    
    if not rows:
        print("ERROR: CSV contains no data rows.")
        return 1
    
    case_ids: set[str] = set()

    for row_number, row in enumerate(rows, start=2):
        extra_values = row.get(None)

        if extra_values:
            add_error(
                errors,
                row_number,
                f"row contains extra values: {extra_values}",
            )
        
        missing_columns = [
            column_name
            for column_name in column_names
            if row.get(column_name) is None
        ]

        if missing_columns:
            add_error(
                errors,
                row_number,
                f"row contains fewer values than the header. "
                f"Missing columns: {missing_columns}",
            )
            continue

        case_id = row["case_id"].strip()
        status = row["status"].strip()
        priority = row["priority"].strip()

        if not case_id:
            add_error(errors, row_number, "case_id is blank.")
        elif case_id in case_ids:
            add_error(
                errors, row_number,
                f"duplicate case_idL {case_id}",
            )
        else:
            case_ids.add(case_id)

        if priority not in VALID_PRIORITIES:
            add_error(
                errors,
                row_number,
                f"invalid priority '{priority}'"
            )
        
        for boolean_column_name in BOOLEAN_COLUMNS:
            boolean_value = row[boolean_column_name].strip()

            if boolean_value not in VALID_BOOLEAN_VALUES:
                add_error(
                    errors,
                    row_number,
                    f"{boolean_column_name} must be Yes or No, "
                    f"but contains '{boolean_value}'",
                )

        if status == "Closed":
            if not row["closure_reason"].strip():
                add_error(
                    errors,
                    row_number,
                    f"{case_id}: closed case has no closure reason.",
                )

            if not row["closed_date"].strip():
                add_error(
                    errors,
                    row_number,
                    f"{case_id}: closed case has no closed date.",
                )
            
            if not row["investigation_notes"].strip():
                add_error(
                    errors,
                    row_number,
                    f"{case_id}: closed case has no investigation notes.",
                )

        if row["open_case_flag"].strip() == "Yes":
            if not row["sla_due_date"].strip():
                add_error(
                    errors,
                    row_number,
                    f"{case_id}: open case has no SLA due date.",
                )
        
        if row["high_value_flag"].strip() == "Yes":
            if priority not in {"High", "Critical"}:
                add_error(
                    errors,
                    row_number,
                    f"{case_id}: high-value case has priority {priority}.",
                )
        
        if row["duplicate_risk_flag"].strip() == "Yes":
            if priority not in {"High", "Critical"}:
                add_error(
                    errors,
                    row_number,
                    f"{case_id}: duplicate-risk case has priority {priority}.",
                )

    print(f"File: {CSV_FILE_PATH}")
    print(f"Columns detected: {len(column_names)}")
    print(f"Data rows detected: {len(rows)}")

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s):")

        for error in errors:
            print(f"- {error}")
        
        return 1
    
    print("\nSample dataset validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(validate_csv())