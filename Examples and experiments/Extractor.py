import FreeSimpleGUI as Gui
import ExtractorBackend as Eb

Gui.theme("DarkPurple3")

Label1 = Gui.Text("Select Files to Extract:")
Input1 = Gui.InputText(tooltip="Where is the files you want to extract.", key="ZipFile")
ChooseButton1 = Gui.FilesBrowse("Choose")

Label2 = Gui.Text("Select Destination Folder:")
Input2 = Gui.InputText(tooltip="Where will you save the extract.", key="Folder")
ChooseButton2 = Gui.FolderBrowse("Choose")
CompressButton = Gui.Button("Extract", button_color="Red")

CompressDone = Gui.Text(key="DoneText", text_color="Red")

window = Gui.Window("File Extractor",
                    layout=[[Label1, Input1, ChooseButton1],
                            [Label2, Input2, ChooseButton2],
                            [CompressButton, CompressDone]])


while True:
    event, value = window.read()
    archive_file = value["ZipFile"]
    dest_file = value["Folder"]
    Eb.extract_archive(archive_file, dest_file)
    window["DoneText"].update(value="Compression Done. ")
window.close()
