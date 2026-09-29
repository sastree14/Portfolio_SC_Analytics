test_that("scenario series is available", {
  x <- c(84,88,93,90,98,104,101,110)
  expect_equal(length(x), 8)
  expect_true(mean(x) > 0)
})
