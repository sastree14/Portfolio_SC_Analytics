let
    Source = Csv.Document(File.Contents("data/fact_sales.csv"),[Delimiter=",",Encoding=65001,QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source,[PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers,{{"Date", type date},{"Revenue", type number},{"Cost", type number}})
in
    Types
