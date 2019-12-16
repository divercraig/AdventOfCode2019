from day16.fft import FFT

sample5 = FFT(file_name='sample5.txt')
print("Sample 5 answer is {}".format(sample5.cleanup_full_signal()))

sample6 = FFT(file_name='sample6.txt')
print("Sample 6 answer is {}".format(sample6.cleanup_full_signal()))

sample7 = FFT(file_name='sample7.txt')
print("Sample 7 answer is {}".format(sample7.cleanup_full_signal()))

question = FFT(file_name='input.txt')
print("Final answer is {}".format(question.cleanup_full_signal()))

