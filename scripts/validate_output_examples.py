import csv
import re
import sys
from pathlib import Path
from typing import Callable

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RISK_CONTROLS_FILE_PATH = (
    PROJECT_ROOT
    / "output_examples"
    / "risk_controls_matrix.csv"
)

UAT_TEST_CASES_FILE_PATH = (
    PROJECT_ROOT
    / "output_examples"
    / "uat_test_cases.csv"
)

TRACEABILITY_FILE_PATH = (
    PROJECT_ROOT
    / "output_examples"
    / "requirements_traceability_matrix.csv"
)

RISK_CONTROLS_REQUIRED_COLUMNS = {
    "risk_id",
    "risk_description",
    "risk_category",
    "inherent_risk_rating",
    "control_id",
    "control_activity",
    "control_type",
    "control_frequency",
    "control_owner",
    "control_evidence",
    "residual_risk_rating",
    "related_requirements",
    "related_uat_test_cases",
}

UAT_REQUIRED_COLUMNS = {
    "test_case_id",
    "test_case_name",
    "test_area",
    "objective",
    "preconditions",
    "test_data",
    "test_steps",
    "expected_result",
    "related_requirements",
    "related_business_rules",
    "related_controls",
    "business_priority",
    "execution_status",
    "actual_result",
    "defect_id",
    "retest_status",
}

TRACEABILITY_REQUIRED_COLUMNS = {
    "trace_id",
    "business_objective",
    "business_requirement",
    "solution_requirement",
    "user_story",
    "business_rule",
    "risk_id",
    "control_id",
    "uat_test_case",
    "coverage_status",
}

VALID_RISK_RATING = {
    "Low",
    "Medium",
    "High",
    "Critical",
}

VALID_CONTROL_TYPES = {
    "Preventive",
    "Detective",
    "Preventive / Detective",
}

VALID_BUSINESS_PRIORITIES = {
    "Must Have",
    "Should Have",
    "Could Have",
    "Won't Have",
}

VALID_EXECUTION_STATUSES = {
    "Not Run",
    "Passed",
    "Failed",
    "Blocked",
}

VALID_RETEST_STATUSES = {
    "Not Required",
    "Pending",
    "Passed",
    "Failed",
}

VALID_COVERAGE_STATUSES = {
    "Covered",
    "Partially Covered",
    "Gap",
}


