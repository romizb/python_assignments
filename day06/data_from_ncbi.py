import argparse
import csv
import os
from datetime import datetime
from Bio import Entrez


#How to run the script:
#Use the command line to execute the script with your desired arguments. Examples:
#    python data_from_ncbi.py --database gene --term aqp1a.1 --number 1 (result number)
#    python data_from_ncbi.py --term cauliflower

# To check the output:
#        Downloaded files will be saved in the current working directory (c/users/rucha/work/python_course/day06)
#        A log file named search_log.csv will be updated with the search details.



# Set up  email address for NCBI Entrez
Entrez.email = "ruchamab123@gmail.com"

# Define the function to search and download data
def download_ncbi_data(database, term, number):
    try:
        # Search the database
        handle = Entrez.esearch(db=database, term=term, retmax=number)
        search_results = Entrez.read(handle)
        handle.close()
        
        ids = search_results["IdList"]
        total_found = search_results["Count"]

        # Download and save data for each ID
        filenames = []
        for ncbi_id in ids:
            handle = Entrez.efetch(db=database, id=ncbi_id, rettype="fasta", retmode="text")
            data = handle.read()
            handle.close()
            
            filename = f"{database}_{ncbi_id}.fasta"
            with open(filename, "w") as f:
                f.write(data)
            filenames.append(filename)

        return filenames, total_found
    except Exception as e:
        print(f"Error: {e}")
        return [], 0

# Append search details to the log CSV file
def log_search_details(csv_filename, date, database, term, max_number, total_found):
    file_exists = os.path.isfile(csv_filename)
    with open(csv_filename, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["date", "database", "term", "max", "total"])
        writer.writerow([date, database, term, max_number, total_found])

# Main function to parse arguments and execute the tool
def main():
    parser = argparse.ArgumentParser(description="Download data from NCBI databases.")
    parser.add_argument("--database", default="nucleotide", help="NCBI database to search (default: nucleotide)")
    parser.add_argument("--term", required=True, help="Search term")
    parser.add_argument("--number", type=int, default=10, help="Number of items to download (default: 10)")

    args = parser.parse_args()

    # Run the search and download process
    print(f"Searching {args.database} for '{args.term}'...")
    filenames, total_found = download_ncbi_data(args.database, args.term, args.number)

    if filenames:
        print("Downloaded files:")
        for filename in filenames:
            print(f"  {filename}")
    else:
        print("No files downloaded.")

    # Log the search details
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_search_details("search_log.csv", current_date, args.database, args.term, args.number, total_found)

    print("Search details logged to search_log.csv")

if __name__ == "__main__":
    main()
