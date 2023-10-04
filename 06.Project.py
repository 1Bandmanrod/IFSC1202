#!/usr/bin/env python
# coding: utf-8

# In[3]:


def merge_and_count_records(file_Input, file_Merge, file_Output):
    input_record_count = 0
    merge_record_count = 0
    output_record_count = 0

    try:
        # Open file_Output for writing
        with open(file_Output, 'w') as output_file:
            # Open and read file_Input
            with open(file_Input, 'r') as input_file:
                is_inserted = False
                for line in input_file:
                    input_record_count += 1
                    if line.strip() == "**Insert Merge File Here**":
                        # Open file_Merge and copy its contents
                        with open(file_Merge, 'r') as merge_file:
                            for merge_line in merge_file:
                                merge_record_count += 1
                                output_file.write(merge_line)
                                output_file.write('\n')  # Add a newline character
                        is_inserted = True
                    else:
                        # Copy line from file_Input to file_Output
                        output_file.write(line)

                if not is_inserted:
                    print("**Insert Merge File Here** not found in file_Input. Merging complete.")

            # Count remaining input records (excluding the marker line)
            input_record_count -= 1
            output_record_count = merge_record_count + input_record_count

        # Print the number of records
        print(f"{input_record_count} input file records")
        print(f"{merge_record_count} merge file records")
        print(f"{output_record_count} output file records")

    except FileNotFoundError:
        print("One or more input files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the file names
file_Input = '06.Project Input File.txt'
file_Merge = '06.Project Merge File.txt'
file_Output = '06.Project Output File.txt'

# Merge files and count records
merge_and_count_records(file_Input, file_Merge, file_Output)


# In[ ]:




