import FreeSimpleGUI as sg

Label1 = sg.Text("Select Files to Compress:")
Input1 = sg.InputText("Where are the files you want to extract.")
ChooseButton1 = sg.FileBrowse("Choose")
Label2 = sg.Text("Select Destination Folder:")
Input2 = sg.InputText("Where will you save the extract.")
ChooseButton2 = sg.FolderBrowse("Choose")
CompressButton = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[Label1, Input1, ChooseButton1], [Label2, Input2, ChooseButton2], [CompressButton]])
window.read()
window.close()