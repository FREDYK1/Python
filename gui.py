import mainFunctions
import FreeSimpleGUI

Label = FreeSimpleGUI.Text("Enter Your Todo:")
TextBox = FreeSimpleGUI.InputText(tooltip="Enter Todo Here")
add_button = FreeSimpleGUI.Button("ADD")
window = FreeSimpleGUI.Window("My Todos App", layout=[[Label, TextBox, add_button]])
window.read()
window.close()

