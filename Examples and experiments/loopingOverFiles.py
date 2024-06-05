waiting_lists = ["sen", "ben", "john"]
file_names = ["doc.txt", "report.txt", "presentation.txt"]

for waiting_list, file_name in zip(waiting_lists, file_names):
    file = open(f"venv/{file_name}","w")
    file.write(waiting_list)