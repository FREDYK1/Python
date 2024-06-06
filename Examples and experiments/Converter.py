import FreeSimpleGUI as Gui

FeetLabel = Gui.Text("Enter Feet:")
InchesLabel = Gui.Text("Enter Inches")
FeetBox = Gui.Input()
InchesBox = Gui.Input()
ConvertButton = Gui.Button("Convert")

window = Gui.Window("CONVERTOR", layout=[[FeetLabel, FeetBox], [InchesLabel, InchesBox], [ConvertButton]])
window.read()
window.close()
