import FreeSimpleGUI as Gui
import ConverterBackend

FeetLabel = Gui.Text("Enter Feet:")
InchesLabel = Gui.Text("Enter Inches")
FeetBox = Gui.Input(tooltip="How many feets are you?", key="Feet")
InchesBox = Gui.Input(tooltip="How many inches are you?", key="Inches")
ConvertButton = Gui.Button("Convert")
MeterText = Gui.Text("", key="CompletionText", text_color="blue")
ExitButton = Gui.Button("Exit")

window = Gui.Window("CONVERTOR", layout=[[FeetLabel, FeetBox],
                                         [InchesLabel, InchesBox],
                                         [ConvertButton, ExitButton, MeterText]])
while True:
    event, value = window.read()
    match event:
        case "Convert":
            try:
                feets = float(value["Feet"])
                inches = float(value["Inches"])
                meter = ConverterBackend.conv(feets, inches)
                window["CompletionText"].update(value=f"{feets}feets and {inches}inches is {meter}m")
            except ValueError:
                Gui.popup("Enter feets and inches!", font=("Cooper Black", 16))
        case "Exit":
            break
        case Gui.WINDOW_CLOSED:
            break

window.close()
