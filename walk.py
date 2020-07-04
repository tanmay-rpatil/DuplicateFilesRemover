import os, csv

current_dir = (os.path.abspath(__file__))



 


primary = input("Enter the absolute path of directory from which files should not be deleted")
secondary = input("Enter the absolute path of directory from which files are to be deleted")



print(f"Prim_Path={primary}, Sec_Path={secondary}")

#csv file with list of all files from primary dir
with open('primary_file_list.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["File_Name","Path", "Size"])
	#print("These are the files form the original directory")
	for root,dirs,files in os.walk(primary):
		#print("current dir is-", root)
		for item in files:
			f_path = os.path.join(root, item)	
			#print(f"File={item}, Path={f_path}, Size={os.path.getsize(f_path)} ")
			writer.writerow([item, f_path, os.path.getsize(f_path)])

#csv file with list of all files from primary dir
with open('secondary_file_list.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["File_Name","Path", "Size"])
	#print("These are the files form the secondary directory-to be deleted")
	for root,dirs,files in os.walk(secondary):
		#print("current dir is-", root)
		for item in files:
			f_path = os.path.join(root, item)
			#print(f"File={item}, Path={f_path}, Size={os.path.getsize(f_path)} ")
			writer.writerow([item, f_path, os.path.getsize(f_path)])


#finding duplicates
found_number=0
found_size=0

with open('deletion.csv', 'w', newline='') as file:
	writer = csv.writer(file) 
	writer.writerow(["File_Name","Sec_Path","Prim_Path", "Size"])
	with open('secondary_file_list.csv') as sec_csv:
		sec_csv_reader=csv.DictReader(sec_csv)
		sec_csv_line=0
		for sec_row in sec_csv_reader:

			#print("Checking the file-", sec_row)

			with open('primary_file_list.csv') as prim_csv:

				prim_csv_reader=csv.DictReader(prim_csv)
				prim_csv_line=0

				for prim_row in prim_csv_reader:

					if ( (sec_row["File_Name"]==prim_row["File_Name"]) and (sec_row["Size"]==prim_row["Size"]) ):
						writer.writerow([sec_row["File_Name"], sec_row["Path"],prim_row["Path"], sec_row["Size"]])
						print("Match found", sec_row)
						found_size+=int(sec_row["Size"])
						found_number+=1
						break
					
					prim_csv_line+=1
			sec_csv_line+=1


if found_number !=0:
	display = input(f"{found_number} duplicates found, amounting to {found_size}bytes. Do you want a list of them? (y/n)")

	if display == 'y':
		with open('deletion.csv') as del_csv:
			del_csv_reader=csv.DictReader(del_csv)
			del_csv_line=0
			for del_row in del_csv_reader:
				print(f"{del_row['File_Name']}, ({del_row['Size']} bytes)")



	answer = input(f"are you shure you want to remove duplicates from {secondary}? (y/n) ")
	if answer == "y":
		with open('deletion.csv') as del_csv:
			del_csv_reader = csv.DictReader(del_csv)
			line_count = 1
			del_size =0
			for del_line in del_csv_reader:
				path = del_line["Sec_Path"]
				temp_size = int(del_line["Size"])
				del_size+=temp_size
				os.remove(path)
				line_count+=1

		print(f"{line_count} Files removed, freeing up {del_size} bytes of space!")
else:
	print("No duplicates found amoung the two dirs")
