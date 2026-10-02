let
    Source = Excel.CurrentWorkbook(){[Name="OrderEvents"]}[Content],
    Typed = Table.TransformColumnTypes(
        Source,
        {{"OrderDate", type date}, {"PromisedDate", type date}, {"DeliveryDate", type date}, {"OrderId", type text}}
    )
in
    Typed
