# Legal Document Organizer
# Organizes documents into folders based on filename keywords

import os
import shutil

# Change this path to your documents folder
SOURCE_FOLDER = "documents_to_organize"
DESTINATION_FOLDER = "Legal_Documents"

# Document categories with keywords
CATEGORIES = {
    "Aadhaar": ["aadhaar", "aadhar", "uid"],
    "PAN": ["pan"],
    "Passport": ["passport"],
    "Education": ["marksheet", "certificate", "degree", "school", "college"],
    "Bank": ["bank", "statement", "passbook", "account"],
    "Property": ["property", "land", "agreement", "sale"],
    "Insurance": ["insurance", "policy"],
}

# Create main destination folder
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

# Create category folders
for category in CATEGORIES:
    os.makedirs(os.path.join(DESTINATION_FOLDER, category), exist_ok=True)

# Other folder
os.makedirs(os.path.join(DESTINATION_FOLDER, "Other"), exist_ok=True)

def organize_documents():
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            file_lower = file.lower()
            moved = False

            for category, keywords in CATEGORIES.items():
                if any(keyword in file_lower for keyword in keywords):
                    shutil.move(
                        file_path,
                        os.path.join(DESTINATION_FOLDER, category, file)
                    )
                    moved = True
                    break

            if not moved:
                shutil.move(
                    file_path,
                    os.path.join(DESTINATION_FOLDER, "Other", file)
                )

    print("Documents organized successfully.")

if __name__ == "__main__":
    organize_documents()
