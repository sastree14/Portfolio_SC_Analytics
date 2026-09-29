# SC-13 · R Shiny Forecasting & Scenario Planning Application
#
# MAIN EXECUTION FILE
#
# This script is the clearest end-to-end public execution path:
# data -> statistical forecast -> scenario adjustment -> result.

suppressPackageStartupMessages({
  library(forecast)
  library(ggplot2)
})

load_series <- function() {
  ts(c(84, 88, 93, 90, 98, 104, 101, 110, 116, 114, 121, 125), frequency = 4)
}

fit_forecast <- function(series, horizon = 4) {
  model <- auto.arima(series)
  forecast(model, h = horizon)
}

apply_scenario <- function(fc, growth = 0.05) {
  values <- as.numeric(fc$mean)
  values * (1 + growth)
}

main <- function() {
  series <- load_series()
  fc <- fit_forecast(series, 4)
  scenario <- apply_scenario(fc, 0.05)

  result <- data.frame(
    horizon = seq_along(scenario),
    baseline = round(as.numeric(fc$mean), 2),
    scenario = round(scenario, 2)
  )

  print(result)
  invisible(result)
}

if (sys.nframe() == 0) {
  main()
}
