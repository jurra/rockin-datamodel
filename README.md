# Pydantic data model for Well and Core extraction
We use this data model to describe relationships between Wells and Cores. The pyndantic model is the specification of the data model. This is something we use mostly at the moment as a contract to define relationships between entities without having to rely on a specific implementation, webapp or database.

The data model can also be used to generate schemas.
Furthermore you can explore the datamodel using python.

## Try out the model
Run the python example in interactive mode and explore the model. You will inmediately see how some fields are required and start changing the creation of objects so that they are valid.

```bash
python -i example.py
```
