import csv
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RISK_CONTROLS_FILE_PATH = (
    PROJECT_ROOT
    / "output_examples"
    / "risk_controls_matrix.csv"
)

REQUIRED_COLUMNS = {
    "risk_id",
    "risk_description",
    "control_id",
    "control_activity",
    "control_type",
    "control_owner",
    "related_requirements",
    "related_uat_test_cases",
}

EXPECTED_ROW_COUNT = 20

def validate_risk_controls_csv() -> int:
    if not RISK_CONTROLS_FILE_PATH.exists():
        print(
            "ERROR: Risk and controls CSV file not found:\n"
            f"{RISK_CONTROLS_FILE_PATH}"
        )
        return 1
    
    errors: list[str] = []

    with RISK_CONTROLS_FILE_PATH.open(
        mode="r",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        csv_reader=csv.DictReader(csv_file)

        if csv_reader.fieldnames is None:
            print("ERROR: CSV header is missing.")
            return 1
        
        column_names = csv_reader.fieldnames
        rows = list(csv_reader)

    missing_columns = REQUIRED_COLUMNS - set(column_names)

    if missing_columns:
        errors.append(
            "Missing required columns: "
            f"{sorted(missing_columns)}"
        )

    if len(rows) != EXPECTED_ROW_COUNT:
        errors.append(
            f"Expected {EXPECTED_ROW_COUNT} data rows, "
            f"but found {len(rows)}."
        )

    risk_ids: set[str] = set()
    control_ids: set[str] = set()

    for row_number, row in enumerate(rows, start=2):
        extra_values = row.get(None)

        if extra_values:
            errors.append(
                f"Row {row_number}: extra values detected: "
                f"{extra_values}"
            )

        missing_row_columns = [
            column_name
            for column_name in column_names
            if row.get(column_name) is None
        ]

        if missing_row_columns:
            errors.append(
                f"Row {row_number}: fewer values than expected. "
                f"Missing values for columns: {missing_row_columns}"
            )
            continue

        risk_id=row["risk_id"].strip()
        control_id=row["control_id"].strip()

        if not risk_id:
            errors.append(
                f"Row {row_number}: risk_id is blank."
            )
        elif risk_id in risk_ids:
            errors.append(
                f"Row {row_number}: duplicate risk_id '{risk_id}'."
            )
        else:
            risk_ids.add(risk_id)

        if not control_id:
            errors.append(
                f"Row {row_number}: control_id is blank."
            )
        elif control_id in control_ids:
            errors.append(
                f"Row {row_number}: duplicate control_id "
                f"'{control_id}'."          
            )
        else:
            control_ids.add(control_id)

        for required_column in REQUIRED_COLUMNS:
            if required_column in row:
                if not row[required_column].strip():
                    errors.append(
                        f"Row {row_number}: "
                        f"{required_column} is blank."
                    )

    print(f"File: {RISK_CONTROLS_FILE_PATH}")
    print(f"Columns detected: {len(column_names)}")
    print(f"Data rows detected: {len(rows)}")
    print(f"Unique risks detected: {len(risk_ids)}")
    print(f"Unique controls detected: {len(control_ids)}")

    if errors:
        print(
            f"\nValidation failed with "
            f"{len(errors)} error(s):"
        )

        for error in errors:
            print(f"- {error}")

        return 1
    
    print("\nRisk and controls CSV calidation passed.")


def main() -> int:
    return validate_risk_controls_csv()


if __name__ == "__main__":
    sys.exit(main())