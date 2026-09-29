# SC-13 · R Shiny Forecasting & Scenario Planning Application
#
# MAIN EXECUTION FILE
#
# This base-R entrypoint is intentionally dependency-light so the complete
# public execution path can be validated automatically. The Shiny application
# and forecast/fable implementation remain in the supporting folders.

load_series <- function() {
  c(84, 88, 93, 90, 98, 104, 101, 110, 116, 114, 121, 125)
}

linear_forecast <- function(series, horizon = 4) {
  x <- seq_along(series)
  fit <- lm(series ~ x)
  future_x <- length(series) + seq_len(horizon)
  as.numeric(predict(fit, newdata = data.frame(x = future_x)))
}

apply_scenario <- function(values, growth = 0.05) {
  values * (1 + growth)
}

main <- function() {
  series <- load_series()
  baseline <- linear_forecast(series, 4)
  scenario <- apply_scenario(baseline, 0.05)

  result <- data.frame(
    horizon = seq_along(baseline),
    baseline = round(baseline, 2),
    scenario = round(scenario, 2)
  )

  print(result)
  invisible(result)
}

if (sys.nframe() == 0) {
  main()
}
