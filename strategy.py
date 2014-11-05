__author__ = 'Michyo'

import algorithm

text = "Slippage 1 && test for multiplier"

algorithm.Bollinger_day_duration_slippage1(text, "test_for_multiplier_1.log", 20, 1.2)
algorithm.Bollinger_day_duration_slippage1(text, "test_for_multiplier_2.log", 20, 1.0)
algorithm.Bollinger_day_duration_slippage1(text, "test_for_multiplier_3.log", 20, 0.8)
algorithm.Bollinger_day_duration_slippage1(text, "test_for_multiplier_4.log", 20, 0.6)
algorithm.Bollinger_day_duration_slippage1(text, "test_for_multiplier_5.log", 20, 0.4)
algorithm.Bollinger_day_duration_slippage1(text, "test_for_multiplier_6.log", 20, 0.2)



