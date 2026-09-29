library(shiny)
library(ggplot2)
library(forecast)

ui <- fluidPage(
  titlePanel("SC-13 Forecasting & Scenario Planning"),
  sidebarLayout(
    sidebarPanel(sliderInput("growth","Scenario growth",min=-0.2,max=0.3,value=0.05,step=0.01)),
    mainPanel(plotOutput("forecastPlot"),tableOutput("summary"))
  )
)

server <- function(input, output, session) {
  values <- ts(c(84,88,93,90,98,104,101,110), frequency=4)
  output$forecastPlot <- renderPlot({
    fit <- auto.arima(values)
    fc <- forecast(fit,h=4)
    autoplot(fc) + ggtitle("Forecast with prediction interval")
  })
  output$summary <- renderTable(data.frame(scenario_growth=input$growth,last_value=tail(values,1)))
}
shinyApp(ui,server)
