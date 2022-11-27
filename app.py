from htmltools import HTML, div, TagList
from shiny import *
from pathlib import Path
from palmerpenguins import load_penguins
from sklearn import tree
import json

penguins = load_penguins()
penguins = penguins.dropna().reset_index(drop=True)
penguins["sex"].replace(["female", "male"], [0, 1], inplace=True)

X, y = (
    penguins[["bill_length_mm", "flipper_length_mm", "body_mass_g", "sex"]],
    penguins["species"],
)
penguin_model = tree.DecisionTreeClassifier()
penguin_model = penguin_model.fit(X.values, y)

penguins_data = (
    penguins[["bill_length_mm", "flipper_length_mm", "body_mass_g"]]
    .agg(["min", "max"])
    .round(0)
    .to_json()
)

app_ui = TagList(
    div(id="app"),
    ui.tags.script(src="build/index.js"),
    ui.tags.link(
        rel="stylesheet", href="https://unpkg.com/carbon-components-svelte/css/g90.css"
    ),
    ui.tags.link(rel="stylesheet", href="build/index.css"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.Effect
    async def _():
        new_data = json.loads(input.penguin_values())["inputs"]
        prediction = penguin_model.predict([new_data])
        await session.send_custom_message("penguin_prediction", prediction[0])


app_dir = Path(__file__).parent.resolve()
app = App(app_ui, server, static_assets=str(app_dir / "dist/www"))

# https://github.com/rstudio/py-shiny/blob/47d298e11ea5ece81f55bb1b3e7ed1e4742b5c41/shiny/examples/www_dir/app.py
