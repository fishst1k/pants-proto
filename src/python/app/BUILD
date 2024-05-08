# python_sources()
python_source(
    name="main",
    source="main.py",
    # Pants cannot infer this dependency, so we explicitly add it.
    # , ":member_pb2", ":team_pb2"],
    dependencies=[":examples"],
)

resource(
    name="examples",
    source="data/example/examples.py",
)
