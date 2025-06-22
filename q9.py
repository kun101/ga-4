import tabula
import pandas as pd

# Initialize total sum variable
total_maths_marks = 0

# Pages to process (groups 71 to 100)
pages_to_process = list(range(71, 101))

for page in pages_to_process:
    # Read the table from the specific page
    tables = tabula.read_pdf('tables.pdf', pages=page, multiple_tables=False)
    
    if not tables:
        # No table on this page, skip
        continue
    
    df = tables[0]
    
    # If first row is header, set it as column names
    df.columns = df.iloc[0]
    df = df[1:]  # drop old header row
    
    # Convert Maths column to numeric
    df['Maths'] = pd.to_numeric(df['Maths'], errors='coerce')
    
    # Filter students who scored >= 60 in Maths
    filtered_df = df[df['Maths'] >= 60]
    
    # Sum Maths marks for this page and add to total
    total_maths_marks += filtered_df['Maths'].sum()

print(f"Total Maths marks of students with >=60 in Maths in groups 71-100: {total_maths_marks}")
