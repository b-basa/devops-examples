import requests
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Div
from bokeh.plotting import curdoc

# Backend API URL
# TODO: Maybe also send this through nginx
API_URL = "http://backend:5000/api/files"


def fetch_file_names():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        file_names = [file.get("name") for file in data]
        return file_names
    except Exception as e:
        print(f"Error fetching files: {e}")
        return ["Error: Unable to fetch files"]


# Initial Data Fetch
file_names = fetch_file_names()

# Convert to ColumnDataSource for Bokeh
source = ColumnDataSource(data={"file_names": file_names})

# Create a simple Div to display file names
file_list = Div(
    text="<h2>Files:</h2>"
    + "".join(f"<p>{name}</p>" for name in source.data["file_names"])
)


# Function to update file list dynamically
def update():
    new_file_names = fetch_file_names()
    source.data = {"file_names": new_file_names}
    file_list.text = "<h2>Files:</h2>" + "".join(
        f"<p>{name}</p>" for name in new_file_names
    )


# Add periodic callback to update the file list every 5 seconds
curdoc().add_periodic_callback(update, 5000)

# Layout
curdoc().add_root(column(file_list))
curdoc().title = "File Viewer"
