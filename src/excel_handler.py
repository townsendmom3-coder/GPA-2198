import pandas as pd


def read_excel_data(file_path):
    """
    Read molecular weight and response factor data from an Excel file.
    """
    data = pd.read_excel(file_path)
    return data


def write_results_to_excel(data, output_path):
    """
    Write results back to Excel with formatting.
    """
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        data.to_excel(writer, sheet_name='Results', index=False)
        workbook = writer.book
        worksheet = writer.sheets['Results']

        # Apply formatting
        format_bold = workbook.add_format({'bold': True})
        worksheet.set_row(0, None, format_bold)

        # Set column width
        worksheet.set_column('A:A', 20)  # Example for first column
        worksheet.set_column('B:B', 15)  # Example for second column

        # Add more formatting as needed

