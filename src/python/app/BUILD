# python_sources()
python_source(
    name="main",
    source="main.py",
    # Pants cannot infer this dependency, so we explicitly add it.
    dependencies=[":examples"],
)

resource(
    name="examples",
    source="data/example/examples.py",
)
