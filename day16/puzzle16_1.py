from day16.fft import FFT

sample1 = FFT(file_name='sample1.txt')
print("Sample 1 answer is {}".format(sample1.cleanup_signal(phases=4)))

sample2 = FFT(file_name='sample2.txt')
print("Sample 2 answer is {}".format(sample2.cleanup_signal()))

sample3 = FFT(file_name='sample3.txt')
print("Sample 3 answer is {}".format(sample3.cleanup_signal()))

sample4 = FFT(file_name='sample4.txt')
print("Sample 4 answer is {}".format(sample4.cleanup_signal()))

question = FFT(file_name='input.txt')
print("Final answer is {}".format(question.cleanup_signal()))

