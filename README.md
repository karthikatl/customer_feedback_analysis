Task Overview
Developed a robust data cleaning pipeline to process customer feedback data, ensuring:

Consistent handling of missing/null values

Proper datetime parsing and standardization

Text normalization for analysis-ready feedback

Comprehensive error handling and edge-case management

Tools & Technologies Used
Python

Core language for scripting

Pandas

Data manipulation (e.g., dropna, fillna, pd.to_datetime)

VS Code

IDE for development, debugging, and version control

Key Fixes Implemented
Resolved CSV file path errors using absolute paths

Eliminated datetime parsing warnings via explicit format strings (format="%d/%m/%Y %H:%M")

Addressed dtype warnings with column type casting (e.g., df["feedback"].astype(str))

Streamlined testing with dynamic path resolution in test files

Outcome
Cleaned data saved to data/interim/cleaned_data.csv