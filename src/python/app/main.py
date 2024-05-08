import importlib

from google.protobuf.json_format import MessageToJson

# Uncomment this to explicitly import the data file
# and the app will work!
# import app.data.example.examples


if __name__ == "__main__":
    libs = ["examples"]
    for name in libs:
        lib = importlib.import_module(f"app.data.example.{name}")

        data = getattr(lib, name)
        for item in data:
            print(MessageToJson(item))
