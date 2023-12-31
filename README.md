# Projekt01: Streamlit run!
Ich möchte KI-Manager*innen einfache Wege aufzeigen, wie sie Daten visualisieren können.
Streamlit ist eine Bibliothek und ein Framework für Python, mit dem Datenwissenschaftler interaktive Web-Apps mit grafischer Benutzeroberfläche und anschaulicher Datenvisualisierung erstellen können.
________________________________________

## Folgende Schritte kannst Du umsetzen, um eine einfache Datenvisualisierung umzusetzen.

**_01. Entwicklungsumgebung nutzen: VS Code Studio_**

**_02. Python als Extension installieren_**

**_03. Ordner im Editor erstellen: "Übungen"_**

**_04. Python Datei im Ordner erstellen: "deineApp.py"_**

**_05. Codezeile eingeben_**

```
import streamlit as st
import pandas as pd

# Lade die CSV-Datei
csv_file = st.file_uploader("C:/dein Pfad/deine.csv", type=["csv"])

if csv_file is not None:
    # Konvertiere die Datei in ein Pandas DataFrame
    csv_data = pd.read_csv(csv_file)

    # Zeige die ersten 10 Zeilen des DataFrames an
    st.write(csv_data.head(10))

```

_**06. Run clicken**_

``
Terminal erscheint der folgende Output:
`  Warning: to view this Streamlit app on a browser, run it with the following
  command:
``

**_07. Code im Terminal eingeben_**

`streamlit run deineApp.py`

**_08. Browserfenster öffnet sich_**

**_09. Datei hochladen_**

z. B.  https://www.kaggle.com/datasets/thedevastator/national-universities-rankings-explore-quality-t

**10. Daten werden repräsentiert**
__________________________________________________
## Mein Ergebnis:
![Screenshot 2023-11-16 115550](https://github.com/digitalerbildungspartner/projekt01_streamlit/assets/146565610/5fdb24e6-607e-4dbe-9d29-5985b6247177)

___________________________________________________

Weitere Infos und Demos findetst du unter:

https://streamlit.io/