def read_csv_file(
    file_path: Path,
) -> tuple[list[str] | None, list[dict[str, str]]]:
    with file_path.open(
        mode="r",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        if csv_reader.fieldnames is None:
            return None, []
        
        return csv_reader.fieldnames, list(csv_reader)
    
def validate_csv_structure(
        file_name: str,
        file_path: Path,
        required_columns: set[str],
        expected_row_count: int,
        unique_columns: list[str],
) -> tuple[list[str], list[str], list[dict[str, str]]]:
    errors: list[str] = []

    if not file_path.exists():
        errors.append(
            f"{file_name}: file not found: {file_path}"
        )
        return errors, [],[]
    
    column_names, rows = read_csv_file(file_path)

    if column_names is None:
        errors.append(
            f"{file_name}: CSV header is missing."
        )
        return errors, [], []
    
    missing_required_columns = (
        required_columns - set(column_names)
    )

    if missing_required_columns:
        errors.append(
            f"{file_name}: expected {expected_row_count} rows "
            f"but found {len(rows)}."
        )

    unique_values: dict[str, set[str]] = {
        column_name: set()
        for column_name in unique_columns
    }

    for row_number, row in enumerate(rows, start=2):
        extra_values = row.get(None)

        if extra_values:
            errors.append(
                f"{file_name} row {row_number}: "
                f"extra values detected: {extra_values}"
            )

        missing_row_values = [
            column_name
            for column_name in column_names
            if row.get(column_name) is None
        ]

        if missing_row_values:
            errors.append(
                f"{file_name} row {row_number}: "
                f"fewer values than expected. "
                f"Missing values for: {missing_row_values}"
            )
            continue

        for required_column in required_columns:
            if required_column not in row:
                continue

            if not row[required_column].strip():
                errors.append(
                    f"{file_name} row {row_number}: "
                    f"{required_column} is blank."
                )

        for unique_column in unique_columns:
            if unique_column not in row:
                continue

            unique_value = row[unique_column].strip()

            if not unique_value:
                continue

            if unique_value in unique_values[unique_column]:
                errors.append(
                    f"{file_name} row {row_number}: "
                    f"duplicate {unique_column} "
                    f"'{unique_value}'."
                )

    return errors, column_names, rows

def validate_allowed_value(
        errors: list[str],
        file_name: str,
        row_number: int,
        column_name: str,
        value: str,
        allowed_values: set[str],
) -> None:
    if value not in allowed_values:
        errors.append(
            f"{file_name} row {row_number}: "
            f"invalid {column_name} '{value}'. "
            f"Allowed values: {sorted(allowed_values)}"
        )

def validate_risk_controls() -> list[str]:
    file_name = "Risk and controls CSV"

    errors, column_names, rows = validate_csv_structure(
        file_name=file_name,
        file_path=RISK_CONTROLS_FILE_PATH,
        required_columns = RISK_CONTROLS_REQUIRED_COLUMNS,
        expected_row_count=20,
        unique_columns=["risk_id", "control_id"],
    )

    structurally_valid = (
        column_names
        and RISK_CONTROLS_REQUIRED_COLUMNS.issubset(
            set(column_names)
        )
    )
    
    if structurally_valid:
        for row_number, row in enumerate(rows, start=2):
            validate_allowed_value(
                errors=errors,
                file_name=file_name,
                row_number=row_number,
                column_name="inherent_risk_rating",
                value=row["inherent_risk_rating"].strip(),
                allowed_values=VALID_RISK_RATING,
            )

            validate_allowed_value(
                errors=errors,
                file_name=file_name,
                row_number=row_number,
                column_name="residual_risk_rating",
                value=row["residual_risk_rating"].strip(),
                allowed_values=VALID_RISK_RATING,
            )

            validate_allowed_value(
                errors=errors,
                file_name=file_name,
                row_number=row_number,
                column_name="control_type",
                value=row["control_type"].strip(),
                allowed_values=VALID_CONTROL_TYPES
            )

    print(f"\nFile: {RISK_CONTROLS_FILE_PATH}")
    print(f"Columns detected: {len(column_names)}")
    print(f"Data rows detected: {len(rows)}")

    return errors

def validate_uat_test_cases() -> list[str]:
    file_name = "UAT test cases CSV"

    errors, column_names, rows = validate_csv_structure(
        file_name=file_name,
        file_path=UAT_TEST_CASES_FILE_PATH,
        required_columns=UAT_REQUIRED_COLUMNS,
        expected_row_count=30,
        unique_columns=["test_case_id"],
    )

    structurally_valid = (
        column_names
        and UAT_REQUIRED_COLUMNS.issubset(
            set(column_names)
        )
    )

    detected_test_case_ids: set[str] = set()

    if structurally_valid:
        for row_number, row in enumerate(rows, start=2):
            test_case_id = row["test_case_id"].strip()
            detected_test_case_ids.add(test_case_id)

            if not re.fullmatch(
                pattern=r"TC-\d{3}",
                string=test_case_id,
            ):
                errors.append(
                    f"{file_name} row {row_number}: "
                    f"invalid test_case_id format "
                    f"'{test_case_id}'."
                )

            validate_allowed_value(
                errors=errors,
                file_name=file_name,
                row_number=row_number,
                column_name="business_priority",
                value=row["business_priority"].strip(),
                allowed_values=VALID_BUSINESS_PRIORITIES,
            )

            validate_allowed_value(
                errors=errors,
                file_name=file_name,
                row_number=row_number,
                column_name="execution_status",
                value=row["execution_status"].strip(),
                allowed_values=VALID_EXECUTION_STATUSES,
            )

            validate_allowed_value(
                errors=errors,
                file_name=file_name,
                row_number=row_number,
                column_name="retest_status",
                value=row["retest_status"].strip(),
                allowed_values=VALID_RETEST_STATUSES,
            )

            if (
                row["execution_status"].strip() == "Not Run"
                and row["actual_result"].strip()
                != "Not Executed"
            ):
                errors.append(
                    f"{file_name} row {row_number}: "
                    f"a Not Run test should have "
                    f"actual_result = Not Executed."
                )

            if (
                row["execution_status"].strip() == "Failed"
                and row["defect_id"].strip() == "N/A"
            ):
                errors.append(
                    f"{file_name} row {row_number}: "
                    f"a Failed test should reference "
                    f"a defect ID."
                )

        expected_test_case_ids = {
            f"TC-{test_number:03d}"
            for test_number in range(1, 31)
        }

        missing_test_case_ids = (
            expected_test_case_ids
            - detected_test_case_ids
        )

        unexpected_test_case_ids = (
            detected_test_case_ids
            - expected_test_case_ids
        )

        if missing_test_case_ids:
            errors.append(
                f"{file_name}: missing test case IDs: "
                f"{sorted(missing_test_case_ids)}"
            )

        if unexpected_test_case_ids:
            errors.append(
                f"{file_name}: unexpected test case IDs: "
                f"{sorted(unexpected_test_case_ids)}"
            )

    print(f"\nFile: {UAT_TEST_CASES_FILE_PATH}")
    print(f"Columns detected: {len(column_names)}")
    print(f"Data rows detected: {len(rows)}")

    return errors

def validate_traceability_matrix() -> list[str]:
    file_name = "Requirements traceability CSV"

    errors, column_names, rows = validate_csv_structure(
        file_name=file_name,
        file_path=TRACEABILITY_FILE_PATH,
        required_columns=TRACEABILITY_REQUIRED_COLUMNS,
        expected_row_count=23,
        unique_columns=["trace_id"]
    )

    structurally_valid = (
        column_names
        and TRACEABILITY_REQUIRED_COLUMNS.issubset(
            set(column_names)
        )
    )

    detected_trace_ids: set[str] = set()

    if structurally_valid:
        for row_number, row in enumerate(rows, start=2):
            trace_id = row["trace_id"].strip()
            business_objective = row[
                "business_objective"
            ].strip()

            detected_trace_ids.add(trace_id)

            if not re.fullmatch(
                pattern=r"RT-[0-9]{3}",
                string=trace_id,
            ):
                errors.append(
                    f"{file_name} row {row_number}: "
                    f"Invalid trace_id format '{trace_id}'."
                )

            if not re.fullmatch(
                pattern=r"BO-[0-9]{3}",
                string=business_objective,
            ):
                errors.append(
                    f"{file_name} row {row_number}: "
                    f"invalid business_objective format "
                    f"'{business_objective}'."
                )

            validate_allowed_value(
                errors=errors,
                file_name=file_name,
                row_number=row_number,
                column_name="coverage_status",
                value=row["coverage_status"].strip(),
                allowed_values=VALID_COVERAGE_STATUSES,
            )

        expected_trace_ids = {
            f"RT-{trace_number:03d}"
            for trace_number in range(1,24)
        }

        missing_trace_ids = (
            expected_trace_ids - detected_trace_ids
        )

        unexpected_trace_ids = (
            detected_trace_ids - expected_trace_ids
        )

        if missing_trace_ids:
            errors.append(
                f"{file_name}: missing trace IDs: "
                f"{sorted(missing_trace_ids)}"
            )

        if unexpected_trace_ids:
            errors.append(
                f"{file_name}: unexpected trace IDs: "
                f"{sorted(unexpected_trace_ids)}"
            )

    print(f"\nFile: {TRACEABILITY_FILE_PATH}")
    print(f"Columns detected: {len(column_names)}")
    print(f"Data rows detected: {len(rows)}")

    return errors





def main() -> int:
    validation_functions: list[
        Callable[[], list[str]]
    ] = [
        validate_risk_controls,
        validate_uat_test_cases,
        validate_traceability_matrix,
    ]

    all_errors: list[str] = []

    for validation_function in validation_functions:
        all_errors.extend(validation_function())

    if all_errors:
        print(
            f"\nValidation failed with "
            f"{len(all_errors)} error(s):"
        )

        for error in all_errors:
            print(f"- {error}")

        return 1

    print(
        "\nAll output example CSV files passed validation."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
            
                