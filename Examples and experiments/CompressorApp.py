import FreeSimpleGUI as sg
import zipcreatorfunc

Label1 = sg.Text("Select Files to Compress:")
Input1 = sg.InputText(tooltip="Where are the files you want to extract.", key="Files")
ChooseButton1 = sg.FilesBrowse("Choose")
Label2 = sg.Text("Select Destination Folder:")
Input2 = sg.InputText(tooltip="Where will you save the extract.", key="Folder")
ChooseButton2 = sg.FolderBrowse("Choose")
CompressButton = sg.Button("Compress")
CompressDone = sg.Text(key="DoneText", text_color="Red")

window = sg.Window("File Compressor",
                   layout=[[Label1, Input1, ChooseButton1],
                           [Label2, Input2, ChooseButton2],
                           [CompressButton, CompressDone]])

while True:
    event, value = window.read()
    print(event, value)
    Files = value["Files"].split(";")
    folder = value["Folder"]
    zipcreatorfunc.zip_maker(Files, folder)
    window["DoneText"].update(value="Compression Done. ")


window.close()

