def merge_text_files(input_files, output_file):
    try:
        with open(output_file, 'w') as out_file:
            for input_file in input_files:
                with open(input_file, 'r') as in_file:
                    # Read the content of the input file and write it to the output file
                    content = in_file.read()
                    out_file.write(content)

        print(f'Merged files successfully. Merged content saved to {output_file}')
    except Exception as e:
        print(f'Error occurred: {e}')

# List of input text files to merge
input_files = ['combinations_length_1.txt','combinations_length_2.txt','combinations_length_3.txt','combinations_length_4.txt','combinations_length_5.txt','combinations_length_6.txt','combinations_length_7.txt','combinations_length_8.txt','combinations_length_9.txt','combinations_length_10.txt','combinations_length_11.txt']  # Add your file names here

# Output file where the merged content will be saved
output_file = 'merged_output.txt'

# Call the function to merge the files
merge_text_files(input_files, output_file)
