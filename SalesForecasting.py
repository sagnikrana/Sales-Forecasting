
# Checking the graph for seasonality:




# # extracting the results:
#
# # Create forecast object
# forecast_object = results.get_forecast(steps=136)
#
# # Extract prediction mean
# mean = forecast_object.predicted_mean
#
# # Extract the confidence intervals
# conf_int = forecast_object.conf_int()
#
# # Extract the forecast dates
# dates = mean.index
#
# plt.figure()
#
# # Plot past CO2 levels
# plt.plot(co2.index, co2, label='past')
#
# # Plot the prediction means as line
# plt.plot(dates, mean, label='predicted')
#
# # Shade between the confidence intervals
# plt.fill_between(dates, conf_int.iloc[:,0], conf_int.iloc[:,1], alpha=0.2)
#
# # Plot legend and show figure
# plt.legend()
# plt.show()
#
#
# # PLotting it all over
#
# # Print last predicted mean
# print(mean.iloc[-1])
#
# # Print last confidence interval
# print(conf_int.iloc[-1])