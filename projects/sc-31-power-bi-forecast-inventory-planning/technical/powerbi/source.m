let
    Source = Excel.CurrentWorkbook(){[Name="ForecastInput"]}[Content],
    Typed = Table.TransformColumnTypes(
        Source,
        {{"Date", type date}, {"Actual", type number}, {"Forecast", type number}, {"StockUnits", Int64.Type}}
    )
in
    Typed
